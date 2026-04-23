## Create

`$ ant beta:messages create`

**post** `/v1/messages`

Send a structured list of input messages with text and/or image content, and the model will generate the next message in the conversation.

The Messages API can be used for either single queries or stateless multi-turn conversations.

Learn more about the Messages API in our [user guide](https://docs.claude.com/en/docs/initial-setup)

### Parameters

- `--max-tokens: number`

  Body param: The maximum number of tokens to generate before stopping.

  Note that our models may stop _before_ reaching this maximum. This parameter only specifies the absolute maximum number of tokens to generate.

  Different models have different maximum values for this parameter.  See [models](https://docs.claude.com/en/docs/models-overview) for details.

- `--message: array of BetaMessageParam`

  Body param: Input messages.

  Our models are trained to operate on alternating `user` and `assistant` conversational turns. When creating a new `Message`, you specify the prior conversational turns with the `messages` parameter, and the model then generates the next `Message` in the conversation. Consecutive `user` or `assistant` turns in your request will be combined into a single turn.

  Each input message must be an object with a `role` and `content`. You can specify a single `user`-role message, or you can include multiple `user` and `assistant` messages.

  If the final message uses the `assistant` role, the response content will continue immediately from the content in that message. This can be used to constrain part of the model's response.

  Example with a single `user` message:

  ```json
  [{"role": "user", "content": "Hello, Claude"}]
  ```

  Example with multiple conversational turns:

  ```json
  [
    {"role": "user", "content": "Hello there."},
    {"role": "assistant", "content": "Hi, I'm Claude. How can I help you?"},
    {"role": "user", "content": "Can you explain LLMs in plain English?"},
  ]
  ```

  Example with a partially-filled response from Claude:

  ```json
  [
    {"role": "user", "content": "What's the Greek name for Sun? (A) Sol (B) Helios (C) Sun"},
    {"role": "assistant", "content": "The best answer is ("},
  ]
  ```

  Each input message `content` may be either a single `string` or an array of content blocks, where each block has a specific `type`. Using a `string` for `content` is shorthand for an array of one content block of type `"text"`. The following input messages are equivalent:

  ```json
  {"role": "user", "content": "Hello, Claude"}
  ```

  ```json
  {"role": "user", "content": [{"type": "text", "text": "Hello, Claude"}]}
  ```

  See [input examples](https://docs.claude.com/en/api/messages-examples).

  Note that if you want to include a [system prompt](https://docs.claude.com/en/docs/system-prompts), you can use the top-level `system` parameter — there is no `"system"` role for input messages in the Messages API.

  There is a limit of 100,000 messages in a single request.

- `--model: "claude-opus-4-7" or "claude-mythos-preview" or "claude-opus-4-6" or 14 more or string`

  Body param: The model that will complete your prompt.

  See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

- `--cache-control: optional object { type, ttl }`

  Body param: Top-level cache control automatically applies a cache_control marker to the last cacheable block in the request.

- `--container: optional BetaContainerParams or string`

  Body param: Container identifier for reuse across requests.

- `--context-management: optional object { edits }`

  Body param: Context management configuration.

  This allows you to control how Claude manages context across multiple requests, such as whether to clear function results or not.

- `--inference-geo: optional string`

  Body param: Specifies the geographic region for inference processing. If not specified, the workspace's `default_inference_geo` is used.

- `--mcp-server: optional array of BetaRequestMCPServerURLDefinition`

  Body param: MCP servers to be utilized in this request

- `--metadata: optional object { user_id }`

  Body param: An object describing metadata about the request.

- `--output-config: optional object { effort, format }`

  Body param: Configuration options for the model's output, such as the output format.

- `--output-format: optional object { schema, type }`

  Body param: Deprecated: Use `output_config.format` instead. See [structured outputs](https://platform.claude.com/docs/en/build-with-claude/structured-outputs)

  A schema to specify Claude's output format in responses. This parameter will be removed in a future release.

- `--service-tier: optional "auto" or "standard_only"`

  Body param: Determines whether to use priority capacity (if available) or standard capacity for this request.

  Anthropic offers different levels of service for your API requests. See [service-tiers](https://docs.claude.com/en/api/service-tiers) for details.

- `--speed: optional "standard" or "fast"`

  Body param: The inference speed mode for this request. `"fast"` enables high output-tokens-per-second inference.

- `--stop-sequence: optional array of string`

  Body param: Custom text sequences that will cause the model to stop generating.

  Our models will normally stop when they have naturally completed their turn, which will result in a response `stop_reason` of `"end_turn"`.

  If you want the model to stop generating when it encounters custom strings of text, you can use the `stop_sequences` parameter. If the model encounters one of the custom sequences, the response `stop_reason` value will be `"stop_sequence"` and the response `stop_sequence` value will contain the matched stop sequence.

- `--system: optional string or array of BetaTextBlockParam`

  Body param: System prompt.

  A system prompt is a way of providing context and instructions to Claude, such as specifying a particular goal or role. See our [guide to system prompts](https://docs.claude.com/en/docs/system-prompts).

- `--temperature: optional number`

  Body param: Amount of randomness injected into the response.

  Defaults to `1.0`. Ranges from `0.0` to `1.0`. Use `temperature` closer to `0.0` for analytical / multiple choice, and closer to `1.0` for creative and generative tasks.

  Note that even with `temperature` of `0.0`, the results will not be fully deterministic.

- `--thinking: optional BetaThinkingConfigEnabled or BetaThinkingConfigDisabled or BetaThinkingConfigAdaptive`

  Body param: Configuration for enabling Claude's extended thinking.

  When enabled, responses include `thinking` content blocks showing Claude's thinking process before the final answer. Requires a minimum budget of 1,024 tokens and counts towards your `max_tokens` limit.

  See [extended thinking](https://docs.claude.com/en/docs/build-with-claude/extended-thinking) for details.

- `--tool-choice: optional BetaToolChoiceAuto or BetaToolChoiceAny or BetaToolChoiceTool or BetaToolChoiceNone`

  Body param: How the model should use the provided tools. The model can use a specific tool, any available tool, decide by itself, or not use tools at all.

- `--tool: optional array of BetaToolUnion`

  Body param: Definitions of tools that the model may use.

  If you include `tools` in your API request, the model may return `tool_use` content blocks that represent the model's use of those tools. You can then run those tools using the tool input generated by the model and then optionally return results back to the model using `tool_result` content blocks.

  There are two types of tools: **client tools** and **server tools**. The behavior described below applies to client tools. For [server tools](https://docs.claude.com/en/docs/agents-and-tools/tool-use/overview#server-tools), see their individual documentation as each has its own behavior (e.g., the [web search tool](https://docs.claude.com/en/docs/agents-and-tools/tool-use/web-search-tool)).

  Each tool definition includes:

  * `name`: Name of the tool.
  * `description`: Optional, but strongly-recommended description of the tool.
  * `input_schema`: [JSON schema](https://json-schema.org/draft/2020-12) for the tool `input` shape that the model will produce in `tool_use` output content blocks.

  For example, if you defined `tools` as:

  ```json
  [
    {
      "name": "get_stock_price",
      "description": "Get the current stock price for a given ticker symbol.",
      "input_schema": {
        "type": "object",
        "properties": {
          "ticker": {
            "type": "string",
            "description": "The stock ticker symbol, e.g. AAPL for Apple Inc."
          }
        },
        "required": ["ticker"]
      }
    }
  ]
  ```

  And then asked the model "What's the S&P 500 at today?", the model might produce `tool_use` content blocks in the response like this:

  ```json
  [
    {
      "type": "tool_use",
      "id": "toolu_01D7FLrfh4GYq7yT1ULFeyMV",
      "name": "get_stock_price",
      "input": { "ticker": "^GSPC" }
    }
  ]
  ```

  You might then run your `get_stock_price` tool with `{"ticker": "^GSPC"}` as an input, and return the following back to the model in a subsequent `user` message:

  ```json
  [
    {
      "type": "tool_result",
      "tool_use_id": "toolu_01D7FLrfh4GYq7yT1ULFeyMV",
      "content": "259.75 USD"
    }
  ]
  ```

  Tools can be used for workflows that include running client-side tools and functions, or more generally whenever you want the model to produce a particular JSON structure of output.

  See our [guide](https://docs.claude.com/en/docs/tool-use) for more details.

- `--top-k: optional number`

  Body param: Only sample from the top K options for each subsequent token.

  Used to remove "long tail" low probability responses. [Learn more technical details here](https://towardsdatascience.com/how-to-sample-from-language-models-682bceb97277).

  Recommended for advanced use cases only.

- `--top-p: optional number`

  Body param: Use nucleus sampling.

  In nucleus sampling, we compute the cumulative distribution over all the options for each subsequent token in decreasing probability order and cut it off once it reaches a particular probability specified by `top_p`.

  Recommended for advanced use cases only.

- `--beta: optional array of AnthropicBeta`

  Header param: Optional header to specify the beta version(s) you want to use.

### Returns

- `beta_message: object { id, container, content, 8 more }`

  - `id: string`

    Unique object identifier.

    The format and length of IDs may change over time.

  - `container: object { id, expires_at, skills }`

    Information about the container used in the request (for the code execution tool)

    - `id: string`

      Identifier for the container used in this request

    - `expires_at: string`

      The time at which the container will expire.

    - `skills: array of BetaSkill`

      Skills loaded in the container

      - `skill_id: string`

        Skill ID

      - `type: "anthropic" or "custom"`

        Type of skill - either 'anthropic' (built-in) or 'custom' (user-defined)

        - `"anthropic"`

        - `"custom"`

      - `version: string`

        Skill version or 'latest' for most recent version

  - `content: array of BetaContentBlock`

    Content generated by the model.

    This is an array of content blocks, each of which has a `type` that determines its shape.

    Example:

    ```json
    [{"type": "text", "text": "Hi, I'm Claude."}]
    ```

    If the request input `messages` ended with an `assistant` turn, then the response `content` will continue directly from that last turn. You can use this to constrain the model's output.

    For example, if the input `messages` were:

    ```json
    [
      {"role": "user", "content": "What's the Greek name for Sun? (A) Sol (B) Helios (C) Sun"},
      {"role": "assistant", "content": "The best answer is ("}
    ]
    ```

    Then the response `content` might be:

    ```json
    [{"type": "text", "text": "B)"}]
    ```

    - `beta_text_block: object { citations, text, type }`

      - `citations: array of BetaTextCitation`

        Citations supporting the text block.

        The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

        - `beta_citation_char_location: object { cited_text, document_index, document_title, 4 more }`

          - `cited_text: string`

          - `document_index: number`

          - `document_title: string`

          - `end_char_index: number`

          - `file_id: string`

          - `start_char_index: number`

          - `type: "char_location"`

        - `beta_citation_page_location: object { cited_text, document_index, document_title, 4 more }`

          - `cited_text: string`

          - `document_index: number`

          - `document_title: string`

          - `end_page_number: number`

          - `file_id: string`

          - `start_page_number: number`

          - `type: "page_location"`

        - `beta_citation_content_block_location: object { cited_text, document_index, document_title, 4 more }`

          - `cited_text: string`

          - `document_index: number`

          - `document_title: string`

          - `end_block_index: number`

          - `file_id: string`

          - `start_block_index: number`

          - `type: "content_block_location"`

        - `beta_citations_web_search_result_location: object { cited_text, encrypted_index, title, 2 more }`

          - `cited_text: string`

          - `encrypted_index: string`

          - `title: string`

          - `type: "web_search_result_location"`

          - `url: string`

        - `beta_citation_search_result_location: object { cited_text, end_block_index, search_result_index, 4 more }`

          - `cited_text: string`

          - `end_block_index: number`

          - `search_result_index: number`

          - `source: string`

          - `start_block_index: number`

          - `title: string`

          - `type: "search_result_location"`

      - `text: string`

      - `type: "text"`

    - `beta_thinking_block: object { signature, thinking, type }`

      - `signature: string`

      - `thinking: string`

      - `type: "thinking"`

    - `beta_redacted_thinking_block: object { data, type }`

      - `data: string`

      - `type: "redacted_thinking"`

    - `beta_tool_use_block: object { id, input, name, 2 more }`

      - `id: string`

      - `input: map[unknown]`

      - `name: string`

      - `type: "tool_use"`

      - `caller: optional BetaDirectCaller or BetaServerToolCaller or BetaServerToolCaller20260120`

        Tool invocation directly from the model.

        - `beta_direct_caller: object { type }`

          Tool invocation directly from the model.

          - `type: "direct"`

        - `beta_server_tool_caller: object { tool_id, type }`

          Tool invocation generated by a server-side tool.

          - `tool_id: string`

          - `type: "code_execution_20250825"`

        - `beta_server_tool_caller_20260120: object { tool_id, type }`

          - `tool_id: string`

          - `type: "code_execution_20260120"`

    - `beta_server_tool_use_block: object { id, input, name, 2 more }`

      - `id: string`

      - `input: map[unknown]`

      - `name: "advisor" or "web_search" or "web_fetch" or 5 more`

        - `"advisor"`

        - `"web_search"`

        - `"web_fetch"`

        - `"code_execution"`

        - `"bash_code_execution"`

        - `"text_editor_code_execution"`

        - `"tool_search_tool_regex"`

        - `"tool_search_tool_bm25"`

      - `type: "server_tool_use"`

      - `caller: optional BetaDirectCaller or BetaServerToolCaller or BetaServerToolCaller20260120`

        Tool invocation directly from the model.

        - `beta_direct_caller: object { type }`

          Tool invocation directly from the model.

          - `type: "direct"`

        - `beta_server_tool_caller: object { tool_id, type }`

          Tool invocation generated by a server-side tool.

          - `tool_id: string`

          - `type: "code_execution_20250825"`

        - `beta_server_tool_caller_20260120: object { tool_id, type }`

          - `tool_id: string`

          - `type: "code_execution_20260120"`

    - `beta_web_search_tool_result_block: object { content, tool_use_id, type, caller }`

      - `content: BetaWebSearchToolResultError or array of BetaWebSearchResultBlock`

        - `beta_web_search_tool_result_error: object { error_code, type }`

          - `error_code: "invalid_tool_input" or "unavailable" or "max_uses_exceeded" or 3 more`

            - `"invalid_tool_input"`

            - `"unavailable"`

            - `"max_uses_exceeded"`

            - `"too_many_requests"`

            - `"query_too_long"`

            - `"request_too_large"`

          - `type: "web_search_tool_result_error"`

        - `union_member_1: array of BetaWebSearchResultBlock`

          - `encrypted_content: string`

          - `page_age: string`

          - `title: string`

          - `type: "web_search_result"`

          - `url: string`

      - `tool_use_id: string`

      - `type: "web_search_tool_result"`

      - `caller: optional BetaDirectCaller or BetaServerToolCaller or BetaServerToolCaller20260120`

        Tool invocation directly from the model.

        - `beta_direct_caller: object { type }`

          Tool invocation directly from the model.

          - `type: "direct"`

        - `beta_server_tool_caller: object { tool_id, type }`

          Tool invocation generated by a server-side tool.

          - `tool_id: string`

          - `type: "code_execution_20250825"`

        - `beta_server_tool_caller_20260120: object { tool_id, type }`

          - `tool_id: string`

          - `type: "code_execution_20260120"`

    - `beta_web_fetch_tool_result_block: object { content, tool_use_id, type, caller }`

      - `content: BetaWebFetchToolResultErrorBlock or BetaWebFetchBlock`

        - `beta_web_fetch_tool_result_error_block: object { error_code, type }`

          - `error_code: "invalid_tool_input" or "url_too_long" or "url_not_allowed" or 5 more`

            - `"invalid_tool_input"`

            - `"url_too_long"`

            - `"url_not_allowed"`

            - `"url_not_accessible"`

            - `"unsupported_content_type"`

            - `"too_many_requests"`

            - `"max_uses_exceeded"`

            - `"unavailable"`

          - `type: "web_fetch_tool_result_error"`

        - `beta_web_fetch_block: object { content, retrieved_at, type, url }`

          - `content: object { citations, source, title, type }`

            - `citations: object { enabled }`

              Citation configuration for the document

              - `enabled: boolean`

            - `source: BetaBase64PDFSource or BetaPlainTextSource`

              - `beta_base64_pdf_source: object { data, media_type, type }`

                - `data: string`

                - `media_type: "application/pdf"`

                - `type: "base64"`

              - `beta_plain_text_source: object { data, media_type, type }`

                - `data: string`

                - `media_type: "text/plain"`

                - `type: "text"`

            - `title: string`

              The title of the document

            - `type: "document"`

          - `retrieved_at: string`

            ISO 8601 timestamp when the content was retrieved

          - `type: "web_fetch_result"`

          - `url: string`

            Fetched content URL

      - `tool_use_id: string`

      - `type: "web_fetch_tool_result"`

      - `caller: optional BetaDirectCaller or BetaServerToolCaller or BetaServerToolCaller20260120`

        Tool invocation directly from the model.

        - `beta_direct_caller: object { type }`

          Tool invocation directly from the model.

          - `type: "direct"`

        - `beta_server_tool_caller: object { tool_id, type }`

          Tool invocation generated by a server-side tool.

          - `tool_id: string`

          - `type: "code_execution_20250825"`

        - `beta_server_tool_caller_20260120: object { tool_id, type }`

          - `tool_id: string`

          - `type: "code_execution_20260120"`

    - `beta_advisor_tool_result_block: object { content, tool_use_id, type }`

      - `content: BetaAdvisorToolResultError or BetaAdvisorResultBlock or BetaAdvisorRedactedResultBlock`

        - `beta_advisor_tool_result_error: object { error_code, type }`

          - `error_code: "max_uses_exceeded" or "prompt_too_long" or "too_many_requests" or 3 more`

            - `"max_uses_exceeded"`

            - `"prompt_too_long"`

            - `"too_many_requests"`

            - `"overloaded"`

            - `"unavailable"`

            - `"execution_time_exceeded"`

          - `type: "advisor_tool_result_error"`

        - `beta_advisor_result_block: object { text, type }`

          - `text: string`

          - `type: "advisor_result"`

        - `beta_advisor_redacted_result_block: object { encrypted_content, type }`

          - `encrypted_content: string`

            Opaque blob containing the advisor's output. Round-trip verbatim; do not inspect or modify.

          - `type: "advisor_redacted_result"`

      - `tool_use_id: string`

      - `type: "advisor_tool_result"`

    - `beta_code_execution_tool_result_block: object { content, tool_use_id, type }`

      - `content: BetaCodeExecutionToolResultError or BetaCodeExecutionResultBlock or BetaEncryptedCodeExecutionResultBlock`

        Code execution result with encrypted stdout for PFC + web_search results.

        - `beta_code_execution_tool_result_error: object { error_code, type }`

          - `error_code: "invalid_tool_input" or "unavailable" or "too_many_requests" or "execution_time_exceeded"`

            - `"invalid_tool_input"`

            - `"unavailable"`

            - `"too_many_requests"`

            - `"execution_time_exceeded"`

          - `type: "code_execution_tool_result_error"`

        - `beta_code_execution_result_block: object { content, return_code, stderr, 2 more }`

          - `content: array of BetaCodeExecutionOutputBlock`

            - `file_id: string`

            - `type: "code_execution_output"`

          - `return_code: number`

          - `stderr: string`

          - `stdout: string`

          - `type: "code_execution_result"`

        - `beta_encrypted_code_execution_result_block: object { content, encrypted_stdout, return_code, 2 more }`

          Code execution result with encrypted stdout for PFC + web_search results.

          - `content: array of BetaCodeExecutionOutputBlock`

            - `file_id: string`

            - `type: "code_execution_output"`

          - `encrypted_stdout: string`

          - `return_code: number`

          - `stderr: string`

          - `type: "encrypted_code_execution_result"`

      - `tool_use_id: string`

      - `type: "code_execution_tool_result"`

    - `beta_bash_code_execution_tool_result_block: object { content, tool_use_id, type }`

      - `content: BetaBashCodeExecutionToolResultError or BetaBashCodeExecutionResultBlock`

        - `beta_bash_code_execution_tool_result_error: object { error_code, type }`

          - `error_code: "invalid_tool_input" or "unavailable" or "too_many_requests" or 2 more`

            - `"invalid_tool_input"`

            - `"unavailable"`

            - `"too_many_requests"`

            - `"execution_time_exceeded"`

            - `"output_file_too_large"`

          - `type: "bash_code_execution_tool_result_error"`

        - `beta_bash_code_execution_result_block: object { content, return_code, stderr, 2 more }`

          - `content: array of BetaBashCodeExecutionOutputBlock`

            - `file_id: string`

            - `type: "bash_code_execution_output"`

          - `return_code: number`

          - `stderr: string`

          - `stdout: string`

          - `type: "bash_code_execution_result"`

      - `tool_use_id: string`

      - `type: "bash_code_execution_tool_result"`

    - `beta_text_editor_code_execution_tool_result_block: object { content, tool_use_id, type }`

      - `content: BetaTextEditorCodeExecutionToolResultError or BetaTextEditorCodeExecutionViewResultBlock or BetaTextEditorCodeExecutionCreateResultBlock or BetaTextEditorCodeExecutionStrReplaceResultBlock`

        - `beta_text_editor_code_execution_tool_result_error: object { error_code, error_message, type }`

          - `error_code: "invalid_tool_input" or "unavailable" or "too_many_requests" or 2 more`

            - `"invalid_tool_input"`

            - `"unavailable"`

            - `"too_many_requests"`

            - `"execution_time_exceeded"`

            - `"file_not_found"`

          - `error_message: string`

          - `type: "text_editor_code_execution_tool_result_error"`

        - `beta_text_editor_code_execution_view_result_block: object { content, file_type, num_lines, 3 more }`

          - `content: string`

          - `file_type: "text" or "image" or "pdf"`

            - `"text"`

            - `"image"`

            - `"pdf"`

          - `num_lines: number`

          - `start_line: number`

          - `total_lines: number`

          - `type: "text_editor_code_execution_view_result"`

        - `beta_text_editor_code_execution_create_result_block: object { is_file_update, type }`

          - `is_file_update: boolean`

          - `type: "text_editor_code_execution_create_result"`

        - `beta_text_editor_code_execution_str_replace_result_block: object { lines, new_lines, new_start, 3 more }`

          - `lines: array of string`

          - `new_lines: number`

          - `new_start: number`

          - `old_lines: number`

          - `old_start: number`

          - `type: "text_editor_code_execution_str_replace_result"`

      - `tool_use_id: string`

      - `type: "text_editor_code_execution_tool_result"`

    - `beta_tool_search_tool_result_block: object { content, tool_use_id, type }`

      - `content: BetaToolSearchToolResultError or BetaToolSearchToolSearchResultBlock`

        - `beta_tool_search_tool_result_error: object { error_code, error_message, type }`

          - `error_code: "invalid_tool_input" or "unavailable" or "too_many_requests" or "execution_time_exceeded"`

            - `"invalid_tool_input"`

            - `"unavailable"`

            - `"too_many_requests"`

            - `"execution_time_exceeded"`

          - `error_message: string`

          - `type: "tool_search_tool_result_error"`

        - `beta_tool_search_tool_search_result_block: object { tool_references, type }`

          - `tool_references: array of BetaToolReferenceBlock`

            - `tool_name: string`

            - `type: "tool_reference"`

          - `type: "tool_search_tool_search_result"`

      - `tool_use_id: string`

      - `type: "tool_search_tool_result"`

    - `beta_mcp_tool_use_block: object { id, input, name, 2 more }`

      - `id: string`

      - `input: map[unknown]`

      - `name: string`

        The name of the MCP tool

      - `server_name: string`

        The name of the MCP server

      - `type: "mcp_tool_use"`

    - `beta_mcp_tool_result_block: object { content, is_error, tool_use_id, type }`

      - `content: string or array of BetaTextBlock`

        - `union_member_0: string`

        - `beta_mcp_tool_result_block_content: array of BetaTextBlock`

          - `citations: array of BetaTextCitation`

            Citations supporting the text block.

            The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

            - `beta_citation_char_location: object { cited_text, document_index, document_title, 4 more }`

              - `cited_text: string`

              - `document_index: number`

              - `document_title: string`

              - `end_char_index: number`

              - `file_id: string`

              - `start_char_index: number`

              - `type: "char_location"`

            - `beta_citation_page_location: object { cited_text, document_index, document_title, 4 more }`

              - `cited_text: string`

              - `document_index: number`

              - `document_title: string`

              - `end_page_number: number`

              - `file_id: string`

              - `start_page_number: number`

              - `type: "page_location"`

            - `beta_citation_content_block_location: object { cited_text, document_index, document_title, 4 more }`

              - `cited_text: string`

              - `document_index: number`

              - `document_title: string`

              - `end_block_index: number`

              - `file_id: string`

              - `start_block_index: number`

              - `type: "content_block_location"`

            - `beta_citations_web_search_result_location: object { cited_text, encrypted_index, title, 2 more }`

              - `cited_text: string`

              - `encrypted_index: string`

              - `title: string`

              - `type: "web_search_result_location"`

              - `url: string`

            - `beta_citation_search_result_location: object { cited_text, end_block_index, search_result_index, 4 more }`

              - `cited_text: string`

              - `end_block_index: number`

              - `search_result_index: number`

              - `source: string`

              - `start_block_index: number`

              - `title: string`

              - `type: "search_result_location"`

          - `text: string`

          - `type: "text"`

      - `is_error: boolean`

      - `tool_use_id: string`

      - `type: "mcp_tool_result"`

    - `beta_container_upload_block: object { file_id, type }`

      Response model for a file uploaded to the container.

      - `file_id: string`

      - `type: "container_upload"`

    - `beta_compaction_block: object { content, type }`

      A compaction block returned when autocompact is triggered.

      When content is None, it indicates the compaction failed to produce a valid
      summary (e.g., malformed output from the model). Clients may round-trip
      compaction blocks with null content; the server treats them as no-ops.

      - `content: string`

        Summary of compacted content, or null if compaction failed

      - `type: "compaction"`

  - `context_management: object { applied_edits }`

    Context management response.

    Information about context management strategies applied during the request.

    - `applied_edits: array of BetaClearToolUses20250919EditResponse or BetaClearThinking20251015EditResponse`

      List of context management edits that were applied.

      - `beta_clear_tool_uses_20250919_edit_response: object { cleared_input_tokens, cleared_tool_uses, type }`

        - `cleared_input_tokens: number`

          Number of input tokens cleared by this edit.

        - `cleared_tool_uses: number`

          Number of tool uses that were cleared.

        - `type: "clear_tool_uses_20250919"`

          The type of context management edit applied.

      - `beta_clear_thinking_20251015_edit_response: object { cleared_input_tokens, cleared_thinking_turns, type }`

        - `cleared_input_tokens: number`

          Number of input tokens cleared by this edit.

        - `cleared_thinking_turns: number`

          Number of thinking turns that were cleared.

        - `type: "clear_thinking_20251015"`

          The type of context management edit applied.

  - `model: "claude-opus-4-7" or "claude-mythos-preview" or "claude-opus-4-6" or 14 more or string`

    The model that will complete your prompt.

    See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

    - `"claude-opus-4-7"`

      Frontier intelligence for long-running agents and coding

    - `"claude-mythos-preview"`

      New class of intelligence, strongest in coding and cybersecurity

    - `"claude-opus-4-6"`

      Frontier intelligence for long-running agents and coding

    - `"claude-sonnet-4-6"`

      Best combination of speed and intelligence

    - `"claude-haiku-4-5"`

      Fastest model with near-frontier intelligence

    - `"claude-haiku-4-5-20251001"`

      Fastest model with near-frontier intelligence

    - `"claude-opus-4-5"`

      Premium model combining maximum intelligence with practical performance

    - `"claude-opus-4-5-20251101"`

      Premium model combining maximum intelligence with practical performance

    - `"claude-sonnet-4-5"`

      High-performance model for agents and coding

    - `"claude-sonnet-4-5-20250929"`

      High-performance model for agents and coding

    - `"claude-opus-4-1"`

      Exceptional model for specialized complex tasks

    - `"claude-opus-4-1-20250805"`

      Exceptional model for specialized complex tasks

    - `"claude-opus-4-0"`

      Powerful model for complex tasks

    - `"claude-opus-4-20250514"`

      Powerful model for complex tasks

    - `"claude-sonnet-4-0"`

      High-performance model with extended thinking

    - `"claude-sonnet-4-20250514"`

      High-performance model with extended thinking

    - `"claude-3-haiku-20240307"`

      Fast and cost-effective model

  - `role: "assistant"`

    Conversational role of the generated message.

    This will always be `"assistant"`.

  - `stop_details: object { category, explanation, type }`

    Structured information about a refusal.

    - `category: "cyber" or "bio"`

      The policy category that triggered the refusal.

      `null` when the refusal doesn't map to a named category.

      - `"cyber"`

      - `"bio"`

    - `explanation: string`

      Human-readable explanation of the refusal.

      This text is not guaranteed to be stable. `null` when no explanation is available for the category.

    - `type: "refusal"`

  - `stop_reason: "end_turn" or "max_tokens" or "stop_sequence" or 5 more`

    The reason that we stopped.

    This may be one the following values:

    * `"end_turn"`: the model reached a natural stopping point
    * `"max_tokens"`: we exceeded the requested `max_tokens` or the model's maximum
    * `"stop_sequence"`: one of your provided custom `stop_sequences` was generated
    * `"tool_use"`: the model invoked one or more tools
    * `"pause_turn"`: we paused a long-running turn. You may provide the response back as-is in a subsequent request to let the model continue.
    * `"refusal"`: when streaming classifiers intervene to handle potential policy violations

    In non-streaming mode this value is always non-null. In streaming mode, it is null in the `message_start` event and non-null otherwise.

    - `"end_turn"`

    - `"max_tokens"`

    - `"stop_sequence"`

    - `"tool_use"`

    - `"pause_turn"`

    - `"compaction"`

    - `"refusal"`

    - `"model_context_window_exceeded"`

  - `stop_sequence: string`

    Which custom stop sequence was generated, if any.

    This value will be a non-null string if one of your custom stop sequences was generated.

  - `type: "message"`

    Object type.

    For Messages, this is always `"message"`.

  - `usage: object { cache_creation, cache_creation_input_tokens, cache_read_input_tokens, 7 more }`

    Billing and rate-limit usage.

    Anthropic's API bills and rate-limits by token counts, as tokens represent the underlying cost to our systems.

    Under the hood, the API transforms requests into a format suitable for the model. The model's output then goes through a parsing stage before becoming an API response. As a result, the token counts in `usage` will not match one-to-one with the exact visible content of an API request or response.

    For example, `output_tokens` will be non-zero, even for an empty string response from Claude.

    Total input tokens in a request is the summation of `input_tokens`, `cache_creation_input_tokens`, and `cache_read_input_tokens`.

    - `cache_creation: object { ephemeral_1h_input_tokens, ephemeral_5m_input_tokens }`

      Breakdown of cached tokens by TTL

      - `ephemeral_1h_input_tokens: number`

        The number of input tokens used to create the 1 hour cache entry.

      - `ephemeral_5m_input_tokens: number`

        The number of input tokens used to create the 5 minute cache entry.

    - `cache_creation_input_tokens: number`

      The number of input tokens used to create the cache entry.

    - `cache_read_input_tokens: number`

      The number of input tokens read from the cache.

    - `inference_geo: string`

      The geographic region where inference was performed for this request.

    - `input_tokens: number`

      The number of input tokens which were used.

    - `iterations: array of BetaMessageIterationUsage or BetaCompactionIterationUsage or BetaAdvisorMessageIterationUsage`

      Per-iteration token usage breakdown.

      Each entry represents one sampling iteration, with its own input/output token counts and cache statistics. This allows you to:

      - Determine which iterations exceeded long context thresholds (>=200k tokens)
      - Calculate the true context window size from the last iteration
      - Understand token accumulation across server-side tool use loops

      - `beta_message_iteration_usage: object { cache_creation, cache_creation_input_tokens, cache_read_input_tokens, 3 more }`

        Token usage for a sampling iteration.

        - `cache_creation: object { ephemeral_1h_input_tokens, ephemeral_5m_input_tokens }`

          Breakdown of cached tokens by TTL

          - `ephemeral_1h_input_tokens: number`

            The number of input tokens used to create the 1 hour cache entry.

          - `ephemeral_5m_input_tokens: number`

            The number of input tokens used to create the 5 minute cache entry.

        - `cache_creation_input_tokens: number`

          The number of input tokens used to create the cache entry.

        - `cache_read_input_tokens: number`

          The number of input tokens read from the cache.

        - `input_tokens: number`

          The number of input tokens which were used.

        - `output_tokens: number`

          The number of output tokens which were used.

        - `type: "message"`

          Usage for a sampling iteration

      - `beta_compaction_iteration_usage: object { cache_creation, cache_creation_input_tokens, cache_read_input_tokens, 3 more }`

        Token usage for a compaction iteration.

        - `cache_creation: object { ephemeral_1h_input_tokens, ephemeral_5m_input_tokens }`

          Breakdown of cached tokens by TTL

          - `ephemeral_1h_input_tokens: number`

            The number of input tokens used to create the 1 hour cache entry.

          - `ephemeral_5m_input_tokens: number`

            The number of input tokens used to create the 5 minute cache entry.

        - `cache_creation_input_tokens: number`

          The number of input tokens used to create the cache entry.

        - `cache_read_input_tokens: number`

          The number of input tokens read from the cache.

        - `input_tokens: number`

          The number of input tokens which were used.

        - `output_tokens: number`

          The number of output tokens which were used.

        - `type: "compaction"`

          Usage for a compaction iteration

      - `beta_advisor_message_iteration_usage: object { cache_creation, cache_creation_input_tokens, cache_read_input_tokens, 4 more }`

        Token usage for an advisor sub-inference iteration.

        - `cache_creation: object { ephemeral_1h_input_tokens, ephemeral_5m_input_tokens }`

          Breakdown of cached tokens by TTL

          - `ephemeral_1h_input_tokens: number`

            The number of input tokens used to create the 1 hour cache entry.

          - `ephemeral_5m_input_tokens: number`

            The number of input tokens used to create the 5 minute cache entry.

        - `cache_creation_input_tokens: number`

          The number of input tokens used to create the cache entry.

        - `cache_read_input_tokens: number`

          The number of input tokens read from the cache.

        - `input_tokens: number`

          The number of input tokens which were used.

        - `model: "claude-opus-4-7" or "claude-mythos-preview" or "claude-opus-4-6" or 14 more or string`

          The model that will complete your prompt.

          See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

          - `"claude-opus-4-7"`

            Frontier intelligence for long-running agents and coding

          - `"claude-mythos-preview"`

            New class of intelligence, strongest in coding and cybersecurity

          - `"claude-opus-4-6"`

            Frontier intelligence for long-running agents and coding

          - `"claude-sonnet-4-6"`

            Best combination of speed and intelligence

          - `"claude-haiku-4-5"`

            Fastest model with near-frontier intelligence

          - `"claude-haiku-4-5-20251001"`

            Fastest model with near-frontier intelligence

          - `"claude-opus-4-5"`

            Premium model combining maximum intelligence with practical performance

          - `"claude-opus-4-5-20251101"`

            Premium model combining maximum intelligence with practical performance

          - `"claude-sonnet-4-5"`

            High-performance model for agents and coding

          - `"claude-sonnet-4-5-20250929"`

            High-performance model for agents and coding

          - `"claude-opus-4-1"`

            Exceptional model for specialized complex tasks

          - `"claude-opus-4-1-20250805"`

            Exceptional model for specialized complex tasks

          - `"claude-opus-4-0"`

            Powerful model for complex tasks

          - `"claude-opus-4-20250514"`

            Powerful model for complex tasks

          - `"claude-sonnet-4-0"`

            High-performance model with extended thinking

          - `"claude-sonnet-4-20250514"`

            High-performance model with extended thinking

          - `"claude-3-haiku-20240307"`

            Fast and cost-effective model

        - `output_tokens: number`

          The number of output tokens which were used.

        - `type: "advisor_message"`

          Usage for an advisor sub-inference iteration

    - `output_tokens: number`

      The number of output tokens which were used.

    - `server_tool_use: object { web_fetch_requests, web_search_requests }`

      The number of server tool requests.

      - `web_fetch_requests: number`

        The number of web fetch tool requests.

      - `web_search_requests: number`

        The number of web search tool requests.

    - `service_tier: "standard" or "priority" or "batch"`

      If the request used the priority, standard, or batch tier.

      - `"standard"`

      - `"priority"`

      - `"batch"`

    - `speed: "standard" or "fast"`

      The inference speed mode used for this request.

      - `"standard"`

      - `"fast"`

### Example

```cli
ant beta:messages create \
  --api-key my-anthropic-api-key \
  --max-tokens 1024 \
  --message '{content: [{text: x, type: text}], role: user}' \
  --model claude-opus-4-6
```
