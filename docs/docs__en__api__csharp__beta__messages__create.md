## Create a Message

`BetaMessage Beta.Messages.Create(MessageCreateParamsparameters, CancellationTokencancellationToken = default)`

**post** `/v1/messages`

Send a structured list of input messages with text and/or image content, and the model will generate the next message in the conversation.

The Messages API can be used for either single queries or stateless multi-turn conversations.

Learn more about the Messages API in our [user guide](https://platform.claude.com/docs/en/get-started)

### Parameters

- `MessageCreateParams parameters`

  - `required Long maxTokens`

    Body param: The maximum number of tokens to generate before stopping.

    Note that our models may stop _before_ reaching this maximum. This parameter only specifies the absolute maximum number of tokens to generate.

    Set to `0` to populate the [prompt cache](https://platform.claude.com/docs/en/build-with-claude/prompt-caching#pre-warming-the-cache) without generating a response.

    Different models have different maximum values for this parameter.  See [models](https://platform.claude.com/docs/en/about-claude/models/overview) for details.

  - `required IReadOnlyList<BetaMessageParam> messages`

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

    See [input examples](https://platform.claude.com/docs/en/build-with-claude/working-with-messages).

    Note that if you want to include a [system prompt](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices#give-claude-a-role), you can use the top-level `system` parameter — there is no `"system"` role for input messages in the Messages API.

    There is a limit of 100,000 messages in a single request.

    - `required Content Content`

      - `string`

      - `IReadOnlyList<BetaContentBlockParam>`

        - `class BetaTextBlockParam:`

          - `required string Text`

          - `JsonElement Type "text"constant`

          - `BetaCacheControlEphemeral? CacheControl`

            Create a cache control breakpoint at this content block.

            - `JsonElement Type "ephemeral"constant`

            - `Ttl Ttl`

              The time-to-live for the cache control breakpoint.

              This may be one the following values:

              - `5m`: 5 minutes
              - `1h`: 1 hour

              Defaults to `5m`. See [prompt caching pricing](https://platform.claude.com/docs/en/build-with-claude/prompt-caching) for details.

              - `"5m"Ttl5m`

              - `"1h"Ttl1h`

          - `IReadOnlyList<BetaTextCitationParam>? Citations`

            - `class BetaCitationCharLocationParam:`

              - `required string CitedText`

              - `required Long DocumentIndex`

              - `required string? DocumentTitle`

              - `required Long EndCharIndex`

              - `required Long StartCharIndex`

              - `JsonElement Type "char_location"constant`

            - `class BetaCitationPageLocationParam:`

              - `required string CitedText`

              - `required Long DocumentIndex`

              - `required string? DocumentTitle`

              - `required Long EndPageNumber`

              - `required Long StartPageNumber`

              - `JsonElement Type "page_location"constant`

            - `class BetaCitationContentBlockLocationParam:`

              - `required string CitedText`

                The full text of the cited block range, concatenated.

                Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

              - `required Long DocumentIndex`

              - `required string? DocumentTitle`

              - `required Long EndBlockIndex`

                Exclusive 0-based end index of the cited block range in the source's `content` array.

                Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

              - `required Long StartBlockIndex`

                0-based index of the first cited block in the source's `content` array.

              - `JsonElement Type "content_block_location"constant`

            - `class BetaCitationWebSearchResultLocationParam:`

              - `required string CitedText`

              - `required string EncryptedIndex`

              - `required string? Title`

              - `JsonElement Type "web_search_result_location"constant`

              - `required string Url`

            - `class BetaCitationSearchResultLocationParam:`

              - `required string CitedText`

                The full text of the cited block range, concatenated.

                Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

              - `required Long EndBlockIndex`

                Exclusive 0-based end index of the cited block range in the source's `content` array.

                Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

              - `required Long SearchResultIndex`

                0-based index of the cited search result among all `search_result` content blocks in the request, in the order they appear across messages and tool results.

                Counted separately from `document_index`; server-side web search results are not included in this count.

              - `required string Source`

              - `required Long StartBlockIndex`

                0-based index of the first cited block in the source's `content` array.

              - `required string? Title`

              - `JsonElement Type "search_result_location"constant`

        - `class BetaImageBlockParam:`

          - `required Source Source`

            - `class BetaBase64ImageSource:`

              - `required string Data`

              - `required MediaType MediaType`

                - `"image/jpeg"ImageJpeg`

                - `"image/png"ImagePng`

                - `"image/gif"ImageGif`

                - `"image/webp"ImageWebP`

              - `JsonElement Type "base64"constant`

            - `class BetaUrlImageSource:`

              - `JsonElement Type "url"constant`

              - `required string Url`

            - `class BetaFileImageSource:`

              - `required string FileID`

              - `JsonElement Type "file"constant`

          - `JsonElement Type "image"constant`

          - `BetaCacheControlEphemeral? CacheControl`

            Create a cache control breakpoint at this content block.

        - `class BetaRequestDocumentBlock:`

          - `required Source Source`

            - `class BetaBase64PdfSource:`

              - `required string Data`

              - `JsonElement MediaType "application/pdf"constant`

              - `JsonElement Type "base64"constant`

            - `class BetaPlainTextSource:`

              - `required string Data`

              - `JsonElement MediaType "text/plain"constant`

              - `JsonElement Type "text"constant`

            - `class BetaContentBlockSource:`

              - `required Content Content`

                - `string`

                - `IReadOnlyList<BetaContentBlockSourceContent>`

                  - `class BetaTextBlockParam:`

                  - `class BetaImageBlockParam:`

              - `JsonElement Type "content"constant`

            - `class BetaUrlPdfSource:`

              - `JsonElement Type "url"constant`

              - `required string Url`

            - `class BetaFileDocumentSource:`

              - `required string FileID`

              - `JsonElement Type "file"constant`

          - `JsonElement Type "document"constant`

          - `BetaCacheControlEphemeral? CacheControl`

            Create a cache control breakpoint at this content block.

          - `BetaCitationsConfigParam? Citations`

            - `Boolean Enabled`

          - `string? Context`

          - `string? Title`

        - `class BetaSearchResultBlockParam:`

          - `required IReadOnlyList<BetaTextBlockParam> Content`

            - `required string Text`

            - `JsonElement Type "text"constant`

            - `BetaCacheControlEphemeral? CacheControl`

              Create a cache control breakpoint at this content block.

            - `IReadOnlyList<BetaTextCitationParam>? Citations`

          - `required string Source`

          - `required string Title`

          - `JsonElement Type "search_result"constant`

          - `BetaCacheControlEphemeral? CacheControl`

            Create a cache control breakpoint at this content block.

          - `BetaCitationsConfigParam Citations`

        - `class BetaThinkingBlockParam:`

          - `required string Signature`

          - `required string Thinking`

          - `JsonElement Type "thinking"constant`

        - `class BetaRedactedThinkingBlockParam:`

          - `required string Data`

          - `JsonElement Type "redacted_thinking"constant`

        - `class BetaToolUseBlockParam:`

          - `required string ID`

          - `required IReadOnlyDictionary<string, JsonElement> Input`

          - `required string Name`

          - `JsonElement Type "tool_use"constant`

          - `BetaCacheControlEphemeral? CacheControl`

            Create a cache control breakpoint at this content block.

          - `Caller Caller`

            Tool invocation directly from the model.

            - `class BetaDirectCaller:`

              Tool invocation directly from the model.

              - `JsonElement Type "direct"constant`

            - `class BetaServerToolCaller:`

              Tool invocation generated by a server-side tool.

              - `required string ToolID`

              - `JsonElement Type "code_execution_20250825"constant`

            - `class BetaServerToolCaller20260120:`

              - `required string ToolID`

              - `JsonElement Type "code_execution_20260120"constant`

        - `class BetaToolResultBlockParam:`

          - `required string ToolUseID`

          - `JsonElement Type "tool_result"constant`

          - `BetaCacheControlEphemeral? CacheControl`

            Create a cache control breakpoint at this content block.

          - `Content Content`

            - `string`

            - `IReadOnlyList<Block>`

              - `class BetaTextBlockParam:`

              - `class BetaImageBlockParam:`

              - `class BetaSearchResultBlockParam:`

              - `class BetaRequestDocumentBlock:`

              - `class BetaToolReferenceBlockParam:`

                Tool reference block that can be included in tool_result content.

                - `required string ToolName`

                - `JsonElement Type "tool_reference"constant`

                - `BetaCacheControlEphemeral? CacheControl`

                  Create a cache control breakpoint at this content block.

          - `Boolean IsError`

        - `class BetaServerToolUseBlockParam:`

          - `required string ID`

          - `required IReadOnlyDictionary<string, JsonElement> Input`

          - `required Name Name`

            - `"advisor"Advisor`

            - `"web_search"WebSearch`

            - `"web_fetch"WebFetch`

            - `"code_execution"CodeExecution`

            - `"bash_code_execution"BashCodeExecution`

            - `"text_editor_code_execution"TextEditorCodeExecution`

            - `"tool_search_tool_regex"ToolSearchToolRegex`

            - `"tool_search_tool_bm25"ToolSearchToolBm25`

          - `JsonElement Type "server_tool_use"constant`

          - `BetaCacheControlEphemeral? CacheControl`

            Create a cache control breakpoint at this content block.

          - `Caller Caller`

            Tool invocation directly from the model.

            - `class BetaDirectCaller:`

              Tool invocation directly from the model.

            - `class BetaServerToolCaller:`

              Tool invocation generated by a server-side tool.

            - `class BetaServerToolCaller20260120:`

        - `class BetaWebSearchToolResultBlockParam:`

          - `required BetaWebSearchToolResultBlockParamContent Content`

            - `IReadOnlyList<BetaWebSearchResultBlockParam>`

              - `required string EncryptedContent`

              - `required string Title`

              - `JsonElement Type "web_search_result"constant`

              - `required string Url`

              - `string? PageAge`

            - `class BetaWebSearchToolRequestError:`

              - `required BetaWebSearchToolResultErrorCode ErrorCode`

                - `"invalid_tool_input"InvalidToolInput`

                - `"unavailable"Unavailable`

                - `"max_uses_exceeded"MaxUsesExceeded`

                - `"too_many_requests"TooManyRequests`

                - `"query_too_long"QueryTooLong`

                - `"request_too_large"RequestTooLarge`

              - `JsonElement Type "web_search_tool_result_error"constant`

          - `required string ToolUseID`

          - `JsonElement Type "web_search_tool_result"constant`

          - `BetaCacheControlEphemeral? CacheControl`

            Create a cache control breakpoint at this content block.

          - `Caller Caller`

            Tool invocation directly from the model.

            - `class BetaDirectCaller:`

              Tool invocation directly from the model.

            - `class BetaServerToolCaller:`

              Tool invocation generated by a server-side tool.

            - `class BetaServerToolCaller20260120:`

        - `class BetaWebFetchToolResultBlockParam:`

          - `required Content Content`

            - `class BetaWebFetchToolResultErrorBlockParam:`

              - `required BetaWebFetchToolResultErrorCode ErrorCode`

                - `"invalid_tool_input"InvalidToolInput`

                - `"url_too_long"UrlTooLong`

                - `"url_not_allowed"UrlNotAllowed`

                - `"url_not_in_prior_context"UrlNotInPriorContext`

                - `"url_not_accessible"UrlNotAccessible`

                - `"unsupported_content_type"UnsupportedContentType`

                - `"too_many_requests"TooManyRequests`

                - `"max_uses_exceeded"MaxUsesExceeded`

                - `"unavailable"Unavailable`

              - `JsonElement Type "web_fetch_tool_result_error"constant`

            - `class BetaWebFetchBlockParam:`

              - `required BetaRequestDocumentBlock Content`

              - `JsonElement Type "web_fetch_result"constant`

              - `required string Url`

                Fetched content URL

              - `string? RetrievedAt`

                ISO 8601 timestamp when the content was retrieved

          - `required string ToolUseID`

          - `JsonElement Type "web_fetch_tool_result"constant`

          - `BetaCacheControlEphemeral? CacheControl`

            Create a cache control breakpoint at this content block.

          - `Caller Caller`

            Tool invocation directly from the model.

            - `class BetaDirectCaller:`

              Tool invocation directly from the model.

            - `class BetaServerToolCaller:`

              Tool invocation generated by a server-side tool.

            - `class BetaServerToolCaller20260120:`

        - `class BetaAdvisorToolResultBlockParam:`

          - `required Content Content`

            - `class BetaAdvisorToolResultErrorParam:`

              - `required ErrorCode ErrorCode`

                - `"max_uses_exceeded"MaxUsesExceeded`

                - `"prompt_too_long"PromptTooLong`

                - `"too_many_requests"TooManyRequests`

                - `"overloaded"Overloaded`

                - `"unavailable"Unavailable`

                - `"execution_time_exceeded"ExecutionTimeExceeded`

                - `"model_not_found"ModelNotFound`

              - `JsonElement Type "advisor_tool_result_error"constant`

            - `class BetaAdvisorResultBlockParam:`

              - `required string Text`

              - `JsonElement Type "advisor_result"constant`

              - `string? StopReason`

            - `class BetaAdvisorRedactedResultBlockParam:`

              - `required string EncryptedContent`

                Opaque blob produced by a prior response; must be round-tripped verbatim.

              - `JsonElement Type "advisor_redacted_result"constant`

              - `string? StopReason`

          - `required string ToolUseID`

          - `JsonElement Type "advisor_tool_result"constant`

          - `BetaCacheControlEphemeral? CacheControl`

            Create a cache control breakpoint at this content block.

        - `class BetaCodeExecutionToolResultBlockParam:`

          - `required BetaCodeExecutionToolResultBlockParamContent Content`

            Code execution result with encrypted stdout for PFC + web_search results.

            - `class BetaCodeExecutionToolResultErrorParam:`

              - `required BetaCodeExecutionToolResultErrorCode ErrorCode`

                - `"invalid_tool_input"InvalidToolInput`

                - `"unavailable"Unavailable`

                - `"too_many_requests"TooManyRequests`

                - `"execution_time_exceeded"ExecutionTimeExceeded`

              - `JsonElement Type "code_execution_tool_result_error"constant`

            - `class BetaCodeExecutionResultBlockParam:`

              - `required IReadOnlyList<BetaCodeExecutionOutputBlockParam> Content`

                - `required string FileID`

                - `JsonElement Type "code_execution_output"constant`

              - `required Long ReturnCode`

              - `required string Stderr`

              - `required string Stdout`

              - `JsonElement Type "code_execution_result"constant`

            - `class BetaEncryptedCodeExecutionResultBlockParam:`

              Code execution result with encrypted stdout for PFC + web_search results.

              - `required IReadOnlyList<BetaCodeExecutionOutputBlockParam> Content`

                - `required string FileID`

                - `JsonElement Type "code_execution_output"constant`

              - `required string EncryptedStdout`

              - `required Long ReturnCode`

              - `required string Stderr`

              - `JsonElement Type "encrypted_code_execution_result"constant`

          - `required string ToolUseID`

          - `JsonElement Type "code_execution_tool_result"constant`

          - `BetaCacheControlEphemeral? CacheControl`

            Create a cache control breakpoint at this content block.

        - `class BetaBashCodeExecutionToolResultBlockParam:`

          - `required Content Content`

            - `class BetaBashCodeExecutionToolResultErrorParam:`

              - `required ErrorCode ErrorCode`

                - `"invalid_tool_input"InvalidToolInput`

                - `"unavailable"Unavailable`

                - `"too_many_requests"TooManyRequests`

                - `"execution_time_exceeded"ExecutionTimeExceeded`

                - `"output_file_too_large"OutputFileTooLarge`

              - `JsonElement Type "bash_code_execution_tool_result_error"constant`

            - `class BetaBashCodeExecutionResultBlockParam:`

              - `required IReadOnlyList<BetaBashCodeExecutionOutputBlockParam> Content`

                - `required string FileID`

                - `JsonElement Type "bash_code_execution_output"constant`

              - `required Long ReturnCode`

              - `required string Stderr`

              - `required string Stdout`

              - `JsonElement Type "bash_code_execution_result"constant`

          - `required string ToolUseID`

          - `JsonElement Type "bash_code_execution_tool_result"constant`

          - `BetaCacheControlEphemeral? CacheControl`

            Create a cache control breakpoint at this content block.

        - `class BetaTextEditorCodeExecutionToolResultBlockParam:`

          - `required Content Content`

            - `class BetaTextEditorCodeExecutionToolResultErrorParam:`

              - `required ErrorCode ErrorCode`

                - `"invalid_tool_input"InvalidToolInput`

                - `"unavailable"Unavailable`

                - `"too_many_requests"TooManyRequests`

                - `"execution_time_exceeded"ExecutionTimeExceeded`

                - `"file_not_found"FileNotFound`

              - `JsonElement Type "text_editor_code_execution_tool_result_error"constant`

              - `string? ErrorMessage`

            - `class BetaTextEditorCodeExecutionViewResultBlockParam:`

              - `required string Content`

              - `required FileType FileType`

                - `"text"Text`

                - `"image"Image`

                - `"pdf"Pdf`

              - `JsonElement Type "text_editor_code_execution_view_result"constant`

              - `Long? NumLines`

              - `Long? StartLine`

              - `Long? TotalLines`

            - `class BetaTextEditorCodeExecutionCreateResultBlockParam:`

              - `required Boolean IsFileUpdate`

              - `JsonElement Type "text_editor_code_execution_create_result"constant`

            - `class BetaTextEditorCodeExecutionStrReplaceResultBlockParam:`

              - `JsonElement Type "text_editor_code_execution_str_replace_result"constant`

              - `IReadOnlyList<string>? Lines`

              - `Long? NewLines`

              - `Long? NewStart`

              - `Long? OldLines`

              - `Long? OldStart`

          - `required string ToolUseID`

          - `JsonElement Type "text_editor_code_execution_tool_result"constant`

          - `BetaCacheControlEphemeral? CacheControl`

            Create a cache control breakpoint at this content block.

        - `class BetaToolSearchToolResultBlockParam:`

          - `required Content Content`

            - `class BetaToolSearchToolResultErrorParam:`

              - `required ErrorCode ErrorCode`

                - `"invalid_tool_input"InvalidToolInput`

                - `"unavailable"Unavailable`

                - `"too_many_requests"TooManyRequests`

                - `"execution_time_exceeded"ExecutionTimeExceeded`

              - `JsonElement Type "tool_search_tool_result_error"constant`

              - `string? ErrorMessage`

            - `class BetaToolSearchToolSearchResultBlockParam:`

              - `required IReadOnlyList<BetaToolReferenceBlockParam> ToolReferences`

                - `required string ToolName`

                - `JsonElement Type "tool_reference"constant`

                - `BetaCacheControlEphemeral? CacheControl`

                  Create a cache control breakpoint at this content block.

              - `JsonElement Type "tool_search_tool_search_result"constant`

          - `required string ToolUseID`

          - `JsonElement Type "tool_search_tool_result"constant`

          - `BetaCacheControlEphemeral? CacheControl`

            Create a cache control breakpoint at this content block.

        - `class BetaMcpToolUseBlockParam:`

          - `required string ID`

          - `required IReadOnlyDictionary<string, JsonElement> Input`

          - `required string Name`

          - `required string ServerName`

            The name of the MCP server

          - `JsonElement Type "mcp_tool_use"constant`

          - `BetaCacheControlEphemeral? CacheControl`

            Create a cache control breakpoint at this content block.

        - `class BetaRequestMcpToolResultBlockParam:`

          - `required string ToolUseID`

          - `JsonElement Type "mcp_tool_result"constant`

          - `BetaCacheControlEphemeral? CacheControl`

            Create a cache control breakpoint at this content block.

          - `Content Content`

            - `string`

            - `IReadOnlyList<BetaTextBlockParam>`

              - `required string Text`

              - `JsonElement Type "text"constant`

              - `BetaCacheControlEphemeral? CacheControl`

                Create a cache control breakpoint at this content block.

              - `IReadOnlyList<BetaTextCitationParam>? Citations`

          - `Boolean IsError`

        - `class BetaContainerUploadBlockParam:`

          A content block that represents a file to be uploaded to the container
          Files uploaded via this block will be available in the container's input directory.

          - `required string FileID`

          - `JsonElement Type "container_upload"constant`

          - `BetaCacheControlEphemeral? CacheControl`

            Create a cache control breakpoint at this content block.

        - `class BetaCompactionBlockParam:`

          A compaction block containing summary of previous context.

          Users should round-trip these blocks from responses to subsequent requests
          to maintain context across compaction boundaries.

          When content is None, the block represents a failed compaction. The server
          treats these as no-ops. Empty string content is not allowed.

          - `JsonElement Type "compaction"constant`

          - `BetaCacheControlEphemeral? CacheControl`

            Create a cache control breakpoint at this content block.

          - `string? Content`

            Summary of previously compacted content, or null if compaction failed

          - `string? EncryptedContent`

            Opaque metadata from prior compaction, to be round-tripped verbatim

        - `class BetaMidConversationSystemBlockParam:`

          System instructions that appear mid-conversation.

          Use this block to provide or update system-level instructions at a specific
          point in the conversation, rather than only via the top-level `system` parameter.

          - `required IReadOnlyList<BetaTextBlockParam> Content`

            System instruction text blocks.

            - `required string Text`

            - `JsonElement Type "text"constant`

            - `BetaCacheControlEphemeral? CacheControl`

              Create a cache control breakpoint at this content block.

            - `IReadOnlyList<BetaTextCitationParam>? Citations`

          - `JsonElement Type "mid_conv_system"constant`

          - `BetaCacheControlEphemeral? CacheControl`

            Create a cache control breakpoint at this content block.

        - `class BetaFallbackBlockParam:`

          A `fallback` block echoed back from a prior response.

          Accepted in `messages[].content` and not rendered into the prompt; not
          validated against the request's `fallbacks` chain or top-level `model`.

          Echo the assistant turn back verbatim, including this block in its
          original position. The block marks the boundary between content produced
          before and after a fallback hop, and the server relies on that boundary
          to validate the turn: when thinking runs flank the boundary, omitting
          the block merges them into one span the server cannot validate (the
          request is rejected), and moving it into the middle of a single run is
          likewise rejected; between non-thinking blocks the block's placement has
          no validation effect.

          - `required BetaFallbackInfoParam From`

            Identifies one hop of a fallback transition.

            - `required Model Model`

              The model that will complete your prompt.

              See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

              - `"claude-fable-5"ClaudeFable5`

                Next generation of intelligence for the hardest knowledge work and coding problems

              - `"claude-mythos-5"ClaudeMythos5`

                Most capable model for cybersecurity and biology research

              - `"claude-opus-4-8"ClaudeOpus4_8`

                Frontier intelligence for long-running agents and coding

              - `"claude-opus-4-7"ClaudeOpus4_7`

                Frontier intelligence for long-running agents and coding

              - `"claude-mythos-preview"ClaudeMythosPreview`

                New class of intelligence, strongest in coding and cybersecurity

              - `"claude-opus-4-6"ClaudeOpus4_6`

                Frontier intelligence for long-running agents and coding

              - `"claude-sonnet-4-6"ClaudeSonnet4_6`

                Best combination of speed and intelligence

              - `"claude-haiku-4-5"ClaudeHaiku4_5`

                Fastest model with near-frontier intelligence

              - `"claude-haiku-4-5-20251001"ClaudeHaiku4_5_20251001`

                Fastest model with near-frontier intelligence

              - `"claude-opus-4-5"ClaudeOpus4_5`

                Premium model combining maximum intelligence with practical performance

              - `"claude-opus-4-5-20251101"ClaudeOpus4_5_20251101`

                Premium model combining maximum intelligence with practical performance

              - `"claude-sonnet-4-5"ClaudeSonnet4_5`

                High-performance model for agents and coding

              - `"claude-sonnet-4-5-20250929"ClaudeSonnet4_5_20250929`

                High-performance model for agents and coding

              - `"claude-opus-4-1"ClaudeOpus4_1`

                Exceptional model for specialized complex tasks

              - `"claude-opus-4-1-20250805"ClaudeOpus4_1_20250805`

                Exceptional model for specialized complex tasks

          - `required BetaFallbackInfoParam To`

            Identifies one hop of a fallback transition.

          - `JsonElement Type "fallback"constant`

          - `JsonElement Trigger`

            The response block's `trigger`, echoed verbatim. Accepted and ignored by the server; any object or `null` is allowed.

    - `required Role Role`

      - `"user"User`

      - `"assistant"Assistant`

      - `"system"System`

  - `required Model model`

    Body param: The model that will complete your prompt.

    See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

  - `BetaCacheControlEphemeral? cacheControl`

    Body param: Top-level cache control automatically applies a cache_control marker to the last cacheable block in the request.

  - `Container? container`

    Body param: Container identifier for reuse across requests.

    - `class BetaContainerParams:`

      Container parameters with skills to be loaded.

      - `string? ID`

        Container id

      - `IReadOnlyList<BetaSkillParams>? Skills`

        List of skills to load in the container

        - `required string SkillID`

          Skill ID

        - `required Type Type`

          Type of skill - either 'anthropic' (built-in) or 'custom' (user-defined)

          - `"anthropic"Anthropic`

          - `"custom"Custom`

        - `string Version`

          Skill version or 'latest' for most recent version

    - `string`

  - `BetaContextManagementConfig? contextManagement`

    Body param: Context management configuration.

    This allows you to control how Claude manages context across multiple requests, such as whether to clear function results or not.

  - `BetaDiagnosticsParam? diagnostics`

    Body param: Request-level diagnostics. Currently carries the previous response
    id for prompt-cache divergence reporting.

  - `string? fallbackCreditToken`

    Body param: The `fallback_credit_token` from a prior refusal's `stop_details`.

    When a preceding request was refused and returned a `fallback_credit_token`,
    pass that code here on the retry to have the retry's cache-creation tokens
    for the prefix that was warm on the refused model billed at the cache-read
    rate. Must be redeemed by the same organization and workspace, with the same
    request body (optionally extended by one appended `assistant` message whose
    content is the partial text — with any trailing whitespace stripped from
    the final text block — and paired server-tool blocks streamed before the
    refusal; the appended-assistant form is not available for requests with
    `output_format` set or forced `tool_choice`), on an eligible fallback
    model, on the same platform,
    and within 5 minutes of the refusal; a mismatch is a 400. A token minted
    mid-server-tool-loop whose partial content was continuable may only be
    redeemed with the appended-assistant form — if an exact-body retry is
    rejected with a 400 saying the token must be redeemed by continuing the
    partial response, retry with the appended-assistant form instead.

    When the appended-assistant form is used on a model that otherwise disallows
    assistant-turn prefill, this token also authorizes that one prefill.

  - `IReadOnlyList<BetaFallbackParam>? fallbacks`

    Body param: Opt-in server-side retry on one or more substitute models when the requested model declines for policy reasons. Tried in order: if the first entry also declines, the second is tried, and so on.

    - `required Model Model`

      The model that will complete your prompt.

      See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

    - `Long? MaxTokens`

    - `BetaOutputConfig? OutputConfig`

      - `Effort? Effort`

        All possible effort levels.

        - `"low"Low`

        - `"medium"Medium`

        - `"high"High`

        - `"xhigh"Xhigh`

        - `"max"Max`

      - `BetaJsonOutputFormat? Format`

        A schema to specify Claude's output format in responses. See [structured outputs](https://platform.claude.com/docs/en/build-with-claude/structured-outputs)

        - `required IReadOnlyDictionary<string, JsonElement> Schema`

          The JSON schema of the format

        - `JsonElement Type "json_schema"constant`

      - `BetaTokenTaskBudget? TaskBudget`

        User-configurable total token budget across contexts.

        - `required Long Total`

          Total token budget across all contexts in the session.

        - `JsonElement Type "tokens"constant`

          The budget type. Currently only 'tokens' is supported.

        - `Long? Remaining`

          Remaining tokens in the budget. Use this to track usage across contexts when implementing compaction client-side. Defaults to total if not provided.

    - `Speed? Speed`

      - `"standard"Standard`

      - `"fast"Fast`

    - `Thinking? Thinking`

      - `class BetaThinkingConfigEnabled:`

        - `required Long BudgetTokens`

          Determines how many tokens Claude can use for its internal reasoning process. Larger budgets can enable more thorough analysis for complex problems, improving response quality.

          Must be ≥1024 and less than `max_tokens`.

          See [extended thinking](https://platform.claude.com/docs/en/build-with-claude/extended-thinking) for details.

        - `JsonElement Type "enabled"constant`

        - `Display? Display`

          Controls how thinking content appears in the response. When set to `summarized`, thinking is returned normally. When set to `omitted`, thinking content is redacted but a signature is returned for multi-turn continuity. Defaults to `summarized`.

          - `"summarized"Summarized`

          - `"omitted"Omitted`

      - `class BetaThinkingConfigDisabled:`

        - `JsonElement Type "disabled"constant`

      - `class BetaThinkingConfigAdaptive:`

        - `JsonElement Type "adaptive"constant`

        - `Display? Display`

          Controls how thinking content appears in the response. When set to `summarized`, thinking is returned normally. When set to `omitted`, thinking content is redacted but a signature is returned for multi-turn continuity. Defaults to `summarized`.

          - `"summarized"Summarized`

          - `"omitted"Omitted`

  - `string? inferenceGeo`

    Body param: Specifies the geographic region for inference processing. If not specified, the workspace's `default_inference_geo` is used.

  - `IReadOnlyList<BetaRequestMcpServerUrlDefinition> mcpServers`

    Body param: MCP servers to be utilized in this request

    - `required string Name`

    - `JsonElement Type "url"constant`

    - `required string Url`

    - `string? AuthorizationToken`

    - `BetaRequestMcpServerToolConfiguration? ToolConfiguration`

      - `IReadOnlyList<string>? AllowedTools`

      - `Boolean? Enabled`

  - `BetaMetadata metadata`

    Body param: An object describing metadata about the request.

  - `BetaOutputConfig outputConfig`

    Body param: Configuration options for the model's output, such as the output format.

  - `BetaJsonOutputFormat? outputFormat`

    Body param: Deprecated: Use `output_config.format` instead. See [structured outputs](https://platform.claude.com/docs/en/build-with-claude/structured-outputs)

    A schema to specify Claude's output format in responses. This parameter will be removed in a future release.

  - `ServiceTier serviceTier`

    Body param: Determines whether to use priority capacity (if available) or standard capacity for this request.

    Anthropic offers different levels of service for your API requests. See [service-tiers](https://platform.claude.com/docs/en/api/service-tiers) for details.

    - `"auto"Auto`

    - `"standard_only"StandardOnly`

  - `Speed? speed`

    Body param: The inference speed mode for this request. `"fast"` enables high output-tokens-per-second inference.

    - `"standard"Standard`

    - `"fast"Fast`

  - `IReadOnlyList<string> stopSequences`

    Body param: Custom text sequences that will cause the model to stop generating.

    Our models will normally stop when they have naturally completed their turn, which will result in a response `stop_reason` of `"end_turn"`.

    If you want the model to stop generating when it encounters custom strings of text, you can use the `stop_sequences` parameter. If the model encounters one of the custom sequences, the response `stop_reason` value will be `"stop_sequence"` and the response `stop_sequence` value will contain the matched stop sequence.

  - `System system`

    Body param: System prompt.

    A system prompt is a way of providing context and instructions to Claude, such as specifying a particular goal or role. See our [guide to system prompts](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices#give-claude-a-role).

    - `string`

    - `IReadOnlyList<BetaTextBlockParam>`

      - `required string Text`

      - `JsonElement Type "text"constant`

      - `BetaCacheControlEphemeral? CacheControl`

        Create a cache control breakpoint at this content block.

      - `IReadOnlyList<BetaTextCitationParam>? Citations`

  - `Double temperature`

    Body param: Amount of randomness injected into the response.

    Defaults to `1.0`. Ranges from `0.0` to `1.0`. Use `temperature` closer to `0.0` for analytical / multiple choice, and closer to `1.0` for creative and generative tasks.

    Note that even with `temperature` of `0.0`, the results will not be fully deterministic.

  - `BetaThinkingConfigParam thinking`

    Body param: Configuration for enabling Claude's extended thinking.

    When enabled, responses include `thinking` content blocks showing Claude's thinking process before the final answer. Requires a minimum budget of 1,024 tokens and counts towards your `max_tokens` limit.

    See [extended thinking](https://platform.claude.com/docs/en/build-with-claude/extended-thinking) for details.

  - `BetaToolChoice toolChoice`

    Body param: How the model should use the provided tools. The model can use a specific tool, any available tool, decide by itself, or not use tools at all.

  - `IReadOnlyList<BetaToolUnion> tools`

    Body param: Definitions of tools that the model may use.

    If you include `tools` in your API request, the model may return `tool_use` content blocks that represent the model's use of those tools. You can then run those tools using the tool input generated by the model and then optionally return results back to the model using `tool_result` content blocks.

    There are two types of tools: **client tools** and **server tools**. The behavior described below applies to client tools. For [server tools](https://platform.claude.com/docs/en/agents-and-tools/tool-use/server-tools), see their individual documentation as each has its own behavior (e.g., the [web search tool](https://platform.claude.com/docs/en/agents-and-tools/tool-use/web-search-tool)).

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

    See our [guide](https://platform.claude.com/docs/en/agents-and-tools/tool-use/overview) for more details.

    - `class BetaTool:`

      - `required InputSchema InputSchema`

        [JSON schema](https://json-schema.org/draft/2020-12) for this tool's input.

        This defines the shape of the `input` that your tool accepts and that the model will produce.

        - `JsonElement Type "object"constant`

        - `IReadOnlyDictionary<string, JsonElement>? Properties`

        - `IReadOnlyList<string>? Required`

      - `required string Name`

        Name of the tool.

        This is how the tool will be called by the model and in `tool_use` blocks.

      - `IReadOnlyList<AllowedCaller> AllowedCallers`

        - `"direct"Direct`

        - `"code_execution_20250825"CodeExecution20250825`

        - `"code_execution_20260120"CodeExecution20260120`

        - `"code_execution_20260521"CodeExecution20260521`

      - `BetaCacheControlEphemeral? CacheControl`

        Create a cache control breakpoint at this content block.

      - `Boolean DeferLoading`

        If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

      - `string Description`

        Description of what this tool does.

        Tool descriptions should be as detailed as possible. The more information that the model has about what the tool is and how to use it, the better it will perform. You can use natural language descriptions to reinforce important aspects of the tool input JSON schema.

      - `Boolean? EagerInputStreaming`

        Enable eager input streaming for this tool. When true, tool input parameters will be streamed incrementally as they are generated, and types will be inferred on-the-fly rather than buffering the full JSON output. When false, streaming is disabled for this tool even if the fine-grained-tool-streaming beta is active. When null (default), uses the default behavior based on beta headers.

      - `IReadOnlyList<IReadOnlyDictionary<string, JsonElement>> InputExamples`

      - `Boolean Strict`

        When true, guarantees schema validation on tool names and inputs

      - `Type? Type`

        - `"custom"Custom`

    - `class BetaToolBash20241022:`

      - `JsonElement Name "bash"constant`

        Name of the tool.

        This is how the tool will be called by the model and in `tool_use` blocks.

      - `JsonElement Type "bash_20241022"constant`

      - `IReadOnlyList<AllowedCaller> AllowedCallers`

        - `"direct"Direct`

        - `"code_execution_20250825"CodeExecution20250825`

        - `"code_execution_20260120"CodeExecution20260120`

        - `"code_execution_20260521"CodeExecution20260521`

      - `BetaCacheControlEphemeral? CacheControl`

        Create a cache control breakpoint at this content block.

      - `Boolean DeferLoading`

        If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

      - `IReadOnlyList<IReadOnlyDictionary<string, JsonElement>> InputExamples`

      - `Boolean Strict`

        When true, guarantees schema validation on tool names and inputs

    - `class BetaToolBash20250124:`

      - `JsonElement Name "bash"constant`

        Name of the tool.

        This is how the tool will be called by the model and in `tool_use` blocks.

      - `JsonElement Type "bash_20250124"constant`

      - `IReadOnlyList<AllowedCaller> AllowedCallers`

        - `"direct"Direct`

        - `"code_execution_20250825"CodeExecution20250825`

        - `"code_execution_20260120"CodeExecution20260120`

        - `"code_execution_20260521"CodeExecution20260521`

      - `BetaCacheControlEphemeral? CacheControl`

        Create a cache control breakpoint at this content block.

      - `Boolean DeferLoading`

        If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

      - `IReadOnlyList<IReadOnlyDictionary<string, JsonElement>> InputExamples`

      - `Boolean Strict`

        When true, guarantees schema validation on tool names and inputs

    - `class BetaCodeExecutionTool20250522:`

      - `JsonElement Name "code_execution"constant`

        Name of the tool.

        This is how the tool will be called by the model and in `tool_use` blocks.

      - `JsonElement Type "code_execution_20250522"constant`

      - `IReadOnlyList<AllowedCaller> AllowedCallers`

        - `"direct"Direct`

        - `"code_execution_20250825"CodeExecution20250825`

        - `"code_execution_20260120"CodeExecution20260120`

        - `"code_execution_20260521"CodeExecution20260521`

      - `BetaCacheControlEphemeral? CacheControl`

        Create a cache control breakpoint at this content block.

      - `Boolean DeferLoading`

        If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

      - `Boolean Strict`

        When true, guarantees schema validation on tool names and inputs

    - `class BetaCodeExecutionTool20250825:`

      - `JsonElement Name "code_execution"constant`

        Name of the tool.

        This is how the tool will be called by the model and in `tool_use` blocks.

      - `JsonElement Type "code_execution_20250825"constant`

      - `IReadOnlyList<AllowedCaller> AllowedCallers`

        - `"direct"Direct`

        - `"code_execution_20250825"CodeExecution20250825`

        - `"code_execution_20260120"CodeExecution20260120`

        - `"code_execution_20260521"CodeExecution20260521`

      - `BetaCacheControlEphemeral? CacheControl`

        Create a cache control breakpoint at this content block.

      - `Boolean DeferLoading`

        If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

      - `Boolean Strict`

        When true, guarantees schema validation on tool names and inputs

    - `class BetaCodeExecutionTool20260120:`

      Code execution tool with REPL state persistence (daemon mode + gVisor checkpoint).

      - `JsonElement Name "code_execution"constant`

        Name of the tool.

        This is how the tool will be called by the model and in `tool_use` blocks.

      - `JsonElement Type "code_execution_20260120"constant`

      - `IReadOnlyList<AllowedCaller> AllowedCallers`

        - `"direct"Direct`

        - `"code_execution_20250825"CodeExecution20250825`

        - `"code_execution_20260120"CodeExecution20260120`

        - `"code_execution_20260521"CodeExecution20260521`

      - `BetaCacheControlEphemeral? CacheControl`

        Create a cache control breakpoint at this content block.

      - `Boolean DeferLoading`

        If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

      - `Boolean Strict`

        When true, guarantees schema validation on tool names and inputs

    - `class BetaCodeExecutionTool20260521:`

      Code execution tool with REPL state persistence.

      - `JsonElement Name "code_execution"constant`

        Name of the tool.

        This is how the tool will be called by the model and in `tool_use` blocks.

      - `JsonElement Type "code_execution_20260521"constant`

      - `IReadOnlyList<AllowedCaller> AllowedCallers`

        - `"direct"Direct`

        - `"code_execution_20250825"CodeExecution20250825`

        - `"code_execution_20260120"CodeExecution20260120`

        - `"code_execution_20260521"CodeExecution20260521`

      - `BetaCacheControlEphemeral? CacheControl`

        Create a cache control breakpoint at this content block.

      - `Boolean DeferLoading`

        If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

      - `Boolean Strict`

        When true, guarantees schema validation on tool names and inputs

    - `class BetaToolComputerUse20241022:`

      - `required Long DisplayHeightPx`

        The height of the display in pixels.

      - `required Long DisplayWidthPx`

        The width of the display in pixels.

      - `JsonElement Name "computer"constant`

        Name of the tool.

        This is how the tool will be called by the model and in `tool_use` blocks.

      - `JsonElement Type "computer_20241022"constant`

      - `IReadOnlyList<AllowedCaller> AllowedCallers`

        - `"direct"Direct`

        - `"code_execution_20250825"CodeExecution20250825`

        - `"code_execution_20260120"CodeExecution20260120`

        - `"code_execution_20260521"CodeExecution20260521`

      - `BetaCacheControlEphemeral? CacheControl`

        Create a cache control breakpoint at this content block.

      - `Boolean DeferLoading`

        If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

      - `Long? DisplayNumber`

        The X11 display number (e.g. 0, 1) for the display.

      - `IReadOnlyList<IReadOnlyDictionary<string, JsonElement>> InputExamples`

      - `Boolean Strict`

        When true, guarantees schema validation on tool names and inputs

    - `class BetaMemoryTool20250818:`

      - `JsonElement Name "memory"constant`

        Name of the tool.

        This is how the tool will be called by the model and in `tool_use` blocks.

      - `JsonElement Type "memory_20250818"constant`

      - `IReadOnlyList<AllowedCaller> AllowedCallers`

        - `"direct"Direct`

        - `"code_execution_20250825"CodeExecution20250825`

        - `"code_execution_20260120"CodeExecution20260120`

        - `"code_execution_20260521"CodeExecution20260521`

      - `BetaCacheControlEphemeral? CacheControl`

        Create a cache control breakpoint at this content block.

      - `Boolean DeferLoading`

        If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

      - `IReadOnlyList<IReadOnlyDictionary<string, JsonElement>> InputExamples`

      - `Boolean Strict`

        When true, guarantees schema validation on tool names and inputs

    - `class BetaToolComputerUse20250124:`

      - `required Long DisplayHeightPx`

        The height of the display in pixels.

      - `required Long DisplayWidthPx`

        The width of the display in pixels.

      - `JsonElement Name "computer"constant`

        Name of the tool.

        This is how the tool will be called by the model and in `tool_use` blocks.

      - `JsonElement Type "computer_20250124"constant`

      - `IReadOnlyList<AllowedCaller> AllowedCallers`

        - `"direct"Direct`

        - `"code_execution_20250825"CodeExecution20250825`

        - `"code_execution_20260120"CodeExecution20260120`

        - `"code_execution_20260521"CodeExecution20260521`

      - `BetaCacheControlEphemeral? CacheControl`

        Create a cache control breakpoint at this content block.

      - `Boolean DeferLoading`

        If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

      - `Long? DisplayNumber`

        The X11 display number (e.g. 0, 1) for the display.

      - `IReadOnlyList<IReadOnlyDictionary<string, JsonElement>> InputExamples`

      - `Boolean Strict`

        When true, guarantees schema validation on tool names and inputs

    - `class BetaToolTextEditor20241022:`

      - `JsonElement Name "str_replace_editor"constant`

        Name of the tool.

        This is how the tool will be called by the model and in `tool_use` blocks.

      - `JsonElement Type "text_editor_20241022"constant`

      - `IReadOnlyList<AllowedCaller> AllowedCallers`

        - `"direct"Direct`

        - `"code_execution_20250825"CodeExecution20250825`

        - `"code_execution_20260120"CodeExecution20260120`

        - `"code_execution_20260521"CodeExecution20260521`

      - `BetaCacheControlEphemeral? CacheControl`

        Create a cache control breakpoint at this content block.

      - `Boolean DeferLoading`

        If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

      - `IReadOnlyList<IReadOnlyDictionary<string, JsonElement>> InputExamples`

      - `Boolean Strict`

        When true, guarantees schema validation on tool names and inputs

    - `class BetaToolComputerUse20251124:`

      - `required Long DisplayHeightPx`

        The height of the display in pixels.

      - `required Long DisplayWidthPx`

        The width of the display in pixels.

      - `JsonElement Name "computer"constant`

        Name of the tool.

        This is how the tool will be called by the model and in `tool_use` blocks.

      - `JsonElement Type "computer_20251124"constant`

      - `IReadOnlyList<AllowedCaller> AllowedCallers`

        - `"direct"Direct`

        - `"code_execution_20250825"CodeExecution20250825`

        - `"code_execution_20260120"CodeExecution20260120`

        - `"code_execution_20260521"CodeExecution20260521`

      - `BetaCacheControlEphemeral? CacheControl`

        Create a cache control breakpoint at this content block.

      - `Boolean DeferLoading`

        If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

      - `Long? DisplayNumber`

        The X11 display number (e.g. 0, 1) for the display.

      - `Boolean EnableZoom`

        Whether to enable an action to take a zoomed-in screenshot of the screen.

      - `IReadOnlyList<IReadOnlyDictionary<string, JsonElement>> InputExamples`

      - `Boolean Strict`

        When true, guarantees schema validation on tool names and inputs

    - `class BetaToolTextEditor20250124:`

      - `JsonElement Name "str_replace_editor"constant`

        Name of the tool.

        This is how the tool will be called by the model and in `tool_use` blocks.

      - `JsonElement Type "text_editor_20250124"constant`

      - `IReadOnlyList<AllowedCaller> AllowedCallers`

        - `"direct"Direct`

        - `"code_execution_20250825"CodeExecution20250825`

        - `"code_execution_20260120"CodeExecution20260120`

        - `"code_execution_20260521"CodeExecution20260521`

      - `BetaCacheControlEphemeral? CacheControl`

        Create a cache control breakpoint at this content block.

      - `Boolean DeferLoading`

        If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

      - `IReadOnlyList<IReadOnlyDictionary<string, JsonElement>> InputExamples`

      - `Boolean Strict`

        When true, guarantees schema validation on tool names and inputs

    - `class BetaToolTextEditor20250429:`

      - `JsonElement Name "str_replace_based_edit_tool"constant`

        Name of the tool.

        This is how the tool will be called by the model and in `tool_use` blocks.

      - `JsonElement Type "text_editor_20250429"constant`

      - `IReadOnlyList<AllowedCaller> AllowedCallers`

        - `"direct"Direct`

        - `"code_execution_20250825"CodeExecution20250825`

        - `"code_execution_20260120"CodeExecution20260120`

        - `"code_execution_20260521"CodeExecution20260521`

      - `BetaCacheControlEphemeral? CacheControl`

        Create a cache control breakpoint at this content block.

      - `Boolean DeferLoading`

        If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

      - `IReadOnlyList<IReadOnlyDictionary<string, JsonElement>> InputExamples`

      - `Boolean Strict`

        When true, guarantees schema validation on tool names and inputs

    - `class BetaToolTextEditor20250728:`

      - `JsonElement Name "str_replace_based_edit_tool"constant`

        Name of the tool.

        This is how the tool will be called by the model and in `tool_use` blocks.

      - `JsonElement Type "text_editor_20250728"constant`

      - `IReadOnlyList<AllowedCaller> AllowedCallers`

        - `"direct"Direct`

        - `"code_execution_20250825"CodeExecution20250825`

        - `"code_execution_20260120"CodeExecution20260120`

        - `"code_execution_20260521"CodeExecution20260521`

      - `BetaCacheControlEphemeral? CacheControl`

        Create a cache control breakpoint at this content block.

      - `Boolean DeferLoading`

        If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

      - `IReadOnlyList<IReadOnlyDictionary<string, JsonElement>> InputExamples`

      - `Long? MaxCharacters`

        Maximum number of characters to display when viewing a file. If not specified, defaults to displaying the full file.

      - `Boolean Strict`

        When true, guarantees schema validation on tool names and inputs

    - `class BetaWebSearchTool20250305:`

      - `JsonElement Name "web_search"constant`

        Name of the tool.

        This is how the tool will be called by the model and in `tool_use` blocks.

      - `JsonElement Type "web_search_20250305"constant`

      - `IReadOnlyList<AllowedCaller> AllowedCallers`

        - `"direct"Direct`

        - `"code_execution_20250825"CodeExecution20250825`

        - `"code_execution_20260120"CodeExecution20260120`

        - `"code_execution_20260521"CodeExecution20260521`

      - `IReadOnlyList<string>? AllowedDomains`

        If provided, only these domains will be included in results. Cannot be used alongside `blocked_domains`.

      - `IReadOnlyList<string>? BlockedDomains`

        If provided, these domains will never appear in results. Cannot be used alongside `allowed_domains`.

      - `BetaCacheControlEphemeral? CacheControl`

        Create a cache control breakpoint at this content block.

      - `Boolean DeferLoading`

        If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

      - `Long? MaxUses`

        Maximum number of times the tool can be used in the API request.

      - `Boolean Strict`

        When true, guarantees schema validation on tool names and inputs

      - `BetaUserLocation? UserLocation`

        Parameters for the user's location. Used to provide more relevant search results.

        - `JsonElement Type "approximate"constant`

        - `string? City`

          The city of the user.

        - `string? Country`

          The two letter [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) of the user.

        - `string? Region`

          The region of the user.

        - `string? Timezone`

          The [IANA timezone](https://nodatime.org/TimeZones) of the user.

    - `class BetaWebFetchTool20250910:`

      - `JsonElement Name "web_fetch"constant`

        Name of the tool.

        This is how the tool will be called by the model and in `tool_use` blocks.

      - `JsonElement Type "web_fetch_20250910"constant`

      - `IReadOnlyList<AllowedCaller> AllowedCallers`

        - `"direct"Direct`

        - `"code_execution_20250825"CodeExecution20250825`

        - `"code_execution_20260120"CodeExecution20260120`

        - `"code_execution_20260521"CodeExecution20260521`

      - `IReadOnlyList<string>? AllowedDomains`

        List of domains to allow fetching from

      - `IReadOnlyList<string>? BlockedDomains`

        List of domains to block fetching from

      - `BetaCacheControlEphemeral? CacheControl`

        Create a cache control breakpoint at this content block.

      - `BetaCitationsConfigParam? Citations`

        Citations configuration for fetched documents. Citations are disabled by default.

      - `Boolean DeferLoading`

        If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

      - `Long? MaxContentTokens`

        Maximum number of tokens used by including web page text content in the context. The limit is approximate and does not apply to binary content such as PDFs.

      - `Long? MaxUses`

        Maximum number of times the tool can be used in the API request.

      - `Boolean Strict`

        When true, guarantees schema validation on tool names and inputs

    - `class BetaWebSearchTool20260209:`

      - `JsonElement Name "web_search"constant`

        Name of the tool.

        This is how the tool will be called by the model and in `tool_use` blocks.

      - `JsonElement Type "web_search_20260209"constant`

      - `IReadOnlyList<AllowedCaller> AllowedCallers`

        - `"direct"Direct`

        - `"code_execution_20250825"CodeExecution20250825`

        - `"code_execution_20260120"CodeExecution20260120`

        - `"code_execution_20260521"CodeExecution20260521`

      - `IReadOnlyList<string>? AllowedDomains`

        If provided, only these domains will be included in results. Cannot be used alongside `blocked_domains`.

      - `IReadOnlyList<string>? BlockedDomains`

        If provided, these domains will never appear in results. Cannot be used alongside `allowed_domains`.

      - `BetaCacheControlEphemeral? CacheControl`

        Create a cache control breakpoint at this content block.

      - `Boolean DeferLoading`

        If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

      - `Long? MaxUses`

        Maximum number of times the tool can be used in the API request.

      - `Boolean Strict`

        When true, guarantees schema validation on tool names and inputs

      - `BetaUserLocation? UserLocation`

        Parameters for the user's location. Used to provide more relevant search results.

    - `class BetaWebFetchTool20260209:`

      - `JsonElement Name "web_fetch"constant`

        Name of the tool.

        This is how the tool will be called by the model and in `tool_use` blocks.

      - `JsonElement Type "web_fetch_20260209"constant`

      - `IReadOnlyList<AllowedCaller> AllowedCallers`

        - `"direct"Direct`

        - `"code_execution_20250825"CodeExecution20250825`

        - `"code_execution_20260120"CodeExecution20260120`

        - `"code_execution_20260521"CodeExecution20260521`

      - `IReadOnlyList<string>? AllowedDomains`

        List of domains to allow fetching from

      - `IReadOnlyList<string>? BlockedDomains`

        List of domains to block fetching from

      - `BetaCacheControlEphemeral? CacheControl`

        Create a cache control breakpoint at this content block.

      - `BetaCitationsConfigParam? Citations`

        Citations configuration for fetched documents. Citations are disabled by default.

      - `Boolean DeferLoading`

        If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

      - `Long? MaxContentTokens`

        Maximum number of tokens used by including web page text content in the context. The limit is approximate and does not apply to binary content such as PDFs.

      - `Long? MaxUses`

        Maximum number of times the tool can be used in the API request.

      - `Boolean Strict`

        When true, guarantees schema validation on tool names and inputs

    - `class BetaWebFetchTool20260309:`

      Web fetch tool with use_cache parameter for bypassing cached content.

      - `JsonElement Name "web_fetch"constant`

        Name of the tool.

        This is how the tool will be called by the model and in `tool_use` blocks.

      - `JsonElement Type "web_fetch_20260309"constant`

      - `IReadOnlyList<AllowedCaller> AllowedCallers`

        - `"direct"Direct`

        - `"code_execution_20250825"CodeExecution20250825`

        - `"code_execution_20260120"CodeExecution20260120`

        - `"code_execution_20260521"CodeExecution20260521`

      - `IReadOnlyList<string>? AllowedDomains`

        List of domains to allow fetching from

      - `IReadOnlyList<string>? BlockedDomains`

        List of domains to block fetching from

      - `BetaCacheControlEphemeral? CacheControl`

        Create a cache control breakpoint at this content block.

      - `BetaCitationsConfigParam? Citations`

        Citations configuration for fetched documents. Citations are disabled by default.

      - `Boolean DeferLoading`

        If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

      - `Long? MaxContentTokens`

        Maximum number of tokens used by including web page text content in the context. The limit is approximate and does not apply to binary content such as PDFs.

      - `Long? MaxUses`

        Maximum number of times the tool can be used in the API request.

      - `Boolean Strict`

        When true, guarantees schema validation on tool names and inputs

      - `Boolean UseCache`

        Whether to use cached content. Set to false to bypass the cache and fetch fresh content. Only set to false when the user explicitly requests fresh content or when fetching rapidly-changing sources.

    - `class BetaWebSearchTool20260318:`

      - `JsonElement Name "web_search"constant`

        Name of the tool.

        This is how the tool will be called by the model and in `tool_use` blocks.

      - `JsonElement Type "web_search_20260318"constant`

      - `IReadOnlyList<AllowedCaller> AllowedCallers`

        - `"direct"Direct`

        - `"code_execution_20250825"CodeExecution20250825`

        - `"code_execution_20260120"CodeExecution20260120`

        - `"code_execution_20260521"CodeExecution20260521`

      - `IReadOnlyList<string>? AllowedDomains`

        If provided, only these domains will be included in results. Cannot be used alongside `blocked_domains`.

      - `IReadOnlyList<string>? BlockedDomains`

        If provided, these domains will never appear in results. Cannot be used alongside `allowed_domains`.

      - `BetaCacheControlEphemeral? CacheControl`

        Create a cache control breakpoint at this content block.

      - `Boolean DeferLoading`

        If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

      - `Long? MaxUses`

        Maximum number of times the tool can be used in the API request.

      - `ResponseInclusion ResponseInclusion`

        How this tool's result blocks appear in the API response when the result was consumed by a completed code_execution call in the same turn. 'full' returns the complete content (default). 'excluded' drops the nested server_tool_use and result block pair entirely. Results from direct calls, or from code_execution calls that paused before completing, are always returned in full so they can be sent back on the next turn.

        - `"full"Full`

        - `"excluded"Excluded`

      - `Boolean Strict`

        When true, guarantees schema validation on tool names and inputs

      - `BetaUserLocation? UserLocation`

        Parameters for the user's location. Used to provide more relevant search results.

    - `class BetaWebFetchTool20260318:`

      - `JsonElement Name "web_fetch"constant`

        Name of the tool.

        This is how the tool will be called by the model and in `tool_use` blocks.

      - `JsonElement Type "web_fetch_20260318"constant`

      - `IReadOnlyList<AllowedCaller> AllowedCallers`

        - `"direct"Direct`

        - `"code_execution_20250825"CodeExecution20250825`

        - `"code_execution_20260120"CodeExecution20260120`

        - `"code_execution_20260521"CodeExecution20260521`

      - `IReadOnlyList<string>? AllowedDomains`

        List of domains to allow fetching from

      - `IReadOnlyList<string>? BlockedDomains`

        List of domains to block fetching from

      - `BetaCacheControlEphemeral? CacheControl`

        Create a cache control breakpoint at this content block.

      - `BetaCitationsConfigParam? Citations`

        Citations configuration for fetched documents. Citations are disabled by default.

      - `Boolean DeferLoading`

        If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

      - `Long? MaxContentTokens`

        Maximum number of tokens used by including web page text content in the context. The limit is approximate and does not apply to binary content such as PDFs.

      - `Long? MaxUses`

        Maximum number of times the tool can be used in the API request.

      - `ResponseInclusion ResponseInclusion`

        How this tool's result blocks appear in the API response when the result was consumed by a completed code_execution call in the same turn. 'full' returns the complete content (default). 'excluded' drops the nested server_tool_use and result block pair entirely. Results from direct calls, or from code_execution calls that paused before completing, are always returned in full so they can be sent back on the next turn.

        - `"full"Full`

        - `"excluded"Excluded`

      - `Boolean Strict`

        When true, guarantees schema validation on tool names and inputs

      - `Boolean UseCache`

        Whether to use cached content. Set to false to bypass the cache and fetch fresh content. Only set to false when the user explicitly requests fresh content or when fetching rapidly-changing sources.

    - `class BetaAdvisorTool20260301:`

      - `required Model Model`

        The model that will complete your prompt.

        See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

      - `JsonElement Name "advisor"constant`

        Name of the tool.

        This is how the tool will be called by the model and in `tool_use` blocks.

      - `JsonElement Type "advisor_20260301"constant`

      - `IReadOnlyList<AllowedCaller> AllowedCallers`

        - `"direct"Direct`

        - `"code_execution_20250825"CodeExecution20250825`

        - `"code_execution_20260120"CodeExecution20260120`

        - `"code_execution_20260521"CodeExecution20260521`

      - `BetaCacheControlEphemeral? CacheControl`

        Create a cache control breakpoint at this content block.

      - `BetaCacheControlEphemeral? Caching`

        Caching for the advisor's own prompt. When set, each advisor call writes a cache entry at the given TTL so subsequent calls in the same conversation read the stable prefix. When omitted, the advisor prompt is not cached.

      - `Boolean DeferLoading`

        If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

      - `Long? MaxTokens`

        Bounds the advisor's total output (thinking + text) per call. When the advisor hits this cap, the returned advisor_result or advisor_redacted_result block carries stop_reason='max_tokens', and a truncation note is appended to the advice text the worker model sees (inside the encrypted blob in redacted mode). When set, the server also emits a remaining-tokens budget block in the advisor's prompt so the advisor self-shapes toward the cap. When omitted, the advisor model's default output cap applies and no budget block is emitted.

      - `Long? MaxUses`

        Maximum number of times the tool can be used in the API request.

      - `Boolean Strict`

        When true, guarantees schema validation on tool names and inputs

    - `class BetaToolSearchToolBm25_20251119:`

      - `JsonElement Name "tool_search_tool_bm25"constant`

        Name of the tool.

        This is how the tool will be called by the model and in `tool_use` blocks.

      - `required Type Type`

        - `"tool_search_tool_bm25_20251119"ToolSearchToolBm25_20251119`

        - `"tool_search_tool_bm25"ToolSearchToolBm25`

      - `IReadOnlyList<AllowedCaller> AllowedCallers`

        - `"direct"Direct`

        - `"code_execution_20250825"CodeExecution20250825`

        - `"code_execution_20260120"CodeExecution20260120`

        - `"code_execution_20260521"CodeExecution20260521`

      - `BetaCacheControlEphemeral? CacheControl`

        Create a cache control breakpoint at this content block.

      - `Boolean DeferLoading`

        If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

      - `Boolean Strict`

        When true, guarantees schema validation on tool names and inputs

    - `class BetaToolSearchToolRegex20251119:`

      - `JsonElement Name "tool_search_tool_regex"constant`

        Name of the tool.

        This is how the tool will be called by the model and in `tool_use` blocks.

      - `required Type Type`

        - `"tool_search_tool_regex_20251119"ToolSearchToolRegex20251119`

        - `"tool_search_tool_regex"ToolSearchToolRegex`

      - `IReadOnlyList<AllowedCaller> AllowedCallers`

        - `"direct"Direct`

        - `"code_execution_20250825"CodeExecution20250825`

        - `"code_execution_20260120"CodeExecution20260120`

        - `"code_execution_20260521"CodeExecution20260521`

      - `BetaCacheControlEphemeral? CacheControl`

        Create a cache control breakpoint at this content block.

      - `Boolean DeferLoading`

        If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

      - `Boolean Strict`

        When true, guarantees schema validation on tool names and inputs

    - `class BetaMcpToolset:`

      Configuration for a group of tools from an MCP server.

      Allows configuring enabled status and defer_loading for all tools
      from an MCP server, with optional per-tool overrides.

      - `required string McpServerName`

        Name of the MCP server to configure tools for

      - `JsonElement Type "mcp_toolset"constant`

      - `BetaCacheControlEphemeral? CacheControl`

        Create a cache control breakpoint at this content block.

      - `IReadOnlyDictionary<string, BetaMcpToolConfig>? Configs`

        Configuration overrides for specific tools, keyed by tool name

        - `Boolean DeferLoading`

        - `Boolean Enabled`

      - `BetaMcpToolDefaultConfig DefaultConfig`

        Default configuration applied to all tools from this server

        - `Boolean DeferLoading`

        - `Boolean Enabled`

  - `Long topK`

    Body param: Only sample from the top K options for each subsequent token.

    Used to remove "long tail" low probability responses. [Learn more technical details here](https://towardsdatascience.com/how-to-sample-from-language-models-682bceb97277).

    Recommended for advanced use cases only.

  - `Double topP`

    Body param: Use nucleus sampling.

    In nucleus sampling, we compute the cumulative distribution over all the options for each subsequent token in decreasing probability order and cut it off once it reaches a particular probability specified by `top_p`.

    Recommended for advanced use cases only.

  - `IReadOnlyList<AnthropicBeta> betas`

    Header param: Optional header to specify the beta version(s) you want to use.

    - `"message-batches-2024-09-24"MessageBatches2024_09_24`

    - `"prompt-caching-2024-07-31"PromptCaching2024_07_31`

    - `"computer-use-2024-10-22"ComputerUse2024_10_22`

    - `"computer-use-2025-01-24"ComputerUse2025_01_24`

    - `"pdfs-2024-09-25"Pdfs2024_09_25`

    - `"token-counting-2024-11-01"TokenCounting2024_11_01`

    - `"token-efficient-tools-2025-02-19"TokenEfficientTools2025_02_19`

    - `"output-128k-2025-02-19"Output128k2025_02_19`

    - `"files-api-2025-04-14"FilesApi2025_04_14`

    - `"mcp-client-2025-04-04"McpClient2025_04_04`

    - `"mcp-client-2025-11-20"McpClient2025_11_20`

    - `"dev-full-thinking-2025-05-14"DevFullThinking2025_05_14`

    - `"interleaved-thinking-2025-05-14"InterleavedThinking2025_05_14`

    - `"code-execution-2025-05-22"CodeExecution2025_05_22`

    - `"extended-cache-ttl-2025-04-11"ExtendedCacheTtl2025_04_11`

    - `"context-1m-2025-08-07"Context1m2025_08_07`

    - `"context-management-2025-06-27"ContextManagement2025_06_27`

    - `"model-context-window-exceeded-2025-08-26"ModelContextWindowExceeded2025_08_26`

    - `"skills-2025-10-02"Skills2025_10_02`

    - `"fast-mode-2026-02-01"FastMode2026_02_01`

    - `"output-300k-2026-03-24"Output300k2026_03_24`

    - `"user-profiles-2026-03-24"UserProfiles2026_03_24`

    - `"advisor-tool-2026-03-01"AdvisorTool2026_03_01`

    - `"managed-agents-2026-04-01"ManagedAgents2026_04_01`

    - `"cache-diagnosis-2026-04-07"CacheDiagnosis2026_04_07`

    - `"thinking-token-count-2026-05-13"ThinkingTokenCount2026_05_13`

    - `"server-side-fallback-2026-06-01"ServerSideFallback2026_06_01`

    - `"fallback-credit-2026-06-01"FallbackCredit2026_06_01`

  - `string userProfileID`

    Header param: The user profile ID to attribute this request to. Use when acting on behalf of a party other than your organization. Requires the `user-profiles` beta header.

### Returns

- `class BetaMessage:`

  - `required string ID`

    Unique object identifier.

    The format and length of IDs may change over time.

  - `required BetaContainer? Container`

    Information about the container used in the request (for the code execution tool)

    - `required string ID`

      Identifier for the container used in this request

    - `required DateTimeOffset ExpiresAt`

      The time at which the container will expire.

    - `required IReadOnlyList<BetaSkill>? Skills`

      Skills loaded in the container

      - `required string SkillID`

        Skill ID

      - `required Type Type`

        Type of skill - either 'anthropic' (built-in) or 'custom' (user-defined)

        - `"anthropic"Anthropic`

        - `"custom"Custom`

      - `required string Version`

        Skill version or 'latest' for most recent version

  - `required IReadOnlyList<BetaContentBlock> Content`

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

    - `class BetaTextBlock:`

      - `required IReadOnlyList<BetaTextCitation>? Citations`

        Citations supporting the text block.

        The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

        - `class BetaCitationCharLocation:`

          - `required string CitedText`

          - `required Long DocumentIndex`

          - `required string? DocumentTitle`

          - `required Long EndCharIndex`

          - `required string? FileID`

          - `required Long StartCharIndex`

          - `JsonElement Type "char_location"constant`

        - `class BetaCitationPageLocation:`

          - `required string CitedText`

          - `required Long DocumentIndex`

          - `required string? DocumentTitle`

          - `required Long EndPageNumber`

          - `required string? FileID`

          - `required Long StartPageNumber`

          - `JsonElement Type "page_location"constant`

        - `class BetaCitationContentBlockLocation:`

          - `required string CitedText`

            The full text of the cited block range, concatenated.

            Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

          - `required Long DocumentIndex`

          - `required string? DocumentTitle`

          - `required Long EndBlockIndex`

            Exclusive 0-based end index of the cited block range in the source's `content` array.

            Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

          - `required string? FileID`

          - `required Long StartBlockIndex`

            0-based index of the first cited block in the source's `content` array.

          - `JsonElement Type "content_block_location"constant`

        - `class BetaCitationsWebSearchResultLocation:`

          - `required string CitedText`

          - `required string EncryptedIndex`

          - `required string? Title`

          - `JsonElement Type "web_search_result_location"constant`

          - `required string Url`

        - `class BetaCitationSearchResultLocation:`

          - `required string CitedText`

            The full text of the cited block range, concatenated.

            Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

          - `required Long EndBlockIndex`

            Exclusive 0-based end index of the cited block range in the source's `content` array.

            Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

          - `required Long SearchResultIndex`

            0-based index of the cited search result among all `search_result` content blocks in the request, in the order they appear across messages and tool results.

            Counted separately from `document_index`; server-side web search results are not included in this count.

          - `required string Source`

          - `required Long StartBlockIndex`

            0-based index of the first cited block in the source's `content` array.

          - `required string? Title`

          - `JsonElement Type "search_result_location"constant`

      - `required string Text`

      - `JsonElement Type "text"constant`

    - `class BetaThinkingBlock:`

      - `required string Signature`

      - `required string Thinking`

      - `JsonElement Type "thinking"constant`

    - `class BetaRedactedThinkingBlock:`

      - `required string Data`

      - `JsonElement Type "redacted_thinking"constant`

    - `class BetaToolUseBlock:`

      - `required string ID`

      - `required IReadOnlyDictionary<string, JsonElement> Input`

      - `required string Name`

      - `JsonElement Type "tool_use"constant`

      - `Caller Caller`

        Tool invocation directly from the model.

        - `class BetaDirectCaller:`

          Tool invocation directly from the model.

          - `JsonElement Type "direct"constant`

        - `class BetaServerToolCaller:`

          Tool invocation generated by a server-side tool.

          - `required string ToolID`

          - `JsonElement Type "code_execution_20250825"constant`

        - `class BetaServerToolCaller20260120:`

          - `required string ToolID`

          - `JsonElement Type "code_execution_20260120"constant`

    - `class BetaServerToolUseBlock:`

      - `required string ID`

      - `required IReadOnlyDictionary<string, JsonElement> Input`

      - `required Name Name`

        - `"advisor"Advisor`

        - `"web_search"WebSearch`

        - `"web_fetch"WebFetch`

        - `"code_execution"CodeExecution`

        - `"bash_code_execution"BashCodeExecution`

        - `"text_editor_code_execution"TextEditorCodeExecution`

        - `"tool_search_tool_regex"ToolSearchToolRegex`

        - `"tool_search_tool_bm25"ToolSearchToolBm25`

      - `JsonElement Type "server_tool_use"constant`

      - `Caller Caller`

        Tool invocation directly from the model.

        - `class BetaDirectCaller:`

          Tool invocation directly from the model.

        - `class BetaServerToolCaller:`

          Tool invocation generated by a server-side tool.

        - `class BetaServerToolCaller20260120:`

    - `class BetaWebSearchToolResultBlock:`

      - `required BetaWebSearchToolResultBlockContent Content`

        - `class BetaWebSearchToolResultError:`

          - `required BetaWebSearchToolResultErrorCode ErrorCode`

            - `"invalid_tool_input"InvalidToolInput`

            - `"unavailable"Unavailable`

            - `"max_uses_exceeded"MaxUsesExceeded`

            - `"too_many_requests"TooManyRequests`

            - `"query_too_long"QueryTooLong`

            - `"request_too_large"RequestTooLarge`

          - `JsonElement Type "web_search_tool_result_error"constant`

        - `IReadOnlyList<BetaWebSearchResultBlock>`

          - `required string EncryptedContent`

          - `required string? PageAge`

          - `required string Title`

          - `JsonElement Type "web_search_result"constant`

          - `required string Url`

      - `required string ToolUseID`

      - `JsonElement Type "web_search_tool_result"constant`

      - `Caller Caller`

        Tool invocation directly from the model.

        - `class BetaDirectCaller:`

          Tool invocation directly from the model.

        - `class BetaServerToolCaller:`

          Tool invocation generated by a server-side tool.

        - `class BetaServerToolCaller20260120:`

    - `class BetaWebFetchToolResultBlock:`

      - `required Content Content`

        - `class BetaWebFetchToolResultErrorBlock:`

          - `required BetaWebFetchToolResultErrorCode ErrorCode`

            - `"invalid_tool_input"InvalidToolInput`

            - `"url_too_long"UrlTooLong`

            - `"url_not_allowed"UrlNotAllowed`

            - `"url_not_in_prior_context"UrlNotInPriorContext`

            - `"url_not_accessible"UrlNotAccessible`

            - `"unsupported_content_type"UnsupportedContentType`

            - `"too_many_requests"TooManyRequests`

            - `"max_uses_exceeded"MaxUsesExceeded`

            - `"unavailable"Unavailable`

          - `JsonElement Type "web_fetch_tool_result_error"constant`

        - `class BetaWebFetchBlock:`

          - `required BetaDocumentBlock Content`

            - `required BetaCitationConfig? Citations`

              Citation configuration for the document

              - `required Boolean Enabled`

            - `required Source Source`

              - `class BetaBase64PdfSource:`

                - `required string Data`

                - `JsonElement MediaType "application/pdf"constant`

                - `JsonElement Type "base64"constant`

              - `class BetaPlainTextSource:`

                - `required string Data`

                - `JsonElement MediaType "text/plain"constant`

                - `JsonElement Type "text"constant`

            - `required string? Title`

              The title of the document

            - `JsonElement Type "document"constant`

          - `required string? RetrievedAt`

            ISO 8601 timestamp when the content was retrieved

          - `JsonElement Type "web_fetch_result"constant`

          - `required string Url`

            Fetched content URL

      - `required string ToolUseID`

      - `JsonElement Type "web_fetch_tool_result"constant`

      - `Caller Caller`

        Tool invocation directly from the model.

        - `class BetaDirectCaller:`

          Tool invocation directly from the model.

        - `class BetaServerToolCaller:`

          Tool invocation generated by a server-side tool.

        - `class BetaServerToolCaller20260120:`

    - `class BetaAdvisorToolResultBlock:`

      - `required Content Content`

        - `class BetaAdvisorToolResultError:`

          - `required ErrorCode ErrorCode`

            - `"max_uses_exceeded"MaxUsesExceeded`

            - `"prompt_too_long"PromptTooLong`

            - `"too_many_requests"TooManyRequests`

            - `"overloaded"Overloaded`

            - `"unavailable"Unavailable`

            - `"execution_time_exceeded"ExecutionTimeExceeded`

            - `"model_not_found"ModelNotFound`

          - `JsonElement Type "advisor_tool_result_error"constant`

        - `class BetaAdvisorResultBlock:`

          - `required string? StopReason`

            The advisor sub-inference's stop reason (same values as the top-level message `stop_reason`). `max_tokens` indicates the advisor's output was truncated at the tool's `max_tokens` value or the advisor model's policy cap.

          - `required string Text`

          - `JsonElement Type "advisor_result"constant`

        - `class BetaAdvisorRedactedResultBlock:`

          - `required string EncryptedContent`

            Opaque blob containing the advisor's output. Round-trip verbatim; do not inspect or modify.

          - `required string? StopReason`

            The advisor sub-inference's stop reason (same values as the top-level message `stop_reason`).

          - `JsonElement Type "advisor_redacted_result"constant`

      - `required string ToolUseID`

      - `JsonElement Type "advisor_tool_result"constant`

    - `class BetaCodeExecutionToolResultBlock:`

      - `required BetaCodeExecutionToolResultBlockContent Content`

        Code execution result with encrypted stdout for PFC + web_search results.

        - `class BetaCodeExecutionToolResultError:`

          - `required BetaCodeExecutionToolResultErrorCode ErrorCode`

            - `"invalid_tool_input"InvalidToolInput`

            - `"unavailable"Unavailable`

            - `"too_many_requests"TooManyRequests`

            - `"execution_time_exceeded"ExecutionTimeExceeded`

          - `JsonElement Type "code_execution_tool_result_error"constant`

        - `class BetaCodeExecutionResultBlock:`

          - `required IReadOnlyList<BetaCodeExecutionOutputBlock> Content`

            - `required string FileID`

            - `JsonElement Type "code_execution_output"constant`

          - `required Long ReturnCode`

          - `required string Stderr`

          - `required string Stdout`

          - `JsonElement Type "code_execution_result"constant`

        - `class BetaEncryptedCodeExecutionResultBlock:`

          Code execution result with encrypted stdout for PFC + web_search results.

          - `required IReadOnlyList<BetaCodeExecutionOutputBlock> Content`

            - `required string FileID`

            - `JsonElement Type "code_execution_output"constant`

          - `required string EncryptedStdout`

          - `required Long ReturnCode`

          - `required string Stderr`

          - `JsonElement Type "encrypted_code_execution_result"constant`

      - `required string ToolUseID`

      - `JsonElement Type "code_execution_tool_result"constant`

    - `class BetaBashCodeExecutionToolResultBlock:`

      - `required Content Content`

        - `class BetaBashCodeExecutionToolResultError:`

          - `required ErrorCode ErrorCode`

            - `"invalid_tool_input"InvalidToolInput`

            - `"unavailable"Unavailable`

            - `"too_many_requests"TooManyRequests`

            - `"execution_time_exceeded"ExecutionTimeExceeded`

            - `"output_file_too_large"OutputFileTooLarge`

          - `JsonElement Type "bash_code_execution_tool_result_error"constant`

        - `class BetaBashCodeExecutionResultBlock:`

          - `required IReadOnlyList<BetaBashCodeExecutionOutputBlock> Content`

            - `required string FileID`

            - `JsonElement Type "bash_code_execution_output"constant`

          - `required Long ReturnCode`

          - `required string Stderr`

          - `required string Stdout`

          - `JsonElement Type "bash_code_execution_result"constant`

      - `required string ToolUseID`

      - `JsonElement Type "bash_code_execution_tool_result"constant`

    - `class BetaTextEditorCodeExecutionToolResultBlock:`

      - `required Content Content`

        - `class BetaTextEditorCodeExecutionToolResultError:`

          - `required ErrorCode ErrorCode`

            - `"invalid_tool_input"InvalidToolInput`

            - `"unavailable"Unavailable`

            - `"too_many_requests"TooManyRequests`

            - `"execution_time_exceeded"ExecutionTimeExceeded`

            - `"file_not_found"FileNotFound`

          - `required string? ErrorMessage`

          - `JsonElement Type "text_editor_code_execution_tool_result_error"constant`

        - `class BetaTextEditorCodeExecutionViewResultBlock:`

          - `required string Content`

          - `required FileType FileType`

            - `"text"Text`

            - `"image"Image`

            - `"pdf"Pdf`

          - `required Long? NumLines`

          - `required Long? StartLine`

          - `required Long? TotalLines`

          - `JsonElement Type "text_editor_code_execution_view_result"constant`

        - `class BetaTextEditorCodeExecutionCreateResultBlock:`

          - `required Boolean IsFileUpdate`

          - `JsonElement Type "text_editor_code_execution_create_result"constant`

        - `class BetaTextEditorCodeExecutionStrReplaceResultBlock:`

          - `required IReadOnlyList<string>? Lines`

          - `required Long? NewLines`

          - `required Long? NewStart`

          - `required Long? OldLines`

          - `required Long? OldStart`

          - `JsonElement Type "text_editor_code_execution_str_replace_result"constant`

      - `required string ToolUseID`

      - `JsonElement Type "text_editor_code_execution_tool_result"constant`

    - `class BetaToolSearchToolResultBlock:`

      - `required Content Content`

        - `class BetaToolSearchToolResultError:`

          - `required ErrorCode ErrorCode`

            - `"invalid_tool_input"InvalidToolInput`

            - `"unavailable"Unavailable`

            - `"too_many_requests"TooManyRequests`

            - `"execution_time_exceeded"ExecutionTimeExceeded`

          - `required string? ErrorMessage`

          - `JsonElement Type "tool_search_tool_result_error"constant`

        - `class BetaToolSearchToolSearchResultBlock:`

          - `required IReadOnlyList<BetaToolReferenceBlock> ToolReferences`

            - `required string ToolName`

            - `JsonElement Type "tool_reference"constant`

          - `JsonElement Type "tool_search_tool_search_result"constant`

      - `required string ToolUseID`

      - `JsonElement Type "tool_search_tool_result"constant`

    - `class BetaMcpToolUseBlock:`

      - `required string ID`

      - `required IReadOnlyDictionary<string, JsonElement> Input`

      - `required string Name`

        The name of the MCP tool

      - `required string ServerName`

        The name of the MCP server

      - `JsonElement Type "mcp_tool_use"constant`

    - `class BetaMcpToolResultBlock:`

      - `required Content Content`

        - `string`

        - `IReadOnlyList<BetaTextBlock>`

          - `required IReadOnlyList<BetaTextCitation>? Citations`

            Citations supporting the text block.

            The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

          - `required string Text`

          - `JsonElement Type "text"constant`

      - `required Boolean IsError`

      - `required string ToolUseID`

      - `JsonElement Type "mcp_tool_result"constant`

    - `class BetaContainerUploadBlock:`

      Response model for a file uploaded to the container.

      - `required string FileID`

      - `JsonElement Type "container_upload"constant`

    - `class BetaCompactionBlock:`

      A compaction block returned when autocompact is triggered.

      When content is None, it indicates the compaction failed to produce a valid
      summary (e.g., malformed output from the model). Clients may round-trip
      compaction blocks with null content; the server treats them as no-ops.

      - `required string? Content`

        Summary of compacted content, or null if compaction failed

      - `required string? EncryptedContent`

        Opaque metadata from prior compaction, to be round-tripped verbatim

      - `JsonElement Type "compaction"constant`

    - `class BetaFallbackBlock:`

      Marks the point in `content` where one model's output gives way to the next.

      One block appears per hop where a preceding model actually ran this turn and
      declined. A turn where no preceding model ran and declined has no such
      boundary and carries no block — the signal for whether a fallback model
      served the response is the presence of a `fallback_message` entry in
      `usage.iterations`, not this block.

      The block is treated like a server-tool content block for streaming: it
      arrives via the standard `content_block_start` / `content_block_stop`
      pair and carries no deltas.

      - `required BetaFallbackInfo From`

        The model whose output ends at this point — the model that declined at this hop. When the declining hop is the requested model, its `model` echoes the top-level `model` string the caller sent (alias or canonical); when the declining hop is a fallback model, its `model` is that model's canonical id.

        - `required Model Model`

          The model that will complete your prompt.

          See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

          - `"claude-fable-5"ClaudeFable5`

            Next generation of intelligence for the hardest knowledge work and coding problems

          - `"claude-mythos-5"ClaudeMythos5`

            Most capable model for cybersecurity and biology research

          - `"claude-opus-4-8"ClaudeOpus4_8`

            Frontier intelligence for long-running agents and coding

          - `"claude-opus-4-7"ClaudeOpus4_7`

            Frontier intelligence for long-running agents and coding

          - `"claude-mythos-preview"ClaudeMythosPreview`

            New class of intelligence, strongest in coding and cybersecurity

          - `"claude-opus-4-6"ClaudeOpus4_6`

            Frontier intelligence for long-running agents and coding

          - `"claude-sonnet-4-6"ClaudeSonnet4_6`

            Best combination of speed and intelligence

          - `"claude-haiku-4-5"ClaudeHaiku4_5`

            Fastest model with near-frontier intelligence

          - `"claude-haiku-4-5-20251001"ClaudeHaiku4_5_20251001`

            Fastest model with near-frontier intelligence

          - `"claude-opus-4-5"ClaudeOpus4_5`

            Premium model combining maximum intelligence with practical performance

          - `"claude-opus-4-5-20251101"ClaudeOpus4_5_20251101`

            Premium model combining maximum intelligence with practical performance

          - `"claude-sonnet-4-5"ClaudeSonnet4_5`

            High-performance model for agents and coding

          - `"claude-sonnet-4-5-20250929"ClaudeSonnet4_5_20250929`

            High-performance model for agents and coding

          - `"claude-opus-4-1"ClaudeOpus4_1`

            Exceptional model for specialized complex tasks

          - `"claude-opus-4-1-20250805"ClaudeOpus4_1_20250805`

            Exceptional model for specialized complex tasks

      - `required BetaFallbackInfo To`

        The fallback model producing the content that follows this block. Its `model` is always the canonical id.

      - `required BetaFallbackRefusalTrigger Trigger`

        What caused the `from` model to hand over at this hop.

        - `required BetaFallbackRefusalTriggerCategory? Category`

          The policy category that triggered a refusal.

          - `"cyber"Cyber`

          - `"bio"Bio`

          - `"frontier_llm"FrontierLlm`

          - `"reasoning_extraction"ReasoningExtraction`

          - `"military_weapons"MilitaryWeapons`

        - `JsonElement Type "refusal"constant`

      - `JsonElement Type "fallback"constant`

  - `required BetaContextManagementResponse? ContextManagement`

    Context management response.

    Information about context management strategies applied during the request.

    - `required IReadOnlyList<AppliedEdit> AppliedEdits`

      List of context management edits that were applied.

      - `class BetaClearToolUses20250919EditResponse:`

        - `required Long ClearedInputTokens`

          Number of input tokens cleared by this edit.

        - `required Long ClearedToolUses`

          Number of tool uses that were cleared.

        - `JsonElement Type "clear_tool_uses_20250919"constant`

          The type of context management edit applied.

      - `class BetaClearThinking20251015EditResponse:`

        - `required Long ClearedInputTokens`

          Number of input tokens cleared by this edit.

        - `required Long ClearedThinkingTurns`

          Number of thinking turns that were cleared.

        - `JsonElement Type "clear_thinking_20251015"constant`

          The type of context management edit applied.

  - `required BetaDiagnostics? Diagnostics`

    Response envelope for request-level diagnostics. Present (possibly
    null) whenever the caller supplied `diagnostics` on the request.

    - `required CacheMissReason? CacheMissReason`

      Explains why the prompt cache could not fully reuse the prefix from the request identified by `diagnostics.previous_message_id`. `null` means diagnosis is still pending — the response was serialized before the background comparison completed.

      - `class BetaCacheMissModelChanged:`

        - `required Long CacheMissedInputTokens`

          Approximate number of input tokens that would have been read from cache had the prefix matched the previous request.

        - `JsonElement Type "model_changed"constant`

      - `class BetaCacheMissSystemChanged:`

        - `required Long CacheMissedInputTokens`

          Approximate number of input tokens that would have been read from cache had the prefix matched the previous request.

        - `JsonElement Type "system_changed"constant`

      - `class BetaCacheMissToolsChanged:`

        - `required Long CacheMissedInputTokens`

          Approximate number of input tokens that would have been read from cache had the prefix matched the previous request.

        - `JsonElement Type "tools_changed"constant`

      - `class BetaCacheMissMessagesChanged:`

        - `required Long CacheMissedInputTokens`

          Approximate number of input tokens that would have been read from cache had the prefix matched the previous request.

        - `JsonElement Type "messages_changed"constant`

      - `class BetaCacheMissPreviousMessageNotFound:`

        - `JsonElement Type "previous_message_not_found"constant`

      - `class BetaCacheMissUnavailable:`

        - `JsonElement Type "unavailable"constant`

  - `required Model Model`

    The model that will complete your prompt.

    See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

  - `JsonElement Role "assistant"constant`

    Conversational role of the generated message.

    This will always be `"assistant"`.

  - `required BetaRefusalStopDetails? StopDetails`

    Structured information about a refusal.

    - `required Category? Category`

      The policy category that triggered a refusal.

      - `"cyber"Cyber`

      - `"bio"Bio`

      - `"frontier_llm"FrontierLlm`

      - `"reasoning_extraction"ReasoningExtraction`

      - `"military_weapons"MilitaryWeapons`

    - `required string? Explanation`

      Human-readable explanation of the refusal.

      This text is not guaranteed to be stable. `null` when no explanation is available for the category.

    - `required string? FallbackCreditToken`

      Opaque code that refunds the cache-miss cost when retrying this refused
      request on the fallback model. Pass it as `fallback_credit_token` on the
      retry request. Expires 5 minutes after the refusal.

      The retry is sent either with the same request body (`system`, `messages`,
      `tools`, and other render-shaping fields), or with the same body plus one
      appended `assistant` message whose content is the partial text (with any
      trailing whitespace stripped from the final text block) and paired
      server-tool blocks from this refusal — which also authorizes that
      appended turn as an assistant-prefill continuation on models that otherwise
      disallow prefill. A token minted mid-server-tool-loop whose partial content
      was continuable may only be redeemed the second way — if a same-body retry
      is rejected with a 400 saying the token must be redeemed by continuing the
      partial response, retry the second way instead. Either way: same workspace,
      same platform; a mismatch is a 400. Resending a token for an already-warm
      prefix is permitted but yields no additional credit.

      `null` when the refused model isn't eligible for a fallback credit.

    - `required Boolean? FallbackHasPrefillClaim`

      Whether the accompanying `fallback_credit_token` may be redeemed with the
      appended-assistant retry form. Only set when `fallback_credit_token` is
      present.

      `true`: retry by resending the same request body plus one appended
      `assistant` message whose content is this response's `content` with any
      trailing whitespace stripped from the final text block and unpaired
      `tool_use` blocks omitted (the same appended-turn shape described on
      `fallback_credit_token`), with the token attached. `false`: retry by
      resending the original request body unchanged, with the token attached —
      the appended-assistant form is not available for this refusal (no
      continuable partial content, or the request uses `output_format` or a
      `tool_choice` that forces tool use). One exception: when the request used
      `output_format` or a forced `tool_choice` and the refusal arrived after
      server tools (including MCP connector tools) had already executed, the
      token may not be redeemable by either retry form; if the exact-body retry
      is then rejected with a 400 saying the token must be redeemed by
      continuing the partial response, discard the token and retry without it.

      Advisory: if an appended-assistant retry is rejected with a 400 despite
      `true`, fall back to resending the original request body with the token.

    - `required string? RecommendedModel`

      The server's suggested retry target for this refusal. Populated when a fallback attempt could not be made (the fallback model's rate limit was exhausted, or it was overloaded); names the fallback model the caller can retry directly. Null otherwise.

    - `JsonElement Type "refusal"constant`

  - `required BetaStopReason? StopReason`

    The reason that we stopped.

    This may be one the following values:

    * `"end_turn"`: the model reached a natural stopping point
    * `"max_tokens"`: we exceeded the requested `max_tokens` or the model's maximum
    * `"stop_sequence"`: one of your provided custom `stop_sequences` was generated
    * `"tool_use"`: the model invoked one or more tools
    * `"pause_turn"`: we paused a long-running turn. You may provide the response back as-is in a subsequent request to let the model continue.
    * `"refusal"`: when streaming classifiers intervene to handle potential policy violations

    In non-streaming mode this value is always non-null. In streaming mode, it is null in the `message_start` event and non-null otherwise.

    - `"end_turn"EndTurn`

    - `"max_tokens"MaxTokens`

    - `"stop_sequence"StopSequence`

    - `"tool_use"ToolUse`

    - `"pause_turn"PauseTurn`

    - `"compaction"Compaction`

    - `"refusal"Refusal`

    - `"model_context_window_exceeded"ModelContextWindowExceeded`

  - `required string? StopSequence`

    Which custom stop sequence was generated, if any.

    This value will be a non-null string if one of your custom stop sequences was generated.

  - `JsonElement Type "message"constant`

    Object type.

    For Messages, this is always `"message"`.

  - `required BetaUsage Usage`

    Billing and rate-limit usage.

    Anthropic's API bills and rate-limits by token counts, as tokens represent the underlying cost to our systems.

    Under the hood, the API transforms requests into a format suitable for the model. The model's output then goes through a parsing stage before becoming an API response. As a result, the token counts in `usage` will not match one-to-one with the exact visible content of an API request or response.

    For example, `output_tokens` will be non-zero, even for an empty string response from Claude.

    Total input tokens in a request is the summation of `input_tokens`, `cache_creation_input_tokens`, and `cache_read_input_tokens`.

    - `required BetaCacheCreation? CacheCreation`

      Breakdown of cached tokens by TTL

      - `required Long Ephemeral1hInputTokens`

        The number of input tokens used to create the 1 hour cache entry.

      - `required Long Ephemeral5mInputTokens`

        The number of input tokens used to create the 5 minute cache entry.

    - `required Long? CacheCreationInputTokens`

      The number of input tokens used to create the cache entry.

    - `required Long? CacheReadInputTokens`

      The number of input tokens read from the cache.

    - `required string? InferenceGeo`

      The geographic region where inference was performed for this request.

    - `required Long InputTokens`

      The number of input tokens which were used.

    - `required IReadOnlyList<BetaIterationsUsageItems>? Iterations`

      Per-iteration token usage breakdown.

      Each entry represents one sampling iteration, with its own input/output token counts and cache statistics. This allows you to:

      - Determine which iterations exceeded long context thresholds (>=200k tokens)
      - Calculate the true context window size from the last iteration
      - Understand token accumulation across server-side tool use loops

      - `class BetaMessageIterationUsage:`

        Token usage for a sampling iteration.

        - `required BetaCacheCreation? CacheCreation`

          Breakdown of cached tokens by TTL

        - `required Long CacheCreationInputTokens`

          The number of input tokens used to create the cache entry.

        - `required Long CacheReadInputTokens`

          The number of input tokens read from the cache.

        - `required Long InputTokens`

          The number of input tokens which were used.

        - `required Model Model`

          The model that will complete your prompt.

          See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

        - `required Long OutputTokens`

          The number of output tokens which were used.

        - `JsonElement Type "message"constant`

          Usage for a sampling iteration

      - `class BetaCompactionIterationUsage:`

        Token usage for a compaction iteration.

        - `required BetaCacheCreation? CacheCreation`

          Breakdown of cached tokens by TTL

        - `required Long CacheCreationInputTokens`

          The number of input tokens used to create the cache entry.

        - `required Long CacheReadInputTokens`

          The number of input tokens read from the cache.

        - `required Long InputTokens`

          The number of input tokens which were used.

        - `required Long OutputTokens`

          The number of output tokens which were used.

        - `JsonElement Type "compaction"constant`

          Usage for a compaction iteration

      - `class BetaAdvisorMessageIterationUsage:`

        Token usage for an advisor sub-inference iteration.

        - `required BetaCacheCreation? CacheCreation`

          Breakdown of cached tokens by TTL

        - `required Long CacheCreationInputTokens`

          The number of input tokens used to create the cache entry.

        - `required Long CacheReadInputTokens`

          The number of input tokens read from the cache.

        - `required Long InputTokens`

          The number of input tokens which were used.

        - `required Model Model`

          The model that will complete your prompt.

          See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

        - `required Long OutputTokens`

          The number of output tokens which were used.

        - `JsonElement Type "advisor_message"constant`

          Usage for an advisor sub-inference iteration

      - `class BetaFallbackMessageIterationUsage:`

        Token usage for the fallback-model attempt of a server-side fallback request.

        Produced in place of a `message` entry for whichever hop served the
        response. A declined hop produces the existing `message` entry. Whether
        a fallback model served the response is signalled by the presence of this
        entry in `usage.iterations`.

        - `required BetaCacheCreation? CacheCreation`

          Breakdown of cached tokens by TTL

        - `required Long CacheCreationInputTokens`

          The number of input tokens used to create the cache entry.

        - `required Long CacheReadInputTokens`

          The number of input tokens read from the cache.

        - `required Long InputTokens`

          The number of input tokens which were used.

        - `required Model Model`

          The model that will complete your prompt.

          See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

        - `required Long OutputTokens`

          The number of output tokens which were used.

        - `JsonElement Type "fallback_message"constant`

          Usage for the fallback-model attempt that served the response

    - `required Long OutputTokens`

      The number of output tokens which were used.

    - `required BetaOutputTokensDetails? OutputTokensDetails`

      Breakdown of output tokens by category.

      `output_tokens` remains the inclusive, authoritative total used for billing.
      This object provides a read-only decomposition for observability — for example,
      how many of the billed output tokens were spent on internal reasoning that may
      have been summarized before being returned to you.

      - `required Long ThinkingTokens`

        Number of output tokens the model generated as internal reasoning, including
        the thinking-block delimiter tokens.

        Reflects the raw reasoning the model produced, not the (possibly shorter)
        summarized thinking text returned in the response body. Computed by
        re-tokenizing the raw reasoning text, so it may differ from the model's exact
        generation count by a small number of tokens. Always ≤ `output_tokens`;
        `output_tokens - thinking_tokens` approximates the non-reasoning output.

    - `required BetaServerToolUsage? ServerToolUse`

      The number of server tool requests.

      - `required Long WebFetchRequests`

        The number of web fetch tool requests.

      - `required Long WebSearchRequests`

        The number of web search tool requests.

    - `required ServiceTier? ServiceTier`

      If the request used the priority, standard, or batch tier.

      - `"standard"Standard`

      - `"priority"Priority`

      - `"batch"Batch`

    - `required Speed? Speed`

      The inference speed mode used for this request.

      - `"standard"Standard`

      - `"fast"Fast`

### Example

```csharp
MessageCreateParams parameters = new()
{
    MaxTokens = 1024,
    Messages =
    [
        new()
        {
            Content = "Hello, world",
            Role = Role.User,
        },
    ],
    Model = Model.ClaudeOpus4_6,
};

var betaMessage = await client.Beta.Messages.Create(parameters);

Console.WriteLine(betaMessage);
```

#### Response

```json
{
  "id": "msg_013Zva2CMHLNnXjNJJKqJ2EF",
  "container": {
    "id": "id",
    "expires_at": "2019-12-27T18:11:19.117Z",
    "skills": [
      {
        "skill_id": "pdf",
        "type": "anthropic",
        "version": "latest"
      }
    ]
  },
  "content": [
    {
      "citations": [
        {
          "cited_text": "cited_text",
          "document_index": 0,
          "document_title": "document_title",
          "end_char_index": 0,
          "file_id": "file_id",
          "start_char_index": 0,
          "type": "char_location"
        }
      ],
      "text": "Hi! My name is Claude.",
      "type": "text"
    }
  ],
  "context_management": {
    "applied_edits": [
      {
        "cleared_input_tokens": 0,
        "cleared_tool_uses": 0,
        "type": "clear_tool_uses_20250919"
      }
    ]
  },
  "diagnostics": {
    "cache_miss_reason": {
      "cache_missed_input_tokens": 0,
      "type": "model_changed"
    }
  },
  "model": "claude-opus-4-6",
  "role": "assistant",
  "stop_details": {
    "category": "cyber",
    "explanation": "explanation",
    "fallback_credit_token": "fallback_credit_token",
    "fallback_has_prefill_claim": true,
    "recommended_model": "recommended_model",
    "type": "refusal"
  },
  "stop_reason": "end_turn",
  "stop_sequence": null,
  "type": "message",
  "usage": {
    "cache_creation": {
      "ephemeral_1h_input_tokens": 0,
      "ephemeral_5m_input_tokens": 0
    },
    "cache_creation_input_tokens": 2051,
    "cache_read_input_tokens": 2051,
    "inference_geo": "inference_geo",
    "input_tokens": 2095,
    "iterations": [
      {
        "cache_creation": {
          "ephemeral_1h_input_tokens": 0,
          "ephemeral_5m_input_tokens": 0
        },
        "cache_creation_input_tokens": 0,
        "cache_read_input_tokens": 0,
        "input_tokens": 0,
        "model": "claude-fable-5",
        "output_tokens": 0,
        "type": "message"
      }
    ],
    "output_tokens": 503,
    "output_tokens_details": {
      "thinking_tokens": 0
    },
    "server_tool_use": {
      "web_fetch_requests": 2,
      "web_search_requests": 0
    },
    "service_tier": "standard",
    "speed": "standard"
  }
}
```
