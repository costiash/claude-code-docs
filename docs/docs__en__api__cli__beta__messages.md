# Messages

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

- `--output-config: optional object { effort, format, task_budget }`

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

  Recommended for advanced use cases only. You usually only need to use `temperature`.

- `--top-p: optional number`

  Body param: Use nucleus sampling.

  In nucleus sampling, we compute the cumulative distribution over all the options for each subsequent token in decreasing probability order and cut it off once it reaches a particular probability specified by `top_p`. You should either alter `temperature` or `top_p`, but not both.

  Recommended for advanced use cases only. You usually only need to use `temperature`.

- `--user-profile-id: optional string`

  Body param: The user profile ID to attribute this request to. Use when acting on behalf of a party other than your organization.

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

    - `beta_compaction_block: object { content, encrypted_content, type }`

      A compaction block returned when autocompact is triggered.

      When content is None, it indicates the compaction failed to produce a valid
      summary (e.g., malformed output from the model). Clients may round-trip
      compaction blocks with null content; the server treats them as no-ops.

      - `content: string`

        Summary of compacted content, or null if compaction failed

      - `encrypted_content: string`

        Opaque metadata from prior compaction, to be round-tripped verbatim

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

## Count Tokens

`$ ant beta:messages count-tokens`

**post** `/v1/messages/count_tokens`

Count the number of tokens in a Message.

The Token Count API can be used to count the number of tokens in a Message, including tools, images, and documents, without creating it.

Learn more about token counting in our [user guide](https://docs.claude.com/en/docs/build-with-claude/token-counting)

### Parameters

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

- `--context-management: optional object { edits }`

  Body param: Context management configuration.

  This allows you to control how Claude manages context across multiple requests, such as whether to clear function results or not.

- `--mcp-server: optional array of BetaRequestMCPServerURLDefinition`

  Body param: MCP servers to be utilized in this request

- `--output-config: optional object { effort, format, task_budget }`

  Body param: Configuration options for the model's output, such as the output format.

- `--output-format: optional object { schema, type }`

  Body param: Deprecated: Use `output_config.format` instead. See [structured outputs](https://platform.claude.com/docs/en/build-with-claude/structured-outputs)

  A schema to specify Claude's output format in responses. This parameter will be removed in a future release.

- `--speed: optional "standard" or "fast"`

  Body param: The inference speed mode for this request. `"fast"` enables high output-tokens-per-second inference.

- `--system: optional string or array of BetaTextBlockParam`

  Body param: System prompt.

  A system prompt is a way of providing context and instructions to Claude, such as specifying a particular goal or role. See our [guide to system prompts](https://docs.claude.com/en/docs/system-prompts).

- `--thinking: optional BetaThinkingConfigEnabled or BetaThinkingConfigDisabled or BetaThinkingConfigAdaptive`

  Body param: Configuration for enabling Claude's extended thinking.

  When enabled, responses include `thinking` content blocks showing Claude's thinking process before the final answer. Requires a minimum budget of 1,024 tokens and counts towards your `max_tokens` limit.

  See [extended thinking](https://docs.claude.com/en/docs/build-with-claude/extended-thinking) for details.

- `--tool-choice: optional BetaToolChoiceAuto or BetaToolChoiceAny or BetaToolChoiceTool or BetaToolChoiceNone`

  Body param: How the model should use the provided tools. The model can use a specific tool, any available tool, decide by itself, or not use tools at all.

- `--tool: optional array of BetaTool or BetaToolBash20241022 or BetaToolBash20250124 or 20 more`

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

- `--beta: optional array of AnthropicBeta`

  Header param: Optional header to specify the beta version(s) you want to use.

### Returns

- `beta_message_tokens_count: object { context_management, input_tokens }`

  - `context_management: object { original_input_tokens }`

    Information about context management applied to the message.

    - `original_input_tokens: number`

      The original token count before context management was applied

  - `input_tokens: number`

    The total number of tokens across the provided list of messages, system prompt, and tools.

### Example

```cli
ant beta:messages count-tokens \
  --api-key my-anthropic-api-key \
  --message '{content: [{text: x, type: text}], role: user}' \
  --model claude-opus-4-6
```

## Domain Types

### Beta Advisor Message Iteration Usage

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

### Beta Advisor Redacted Result Block

- `beta_advisor_redacted_result_block: object { encrypted_content, type }`

  - `encrypted_content: string`

    Opaque blob containing the advisor's output. Round-trip verbatim; do not inspect or modify.

  - `type: "advisor_redacted_result"`

### Beta Advisor Redacted Result Block Param

- `beta_advisor_redacted_result_block_param: object { encrypted_content, type }`

  - `encrypted_content: string`

    Opaque blob produced by a prior response; must be round-tripped verbatim.

  - `type: "advisor_redacted_result"`

### Beta Advisor Result Block

- `beta_advisor_result_block: object { text, type }`

  - `text: string`

  - `type: "advisor_result"`

### Beta Advisor Result Block Param

- `beta_advisor_result_block_param: object { text, type }`

  - `text: string`

  - `type: "advisor_result"`

### Beta Advisor Tool 20260301

- `beta_advisor_tool_20260301: object { model, name, type, 6 more }`

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

  - `name: "advisor"`

    Name of the tool.

    This is how the tool will be called by the model and in `tool_use` blocks.

  - `type: "advisor_20260301"`

  - `allowed_callers: optional array of "direct" or "code_execution_20250825" or "code_execution_20260120"`

    - `"direct"`

    - `"code_execution_20250825"`

    - `"code_execution_20260120"`

  - `cache_control: optional object { type, ttl }`

    Create a cache control breakpoint at this content block.

    - `type: "ephemeral"`

    - `ttl: optional "5m" or "1h"`

      The time-to-live for the cache control breakpoint.

      This may be one the following values:

      - `5m`: 5 minutes
      - `1h`: 1 hour

      Defaults to `5m`.

      - `"5m"`

      - `"1h"`

  - `caching: optional object { type, ttl }`

    Caching for the advisor's own prompt. When set, each advisor call writes a cache entry at the given TTL so subsequent calls in the same conversation read the stable prefix. When omitted, the advisor prompt is not cached.

    - `type: "ephemeral"`

    - `ttl: optional "5m" or "1h"`

      The time-to-live for the cache control breakpoint.

      This may be one the following values:

      - `5m`: 5 minutes
      - `1h`: 1 hour

      Defaults to `5m`.

      - `"5m"`

      - `"1h"`

  - `defer_loading: optional boolean`

    If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

  - `max_uses: optional number`

    Maximum number of times the tool can be used in the API request.

  - `strict: optional boolean`

    When true, guarantees schema validation on tool names and inputs

### Beta Advisor Tool Result Block

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

### Beta Advisor Tool Result Block Param

- `beta_advisor_tool_result_block_param: object { content, tool_use_id, type, cache_control }`

  - `content: BetaAdvisorToolResultErrorParam or BetaAdvisorResultBlockParam or BetaAdvisorRedactedResultBlockParam`

    - `beta_advisor_tool_result_error_param: object { error_code, type }`

      - `error_code: "max_uses_exceeded" or "prompt_too_long" or "too_many_requests" or 3 more`

        - `"max_uses_exceeded"`

        - `"prompt_too_long"`

        - `"too_many_requests"`

        - `"overloaded"`

        - `"unavailable"`

        - `"execution_time_exceeded"`

      - `type: "advisor_tool_result_error"`

    - `beta_advisor_result_block_param: object { text, type }`

      - `text: string`

      - `type: "advisor_result"`

    - `beta_advisor_redacted_result_block_param: object { encrypted_content, type }`

      - `encrypted_content: string`

        Opaque blob produced by a prior response; must be round-tripped verbatim.

      - `type: "advisor_redacted_result"`

  - `tool_use_id: string`

  - `type: "advisor_tool_result"`

  - `cache_control: optional object { type, ttl }`

    Create a cache control breakpoint at this content block.

    - `type: "ephemeral"`

    - `ttl: optional "5m" or "1h"`

      The time-to-live for the cache control breakpoint.

      This may be one the following values:

      - `5m`: 5 minutes
      - `1h`: 1 hour

      Defaults to `5m`.

      - `"5m"`

      - `"1h"`

### Beta Advisor Tool Result Error

- `beta_advisor_tool_result_error: object { error_code, type }`

  - `error_code: "max_uses_exceeded" or "prompt_too_long" or "too_many_requests" or 3 more`

    - `"max_uses_exceeded"`

    - `"prompt_too_long"`

    - `"too_many_requests"`

    - `"overloaded"`

    - `"unavailable"`

    - `"execution_time_exceeded"`

  - `type: "advisor_tool_result_error"`

### Beta Advisor Tool Result Error Param

- `beta_advisor_tool_result_error_param: object { error_code, type }`

  - `error_code: "max_uses_exceeded" or "prompt_too_long" or "too_many_requests" or 3 more`

    - `"max_uses_exceeded"`

    - `"prompt_too_long"`

    - `"too_many_requests"`

    - `"overloaded"`

    - `"unavailable"`

    - `"execution_time_exceeded"`

  - `type: "advisor_tool_result_error"`

### Beta All Thinking Turns

- `beta_all_thinking_turns: object { type }`

  - `type: "all"`

### Beta Base64 Image Source

- `beta_base64_image_source: object { data, media_type, type }`

  - `data: string`

  - `media_type: "image/jpeg" or "image/png" or "image/gif" or "image/webp"`

    - `"image/jpeg"`

    - `"image/png"`

    - `"image/gif"`

    - `"image/webp"`

  - `type: "base64"`

### Beta Base64 PDF Source

- `beta_base64_pdf_source: object { data, media_type, type }`

  - `data: string`

  - `media_type: "application/pdf"`

  - `type: "base64"`

### Beta Bash Code Execution Output Block

- `beta_bash_code_execution_output_block: object { file_id, type }`

  - `file_id: string`

  - `type: "bash_code_execution_output"`

### Beta Bash Code Execution Output Block Param

- `beta_bash_code_execution_output_block_param: object { file_id, type }`

  - `file_id: string`

  - `type: "bash_code_execution_output"`

### Beta Bash Code Execution Result Block

- `beta_bash_code_execution_result_block: object { content, return_code, stderr, 2 more }`

  - `content: array of BetaBashCodeExecutionOutputBlock`

    - `file_id: string`

    - `type: "bash_code_execution_output"`

  - `return_code: number`

  - `stderr: string`

  - `stdout: string`

  - `type: "bash_code_execution_result"`

### Beta Bash Code Execution Result Block Param

- `beta_bash_code_execution_result_block_param: object { content, return_code, stderr, 2 more }`

  - `content: array of BetaBashCodeExecutionOutputBlockParam`

    - `file_id: string`

    - `type: "bash_code_execution_output"`

  - `return_code: number`

  - `stderr: string`

  - `stdout: string`

  - `type: "bash_code_execution_result"`

### Beta Bash Code Execution Tool Result Block

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

### Beta Bash Code Execution Tool Result Block Param

- `beta_bash_code_execution_tool_result_block_param: object { content, tool_use_id, type, cache_control }`

  - `content: BetaBashCodeExecutionToolResultErrorParam or BetaBashCodeExecutionResultBlockParam`

    - `beta_bash_code_execution_tool_result_error_param: object { error_code, type }`

      - `error_code: "invalid_tool_input" or "unavailable" or "too_many_requests" or 2 more`

        - `"invalid_tool_input"`

        - `"unavailable"`

        - `"too_many_requests"`

        - `"execution_time_exceeded"`

        - `"output_file_too_large"`

      - `type: "bash_code_execution_tool_result_error"`

    - `beta_bash_code_execution_result_block_param: object { content, return_code, stderr, 2 more }`

      - `content: array of BetaBashCodeExecutionOutputBlockParam`

        - `file_id: string`

        - `type: "bash_code_execution_output"`

      - `return_code: number`

      - `stderr: string`

      - `stdout: string`

      - `type: "bash_code_execution_result"`

  - `tool_use_id: string`

  - `type: "bash_code_execution_tool_result"`

  - `cache_control: optional object { type, ttl }`

    Create a cache control breakpoint at this content block.

    - `type: "ephemeral"`

    - `ttl: optional "5m" or "1h"`

      The time-to-live for the cache control breakpoint.

      This may be one the following values:

      - `5m`: 5 minutes
      - `1h`: 1 hour

      Defaults to `5m`.

      - `"5m"`

      - `"1h"`

### Beta Bash Code Execution Tool Result Error

- `beta_bash_code_execution_tool_result_error: object { error_code, type }`

  - `error_code: "invalid_tool_input" or "unavailable" or "too_many_requests" or 2 more`

    - `"invalid_tool_input"`

    - `"unavailable"`

    - `"too_many_requests"`

    - `"execution_time_exceeded"`

    - `"output_file_too_large"`

  - `type: "bash_code_execution_tool_result_error"`

### Beta Bash Code Execution Tool Result Error Param

- `beta_bash_code_execution_tool_result_error_param: object { error_code, type }`

  - `error_code: "invalid_tool_input" or "unavailable" or "too_many_requests" or 2 more`

    - `"invalid_tool_input"`

    - `"unavailable"`

    - `"too_many_requests"`

    - `"execution_time_exceeded"`

    - `"output_file_too_large"`

  - `type: "bash_code_execution_tool_result_error"`

### Beta Cache Control Ephemeral

- `beta_cache_control_ephemeral: object { type, ttl }`

  - `type: "ephemeral"`

  - `ttl: optional "5m" or "1h"`

    The time-to-live for the cache control breakpoint.

    This may be one the following values:

    - `5m`: 5 minutes
    - `1h`: 1 hour

    Defaults to `5m`.

    - `"5m"`

    - `"1h"`

### Beta Cache Creation

- `beta_cache_creation: object { ephemeral_1h_input_tokens, ephemeral_5m_input_tokens }`

  - `ephemeral_1h_input_tokens: number`

    The number of input tokens used to create the 1 hour cache entry.

  - `ephemeral_5m_input_tokens: number`

    The number of input tokens used to create the 5 minute cache entry.

### Beta Citation Char Location

- `beta_citation_char_location: object { cited_text, document_index, document_title, 4 more }`

  - `cited_text: string`

  - `document_index: number`

  - `document_title: string`

  - `end_char_index: number`

  - `file_id: string`

  - `start_char_index: number`

  - `type: "char_location"`

### Beta Citation Char Location Param

- `beta_citation_char_location_param: object { cited_text, document_index, document_title, 3 more }`

  - `cited_text: string`

  - `document_index: number`

  - `document_title: string`

  - `end_char_index: number`

  - `start_char_index: number`

  - `type: "char_location"`

### Beta Citation Config

- `beta_citation_config: object { enabled }`

  - `enabled: boolean`

### Beta Citation Content Block Location

- `beta_citation_content_block_location: object { cited_text, document_index, document_title, 4 more }`

  - `cited_text: string`

  - `document_index: number`

  - `document_title: string`

  - `end_block_index: number`

  - `file_id: string`

  - `start_block_index: number`

  - `type: "content_block_location"`

### Beta Citation Content Block Location Param

- `beta_citation_content_block_location_param: object { cited_text, document_index, document_title, 3 more }`

  - `cited_text: string`

  - `document_index: number`

  - `document_title: string`

  - `end_block_index: number`

  - `start_block_index: number`

  - `type: "content_block_location"`

### Beta Citation Page Location

- `beta_citation_page_location: object { cited_text, document_index, document_title, 4 more }`

  - `cited_text: string`

  - `document_index: number`

  - `document_title: string`

  - `end_page_number: number`

  - `file_id: string`

  - `start_page_number: number`

  - `type: "page_location"`

### Beta Citation Page Location Param

- `beta_citation_page_location_param: object { cited_text, document_index, document_title, 3 more }`

  - `cited_text: string`

  - `document_index: number`

  - `document_title: string`

  - `end_page_number: number`

  - `start_page_number: number`

  - `type: "page_location"`

### Beta Citation Search Result Location

- `beta_citation_search_result_location: object { cited_text, end_block_index, search_result_index, 4 more }`

  - `cited_text: string`

  - `end_block_index: number`

  - `search_result_index: number`

  - `source: string`

  - `start_block_index: number`

  - `title: string`

  - `type: "search_result_location"`

### Beta Citation Search Result Location Param

- `beta_citation_search_result_location_param: object { cited_text, end_block_index, search_result_index, 4 more }`

  - `cited_text: string`

  - `end_block_index: number`

  - `search_result_index: number`

  - `source: string`

  - `start_block_index: number`

  - `title: string`

  - `type: "search_result_location"`

### Beta Citation Web Search Result Location Param

- `beta_citation_web_search_result_location_param: object { cited_text, encrypted_index, title, 2 more }`

  - `cited_text: string`

  - `encrypted_index: string`

  - `title: string`

  - `type: "web_search_result_location"`

  - `url: string`

### Beta Citations Config Param

- `beta_citations_config_param: object { enabled }`

  - `enabled: optional boolean`

### Beta Citations Delta

- `beta_citations_delta: object { citation, type }`

  - `citation: BetaCitationCharLocation or BetaCitationPageLocation or BetaCitationContentBlockLocation or 2 more`

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

  - `type: "citations_delta"`

### Beta Citations Web Search Result Location

- `beta_citations_web_search_result_location: object { cited_text, encrypted_index, title, 2 more }`

  - `cited_text: string`

  - `encrypted_index: string`

  - `title: string`

  - `type: "web_search_result_location"`

  - `url: string`

### Beta Clear Thinking 20251015 Edit

- `beta_clear_thinking_20251015_edit: object { type, keep }`

  - `type: "clear_thinking_20251015"`

  - `keep: optional BetaThinkingTurns or BetaAllThinkingTurns or "all"`

    Number of most recent assistant turns to keep thinking blocks for. Older turns will have their thinking blocks removed.

    - `beta_thinking_turns: object { type, value }`

      - `type: "thinking_turns"`

      - `value: number`

    - `beta_all_thinking_turns: object { type }`

      - `type: "all"`

    - `union_member_2: "all"`

### Beta Clear Thinking 20251015 Edit Response

- `beta_clear_thinking_20251015_edit_response: object { cleared_input_tokens, cleared_thinking_turns, type }`

  - `cleared_input_tokens: number`

    Number of input tokens cleared by this edit.

  - `cleared_thinking_turns: number`

    Number of thinking turns that were cleared.

  - `type: "clear_thinking_20251015"`

    The type of context management edit applied.

### Beta Clear Tool Uses 20250919 Edit

- `beta_clear_tool_uses_20250919_edit: object { type, clear_at_least, clear_tool_inputs, 3 more }`

  - `type: "clear_tool_uses_20250919"`

  - `clear_at_least: optional object { type, value }`

    Minimum number of tokens that must be cleared when triggered. Context will only be modified if at least this many tokens can be removed.

    - `type: "input_tokens"`

    - `value: number`

  - `clear_tool_inputs: optional boolean or array of string`

    Whether to clear all tool inputs (bool) or specific tool inputs to clear (list)

    - `union_member_0: boolean`

    - `union_member_1: array of string`

  - `exclude_tools: optional array of string`

    Tool names whose uses are preserved from clearing

  - `keep: optional object { type, value }`

    Number of tool uses to retain in the conversation

    - `type: "tool_uses"`

    - `value: number`

  - `trigger: optional BetaInputTokensTrigger or BetaToolUsesTrigger`

    Condition that triggers the context management strategy

    - `beta_input_tokens_trigger: object { type, value }`

      - `type: "input_tokens"`

      - `value: number`

    - `beta_tool_uses_trigger: object { type, value }`

      - `type: "tool_uses"`

      - `value: number`

### Beta Clear Tool Uses 20250919 Edit Response

- `beta_clear_tool_uses_20250919_edit_response: object { cleared_input_tokens, cleared_tool_uses, type }`

  - `cleared_input_tokens: number`

    Number of input tokens cleared by this edit.

  - `cleared_tool_uses: number`

    Number of tool uses that were cleared.

  - `type: "clear_tool_uses_20250919"`

    The type of context management edit applied.

### Beta Code Execution Output Block

- `beta_code_execution_output_block: object { file_id, type }`

  - `file_id: string`

  - `type: "code_execution_output"`

### Beta Code Execution Output Block Param

- `beta_code_execution_output_block_param: object { file_id, type }`

  - `file_id: string`

  - `type: "code_execution_output"`

### Beta Code Execution Result Block

- `beta_code_execution_result_block: object { content, return_code, stderr, 2 more }`

  - `content: array of BetaCodeExecutionOutputBlock`

    - `file_id: string`

    - `type: "code_execution_output"`

  - `return_code: number`

  - `stderr: string`

  - `stdout: string`

  - `type: "code_execution_result"`

### Beta Code Execution Result Block Param

- `beta_code_execution_result_block_param: object { content, return_code, stderr, 2 more }`

  - `content: array of BetaCodeExecutionOutputBlockParam`

    - `file_id: string`

    - `type: "code_execution_output"`

  - `return_code: number`

  - `stderr: string`

  - `stdout: string`

  - `type: "code_execution_result"`

### Beta Code Execution Tool 20250522

- `beta_code_execution_tool_20250522: object { name, type, allowed_callers, 3 more }`

  - `name: "code_execution"`

    Name of the tool.

    This is how the tool will be called by the model and in `tool_use` blocks.

  - `type: "code_execution_20250522"`

  - `allowed_callers: optional array of "direct" or "code_execution_20250825" or "code_execution_20260120"`

    - `"direct"`

    - `"code_execution_20250825"`

    - `"code_execution_20260120"`

  - `cache_control: optional object { type, ttl }`

    Create a cache control breakpoint at this content block.

    - `type: "ephemeral"`

    - `ttl: optional "5m" or "1h"`

      The time-to-live for the cache control breakpoint.

      This may be one the following values:

      - `5m`: 5 minutes
      - `1h`: 1 hour

      Defaults to `5m`.

      - `"5m"`

      - `"1h"`

  - `defer_loading: optional boolean`

    If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

  - `strict: optional boolean`

    When true, guarantees schema validation on tool names and inputs

### Beta Code Execution Tool 20250825

- `beta_code_execution_tool_20250825: object { name, type, allowed_callers, 3 more }`

  - `name: "code_execution"`

    Name of the tool.

    This is how the tool will be called by the model and in `tool_use` blocks.

  - `type: "code_execution_20250825"`

  - `allowed_callers: optional array of "direct" or "code_execution_20250825" or "code_execution_20260120"`

    - `"direct"`

    - `"code_execution_20250825"`

    - `"code_execution_20260120"`

  - `cache_control: optional object { type, ttl }`

    Create a cache control breakpoint at this content block.

    - `type: "ephemeral"`

    - `ttl: optional "5m" or "1h"`

      The time-to-live for the cache control breakpoint.

      This may be one the following values:

      - `5m`: 5 minutes
      - `1h`: 1 hour

      Defaults to `5m`.

      - `"5m"`

      - `"1h"`

  - `defer_loading: optional boolean`

    If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

  - `strict: optional boolean`

    When true, guarantees schema validation on tool names and inputs

### Beta Code Execution Tool 20260120

- `beta_code_execution_tool_20260120: object { name, type, allowed_callers, 3 more }`

  Code execution tool with REPL state persistence (daemon mode + gVisor checkpoint).

  - `name: "code_execution"`

    Name of the tool.

    This is how the tool will be called by the model and in `tool_use` blocks.

  - `type: "code_execution_20260120"`

  - `allowed_callers: optional array of "direct" or "code_execution_20250825" or "code_execution_20260120"`

    - `"direct"`

    - `"code_execution_20250825"`

    - `"code_execution_20260120"`

  - `cache_control: optional object { type, ttl }`

    Create a cache control breakpoint at this content block.

    - `type: "ephemeral"`

    - `ttl: optional "5m" or "1h"`

      The time-to-live for the cache control breakpoint.

      This may be one the following values:

      - `5m`: 5 minutes
      - `1h`: 1 hour

      Defaults to `5m`.

      - `"5m"`

      - `"1h"`

  - `defer_loading: optional boolean`

    If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

  - `strict: optional boolean`

    When true, guarantees schema validation on tool names and inputs

### Beta Code Execution Tool Result Block

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

### Beta Code Execution Tool Result Block Content

- `beta_code_execution_tool_result_block_content: BetaCodeExecutionToolResultError or BetaCodeExecutionResultBlock or BetaEncryptedCodeExecutionResultBlock`

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

### Beta Code Execution Tool Result Block Param

- `beta_code_execution_tool_result_block_param: object { content, tool_use_id, type, cache_control }`

  - `content: BetaCodeExecutionToolResultErrorParam or BetaCodeExecutionResultBlockParam or BetaEncryptedCodeExecutionResultBlockParam`

    Code execution result with encrypted stdout for PFC + web_search results.

    - `beta_code_execution_tool_result_error_param: object { error_code, type }`

      - `error_code: "invalid_tool_input" or "unavailable" or "too_many_requests" or "execution_time_exceeded"`

        - `"invalid_tool_input"`

        - `"unavailable"`

        - `"too_many_requests"`

        - `"execution_time_exceeded"`

      - `type: "code_execution_tool_result_error"`

    - `beta_code_execution_result_block_param: object { content, return_code, stderr, 2 more }`

      - `content: array of BetaCodeExecutionOutputBlockParam`

        - `file_id: string`

        - `type: "code_execution_output"`

      - `return_code: number`

      - `stderr: string`

      - `stdout: string`

      - `type: "code_execution_result"`

    - `beta_encrypted_code_execution_result_block_param: object { content, encrypted_stdout, return_code, 2 more }`

      Code execution result with encrypted stdout for PFC + web_search results.

      - `content: array of BetaCodeExecutionOutputBlockParam`

        - `file_id: string`

        - `type: "code_execution_output"`

      - `encrypted_stdout: string`

      - `return_code: number`

      - `stderr: string`

      - `type: "encrypted_code_execution_result"`

  - `tool_use_id: string`

  - `type: "code_execution_tool_result"`

  - `cache_control: optional object { type, ttl }`

    Create a cache control breakpoint at this content block.

    - `type: "ephemeral"`

    - `ttl: optional "5m" or "1h"`

      The time-to-live for the cache control breakpoint.

      This may be one the following values:

      - `5m`: 5 minutes
      - `1h`: 1 hour

      Defaults to `5m`.

      - `"5m"`

      - `"1h"`

### Beta Code Execution Tool Result Block Param Content

- `beta_code_execution_tool_result_block_param_content: BetaCodeExecutionToolResultErrorParam or BetaCodeExecutionResultBlockParam or BetaEncryptedCodeExecutionResultBlockParam`

  Code execution result with encrypted stdout for PFC + web_search results.

  - `beta_code_execution_tool_result_error_param: object { error_code, type }`

    - `error_code: "invalid_tool_input" or "unavailable" or "too_many_requests" or "execution_time_exceeded"`

      - `"invalid_tool_input"`

      - `"unavailable"`

      - `"too_many_requests"`

      - `"execution_time_exceeded"`

    - `type: "code_execution_tool_result_error"`

  - `beta_code_execution_result_block_param: object { content, return_code, stderr, 2 more }`

    - `content: array of BetaCodeExecutionOutputBlockParam`

      - `file_id: string`

      - `type: "code_execution_output"`

    - `return_code: number`

    - `stderr: string`

    - `stdout: string`

    - `type: "code_execution_result"`

  - `beta_encrypted_code_execution_result_block_param: object { content, encrypted_stdout, return_code, 2 more }`

    Code execution result with encrypted stdout for PFC + web_search results.

    - `content: array of BetaCodeExecutionOutputBlockParam`

      - `file_id: string`

      - `type: "code_execution_output"`

    - `encrypted_stdout: string`

    - `return_code: number`

    - `stderr: string`

    - `type: "encrypted_code_execution_result"`

### Beta Code Execution Tool Result Error

- `beta_code_execution_tool_result_error: object { error_code, type }`

  - `error_code: "invalid_tool_input" or "unavailable" or "too_many_requests" or "execution_time_exceeded"`

    - `"invalid_tool_input"`

    - `"unavailable"`

    - `"too_many_requests"`

    - `"execution_time_exceeded"`

  - `type: "code_execution_tool_result_error"`

### Beta Code Execution Tool Result Error Code

- `beta_code_execution_tool_result_error_code: "invalid_tool_input" or "unavailable" or "too_many_requests" or "execution_time_exceeded"`

  - `"invalid_tool_input"`

  - `"unavailable"`

  - `"too_many_requests"`

  - `"execution_time_exceeded"`

### Beta Code Execution Tool Result Error Param

- `beta_code_execution_tool_result_error_param: object { error_code, type }`

  - `error_code: "invalid_tool_input" or "unavailable" or "too_many_requests" or "execution_time_exceeded"`

    - `"invalid_tool_input"`

    - `"unavailable"`

    - `"too_many_requests"`

    - `"execution_time_exceeded"`

  - `type: "code_execution_tool_result_error"`

### Beta Compact 20260112 Edit

- `beta_compact_20260112_edit: object { type, instructions, pause_after_compaction, trigger }`

  Automatically compact older context when reaching the configured trigger threshold.

  - `type: "compact_20260112"`

  - `instructions: optional string`

    Additional instructions for summarization.

  - `pause_after_compaction: optional boolean`

    Whether to pause after compaction and return the compaction block to the user.

  - `trigger: optional object { type, value }`

    When to trigger compaction. Defaults to 150000 input tokens.

    - `type: "input_tokens"`

    - `value: number`

### Beta Compaction Block

- `beta_compaction_block: object { content, encrypted_content, type }`

  A compaction block returned when autocompact is triggered.

  When content is None, it indicates the compaction failed to produce a valid
  summary (e.g., malformed output from the model). Clients may round-trip
  compaction blocks with null content; the server treats them as no-ops.

  - `content: string`

    Summary of compacted content, or null if compaction failed

  - `encrypted_content: string`

    Opaque metadata from prior compaction, to be round-tripped verbatim

  - `type: "compaction"`

### Beta Compaction Block Param

- `beta_compaction_block_param: object { content, type, cache_control, encrypted_content }`

  A compaction block containing summary of previous context.

  Users should round-trip these blocks from responses to subsequent requests
  to maintain context across compaction boundaries.

  When content is None, the block represents a failed compaction. The server
  treats these as no-ops. Empty string content is not allowed.

  - `content: string`

    Summary of previously compacted content, or null if compaction failed

  - `type: "compaction"`

  - `cache_control: optional object { type, ttl }`

    Create a cache control breakpoint at this content block.

    - `type: "ephemeral"`

    - `ttl: optional "5m" or "1h"`

      The time-to-live for the cache control breakpoint.

      This may be one the following values:

      - `5m`: 5 minutes
      - `1h`: 1 hour

      Defaults to `5m`.

      - `"5m"`

      - `"1h"`

  - `encrypted_content: optional string`

    Opaque metadata from prior compaction, to be round-tripped verbatim

### Beta Compaction Content Block Delta

- `beta_compaction_content_block_delta: object { content, encrypted_content, type }`

  - `content: string`

  - `encrypted_content: string`

    Opaque metadata from prior compaction, to be round-tripped verbatim

  - `type: "compaction_delta"`

### Beta Compaction Iteration Usage

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

### Beta Container

- `beta_container: object { id, expires_at, skills }`

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

### Beta Container Params

- `beta_container_params: object { id, skills }`

  Container parameters with skills to be loaded.

  - `id: optional string`

    Container id

  - `skills: optional array of BetaSkillParams`

    List of skills to load in the container

    - `skill_id: string`

      Skill ID

    - `type: "anthropic" or "custom"`

      Type of skill - either 'anthropic' (built-in) or 'custom' (user-defined)

      - `"anthropic"`

      - `"custom"`

    - `version: optional string`

      Skill version or 'latest' for most recent version

### Beta Container Upload Block

- `beta_container_upload_block: object { file_id, type }`

  Response model for a file uploaded to the container.

  - `file_id: string`

  - `type: "container_upload"`

### Beta Container Upload Block Param

- `beta_container_upload_block_param: object { file_id, type, cache_control }`

  A content block that represents a file to be uploaded to the container
  Files uploaded via this block will be available in the container's input directory.

  - `file_id: string`

  - `type: "container_upload"`

  - `cache_control: optional object { type, ttl }`

    Create a cache control breakpoint at this content block.

    - `type: "ephemeral"`

    - `ttl: optional "5m" or "1h"`

      The time-to-live for the cache control breakpoint.

      This may be one the following values:

      - `5m`: 5 minutes
      - `1h`: 1 hour

      Defaults to `5m`.

      - `"5m"`

      - `"1h"`

### Beta Content Block

- `beta_content_block: BetaTextBlock or BetaThinkingBlock or BetaRedactedThinkingBlock or 13 more`

  Response model for a file uploaded to the container.

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

  - `beta_compaction_block: object { content, encrypted_content, type }`

    A compaction block returned when autocompact is triggered.

    When content is None, it indicates the compaction failed to produce a valid
    summary (e.g., malformed output from the model). Clients may round-trip
    compaction blocks with null content; the server treats them as no-ops.

    - `content: string`

      Summary of compacted content, or null if compaction failed

    - `encrypted_content: string`

      Opaque metadata from prior compaction, to be round-tripped verbatim

    - `type: "compaction"`

### Beta Content Block Param

- `beta_content_block_param: BetaTextBlockParam or BetaImageBlockParam or BetaRequestDocumentBlock or 17 more`

  Regular text content.

  - `beta_text_block_param: object { text, type, cache_control, citations }`

    - `text: string`

    - `type: "text"`

    - `cache_control: optional object { type, ttl }`

      Create a cache control breakpoint at this content block.

      - `type: "ephemeral"`

      - `ttl: optional "5m" or "1h"`

        The time-to-live for the cache control breakpoint.

        This may be one the following values:

        - `5m`: 5 minutes
        - `1h`: 1 hour

        Defaults to `5m`.

        - `"5m"`

        - `"1h"`

    - `citations: optional array of BetaTextCitationParam`

      - `beta_citation_char_location_param: object { cited_text, document_index, document_title, 3 more }`

        - `cited_text: string`

        - `document_index: number`

        - `document_title: string`

        - `end_char_index: number`

        - `start_char_index: number`

        - `type: "char_location"`

      - `beta_citation_page_location_param: object { cited_text, document_index, document_title, 3 more }`

        - `cited_text: string`

        - `document_index: number`

        - `document_title: string`

        - `end_page_number: number`

        - `start_page_number: number`

        - `type: "page_location"`

      - `beta_citation_content_block_location_param: object { cited_text, document_index, document_title, 3 more }`

        - `cited_text: string`

        - `document_index: number`

        - `document_title: string`

        - `end_block_index: number`

        - `start_block_index: number`

        - `type: "content_block_location"`

      - `beta_citation_web_search_result_location_param: object { cited_text, encrypted_index, title, 2 more }`

        - `cited_text: string`

        - `encrypted_index: string`

        - `title: string`

        - `type: "web_search_result_location"`

        - `url: string`

      - `beta_citation_search_result_location_param: object { cited_text, end_block_index, search_result_index, 4 more }`

        - `cited_text: string`

        - `end_block_index: number`

        - `search_result_index: number`

        - `source: string`

        - `start_block_index: number`

        - `title: string`

        - `type: "search_result_location"`

  - `beta_image_block_param: object { source, type, cache_control }`

    - `source: BetaBase64ImageSource or BetaURLImageSource or BetaFileImageSource`

      - `beta_base64_image_source: object { data, media_type, type }`

        - `data: string`

        - `media_type: "image/jpeg" or "image/png" or "image/gif" or "image/webp"`

          - `"image/jpeg"`

          - `"image/png"`

          - `"image/gif"`

          - `"image/webp"`

        - `type: "base64"`

      - `beta_url_image_source: object { type, url }`

        - `type: "url"`

        - `url: string`

      - `beta_file_image_source: object { file_id, type }`

        - `file_id: string`

        - `type: "file"`

    - `type: "image"`

    - `cache_control: optional object { type, ttl }`

      Create a cache control breakpoint at this content block.

      - `type: "ephemeral"`

      - `ttl: optional "5m" or "1h"`

        The time-to-live for the cache control breakpoint.

        This may be one the following values:

        - `5m`: 5 minutes
        - `1h`: 1 hour

        Defaults to `5m`.

        - `"5m"`

        - `"1h"`

  - `beta_request_document_block: object { source, type, cache_control, 3 more }`

    - `source: BetaBase64PDFSource or BetaPlainTextSource or BetaContentBlockSource or 2 more`

      - `beta_base64_pdf_source: object { data, media_type, type }`

        - `data: string`

        - `media_type: "application/pdf"`

        - `type: "base64"`

      - `beta_plain_text_source: object { data, media_type, type }`

        - `data: string`

        - `media_type: "text/plain"`

        - `type: "text"`

      - `beta_content_block_source: object { content, type }`

        - `content: string or array of BetaContentBlockSourceContent`

          - `union_member_0: string`

          - `beta_content_block_source_content: array of BetaContentBlockSourceContent`

            - `beta_text_block_param: object { text, type, cache_control, citations }`

              - `text: string`

              - `type: "text"`

              - `cache_control: optional object { type, ttl }`

                Create a cache control breakpoint at this content block.

                - `type: "ephemeral"`

                - `ttl: optional "5m" or "1h"`

                  The time-to-live for the cache control breakpoint.

                  This may be one the following values:

                  - `5m`: 5 minutes
                  - `1h`: 1 hour

                  Defaults to `5m`.

                  - `"5m"`

                  - `"1h"`

              - `citations: optional array of BetaTextCitationParam`

                - `beta_citation_char_location_param: object { cited_text, document_index, document_title, 3 more }`

                  - `cited_text: string`

                  - `document_index: number`

                  - `document_title: string`

                  - `end_char_index: number`

                  - `start_char_index: number`

                  - `type: "char_location"`

                - `beta_citation_page_location_param: object { cited_text, document_index, document_title, 3 more }`

                  - `cited_text: string`

                  - `document_index: number`

                  - `document_title: string`

                  - `end_page_number: number`

                  - `start_page_number: number`

                  - `type: "page_location"`

                - `beta_citation_content_block_location_param: object { cited_text, document_index, document_title, 3 more }`

                  - `cited_text: string`

                  - `document_index: number`

                  - `document_title: string`

                  - `end_block_index: number`

                  - `start_block_index: number`

                  - `type: "content_block_location"`

                - `beta_citation_web_search_result_location_param: object { cited_text, encrypted_index, title, 2 more }`

                  - `cited_text: string`

                  - `encrypted_index: string`

                  - `title: string`

                  - `type: "web_search_result_location"`

                  - `url: string`

                - `beta_citation_search_result_location_param: object { cited_text, end_block_index, search_result_index, 4 more }`

                  - `cited_text: string`

                  - `end_block_index: number`

                  - `search_result_index: number`

                  - `source: string`

                  - `start_block_index: number`

                  - `title: string`

                  - `type: "search_result_location"`

            - `beta_image_block_param: object { source, type, cache_control }`

              - `source: BetaBase64ImageSource or BetaURLImageSource or BetaFileImageSource`

                - `beta_base64_image_source: object { data, media_type, type }`

                  - `data: string`

                  - `media_type: "image/jpeg" or "image/png" or "image/gif" or "image/webp"`

                    - `"image/jpeg"`

                    - `"image/png"`

                    - `"image/gif"`

                    - `"image/webp"`

                  - `type: "base64"`

                - `beta_url_image_source: object { type, url }`

                  - `type: "url"`

                  - `url: string`

                - `beta_file_image_source: object { file_id, type }`

                  - `file_id: string`

                  - `type: "file"`

              - `type: "image"`

              - `cache_control: optional object { type, ttl }`

                Create a cache control breakpoint at this content block.

                - `type: "ephemeral"`

                - `ttl: optional "5m" or "1h"`

                  The time-to-live for the cache control breakpoint.

                  This may be one the following values:

                  - `5m`: 5 minutes
                  - `1h`: 1 hour

                  Defaults to `5m`.

                  - `"5m"`

                  - `"1h"`

        - `type: "content"`

      - `beta_url_pdf_source: object { type, url }`

        - `type: "url"`

        - `url: string`

      - `beta_file_document_source: object { file_id, type }`

        - `file_id: string`

        - `type: "file"`

    - `type: "document"`

    - `cache_control: optional object { type, ttl }`

      Create a cache control breakpoint at this content block.

      - `type: "ephemeral"`

      - `ttl: optional "5m" or "1h"`

        The time-to-live for the cache control breakpoint.

        This may be one the following values:

        - `5m`: 5 minutes
        - `1h`: 1 hour

        Defaults to `5m`.

        - `"5m"`

        - `"1h"`

    - `citations: optional object { enabled }`

      - `enabled: optional boolean`

    - `context: optional string`

    - `title: optional string`

  - `beta_search_result_block_param: object { content, source, title, 3 more }`

    - `content: array of BetaTextBlockParam`

      - `text: string`

      - `type: "text"`

      - `cache_control: optional object { type, ttl }`

        Create a cache control breakpoint at this content block.

        - `type: "ephemeral"`

        - `ttl: optional "5m" or "1h"`

          The time-to-live for the cache control breakpoint.

          This may be one the following values:

          - `5m`: 5 minutes
          - `1h`: 1 hour

          Defaults to `5m`.

          - `"5m"`

          - `"1h"`

      - `citations: optional array of BetaTextCitationParam`

        - `beta_citation_char_location_param: object { cited_text, document_index, document_title, 3 more }`

          - `cited_text: string`

          - `document_index: number`

          - `document_title: string`

          - `end_char_index: number`

          - `start_char_index: number`

          - `type: "char_location"`

        - `beta_citation_page_location_param: object { cited_text, document_index, document_title, 3 more }`

          - `cited_text: string`

          - `document_index: number`

          - `document_title: string`

          - `end_page_number: number`

          - `start_page_number: number`

          - `type: "page_location"`

        - `beta_citation_content_block_location_param: object { cited_text, document_index, document_title, 3 more }`

          - `cited_text: string`

          - `document_index: number`

          - `document_title: string`

          - `end_block_index: number`

          - `start_block_index: number`

          - `type: "content_block_location"`

        - `beta_citation_web_search_result_location_param: object { cited_text, encrypted_index, title, 2 more }`

          - `cited_text: string`

          - `encrypted_index: string`

          - `title: string`

          - `type: "web_search_result_location"`

          - `url: string`

        - `beta_citation_search_result_location_param: object { cited_text, end_block_index, search_result_index, 4 more }`

          - `cited_text: string`

          - `end_block_index: number`

          - `search_result_index: number`

          - `source: string`

          - `start_block_index: number`

          - `title: string`

          - `type: "search_result_location"`

    - `source: string`

    - `title: string`

    - `type: "search_result"`

    - `cache_control: optional object { type, ttl }`

      Create a cache control breakpoint at this content block.

      - `type: "ephemeral"`

      - `ttl: optional "5m" or "1h"`

        The time-to-live for the cache control breakpoint.

        This may be one the following values:

        - `5m`: 5 minutes
        - `1h`: 1 hour

        Defaults to `5m`.

        - `"5m"`

        - `"1h"`

    - `citations: optional object { enabled }`

      - `enabled: optional boolean`

  - `beta_thinking_block_param: object { signature, thinking, type }`

    - `signature: string`

    - `thinking: string`

    - `type: "thinking"`

  - `beta_redacted_thinking_block_param: object { data, type }`

    - `data: string`

    - `type: "redacted_thinking"`

  - `beta_tool_use_block_param: object { id, input, name, 3 more }`

    - `id: string`

    - `input: map[unknown]`

    - `name: string`

    - `type: "tool_use"`

    - `cache_control: optional object { type, ttl }`

      Create a cache control breakpoint at this content block.

      - `type: "ephemeral"`

      - `ttl: optional "5m" or "1h"`

        The time-to-live for the cache control breakpoint.

        This may be one the following values:

        - `5m`: 5 minutes
        - `1h`: 1 hour

        Defaults to `5m`.

        - `"5m"`

        - `"1h"`

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

  - `beta_tool_result_block_param: object { tool_use_id, type, cache_control, 2 more }`

    - `tool_use_id: string`

    - `type: "tool_result"`

    - `cache_control: optional object { type, ttl }`

      Create a cache control breakpoint at this content block.

      - `type: "ephemeral"`

      - `ttl: optional "5m" or "1h"`

        The time-to-live for the cache control breakpoint.

        This may be one the following values:

        - `5m`: 5 minutes
        - `1h`: 1 hour

        Defaults to `5m`.

        - `"5m"`

        - `"1h"`

    - `content: optional array of BetaTextBlockParam or BetaImageBlockParam or BetaSearchResultBlockParam or 2 more`

      - `beta_text_block_param: object { text, type, cache_control, citations }`

        - `text: string`

        - `type: "text"`

        - `cache_control: optional object { type, ttl }`

          Create a cache control breakpoint at this content block.

          - `type: "ephemeral"`

          - `ttl: optional "5m" or "1h"`

            The time-to-live for the cache control breakpoint.

            This may be one the following values:

            - `5m`: 5 minutes
            - `1h`: 1 hour

            Defaults to `5m`.

            - `"5m"`

            - `"1h"`

        - `citations: optional array of BetaTextCitationParam`

          - `beta_citation_char_location_param: object { cited_text, document_index, document_title, 3 more }`

            - `cited_text: string`

            - `document_index: number`

            - `document_title: string`

            - `end_char_index: number`

            - `start_char_index: number`

            - `type: "char_location"`

          - `beta_citation_page_location_param: object { cited_text, document_index, document_title, 3 more }`

            - `cited_text: string`

            - `document_index: number`

            - `document_title: string`

            - `end_page_number: number`

            - `start_page_number: number`

            - `type: "page_location"`

          - `beta_citation_content_block_location_param: object { cited_text, document_index, document_title, 3 more }`

            - `cited_text: string`

            - `document_index: number`

            - `document_title: string`

            - `end_block_index: number`

            - `start_block_index: number`

            - `type: "content_block_location"`

          - `beta_citation_web_search_result_location_param: object { cited_text, encrypted_index, title, 2 more }`

            - `cited_text: string`

            - `encrypted_index: string`

            - `title: string`

            - `type: "web_search_result_location"`

            - `url: string`

          - `beta_citation_search_result_location_param: object { cited_text, end_block_index, search_result_index, 4 more }`

            - `cited_text: string`

            - `end_block_index: number`

            - `search_result_index: number`

            - `source: string`

            - `start_block_index: number`

            - `title: string`

            - `type: "search_result_location"`

      - `beta_image_block_param: object { source, type, cache_control }`

        - `source: BetaBase64ImageSource or BetaURLImageSource or BetaFileImageSource`

          - `beta_base64_image_source: object { data, media_type, type }`

            - `data: string`

            - `media_type: "image/jpeg" or "image/png" or "image/gif" or "image/webp"`

              - `"image/jpeg"`

              - `"image/png"`

              - `"image/gif"`

              - `"image/webp"`

            - `type: "base64"`

          - `beta_url_image_source: object { type, url }`

            - `type: "url"`

            - `url: string`

          - `beta_file_image_source: object { file_id, type }`

            - `file_id: string`

            - `type: "file"`

        - `type: "image"`

        - `cache_control: optional object { type, ttl }`

          Create a cache control breakpoint at this content block.

          - `type: "ephemeral"`

          - `ttl: optional "5m" or "1h"`

            The time-to-live for the cache control breakpoint.

            This may be one the following values:

            - `5m`: 5 minutes
            - `1h`: 1 hour

            Defaults to `5m`.

            - `"5m"`

            - `"1h"`

      - `beta_search_result_block_param: object { content, source, title, 3 more }`

        - `content: array of BetaTextBlockParam`

          - `text: string`

          - `type: "text"`

          - `cache_control: optional object { type, ttl }`

            Create a cache control breakpoint at this content block.

            - `type: "ephemeral"`

            - `ttl: optional "5m" or "1h"`

              The time-to-live for the cache control breakpoint.

              This may be one the following values:

              - `5m`: 5 minutes
              - `1h`: 1 hour

              Defaults to `5m`.

              - `"5m"`

              - `"1h"`

          - `citations: optional array of BetaTextCitationParam`

            - `beta_citation_char_location_param: object { cited_text, document_index, document_title, 3 more }`

              - `cited_text: string`

              - `document_index: number`

              - `document_title: string`

              - `end_char_index: number`

              - `start_char_index: number`

              - `type: "char_location"`

            - `beta_citation_page_location_param: object { cited_text, document_index, document_title, 3 more }`

              - `cited_text: string`

              - `document_index: number`

              - `document_title: string`

              - `end_page_number: number`

              - `start_page_number: number`

              - `type: "page_location"`

            - `beta_citation_content_block_location_param: object { cited_text, document_index, document_title, 3 more }`

              - `cited_text: string`

              - `document_index: number`

              - `document_title: string`

              - `end_block_index: number`

              - `start_block_index: number`

              - `type: "content_block_location"`

            - `beta_citation_web_search_result_location_param: object { cited_text, encrypted_index, title, 2 more }`

              - `cited_text: string`

              - `encrypted_index: string`

              - `title: string`

              - `type: "web_search_result_location"`

              - `url: string`

            - `beta_citation_search_result_location_param: object { cited_text, end_block_index, search_result_index, 4 more }`

              - `cited_text: string`

              - `end_block_index: number`

              - `search_result_index: number`

              - `source: string`

              - `start_block_index: number`

              - `title: string`

              - `type: "search_result_location"`

        - `source: string`

        - `title: string`

        - `type: "search_result"`

        - `cache_control: optional object { type, ttl }`

          Create a cache control breakpoint at this content block.

          - `type: "ephemeral"`

          - `ttl: optional "5m" or "1h"`

            The time-to-live for the cache control breakpoint.

            This may be one the following values:

            - `5m`: 5 minutes
            - `1h`: 1 hour

            Defaults to `5m`.

            - `"5m"`

            - `"1h"`

        - `citations: optional object { enabled }`

          - `enabled: optional boolean`

      - `beta_request_document_block: object { source, type, cache_control, 3 more }`

        - `source: BetaBase64PDFSource or BetaPlainTextSource or BetaContentBlockSource or 2 more`

          - `beta_base64_pdf_source: object { data, media_type, type }`

            - `data: string`

            - `media_type: "application/pdf"`

            - `type: "base64"`

          - `beta_plain_text_source: object { data, media_type, type }`

            - `data: string`

            - `media_type: "text/plain"`

            - `type: "text"`

          - `beta_content_block_source: object { content, type }`

            - `content: string or array of BetaContentBlockSourceContent`

              - `union_member_0: string`

              - `beta_content_block_source_content: array of BetaContentBlockSourceContent`

                - `beta_text_block_param: object { text, type, cache_control, citations }`

                  - `text: string`

                  - `type: "text"`

                  - `cache_control: optional object { type, ttl }`

                    Create a cache control breakpoint at this content block.

                    - `type: "ephemeral"`

                    - `ttl: optional "5m" or "1h"`

                      The time-to-live for the cache control breakpoint.

                      This may be one the following values:

                      - `5m`: 5 minutes
                      - `1h`: 1 hour

                      Defaults to `5m`.

                      - `"5m"`

                      - `"1h"`

                  - `citations: optional array of BetaTextCitationParam`

                    - `beta_citation_char_location_param: object { cited_text, document_index, document_title, 3 more }`

                      - `cited_text: string`

                      - `document_index: number`

                      - `document_title: string`

                      - `end_char_index: number`

                      - `start_char_index: number`

                      - `type: "char_location"`

                    - `beta_citation_page_location_param: object { cited_text, document_index, document_title, 3 more }`

                      - `cited_text: string`

                      - `document_index: number`

                      - `document_title: string`

                      - `end_page_number: number`

                      - `start_page_number: number`

                      - `type: "page_location"`

                    - `beta_citation_content_block_location_param: object { cited_text, document_index, document_title, 3 more }`

                      - `cited_text: string`

                      - `document_index: number`

                      - `document_title: string`

                      - `end_block_index: number`

                      - `start_block_index: number`

                      - `type: "content_block_location"`

                    - `beta_citation_web_search_result_location_param: object { cited_text, encrypted_index, title, 2 more }`

                      - `cited_text: string`

                      - `encrypted_index: string`

                      - `title: string`

                      - `type: "web_search_result_location"`

                      - `url: string`

                    - `beta_citation_search_result_location_param: object { cited_text, end_block_index, search_result_index, 4 more }`

                      - `cited_text: string`

                      - `end_block_index: number`

                      - `search_result_index: number`

                      - `source: string`

                      - `start_block_index: number`

                      - `title: string`

                      - `type: "search_result_location"`

                - `beta_image_block_param: object { source, type, cache_control }`

                  - `source: BetaBase64ImageSource or BetaURLImageSource or BetaFileImageSource`

                    - `beta_base64_image_source: object { data, media_type, type }`

                      - `data: string`

                      - `media_type: "image/jpeg" or "image/png" or "image/gif" or "image/webp"`

                        - `"image/jpeg"`

                        - `"image/png"`

                        - `"image/gif"`

                        - `"image/webp"`

                      - `type: "base64"`

                    - `beta_url_image_source: object { type, url }`

                      - `type: "url"`

                      - `url: string`

                    - `beta_file_image_source: object { file_id, type }`

                      - `file_id: string`

                      - `type: "file"`

                  - `type: "image"`

                  - `cache_control: optional object { type, ttl }`

                    Create a cache control breakpoint at this content block.

                    - `type: "ephemeral"`

                    - `ttl: optional "5m" or "1h"`

                      The time-to-live for the cache control breakpoint.

                      This may be one the following values:

                      - `5m`: 5 minutes
                      - `1h`: 1 hour

                      Defaults to `5m`.

                      - `"5m"`

                      - `"1h"`

            - `type: "content"`

          - `beta_url_pdf_source: object { type, url }`

            - `type: "url"`

            - `url: string`

          - `beta_file_document_source: object { file_id, type }`

            - `file_id: string`

            - `type: "file"`

        - `type: "document"`

        - `cache_control: optional object { type, ttl }`

          Create a cache control breakpoint at this content block.

          - `type: "ephemeral"`

          - `ttl: optional "5m" or "1h"`

            The time-to-live for the cache control breakpoint.

            This may be one the following values:

            - `5m`: 5 minutes
            - `1h`: 1 hour

            Defaults to `5m`.

            - `"5m"`

            - `"1h"`

        - `citations: optional object { enabled }`

          - `enabled: optional boolean`

        - `context: optional string`

        - `title: optional string`

      - `beta_tool_reference_block_param: object { tool_name, type, cache_control }`

        Tool reference block that can be included in tool_result content.

        - `tool_name: string`

        - `type: "tool_reference"`

        - `cache_control: optional object { type, ttl }`

          Create a cache control breakpoint at this content block.

          - `type: "ephemeral"`

          - `ttl: optional "5m" or "1h"`

            The time-to-live for the cache control breakpoint.

            This may be one the following values:

            - `5m`: 5 minutes
            - `1h`: 1 hour

            Defaults to `5m`.

            - `"5m"`

            - `"1h"`

    - `is_error: optional boolean`

  - `beta_server_tool_use_block_param: object { id, input, name, 3 more }`

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

    - `cache_control: optional object { type, ttl }`

      Create a cache control breakpoint at this content block.

      - `type: "ephemeral"`

      - `ttl: optional "5m" or "1h"`

        The time-to-live for the cache control breakpoint.

        This may be one the following values:

        - `5m`: 5 minutes
        - `1h`: 1 hour

        Defaults to `5m`.

        - `"5m"`

        - `"1h"`

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

  - `beta_web_search_tool_result_block_param: object { content, tool_use_id, type, 2 more }`

    - `content: array of BetaWebSearchResultBlockParam or BetaWebSearchToolRequestError`

      - `Result Block: array of BetaWebSearchResultBlockParam`

        - `encrypted_content: string`

        - `title: string`

        - `type: "web_search_result"`

        - `url: string`

        - `page_age: optional string`

      - `beta_web_search_tool_request_error: object { error_code, type }`

        - `error_code: "invalid_tool_input" or "unavailable" or "max_uses_exceeded" or 3 more`

          - `"invalid_tool_input"`

          - `"unavailable"`

          - `"max_uses_exceeded"`

          - `"too_many_requests"`

          - `"query_too_long"`

          - `"request_too_large"`

        - `type: "web_search_tool_result_error"`

    - `tool_use_id: string`

    - `type: "web_search_tool_result"`

    - `cache_control: optional object { type, ttl }`

      Create a cache control breakpoint at this content block.

      - `type: "ephemeral"`

      - `ttl: optional "5m" or "1h"`

        The time-to-live for the cache control breakpoint.

        This may be one the following values:

        - `5m`: 5 minutes
        - `1h`: 1 hour

        Defaults to `5m`.

        - `"5m"`

        - `"1h"`

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

  - `beta_web_fetch_tool_result_block_param: object { content, tool_use_id, type, 2 more }`

    - `content: BetaWebFetchToolResultErrorBlockParam or BetaWebFetchBlockParam`

      - `beta_web_fetch_tool_result_error_block_param: object { error_code, type }`

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

      - `beta_web_fetch_block_param: object { content, type, url, retrieved_at }`

        - `content: object { source, type, cache_control, 3 more }`

          - `source: BetaBase64PDFSource or BetaPlainTextSource or BetaContentBlockSource or 2 more`

            - `beta_base64_pdf_source: object { data, media_type, type }`

              - `data: string`

              - `media_type: "application/pdf"`

              - `type: "base64"`

            - `beta_plain_text_source: object { data, media_type, type }`

              - `data: string`

              - `media_type: "text/plain"`

              - `type: "text"`

            - `beta_content_block_source: object { content, type }`

              - `content: string or array of BetaContentBlockSourceContent`

                - `union_member_0: string`

                - `beta_content_block_source_content: array of BetaContentBlockSourceContent`

                  - `beta_text_block_param: object { text, type, cache_control, citations }`

                    - `text: string`

                    - `type: "text"`

                    - `cache_control: optional object { type, ttl }`

                      Create a cache control breakpoint at this content block.

                      - `type: "ephemeral"`

                      - `ttl: optional "5m" or "1h"`

                        The time-to-live for the cache control breakpoint.

                        This may be one the following values:

                        - `5m`: 5 minutes
                        - `1h`: 1 hour

                        Defaults to `5m`.

                        - `"5m"`

                        - `"1h"`

                    - `citations: optional array of BetaTextCitationParam`

                      - `beta_citation_char_location_param: object { cited_text, document_index, document_title, 3 more }`

                        - `cited_text: string`

                        - `document_index: number`

                        - `document_title: string`

                        - `end_char_index: number`

                        - `start_char_index: number`

                        - `type: "char_location"`

                      - `beta_citation_page_location_param: object { cited_text, document_index, document_title, 3 more }`

                        - `cited_text: string`

                        - `document_index: number`

                        - `document_title: string`

                        - `end_page_number: number`

                        - `start_page_number: number`

                        - `type: "page_location"`

                      - `beta_citation_content_block_location_param: object { cited_text, document_index, document_title, 3 more }`

                        - `cited_text: string`

                        - `document_index: number`

                        - `document_title: string`

                        - `end_block_index: number`

                        - `start_block_index: number`

                        - `type: "content_block_location"`

                      - `beta_citation_web_search_result_location_param: object { cited_text, encrypted_index, title, 2 more }`

                        - `cited_text: string`

                        - `encrypted_index: string`

                        - `title: string`

                        - `type: "web_search_result_location"`

                        - `url: string`

                      - `beta_citation_search_result_location_param: object { cited_text, end_block_index, search_result_index, 4 more }`

                        - `cited_text: string`

                        - `end_block_index: number`

                        - `search_result_index: number`

                        - `source: string`

                        - `start_block_index: number`

                        - `title: string`

                        - `type: "search_result_location"`

                  - `beta_image_block_param: object { source, type, cache_control }`

                    - `source: BetaBase64ImageSource or BetaURLImageSource or BetaFileImageSource`

                      - `beta_base64_image_source: object { data, media_type, type }`

                        - `data: string`

                        - `media_type: "image/jpeg" or "image/png" or "image/gif" or "image/webp"`

                          - `"image/jpeg"`

                          - `"image/png"`

                          - `"image/gif"`

                          - `"image/webp"`

                        - `type: "base64"`

                      - `beta_url_image_source: object { type, url }`

                        - `type: "url"`

                        - `url: string`

                      - `beta_file_image_source: object { file_id, type }`

                        - `file_id: string`

                        - `type: "file"`

                    - `type: "image"`

                    - `cache_control: optional object { type, ttl }`

                      Create a cache control breakpoint at this content block.

                      - `type: "ephemeral"`

                      - `ttl: optional "5m" or "1h"`

                        The time-to-live for the cache control breakpoint.

                        This may be one the following values:

                        - `5m`: 5 minutes
                        - `1h`: 1 hour

                        Defaults to `5m`.

                        - `"5m"`

                        - `"1h"`

              - `type: "content"`

            - `beta_url_pdf_source: object { type, url }`

              - `type: "url"`

              - `url: string`

            - `beta_file_document_source: object { file_id, type }`

              - `file_id: string`

              - `type: "file"`

          - `type: "document"`

          - `cache_control: optional object { type, ttl }`

            Create a cache control breakpoint at this content block.

            - `type: "ephemeral"`

            - `ttl: optional "5m" or "1h"`

              The time-to-live for the cache control breakpoint.

              This may be one the following values:

              - `5m`: 5 minutes
              - `1h`: 1 hour

              Defaults to `5m`.

              - `"5m"`

              - `"1h"`

          - `citations: optional object { enabled }`

            - `enabled: optional boolean`

          - `context: optional string`

          - `title: optional string`

        - `type: "web_fetch_result"`

        - `url: string`

          Fetched content URL

        - `retrieved_at: optional string`

          ISO 8601 timestamp when the content was retrieved

    - `tool_use_id: string`

    - `type: "web_fetch_tool_result"`

    - `cache_control: optional object { type, ttl }`

      Create a cache control breakpoint at this content block.

      - `type: "ephemeral"`

      - `ttl: optional "5m" or "1h"`

        The time-to-live for the cache control breakpoint.

        This may be one the following values:

        - `5m`: 5 minutes
        - `1h`: 1 hour

        Defaults to `5m`.

        - `"5m"`

        - `"1h"`

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

  - `beta_advisor_tool_result_block_param: object { content, tool_use_id, type, cache_control }`

    - `content: BetaAdvisorToolResultErrorParam or BetaAdvisorResultBlockParam or BetaAdvisorRedactedResultBlockParam`

      - `beta_advisor_tool_result_error_param: object { error_code, type }`

        - `error_code: "max_uses_exceeded" or "prompt_too_long" or "too_many_requests" or 3 more`

          - `"max_uses_exceeded"`

          - `"prompt_too_long"`

          - `"too_many_requests"`

          - `"overloaded"`

          - `"unavailable"`

          - `"execution_time_exceeded"`

        - `type: "advisor_tool_result_error"`

      - `beta_advisor_result_block_param: object { text, type }`

        - `text: string`

        - `type: "advisor_result"`

      - `beta_advisor_redacted_result_block_param: object { encrypted_content, type }`

        - `encrypted_content: string`

          Opaque blob produced by a prior response; must be round-tripped verbatim.

        - `type: "advisor_redacted_result"`

    - `tool_use_id: string`

    - `type: "advisor_tool_result"`

    - `cache_control: optional object { type, ttl }`

      Create a cache control breakpoint at this content block.

      - `type: "ephemeral"`

      - `ttl: optional "5m" or "1h"`

        The time-to-live for the cache control breakpoint.

        This may be one the following values:

        - `5m`: 5 minutes
        - `1h`: 1 hour

        Defaults to `5m`.

        - `"5m"`

        - `"1h"`

  - `beta_code_execution_tool_result_block_param: object { content, tool_use_id, type, cache_control }`

    - `content: BetaCodeExecutionToolResultErrorParam or BetaCodeExecutionResultBlockParam or BetaEncryptedCodeExecutionResultBlockParam`

      Code execution result with encrypted stdout for PFC + web_search results.

      - `beta_code_execution_tool_result_error_param: object { error_code, type }`

        - `error_code: "invalid_tool_input" or "unavailable" or "too_many_requests" or "execution_time_exceeded"`

          - `"invalid_tool_input"`

          - `"unavailable"`

          - `"too_many_requests"`

          - `"execution_time_exceeded"`

        - `type: "code_execution_tool_result_error"`

      - `beta_code_execution_result_block_param: object { content, return_code, stderr, 2 more }`

        - `content: array of BetaCodeExecutionOutputBlockParam`

          - `file_id: string`

          - `type: "code_execution_output"`

        - `return_code: number`

        - `stderr: string`

        - `stdout: string`

        - `type: "code_execution_result"`

      - `beta_encrypted_code_execution_result_block_param: object { content, encrypted_stdout, return_code, 2 more }`

        Code execution result with encrypted stdout for PFC + web_search results.

        - `content: array of BetaCodeExecutionOutputBlockParam`

          - `file_id: string`

          - `type: "code_execution_output"`

        - `encrypted_stdout: string`

        - `return_code: number`

        - `stderr: string`

        - `type: "encrypted_code_execution_result"`

    - `tool_use_id: string`

    - `type: "code_execution_tool_result"`

    - `cache_control: optional object { type, ttl }`

      Create a cache control breakpoint at this content block.

      - `type: "ephemeral"`

      - `ttl: optional "5m" or "1h"`

        The time-to-live for the cache control breakpoint.

        This may be one the following values:

        - `5m`: 5 minutes
        - `1h`: 1 hour

        Defaults to `5m`.

        - `"5m"`

        - `"1h"`

  - `beta_bash_code_execution_tool_result_block_param: object { content, tool_use_id, type, cache_control }`

    - `content: BetaBashCodeExecutionToolResultErrorParam or BetaBashCodeExecutionResultBlockParam`

      - `beta_bash_code_execution_tool_result_error_param: object { error_code, type }`

        - `error_code: "invalid_tool_input" or "unavailable" or "too_many_requests" or 2 more`

          - `"invalid_tool_input"`

          - `"unavailable"`

          - `"too_many_requests"`

          - `"execution_time_exceeded"`

          - `"output_file_too_large"`

        - `type: "bash_code_execution_tool_result_error"`

      - `beta_bash_code_execution_result_block_param: object { content, return_code, stderr, 2 more }`

        - `content: array of BetaBashCodeExecutionOutputBlockParam`

          - `file_id: string`

          - `type: "bash_code_execution_output"`

        - `return_code: number`

        - `stderr: string`

        - `stdout: string`

        - `type: "bash_code_execution_result"`

    - `tool_use_id: string`

    - `type: "bash_code_execution_tool_result"`

    - `cache_control: optional object { type, ttl }`

      Create a cache control breakpoint at this content block.

      - `type: "ephemeral"`

      - `ttl: optional "5m" or "1h"`

        The time-to-live for the cache control breakpoint.

        This may be one the following values:

        - `5m`: 5 minutes
        - `1h`: 1 hour

        Defaults to `5m`.

        - `"5m"`

        - `"1h"`

  - `beta_text_editor_code_execution_tool_result_block_param: object { content, tool_use_id, type, cache_control }`

    - `content: BetaTextEditorCodeExecutionToolResultErrorParam or BetaTextEditorCodeExecutionViewResultBlockParam or BetaTextEditorCodeExecutionCreateResultBlockParam or BetaTextEditorCodeExecutionStrReplaceResultBlockParam`

      - `beta_text_editor_code_execution_tool_result_error_param: object { error_code, type, error_message }`

        - `error_code: "invalid_tool_input" or "unavailable" or "too_many_requests" or 2 more`

          - `"invalid_tool_input"`

          - `"unavailable"`

          - `"too_many_requests"`

          - `"execution_time_exceeded"`

          - `"file_not_found"`

        - `type: "text_editor_code_execution_tool_result_error"`

        - `error_message: optional string`

      - `beta_text_editor_code_execution_view_result_block_param: object { content, file_type, type, 3 more }`

        - `content: string`

        - `file_type: "text" or "image" or "pdf"`

          - `"text"`

          - `"image"`

          - `"pdf"`

        - `type: "text_editor_code_execution_view_result"`

        - `num_lines: optional number`

        - `start_line: optional number`

        - `total_lines: optional number`

      - `beta_text_editor_code_execution_create_result_block_param: object { is_file_update, type }`

        - `is_file_update: boolean`

        - `type: "text_editor_code_execution_create_result"`

      - `beta_text_editor_code_execution_str_replace_result_block_param: object { type, lines, new_lines, 3 more }`

        - `type: "text_editor_code_execution_str_replace_result"`

        - `lines: optional array of string`

        - `new_lines: optional number`

        - `new_start: optional number`

        - `old_lines: optional number`

        - `old_start: optional number`

    - `tool_use_id: string`

    - `type: "text_editor_code_execution_tool_result"`

    - `cache_control: optional object { type, ttl }`

      Create a cache control breakpoint at this content block.

      - `type: "ephemeral"`

      - `ttl: optional "5m" or "1h"`

        The time-to-live for the cache control breakpoint.

        This may be one the following values:

        - `5m`: 5 minutes
        - `1h`: 1 hour

        Defaults to `5m`.

        - `"5m"`

        - `"1h"`

  - `beta_tool_search_tool_result_block_param: object { content, tool_use_id, type, cache_control }`

    - `content: BetaToolSearchToolResultErrorParam or BetaToolSearchToolSearchResultBlockParam`

      - `beta_tool_search_tool_result_error_param: object { error_code, type }`

        - `error_code: "invalid_tool_input" or "unavailable" or "too_many_requests" or "execution_time_exceeded"`

          - `"invalid_tool_input"`

          - `"unavailable"`

          - `"too_many_requests"`

          - `"execution_time_exceeded"`

        - `type: "tool_search_tool_result_error"`

      - `beta_tool_search_tool_search_result_block_param: object { tool_references, type }`

        - `tool_references: array of BetaToolReferenceBlockParam`

          - `tool_name: string`

          - `type: "tool_reference"`

          - `cache_control: optional object { type, ttl }`

            Create a cache control breakpoint at this content block.

            - `type: "ephemeral"`

            - `ttl: optional "5m" or "1h"`

              The time-to-live for the cache control breakpoint.

              This may be one the following values:

              - `5m`: 5 minutes
              - `1h`: 1 hour

              Defaults to `5m`.

              - `"5m"`

              - `"1h"`

        - `type: "tool_search_tool_search_result"`

    - `tool_use_id: string`

    - `type: "tool_search_tool_result"`

    - `cache_control: optional object { type, ttl }`

      Create a cache control breakpoint at this content block.

      - `type: "ephemeral"`

      - `ttl: optional "5m" or "1h"`

        The time-to-live for the cache control breakpoint.

        This may be one the following values:

        - `5m`: 5 minutes
        - `1h`: 1 hour

        Defaults to `5m`.

        - `"5m"`

        - `"1h"`

  - `beta_mcp_tool_use_block_param: object { id, input, name, 3 more }`

    - `id: string`

    - `input: map[unknown]`

    - `name: string`

    - `server_name: string`

      The name of the MCP server

    - `type: "mcp_tool_use"`

    - `cache_control: optional object { type, ttl }`

      Create a cache control breakpoint at this content block.

      - `type: "ephemeral"`

      - `ttl: optional "5m" or "1h"`

        The time-to-live for the cache control breakpoint.

        This may be one the following values:

        - `5m`: 5 minutes
        - `1h`: 1 hour

        Defaults to `5m`.

        - `"5m"`

        - `"1h"`

  - `beta_request_mcp_tool_result_block_param: object { tool_use_id, type, cache_control, 2 more }`

    - `tool_use_id: string`

    - `type: "mcp_tool_result"`

    - `cache_control: optional object { type, ttl }`

      Create a cache control breakpoint at this content block.

      - `type: "ephemeral"`

      - `ttl: optional "5m" or "1h"`

        The time-to-live for the cache control breakpoint.

        This may be one the following values:

        - `5m`: 5 minutes
        - `1h`: 1 hour

        Defaults to `5m`.

        - `"5m"`

        - `"1h"`

    - `content: optional string or array of BetaTextBlockParam`

      - `union_member_0: string`

      - `beta_mcp_tool_result_block_param_content: array of BetaTextBlockParam`

        - `text: string`

        - `type: "text"`

        - `cache_control: optional object { type, ttl }`

          Create a cache control breakpoint at this content block.

          - `type: "ephemeral"`

          - `ttl: optional "5m" or "1h"`

            The time-to-live for the cache control breakpoint.

            This may be one the following values:

            - `5m`: 5 minutes
            - `1h`: 1 hour

            Defaults to `5m`.

            - `"5m"`

            - `"1h"`

        - `citations: optional array of BetaTextCitationParam`

          - `beta_citation_char_location_param: object { cited_text, document_index, document_title, 3 more }`

            - `cited_text: string`

            - `document_index: number`

            - `document_title: string`

            - `end_char_index: number`

            - `start_char_index: number`

            - `type: "char_location"`

          - `beta_citation_page_location_param: object { cited_text, document_index, document_title, 3 more }`

            - `cited_text: string`

            - `document_index: number`

            - `document_title: string`

            - `end_page_number: number`

            - `start_page_number: number`

            - `type: "page_location"`

          - `beta_citation_content_block_location_param: object { cited_text, document_index, document_title, 3 more }`

            - `cited_text: string`

            - `document_index: number`

            - `document_title: string`

            - `end_block_index: number`

            - `start_block_index: number`

            - `type: "content_block_location"`

          - `beta_citation_web_search_result_location_param: object { cited_text, encrypted_index, title, 2 more }`

            - `cited_text: string`

            - `encrypted_index: string`

            - `title: string`

            - `type: "web_search_result_location"`

            - `url: string`

          - `beta_citation_search_result_location_param: object { cited_text, end_block_index, search_result_index, 4 more }`

            - `cited_text: string`

            - `end_block_index: number`

            - `search_result_index: number`

            - `source: string`

            - `start_block_index: number`

            - `title: string`

            - `type: "search_result_location"`

    - `is_error: optional boolean`

  - `beta_container_upload_block_param: object { file_id, type, cache_control }`

    A content block that represents a file to be uploaded to the container
    Files uploaded via this block will be available in the container's input directory.

    - `file_id: string`

    - `type: "container_upload"`

    - `cache_control: optional object { type, ttl }`

      Create a cache control breakpoint at this content block.

      - `type: "ephemeral"`

      - `ttl: optional "5m" or "1h"`

        The time-to-live for the cache control breakpoint.

        This may be one the following values:

        - `5m`: 5 minutes
        - `1h`: 1 hour

        Defaults to `5m`.

        - `"5m"`

        - `"1h"`

  - `beta_compaction_block_param: object { content, type, cache_control, encrypted_content }`

    A compaction block containing summary of previous context.

    Users should round-trip these blocks from responses to subsequent requests
    to maintain context across compaction boundaries.

    When content is None, the block represents a failed compaction. The server
    treats these as no-ops. Empty string content is not allowed.

    - `content: string`

      Summary of previously compacted content, or null if compaction failed

    - `type: "compaction"`

    - `cache_control: optional object { type, ttl }`

      Create a cache control breakpoint at this content block.

      - `type: "ephemeral"`

      - `ttl: optional "5m" or "1h"`

        The time-to-live for the cache control breakpoint.

        This may be one the following values:

        - `5m`: 5 minutes
        - `1h`: 1 hour

        Defaults to `5m`.

        - `"5m"`

        - `"1h"`

    - `encrypted_content: optional string`

      Opaque metadata from prior compaction, to be round-tripped verbatim

### Beta Content Block Source

- `beta_content_block_source: object { content, type }`

  - `content: string or array of BetaContentBlockSourceContent`

    - `union_member_0: string`

    - `beta_content_block_source_content: array of BetaContentBlockSourceContent`

      - `beta_text_block_param: object { text, type, cache_control, citations }`

        - `text: string`

        - `type: "text"`

        - `cache_control: optional object { type, ttl }`

          Create a cache control breakpoint at this content block.

          - `type: "ephemeral"`

          - `ttl: optional "5m" or "1h"`

            The time-to-live for the cache control breakpoint.

            This may be one the following values:

            - `5m`: 5 minutes
            - `1h`: 1 hour

            Defaults to `5m`.

            - `"5m"`

            - `"1h"`

        - `citations: optional array of BetaTextCitationParam`

          - `beta_citation_char_location_param: object { cited_text, document_index, document_title, 3 more }`

            - `cited_text: string`

            - `document_index: number`

            - `document_title: string`

            - `end_char_index: number`

            - `start_char_index: number`

            - `type: "char_location"`

          - `beta_citation_page_location_param: object { cited_text, document_index, document_title, 3 more }`

            - `cited_text: string`

            - `document_index: number`

            - `document_title: string`

            - `end_page_number: number`

            - `start_page_number: number`

            - `type: "page_location"`

          - `beta_citation_content_block_location_param: object { cited_text, document_index, document_title, 3 more }`

            - `cited_text: string`

            - `document_index: number`

            - `document_title: string`

            - `end_block_index: number`

            - `start_block_index: number`

            - `type: "content_block_location"`

          - `beta_citation_web_search_result_location_param: object { cited_text, encrypted_index, title, 2 more }`

            - `cited_text: string`

            - `encrypted_index: string`

            - `title: string`

            - `type: "web_search_result_location"`

            - `url: string`

          - `beta_citation_search_result_location_param: object { cited_text, end_block_index, search_result_index, 4 more }`

            - `cited_text: string`

            - `end_block_index: number`

            - `search_result_index: number`

            - `source: string`

            - `start_block_index: number`

            - `title: string`

            - `type: "search_result_location"`

      - `beta_image_block_param: object { source, type, cache_control }`

        - `source: BetaBase64ImageSource or BetaURLImageSource or BetaFileImageSource`

          - `beta_base64_image_source: object { data, media_type, type }`

            - `data: string`

            - `media_type: "image/jpeg" or "image/png" or "image/gif" or "image/webp"`

              - `"image/jpeg"`

              - `"image/png"`

              - `"image/gif"`

              - `"image/webp"`

            - `type: "base64"`

          - `beta_url_image_source: object { type, url }`

            - `type: "url"`

            - `url: string`

          - `beta_file_image_source: object { file_id, type }`

            - `file_id: string`

            - `type: "file"`

        - `type: "image"`

        - `cache_control: optional object { type, ttl }`

          Create a cache control breakpoint at this content block.

          - `type: "ephemeral"`

          - `ttl: optional "5m" or "1h"`

            The time-to-live for the cache control breakpoint.

            This may be one the following values:

            - `5m`: 5 minutes
            - `1h`: 1 hour

            Defaults to `5m`.

            - `"5m"`

            - `"1h"`

  - `type: "content"`

### Beta Content Block Source Content

- `beta_content_block_source_content: BetaTextBlockParam or BetaImageBlockParam`

  - `beta_text_block_param: object { text, type, cache_control, citations }`

    - `text: string`

    - `type: "text"`

    - `cache_control: optional object { type, ttl }`

      Create a cache control breakpoint at this content block.

      - `type: "ephemeral"`

      - `ttl: optional "5m" or "1h"`

        The time-to-live for the cache control breakpoint.

        This may be one the following values:

        - `5m`: 5 minutes
        - `1h`: 1 hour

        Defaults to `5m`.

        - `"5m"`

        - `"1h"`

    - `citations: optional array of BetaTextCitationParam`

      - `beta_citation_char_location_param: object { cited_text, document_index, document_title, 3 more }`

        - `cited_text: string`

        - `document_index: number`

        - `document_title: string`

        - `end_char_index: number`

        - `start_char_index: number`

        - `type: "char_location"`

      - `beta_citation_page_location_param: object { cited_text, document_index, document_title, 3 more }`

        - `cited_text: string`

        - `document_index: number`

        - `document_title: string`

        - `end_page_number: number`

        - `start_page_number: number`

        - `type: "page_location"`

      - `beta_citation_content_block_location_param: object { cited_text, document_index, document_title, 3 more }`

        - `cited_text: string`

        - `document_index: number`

        - `document_title: string`

        - `end_block_index: number`

        - `start_block_index: number`

        - `type: "content_block_location"`

      - `beta_citation_web_search_result_location_param: object { cited_text, encrypted_index, title, 2 more }`

        - `cited_text: string`

        - `encrypted_index: string`

        - `title: string`

        - `type: "web_search_result_location"`

        - `url: string`

      - `beta_citation_search_result_location_param: object { cited_text, end_block_index, search_result_index, 4 more }`

        - `cited_text: string`

        - `end_block_index: number`

        - `search_result_index: number`

        - `source: string`

        - `start_block_index: number`

        - `title: string`

        - `type: "search_result_location"`

  - `beta_image_block_param: object { source, type, cache_control }`

    - `source: BetaBase64ImageSource or BetaURLImageSource or BetaFileImageSource`

      - `beta_base64_image_source: object { data, media_type, type }`

        - `data: string`

        - `media_type: "image/jpeg" or "image/png" or "image/gif" or "image/webp"`

          - `"image/jpeg"`

          - `"image/png"`

          - `"image/gif"`

          - `"image/webp"`

        - `type: "base64"`

      - `beta_url_image_source: object { type, url }`

        - `type: "url"`

        - `url: string`

      - `beta_file_image_source: object { file_id, type }`

        - `file_id: string`

        - `type: "file"`

    - `type: "image"`

    - `cache_control: optional object { type, ttl }`

      Create a cache control breakpoint at this content block.

      - `type: "ephemeral"`

      - `ttl: optional "5m" or "1h"`

        The time-to-live for the cache control breakpoint.

        This may be one the following values:

        - `5m`: 5 minutes
        - `1h`: 1 hour

        Defaults to `5m`.

        - `"5m"`

        - `"1h"`

### Beta Context Management Config

- `beta_context_management_config: object { edits }`

  - `edits: optional array of BetaClearToolUses20250919Edit or BetaClearThinking20251015Edit or BetaCompact20260112Edit`

    List of context management edits to apply

    - `beta_clear_tool_uses_20250919_edit: object { type, clear_at_least, clear_tool_inputs, 3 more }`

      - `type: "clear_tool_uses_20250919"`

      - `clear_at_least: optional object { type, value }`

        Minimum number of tokens that must be cleared when triggered. Context will only be modified if at least this many tokens can be removed.

        - `type: "input_tokens"`

        - `value: number`

      - `clear_tool_inputs: optional boolean or array of string`

        Whether to clear all tool inputs (bool) or specific tool inputs to clear (list)

        - `union_member_0: boolean`

        - `union_member_1: array of string`

      - `exclude_tools: optional array of string`

        Tool names whose uses are preserved from clearing

      - `keep: optional object { type, value }`

        Number of tool uses to retain in the conversation

        - `type: "tool_uses"`

        - `value: number`

      - `trigger: optional BetaInputTokensTrigger or BetaToolUsesTrigger`

        Condition that triggers the context management strategy

        - `beta_input_tokens_trigger: object { type, value }`

          - `type: "input_tokens"`

          - `value: number`

        - `beta_tool_uses_trigger: object { type, value }`

          - `type: "tool_uses"`

          - `value: number`

    - `beta_clear_thinking_20251015_edit: object { type, keep }`

      - `type: "clear_thinking_20251015"`

      - `keep: optional BetaThinkingTurns or BetaAllThinkingTurns or "all"`

        Number of most recent assistant turns to keep thinking blocks for. Older turns will have their thinking blocks removed.

        - `beta_thinking_turns: object { type, value }`

          - `type: "thinking_turns"`

          - `value: number`

        - `beta_all_thinking_turns: object { type }`

          - `type: "all"`

        - `union_member_2: "all"`

    - `beta_compact_20260112_edit: object { type, instructions, pause_after_compaction, trigger }`

      Automatically compact older context when reaching the configured trigger threshold.

      - `type: "compact_20260112"`

      - `instructions: optional string`

        Additional instructions for summarization.

      - `pause_after_compaction: optional boolean`

        Whether to pause after compaction and return the compaction block to the user.

      - `trigger: optional object { type, value }`

        When to trigger compaction. Defaults to 150000 input tokens.

        - `type: "input_tokens"`

        - `value: number`

### Beta Context Management Response

- `beta_context_management_response: object { applied_edits }`

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

### Beta Count Tokens Context Management Response

- `beta_count_tokens_context_management_response: object { original_input_tokens }`

  - `original_input_tokens: number`

    The original token count before context management was applied

### Beta Direct Caller

- `beta_direct_caller: object { type }`

  Tool invocation directly from the model.

  - `type: "direct"`

### Beta Document Block

- `beta_document_block: object { citations, source, title, type }`

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

### Beta Encrypted Code Execution Result Block

- `beta_encrypted_code_execution_result_block: object { content, encrypted_stdout, return_code, 2 more }`

  Code execution result with encrypted stdout for PFC + web_search results.

  - `content: array of BetaCodeExecutionOutputBlock`

    - `file_id: string`

    - `type: "code_execution_output"`

  - `encrypted_stdout: string`

  - `return_code: number`

  - `stderr: string`

  - `type: "encrypted_code_execution_result"`

### Beta Encrypted Code Execution Result Block Param

- `beta_encrypted_code_execution_result_block_param: object { content, encrypted_stdout, return_code, 2 more }`

  Code execution result with encrypted stdout for PFC + web_search results.

  - `content: array of BetaCodeExecutionOutputBlockParam`

    - `file_id: string`

    - `type: "code_execution_output"`

  - `encrypted_stdout: string`

  - `return_code: number`

  - `stderr: string`

  - `type: "encrypted_code_execution_result"`

### Beta File Document Source

- `beta_file_document_source: object { file_id, type }`

  - `file_id: string`

  - `type: "file"`

### Beta File Image Source

- `beta_file_image_source: object { file_id, type }`

  - `file_id: string`

  - `type: "file"`

### Beta Image Block Param

- `beta_image_block_param: object { source, type, cache_control }`

  - `source: BetaBase64ImageSource or BetaURLImageSource or BetaFileImageSource`

    - `beta_base64_image_source: object { data, media_type, type }`

      - `data: string`

      - `media_type: "image/jpeg" or "image/png" or "image/gif" or "image/webp"`

        - `"image/jpeg"`

        - `"image/png"`

        - `"image/gif"`

        - `"image/webp"`

      - `type: "base64"`

    - `beta_url_image_source: object { type, url }`

      - `type: "url"`

      - `url: string`

    - `beta_file_image_source: object { file_id, type }`

      - `file_id: string`

      - `type: "file"`

  - `type: "image"`

  - `cache_control: optional object { type, ttl }`

    Create a cache control breakpoint at this content block.

    - `type: "ephemeral"`

    - `ttl: optional "5m" or "1h"`

      The time-to-live for the cache control breakpoint.

      This may be one the following values:

      - `5m`: 5 minutes
      - `1h`: 1 hour

      Defaults to `5m`.

      - `"5m"`

      - `"1h"`

### Beta Input JSON Delta

- `beta_input_json_delta: object { partial_json, type }`

  - `partial_json: string`

  - `type: "input_json_delta"`

### Beta Input Tokens Clear At Least

- `beta_input_tokens_clear_at_least: object { type, value }`

  - `type: "input_tokens"`

  - `value: number`

### Beta Input Tokens Trigger

- `beta_input_tokens_trigger: object { type, value }`

  - `type: "input_tokens"`

  - `value: number`

### Beta Iterations Usage

- `beta_iterations_usage: array of BetaMessageIterationUsage or BetaCompactionIterationUsage or BetaAdvisorMessageIterationUsage`

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

### Beta JSON Output Format

- `beta_json_output_format: object { schema, type }`

  - `schema: map[unknown]`

    The JSON schema of the format

  - `type: "json_schema"`

### Beta MCP Tool Config

- `beta_mcp_tool_config: object { defer_loading, enabled }`

  Configuration for a specific tool in an MCP toolset.

  - `defer_loading: optional boolean`

  - `enabled: optional boolean`

### Beta MCP Tool Default Config

- `beta_mcp_tool_default_config: object { defer_loading, enabled }`

  Default configuration for tools in an MCP toolset.

  - `defer_loading: optional boolean`

  - `enabled: optional boolean`

### Beta MCP Tool Result Block

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

### Beta MCP Tool Use Block

- `beta_mcp_tool_use_block: object { id, input, name, 2 more }`

  - `id: string`

  - `input: map[unknown]`

  - `name: string`

    The name of the MCP tool

  - `server_name: string`

    The name of the MCP server

  - `type: "mcp_tool_use"`

### Beta MCP Tool Use Block Param

- `beta_mcp_tool_use_block_param: object { id, input, name, 3 more }`

  - `id: string`

  - `input: map[unknown]`

  - `name: string`

  - `server_name: string`

    The name of the MCP server

  - `type: "mcp_tool_use"`

  - `cache_control: optional object { type, ttl }`

    Create a cache control breakpoint at this content block.

    - `type: "ephemeral"`

    - `ttl: optional "5m" or "1h"`

      The time-to-live for the cache control breakpoint.

      This may be one the following values:

      - `5m`: 5 minutes
      - `1h`: 1 hour

      Defaults to `5m`.

      - `"5m"`

      - `"1h"`

### Beta MCP Toolset

- `beta_mcp_toolset: object { mcp_server_name, type, cache_control, 2 more }`

  Configuration for a group of tools from an MCP server.

  Allows configuring enabled status and defer_loading for all tools
  from an MCP server, with optional per-tool overrides.

  - `mcp_server_name: string`

    Name of the MCP server to configure tools for

  - `type: "mcp_toolset"`

  - `cache_control: optional object { type, ttl }`

    Create a cache control breakpoint at this content block.

    - `type: "ephemeral"`

    - `ttl: optional "5m" or "1h"`

      The time-to-live for the cache control breakpoint.

      This may be one the following values:

      - `5m`: 5 minutes
      - `1h`: 1 hour

      Defaults to `5m`.

      - `"5m"`

      - `"1h"`

  - `configs: optional map[BetaMCPToolConfig]`

    Configuration overrides for specific tools, keyed by tool name

    - `defer_loading: optional boolean`

    - `enabled: optional boolean`

  - `default_config: optional object { defer_loading, enabled }`

    Default configuration applied to all tools from this server

    - `defer_loading: optional boolean`

    - `enabled: optional boolean`

### Beta Memory Tool 20250818

- `beta_memory_tool_20250818: object { name, type, allowed_callers, 4 more }`

  - `name: "memory"`

    Name of the tool.

    This is how the tool will be called by the model and in `tool_use` blocks.

  - `type: "memory_20250818"`

  - `allowed_callers: optional array of "direct" or "code_execution_20250825" or "code_execution_20260120"`

    - `"direct"`

    - `"code_execution_20250825"`

    - `"code_execution_20260120"`

  - `cache_control: optional object { type, ttl }`

    Create a cache control breakpoint at this content block.

    - `type: "ephemeral"`

    - `ttl: optional "5m" or "1h"`

      The time-to-live for the cache control breakpoint.

      This may be one the following values:

      - `5m`: 5 minutes
      - `1h`: 1 hour

      Defaults to `5m`.

      - `"5m"`

      - `"1h"`

  - `defer_loading: optional boolean`

    If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

  - `input_examples: optional array of map[unknown]`

  - `strict: optional boolean`

    When true, guarantees schema validation on tool names and inputs

### Beta Memory Tool 20250818 Command

- `beta_memory_tool_20250818_command: BetaMemoryTool20250818ViewCommand or BetaMemoryTool20250818CreateCommand or BetaMemoryTool20250818StrReplaceCommand or 3 more`

  - `beta_memory_tool_20250818_view_command: object { command, path, view_range }`

    - `command: "view"`

      Command type identifier

    - `path: string`

      Path to directory or file to view

    - `view_range: optional array of number`

      Optional line range for viewing specific lines

  - `beta_memory_tool_20250818_create_command: object { command, file_text, path }`

    - `command: "create"`

      Command type identifier

    - `file_text: string`

      Content to write to the file

    - `path: string`

      Path where the file should be created

  - `beta_memory_tool_20250818_str_replace_command: object { command, new_str, old_str, path }`

    - `command: "str_replace"`

      Command type identifier

    - `new_str: string`

      Text to replace with

    - `old_str: string`

      Text to search for and replace

    - `path: string`

      Path to the file where text should be replaced

  - `beta_memory_tool_20250818_insert_command: object { command, insert_line, insert_text, path }`

    - `command: "insert"`

      Command type identifier

    - `insert_line: number`

      Line number where text should be inserted

    - `insert_text: string`

      Text to insert at the specified line

    - `path: string`

      Path to the file where text should be inserted

  - `beta_memory_tool_20250818_delete_command: object { command, path }`

    - `command: "delete"`

      Command type identifier

    - `path: string`

      Path to the file or directory to delete

  - `beta_memory_tool_20250818_rename_command: object { command, new_path, old_path }`

    - `command: "rename"`

      Command type identifier

    - `new_path: string`

      New path for the file or directory

    - `old_path: string`

      Current path of the file or directory

### Beta Memory Tool 20250818 Create Command

- `beta_memory_tool_20250818_create_command: object { command, file_text, path }`

  - `command: "create"`

    Command type identifier

  - `file_text: string`

    Content to write to the file

  - `path: string`

    Path where the file should be created

### Beta Memory Tool 20250818 Delete Command

- `beta_memory_tool_20250818_delete_command: object { command, path }`

  - `command: "delete"`

    Command type identifier

  - `path: string`

    Path to the file or directory to delete

### Beta Memory Tool 20250818 Insert Command

- `beta_memory_tool_20250818_insert_command: object { command, insert_line, insert_text, path }`

  - `command: "insert"`

    Command type identifier

  - `insert_line: number`

    Line number where text should be inserted

  - `insert_text: string`

    Text to insert at the specified line

  - `path: string`

    Path to the file where text should be inserted

### Beta Memory Tool 20250818 Rename Command

- `beta_memory_tool_20250818_rename_command: object { command, new_path, old_path }`

  - `command: "rename"`

    Command type identifier

  - `new_path: string`

    New path for the file or directory

  - `old_path: string`

    Current path of the file or directory

### Beta Memory Tool 20250818 Str Replace Command

- `beta_memory_tool_20250818_str_replace_command: object { command, new_str, old_str, path }`

  - `command: "str_replace"`

    Command type identifier

  - `new_str: string`

    Text to replace with

  - `old_str: string`

    Text to search for and replace

  - `path: string`

    Path to the file where text should be replaced

### Beta Memory Tool 20250818 View Command

- `beta_memory_tool_20250818_view_command: object { command, path, view_range }`

  - `command: "view"`

    Command type identifier

  - `path: string`

    Path to directory or file to view

  - `view_range: optional array of number`

    Optional line range for viewing specific lines

### Beta Message

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

    - `beta_compaction_block: object { content, encrypted_content, type }`

      A compaction block returned when autocompact is triggered.

      When content is None, it indicates the compaction failed to produce a valid
      summary (e.g., malformed output from the model). Clients may round-trip
      compaction blocks with null content; the server treats them as no-ops.

      - `content: string`

        Summary of compacted content, or null if compaction failed

      - `encrypted_content: string`

        Opaque metadata from prior compaction, to be round-tripped verbatim

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

### Beta Message Delta Usage

- `beta_message_delta_usage: object { cache_creation_input_tokens, cache_read_input_tokens, input_tokens, 3 more }`

  - `cache_creation_input_tokens: number`

    The cumulative number of input tokens used to create the cache entry.

  - `cache_read_input_tokens: number`

    The cumulative number of input tokens read from the cache.

  - `input_tokens: number`

    The cumulative number of input tokens which were used.

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

    The cumulative number of output tokens which were used.

  - `server_tool_use: object { web_fetch_requests, web_search_requests }`

    The number of server tool requests.

    - `web_fetch_requests: number`

      The number of web fetch tool requests.

    - `web_search_requests: number`

      The number of web search tool requests.

### Beta Message Iteration Usage

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

### Beta Message Param

- `beta_message_param: object { content, role }`

  - `content: array of BetaContentBlockParam`

    - `beta_text_block_param: object { text, type, cache_control, citations }`

      - `text: string`

      - `type: "text"`

      - `cache_control: optional object { type, ttl }`

        Create a cache control breakpoint at this content block.

        - `type: "ephemeral"`

        - `ttl: optional "5m" or "1h"`

          The time-to-live for the cache control breakpoint.

          This may be one the following values:

          - `5m`: 5 minutes
          - `1h`: 1 hour

          Defaults to `5m`.

          - `"5m"`

          - `"1h"`

      - `citations: optional array of BetaTextCitationParam`

        - `beta_citation_char_location_param: object { cited_text, document_index, document_title, 3 more }`

          - `cited_text: string`

          - `document_index: number`

          - `document_title: string`

          - `end_char_index: number`

          - `start_char_index: number`

          - `type: "char_location"`

        - `beta_citation_page_location_param: object { cited_text, document_index, document_title, 3 more }`

          - `cited_text: string`

          - `document_index: number`

          - `document_title: string`

          - `end_page_number: number`

          - `start_page_number: number`

          - `type: "page_location"`

        - `beta_citation_content_block_location_param: object { cited_text, document_index, document_title, 3 more }`

          - `cited_text: string`

          - `document_index: number`

          - `document_title: string`

          - `end_block_index: number`

          - `start_block_index: number`

          - `type: "content_block_location"`

        - `beta_citation_web_search_result_location_param: object { cited_text, encrypted_index, title, 2 more }`

          - `cited_text: string`

          - `encrypted_index: string`

          - `title: string`

          - `type: "web_search_result_location"`

          - `url: string`

        - `beta_citation_search_result_location_param: object { cited_text, end_block_index, search_result_index, 4 more }`

          - `cited_text: string`

          - `end_block_index: number`

          - `search_result_index: number`

          - `source: string`

          - `start_block_index: number`

          - `title: string`

          - `type: "search_result_location"`

    - `beta_image_block_param: object { source, type, cache_control }`

      - `source: BetaBase64ImageSource or BetaURLImageSource or BetaFileImageSource`

        - `beta_base64_image_source: object { data, media_type, type }`

          - `data: string`

          - `media_type: "image/jpeg" or "image/png" or "image/gif" or "image/webp"`

            - `"image/jpeg"`

            - `"image/png"`

            - `"image/gif"`

            - `"image/webp"`

          - `type: "base64"`

        - `beta_url_image_source: object { type, url }`

          - `type: "url"`

          - `url: string`

        - `beta_file_image_source: object { file_id, type }`

          - `file_id: string`

          - `type: "file"`

      - `type: "image"`

      - `cache_control: optional object { type, ttl }`

        Create a cache control breakpoint at this content block.

        - `type: "ephemeral"`

        - `ttl: optional "5m" or "1h"`

          The time-to-live for the cache control breakpoint.

          This may be one the following values:

          - `5m`: 5 minutes
          - `1h`: 1 hour

          Defaults to `5m`.

          - `"5m"`

          - `"1h"`

    - `beta_request_document_block: object { source, type, cache_control, 3 more }`

      - `source: BetaBase64PDFSource or BetaPlainTextSource or BetaContentBlockSource or 2 more`

        - `beta_base64_pdf_source: object { data, media_type, type }`

          - `data: string`

          - `media_type: "application/pdf"`

          - `type: "base64"`

        - `beta_plain_text_source: object { data, media_type, type }`

          - `data: string`

          - `media_type: "text/plain"`

          - `type: "text"`

        - `beta_content_block_source: object { content, type }`

          - `content: string or array of BetaContentBlockSourceContent`

            - `union_member_0: string`

            - `beta_content_block_source_content: array of BetaContentBlockSourceContent`

              - `beta_text_block_param: object { text, type, cache_control, citations }`

                - `text: string`

                - `type: "text"`

                - `cache_control: optional object { type, ttl }`

                  Create a cache control breakpoint at this content block.

                  - `type: "ephemeral"`

                  - `ttl: optional "5m" or "1h"`

                    The time-to-live for the cache control breakpoint.

                    This may be one the following values:

                    - `5m`: 5 minutes
                    - `1h`: 1 hour

                    Defaults to `5m`.

                    - `"5m"`

                    - `"1h"`

                - `citations: optional array of BetaTextCitationParam`

                  - `beta_citation_char_location_param: object { cited_text, document_index, document_title, 3 more }`

                    - `cited_text: string`

                    - `document_index: number`

                    - `document_title: string`

                    - `end_char_index: number`

                    - `start_char_index: number`

                    - `type: "char_location"`

                  - `beta_citation_page_location_param: object { cited_text, document_index, document_title, 3 more }`

                    - `cited_text: string`

                    - `document_index: number`

                    - `document_title: string`

                    - `end_page_number: number`

                    - `start_page_number: number`

                    - `type: "page_location"`

                  - `beta_citation_content_block_location_param: object { cited_text, document_index, document_title, 3 more }`

                    - `cited_text: string`

                    - `document_index: number`

                    - `document_title: string`

                    - `end_block_index: number`

                    - `start_block_index: number`

                    - `type: "content_block_location"`

                  - `beta_citation_web_search_result_location_param: object { cited_text, encrypted_index, title, 2 more }`

                    - `cited_text: string`

                    - `encrypted_index: string`

                    - `title: string`

                    - `type: "web_search_result_location"`

                    - `url: string`

                  - `beta_citation_search_result_location_param: object { cited_text, end_block_index, search_result_index, 4 more }`

                    - `cited_text: string`

                    - `end_block_index: number`

                    - `search_result_index: number`

                    - `source: string`

                    - `start_block_index: number`

                    - `title: string`

                    - `type: "search_result_location"`

              - `beta_image_block_param: object { source, type, cache_control }`

                - `source: BetaBase64ImageSource or BetaURLImageSource or BetaFileImageSource`

                  - `beta_base64_image_source: object { data, media_type, type }`

                    - `data: string`

                    - `media_type: "image/jpeg" or "image/png" or "image/gif" or "image/webp"`

                      - `"image/jpeg"`

                      - `"image/png"`

                      - `"image/gif"`

                      - `"image/webp"`

                    - `type: "base64"`

                  - `beta_url_image_source: object { type, url }`

                    - `type: "url"`

                    - `url: string`

                  - `beta_file_image_source: object { file_id, type }`

                    - `file_id: string`

                    - `type: "file"`

                - `type: "image"`

                - `cache_control: optional object { type, ttl }`

                  Create a cache control breakpoint at this content block.

                  - `type: "ephemeral"`

                  - `ttl: optional "5m" or "1h"`

                    The time-to-live for the cache control breakpoint.

                    This may be one the following values:

                    - `5m`: 5 minutes
                    - `1h`: 1 hour

                    Defaults to `5m`.

                    - `"5m"`

                    - `"1h"`

          - `type: "content"`

        - `beta_url_pdf_source: object { type, url }`

          - `type: "url"`

          - `url: string`

        - `beta_file_document_source: object { file_id, type }`

          - `file_id: string`

          - `type: "file"`

      - `type: "document"`

      - `cache_control: optional object { type, ttl }`

        Create a cache control breakpoint at this content block.

        - `type: "ephemeral"`

        - `ttl: optional "5m" or "1h"`

          The time-to-live for the cache control breakpoint.

          This may be one the following values:

          - `5m`: 5 minutes
          - `1h`: 1 hour

          Defaults to `5m`.

          - `"5m"`

          - `"1h"`

      - `citations: optional object { enabled }`

        - `enabled: optional boolean`

      - `context: optional string`

      - `title: optional string`

    - `beta_search_result_block_param: object { content, source, title, 3 more }`

      - `content: array of BetaTextBlockParam`

        - `text: string`

        - `type: "text"`

        - `cache_control: optional object { type, ttl }`

          Create a cache control breakpoint at this content block.

          - `type: "ephemeral"`

          - `ttl: optional "5m" or "1h"`

            The time-to-live for the cache control breakpoint.

            This may be one the following values:

            - `5m`: 5 minutes
            - `1h`: 1 hour

            Defaults to `5m`.

            - `"5m"`

            - `"1h"`

        - `citations: optional array of BetaTextCitationParam`

          - `beta_citation_char_location_param: object { cited_text, document_index, document_title, 3 more }`

            - `cited_text: string`

            - `document_index: number`

            - `document_title: string`

            - `end_char_index: number`

            - `start_char_index: number`

            - `type: "char_location"`

          - `beta_citation_page_location_param: object { cited_text, document_index, document_title, 3 more }`

            - `cited_text: string`

            - `document_index: number`

            - `document_title: string`

            - `end_page_number: number`

            - `start_page_number: number`

            - `type: "page_location"`

          - `beta_citation_content_block_location_param: object { cited_text, document_index, document_title, 3 more }`

            - `cited_text: string`

            - `document_index: number`

            - `document_title: string`

            - `end_block_index: number`

            - `start_block_index: number`

            - `type: "content_block_location"`

          - `beta_citation_web_search_result_location_param: object { cited_text, encrypted_index, title, 2 more }`

            - `cited_text: string`

            - `encrypted_index: string`

            - `title: string`

            - `type: "web_search_result_location"`

            - `url: string`

          - `beta_citation_search_result_location_param: object { cited_text, end_block_index, search_result_index, 4 more }`

            - `cited_text: string`

            - `end_block_index: number`

            - `search_result_index: number`

            - `source: string`

            - `start_block_index: number`

            - `title: string`

            - `type: "search_result_location"`

      - `source: string`

      - `title: string`

      - `type: "search_result"`

      - `cache_control: optional object { type, ttl }`

        Create a cache control breakpoint at this content block.

        - `type: "ephemeral"`

        - `ttl: optional "5m" or "1h"`

          The time-to-live for the cache control breakpoint.

          This may be one the following values:

          - `5m`: 5 minutes
          - `1h`: 1 hour

          Defaults to `5m`.

          - `"5m"`

          - `"1h"`

      - `citations: optional object { enabled }`

        - `enabled: optional boolean`

    - `beta_thinking_block_param: object { signature, thinking, type }`

      - `signature: string`

      - `thinking: string`

      - `type: "thinking"`

    - `beta_redacted_thinking_block_param: object { data, type }`

      - `data: string`

      - `type: "redacted_thinking"`

    - `beta_tool_use_block_param: object { id, input, name, 3 more }`

      - `id: string`

      - `input: map[unknown]`

      - `name: string`

      - `type: "tool_use"`

      - `cache_control: optional object { type, ttl }`

        Create a cache control breakpoint at this content block.

        - `type: "ephemeral"`

        - `ttl: optional "5m" or "1h"`

          The time-to-live for the cache control breakpoint.

          This may be one the following values:

          - `5m`: 5 minutes
          - `1h`: 1 hour

          Defaults to `5m`.

          - `"5m"`

          - `"1h"`

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

    - `beta_tool_result_block_param: object { tool_use_id, type, cache_control, 2 more }`

      - `tool_use_id: string`

      - `type: "tool_result"`

      - `cache_control: optional object { type, ttl }`

        Create a cache control breakpoint at this content block.

        - `type: "ephemeral"`

        - `ttl: optional "5m" or "1h"`

          The time-to-live for the cache control breakpoint.

          This may be one the following values:

          - `5m`: 5 minutes
          - `1h`: 1 hour

          Defaults to `5m`.

          - `"5m"`

          - `"1h"`

      - `content: optional array of BetaTextBlockParam or BetaImageBlockParam or BetaSearchResultBlockParam or 2 more`

        - `beta_text_block_param: object { text, type, cache_control, citations }`

          - `text: string`

          - `type: "text"`

          - `cache_control: optional object { type, ttl }`

            Create a cache control breakpoint at this content block.

            - `type: "ephemeral"`

            - `ttl: optional "5m" or "1h"`

              The time-to-live for the cache control breakpoint.

              This may be one the following values:

              - `5m`: 5 minutes
              - `1h`: 1 hour

              Defaults to `5m`.

              - `"5m"`

              - `"1h"`

          - `citations: optional array of BetaTextCitationParam`

            - `beta_citation_char_location_param: object { cited_text, document_index, document_title, 3 more }`

              - `cited_text: string`

              - `document_index: number`

              - `document_title: string`

              - `end_char_index: number`

              - `start_char_index: number`

              - `type: "char_location"`

            - `beta_citation_page_location_param: object { cited_text, document_index, document_title, 3 more }`

              - `cited_text: string`

              - `document_index: number`

              - `document_title: string`

              - `end_page_number: number`

              - `start_page_number: number`

              - `type: "page_location"`

            - `beta_citation_content_block_location_param: object { cited_text, document_index, document_title, 3 more }`

              - `cited_text: string`

              - `document_index: number`

              - `document_title: string`

              - `end_block_index: number`

              - `start_block_index: number`

              - `type: "content_block_location"`

            - `beta_citation_web_search_result_location_param: object { cited_text, encrypted_index, title, 2 more }`

              - `cited_text: string`

              - `encrypted_index: string`

              - `title: string`

              - `type: "web_search_result_location"`

              - `url: string`

            - `beta_citation_search_result_location_param: object { cited_text, end_block_index, search_result_index, 4 more }`

              - `cited_text: string`

              - `end_block_index: number`

              - `search_result_index: number`

              - `source: string`

              - `start_block_index: number`

              - `title: string`

              - `type: "search_result_location"`

        - `beta_image_block_param: object { source, type, cache_control }`

          - `source: BetaBase64ImageSource or BetaURLImageSource or BetaFileImageSource`

            - `beta_base64_image_source: object { data, media_type, type }`

              - `data: string`

              - `media_type: "image/jpeg" or "image/png" or "image/gif" or "image/webp"`

                - `"image/jpeg"`

                - `"image/png"`

                - `"image/gif"`

                - `"image/webp"`

              - `type: "base64"`

            - `beta_url_image_source: object { type, url }`

              - `type: "url"`

              - `url: string`

            - `beta_file_image_source: object { file_id, type }`

              - `file_id: string`

              - `type: "file"`

          - `type: "image"`

          - `cache_control: optional object { type, ttl }`

            Create a cache control breakpoint at this content block.

            - `type: "ephemeral"`

            - `ttl: optional "5m" or "1h"`

              The time-to-live for the cache control breakpoint.

              This may be one the following values:

              - `5m`: 5 minutes
              - `1h`: 1 hour

              Defaults to `5m`.

              - `"5m"`

              - `"1h"`

        - `beta_search_result_block_param: object { content, source, title, 3 more }`

          - `content: array of BetaTextBlockParam`

            - `text: string`

            - `type: "text"`

            - `cache_control: optional object { type, ttl }`

              Create a cache control breakpoint at this content block.

              - `type: "ephemeral"`

              - `ttl: optional "5m" or "1h"`

                The time-to-live for the cache control breakpoint.

                This may be one the following values:

                - `5m`: 5 minutes
                - `1h`: 1 hour

                Defaults to `5m`.

                - `"5m"`

                - `"1h"`

            - `citations: optional array of BetaTextCitationParam`

              - `beta_citation_char_location_param: object { cited_text, document_index, document_title, 3 more }`

                - `cited_text: string`

                - `document_index: number`

                - `document_title: string`

                - `end_char_index: number`

                - `start_char_index: number`

                - `type: "char_location"`

              - `beta_citation_page_location_param: object { cited_text, document_index, document_title, 3 more }`

                - `cited_text: string`

                - `document_index: number`

                - `document_title: string`

                - `end_page_number: number`

                - `start_page_number: number`

                - `type: "page_location"`

              - `beta_citation_content_block_location_param: object { cited_text, document_index, document_title, 3 more }`

                - `cited_text: string`

                - `document_index: number`

                - `document_title: string`

                - `end_block_index: number`

                - `start_block_index: number`

                - `type: "content_block_location"`

              - `beta_citation_web_search_result_location_param: object { cited_text, encrypted_index, title, 2 more }`

                - `cited_text: string`

                - `encrypted_index: string`

                - `title: string`

                - `type: "web_search_result_location"`

                - `url: string`

              - `beta_citation_search_result_location_param: object { cited_text, end_block_index, search_result_index, 4 more }`

                - `cited_text: string`

                - `end_block_index: number`

                - `search_result_index: number`

                - `source: string`

                - `start_block_index: number`

                - `title: string`

                - `type: "search_result_location"`

          - `source: string`

          - `title: string`

          - `type: "search_result"`

          - `cache_control: optional object { type, ttl }`

            Create a cache control breakpoint at this content block.

            - `type: "ephemeral"`

            - `ttl: optional "5m" or "1h"`

              The time-to-live for the cache control breakpoint.

              This may be one the following values:

              - `5m`: 5 minutes
              - `1h`: 1 hour

              Defaults to `5m`.

              - `"5m"`

              - `"1h"`

          - `citations: optional object { enabled }`

            - `enabled: optional boolean`

        - `beta_request_document_block: object { source, type, cache_control, 3 more }`

          - `source: BetaBase64PDFSource or BetaPlainTextSource or BetaContentBlockSource or 2 more`

            - `beta_base64_pdf_source: object { data, media_type, type }`

              - `data: string`

              - `media_type: "application/pdf"`

              - `type: "base64"`

            - `beta_plain_text_source: object { data, media_type, type }`

              - `data: string`

              - `media_type: "text/plain"`

              - `type: "text"`

            - `beta_content_block_source: object { content, type }`

              - `content: string or array of BetaContentBlockSourceContent`

                - `union_member_0: string`

                - `beta_content_block_source_content: array of BetaContentBlockSourceContent`

                  - `beta_text_block_param: object { text, type, cache_control, citations }`

                    - `text: string`

                    - `type: "text"`

                    - `cache_control: optional object { type, ttl }`

                      Create a cache control breakpoint at this content block.

                      - `type: "ephemeral"`

                      - `ttl: optional "5m" or "1h"`

                        The time-to-live for the cache control breakpoint.

                        This may be one the following values:

                        - `5m`: 5 minutes
                        - `1h`: 1 hour

                        Defaults to `5m`.

                        - `"5m"`

                        - `"1h"`

                    - `citations: optional array of BetaTextCitationParam`

                      - `beta_citation_char_location_param: object { cited_text, document_index, document_title, 3 more }`

                        - `cited_text: string`

                        - `document_index: number`

                        - `document_title: string`

                        - `end_char_index: number`

                        - `start_char_index: number`

                        - `type: "char_location"`

                      - `beta_citation_page_location_param: object { cited_text, document_index, document_title, 3 more }`

                        - `cited_text: string`

                        - `document_index: number`

                        - `document_title: string`

                        - `end_page_number: number`

                        - `start_page_number: number`

                        - `type: "page_location"`

                      - `beta_citation_content_block_location_param: object { cited_text, document_index, document_title, 3 more }`

                        - `cited_text: string`

                        - `document_index: number`

                        - `document_title: string`

                        - `end_block_index: number`

                        - `start_block_index: number`

                        - `type: "content_block_location"`

                      - `beta_citation_web_search_result_location_param: object { cited_text, encrypted_index, title, 2 more }`

                        - `cited_text: string`

                        - `encrypted_index: string`

                        - `title: string`

                        - `type: "web_search_result_location"`

                        - `url: string`

                      - `beta_citation_search_result_location_param: object { cited_text, end_block_index, search_result_index, 4 more }`

                        - `cited_text: string`

                        - `end_block_index: number`

                        - `search_result_index: number`

                        - `source: string`

                        - `start_block_index: number`

                        - `title: string`

                        - `type: "search_result_location"`

                  - `beta_image_block_param: object { source, type, cache_control }`

                    - `source: BetaBase64ImageSource or BetaURLImageSource or BetaFileImageSource`

                      - `beta_base64_image_source: object { data, media_type, type }`

                        - `data: string`

                        - `media_type: "image/jpeg" or "image/png" or "image/gif" or "image/webp"`

                          - `"image/jpeg"`

                          - `"image/png"`

                          - `"image/gif"`

                          - `"image/webp"`

                        - `type: "base64"`

                      - `beta_url_image_source: object { type, url }`

                        - `type: "url"`

                        - `url: string`

                      - `beta_file_image_source: object { file_id, type }`

                        - `file_id: string`

                        - `type: "file"`

                    - `type: "image"`

                    - `cache_control: optional object { type, ttl }`

                      Create a cache control breakpoint at this content block.

                      - `type: "ephemeral"`

                      - `ttl: optional "5m" or "1h"`

                        The time-to-live for the cache control breakpoint.

                        This may be one the following values:

                        - `5m`: 5 minutes
                        - `1h`: 1 hour

                        Defaults to `5m`.

                        - `"5m"`

                        - `"1h"`

              - `type: "content"`

            - `beta_url_pdf_source: object { type, url }`

              - `type: "url"`

              - `url: string`

            - `beta_file_document_source: object { file_id, type }`

              - `file_id: string`

              - `type: "file"`

          - `type: "document"`

          - `cache_control: optional object { type, ttl }`

            Create a cache control breakpoint at this content block.

            - `type: "ephemeral"`

            - `ttl: optional "5m" or "1h"`

              The time-to-live for the cache control breakpoint.

              This may be one the following values:

              - `5m`: 5 minutes
              - `1h`: 1 hour

              Defaults to `5m`.

              - `"5m"`

              - `"1h"`

          - `citations: optional object { enabled }`

            - `enabled: optional boolean`

          - `context: optional string`

          - `title: optional string`

        - `beta_tool_reference_block_param: object { tool_name, type, cache_control }`

          Tool reference block that can be included in tool_result content.

          - `tool_name: string`

          - `type: "tool_reference"`

          - `cache_control: optional object { type, ttl }`

            Create a cache control breakpoint at this content block.

            - `type: "ephemeral"`

            - `ttl: optional "5m" or "1h"`

              The time-to-live for the cache control breakpoint.

              This may be one the following values:

              - `5m`: 5 minutes
              - `1h`: 1 hour

              Defaults to `5m`.

              - `"5m"`

              - `"1h"`

      - `is_error: optional boolean`

    - `beta_server_tool_use_block_param: object { id, input, name, 3 more }`

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

      - `cache_control: optional object { type, ttl }`

        Create a cache control breakpoint at this content block.

        - `type: "ephemeral"`

        - `ttl: optional "5m" or "1h"`

          The time-to-live for the cache control breakpoint.

          This may be one the following values:

          - `5m`: 5 minutes
          - `1h`: 1 hour

          Defaults to `5m`.

          - `"5m"`

          - `"1h"`

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

    - `beta_web_search_tool_result_block_param: object { content, tool_use_id, type, 2 more }`

      - `content: array of BetaWebSearchResultBlockParam or BetaWebSearchToolRequestError`

        - `Result Block: array of BetaWebSearchResultBlockParam`

          - `encrypted_content: string`

          - `title: string`

          - `type: "web_search_result"`

          - `url: string`

          - `page_age: optional string`

        - `beta_web_search_tool_request_error: object { error_code, type }`

          - `error_code: "invalid_tool_input" or "unavailable" or "max_uses_exceeded" or 3 more`

            - `"invalid_tool_input"`

            - `"unavailable"`

            - `"max_uses_exceeded"`

            - `"too_many_requests"`

            - `"query_too_long"`

            - `"request_too_large"`

          - `type: "web_search_tool_result_error"`

      - `tool_use_id: string`

      - `type: "web_search_tool_result"`

      - `cache_control: optional object { type, ttl }`

        Create a cache control breakpoint at this content block.

        - `type: "ephemeral"`

        - `ttl: optional "5m" or "1h"`

          The time-to-live for the cache control breakpoint.

          This may be one the following values:

          - `5m`: 5 minutes
          - `1h`: 1 hour

          Defaults to `5m`.

          - `"5m"`

          - `"1h"`

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

    - `beta_web_fetch_tool_result_block_param: object { content, tool_use_id, type, 2 more }`

      - `content: BetaWebFetchToolResultErrorBlockParam or BetaWebFetchBlockParam`

        - `beta_web_fetch_tool_result_error_block_param: object { error_code, type }`

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

        - `beta_web_fetch_block_param: object { content, type, url, retrieved_at }`

          - `content: object { source, type, cache_control, 3 more }`

            - `source: BetaBase64PDFSource or BetaPlainTextSource or BetaContentBlockSource or 2 more`

              - `beta_base64_pdf_source: object { data, media_type, type }`

                - `data: string`

                - `media_type: "application/pdf"`

                - `type: "base64"`

              - `beta_plain_text_source: object { data, media_type, type }`

                - `data: string`

                - `media_type: "text/plain"`

                - `type: "text"`

              - `beta_content_block_source: object { content, type }`

                - `content: string or array of BetaContentBlockSourceContent`

                  - `union_member_0: string`

                  - `beta_content_block_source_content: array of BetaContentBlockSourceContent`

                    - `beta_text_block_param: object { text, type, cache_control, citations }`

                      - `text: string`

                      - `type: "text"`

                      - `cache_control: optional object { type, ttl }`

                        Create a cache control breakpoint at this content block.

                        - `type: "ephemeral"`

                        - `ttl: optional "5m" or "1h"`

                          The time-to-live for the cache control breakpoint.

                          This may be one the following values:

                          - `5m`: 5 minutes
                          - `1h`: 1 hour

                          Defaults to `5m`.

                          - `"5m"`

                          - `"1h"`

                      - `citations: optional array of BetaTextCitationParam`

                        - `beta_citation_char_location_param: object { cited_text, document_index, document_title, 3 more }`

                          - `cited_text: string`

                          - `document_index: number`

                          - `document_title: string`

                          - `end_char_index: number`

                          - `start_char_index: number`

                          - `type: "char_location"`

                        - `beta_citation_page_location_param: object { cited_text, document_index, document_title, 3 more }`

                          - `cited_text: string`

                          - `document_index: number`

                          - `document_title: string`

                          - `end_page_number: number`

                          - `start_page_number: number`

                          - `type: "page_location"`

                        - `beta_citation_content_block_location_param: object { cited_text, document_index, document_title, 3 more }`

                          - `cited_text: string`

                          - `document_index: number`

                          - `document_title: string`

                          - `end_block_index: number`

                          - `start_block_index: number`

                          - `type: "content_block_location"`

                        - `beta_citation_web_search_result_location_param: object { cited_text, encrypted_index, title, 2 more }`

                          - `cited_text: string`

                          - `encrypted_index: string`

                          - `title: string`

                          - `type: "web_search_result_location"`

                          - `url: string`

                        - `beta_citation_search_result_location_param: object { cited_text, end_block_index, search_result_index, 4 more }`

                          - `cited_text: string`

                          - `end_block_index: number`

                          - `search_result_index: number`

                          - `source: string`

                          - `start_block_index: number`

                          - `title: string`

                          - `type: "search_result_location"`

                    - `beta_image_block_param: object { source, type, cache_control }`

                      - `source: BetaBase64ImageSource or BetaURLImageSource or BetaFileImageSource`

                        - `beta_base64_image_source: object { data, media_type, type }`

                          - `data: string`

                          - `media_type: "image/jpeg" or "image/png" or "image/gif" or "image/webp"`

                            - `"image/jpeg"`

                            - `"image/png"`

                            - `"image/gif"`

                            - `"image/webp"`

                          - `type: "base64"`

                        - `beta_url_image_source: object { type, url }`

                          - `type: "url"`

                          - `url: string`

                        - `beta_file_image_source: object { file_id, type }`

                          - `file_id: string`

                          - `type: "file"`

                      - `type: "image"`

                      - `cache_control: optional object { type, ttl }`

                        Create a cache control breakpoint at this content block.

                        - `type: "ephemeral"`

                        - `ttl: optional "5m" or "1h"`

                          The time-to-live for the cache control breakpoint.

                          This may be one the following values:

                          - `5m`: 5 minutes
                          - `1h`: 1 hour

                          Defaults to `5m`.

                          - `"5m"`

                          - `"1h"`

                - `type: "content"`

              - `beta_url_pdf_source: object { type, url }`

                - `type: "url"`

                - `url: string`

              - `beta_file_document_source: object { file_id, type }`

                - `file_id: string`

                - `type: "file"`

            - `type: "document"`

            - `cache_control: optional object { type, ttl }`

              Create a cache control breakpoint at this content block.

              - `type: "ephemeral"`

              - `ttl: optional "5m" or "1h"`

                The time-to-live for the cache control breakpoint.

                This may be one the following values:

                - `5m`: 5 minutes
                - `1h`: 1 hour

                Defaults to `5m`.

                - `"5m"`

                - `"1h"`

            - `citations: optional object { enabled }`

              - `enabled: optional boolean`

            - `context: optional string`

            - `title: optional string`

          - `type: "web_fetch_result"`

          - `url: string`

            Fetched content URL

          - `retrieved_at: optional string`

            ISO 8601 timestamp when the content was retrieved

      - `tool_use_id: string`

      - `type: "web_fetch_tool_result"`

      - `cache_control: optional object { type, ttl }`

        Create a cache control breakpoint at this content block.

        - `type: "ephemeral"`

        - `ttl: optional "5m" or "1h"`

          The time-to-live for the cache control breakpoint.

          This may be one the following values:

          - `5m`: 5 minutes
          - `1h`: 1 hour

          Defaults to `5m`.

          - `"5m"`

          - `"1h"`

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

    - `beta_advisor_tool_result_block_param: object { content, tool_use_id, type, cache_control }`

      - `content: BetaAdvisorToolResultErrorParam or BetaAdvisorResultBlockParam or BetaAdvisorRedactedResultBlockParam`

        - `beta_advisor_tool_result_error_param: object { error_code, type }`

          - `error_code: "max_uses_exceeded" or "prompt_too_long" or "too_many_requests" or 3 more`

            - `"max_uses_exceeded"`

            - `"prompt_too_long"`

            - `"too_many_requests"`

            - `"overloaded"`

            - `"unavailable"`

            - `"execution_time_exceeded"`

          - `type: "advisor_tool_result_error"`

        - `beta_advisor_result_block_param: object { text, type }`

          - `text: string`

          - `type: "advisor_result"`

        - `beta_advisor_redacted_result_block_param: object { encrypted_content, type }`

          - `encrypted_content: string`

            Opaque blob produced by a prior response; must be round-tripped verbatim.

          - `type: "advisor_redacted_result"`

      - `tool_use_id: string`

      - `type: "advisor_tool_result"`

      - `cache_control: optional object { type, ttl }`

        Create a cache control breakpoint at this content block.

        - `type: "ephemeral"`

        - `ttl: optional "5m" or "1h"`

          The time-to-live for the cache control breakpoint.

          This may be one the following values:

          - `5m`: 5 minutes
          - `1h`: 1 hour

          Defaults to `5m`.

          - `"5m"`

          - `"1h"`

    - `beta_code_execution_tool_result_block_param: object { content, tool_use_id, type, cache_control }`

      - `content: BetaCodeExecutionToolResultErrorParam or BetaCodeExecutionResultBlockParam or BetaEncryptedCodeExecutionResultBlockParam`

        Code execution result with encrypted stdout for PFC + web_search results.

        - `beta_code_execution_tool_result_error_param: object { error_code, type }`

          - `error_code: "invalid_tool_input" or "unavailable" or "too_many_requests" or "execution_time_exceeded"`

            - `"invalid_tool_input"`

            - `"unavailable"`

            - `"too_many_requests"`

            - `"execution_time_exceeded"`

          - `type: "code_execution_tool_result_error"`

        - `beta_code_execution_result_block_param: object { content, return_code, stderr, 2 more }`

          - `content: array of BetaCodeExecutionOutputBlockParam`

            - `file_id: string`

            - `type: "code_execution_output"`

          - `return_code: number`

          - `stderr: string`

          - `stdout: string`

          - `type: "code_execution_result"`

        - `beta_encrypted_code_execution_result_block_param: object { content, encrypted_stdout, return_code, 2 more }`

          Code execution result with encrypted stdout for PFC + web_search results.

          - `content: array of BetaCodeExecutionOutputBlockParam`

            - `file_id: string`

            - `type: "code_execution_output"`

          - `encrypted_stdout: string`

          - `return_code: number`

          - `stderr: string`

          - `type: "encrypted_code_execution_result"`

      - `tool_use_id: string`

      - `type: "code_execution_tool_result"`

      - `cache_control: optional object { type, ttl }`

        Create a cache control breakpoint at this content block.

        - `type: "ephemeral"`

        - `ttl: optional "5m" or "1h"`

          The time-to-live for the cache control breakpoint.

          This may be one the following values:

          - `5m`: 5 minutes
          - `1h`: 1 hour

          Defaults to `5m`.

          - `"5m"`

          - `"1h"`

    - `beta_bash_code_execution_tool_result_block_param: object { content, tool_use_id, type, cache_control }`

      - `content: BetaBashCodeExecutionToolResultErrorParam or BetaBashCodeExecutionResultBlockParam`

        - `beta_bash_code_execution_tool_result_error_param: object { error_code, type }`

          - `error_code: "invalid_tool_input" or "unavailable" or "too_many_requests" or 2 more`

            - `"invalid_tool_input"`

            - `"unavailable"`

            - `"too_many_requests"`

            - `"execution_time_exceeded"`

            - `"output_file_too_large"`

          - `type: "bash_code_execution_tool_result_error"`

        - `beta_bash_code_execution_result_block_param: object { content, return_code, stderr, 2 more }`

          - `content: array of BetaBashCodeExecutionOutputBlockParam`

            - `file_id: string`

            - `type: "bash_code_execution_output"`

          - `return_code: number`

          - `stderr: string`

          - `stdout: string`

          - `type: "bash_code_execution_result"`

      - `tool_use_id: string`

      - `type: "bash_code_execution_tool_result"`

      - `cache_control: optional object { type, ttl }`

        Create a cache control breakpoint at this content block.

        - `type: "ephemeral"`

        - `ttl: optional "5m" or "1h"`

          The time-to-live for the cache control breakpoint.

          This may be one the following values:

          - `5m`: 5 minutes
          - `1h`: 1 hour

          Defaults to `5m`.

          - `"5m"`

          - `"1h"`

    - `beta_text_editor_code_execution_tool_result_block_param: object { content, tool_use_id, type, cache_control }`

      - `content: BetaTextEditorCodeExecutionToolResultErrorParam or BetaTextEditorCodeExecutionViewResultBlockParam or BetaTextEditorCodeExecutionCreateResultBlockParam or BetaTextEditorCodeExecutionStrReplaceResultBlockParam`

        - `beta_text_editor_code_execution_tool_result_error_param: object { error_code, type, error_message }`

          - `error_code: "invalid_tool_input" or "unavailable" or "too_many_requests" or 2 more`

            - `"invalid_tool_input"`

            - `"unavailable"`

            - `"too_many_requests"`

            - `"execution_time_exceeded"`

            - `"file_not_found"`

          - `type: "text_editor_code_execution_tool_result_error"`

          - `error_message: optional string`

        - `beta_text_editor_code_execution_view_result_block_param: object { content, file_type, type, 3 more }`

          - `content: string`

          - `file_type: "text" or "image" or "pdf"`

            - `"text"`

            - `"image"`

            - `"pdf"`

          - `type: "text_editor_code_execution_view_result"`

          - `num_lines: optional number`

          - `start_line: optional number`

          - `total_lines: optional number`

        - `beta_text_editor_code_execution_create_result_block_param: object { is_file_update, type }`

          - `is_file_update: boolean`

          - `type: "text_editor_code_execution_create_result"`

        - `beta_text_editor_code_execution_str_replace_result_block_param: object { type, lines, new_lines, 3 more }`

          - `type: "text_editor_code_execution_str_replace_result"`

          - `lines: optional array of string`

          - `new_lines: optional number`

          - `new_start: optional number`

          - `old_lines: optional number`

          - `old_start: optional number`

      - `tool_use_id: string`

      - `type: "text_editor_code_execution_tool_result"`

      - `cache_control: optional object { type, ttl }`

        Create a cache control breakpoint at this content block.

        - `type: "ephemeral"`

        - `ttl: optional "5m" or "1h"`

          The time-to-live for the cache control breakpoint.

          This may be one the following values:

          - `5m`: 5 minutes
          - `1h`: 1 hour

          Defaults to `5m`.

          - `"5m"`

          - `"1h"`

    - `beta_tool_search_tool_result_block_param: object { content, tool_use_id, type, cache_control }`

      - `content: BetaToolSearchToolResultErrorParam or BetaToolSearchToolSearchResultBlockParam`

        - `beta_tool_search_tool_result_error_param: object { error_code, type }`

          - `error_code: "invalid_tool_input" or "unavailable" or "too_many_requests" or "execution_time_exceeded"`

            - `"invalid_tool_input"`

            - `"unavailable"`

            - `"too_many_requests"`

            - `"execution_time_exceeded"`

          - `type: "tool_search_tool_result_error"`

        - `beta_tool_search_tool_search_result_block_param: object { tool_references, type }`

          - `tool_references: array of BetaToolReferenceBlockParam`

            - `tool_name: string`

            - `type: "tool_reference"`

            - `cache_control: optional object { type, ttl }`

              Create a cache control breakpoint at this content block.

              - `type: "ephemeral"`

              - `ttl: optional "5m" or "1h"`

                The time-to-live for the cache control breakpoint.

                This may be one the following values:

                - `5m`: 5 minutes
                - `1h`: 1 hour

                Defaults to `5m`.

                - `"5m"`

                - `"1h"`

          - `type: "tool_search_tool_search_result"`

      - `tool_use_id: string`

      - `type: "tool_search_tool_result"`

      - `cache_control: optional object { type, ttl }`

        Create a cache control breakpoint at this content block.

        - `type: "ephemeral"`

        - `ttl: optional "5m" or "1h"`

          The time-to-live for the cache control breakpoint.

          This may be one the following values:

          - `5m`: 5 minutes
          - `1h`: 1 hour

          Defaults to `5m`.

          - `"5m"`

          - `"1h"`

    - `beta_mcp_tool_use_block_param: object { id, input, name, 3 more }`

      - `id: string`

      - `input: map[unknown]`

      - `name: string`

      - `server_name: string`

        The name of the MCP server

      - `type: "mcp_tool_use"`

      - `cache_control: optional object { type, ttl }`

        Create a cache control breakpoint at this content block.

        - `type: "ephemeral"`

        - `ttl: optional "5m" or "1h"`

          The time-to-live for the cache control breakpoint.

          This may be one the following values:

          - `5m`: 5 minutes
          - `1h`: 1 hour

          Defaults to `5m`.

          - `"5m"`

          - `"1h"`

    - `beta_request_mcp_tool_result_block_param: object { tool_use_id, type, cache_control, 2 more }`

      - `tool_use_id: string`

      - `type: "mcp_tool_result"`

      - `cache_control: optional object { type, ttl }`

        Create a cache control breakpoint at this content block.

        - `type: "ephemeral"`

        - `ttl: optional "5m" or "1h"`

          The time-to-live for the cache control breakpoint.

          This may be one the following values:

          - `5m`: 5 minutes
          - `1h`: 1 hour

          Defaults to `5m`.

          - `"5m"`

          - `"1h"`

      - `content: optional string or array of BetaTextBlockParam`

        - `union_member_0: string`

        - `beta_mcp_tool_result_block_param_content: array of BetaTextBlockParam`

          - `text: string`

          - `type: "text"`

          - `cache_control: optional object { type, ttl }`

            Create a cache control breakpoint at this content block.

            - `type: "ephemeral"`

            - `ttl: optional "5m" or "1h"`

              The time-to-live for the cache control breakpoint.

              This may be one the following values:

              - `5m`: 5 minutes
              - `1h`: 1 hour

              Defaults to `5m`.

              - `"5m"`

              - `"1h"`

          - `citations: optional array of BetaTextCitationParam`

            - `beta_citation_char_location_param: object { cited_text, document_index, document_title, 3 more }`

              - `cited_text: string`

              - `document_index: number`

              - `document_title: string`

              - `end_char_index: number`

              - `start_char_index: number`

              - `type: "char_location"`

            - `beta_citation_page_location_param: object { cited_text, document_index, document_title, 3 more }`

              - `cited_text: string`

              - `document_index: number`

              - `document_title: string`

              - `end_page_number: number`

              - `start_page_number: number`

              - `type: "page_location"`

            - `beta_citation_content_block_location_param: object { cited_text, document_index, document_title, 3 more }`

              - `cited_text: string`

              - `document_index: number`

              - `document_title: string`

              - `end_block_index: number`

              - `start_block_index: number`

              - `type: "content_block_location"`

            - `beta_citation_web_search_result_location_param: object { cited_text, encrypted_index, title, 2 more }`

              - `cited_text: string`

              - `encrypted_index: string`

              - `title: string`

              - `type: "web_search_result_location"`

              - `url: string`

            - `beta_citation_search_result_location_param: object { cited_text, end_block_index, search_result_index, 4 more }`

              - `cited_text: string`

              - `end_block_index: number`

              - `search_result_index: number`

              - `source: string`

              - `start_block_index: number`

              - `title: string`

              - `type: "search_result_location"`

      - `is_error: optional boolean`

    - `beta_container_upload_block_param: object { file_id, type, cache_control }`

      A content block that represents a file to be uploaded to the container
      Files uploaded via this block will be available in the container's input directory.

      - `file_id: string`

      - `type: "container_upload"`

      - `cache_control: optional object { type, ttl }`

        Create a cache control breakpoint at this content block.

        - `type: "ephemeral"`

        - `ttl: optional "5m" or "1h"`

          The time-to-live for the cache control breakpoint.

          This may be one the following values:

          - `5m`: 5 minutes
          - `1h`: 1 hour

          Defaults to `5m`.

          - `"5m"`

          - `"1h"`

    - `beta_compaction_block_param: object { content, type, cache_control, encrypted_content }`

      A compaction block containing summary of previous context.

      Users should round-trip these blocks from responses to subsequent requests
      to maintain context across compaction boundaries.

      When content is None, the block represents a failed compaction. The server
      treats these as no-ops. Empty string content is not allowed.

      - `content: string`

        Summary of previously compacted content, or null if compaction failed

      - `type: "compaction"`

      - `cache_control: optional object { type, ttl }`

        Create a cache control breakpoint at this content block.

        - `type: "ephemeral"`

        - `ttl: optional "5m" or "1h"`

          The time-to-live for the cache control breakpoint.

          This may be one the following values:

          - `5m`: 5 minutes
          - `1h`: 1 hour

          Defaults to `5m`.

          - `"5m"`

          - `"1h"`

      - `encrypted_content: optional string`

        Opaque metadata from prior compaction, to be round-tripped verbatim

  - `role: "user" or "assistant"`

    - `"user"`

    - `"assistant"`

### Beta Message Tokens Count

- `beta_message_tokens_count: object { context_management, input_tokens }`

  - `context_management: object { original_input_tokens }`

    Information about context management applied to the message.

    - `original_input_tokens: number`

      The original token count before context management was applied

  - `input_tokens: number`

    The total number of tokens across the provided list of messages, system prompt, and tools.

### Beta Metadata

- `beta_metadata: object { user_id }`

  - `user_id: optional string`

    An external identifier for the user who is associated with the request.

    This should be a uuid, hash value, or other opaque identifier. Anthropic may use this id to help detect abuse. Do not include any identifying information such as name, email address, or phone number.

### Beta Output Config

- `beta_output_config: object { effort, format, task_budget }`

  - `effort: optional "low" or "medium" or "high" or 2 more`

    All possible effort levels.

    - `"low"`

    - `"medium"`

    - `"high"`

    - `"xhigh"`

    - `"max"`

  - `format: optional object { schema, type }`

    A schema to specify Claude's output format in responses. See [structured outputs](https://platform.claude.com/docs/en/build-with-claude/structured-outputs)

    - `schema: map[unknown]`

      The JSON schema of the format

    - `type: "json_schema"`

  - `task_budget: optional object { total, type, remaining }`

    User-configurable total token budget across contexts.

    - `total: number`

      Total token budget across all contexts in the session.

    - `type: "tokens"`

      The budget type. Currently only 'tokens' is supported.

    - `remaining: optional number`

      Remaining tokens in the budget. Use this to track usage across contexts when implementing compaction client-side. Defaults to total if not provided.

### Beta Plain Text Source

- `beta_plain_text_source: object { data, media_type, type }`

  - `data: string`

  - `media_type: "text/plain"`

  - `type: "text"`

### Beta Raw Content Block Delta

- `beta_raw_content_block_delta: BetaTextDelta or BetaInputJSONDelta or BetaCitationsDelta or 3 more`

  - `beta_text_delta: object { text, type }`

    - `text: string`

    - `type: "text_delta"`

  - `beta_input_json_delta: object { partial_json, type }`

    - `partial_json: string`

    - `type: "input_json_delta"`

  - `beta_citations_delta: object { citation, type }`

    - `citation: BetaCitationCharLocation or BetaCitationPageLocation or BetaCitationContentBlockLocation or 2 more`

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

    - `type: "citations_delta"`

  - `beta_thinking_delta: object { thinking, type }`

    - `thinking: string`

    - `type: "thinking_delta"`

  - `beta_signature_delta: object { signature, type }`

    - `signature: string`

    - `type: "signature_delta"`

  - `beta_compaction_content_block_delta: object { content, encrypted_content, type }`

    - `content: string`

    - `encrypted_content: string`

      Opaque metadata from prior compaction, to be round-tripped verbatim

    - `type: "compaction_delta"`

### Beta Raw Content Block Delta Event

- `beta_raw_content_block_delta_event: object { delta, index, type }`

  - `delta: BetaTextDelta or BetaInputJSONDelta or BetaCitationsDelta or 3 more`

    - `beta_text_delta: object { text, type }`

      - `text: string`

      - `type: "text_delta"`

    - `beta_input_json_delta: object { partial_json, type }`

      - `partial_json: string`

      - `type: "input_json_delta"`

    - `beta_citations_delta: object { citation, type }`

      - `citation: BetaCitationCharLocation or BetaCitationPageLocation or BetaCitationContentBlockLocation or 2 more`

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

      - `type: "citations_delta"`

    - `beta_thinking_delta: object { thinking, type }`

      - `thinking: string`

      - `type: "thinking_delta"`

    - `beta_signature_delta: object { signature, type }`

      - `signature: string`

      - `type: "signature_delta"`

    - `beta_compaction_content_block_delta: object { content, encrypted_content, type }`

      - `content: string`

      - `encrypted_content: string`

        Opaque metadata from prior compaction, to be round-tripped verbatim

      - `type: "compaction_delta"`

  - `index: number`

  - `type: "content_block_delta"`

### Beta Raw Content Block Start Event

- `beta_raw_content_block_start_event: object { content_block, index, type }`

  - `content_block: BetaTextBlock or BetaThinkingBlock or BetaRedactedThinkingBlock or 13 more`

    Response model for a file uploaded to the container.

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

    - `beta_compaction_block: object { content, encrypted_content, type }`

      A compaction block returned when autocompact is triggered.

      When content is None, it indicates the compaction failed to produce a valid
      summary (e.g., malformed output from the model). Clients may round-trip
      compaction blocks with null content; the server treats them as no-ops.

      - `content: string`

        Summary of compacted content, or null if compaction failed

      - `encrypted_content: string`

        Opaque metadata from prior compaction, to be round-tripped verbatim

      - `type: "compaction"`

  - `index: number`

  - `type: "content_block_start"`

### Beta Raw Content Block Stop Event

- `beta_raw_content_block_stop_event: object { index, type }`

  - `index: number`

  - `type: "content_block_stop"`

### Beta Raw Message Delta Event

- `beta_raw_message_delta_event: object { context_management, delta, type, usage }`

  - `context_management: object { applied_edits }`

    Information about context management strategies applied during the request

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

  - `delta: object { container, stop_details, stop_reason, stop_sequence }`

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

      - `"end_turn"`

      - `"max_tokens"`

      - `"stop_sequence"`

      - `"tool_use"`

      - `"pause_turn"`

      - `"compaction"`

      - `"refusal"`

      - `"model_context_window_exceeded"`

    - `stop_sequence: string`

  - `type: "message_delta"`

  - `usage: object { cache_creation_input_tokens, cache_read_input_tokens, input_tokens, 3 more }`

    Billing and rate-limit usage.

    Anthropic's API bills and rate-limits by token counts, as tokens represent the underlying cost to our systems.

    Under the hood, the API transforms requests into a format suitable for the model. The model's output then goes through a parsing stage before becoming an API response. As a result, the token counts in `usage` will not match one-to-one with the exact visible content of an API request or response.

    For example, `output_tokens` will be non-zero, even for an empty string response from Claude.

    Total input tokens in a request is the summation of `input_tokens`, `cache_creation_input_tokens`, and `cache_read_input_tokens`.

    - `cache_creation_input_tokens: number`

      The cumulative number of input tokens used to create the cache entry.

    - `cache_read_input_tokens: number`

      The cumulative number of input tokens read from the cache.

    - `input_tokens: number`

      The cumulative number of input tokens which were used.

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

      The cumulative number of output tokens which were used.

    - `server_tool_use: object { web_fetch_requests, web_search_requests }`

      The number of server tool requests.

      - `web_fetch_requests: number`

        The number of web fetch tool requests.

      - `web_search_requests: number`

        The number of web search tool requests.

### Beta Raw Message Start Event

- `beta_raw_message_start_event: object { message, type }`

  - `message: object { id, container, content, 8 more }`

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

      - `beta_compaction_block: object { content, encrypted_content, type }`

        A compaction block returned when autocompact is triggered.

        When content is None, it indicates the compaction failed to produce a valid
        summary (e.g., malformed output from the model). Clients may round-trip
        compaction blocks with null content; the server treats them as no-ops.

        - `content: string`

          Summary of compacted content, or null if compaction failed

        - `encrypted_content: string`

          Opaque metadata from prior compaction, to be round-tripped verbatim

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

  - `type: "message_start"`

### Beta Raw Message Stop Event

- `beta_raw_message_stop_event: object { type }`

  - `type: "message_stop"`

### Beta Raw Message Stream Event

- `beta_raw_message_stream_event: BetaRawMessageStartEvent or BetaRawMessageDeltaEvent or BetaRawMessageStopEvent or 3 more`

  - `beta_raw_message_start_event: object { message, type }`

    - `message: object { id, container, content, 8 more }`

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

        - `beta_compaction_block: object { content, encrypted_content, type }`

          A compaction block returned when autocompact is triggered.

          When content is None, it indicates the compaction failed to produce a valid
          summary (e.g., malformed output from the model). Clients may round-trip
          compaction blocks with null content; the server treats them as no-ops.

          - `content: string`

            Summary of compacted content, or null if compaction failed

          - `encrypted_content: string`

            Opaque metadata from prior compaction, to be round-tripped verbatim

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

    - `type: "message_start"`

  - `beta_raw_message_delta_event: object { context_management, delta, type, usage }`

    - `context_management: object { applied_edits }`

      Information about context management strategies applied during the request

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

    - `delta: object { container, stop_details, stop_reason, stop_sequence }`

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

        - `"end_turn"`

        - `"max_tokens"`

        - `"stop_sequence"`

        - `"tool_use"`

        - `"pause_turn"`

        - `"compaction"`

        - `"refusal"`

        - `"model_context_window_exceeded"`

      - `stop_sequence: string`

    - `type: "message_delta"`

    - `usage: object { cache_creation_input_tokens, cache_read_input_tokens, input_tokens, 3 more }`

      Billing and rate-limit usage.

      Anthropic's API bills and rate-limits by token counts, as tokens represent the underlying cost to our systems.

      Under the hood, the API transforms requests into a format suitable for the model. The model's output then goes through a parsing stage before becoming an API response. As a result, the token counts in `usage` will not match one-to-one with the exact visible content of an API request or response.

      For example, `output_tokens` will be non-zero, even for an empty string response from Claude.

      Total input tokens in a request is the summation of `input_tokens`, `cache_creation_input_tokens`, and `cache_read_input_tokens`.

      - `cache_creation_input_tokens: number`

        The cumulative number of input tokens used to create the cache entry.

      - `cache_read_input_tokens: number`

        The cumulative number of input tokens read from the cache.

      - `input_tokens: number`

        The cumulative number of input tokens which were used.

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

        The cumulative number of output tokens which were used.

      - `server_tool_use: object { web_fetch_requests, web_search_requests }`

        The number of server tool requests.

        - `web_fetch_requests: number`

          The number of web fetch tool requests.

        - `web_search_requests: number`

          The number of web search tool requests.

  - `beta_raw_message_stop_event: object { type }`

    - `type: "message_stop"`

  - `beta_raw_content_block_start_event: object { content_block, index, type }`

    - `content_block: BetaTextBlock or BetaThinkingBlock or BetaRedactedThinkingBlock or 13 more`

      Response model for a file uploaded to the container.

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

      - `beta_compaction_block: object { content, encrypted_content, type }`

        A compaction block returned when autocompact is triggered.

        When content is None, it indicates the compaction failed to produce a valid
        summary (e.g., malformed output from the model). Clients may round-trip
        compaction blocks with null content; the server treats them as no-ops.

        - `content: string`

          Summary of compacted content, or null if compaction failed

        - `encrypted_content: string`

          Opaque metadata from prior compaction, to be round-tripped verbatim

        - `type: "compaction"`

    - `index: number`

    - `type: "content_block_start"`

  - `beta_raw_content_block_delta_event: object { delta, index, type }`

    - `delta: BetaTextDelta or BetaInputJSONDelta or BetaCitationsDelta or 3 more`

      - `beta_text_delta: object { text, type }`

        - `text: string`

        - `type: "text_delta"`

      - `beta_input_json_delta: object { partial_json, type }`

        - `partial_json: string`

        - `type: "input_json_delta"`

      - `beta_citations_delta: object { citation, type }`

        - `citation: BetaCitationCharLocation or BetaCitationPageLocation or BetaCitationContentBlockLocation or 2 more`

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

        - `type: "citations_delta"`

      - `beta_thinking_delta: object { thinking, type }`

        - `thinking: string`

        - `type: "thinking_delta"`

      - `beta_signature_delta: object { signature, type }`

        - `signature: string`

        - `type: "signature_delta"`

      - `beta_compaction_content_block_delta: object { content, encrypted_content, type }`

        - `content: string`

        - `encrypted_content: string`

          Opaque metadata from prior compaction, to be round-tripped verbatim

        - `type: "compaction_delta"`

    - `index: number`

    - `type: "content_block_delta"`

  - `beta_raw_content_block_stop_event: object { index, type }`

    - `index: number`

    - `type: "content_block_stop"`

### Beta Redacted Thinking Block

- `beta_redacted_thinking_block: object { data, type }`

  - `data: string`

  - `type: "redacted_thinking"`

### Beta Redacted Thinking Block Param

- `beta_redacted_thinking_block_param: object { data, type }`

  - `data: string`

  - `type: "redacted_thinking"`

### Beta Refusal Stop Details

- `beta_refusal_stop_details: object { category, explanation, type }`

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

### Beta Request Document Block

- `beta_request_document_block: object { source, type, cache_control, 3 more }`

  - `source: BetaBase64PDFSource or BetaPlainTextSource or BetaContentBlockSource or 2 more`

    - `beta_base64_pdf_source: object { data, media_type, type }`

      - `data: string`

      - `media_type: "application/pdf"`

      - `type: "base64"`

    - `beta_plain_text_source: object { data, media_type, type }`

      - `data: string`

      - `media_type: "text/plain"`

      - `type: "text"`

    - `beta_content_block_source: object { content, type }`

      - `content: string or array of BetaContentBlockSourceContent`

        - `union_member_0: string`

        - `beta_content_block_source_content: array of BetaContentBlockSourceContent`

          - `beta_text_block_param: object { text, type, cache_control, citations }`

            - `text: string`

            - `type: "text"`

            - `cache_control: optional object { type, ttl }`

              Create a cache control breakpoint at this content block.

              - `type: "ephemeral"`

              - `ttl: optional "5m" or "1h"`

                The time-to-live for the cache control breakpoint.

                This may be one the following values:

                - `5m`: 5 minutes
                - `1h`: 1 hour

                Defaults to `5m`.

                - `"5m"`

                - `"1h"`

            - `citations: optional array of BetaTextCitationParam`

              - `beta_citation_char_location_param: object { cited_text, document_index, document_title, 3 more }`

                - `cited_text: string`

                - `document_index: number`

                - `document_title: string`

                - `end_char_index: number`

                - `start_char_index: number`

                - `type: "char_location"`

              - `beta_citation_page_location_param: object { cited_text, document_index, document_title, 3 more }`

                - `cited_text: string`

                - `document_index: number`

                - `document_title: string`

                - `end_page_number: number`

                - `start_page_number: number`

                - `type: "page_location"`

              - `beta_citation_content_block_location_param: object { cited_text, document_index, document_title, 3 more }`

                - `cited_text: string`

                - `document_index: number`

                - `document_title: string`

                - `end_block_index: number`

                - `start_block_index: number`

                - `type: "content_block_location"`

              - `beta_citation_web_search_result_location_param: object { cited_text, encrypted_index, title, 2 more }`

                - `cited_text: string`

                - `encrypted_index: string`

                - `title: string`

                - `type: "web_search_result_location"`

                - `url: string`

              - `beta_citation_search_result_location_param: object { cited_text, end_block_index, search_result_index, 4 more }`

                - `cited_text: string`

                - `end_block_index: number`

                - `search_result_index: number`

                - `source: string`

                - `start_block_index: number`

                - `title: string`

                - `type: "search_result_location"`

          - `beta_image_block_param: object { source, type, cache_control }`

            - `source: BetaBase64ImageSource or BetaURLImageSource or BetaFileImageSource`

              - `beta_base64_image_source: object { data, media_type, type }`

                - `data: string`

                - `media_type: "image/jpeg" or "image/png" or "image/gif" or "image/webp"`

                  - `"image/jpeg"`

                  - `"image/png"`

                  - `"image/gif"`

                  - `"image/webp"`

                - `type: "base64"`

              - `beta_url_image_source: object { type, url }`

                - `type: "url"`

                - `url: string`

              - `beta_file_image_source: object { file_id, type }`

                - `file_id: string`

                - `type: "file"`

            - `type: "image"`

            - `cache_control: optional object { type, ttl }`

              Create a cache control breakpoint at this content block.

              - `type: "ephemeral"`

              - `ttl: optional "5m" or "1h"`

                The time-to-live for the cache control breakpoint.

                This may be one the following values:

                - `5m`: 5 minutes
                - `1h`: 1 hour

                Defaults to `5m`.

                - `"5m"`

                - `"1h"`

      - `type: "content"`

    - `beta_url_pdf_source: object { type, url }`

      - `type: "url"`

      - `url: string`

    - `beta_file_document_source: object { file_id, type }`

      - `file_id: string`

      - `type: "file"`

  - `type: "document"`

  - `cache_control: optional object { type, ttl }`

    Create a cache control breakpoint at this content block.

    - `type: "ephemeral"`

    - `ttl: optional "5m" or "1h"`

      The time-to-live for the cache control breakpoint.

      This may be one the following values:

      - `5m`: 5 minutes
      - `1h`: 1 hour

      Defaults to `5m`.

      - `"5m"`

      - `"1h"`

  - `citations: optional object { enabled }`

    - `enabled: optional boolean`

  - `context: optional string`

  - `title: optional string`

### Beta Request MCP Server Tool Configuration

- `beta_request_mcp_server_tool_configuration: object { allowed_tools, enabled }`

  - `allowed_tools: optional array of string`

  - `enabled: optional boolean`

### Beta Request MCP Server URL Definition

- `beta_request_mcp_server_url_definition: object { name, type, url, 2 more }`

  - `name: string`

  - `type: "url"`

  - `url: string`

  - `authorization_token: optional string`

  - `tool_configuration: optional object { allowed_tools, enabled }`

    - `allowed_tools: optional array of string`

    - `enabled: optional boolean`

### Beta Request MCP Tool Result Block Param

- `beta_request_mcp_tool_result_block_param: object { tool_use_id, type, cache_control, 2 more }`

  - `tool_use_id: string`

  - `type: "mcp_tool_result"`

  - `cache_control: optional object { type, ttl }`

    Create a cache control breakpoint at this content block.

    - `type: "ephemeral"`

    - `ttl: optional "5m" or "1h"`

      The time-to-live for the cache control breakpoint.

      This may be one the following values:

      - `5m`: 5 minutes
      - `1h`: 1 hour

      Defaults to `5m`.

      - `"5m"`

      - `"1h"`

  - `content: optional string or array of BetaTextBlockParam`

    - `union_member_0: string`

    - `beta_mcp_tool_result_block_param_content: array of BetaTextBlockParam`

      - `text: string`

      - `type: "text"`

      - `cache_control: optional object { type, ttl }`

        Create a cache control breakpoint at this content block.

        - `type: "ephemeral"`

        - `ttl: optional "5m" or "1h"`

          The time-to-live for the cache control breakpoint.

          This may be one the following values:

          - `5m`: 5 minutes
          - `1h`: 1 hour

          Defaults to `5m`.

          - `"5m"`

          - `"1h"`

      - `citations: optional array of BetaTextCitationParam`

        - `beta_citation_char_location_param: object { cited_text, document_index, document_title, 3 more }`

          - `cited_text: string`

          - `document_index: number`

          - `document_title: string`

          - `end_char_index: number`

          - `start_char_index: number`

          - `type: "char_location"`

        - `beta_citation_page_location_param: object { cited_text, document_index, document_title, 3 more }`

          - `cited_text: string`

          - `document_index: number`

          - `document_title: string`

          - `end_page_number: number`

          - `start_page_number: number`

          - `type: "page_location"`

        - `beta_citation_content_block_location_param: object { cited_text, document_index, document_title, 3 more }`

          - `cited_text: string`

          - `document_index: number`

          - `document_title: string`

          - `end_block_index: number`

          - `start_block_index: number`

          - `type: "content_block_location"`

        - `beta_citation_web_search_result_location_param: object { cited_text, encrypted_index, title, 2 more }`

          - `cited_text: string`

          - `encrypted_index: string`

          - `title: string`

          - `type: "web_search_result_location"`

          - `url: string`

        - `beta_citation_search_result_location_param: object { cited_text, end_block_index, search_result_index, 4 more }`

          - `cited_text: string`

          - `end_block_index: number`

          - `search_result_index: number`

          - `source: string`

          - `start_block_index: number`

          - `title: string`

          - `type: "search_result_location"`

  - `is_error: optional boolean`

### Beta Search Result Block Param

- `beta_search_result_block_param: object { content, source, title, 3 more }`

  - `content: array of BetaTextBlockParam`

    - `text: string`

    - `type: "text"`

    - `cache_control: optional object { type, ttl }`

      Create a cache control breakpoint at this content block.

      - `type: "ephemeral"`

      - `ttl: optional "5m" or "1h"`

        The time-to-live for the cache control breakpoint.

        This may be one the following values:

        - `5m`: 5 minutes
        - `1h`: 1 hour

        Defaults to `5m`.

        - `"5m"`

        - `"1h"`

    - `citations: optional array of BetaTextCitationParam`

      - `beta_citation_char_location_param: object { cited_text, document_index, document_title, 3 more }`

        - `cited_text: string`

        - `document_index: number`

        - `document_title: string`

        - `end_char_index: number`

        - `start_char_index: number`

        - `type: "char_location"`

      - `beta_citation_page_location_param: object { cited_text, document_index, document_title, 3 more }`

        - `cited_text: string`

        - `document_index: number`

        - `document_title: string`

        - `end_page_number: number`

        - `start_page_number: number`

        - `type: "page_location"`

      - `beta_citation_content_block_location_param: object { cited_text, document_index, document_title, 3 more }`

        - `cited_text: string`

        - `document_index: number`

        - `document_title: string`

        - `end_block_index: number`

        - `start_block_index: number`

        - `type: "content_block_location"`

      - `beta_citation_web_search_result_location_param: object { cited_text, encrypted_index, title, 2 more }`

        - `cited_text: string`

        - `encrypted_index: string`

        - `title: string`

        - `type: "web_search_result_location"`

        - `url: string`

      - `beta_citation_search_result_location_param: object { cited_text, end_block_index, search_result_index, 4 more }`

        - `cited_text: string`

        - `end_block_index: number`

        - `search_result_index: number`

        - `source: string`

        - `start_block_index: number`

        - `title: string`

        - `type: "search_result_location"`

  - `source: string`

  - `title: string`

  - `type: "search_result"`

  - `cache_control: optional object { type, ttl }`

    Create a cache control breakpoint at this content block.

    - `type: "ephemeral"`

    - `ttl: optional "5m" or "1h"`

      The time-to-live for the cache control breakpoint.

      This may be one the following values:

      - `5m`: 5 minutes
      - `1h`: 1 hour

      Defaults to `5m`.

      - `"5m"`

      - `"1h"`

  - `citations: optional object { enabled }`

    - `enabled: optional boolean`

### Beta Server Tool Caller

- `beta_server_tool_caller: object { tool_id, type }`

  Tool invocation generated by a server-side tool.

  - `tool_id: string`

  - `type: "code_execution_20250825"`

### Beta Server Tool Caller 20260120

- `beta_server_tool_caller_20260120: object { tool_id, type }`

  - `tool_id: string`

  - `type: "code_execution_20260120"`

### Beta Server Tool Usage

- `beta_server_tool_usage: object { web_fetch_requests, web_search_requests }`

  - `web_fetch_requests: number`

    The number of web fetch tool requests.

  - `web_search_requests: number`

    The number of web search tool requests.

### Beta Server Tool Use Block

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

### Beta Server Tool Use Block Param

- `beta_server_tool_use_block_param: object { id, input, name, 3 more }`

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

  - `cache_control: optional object { type, ttl }`

    Create a cache control breakpoint at this content block.

    - `type: "ephemeral"`

    - `ttl: optional "5m" or "1h"`

      The time-to-live for the cache control breakpoint.

      This may be one the following values:

      - `5m`: 5 minutes
      - `1h`: 1 hour

      Defaults to `5m`.

      - `"5m"`

      - `"1h"`

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

### Beta Signature Delta

- `beta_signature_delta: object { signature, type }`

  - `signature: string`

  - `type: "signature_delta"`

### Beta Skill

- `beta_skill: object { skill_id, type, version }`

  A skill that was loaded in a container (response model).

  - `skill_id: string`

    Skill ID

  - `type: "anthropic" or "custom"`

    Type of skill - either 'anthropic' (built-in) or 'custom' (user-defined)

    - `"anthropic"`

    - `"custom"`

  - `version: string`

    Skill version or 'latest' for most recent version

### Beta Skill Params

- `beta_skill_params: object { skill_id, type, version }`

  Specification for a skill to be loaded in a container (request model).

  - `skill_id: string`

    Skill ID

  - `type: "anthropic" or "custom"`

    Type of skill - either 'anthropic' (built-in) or 'custom' (user-defined)

    - `"anthropic"`

    - `"custom"`

  - `version: optional string`

    Skill version or 'latest' for most recent version

### Beta Stop Reason

- `beta_stop_reason: "end_turn" or "max_tokens" or "stop_sequence" or 5 more`

  - `"end_turn"`

  - `"max_tokens"`

  - `"stop_sequence"`

  - `"tool_use"`

  - `"pause_turn"`

  - `"compaction"`

  - `"refusal"`

  - `"model_context_window_exceeded"`

### Beta Text Block

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

### Beta Text Block Param

- `beta_text_block_param: object { text, type, cache_control, citations }`

  - `text: string`

  - `type: "text"`

  - `cache_control: optional object { type, ttl }`

    Create a cache control breakpoint at this content block.

    - `type: "ephemeral"`

    - `ttl: optional "5m" or "1h"`

      The time-to-live for the cache control breakpoint.

      This may be one the following values:

      - `5m`: 5 minutes
      - `1h`: 1 hour

      Defaults to `5m`.

      - `"5m"`

      - `"1h"`

  - `citations: optional array of BetaTextCitationParam`

    - `beta_citation_char_location_param: object { cited_text, document_index, document_title, 3 more }`

      - `cited_text: string`

      - `document_index: number`

      - `document_title: string`

      - `end_char_index: number`

      - `start_char_index: number`

      - `type: "char_location"`

    - `beta_citation_page_location_param: object { cited_text, document_index, document_title, 3 more }`

      - `cited_text: string`

      - `document_index: number`

      - `document_title: string`

      - `end_page_number: number`

      - `start_page_number: number`

      - `type: "page_location"`

    - `beta_citation_content_block_location_param: object { cited_text, document_index, document_title, 3 more }`

      - `cited_text: string`

      - `document_index: number`

      - `document_title: string`

      - `end_block_index: number`

      - `start_block_index: number`

      - `type: "content_block_location"`

    - `beta_citation_web_search_result_location_param: object { cited_text, encrypted_index, title, 2 more }`

      - `cited_text: string`

      - `encrypted_index: string`

      - `title: string`

      - `type: "web_search_result_location"`

      - `url: string`

    - `beta_citation_search_result_location_param: object { cited_text, end_block_index, search_result_index, 4 more }`

      - `cited_text: string`

      - `end_block_index: number`

      - `search_result_index: number`

      - `source: string`

      - `start_block_index: number`

      - `title: string`

      - `type: "search_result_location"`

### Beta Text Citation

- `beta_text_citation: BetaCitationCharLocation or BetaCitationPageLocation or BetaCitationContentBlockLocation or 2 more`

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

### Beta Text Citation Param

- `beta_text_citation_param: BetaCitationCharLocationParam or BetaCitationPageLocationParam or BetaCitationContentBlockLocationParam or 2 more`

  - `beta_citation_char_location_param: object { cited_text, document_index, document_title, 3 more }`

    - `cited_text: string`

    - `document_index: number`

    - `document_title: string`

    - `end_char_index: number`

    - `start_char_index: number`

    - `type: "char_location"`

  - `beta_citation_page_location_param: object { cited_text, document_index, document_title, 3 more }`

    - `cited_text: string`

    - `document_index: number`

    - `document_title: string`

    - `end_page_number: number`

    - `start_page_number: number`

    - `type: "page_location"`

  - `beta_citation_content_block_location_param: object { cited_text, document_index, document_title, 3 more }`

    - `cited_text: string`

    - `document_index: number`

    - `document_title: string`

    - `end_block_index: number`

    - `start_block_index: number`

    - `type: "content_block_location"`

  - `beta_citation_web_search_result_location_param: object { cited_text, encrypted_index, title, 2 more }`

    - `cited_text: string`

    - `encrypted_index: string`

    - `title: string`

    - `type: "web_search_result_location"`

    - `url: string`

  - `beta_citation_search_result_location_param: object { cited_text, end_block_index, search_result_index, 4 more }`

    - `cited_text: string`

    - `end_block_index: number`

    - `search_result_index: number`

    - `source: string`

    - `start_block_index: number`

    - `title: string`

    - `type: "search_result_location"`

### Beta Text Delta

- `beta_text_delta: object { text, type }`

  - `text: string`

  - `type: "text_delta"`

### Beta Text Editor Code Execution Create Result Block

- `beta_text_editor_code_execution_create_result_block: object { is_file_update, type }`

  - `is_file_update: boolean`

  - `type: "text_editor_code_execution_create_result"`

### Beta Text Editor Code Execution Create Result Block Param

- `beta_text_editor_code_execution_create_result_block_param: object { is_file_update, type }`

  - `is_file_update: boolean`

  - `type: "text_editor_code_execution_create_result"`

### Beta Text Editor Code Execution Str Replace Result Block

- `beta_text_editor_code_execution_str_replace_result_block: object { lines, new_lines, new_start, 3 more }`

  - `lines: array of string`

  - `new_lines: number`

  - `new_start: number`

  - `old_lines: number`

  - `old_start: number`

  - `type: "text_editor_code_execution_str_replace_result"`

### Beta Text Editor Code Execution Str Replace Result Block Param

- `beta_text_editor_code_execution_str_replace_result_block_param: object { type, lines, new_lines, 3 more }`

  - `type: "text_editor_code_execution_str_replace_result"`

  - `lines: optional array of string`

  - `new_lines: optional number`

  - `new_start: optional number`

  - `old_lines: optional number`

  - `old_start: optional number`

### Beta Text Editor Code Execution Tool Result Block

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

### Beta Text Editor Code Execution Tool Result Block Param

- `beta_text_editor_code_execution_tool_result_block_param: object { content, tool_use_id, type, cache_control }`

  - `content: BetaTextEditorCodeExecutionToolResultErrorParam or BetaTextEditorCodeExecutionViewResultBlockParam or BetaTextEditorCodeExecutionCreateResultBlockParam or BetaTextEditorCodeExecutionStrReplaceResultBlockParam`

    - `beta_text_editor_code_execution_tool_result_error_param: object { error_code, type, error_message }`

      - `error_code: "invalid_tool_input" or "unavailable" or "too_many_requests" or 2 more`

        - `"invalid_tool_input"`

        - `"unavailable"`

        - `"too_many_requests"`

        - `"execution_time_exceeded"`

        - `"file_not_found"`

      - `type: "text_editor_code_execution_tool_result_error"`

      - `error_message: optional string`

    - `beta_text_editor_code_execution_view_result_block_param: object { content, file_type, type, 3 more }`

      - `content: string`

      - `file_type: "text" or "image" or "pdf"`

        - `"text"`

        - `"image"`

        - `"pdf"`

      - `type: "text_editor_code_execution_view_result"`

      - `num_lines: optional number`

      - `start_line: optional number`

      - `total_lines: optional number`

    - `beta_text_editor_code_execution_create_result_block_param: object { is_file_update, type }`

      - `is_file_update: boolean`

      - `type: "text_editor_code_execution_create_result"`

    - `beta_text_editor_code_execution_str_replace_result_block_param: object { type, lines, new_lines, 3 more }`

      - `type: "text_editor_code_execution_str_replace_result"`

      - `lines: optional array of string`

      - `new_lines: optional number`

      - `new_start: optional number`

      - `old_lines: optional number`

      - `old_start: optional number`

  - `tool_use_id: string`

  - `type: "text_editor_code_execution_tool_result"`

  - `cache_control: optional object { type, ttl }`

    Create a cache control breakpoint at this content block.

    - `type: "ephemeral"`

    - `ttl: optional "5m" or "1h"`

      The time-to-live for the cache control breakpoint.

      This may be one the following values:

      - `5m`: 5 minutes
      - `1h`: 1 hour

      Defaults to `5m`.

      - `"5m"`

      - `"1h"`

### Beta Text Editor Code Execution Tool Result Error

- `beta_text_editor_code_execution_tool_result_error: object { error_code, error_message, type }`

  - `error_code: "invalid_tool_input" or "unavailable" or "too_many_requests" or 2 more`

    - `"invalid_tool_input"`

    - `"unavailable"`

    - `"too_many_requests"`

    - `"execution_time_exceeded"`

    - `"file_not_found"`

  - `error_message: string`

  - `type: "text_editor_code_execution_tool_result_error"`

### Beta Text Editor Code Execution Tool Result Error Param

- `beta_text_editor_code_execution_tool_result_error_param: object { error_code, type, error_message }`

  - `error_code: "invalid_tool_input" or "unavailable" or "too_many_requests" or 2 more`

    - `"invalid_tool_input"`

    - `"unavailable"`

    - `"too_many_requests"`

    - `"execution_time_exceeded"`

    - `"file_not_found"`

  - `type: "text_editor_code_execution_tool_result_error"`

  - `error_message: optional string`

### Beta Text Editor Code Execution View Result Block

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

### Beta Text Editor Code Execution View Result Block Param

- `beta_text_editor_code_execution_view_result_block_param: object { content, file_type, type, 3 more }`

  - `content: string`

  - `file_type: "text" or "image" or "pdf"`

    - `"text"`

    - `"image"`

    - `"pdf"`

  - `type: "text_editor_code_execution_view_result"`

  - `num_lines: optional number`

  - `start_line: optional number`

  - `total_lines: optional number`

### Beta Thinking Block

- `beta_thinking_block: object { signature, thinking, type }`

  - `signature: string`

  - `thinking: string`

  - `type: "thinking"`

### Beta Thinking Block Param

- `beta_thinking_block_param: object { signature, thinking, type }`

  - `signature: string`

  - `thinking: string`

  - `type: "thinking"`

### Beta Thinking Config Adaptive

- `beta_thinking_config_adaptive: object { type, display }`

  - `type: "adaptive"`

  - `display: optional "summarized" or "omitted"`

    Controls how thinking content appears in the response. When set to `summarized`, thinking is returned normally. When set to `omitted`, thinking content is redacted but a signature is returned for multi-turn continuity. Defaults to `summarized`.

    - `"summarized"`

    - `"omitted"`

### Beta Thinking Config Disabled

- `beta_thinking_config_disabled: object { type }`

  - `type: "disabled"`

### Beta Thinking Config Enabled

- `beta_thinking_config_enabled: object { budget_tokens, type, display }`

  - `budget_tokens: number`

    Determines how many tokens Claude can use for its internal reasoning process. Larger budgets can enable more thorough analysis for complex problems, improving response quality.

    Must be ≥1024 and less than `max_tokens`.

    See [extended thinking](https://docs.claude.com/en/docs/build-with-claude/extended-thinking) for details.

  - `type: "enabled"`

  - `display: optional "summarized" or "omitted"`

    Controls how thinking content appears in the response. When set to `summarized`, thinking is returned normally. When set to `omitted`, thinking content is redacted but a signature is returned for multi-turn continuity. Defaults to `summarized`.

    - `"summarized"`

    - `"omitted"`

### Beta Thinking Config Param

- `beta_thinking_config_param: BetaThinkingConfigEnabled or BetaThinkingConfigDisabled or BetaThinkingConfigAdaptive`

  Configuration for enabling Claude's extended thinking.

  When enabled, responses include `thinking` content blocks showing Claude's thinking process before the final answer. Requires a minimum budget of 1,024 tokens and counts towards your `max_tokens` limit.

  See [extended thinking](https://docs.claude.com/en/docs/build-with-claude/extended-thinking) for details.

  - `beta_thinking_config_enabled: object { budget_tokens, type, display }`

    - `budget_tokens: number`

      Determines how many tokens Claude can use for its internal reasoning process. Larger budgets can enable more thorough analysis for complex problems, improving response quality.

      Must be ≥1024 and less than `max_tokens`.

      See [extended thinking](https://docs.claude.com/en/docs/build-with-claude/extended-thinking) for details.

    - `type: "enabled"`

    - `display: optional "summarized" or "omitted"`

      Controls how thinking content appears in the response. When set to `summarized`, thinking is returned normally. When set to `omitted`, thinking content is redacted but a signature is returned for multi-turn continuity. Defaults to `summarized`.

      - `"summarized"`

      - `"omitted"`

  - `beta_thinking_config_disabled: object { type }`

    - `type: "disabled"`

  - `beta_thinking_config_adaptive: object { type, display }`

    - `type: "adaptive"`

    - `display: optional "summarized" or "omitted"`

      Controls how thinking content appears in the response. When set to `summarized`, thinking is returned normally. When set to `omitted`, thinking content is redacted but a signature is returned for multi-turn continuity. Defaults to `summarized`.

      - `"summarized"`

      - `"omitted"`

### Beta Thinking Delta

- `beta_thinking_delta: object { thinking, type }`

  - `thinking: string`

  - `type: "thinking_delta"`

### Beta Thinking Turns

- `beta_thinking_turns: object { type, value }`

  - `type: "thinking_turns"`

  - `value: number`

### Beta Token Task Budget

- `beta_token_task_budget: object { total, type, remaining }`

  User-configurable total token budget across contexts.

  - `total: number`

    Total token budget across all contexts in the session.

  - `type: "tokens"`

    The budget type. Currently only 'tokens' is supported.

  - `remaining: optional number`

    Remaining tokens in the budget. Use this to track usage across contexts when implementing compaction client-side. Defaults to total if not provided.

### Beta Tool

- `beta_tool: object { input_schema, name, allowed_callers, 7 more }`

  - `input_schema: object { type, properties, required }`

    [JSON schema](https://json-schema.org/draft/2020-12) for this tool's input.

    This defines the shape of the `input` that your tool accepts and that the model will produce.

    - `type: "object"`

    - `properties: optional map[unknown]`

    - `required: optional array of string`

  - `name: string`

    Name of the tool.

    This is how the tool will be called by the model and in `tool_use` blocks.

  - `allowed_callers: optional array of "direct" or "code_execution_20250825" or "code_execution_20260120"`

    - `"direct"`

    - `"code_execution_20250825"`

    - `"code_execution_20260120"`

  - `cache_control: optional object { type, ttl }`

    Create a cache control breakpoint at this content block.

    - `type: "ephemeral"`

    - `ttl: optional "5m" or "1h"`

      The time-to-live for the cache control breakpoint.

      This may be one the following values:

      - `5m`: 5 minutes
      - `1h`: 1 hour

      Defaults to `5m`.

      - `"5m"`

      - `"1h"`

  - `defer_loading: optional boolean`

    If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

  - `description: optional string`

    Description of what this tool does.

    Tool descriptions should be as detailed as possible. The more information that the model has about what the tool is and how to use it, the better it will perform. You can use natural language descriptions to reinforce important aspects of the tool input JSON schema.

  - `eager_input_streaming: optional boolean`

    Enable eager input streaming for this tool. When true, tool input parameters will be streamed incrementally as they are generated, and types will be inferred on-the-fly rather than buffering the full JSON output. When false, streaming is disabled for this tool even if the fine-grained-tool-streaming beta is active. When null (default), uses the default behavior based on beta headers.

  - `input_examples: optional array of map[unknown]`

  - `strict: optional boolean`

    When true, guarantees schema validation on tool names and inputs

  - `type: optional "custom"`

    - `"custom"`

### Beta Tool Bash 20241022

- `beta_tool_bash_20241022: object { name, type, allowed_callers, 4 more }`

  - `name: "bash"`

    Name of the tool.

    This is how the tool will be called by the model and in `tool_use` blocks.

  - `type: "bash_20241022"`

  - `allowed_callers: optional array of "direct" or "code_execution_20250825" or "code_execution_20260120"`

    - `"direct"`

    - `"code_execution_20250825"`

    - `"code_execution_20260120"`

  - `cache_control: optional object { type, ttl }`

    Create a cache control breakpoint at this content block.

    - `type: "ephemeral"`

    - `ttl: optional "5m" or "1h"`

      The time-to-live for the cache control breakpoint.

      This may be one the following values:

      - `5m`: 5 minutes
      - `1h`: 1 hour

      Defaults to `5m`.

      - `"5m"`

      - `"1h"`

  - `defer_loading: optional boolean`

    If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

  - `input_examples: optional array of map[unknown]`

  - `strict: optional boolean`

    When true, guarantees schema validation on tool names and inputs

### Beta Tool Bash 20250124

- `beta_tool_bash_20250124: object { name, type, allowed_callers, 4 more }`

  - `name: "bash"`

    Name of the tool.

    This is how the tool will be called by the model and in `tool_use` blocks.

  - `type: "bash_20250124"`

  - `allowed_callers: optional array of "direct" or "code_execution_20250825" or "code_execution_20260120"`

    - `"direct"`

    - `"code_execution_20250825"`

    - `"code_execution_20260120"`

  - `cache_control: optional object { type, ttl }`

    Create a cache control breakpoint at this content block.

    - `type: "ephemeral"`

    - `ttl: optional "5m" or "1h"`

      The time-to-live for the cache control breakpoint.

      This may be one the following values:

      - `5m`: 5 minutes
      - `1h`: 1 hour

      Defaults to `5m`.

      - `"5m"`

      - `"1h"`

  - `defer_loading: optional boolean`

    If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

  - `input_examples: optional array of map[unknown]`

  - `strict: optional boolean`

    When true, guarantees schema validation on tool names and inputs

### Beta Tool Choice

- `beta_tool_choice: BetaToolChoiceAuto or BetaToolChoiceAny or BetaToolChoiceTool or BetaToolChoiceNone`

  How the model should use the provided tools. The model can use a specific tool, any available tool, decide by itself, or not use tools at all.

  - `beta_tool_choice_auto: object { type, disable_parallel_tool_use }`

    The model will automatically decide whether to use tools.

    - `type: "auto"`

    - `disable_parallel_tool_use: optional boolean`

      Whether to disable parallel tool use.

      Defaults to `false`. If set to `true`, the model will output at most one tool use.

  - `beta_tool_choice_any: object { type, disable_parallel_tool_use }`

    The model will use any available tools.

    - `type: "any"`

    - `disable_parallel_tool_use: optional boolean`

      Whether to disable parallel tool use.

      Defaults to `false`. If set to `true`, the model will output exactly one tool use.

  - `beta_tool_choice_tool: object { name, type, disable_parallel_tool_use }`

    The model will use the specified tool with `tool_choice.name`.

    - `name: string`

      The name of the tool to use.

    - `type: "tool"`

    - `disable_parallel_tool_use: optional boolean`

      Whether to disable parallel tool use.

      Defaults to `false`. If set to `true`, the model will output exactly one tool use.

  - `beta_tool_choice_none: object { type }`

    The model will not be allowed to use tools.

    - `type: "none"`

### Beta Tool Choice Any

- `beta_tool_choice_any: object { type, disable_parallel_tool_use }`

  The model will use any available tools.

  - `type: "any"`

  - `disable_parallel_tool_use: optional boolean`

    Whether to disable parallel tool use.

    Defaults to `false`. If set to `true`, the model will output exactly one tool use.

### Beta Tool Choice Auto

- `beta_tool_choice_auto: object { type, disable_parallel_tool_use }`

  The model will automatically decide whether to use tools.

  - `type: "auto"`

  - `disable_parallel_tool_use: optional boolean`

    Whether to disable parallel tool use.

    Defaults to `false`. If set to `true`, the model will output at most one tool use.

### Beta Tool Choice None

- `beta_tool_choice_none: object { type }`

  The model will not be allowed to use tools.

  - `type: "none"`

### Beta Tool Choice Tool

- `beta_tool_choice_tool: object { name, type, disable_parallel_tool_use }`

  The model will use the specified tool with `tool_choice.name`.

  - `name: string`

    The name of the tool to use.

  - `type: "tool"`

  - `disable_parallel_tool_use: optional boolean`

    Whether to disable parallel tool use.

    Defaults to `false`. If set to `true`, the model will output exactly one tool use.

### Beta Tool Computer Use 20241022

- `beta_tool_computer_use_20241022: object { display_height_px, display_width_px, name, 7 more }`

  - `display_height_px: number`

    The height of the display in pixels.

  - `display_width_px: number`

    The width of the display in pixels.

  - `name: "computer"`

    Name of the tool.

    This is how the tool will be called by the model and in `tool_use` blocks.

  - `type: "computer_20241022"`

  - `allowed_callers: optional array of "direct" or "code_execution_20250825" or "code_execution_20260120"`

    - `"direct"`

    - `"code_execution_20250825"`

    - `"code_execution_20260120"`

  - `cache_control: optional object { type, ttl }`

    Create a cache control breakpoint at this content block.

    - `type: "ephemeral"`

    - `ttl: optional "5m" or "1h"`

      The time-to-live for the cache control breakpoint.

      This may be one the following values:

      - `5m`: 5 minutes
      - `1h`: 1 hour

      Defaults to `5m`.

      - `"5m"`

      - `"1h"`

  - `defer_loading: optional boolean`

    If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

  - `display_number: optional number`

    The X11 display number (e.g. 0, 1) for the display.

  - `input_examples: optional array of map[unknown]`

  - `strict: optional boolean`

    When true, guarantees schema validation on tool names and inputs

### Beta Tool Computer Use 20250124

- `beta_tool_computer_use_20250124: object { display_height_px, display_width_px, name, 7 more }`

  - `display_height_px: number`

    The height of the display in pixels.

  - `display_width_px: number`

    The width of the display in pixels.

  - `name: "computer"`

    Name of the tool.

    This is how the tool will be called by the model and in `tool_use` blocks.

  - `type: "computer_20250124"`

  - `allowed_callers: optional array of "direct" or "code_execution_20250825" or "code_execution_20260120"`

    - `"direct"`

    - `"code_execution_20250825"`

    - `"code_execution_20260120"`

  - `cache_control: optional object { type, ttl }`

    Create a cache control breakpoint at this content block.

    - `type: "ephemeral"`

    - `ttl: optional "5m" or "1h"`

      The time-to-live for the cache control breakpoint.

      This may be one the following values:

      - `5m`: 5 minutes
      - `1h`: 1 hour

      Defaults to `5m`.

      - `"5m"`

      - `"1h"`

  - `defer_loading: optional boolean`

    If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

  - `display_number: optional number`

    The X11 display number (e.g. 0, 1) for the display.

  - `input_examples: optional array of map[unknown]`

  - `strict: optional boolean`

    When true, guarantees schema validation on tool names and inputs

### Beta Tool Computer Use 20251124

- `beta_tool_computer_use_20251124: object { display_height_px, display_width_px, name, 8 more }`

  - `display_height_px: number`

    The height of the display in pixels.

  - `display_width_px: number`

    The width of the display in pixels.

  - `name: "computer"`

    Name of the tool.

    This is how the tool will be called by the model and in `tool_use` blocks.

  - `type: "computer_20251124"`

  - `allowed_callers: optional array of "direct" or "code_execution_20250825" or "code_execution_20260120"`

    - `"direct"`

    - `"code_execution_20250825"`

    - `"code_execution_20260120"`

  - `cache_control: optional object { type, ttl }`

    Create a cache control breakpoint at this content block.

    - `type: "ephemeral"`

    - `ttl: optional "5m" or "1h"`

      The time-to-live for the cache control breakpoint.

      This may be one the following values:

      - `5m`: 5 minutes
      - `1h`: 1 hour

      Defaults to `5m`.

      - `"5m"`

      - `"1h"`

  - `defer_loading: optional boolean`

    If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

  - `display_number: optional number`

    The X11 display number (e.g. 0, 1) for the display.

  - `enable_zoom: optional boolean`

    Whether to enable an action to take a zoomed-in screenshot of the screen.

  - `input_examples: optional array of map[unknown]`

  - `strict: optional boolean`

    When true, guarantees schema validation on tool names and inputs

### Beta Tool Reference Block

- `beta_tool_reference_block: object { tool_name, type }`

  - `tool_name: string`

  - `type: "tool_reference"`

### Beta Tool Reference Block Param

- `beta_tool_reference_block_param: object { tool_name, type, cache_control }`

  Tool reference block that can be included in tool_result content.

  - `tool_name: string`

  - `type: "tool_reference"`

  - `cache_control: optional object { type, ttl }`

    Create a cache control breakpoint at this content block.

    - `type: "ephemeral"`

    - `ttl: optional "5m" or "1h"`

      The time-to-live for the cache control breakpoint.

      This may be one the following values:

      - `5m`: 5 minutes
      - `1h`: 1 hour

      Defaults to `5m`.

      - `"5m"`

      - `"1h"`

### Beta Tool Result Block Param

- `beta_tool_result_block_param: object { tool_use_id, type, cache_control, 2 more }`

  - `tool_use_id: string`

  - `type: "tool_result"`

  - `cache_control: optional object { type, ttl }`

    Create a cache control breakpoint at this content block.

    - `type: "ephemeral"`

    - `ttl: optional "5m" or "1h"`

      The time-to-live for the cache control breakpoint.

      This may be one the following values:

      - `5m`: 5 minutes
      - `1h`: 1 hour

      Defaults to `5m`.

      - `"5m"`

      - `"1h"`

  - `content: optional array of BetaTextBlockParam or BetaImageBlockParam or BetaSearchResultBlockParam or 2 more`

    - `beta_text_block_param: object { text, type, cache_control, citations }`

      - `text: string`

      - `type: "text"`

      - `cache_control: optional object { type, ttl }`

        Create a cache control breakpoint at this content block.

        - `type: "ephemeral"`

        - `ttl: optional "5m" or "1h"`

          The time-to-live for the cache control breakpoint.

          This may be one the following values:

          - `5m`: 5 minutes
          - `1h`: 1 hour

          Defaults to `5m`.

          - `"5m"`

          - `"1h"`

      - `citations: optional array of BetaTextCitationParam`

        - `beta_citation_char_location_param: object { cited_text, document_index, document_title, 3 more }`

          - `cited_text: string`

          - `document_index: number`

          - `document_title: string`

          - `end_char_index: number`

          - `start_char_index: number`

          - `type: "char_location"`

        - `beta_citation_page_location_param: object { cited_text, document_index, document_title, 3 more }`

          - `cited_text: string`

          - `document_index: number`

          - `document_title: string`

          - `end_page_number: number`

          - `start_page_number: number`

          - `type: "page_location"`

        - `beta_citation_content_block_location_param: object { cited_text, document_index, document_title, 3 more }`

          - `cited_text: string`

          - `document_index: number`

          - `document_title: string`

          - `end_block_index: number`

          - `start_block_index: number`

          - `type: "content_block_location"`

        - `beta_citation_web_search_result_location_param: object { cited_text, encrypted_index, title, 2 more }`

          - `cited_text: string`

          - `encrypted_index: string`

          - `title: string`

          - `type: "web_search_result_location"`

          - `url: string`

        - `beta_citation_search_result_location_param: object { cited_text, end_block_index, search_result_index, 4 more }`

          - `cited_text: string`

          - `end_block_index: number`

          - `search_result_index: number`

          - `source: string`

          - `start_block_index: number`

          - `title: string`

          - `type: "search_result_location"`

    - `beta_image_block_param: object { source, type, cache_control }`

      - `source: BetaBase64ImageSource or BetaURLImageSource or BetaFileImageSource`

        - `beta_base64_image_source: object { data, media_type, type }`

          - `data: string`

          - `media_type: "image/jpeg" or "image/png" or "image/gif" or "image/webp"`

            - `"image/jpeg"`

            - `"image/png"`

            - `"image/gif"`

            - `"image/webp"`

          - `type: "base64"`

        - `beta_url_image_source: object { type, url }`

          - `type: "url"`

          - `url: string`

        - `beta_file_image_source: object { file_id, type }`

          - `file_id: string`

          - `type: "file"`

      - `type: "image"`

      - `cache_control: optional object { type, ttl }`

        Create a cache control breakpoint at this content block.

        - `type: "ephemeral"`

        - `ttl: optional "5m" or "1h"`

          The time-to-live for the cache control breakpoint.

          This may be one the following values:

          - `5m`: 5 minutes
          - `1h`: 1 hour

          Defaults to `5m`.

          - `"5m"`

          - `"1h"`

    - `beta_search_result_block_param: object { content, source, title, 3 more }`

      - `content: array of BetaTextBlockParam`

        - `text: string`

        - `type: "text"`

        - `cache_control: optional object { type, ttl }`

          Create a cache control breakpoint at this content block.

          - `type: "ephemeral"`

          - `ttl: optional "5m" or "1h"`

            The time-to-live for the cache control breakpoint.

            This may be one the following values:

            - `5m`: 5 minutes
            - `1h`: 1 hour

            Defaults to `5m`.

            - `"5m"`

            - `"1h"`

        - `citations: optional array of BetaTextCitationParam`

          - `beta_citation_char_location_param: object { cited_text, document_index, document_title, 3 more }`

            - `cited_text: string`

            - `document_index: number`

            - `document_title: string`

            - `end_char_index: number`

            - `start_char_index: number`

            - `type: "char_location"`

          - `beta_citation_page_location_param: object { cited_text, document_index, document_title, 3 more }`

            - `cited_text: string`

            - `document_index: number`

            - `document_title: string`

            - `end_page_number: number`

            - `start_page_number: number`

            - `type: "page_location"`

          - `beta_citation_content_block_location_param: object { cited_text, document_index, document_title, 3 more }`

            - `cited_text: string`

            - `document_index: number`

            - `document_title: string`

            - `end_block_index: number`

            - `start_block_index: number`

            - `type: "content_block_location"`

          - `beta_citation_web_search_result_location_param: object { cited_text, encrypted_index, title, 2 more }`

            - `cited_text: string`

            - `encrypted_index: string`

            - `title: string`

            - `type: "web_search_result_location"`

            - `url: string`

          - `beta_citation_search_result_location_param: object { cited_text, end_block_index, search_result_index, 4 more }`

            - `cited_text: string`

            - `end_block_index: number`

            - `search_result_index: number`

            - `source: string`

            - `start_block_index: number`

            - `title: string`

            - `type: "search_result_location"`

      - `source: string`

      - `title: string`

      - `type: "search_result"`

      - `cache_control: optional object { type, ttl }`

        Create a cache control breakpoint at this content block.

        - `type: "ephemeral"`

        - `ttl: optional "5m" or "1h"`

          The time-to-live for the cache control breakpoint.

          This may be one the following values:

          - `5m`: 5 minutes
          - `1h`: 1 hour

          Defaults to `5m`.

          - `"5m"`

          - `"1h"`

      - `citations: optional object { enabled }`

        - `enabled: optional boolean`

    - `beta_request_document_block: object { source, type, cache_control, 3 more }`

      - `source: BetaBase64PDFSource or BetaPlainTextSource or BetaContentBlockSource or 2 more`

        - `beta_base64_pdf_source: object { data, media_type, type }`

          - `data: string`

          - `media_type: "application/pdf"`

          - `type: "base64"`

        - `beta_plain_text_source: object { data, media_type, type }`

          - `data: string`

          - `media_type: "text/plain"`

          - `type: "text"`

        - `beta_content_block_source: object { content, type }`

          - `content: string or array of BetaContentBlockSourceContent`

            - `union_member_0: string`

            - `beta_content_block_source_content: array of BetaContentBlockSourceContent`

              - `beta_text_block_param: object { text, type, cache_control, citations }`

                - `text: string`

                - `type: "text"`

                - `cache_control: optional object { type, ttl }`

                  Create a cache control breakpoint at this content block.

                  - `type: "ephemeral"`

                  - `ttl: optional "5m" or "1h"`

                    The time-to-live for the cache control breakpoint.

                    This may be one the following values:

                    - `5m`: 5 minutes
                    - `1h`: 1 hour

                    Defaults to `5m`.

                    - `"5m"`

                    - `"1h"`

                - `citations: optional array of BetaTextCitationParam`

                  - `beta_citation_char_location_param: object { cited_text, document_index, document_title, 3 more }`

                    - `cited_text: string`

                    - `document_index: number`

                    - `document_title: string`

                    - `end_char_index: number`

                    - `start_char_index: number`

                    - `type: "char_location"`

                  - `beta_citation_page_location_param: object { cited_text, document_index, document_title, 3 more }`

                    - `cited_text: string`

                    - `document_index: number`

                    - `document_title: string`

                    - `end_page_number: number`

                    - `start_page_number: number`

                    - `type: "page_location"`

                  - `beta_citation_content_block_location_param: object { cited_text, document_index, document_title, 3 more }`

                    - `cited_text: string`

                    - `document_index: number`

                    - `document_title: string`

                    - `end_block_index: number`

                    - `start_block_index: number`

                    - `type: "content_block_location"`

                  - `beta_citation_web_search_result_location_param: object { cited_text, encrypted_index, title, 2 more }`

                    - `cited_text: string`

                    - `encrypted_index: string`

                    - `title: string`

                    - `type: "web_search_result_location"`

                    - `url: string`

                  - `beta_citation_search_result_location_param: object { cited_text, end_block_index, search_result_index, 4 more }`

                    - `cited_text: string`

                    - `end_block_index: number`

                    - `search_result_index: number`

                    - `source: string`

                    - `start_block_index: number`

                    - `title: string`

                    - `type: "search_result_location"`

              - `beta_image_block_param: object { source, type, cache_control }`

                - `source: BetaBase64ImageSource or BetaURLImageSource or BetaFileImageSource`

                  - `beta_base64_image_source: object { data, media_type, type }`

                    - `data: string`

                    - `media_type: "image/jpeg" or "image/png" or "image/gif" or "image/webp"`

                      - `"image/jpeg"`

                      - `"image/png"`

                      - `"image/gif"`

                      - `"image/webp"`

                    - `type: "base64"`

                  - `beta_url_image_source: object { type, url }`

                    - `type: "url"`

                    - `url: string`

                  - `beta_file_image_source: object { file_id, type }`

                    - `file_id: string`

                    - `type: "file"`

                - `type: "image"`

                - `cache_control: optional object { type, ttl }`

                  Create a cache control breakpoint at this content block.

                  - `type: "ephemeral"`

                  - `ttl: optional "5m" or "1h"`

                    The time-to-live for the cache control breakpoint.

                    This may be one the following values:

                    - `5m`: 5 minutes
                    - `1h`: 1 hour

                    Defaults to `5m`.

                    - `"5m"`

                    - `"1h"`

          - `type: "content"`

        - `beta_url_pdf_source: object { type, url }`

          - `type: "url"`

          - `url: string`

        - `beta_file_document_source: object { file_id, type }`

          - `file_id: string`

          - `type: "file"`

      - `type: "document"`

      - `cache_control: optional object { type, ttl }`

        Create a cache control breakpoint at this content block.

        - `type: "ephemeral"`

        - `ttl: optional "5m" or "1h"`

          The time-to-live for the cache control breakpoint.

          This may be one the following values:

          - `5m`: 5 minutes
          - `1h`: 1 hour

          Defaults to `5m`.

          - `"5m"`

          - `"1h"`

      - `citations: optional object { enabled }`

        - `enabled: optional boolean`

      - `context: optional string`

      - `title: optional string`

    - `beta_tool_reference_block_param: object { tool_name, type, cache_control }`

      Tool reference block that can be included in tool_result content.

      - `tool_name: string`

      - `type: "tool_reference"`

      - `cache_control: optional object { type, ttl }`

        Create a cache control breakpoint at this content block.

        - `type: "ephemeral"`

        - `ttl: optional "5m" or "1h"`

          The time-to-live for the cache control breakpoint.

          This may be one the following values:

          - `5m`: 5 minutes
          - `1h`: 1 hour

          Defaults to `5m`.

          - `"5m"`

          - `"1h"`

  - `is_error: optional boolean`

### Beta Tool Search Tool Bm25 20251119

- `beta_tool_search_tool_bm25_20251119: object { name, type, allowed_callers, 3 more }`

  - `name: "tool_search_tool_bm25"`

    Name of the tool.

    This is how the tool will be called by the model and in `tool_use` blocks.

  - `type: "tool_search_tool_bm25_20251119" or "tool_search_tool_bm25"`

    - `"tool_search_tool_bm25_20251119"`

    - `"tool_search_tool_bm25"`

  - `allowed_callers: optional array of "direct" or "code_execution_20250825" or "code_execution_20260120"`

    - `"direct"`

    - `"code_execution_20250825"`

    - `"code_execution_20260120"`

  - `cache_control: optional object { type, ttl }`

    Create a cache control breakpoint at this content block.

    - `type: "ephemeral"`

    - `ttl: optional "5m" or "1h"`

      The time-to-live for the cache control breakpoint.

      This may be one the following values:

      - `5m`: 5 minutes
      - `1h`: 1 hour

      Defaults to `5m`.

      - `"5m"`

      - `"1h"`

  - `defer_loading: optional boolean`

    If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

  - `strict: optional boolean`

    When true, guarantees schema validation on tool names and inputs

### Beta Tool Search Tool Regex 20251119

- `beta_tool_search_tool_regex_20251119: object { name, type, allowed_callers, 3 more }`

  - `name: "tool_search_tool_regex"`

    Name of the tool.

    This is how the tool will be called by the model and in `tool_use` blocks.

  - `type: "tool_search_tool_regex_20251119" or "tool_search_tool_regex"`

    - `"tool_search_tool_regex_20251119"`

    - `"tool_search_tool_regex"`

  - `allowed_callers: optional array of "direct" or "code_execution_20250825" or "code_execution_20260120"`

    - `"direct"`

    - `"code_execution_20250825"`

    - `"code_execution_20260120"`

  - `cache_control: optional object { type, ttl }`

    Create a cache control breakpoint at this content block.

    - `type: "ephemeral"`

    - `ttl: optional "5m" or "1h"`

      The time-to-live for the cache control breakpoint.

      This may be one the following values:

      - `5m`: 5 minutes
      - `1h`: 1 hour

      Defaults to `5m`.

      - `"5m"`

      - `"1h"`

  - `defer_loading: optional boolean`

    If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

  - `strict: optional boolean`

    When true, guarantees schema validation on tool names and inputs

### Beta Tool Search Tool Result Block

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

### Beta Tool Search Tool Result Block Param

- `beta_tool_search_tool_result_block_param: object { content, tool_use_id, type, cache_control }`

  - `content: BetaToolSearchToolResultErrorParam or BetaToolSearchToolSearchResultBlockParam`

    - `beta_tool_search_tool_result_error_param: object { error_code, type }`

      - `error_code: "invalid_tool_input" or "unavailable" or "too_many_requests" or "execution_time_exceeded"`

        - `"invalid_tool_input"`

        - `"unavailable"`

        - `"too_many_requests"`

        - `"execution_time_exceeded"`

      - `type: "tool_search_tool_result_error"`

    - `beta_tool_search_tool_search_result_block_param: object { tool_references, type }`

      - `tool_references: array of BetaToolReferenceBlockParam`

        - `tool_name: string`

        - `type: "tool_reference"`

        - `cache_control: optional object { type, ttl }`

          Create a cache control breakpoint at this content block.

          - `type: "ephemeral"`

          - `ttl: optional "5m" or "1h"`

            The time-to-live for the cache control breakpoint.

            This may be one the following values:

            - `5m`: 5 minutes
            - `1h`: 1 hour

            Defaults to `5m`.

            - `"5m"`

            - `"1h"`

      - `type: "tool_search_tool_search_result"`

  - `tool_use_id: string`

  - `type: "tool_search_tool_result"`

  - `cache_control: optional object { type, ttl }`

    Create a cache control breakpoint at this content block.

    - `type: "ephemeral"`

    - `ttl: optional "5m" or "1h"`

      The time-to-live for the cache control breakpoint.

      This may be one the following values:

      - `5m`: 5 minutes
      - `1h`: 1 hour

      Defaults to `5m`.

      - `"5m"`

      - `"1h"`

### Beta Tool Search Tool Result Error

- `beta_tool_search_tool_result_error: object { error_code, error_message, type }`

  - `error_code: "invalid_tool_input" or "unavailable" or "too_many_requests" or "execution_time_exceeded"`

    - `"invalid_tool_input"`

    - `"unavailable"`

    - `"too_many_requests"`

    - `"execution_time_exceeded"`

  - `error_message: string`

  - `type: "tool_search_tool_result_error"`

### Beta Tool Search Tool Result Error Param

- `beta_tool_search_tool_result_error_param: object { error_code, type }`

  - `error_code: "invalid_tool_input" or "unavailable" or "too_many_requests" or "execution_time_exceeded"`

    - `"invalid_tool_input"`

    - `"unavailable"`

    - `"too_many_requests"`

    - `"execution_time_exceeded"`

  - `type: "tool_search_tool_result_error"`

### Beta Tool Search Tool Search Result Block

- `beta_tool_search_tool_search_result_block: object { tool_references, type }`

  - `tool_references: array of BetaToolReferenceBlock`

    - `tool_name: string`

    - `type: "tool_reference"`

  - `type: "tool_search_tool_search_result"`

### Beta Tool Search Tool Search Result Block Param

- `beta_tool_search_tool_search_result_block_param: object { tool_references, type }`

  - `tool_references: array of BetaToolReferenceBlockParam`

    - `tool_name: string`

    - `type: "tool_reference"`

    - `cache_control: optional object { type, ttl }`

      Create a cache control breakpoint at this content block.

      - `type: "ephemeral"`

      - `ttl: optional "5m" or "1h"`

        The time-to-live for the cache control breakpoint.

        This may be one the following values:

        - `5m`: 5 minutes
        - `1h`: 1 hour

        Defaults to `5m`.

        - `"5m"`

        - `"1h"`

  - `type: "tool_search_tool_search_result"`

### Beta Tool Text Editor 20241022

- `beta_tool_text_editor_20241022: object { name, type, allowed_callers, 4 more }`

  - `name: "str_replace_editor"`

    Name of the tool.

    This is how the tool will be called by the model and in `tool_use` blocks.

  - `type: "text_editor_20241022"`

  - `allowed_callers: optional array of "direct" or "code_execution_20250825" or "code_execution_20260120"`

    - `"direct"`

    - `"code_execution_20250825"`

    - `"code_execution_20260120"`

  - `cache_control: optional object { type, ttl }`

    Create a cache control breakpoint at this content block.

    - `type: "ephemeral"`

    - `ttl: optional "5m" or "1h"`

      The time-to-live for the cache control breakpoint.

      This may be one the following values:

      - `5m`: 5 minutes
      - `1h`: 1 hour

      Defaults to `5m`.

      - `"5m"`

      - `"1h"`

  - `defer_loading: optional boolean`

    If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

  - `input_examples: optional array of map[unknown]`

  - `strict: optional boolean`

    When true, guarantees schema validation on tool names and inputs

### Beta Tool Text Editor 20250124

- `beta_tool_text_editor_20250124: object { name, type, allowed_callers, 4 more }`

  - `name: "str_replace_editor"`

    Name of the tool.

    This is how the tool will be called by the model and in `tool_use` blocks.

  - `type: "text_editor_20250124"`

  - `allowed_callers: optional array of "direct" or "code_execution_20250825" or "code_execution_20260120"`

    - `"direct"`

    - `"code_execution_20250825"`

    - `"code_execution_20260120"`

  - `cache_control: optional object { type, ttl }`

    Create a cache control breakpoint at this content block.

    - `type: "ephemeral"`

    - `ttl: optional "5m" or "1h"`

      The time-to-live for the cache control breakpoint.

      This may be one the following values:

      - `5m`: 5 minutes
      - `1h`: 1 hour

      Defaults to `5m`.

      - `"5m"`

      - `"1h"`

  - `defer_loading: optional boolean`

    If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

  - `input_examples: optional array of map[unknown]`

  - `strict: optional boolean`

    When true, guarantees schema validation on tool names and inputs

### Beta Tool Text Editor 20250429

- `beta_tool_text_editor_20250429: object { name, type, allowed_callers, 4 more }`

  - `name: "str_replace_based_edit_tool"`

    Name of the tool.

    This is how the tool will be called by the model and in `tool_use` blocks.

  - `type: "text_editor_20250429"`

  - `allowed_callers: optional array of "direct" or "code_execution_20250825" or "code_execution_20260120"`

    - `"direct"`

    - `"code_execution_20250825"`

    - `"code_execution_20260120"`

  - `cache_control: optional object { type, ttl }`

    Create a cache control breakpoint at this content block.

    - `type: "ephemeral"`

    - `ttl: optional "5m" or "1h"`

      The time-to-live for the cache control breakpoint.

      This may be one the following values:

      - `5m`: 5 minutes
      - `1h`: 1 hour

      Defaults to `5m`.

      - `"5m"`

      - `"1h"`

  - `defer_loading: optional boolean`

    If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

  - `input_examples: optional array of map[unknown]`

  - `strict: optional boolean`

    When true, guarantees schema validation on tool names and inputs

### Beta Tool Text Editor 20250728

- `beta_tool_text_editor_20250728: object { name, type, allowed_callers, 5 more }`

  - `name: "str_replace_based_edit_tool"`

    Name of the tool.

    This is how the tool will be called by the model and in `tool_use` blocks.

  - `type: "text_editor_20250728"`

  - `allowed_callers: optional array of "direct" or "code_execution_20250825" or "code_execution_20260120"`

    - `"direct"`

    - `"code_execution_20250825"`

    - `"code_execution_20260120"`

  - `cache_control: optional object { type, ttl }`

    Create a cache control breakpoint at this content block.

    - `type: "ephemeral"`

    - `ttl: optional "5m" or "1h"`

      The time-to-live for the cache control breakpoint.

      This may be one the following values:

      - `5m`: 5 minutes
      - `1h`: 1 hour

      Defaults to `5m`.

      - `"5m"`

      - `"1h"`

  - `defer_loading: optional boolean`

    If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

  - `input_examples: optional array of map[unknown]`

  - `max_characters: optional number`

    Maximum number of characters to display when viewing a file. If not specified, defaults to displaying the full file.

  - `strict: optional boolean`

    When true, guarantees schema validation on tool names and inputs

### Beta Tool Union

- `beta_tool_union: BetaTool or BetaToolBash20241022 or BetaToolBash20250124 or 20 more`

  Code execution tool with REPL state persistence (daemon mode + gVisor checkpoint).

  - `beta_tool: object { input_schema, name, allowed_callers, 7 more }`

    - `input_schema: object { type, properties, required }`

      [JSON schema](https://json-schema.org/draft/2020-12) for this tool's input.

      This defines the shape of the `input` that your tool accepts and that the model will produce.

      - `type: "object"`

      - `properties: optional map[unknown]`

      - `required: optional array of string`

    - `name: string`

      Name of the tool.

      This is how the tool will be called by the model and in `tool_use` blocks.

    - `allowed_callers: optional array of "direct" or "code_execution_20250825" or "code_execution_20260120"`

      - `"direct"`

      - `"code_execution_20250825"`

      - `"code_execution_20260120"`

    - `cache_control: optional object { type, ttl }`

      Create a cache control breakpoint at this content block.

      - `type: "ephemeral"`

      - `ttl: optional "5m" or "1h"`

        The time-to-live for the cache control breakpoint.

        This may be one the following values:

        - `5m`: 5 minutes
        - `1h`: 1 hour

        Defaults to `5m`.

        - `"5m"`

        - `"1h"`

    - `defer_loading: optional boolean`

      If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

    - `description: optional string`

      Description of what this tool does.

      Tool descriptions should be as detailed as possible. The more information that the model has about what the tool is and how to use it, the better it will perform. You can use natural language descriptions to reinforce important aspects of the tool input JSON schema.

    - `eager_input_streaming: optional boolean`

      Enable eager input streaming for this tool. When true, tool input parameters will be streamed incrementally as they are generated, and types will be inferred on-the-fly rather than buffering the full JSON output. When false, streaming is disabled for this tool even if the fine-grained-tool-streaming beta is active. When null (default), uses the default behavior based on beta headers.

    - `input_examples: optional array of map[unknown]`

    - `strict: optional boolean`

      When true, guarantees schema validation on tool names and inputs

    - `type: optional "custom"`

      - `"custom"`

  - `beta_tool_bash_20241022: object { name, type, allowed_callers, 4 more }`

    - `name: "bash"`

      Name of the tool.

      This is how the tool will be called by the model and in `tool_use` blocks.

    - `type: "bash_20241022"`

    - `allowed_callers: optional array of "direct" or "code_execution_20250825" or "code_execution_20260120"`

      - `"direct"`

      - `"code_execution_20250825"`

      - `"code_execution_20260120"`

    - `cache_control: optional object { type, ttl }`

      Create a cache control breakpoint at this content block.

      - `type: "ephemeral"`

      - `ttl: optional "5m" or "1h"`

        The time-to-live for the cache control breakpoint.

        This may be one the following values:

        - `5m`: 5 minutes
        - `1h`: 1 hour

        Defaults to `5m`.

        - `"5m"`

        - `"1h"`

    - `defer_loading: optional boolean`

      If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

    - `input_examples: optional array of map[unknown]`

    - `strict: optional boolean`

      When true, guarantees schema validation on tool names and inputs

  - `beta_tool_bash_20250124: object { name, type, allowed_callers, 4 more }`

    - `name: "bash"`

      Name of the tool.

      This is how the tool will be called by the model and in `tool_use` blocks.

    - `type: "bash_20250124"`

    - `allowed_callers: optional array of "direct" or "code_execution_20250825" or "code_execution_20260120"`

      - `"direct"`

      - `"code_execution_20250825"`

      - `"code_execution_20260120"`

    - `cache_control: optional object { type, ttl }`

      Create a cache control breakpoint at this content block.

      - `type: "ephemeral"`

      - `ttl: optional "5m" or "1h"`

        The time-to-live for the cache control breakpoint.

        This may be one the following values:

        - `5m`: 5 minutes
        - `1h`: 1 hour

        Defaults to `5m`.

        - `"5m"`

        - `"1h"`

    - `defer_loading: optional boolean`

      If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

    - `input_examples: optional array of map[unknown]`

    - `strict: optional boolean`

      When true, guarantees schema validation on tool names and inputs

  - `beta_code_execution_tool_20250522: object { name, type, allowed_callers, 3 more }`

    - `name: "code_execution"`

      Name of the tool.

      This is how the tool will be called by the model and in `tool_use` blocks.

    - `type: "code_execution_20250522"`

    - `allowed_callers: optional array of "direct" or "code_execution_20250825" or "code_execution_20260120"`

      - `"direct"`

      - `"code_execution_20250825"`

      - `"code_execution_20260120"`

    - `cache_control: optional object { type, ttl }`

      Create a cache control breakpoint at this content block.

      - `type: "ephemeral"`

      - `ttl: optional "5m" or "1h"`

        The time-to-live for the cache control breakpoint.

        This may be one the following values:

        - `5m`: 5 minutes
        - `1h`: 1 hour

        Defaults to `5m`.

        - `"5m"`

        - `"1h"`

    - `defer_loading: optional boolean`

      If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

    - `strict: optional boolean`

      When true, guarantees schema validation on tool names and inputs

  - `beta_code_execution_tool_20250825: object { name, type, allowed_callers, 3 more }`

    - `name: "code_execution"`

      Name of the tool.

      This is how the tool will be called by the model and in `tool_use` blocks.

    - `type: "code_execution_20250825"`

    - `allowed_callers: optional array of "direct" or "code_execution_20250825" or "code_execution_20260120"`

      - `"direct"`

      - `"code_execution_20250825"`

      - `"code_execution_20260120"`

    - `cache_control: optional object { type, ttl }`

      Create a cache control breakpoint at this content block.

      - `type: "ephemeral"`

      - `ttl: optional "5m" or "1h"`

        The time-to-live for the cache control breakpoint.

        This may be one the following values:

        - `5m`: 5 minutes
        - `1h`: 1 hour

        Defaults to `5m`.

        - `"5m"`

        - `"1h"`

    - `defer_loading: optional boolean`

      If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

    - `strict: optional boolean`

      When true, guarantees schema validation on tool names and inputs

  - `beta_code_execution_tool_20260120: object { name, type, allowed_callers, 3 more }`

    Code execution tool with REPL state persistence (daemon mode + gVisor checkpoint).

    - `name: "code_execution"`

      Name of the tool.

      This is how the tool will be called by the model and in `tool_use` blocks.

    - `type: "code_execution_20260120"`

    - `allowed_callers: optional array of "direct" or "code_execution_20250825" or "code_execution_20260120"`

      - `"direct"`

      - `"code_execution_20250825"`

      - `"code_execution_20260120"`

    - `cache_control: optional object { type, ttl }`

      Create a cache control breakpoint at this content block.

      - `type: "ephemeral"`

      - `ttl: optional "5m" or "1h"`

        The time-to-live for the cache control breakpoint.

        This may be one the following values:

        - `5m`: 5 minutes
        - `1h`: 1 hour

        Defaults to `5m`.

        - `"5m"`

        - `"1h"`

    - `defer_loading: optional boolean`

      If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

    - `strict: optional boolean`

      When true, guarantees schema validation on tool names and inputs

  - `beta_tool_computer_use_20241022: object { display_height_px, display_width_px, name, 7 more }`

    - `display_height_px: number`

      The height of the display in pixels.

    - `display_width_px: number`

      The width of the display in pixels.

    - `name: "computer"`

      Name of the tool.

      This is how the tool will be called by the model and in `tool_use` blocks.

    - `type: "computer_20241022"`

    - `allowed_callers: optional array of "direct" or "code_execution_20250825" or "code_execution_20260120"`

      - `"direct"`

      - `"code_execution_20250825"`

      - `"code_execution_20260120"`

    - `cache_control: optional object { type, ttl }`

      Create a cache control breakpoint at this content block.

      - `type: "ephemeral"`

      - `ttl: optional "5m" or "1h"`

        The time-to-live for the cache control breakpoint.

        This may be one the following values:

        - `5m`: 5 minutes
        - `1h`: 1 hour

        Defaults to `5m`.

        - `"5m"`

        - `"1h"`

    - `defer_loading: optional boolean`

      If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

    - `display_number: optional number`

      The X11 display number (e.g. 0, 1) for the display.

    - `input_examples: optional array of map[unknown]`

    - `strict: optional boolean`

      When true, guarantees schema validation on tool names and inputs

  - `beta_memory_tool_20250818: object { name, type, allowed_callers, 4 more }`

    - `name: "memory"`

      Name of the tool.

      This is how the tool will be called by the model and in `tool_use` blocks.

    - `type: "memory_20250818"`

    - `allowed_callers: optional array of "direct" or "code_execution_20250825" or "code_execution_20260120"`

      - `"direct"`

      - `"code_execution_20250825"`

      - `"code_execution_20260120"`

    - `cache_control: optional object { type, ttl }`

      Create a cache control breakpoint at this content block.

      - `type: "ephemeral"`

      - `ttl: optional "5m" or "1h"`

        The time-to-live for the cache control breakpoint.

        This may be one the following values:

        - `5m`: 5 minutes
        - `1h`: 1 hour

        Defaults to `5m`.

        - `"5m"`

        - `"1h"`

    - `defer_loading: optional boolean`

      If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

    - `input_examples: optional array of map[unknown]`

    - `strict: optional boolean`

      When true, guarantees schema validation on tool names and inputs

  - `beta_tool_computer_use_20250124: object { display_height_px, display_width_px, name, 7 more }`

    - `display_height_px: number`

      The height of the display in pixels.

    - `display_width_px: number`

      The width of the display in pixels.

    - `name: "computer"`

      Name of the tool.

      This is how the tool will be called by the model and in `tool_use` blocks.

    - `type: "computer_20250124"`

    - `allowed_callers: optional array of "direct" or "code_execution_20250825" or "code_execution_20260120"`

      - `"direct"`

      - `"code_execution_20250825"`

      - `"code_execution_20260120"`

    - `cache_control: optional object { type, ttl }`

      Create a cache control breakpoint at this content block.

      - `type: "ephemeral"`

      - `ttl: optional "5m" or "1h"`

        The time-to-live for the cache control breakpoint.

        This may be one the following values:

        - `5m`: 5 minutes
        - `1h`: 1 hour

        Defaults to `5m`.

        - `"5m"`

        - `"1h"`

    - `defer_loading: optional boolean`

      If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

    - `display_number: optional number`

      The X11 display number (e.g. 0, 1) for the display.

    - `input_examples: optional array of map[unknown]`

    - `strict: optional boolean`

      When true, guarantees schema validation on tool names and inputs

  - `beta_tool_text_editor_20241022: object { name, type, allowed_callers, 4 more }`

    - `name: "str_replace_editor"`

      Name of the tool.

      This is how the tool will be called by the model and in `tool_use` blocks.

    - `type: "text_editor_20241022"`

    - `allowed_callers: optional array of "direct" or "code_execution_20250825" or "code_execution_20260120"`

      - `"direct"`

      - `"code_execution_20250825"`

      - `"code_execution_20260120"`

    - `cache_control: optional object { type, ttl }`

      Create a cache control breakpoint at this content block.

      - `type: "ephemeral"`

      - `ttl: optional "5m" or "1h"`

        The time-to-live for the cache control breakpoint.

        This may be one the following values:

        - `5m`: 5 minutes
        - `1h`: 1 hour

        Defaults to `5m`.

        - `"5m"`

        - `"1h"`

    - `defer_loading: optional boolean`

      If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

    - `input_examples: optional array of map[unknown]`

    - `strict: optional boolean`

      When true, guarantees schema validation on tool names and inputs

  - `beta_tool_computer_use_20251124: object { display_height_px, display_width_px, name, 8 more }`

    - `display_height_px: number`

      The height of the display in pixels.

    - `display_width_px: number`

      The width of the display in pixels.

    - `name: "computer"`

      Name of the tool.

      This is how the tool will be called by the model and in `tool_use` blocks.

    - `type: "computer_20251124"`

    - `allowed_callers: optional array of "direct" or "code_execution_20250825" or "code_execution_20260120"`

      - `"direct"`

      - `"code_execution_20250825"`

      - `"code_execution_20260120"`

    - `cache_control: optional object { type, ttl }`

      Create a cache control breakpoint at this content block.

      - `type: "ephemeral"`

      - `ttl: optional "5m" or "1h"`

        The time-to-live for the cache control breakpoint.

        This may be one the following values:

        - `5m`: 5 minutes
        - `1h`: 1 hour

        Defaults to `5m`.

        - `"5m"`

        - `"1h"`

    - `defer_loading: optional boolean`

      If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

    - `display_number: optional number`

      The X11 display number (e.g. 0, 1) for the display.

    - `enable_zoom: optional boolean`

      Whether to enable an action to take a zoomed-in screenshot of the screen.

    - `input_examples: optional array of map[unknown]`

    - `strict: optional boolean`

      When true, guarantees schema validation on tool names and inputs

  - `beta_tool_text_editor_20250124: object { name, type, allowed_callers, 4 more }`

    - `name: "str_replace_editor"`

      Name of the tool.

      This is how the tool will be called by the model and in `tool_use` blocks.

    - `type: "text_editor_20250124"`

    - `allowed_callers: optional array of "direct" or "code_execution_20250825" or "code_execution_20260120"`

      - `"direct"`

      - `"code_execution_20250825"`

      - `"code_execution_20260120"`

    - `cache_control: optional object { type, ttl }`

      Create a cache control breakpoint at this content block.

      - `type: "ephemeral"`

      - `ttl: optional "5m" or "1h"`

        The time-to-live for the cache control breakpoint.

        This may be one the following values:

        - `5m`: 5 minutes
        - `1h`: 1 hour

        Defaults to `5m`.

        - `"5m"`

        - `"1h"`

    - `defer_loading: optional boolean`

      If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

    - `input_examples: optional array of map[unknown]`

    - `strict: optional boolean`

      When true, guarantees schema validation on tool names and inputs

  - `beta_tool_text_editor_20250429: object { name, type, allowed_callers, 4 more }`

    - `name: "str_replace_based_edit_tool"`

      Name of the tool.

      This is how the tool will be called by the model and in `tool_use` blocks.

    - `type: "text_editor_20250429"`

    - `allowed_callers: optional array of "direct" or "code_execution_20250825" or "code_execution_20260120"`

      - `"direct"`

      - `"code_execution_20250825"`

      - `"code_execution_20260120"`

    - `cache_control: optional object { type, ttl }`

      Create a cache control breakpoint at this content block.

      - `type: "ephemeral"`

      - `ttl: optional "5m" or "1h"`

        The time-to-live for the cache control breakpoint.

        This may be one the following values:

        - `5m`: 5 minutes
        - `1h`: 1 hour

        Defaults to `5m`.

        - `"5m"`

        - `"1h"`

    - `defer_loading: optional boolean`

      If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

    - `input_examples: optional array of map[unknown]`

    - `strict: optional boolean`

      When true, guarantees schema validation on tool names and inputs

  - `beta_tool_text_editor_20250728: object { name, type, allowed_callers, 5 more }`

    - `name: "str_replace_based_edit_tool"`

      Name of the tool.

      This is how the tool will be called by the model and in `tool_use` blocks.

    - `type: "text_editor_20250728"`

    - `allowed_callers: optional array of "direct" or "code_execution_20250825" or "code_execution_20260120"`

      - `"direct"`

      - `"code_execution_20250825"`

      - `"code_execution_20260120"`

    - `cache_control: optional object { type, ttl }`

      Create a cache control breakpoint at this content block.

      - `type: "ephemeral"`

      - `ttl: optional "5m" or "1h"`

        The time-to-live for the cache control breakpoint.

        This may be one the following values:

        - `5m`: 5 minutes
        - `1h`: 1 hour

        Defaults to `5m`.

        - `"5m"`

        - `"1h"`

    - `defer_loading: optional boolean`

      If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

    - `input_examples: optional array of map[unknown]`

    - `max_characters: optional number`

      Maximum number of characters to display when viewing a file. If not specified, defaults to displaying the full file.

    - `strict: optional boolean`

      When true, guarantees schema validation on tool names and inputs

  - `beta_web_search_tool_20250305: object { name, type, allowed_callers, 7 more }`

    - `name: "web_search"`

      Name of the tool.

      This is how the tool will be called by the model and in `tool_use` blocks.

    - `type: "web_search_20250305"`

    - `allowed_callers: optional array of "direct" or "code_execution_20250825" or "code_execution_20260120"`

      - `"direct"`

      - `"code_execution_20250825"`

      - `"code_execution_20260120"`

    - `allowed_domains: optional array of string`

      If provided, only these domains will be included in results. Cannot be used alongside `blocked_domains`.

    - `blocked_domains: optional array of string`

      If provided, these domains will never appear in results. Cannot be used alongside `allowed_domains`.

    - `cache_control: optional object { type, ttl }`

      Create a cache control breakpoint at this content block.

      - `type: "ephemeral"`

      - `ttl: optional "5m" or "1h"`

        The time-to-live for the cache control breakpoint.

        This may be one the following values:

        - `5m`: 5 minutes
        - `1h`: 1 hour

        Defaults to `5m`.

        - `"5m"`

        - `"1h"`

    - `defer_loading: optional boolean`

      If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

    - `max_uses: optional number`

      Maximum number of times the tool can be used in the API request.

    - `strict: optional boolean`

      When true, guarantees schema validation on tool names and inputs

    - `user_location: optional object { type, city, country, 2 more }`

      Parameters for the user's location. Used to provide more relevant search results.

      - `type: "approximate"`

      - `city: optional string`

        The city of the user.

      - `country: optional string`

        The two letter [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) of the user.

      - `region: optional string`

        The region of the user.

      - `timezone: optional string`

        The [IANA timezone](https://nodatime.org/TimeZones) of the user.

  - `beta_web_fetch_tool_20250910: object { name, type, allowed_callers, 8 more }`

    - `name: "web_fetch"`

      Name of the tool.

      This is how the tool will be called by the model and in `tool_use` blocks.

    - `type: "web_fetch_20250910"`

    - `allowed_callers: optional array of "direct" or "code_execution_20250825" or "code_execution_20260120"`

      - `"direct"`

      - `"code_execution_20250825"`

      - `"code_execution_20260120"`

    - `allowed_domains: optional array of string`

      List of domains to allow fetching from

    - `blocked_domains: optional array of string`

      List of domains to block fetching from

    - `cache_control: optional object { type, ttl }`

      Create a cache control breakpoint at this content block.

      - `type: "ephemeral"`

      - `ttl: optional "5m" or "1h"`

        The time-to-live for the cache control breakpoint.

        This may be one the following values:

        - `5m`: 5 minutes
        - `1h`: 1 hour

        Defaults to `5m`.

        - `"5m"`

        - `"1h"`

    - `citations: optional object { enabled }`

      Citations configuration for fetched documents. Citations are disabled by default.

      - `enabled: optional boolean`

    - `defer_loading: optional boolean`

      If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

    - `max_content_tokens: optional number`

      Maximum number of tokens used by including web page text content in the context. The limit is approximate and does not apply to binary content such as PDFs.

    - `max_uses: optional number`

      Maximum number of times the tool can be used in the API request.

    - `strict: optional boolean`

      When true, guarantees schema validation on tool names and inputs

  - `beta_web_search_tool_20260209: object { name, type, allowed_callers, 7 more }`

    - `name: "web_search"`

      Name of the tool.

      This is how the tool will be called by the model and in `tool_use` blocks.

    - `type: "web_search_20260209"`

    - `allowed_callers: optional array of "direct" or "code_execution_20250825" or "code_execution_20260120"`

      - `"direct"`

      - `"code_execution_20250825"`

      - `"code_execution_20260120"`

    - `allowed_domains: optional array of string`

      If provided, only these domains will be included in results. Cannot be used alongside `blocked_domains`.

    - `blocked_domains: optional array of string`

      If provided, these domains will never appear in results. Cannot be used alongside `allowed_domains`.

    - `cache_control: optional object { type, ttl }`

      Create a cache control breakpoint at this content block.

      - `type: "ephemeral"`

      - `ttl: optional "5m" or "1h"`

        The time-to-live for the cache control breakpoint.

        This may be one the following values:

        - `5m`: 5 minutes
        - `1h`: 1 hour

        Defaults to `5m`.

        - `"5m"`

        - `"1h"`

    - `defer_loading: optional boolean`

      If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

    - `max_uses: optional number`

      Maximum number of times the tool can be used in the API request.

    - `strict: optional boolean`

      When true, guarantees schema validation on tool names and inputs

    - `user_location: optional object { type, city, country, 2 more }`

      Parameters for the user's location. Used to provide more relevant search results.

      - `type: "approximate"`

      - `city: optional string`

        The city of the user.

      - `country: optional string`

        The two letter [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) of the user.

      - `region: optional string`

        The region of the user.

      - `timezone: optional string`

        The [IANA timezone](https://nodatime.org/TimeZones) of the user.

  - `beta_web_fetch_tool_20260209: object { name, type, allowed_callers, 8 more }`

    - `name: "web_fetch"`

      Name of the tool.

      This is how the tool will be called by the model and in `tool_use` blocks.

    - `type: "web_fetch_20260209"`

    - `allowed_callers: optional array of "direct" or "code_execution_20250825" or "code_execution_20260120"`

      - `"direct"`

      - `"code_execution_20250825"`

      - `"code_execution_20260120"`

    - `allowed_domains: optional array of string`

      List of domains to allow fetching from

    - `blocked_domains: optional array of string`

      List of domains to block fetching from

    - `cache_control: optional object { type, ttl }`

      Create a cache control breakpoint at this content block.

      - `type: "ephemeral"`

      - `ttl: optional "5m" or "1h"`

        The time-to-live for the cache control breakpoint.

        This may be one the following values:

        - `5m`: 5 minutes
        - `1h`: 1 hour

        Defaults to `5m`.

        - `"5m"`

        - `"1h"`

    - `citations: optional object { enabled }`

      Citations configuration for fetched documents. Citations are disabled by default.

      - `enabled: optional boolean`

    - `defer_loading: optional boolean`

      If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

    - `max_content_tokens: optional number`

      Maximum number of tokens used by including web page text content in the context. The limit is approximate and does not apply to binary content such as PDFs.

    - `max_uses: optional number`

      Maximum number of times the tool can be used in the API request.

    - `strict: optional boolean`

      When true, guarantees schema validation on tool names and inputs

  - `beta_web_fetch_tool_20260309: object { name, type, allowed_callers, 9 more }`

    Web fetch tool with use_cache parameter for bypassing cached content.

    - `name: "web_fetch"`

      Name of the tool.

      This is how the tool will be called by the model and in `tool_use` blocks.

    - `type: "web_fetch_20260309"`

    - `allowed_callers: optional array of "direct" or "code_execution_20250825" or "code_execution_20260120"`

      - `"direct"`

      - `"code_execution_20250825"`

      - `"code_execution_20260120"`

    - `allowed_domains: optional array of string`

      List of domains to allow fetching from

    - `blocked_domains: optional array of string`

      List of domains to block fetching from

    - `cache_control: optional object { type, ttl }`

      Create a cache control breakpoint at this content block.

      - `type: "ephemeral"`

      - `ttl: optional "5m" or "1h"`

        The time-to-live for the cache control breakpoint.

        This may be one the following values:

        - `5m`: 5 minutes
        - `1h`: 1 hour

        Defaults to `5m`.

        - `"5m"`

        - `"1h"`

    - `citations: optional object { enabled }`

      Citations configuration for fetched documents. Citations are disabled by default.

      - `enabled: optional boolean`

    - `defer_loading: optional boolean`

      If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

    - `max_content_tokens: optional number`

      Maximum number of tokens used by including web page text content in the context. The limit is approximate and does not apply to binary content such as PDFs.

    - `max_uses: optional number`

      Maximum number of times the tool can be used in the API request.

    - `strict: optional boolean`

      When true, guarantees schema validation on tool names and inputs

    - `use_cache: optional boolean`

      Whether to use cached content. Set to false to bypass the cache and fetch fresh content. Only set to false when the user explicitly requests fresh content or when fetching rapidly-changing sources.

  - `beta_advisor_tool_20260301: object { model, name, type, 6 more }`

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

    - `name: "advisor"`

      Name of the tool.

      This is how the tool will be called by the model and in `tool_use` blocks.

    - `type: "advisor_20260301"`

    - `allowed_callers: optional array of "direct" or "code_execution_20250825" or "code_execution_20260120"`

      - `"direct"`

      - `"code_execution_20250825"`

      - `"code_execution_20260120"`

    - `cache_control: optional object { type, ttl }`

      Create a cache control breakpoint at this content block.

      - `type: "ephemeral"`

      - `ttl: optional "5m" or "1h"`

        The time-to-live for the cache control breakpoint.

        This may be one the following values:

        - `5m`: 5 minutes
        - `1h`: 1 hour

        Defaults to `5m`.

        - `"5m"`

        - `"1h"`

    - `caching: optional object { type, ttl }`

      Caching for the advisor's own prompt. When set, each advisor call writes a cache entry at the given TTL so subsequent calls in the same conversation read the stable prefix. When omitted, the advisor prompt is not cached.

      - `type: "ephemeral"`

      - `ttl: optional "5m" or "1h"`

        The time-to-live for the cache control breakpoint.

        This may be one the following values:

        - `5m`: 5 minutes
        - `1h`: 1 hour

        Defaults to `5m`.

        - `"5m"`

        - `"1h"`

    - `defer_loading: optional boolean`

      If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

    - `max_uses: optional number`

      Maximum number of times the tool can be used in the API request.

    - `strict: optional boolean`

      When true, guarantees schema validation on tool names and inputs

  - `beta_tool_search_tool_bm25_20251119: object { name, type, allowed_callers, 3 more }`

    - `name: "tool_search_tool_bm25"`

      Name of the tool.

      This is how the tool will be called by the model and in `tool_use` blocks.

    - `type: "tool_search_tool_bm25_20251119" or "tool_search_tool_bm25"`

      - `"tool_search_tool_bm25_20251119"`

      - `"tool_search_tool_bm25"`

    - `allowed_callers: optional array of "direct" or "code_execution_20250825" or "code_execution_20260120"`

      - `"direct"`

      - `"code_execution_20250825"`

      - `"code_execution_20260120"`

    - `cache_control: optional object { type, ttl }`

      Create a cache control breakpoint at this content block.

      - `type: "ephemeral"`

      - `ttl: optional "5m" or "1h"`

        The time-to-live for the cache control breakpoint.

        This may be one the following values:

        - `5m`: 5 minutes
        - `1h`: 1 hour

        Defaults to `5m`.

        - `"5m"`

        - `"1h"`

    - `defer_loading: optional boolean`

      If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

    - `strict: optional boolean`

      When true, guarantees schema validation on tool names and inputs

  - `beta_tool_search_tool_regex_20251119: object { name, type, allowed_callers, 3 more }`

    - `name: "tool_search_tool_regex"`

      Name of the tool.

      This is how the tool will be called by the model and in `tool_use` blocks.

    - `type: "tool_search_tool_regex_20251119" or "tool_search_tool_regex"`

      - `"tool_search_tool_regex_20251119"`

      - `"tool_search_tool_regex"`

    - `allowed_callers: optional array of "direct" or "code_execution_20250825" or "code_execution_20260120"`

      - `"direct"`

      - `"code_execution_20250825"`

      - `"code_execution_20260120"`

    - `cache_control: optional object { type, ttl }`

      Create a cache control breakpoint at this content block.

      - `type: "ephemeral"`

      - `ttl: optional "5m" or "1h"`

        The time-to-live for the cache control breakpoint.

        This may be one the following values:

        - `5m`: 5 minutes
        - `1h`: 1 hour

        Defaults to `5m`.

        - `"5m"`

        - `"1h"`

    - `defer_loading: optional boolean`

      If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

    - `strict: optional boolean`

      When true, guarantees schema validation on tool names and inputs

  - `beta_mcp_toolset: object { mcp_server_name, type, cache_control, 2 more }`

    Configuration for a group of tools from an MCP server.

    Allows configuring enabled status and defer_loading for all tools
    from an MCP server, with optional per-tool overrides.

    - `mcp_server_name: string`

      Name of the MCP server to configure tools for

    - `type: "mcp_toolset"`

    - `cache_control: optional object { type, ttl }`

      Create a cache control breakpoint at this content block.

      - `type: "ephemeral"`

      - `ttl: optional "5m" or "1h"`

        The time-to-live for the cache control breakpoint.

        This may be one the following values:

        - `5m`: 5 minutes
        - `1h`: 1 hour

        Defaults to `5m`.

        - `"5m"`

        - `"1h"`

    - `configs: optional map[BetaMCPToolConfig]`

      Configuration overrides for specific tools, keyed by tool name

      - `defer_loading: optional boolean`

      - `enabled: optional boolean`

    - `default_config: optional object { defer_loading, enabled }`

      Default configuration applied to all tools from this server

      - `defer_loading: optional boolean`

      - `enabled: optional boolean`

### Beta Tool Use Block

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

### Beta Tool Use Block Param

- `beta_tool_use_block_param: object { id, input, name, 3 more }`

  - `id: string`

  - `input: map[unknown]`

  - `name: string`

  - `type: "tool_use"`

  - `cache_control: optional object { type, ttl }`

    Create a cache control breakpoint at this content block.

    - `type: "ephemeral"`

    - `ttl: optional "5m" or "1h"`

      The time-to-live for the cache control breakpoint.

      This may be one the following values:

      - `5m`: 5 minutes
      - `1h`: 1 hour

      Defaults to `5m`.

      - `"5m"`

      - `"1h"`

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

### Beta Tool Uses Keep

- `beta_tool_uses_keep: object { type, value }`

  - `type: "tool_uses"`

  - `value: number`

### Beta Tool Uses Trigger

- `beta_tool_uses_trigger: object { type, value }`

  - `type: "tool_uses"`

  - `value: number`

### Beta URL Image Source

- `beta_url_image_source: object { type, url }`

  - `type: "url"`

  - `url: string`

### Beta URL PDF Source

- `beta_url_pdf_source: object { type, url }`

  - `type: "url"`

  - `url: string`

### Beta Usage

- `beta_usage: object { cache_creation, cache_creation_input_tokens, cache_read_input_tokens, 7 more }`

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

### Beta User Location

- `beta_user_location: object { type, city, country, 2 more }`

  - `type: "approximate"`

  - `city: optional string`

    The city of the user.

  - `country: optional string`

    The two letter [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) of the user.

  - `region: optional string`

    The region of the user.

  - `timezone: optional string`

    The [IANA timezone](https://nodatime.org/TimeZones) of the user.

### Beta Web Fetch Block

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

### Beta Web Fetch Block Param

- `beta_web_fetch_block_param: object { content, type, url, retrieved_at }`

  - `content: object { source, type, cache_control, 3 more }`

    - `source: BetaBase64PDFSource or BetaPlainTextSource or BetaContentBlockSource or 2 more`

      - `beta_base64_pdf_source: object { data, media_type, type }`

        - `data: string`

        - `media_type: "application/pdf"`

        - `type: "base64"`

      - `beta_plain_text_source: object { data, media_type, type }`

        - `data: string`

        - `media_type: "text/plain"`

        - `type: "text"`

      - `beta_content_block_source: object { content, type }`

        - `content: string or array of BetaContentBlockSourceContent`

          - `union_member_0: string`

          - `beta_content_block_source_content: array of BetaContentBlockSourceContent`

            - `beta_text_block_param: object { text, type, cache_control, citations }`

              - `text: string`

              - `type: "text"`

              - `cache_control: optional object { type, ttl }`

                Create a cache control breakpoint at this content block.

                - `type: "ephemeral"`

                - `ttl: optional "5m" or "1h"`

                  The time-to-live for the cache control breakpoint.

                  This may be one the following values:

                  - `5m`: 5 minutes
                  - `1h`: 1 hour

                  Defaults to `5m`.

                  - `"5m"`

                  - `"1h"`

              - `citations: optional array of BetaTextCitationParam`

                - `beta_citation_char_location_param: object { cited_text, document_index, document_title, 3 more }`

                  - `cited_text: string`

                  - `document_index: number`

                  - `document_title: string`

                  - `end_char_index: number`

                  - `start_char_index: number`

                  - `type: "char_location"`

                - `beta_citation_page_location_param: object { cited_text, document_index, document_title, 3 more }`

                  - `cited_text: string`

                  - `document_index: number`

                  - `document_title: string`

                  - `end_page_number: number`

                  - `start_page_number: number`

                  - `type: "page_location"`

                - `beta_citation_content_block_location_param: object { cited_text, document_index, document_title, 3 more }`

                  - `cited_text: string`

                  - `document_index: number`

                  - `document_title: string`

                  - `end_block_index: number`

                  - `start_block_index: number`

                  - `type: "content_block_location"`

                - `beta_citation_web_search_result_location_param: object { cited_text, encrypted_index, title, 2 more }`

                  - `cited_text: string`

                  - `encrypted_index: string`

                  - `title: string`

                  - `type: "web_search_result_location"`

                  - `url: string`

                - `beta_citation_search_result_location_param: object { cited_text, end_block_index, search_result_index, 4 more }`

                  - `cited_text: string`

                  - `end_block_index: number`

                  - `search_result_index: number`

                  - `source: string`

                  - `start_block_index: number`

                  - `title: string`

                  - `type: "search_result_location"`

            - `beta_image_block_param: object { source, type, cache_control }`

              - `source: BetaBase64ImageSource or BetaURLImageSource or BetaFileImageSource`

                - `beta_base64_image_source: object { data, media_type, type }`

                  - `data: string`

                  - `media_type: "image/jpeg" or "image/png" or "image/gif" or "image/webp"`

                    - `"image/jpeg"`

                    - `"image/png"`

                    - `"image/gif"`

                    - `"image/webp"`

                  - `type: "base64"`

                - `beta_url_image_source: object { type, url }`

                  - `type: "url"`

                  - `url: string`

                - `beta_file_image_source: object { file_id, type }`

                  - `file_id: string`

                  - `type: "file"`

              - `type: "image"`

              - `cache_control: optional object { type, ttl }`

                Create a cache control breakpoint at this content block.

                - `type: "ephemeral"`

                - `ttl: optional "5m" or "1h"`

                  The time-to-live for the cache control breakpoint.

                  This may be one the following values:

                  - `5m`: 5 minutes
                  - `1h`: 1 hour

                  Defaults to `5m`.

                  - `"5m"`

                  - `"1h"`

        - `type: "content"`

      - `beta_url_pdf_source: object { type, url }`

        - `type: "url"`

        - `url: string`

      - `beta_file_document_source: object { file_id, type }`

        - `file_id: string`

        - `type: "file"`

    - `type: "document"`

    - `cache_control: optional object { type, ttl }`

      Create a cache control breakpoint at this content block.

      - `type: "ephemeral"`

      - `ttl: optional "5m" or "1h"`

        The time-to-live for the cache control breakpoint.

        This may be one the following values:

        - `5m`: 5 minutes
        - `1h`: 1 hour

        Defaults to `5m`.

        - `"5m"`

        - `"1h"`

    - `citations: optional object { enabled }`

      - `enabled: optional boolean`

    - `context: optional string`

    - `title: optional string`

  - `type: "web_fetch_result"`

  - `url: string`

    Fetched content URL

  - `retrieved_at: optional string`

    ISO 8601 timestamp when the content was retrieved

### Beta Web Fetch Tool 20250910

- `beta_web_fetch_tool_20250910: object { name, type, allowed_callers, 8 more }`

  - `name: "web_fetch"`

    Name of the tool.

    This is how the tool will be called by the model and in `tool_use` blocks.

  - `type: "web_fetch_20250910"`

  - `allowed_callers: optional array of "direct" or "code_execution_20250825" or "code_execution_20260120"`

    - `"direct"`

    - `"code_execution_20250825"`

    - `"code_execution_20260120"`

  - `allowed_domains: optional array of string`

    List of domains to allow fetching from

  - `blocked_domains: optional array of string`

    List of domains to block fetching from

  - `cache_control: optional object { type, ttl }`

    Create a cache control breakpoint at this content block.

    - `type: "ephemeral"`

    - `ttl: optional "5m" or "1h"`

      The time-to-live for the cache control breakpoint.

      This may be one the following values:

      - `5m`: 5 minutes
      - `1h`: 1 hour

      Defaults to `5m`.

      - `"5m"`

      - `"1h"`

  - `citations: optional object { enabled }`

    Citations configuration for fetched documents. Citations are disabled by default.

    - `enabled: optional boolean`

  - `defer_loading: optional boolean`

    If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

  - `max_content_tokens: optional number`

    Maximum number of tokens used by including web page text content in the context. The limit is approximate and does not apply to binary content such as PDFs.

  - `max_uses: optional number`

    Maximum number of times the tool can be used in the API request.

  - `strict: optional boolean`

    When true, guarantees schema validation on tool names and inputs

### Beta Web Fetch Tool 20260209

- `beta_web_fetch_tool_20260209: object { name, type, allowed_callers, 8 more }`

  - `name: "web_fetch"`

    Name of the tool.

    This is how the tool will be called by the model and in `tool_use` blocks.

  - `type: "web_fetch_20260209"`

  - `allowed_callers: optional array of "direct" or "code_execution_20250825" or "code_execution_20260120"`

    - `"direct"`

    - `"code_execution_20250825"`

    - `"code_execution_20260120"`

  - `allowed_domains: optional array of string`

    List of domains to allow fetching from

  - `blocked_domains: optional array of string`

    List of domains to block fetching from

  - `cache_control: optional object { type, ttl }`

    Create a cache control breakpoint at this content block.

    - `type: "ephemeral"`

    - `ttl: optional "5m" or "1h"`

      The time-to-live for the cache control breakpoint.

      This may be one the following values:

      - `5m`: 5 minutes
      - `1h`: 1 hour

      Defaults to `5m`.

      - `"5m"`

      - `"1h"`

  - `citations: optional object { enabled }`

    Citations configuration for fetched documents. Citations are disabled by default.

    - `enabled: optional boolean`

  - `defer_loading: optional boolean`

    If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

  - `max_content_tokens: optional number`

    Maximum number of tokens used by including web page text content in the context. The limit is approximate and does not apply to binary content such as PDFs.

  - `max_uses: optional number`

    Maximum number of times the tool can be used in the API request.

  - `strict: optional boolean`

    When true, guarantees schema validation on tool names and inputs

### Beta Web Fetch Tool 20260309

- `beta_web_fetch_tool_20260309: object { name, type, allowed_callers, 9 more }`

  Web fetch tool with use_cache parameter for bypassing cached content.

  - `name: "web_fetch"`

    Name of the tool.

    This is how the tool will be called by the model and in `tool_use` blocks.

  - `type: "web_fetch_20260309"`

  - `allowed_callers: optional array of "direct" or "code_execution_20250825" or "code_execution_20260120"`

    - `"direct"`

    - `"code_execution_20250825"`

    - `"code_execution_20260120"`

  - `allowed_domains: optional array of string`

    List of domains to allow fetching from

  - `blocked_domains: optional array of string`

    List of domains to block fetching from

  - `cache_control: optional object { type, ttl }`

    Create a cache control breakpoint at this content block.

    - `type: "ephemeral"`

    - `ttl: optional "5m" or "1h"`

      The time-to-live for the cache control breakpoint.

      This may be one the following values:

      - `5m`: 5 minutes
      - `1h`: 1 hour

      Defaults to `5m`.

      - `"5m"`

      - `"1h"`

  - `citations: optional object { enabled }`

    Citations configuration for fetched documents. Citations are disabled by default.

    - `enabled: optional boolean`

  - `defer_loading: optional boolean`

    If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

  - `max_content_tokens: optional number`

    Maximum number of tokens used by including web page text content in the context. The limit is approximate and does not apply to binary content such as PDFs.

  - `max_uses: optional number`

    Maximum number of times the tool can be used in the API request.

  - `strict: optional boolean`

    When true, guarantees schema validation on tool names and inputs

  - `use_cache: optional boolean`

    Whether to use cached content. Set to false to bypass the cache and fetch fresh content. Only set to false when the user explicitly requests fresh content or when fetching rapidly-changing sources.

### Beta Web Fetch Tool Result Block

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

### Beta Web Fetch Tool Result Block Param

- `beta_web_fetch_tool_result_block_param: object { content, tool_use_id, type, 2 more }`

  - `content: BetaWebFetchToolResultErrorBlockParam or BetaWebFetchBlockParam`

    - `beta_web_fetch_tool_result_error_block_param: object { error_code, type }`

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

    - `beta_web_fetch_block_param: object { content, type, url, retrieved_at }`

      - `content: object { source, type, cache_control, 3 more }`

        - `source: BetaBase64PDFSource or BetaPlainTextSource or BetaContentBlockSource or 2 more`

          - `beta_base64_pdf_source: object { data, media_type, type }`

            - `data: string`

            - `media_type: "application/pdf"`

            - `type: "base64"`

          - `beta_plain_text_source: object { data, media_type, type }`

            - `data: string`

            - `media_type: "text/plain"`

            - `type: "text"`

          - `beta_content_block_source: object { content, type }`

            - `content: string or array of BetaContentBlockSourceContent`

              - `union_member_0: string`

              - `beta_content_block_source_content: array of BetaContentBlockSourceContent`

                - `beta_text_block_param: object { text, type, cache_control, citations }`

                  - `text: string`

                  - `type: "text"`

                  - `cache_control: optional object { type, ttl }`

                    Create a cache control breakpoint at this content block.

                    - `type: "ephemeral"`

                    - `ttl: optional "5m" or "1h"`

                      The time-to-live for the cache control breakpoint.

                      This may be one the following values:

                      - `5m`: 5 minutes
                      - `1h`: 1 hour

                      Defaults to `5m`.

                      - `"5m"`

                      - `"1h"`

                  - `citations: optional array of BetaTextCitationParam`

                    - `beta_citation_char_location_param: object { cited_text, document_index, document_title, 3 more }`

                      - `cited_text: string`

                      - `document_index: number`

                      - `document_title: string`

                      - `end_char_index: number`

                      - `start_char_index: number`

                      - `type: "char_location"`

                    - `beta_citation_page_location_param: object { cited_text, document_index, document_title, 3 more }`

                      - `cited_text: string`

                      - `document_index: number`

                      - `document_title: string`

                      - `end_page_number: number`

                      - `start_page_number: number`

                      - `type: "page_location"`

                    - `beta_citation_content_block_location_param: object { cited_text, document_index, document_title, 3 more }`

                      - `cited_text: string`

                      - `document_index: number`

                      - `document_title: string`

                      - `end_block_index: number`

                      - `start_block_index: number`

                      - `type: "content_block_location"`

                    - `beta_citation_web_search_result_location_param: object { cited_text, encrypted_index, title, 2 more }`

                      - `cited_text: string`

                      - `encrypted_index: string`

                      - `title: string`

                      - `type: "web_search_result_location"`

                      - `url: string`

                    - `beta_citation_search_result_location_param: object { cited_text, end_block_index, search_result_index, 4 more }`

                      - `cited_text: string`

                      - `end_block_index: number`

                      - `search_result_index: number`

                      - `source: string`

                      - `start_block_index: number`

                      - `title: string`

                      - `type: "search_result_location"`

                - `beta_image_block_param: object { source, type, cache_control }`

                  - `source: BetaBase64ImageSource or BetaURLImageSource or BetaFileImageSource`

                    - `beta_base64_image_source: object { data, media_type, type }`

                      - `data: string`

                      - `media_type: "image/jpeg" or "image/png" or "image/gif" or "image/webp"`

                        - `"image/jpeg"`

                        - `"image/png"`

                        - `"image/gif"`

                        - `"image/webp"`

                      - `type: "base64"`

                    - `beta_url_image_source: object { type, url }`

                      - `type: "url"`

                      - `url: string`

                    - `beta_file_image_source: object { file_id, type }`

                      - `file_id: string`

                      - `type: "file"`

                  - `type: "image"`

                  - `cache_control: optional object { type, ttl }`

                    Create a cache control breakpoint at this content block.

                    - `type: "ephemeral"`

                    - `ttl: optional "5m" or "1h"`

                      The time-to-live for the cache control breakpoint.

                      This may be one the following values:

                      - `5m`: 5 minutes
                      - `1h`: 1 hour

                      Defaults to `5m`.

                      - `"5m"`

                      - `"1h"`

            - `type: "content"`

          - `beta_url_pdf_source: object { type, url }`

            - `type: "url"`

            - `url: string`

          - `beta_file_document_source: object { file_id, type }`

            - `file_id: string`

            - `type: "file"`

        - `type: "document"`

        - `cache_control: optional object { type, ttl }`

          Create a cache control breakpoint at this content block.

          - `type: "ephemeral"`

          - `ttl: optional "5m" or "1h"`

            The time-to-live for the cache control breakpoint.

            This may be one the following values:

            - `5m`: 5 minutes
            - `1h`: 1 hour

            Defaults to `5m`.

            - `"5m"`

            - `"1h"`

        - `citations: optional object { enabled }`

          - `enabled: optional boolean`

        - `context: optional string`

        - `title: optional string`

      - `type: "web_fetch_result"`

      - `url: string`

        Fetched content URL

      - `retrieved_at: optional string`

        ISO 8601 timestamp when the content was retrieved

  - `tool_use_id: string`

  - `type: "web_fetch_tool_result"`

  - `cache_control: optional object { type, ttl }`

    Create a cache control breakpoint at this content block.

    - `type: "ephemeral"`

    - `ttl: optional "5m" or "1h"`

      The time-to-live for the cache control breakpoint.

      This may be one the following values:

      - `5m`: 5 minutes
      - `1h`: 1 hour

      Defaults to `5m`.

      - `"5m"`

      - `"1h"`

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

### Beta Web Fetch Tool Result Error Block

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

### Beta Web Fetch Tool Result Error Block Param

- `beta_web_fetch_tool_result_error_block_param: object { error_code, type }`

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

### Beta Web Fetch Tool Result Error Code

- `beta_web_fetch_tool_result_error_code: "invalid_tool_input" or "url_too_long" or "url_not_allowed" or 5 more`

  - `"invalid_tool_input"`

  - `"url_too_long"`

  - `"url_not_allowed"`

  - `"url_not_accessible"`

  - `"unsupported_content_type"`

  - `"too_many_requests"`

  - `"max_uses_exceeded"`

  - `"unavailable"`

### Beta Web Search Result Block

- `beta_web_search_result_block: object { encrypted_content, page_age, title, 2 more }`

  - `encrypted_content: string`

  - `page_age: string`

  - `title: string`

  - `type: "web_search_result"`

  - `url: string`

### Beta Web Search Result Block Param

- `beta_web_search_result_block_param: object { encrypted_content, title, type, 2 more }`

  - `encrypted_content: string`

  - `title: string`

  - `type: "web_search_result"`

  - `url: string`

  - `page_age: optional string`

### Beta Web Search Tool 20250305

- `beta_web_search_tool_20250305: object { name, type, allowed_callers, 7 more }`

  - `name: "web_search"`

    Name of the tool.

    This is how the tool will be called by the model and in `tool_use` blocks.

  - `type: "web_search_20250305"`

  - `allowed_callers: optional array of "direct" or "code_execution_20250825" or "code_execution_20260120"`

    - `"direct"`

    - `"code_execution_20250825"`

    - `"code_execution_20260120"`

  - `allowed_domains: optional array of string`

    If provided, only these domains will be included in results. Cannot be used alongside `blocked_domains`.

  - `blocked_domains: optional array of string`

    If provided, these domains will never appear in results. Cannot be used alongside `allowed_domains`.

  - `cache_control: optional object { type, ttl }`

    Create a cache control breakpoint at this content block.

    - `type: "ephemeral"`

    - `ttl: optional "5m" or "1h"`

      The time-to-live for the cache control breakpoint.

      This may be one the following values:

      - `5m`: 5 minutes
      - `1h`: 1 hour

      Defaults to `5m`.

      - `"5m"`

      - `"1h"`

  - `defer_loading: optional boolean`

    If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

  - `max_uses: optional number`

    Maximum number of times the tool can be used in the API request.

  - `strict: optional boolean`

    When true, guarantees schema validation on tool names and inputs

  - `user_location: optional object { type, city, country, 2 more }`

    Parameters for the user's location. Used to provide more relevant search results.

    - `type: "approximate"`

    - `city: optional string`

      The city of the user.

    - `country: optional string`

      The two letter [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) of the user.

    - `region: optional string`

      The region of the user.

    - `timezone: optional string`

      The [IANA timezone](https://nodatime.org/TimeZones) of the user.

### Beta Web Search Tool 20260209

- `beta_web_search_tool_20260209: object { name, type, allowed_callers, 7 more }`

  - `name: "web_search"`

    Name of the tool.

    This is how the tool will be called by the model and in `tool_use` blocks.

  - `type: "web_search_20260209"`

  - `allowed_callers: optional array of "direct" or "code_execution_20250825" or "code_execution_20260120"`

    - `"direct"`

    - `"code_execution_20250825"`

    - `"code_execution_20260120"`

  - `allowed_domains: optional array of string`

    If provided, only these domains will be included in results. Cannot be used alongside `blocked_domains`.

  - `blocked_domains: optional array of string`

    If provided, these domains will never appear in results. Cannot be used alongside `allowed_domains`.

  - `cache_control: optional object { type, ttl }`

    Create a cache control breakpoint at this content block.

    - `type: "ephemeral"`

    - `ttl: optional "5m" or "1h"`

      The time-to-live for the cache control breakpoint.

      This may be one the following values:

      - `5m`: 5 minutes
      - `1h`: 1 hour

      Defaults to `5m`.

      - `"5m"`

      - `"1h"`

  - `defer_loading: optional boolean`

    If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

  - `max_uses: optional number`

    Maximum number of times the tool can be used in the API request.

  - `strict: optional boolean`

    When true, guarantees schema validation on tool names and inputs

  - `user_location: optional object { type, city, country, 2 more }`

    Parameters for the user's location. Used to provide more relevant search results.

    - `type: "approximate"`

    - `city: optional string`

      The city of the user.

    - `country: optional string`

      The two letter [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) of the user.

    - `region: optional string`

      The region of the user.

    - `timezone: optional string`

      The [IANA timezone](https://nodatime.org/TimeZones) of the user.

### Beta Web Search Tool Request Error

- `beta_web_search_tool_request_error: object { error_code, type }`

  - `error_code: "invalid_tool_input" or "unavailable" or "max_uses_exceeded" or 3 more`

    - `"invalid_tool_input"`

    - `"unavailable"`

    - `"max_uses_exceeded"`

    - `"too_many_requests"`

    - `"query_too_long"`

    - `"request_too_large"`

  - `type: "web_search_tool_result_error"`

### Beta Web Search Tool Result Block

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

### Beta Web Search Tool Result Block Content

- `beta_web_search_tool_result_block_content: BetaWebSearchToolResultError or array of BetaWebSearchResultBlock`

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

### Beta Web Search Tool Result Block Param

- `beta_web_search_tool_result_block_param: object { content, tool_use_id, type, 2 more }`

  - `content: array of BetaWebSearchResultBlockParam or BetaWebSearchToolRequestError`

    - `Result Block: array of BetaWebSearchResultBlockParam`

      - `encrypted_content: string`

      - `title: string`

      - `type: "web_search_result"`

      - `url: string`

      - `page_age: optional string`

    - `beta_web_search_tool_request_error: object { error_code, type }`

      - `error_code: "invalid_tool_input" or "unavailable" or "max_uses_exceeded" or 3 more`

        - `"invalid_tool_input"`

        - `"unavailable"`

        - `"max_uses_exceeded"`

        - `"too_many_requests"`

        - `"query_too_long"`

        - `"request_too_large"`

      - `type: "web_search_tool_result_error"`

  - `tool_use_id: string`

  - `type: "web_search_tool_result"`

  - `cache_control: optional object { type, ttl }`

    Create a cache control breakpoint at this content block.

    - `type: "ephemeral"`

    - `ttl: optional "5m" or "1h"`

      The time-to-live for the cache control breakpoint.

      This may be one the following values:

      - `5m`: 5 minutes
      - `1h`: 1 hour

      Defaults to `5m`.

      - `"5m"`

      - `"1h"`

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

### Beta Web Search Tool Result Block Param Content

- `beta_web_search_tool_result_block_param_content: array of BetaWebSearchResultBlockParam or BetaWebSearchToolRequestError`

  - `Result Block: array of BetaWebSearchResultBlockParam`

    - `encrypted_content: string`

    - `title: string`

    - `type: "web_search_result"`

    - `url: string`

    - `page_age: optional string`

  - `beta_web_search_tool_request_error: object { error_code, type }`

    - `error_code: "invalid_tool_input" or "unavailable" or "max_uses_exceeded" or 3 more`

      - `"invalid_tool_input"`

      - `"unavailable"`

      - `"max_uses_exceeded"`

      - `"too_many_requests"`

      - `"query_too_long"`

      - `"request_too_large"`

    - `type: "web_search_tool_result_error"`

### Beta Web Search Tool Result Error

- `beta_web_search_tool_result_error: object { error_code, type }`

  - `error_code: "invalid_tool_input" or "unavailable" or "max_uses_exceeded" or 3 more`

    - `"invalid_tool_input"`

    - `"unavailable"`

    - `"max_uses_exceeded"`

    - `"too_many_requests"`

    - `"query_too_long"`

    - `"request_too_large"`

  - `type: "web_search_tool_result_error"`

### Beta Web Search Tool Result Error Code

- `beta_web_search_tool_result_error_code: "invalid_tool_input" or "unavailable" or "max_uses_exceeded" or 3 more`

  - `"invalid_tool_input"`

  - `"unavailable"`

  - `"max_uses_exceeded"`

  - `"too_many_requests"`

  - `"query_too_long"`

  - `"request_too_large"`

# Batches

## Create

`$ ant beta:messages:batches create`

**post** `/v1/messages/batches`

Send a batch of Message creation requests.

The Message Batches API can be used to process multiple Messages API requests at once. Once a Message Batch is created, it begins processing immediately. Batches can take up to 24 hours to complete.

Learn more about the Message Batches API in our [user guide](https://docs.claude.com/en/docs/build-with-claude/batch-processing)

### Parameters

- `--request: array of object { custom_id, params }`

  Body param: List of requests for prompt completion. Each is an individual request to create a Message.

- `--beta: optional array of AnthropicBeta`

  Header param: Optional header to specify the beta version(s) you want to use.

### Returns

- `beta_message_batch: object { id, archived_at, cancel_initiated_at, 7 more }`

  - `id: string`

    Unique object identifier.

    The format and length of IDs may change over time.

  - `archived_at: string`

    RFC 3339 datetime string representing the time at which the Message Batch was archived and its results became unavailable.

  - `cancel_initiated_at: string`

    RFC 3339 datetime string representing the time at which cancellation was initiated for the Message Batch. Specified only if cancellation was initiated.

  - `created_at: string`

    RFC 3339 datetime string representing the time at which the Message Batch was created.

  - `ended_at: string`

    RFC 3339 datetime string representing the time at which processing for the Message Batch ended. Specified only once processing ends.

    Processing ends when every request in a Message Batch has either succeeded, errored, canceled, or expired.

  - `expires_at: string`

    RFC 3339 datetime string representing the time at which the Message Batch will expire and end processing, which is 24 hours after creation.

  - `processing_status: "in_progress" or "canceling" or "ended"`

    Processing status of the Message Batch.

    - `"in_progress"`

    - `"canceling"`

    - `"ended"`

  - `request_counts: object { canceled, errored, expired, 2 more }`

    Tallies requests within the Message Batch, categorized by their status.

    Requests start as `processing` and move to one of the other statuses only once processing of the entire batch ends. The sum of all values always matches the total number of requests in the batch.

    - `canceled: number`

      Number of requests in the Message Batch that have been canceled.

      This is zero until processing of the entire Message Batch has ended.

    - `errored: number`

      Number of requests in the Message Batch that encountered an error.

      This is zero until processing of the entire Message Batch has ended.

    - `expired: number`

      Number of requests in the Message Batch that have expired.

      This is zero until processing of the entire Message Batch has ended.

    - `processing: number`

      Number of requests in the Message Batch that are processing.

    - `succeeded: number`

      Number of requests in the Message Batch that have completed successfully.

      This is zero until processing of the entire Message Batch has ended.

  - `results_url: string`

    URL to a `.jsonl` file containing the results of the Message Batch requests. Specified only once processing ends.

    Results in the file are not guaranteed to be in the same order as requests. Use the `custom_id` field to match results to requests.

  - `type: "message_batch"`

    Object type.

    For Message Batches, this is always `"message_batch"`.

### Example

```cli
ant beta:messages:batches create \
  --api-key my-anthropic-api-key \
  --request '{custom_id: my-custom-id-1, params: {max_tokens: 1024, messages: [{content: [{text: x, type: text}], role: user}], model: claude-opus-4-6}}'
```

## Retrieve

`$ ant beta:messages:batches retrieve`

**get** `/v1/messages/batches/{message_batch_id}`

This endpoint is idempotent and can be used to poll for Message Batch completion. To access the results of a Message Batch, make a request to the `results_url` field in the response.

Learn more about the Message Batches API in our [user guide](https://docs.claude.com/en/docs/build-with-claude/batch-processing)

### Parameters

- `--message-batch-id: string`

  ID of the Message Batch.

- `--beta: optional array of AnthropicBeta`

  Optional header to specify the beta version(s) you want to use.

### Returns

- `beta_message_batch: object { id, archived_at, cancel_initiated_at, 7 more }`

  - `id: string`

    Unique object identifier.

    The format and length of IDs may change over time.

  - `archived_at: string`

    RFC 3339 datetime string representing the time at which the Message Batch was archived and its results became unavailable.

  - `cancel_initiated_at: string`

    RFC 3339 datetime string representing the time at which cancellation was initiated for the Message Batch. Specified only if cancellation was initiated.

  - `created_at: string`

    RFC 3339 datetime string representing the time at which the Message Batch was created.

  - `ended_at: string`

    RFC 3339 datetime string representing the time at which processing for the Message Batch ended. Specified only once processing ends.

    Processing ends when every request in a Message Batch has either succeeded, errored, canceled, or expired.

  - `expires_at: string`

    RFC 3339 datetime string representing the time at which the Message Batch will expire and end processing, which is 24 hours after creation.

  - `processing_status: "in_progress" or "canceling" or "ended"`

    Processing status of the Message Batch.

    - `"in_progress"`

    - `"canceling"`

    - `"ended"`

  - `request_counts: object { canceled, errored, expired, 2 more }`

    Tallies requests within the Message Batch, categorized by their status.

    Requests start as `processing` and move to one of the other statuses only once processing of the entire batch ends. The sum of all values always matches the total number of requests in the batch.

    - `canceled: number`

      Number of requests in the Message Batch that have been canceled.

      This is zero until processing of the entire Message Batch has ended.

    - `errored: number`

      Number of requests in the Message Batch that encountered an error.

      This is zero until processing of the entire Message Batch has ended.

    - `expired: number`

      Number of requests in the Message Batch that have expired.

      This is zero until processing of the entire Message Batch has ended.

    - `processing: number`

      Number of requests in the Message Batch that are processing.

    - `succeeded: number`

      Number of requests in the Message Batch that have completed successfully.

      This is zero until processing of the entire Message Batch has ended.

  - `results_url: string`

    URL to a `.jsonl` file containing the results of the Message Batch requests. Specified only once processing ends.

    Results in the file are not guaranteed to be in the same order as requests. Use the `custom_id` field to match results to requests.

  - `type: "message_batch"`

    Object type.

    For Message Batches, this is always `"message_batch"`.

### Example

```cli
ant beta:messages:batches retrieve \
  --api-key my-anthropic-api-key \
  --message-batch-id message_batch_id
```

## List

`$ ant beta:messages:batches list`

**get** `/v1/messages/batches`

List all Message Batches within a Workspace. Most recently created batches are returned first.

Learn more about the Message Batches API in our [user guide](https://docs.claude.com/en/docs/build-with-claude/batch-processing)

### Parameters

- `--after-id: optional string`

  Query param: ID of the object to use as a cursor for pagination. When provided, returns the page of results immediately after this object.

- `--before-id: optional string`

  Query param: ID of the object to use as a cursor for pagination. When provided, returns the page of results immediately before this object.

- `--limit: optional number`

  Query param: Number of items to return per page.

  Defaults to `20`. Ranges from `1` to `1000`.

- `--beta: optional array of AnthropicBeta`

  Header param: Optional header to specify the beta version(s) you want to use.

### Returns

- `BetaListResponse_MessageBatch_: object { data, first_id, has_more, last_id }`

  - `data: array of BetaMessageBatch`

    - `id: string`

      Unique object identifier.

      The format and length of IDs may change over time.

    - `archived_at: string`

      RFC 3339 datetime string representing the time at which the Message Batch was archived and its results became unavailable.

    - `cancel_initiated_at: string`

      RFC 3339 datetime string representing the time at which cancellation was initiated for the Message Batch. Specified only if cancellation was initiated.

    - `created_at: string`

      RFC 3339 datetime string representing the time at which the Message Batch was created.

    - `ended_at: string`

      RFC 3339 datetime string representing the time at which processing for the Message Batch ended. Specified only once processing ends.

      Processing ends when every request in a Message Batch has either succeeded, errored, canceled, or expired.

    - `expires_at: string`

      RFC 3339 datetime string representing the time at which the Message Batch will expire and end processing, which is 24 hours after creation.

    - `processing_status: "in_progress" or "canceling" or "ended"`

      Processing status of the Message Batch.

      - `"in_progress"`

      - `"canceling"`

      - `"ended"`

    - `request_counts: object { canceled, errored, expired, 2 more }`

      Tallies requests within the Message Batch, categorized by their status.

      Requests start as `processing` and move to one of the other statuses only once processing of the entire batch ends. The sum of all values always matches the total number of requests in the batch.

      - `canceled: number`

        Number of requests in the Message Batch that have been canceled.

        This is zero until processing of the entire Message Batch has ended.

      - `errored: number`

        Number of requests in the Message Batch that encountered an error.

        This is zero until processing of the entire Message Batch has ended.

      - `expired: number`

        Number of requests in the Message Batch that have expired.

        This is zero until processing of the entire Message Batch has ended.

      - `processing: number`

        Number of requests in the Message Batch that are processing.

      - `succeeded: number`

        Number of requests in the Message Batch that have completed successfully.

        This is zero until processing of the entire Message Batch has ended.

    - `results_url: string`

      URL to a `.jsonl` file containing the results of the Message Batch requests. Specified only once processing ends.

      Results in the file are not guaranteed to be in the same order as requests. Use the `custom_id` field to match results to requests.

    - `type: "message_batch"`

      Object type.

      For Message Batches, this is always `"message_batch"`.

  - `first_id: string`

    First ID in the `data` list. Can be used as the `before_id` for the previous page.

  - `has_more: boolean`

    Indicates if there are more results in the requested page direction.

  - `last_id: string`

    Last ID in the `data` list. Can be used as the `after_id` for the next page.

### Example

```cli
ant beta:messages:batches list \
  --api-key my-anthropic-api-key
```

## Cancel

`$ ant beta:messages:batches cancel`

**post** `/v1/messages/batches/{message_batch_id}/cancel`

Batches may be canceled any time before processing ends. Once cancellation is initiated, the batch enters a `canceling` state, at which time the system may complete any in-progress, non-interruptible requests before finalizing cancellation.

The number of canceled requests is specified in `request_counts`. To determine which requests were canceled, check the individual results within the batch. Note that cancellation may not result in any canceled requests if they were non-interruptible.

Learn more about the Message Batches API in our [user guide](https://docs.claude.com/en/docs/build-with-claude/batch-processing)

### Parameters

- `--message-batch-id: string`

  ID of the Message Batch.

- `--beta: optional array of AnthropicBeta`

  Optional header to specify the beta version(s) you want to use.

### Returns

- `beta_message_batch: object { id, archived_at, cancel_initiated_at, 7 more }`

  - `id: string`

    Unique object identifier.

    The format and length of IDs may change over time.

  - `archived_at: string`

    RFC 3339 datetime string representing the time at which the Message Batch was archived and its results became unavailable.

  - `cancel_initiated_at: string`

    RFC 3339 datetime string representing the time at which cancellation was initiated for the Message Batch. Specified only if cancellation was initiated.

  - `created_at: string`

    RFC 3339 datetime string representing the time at which the Message Batch was created.

  - `ended_at: string`

    RFC 3339 datetime string representing the time at which processing for the Message Batch ended. Specified only once processing ends.

    Processing ends when every request in a Message Batch has either succeeded, errored, canceled, or expired.

  - `expires_at: string`

    RFC 3339 datetime string representing the time at which the Message Batch will expire and end processing, which is 24 hours after creation.

  - `processing_status: "in_progress" or "canceling" or "ended"`

    Processing status of the Message Batch.

    - `"in_progress"`

    - `"canceling"`

    - `"ended"`

  - `request_counts: object { canceled, errored, expired, 2 more }`

    Tallies requests within the Message Batch, categorized by their status.

    Requests start as `processing` and move to one of the other statuses only once processing of the entire batch ends. The sum of all values always matches the total number of requests in the batch.

    - `canceled: number`

      Number of requests in the Message Batch that have been canceled.

      This is zero until processing of the entire Message Batch has ended.

    - `errored: number`

      Number of requests in the Message Batch that encountered an error.

      This is zero until processing of the entire Message Batch has ended.

    - `expired: number`

      Number of requests in the Message Batch that have expired.

      This is zero until processing of the entire Message Batch has ended.

    - `processing: number`

      Number of requests in the Message Batch that are processing.

    - `succeeded: number`

      Number of requests in the Message Batch that have completed successfully.

      This is zero until processing of the entire Message Batch has ended.

  - `results_url: string`

    URL to a `.jsonl` file containing the results of the Message Batch requests. Specified only once processing ends.

    Results in the file are not guaranteed to be in the same order as requests. Use the `custom_id` field to match results to requests.

  - `type: "message_batch"`

    Object type.

    For Message Batches, this is always `"message_batch"`.

### Example

```cli
ant beta:messages:batches cancel \
  --api-key my-anthropic-api-key \
  --message-batch-id message_batch_id
```

## Delete

`$ ant beta:messages:batches delete`

**delete** `/v1/messages/batches/{message_batch_id}`

Delete a Message Batch.

Message Batches can only be deleted once they've finished processing. If you'd like to delete an in-progress batch, you must first cancel it.

Learn more about the Message Batches API in our [user guide](https://docs.claude.com/en/docs/build-with-claude/batch-processing)

### Parameters

- `--message-batch-id: string`

  ID of the Message Batch.

- `--beta: optional array of AnthropicBeta`

  Optional header to specify the beta version(s) you want to use.

### Returns

- `beta_deleted_message_batch: object { id, type }`

  - `id: string`

    ID of the Message Batch.

  - `type: "message_batch_deleted"`

    Deleted object type.

    For Message Batches, this is always `"message_batch_deleted"`.

### Example

```cli
ant beta:messages:batches delete \
  --api-key my-anthropic-api-key \
  --message-batch-id message_batch_id
```

## Results

`$ ant beta:messages:batches results`

**get** `/v1/messages/batches/{message_batch_id}/results`

Streams the results of a Message Batch as a `.jsonl` file.

Each line in the file is a JSON object containing the result of a single request in the Message Batch. Results are not guaranteed to be in the same order as requests. Use the `custom_id` field to match results to requests.

Learn more about the Message Batches API in our [user guide](https://docs.claude.com/en/docs/build-with-claude/batch-processing)

### Parameters

- `--message-batch-id: string`

  ID of the Message Batch.

- `--beta: optional array of AnthropicBeta`

  Optional header to specify the beta version(s) you want to use.

### Returns

- `beta_message_batch_individual_response: object { custom_id, result }`

  This is a single line in the response `.jsonl` file and does not represent the response as a whole.

  - `custom_id: string`

    Developer-provided ID created for each request in a Message Batch. Useful for matching results to requests, as results may be given out of request order.

    Must be unique for each request within the Message Batch.

  - `result: BetaMessageBatchSucceededResult or BetaMessageBatchErroredResult or BetaMessageBatchCanceledResult or BetaMessageBatchExpiredResult`

    Processing result for this request.

    Contains a Message output if processing was successful, an error response if processing failed, or the reason why processing was not attempted, such as cancellation or expiration.

    - `beta_message_batch_succeeded_result: object { message, type }`

      - `message: object { id, container, content, 8 more }`

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

          - `beta_compaction_block: object { content, encrypted_content, type }`

            A compaction block returned when autocompact is triggered.

            When content is None, it indicates the compaction failed to produce a valid
            summary (e.g., malformed output from the model). Clients may round-trip
            compaction blocks with null content; the server treats them as no-ops.

            - `content: string`

              Summary of compacted content, or null if compaction failed

            - `encrypted_content: string`

              Opaque metadata from prior compaction, to be round-tripped verbatim

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

      - `type: "succeeded"`

    - `beta_message_batch_errored_result: object { error, type }`

      - `error: object { error, request_id, type }`

        - `error: BetaInvalidRequestError or BetaAuthenticationError or BetaBillingError or 6 more`

          - `beta_invalid_request_error: object { message, type }`

            - `message: string`

            - `type: "invalid_request_error"`

          - `beta_authentication_error: object { message, type }`

            - `message: string`

            - `type: "authentication_error"`

          - `beta_billing_error: object { message, type }`

            - `message: string`

            - `type: "billing_error"`

          - `beta_permission_error: object { message, type }`

            - `message: string`

            - `type: "permission_error"`

          - `beta_not_found_error: object { message, type }`

            - `message: string`

            - `type: "not_found_error"`

          - `beta_rate_limit_error: object { message, type }`

            - `message: string`

            - `type: "rate_limit_error"`

          - `beta_gateway_timeout_error: object { message, type }`

            - `message: string`

            - `type: "timeout_error"`

          - `beta_api_error: object { message, type }`

            - `message: string`

            - `type: "api_error"`

          - `beta_overloaded_error: object { message, type }`

            - `message: string`

            - `type: "overloaded_error"`

        - `request_id: string`

        - `type: "error"`

      - `type: "errored"`

    - `beta_message_batch_canceled_result: object { type }`

      - `type: "canceled"`

    - `beta_message_batch_expired_result: object { type }`

      - `type: "expired"`

### Example

```cli
ant beta:messages:batches results \
  --api-key my-anthropic-api-key \
  --message-batch-id message_batch_id
```

## Domain Types

### Beta Deleted Message Batch

- `beta_deleted_message_batch: object { id, type }`

  - `id: string`

    ID of the Message Batch.

  - `type: "message_batch_deleted"`

    Deleted object type.

    For Message Batches, this is always `"message_batch_deleted"`.

### Beta Message Batch

- `beta_message_batch: object { id, archived_at, cancel_initiated_at, 7 more }`

  - `id: string`

    Unique object identifier.

    The format and length of IDs may change over time.

  - `archived_at: string`

    RFC 3339 datetime string representing the time at which the Message Batch was archived and its results became unavailable.

  - `cancel_initiated_at: string`

    RFC 3339 datetime string representing the time at which cancellation was initiated for the Message Batch. Specified only if cancellation was initiated.

  - `created_at: string`

    RFC 3339 datetime string representing the time at which the Message Batch was created.

  - `ended_at: string`

    RFC 3339 datetime string representing the time at which processing for the Message Batch ended. Specified only once processing ends.

    Processing ends when every request in a Message Batch has either succeeded, errored, canceled, or expired.

  - `expires_at: string`

    RFC 3339 datetime string representing the time at which the Message Batch will expire and end processing, which is 24 hours after creation.

  - `processing_status: "in_progress" or "canceling" or "ended"`

    Processing status of the Message Batch.

    - `"in_progress"`

    - `"canceling"`

    - `"ended"`

  - `request_counts: object { canceled, errored, expired, 2 more }`

    Tallies requests within the Message Batch, categorized by their status.

    Requests start as `processing` and move to one of the other statuses only once processing of the entire batch ends. The sum of all values always matches the total number of requests in the batch.

    - `canceled: number`

      Number of requests in the Message Batch that have been canceled.

      This is zero until processing of the entire Message Batch has ended.

    - `errored: number`

      Number of requests in the Message Batch that encountered an error.

      This is zero until processing of the entire Message Batch has ended.

    - `expired: number`

      Number of requests in the Message Batch that have expired.

      This is zero until processing of the entire Message Batch has ended.

    - `processing: number`

      Number of requests in the Message Batch that are processing.

    - `succeeded: number`

      Number of requests in the Message Batch that have completed successfully.

      This is zero until processing of the entire Message Batch has ended.

  - `results_url: string`

    URL to a `.jsonl` file containing the results of the Message Batch requests. Specified only once processing ends.

    Results in the file are not guaranteed to be in the same order as requests. Use the `custom_id` field to match results to requests.

  - `type: "message_batch"`

    Object type.

    For Message Batches, this is always `"message_batch"`.

### Beta Message Batch Canceled Result

- `beta_message_batch_canceled_result: object { type }`

  - `type: "canceled"`

### Beta Message Batch Errored Result

- `beta_message_batch_errored_result: object { error, type }`

  - `error: object { error, request_id, type }`

    - `error: BetaInvalidRequestError or BetaAuthenticationError or BetaBillingError or 6 more`

      - `beta_invalid_request_error: object { message, type }`

        - `message: string`

        - `type: "invalid_request_error"`

      - `beta_authentication_error: object { message, type }`

        - `message: string`

        - `type: "authentication_error"`

      - `beta_billing_error: object { message, type }`

        - `message: string`

        - `type: "billing_error"`

      - `beta_permission_error: object { message, type }`

        - `message: string`

        - `type: "permission_error"`

      - `beta_not_found_error: object { message, type }`

        - `message: string`

        - `type: "not_found_error"`

      - `beta_rate_limit_error: object { message, type }`

        - `message: string`

        - `type: "rate_limit_error"`

      - `beta_gateway_timeout_error: object { message, type }`

        - `message: string`

        - `type: "timeout_error"`

      - `beta_api_error: object { message, type }`

        - `message: string`

        - `type: "api_error"`

      - `beta_overloaded_error: object { message, type }`

        - `message: string`

        - `type: "overloaded_error"`

    - `request_id: string`

    - `type: "error"`

  - `type: "errored"`

### Beta Message Batch Expired Result

- `beta_message_batch_expired_result: object { type }`

  - `type: "expired"`

### Beta Message Batch Individual Response

- `beta_message_batch_individual_response: object { custom_id, result }`

  This is a single line in the response `.jsonl` file and does not represent the response as a whole.

  - `custom_id: string`

    Developer-provided ID created for each request in a Message Batch. Useful for matching results to requests, as results may be given out of request order.

    Must be unique for each request within the Message Batch.

  - `result: BetaMessageBatchSucceededResult or BetaMessageBatchErroredResult or BetaMessageBatchCanceledResult or BetaMessageBatchExpiredResult`

    Processing result for this request.

    Contains a Message output if processing was successful, an error response if processing failed, or the reason why processing was not attempted, such as cancellation or expiration.

    - `beta_message_batch_succeeded_result: object { message, type }`

      - `message: object { id, container, content, 8 more }`

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

          - `beta_compaction_block: object { content, encrypted_content, type }`

            A compaction block returned when autocompact is triggered.

            When content is None, it indicates the compaction failed to produce a valid
            summary (e.g., malformed output from the model). Clients may round-trip
            compaction blocks with null content; the server treats them as no-ops.

            - `content: string`

              Summary of compacted content, or null if compaction failed

            - `encrypted_content: string`

              Opaque metadata from prior compaction, to be round-tripped verbatim

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

      - `type: "succeeded"`

    - `beta_message_batch_errored_result: object { error, type }`

      - `error: object { error, request_id, type }`

        - `error: BetaInvalidRequestError or BetaAuthenticationError or BetaBillingError or 6 more`

          - `beta_invalid_request_error: object { message, type }`

            - `message: string`

            - `type: "invalid_request_error"`

          - `beta_authentication_error: object { message, type }`

            - `message: string`

            - `type: "authentication_error"`

          - `beta_billing_error: object { message, type }`

            - `message: string`

            - `type: "billing_error"`

          - `beta_permission_error: object { message, type }`

            - `message: string`

            - `type: "permission_error"`

          - `beta_not_found_error: object { message, type }`

            - `message: string`

            - `type: "not_found_error"`

          - `beta_rate_limit_error: object { message, type }`

            - `message: string`

            - `type: "rate_limit_error"`

          - `beta_gateway_timeout_error: object { message, type }`

            - `message: string`

            - `type: "timeout_error"`

          - `beta_api_error: object { message, type }`

            - `message: string`

            - `type: "api_error"`

          - `beta_overloaded_error: object { message, type }`

            - `message: string`

            - `type: "overloaded_error"`

        - `request_id: string`

        - `type: "error"`

      - `type: "errored"`

    - `beta_message_batch_canceled_result: object { type }`

      - `type: "canceled"`

    - `beta_message_batch_expired_result: object { type }`

      - `type: "expired"`

### Beta Message Batch Request Counts

- `beta_message_batch_request_counts: object { canceled, errored, expired, 2 more }`

  - `canceled: number`

    Number of requests in the Message Batch that have been canceled.

    This is zero until processing of the entire Message Batch has ended.

  - `errored: number`

    Number of requests in the Message Batch that encountered an error.

    This is zero until processing of the entire Message Batch has ended.

  - `expired: number`

    Number of requests in the Message Batch that have expired.

    This is zero until processing of the entire Message Batch has ended.

  - `processing: number`

    Number of requests in the Message Batch that are processing.

  - `succeeded: number`

    Number of requests in the Message Batch that have completed successfully.

    This is zero until processing of the entire Message Batch has ended.

### Beta Message Batch Result

- `beta_message_batch_result: BetaMessageBatchSucceededResult or BetaMessageBatchErroredResult or BetaMessageBatchCanceledResult or BetaMessageBatchExpiredResult`

  Processing result for this request.

  Contains a Message output if processing was successful, an error response if processing failed, or the reason why processing was not attempted, such as cancellation or expiration.

  - `beta_message_batch_succeeded_result: object { message, type }`

    - `message: object { id, container, content, 8 more }`

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

        - `beta_compaction_block: object { content, encrypted_content, type }`

          A compaction block returned when autocompact is triggered.

          When content is None, it indicates the compaction failed to produce a valid
          summary (e.g., malformed output from the model). Clients may round-trip
          compaction blocks with null content; the server treats them as no-ops.

          - `content: string`

            Summary of compacted content, or null if compaction failed

          - `encrypted_content: string`

            Opaque metadata from prior compaction, to be round-tripped verbatim

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

    - `type: "succeeded"`

  - `beta_message_batch_errored_result: object { error, type }`

    - `error: object { error, request_id, type }`

      - `error: BetaInvalidRequestError or BetaAuthenticationError or BetaBillingError or 6 more`

        - `beta_invalid_request_error: object { message, type }`

          - `message: string`

          - `type: "invalid_request_error"`

        - `beta_authentication_error: object { message, type }`

          - `message: string`

          - `type: "authentication_error"`

        - `beta_billing_error: object { message, type }`

          - `message: string`

          - `type: "billing_error"`

        - `beta_permission_error: object { message, type }`

          - `message: string`

          - `type: "permission_error"`

        - `beta_not_found_error: object { message, type }`

          - `message: string`

          - `type: "not_found_error"`

        - `beta_rate_limit_error: object { message, type }`

          - `message: string`

          - `type: "rate_limit_error"`

        - `beta_gateway_timeout_error: object { message, type }`

          - `message: string`

          - `type: "timeout_error"`

        - `beta_api_error: object { message, type }`

          - `message: string`

          - `type: "api_error"`

        - `beta_overloaded_error: object { message, type }`

          - `message: string`

          - `type: "overloaded_error"`

      - `request_id: string`

      - `type: "error"`

    - `type: "errored"`

  - `beta_message_batch_canceled_result: object { type }`

    - `type: "canceled"`

  - `beta_message_batch_expired_result: object { type }`

    - `type: "expired"`

### Beta Message Batch Succeeded Result

- `beta_message_batch_succeeded_result: object { message, type }`

  - `message: object { id, container, content, 8 more }`

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

      - `beta_compaction_block: object { content, encrypted_content, type }`

        A compaction block returned when autocompact is triggered.

        When content is None, it indicates the compaction failed to produce a valid
        summary (e.g., malformed output from the model). Clients may round-trip
        compaction blocks with null content; the server treats them as no-ops.

        - `content: string`

          Summary of compacted content, or null if compaction failed

        - `encrypted_content: string`

          Opaque metadata from prior compaction, to be round-tripped verbatim

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

  - `type: "succeeded"`
