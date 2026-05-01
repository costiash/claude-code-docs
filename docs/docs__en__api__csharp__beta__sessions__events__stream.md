## Stream

`BetaManagedAgentsStreamSessionEvents Beta.Sessions.Events.StreamStreaming(EventStreamParamsparameters, CancellationTokencancellationToken = default)`

**get** `/v1/sessions/{session_id}/events/stream`

Stream Events

### Parameters

- `EventStreamParams parameters`

  - `required string sessionID`

    Path parameter session_id

  - `IReadOnlyList<AnthropicBeta> betas`

    Optional header to specify the beta version(s) you want to use.

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

### Returns

- `class BetaManagedAgentsStreamSessionEvents: A class that can be one of several variants.union`

  Server-sent event in the session stream.

  - `class BetaManagedAgentsUserMessageEvent:`

    A user message event in the session conversation.

    - `required string ID`

      Unique identifier for this event.

    - `required IReadOnlyList<Content> Content`

      Array of content blocks comprising the user message.

      - `class BetaManagedAgentsTextBlock:`

        Regular text content.

        - `required string Text`

          The text content.

        - `required Type Type`

          - `"text"Text`

      - `class BetaManagedAgentsImageBlock:`

        Image content specified directly as base64 data or as a reference via a URL.

        - `required Source Source`

          Union type for image source variants.

          - `class BetaManagedAgentsBase64ImageSource:`

            Base64-encoded image data.

            - `required string Data`

              Base64-encoded image data.

            - `required string MediaType`

              MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

            - `required Type Type`

              - `"base64"Base64`

          - `class BetaManagedAgentsUrlImageSource:`

            Image referenced by URL.

            - `required Type Type`

              - `"url"Url`

            - `required string Url`

              URL of the image to fetch.

          - `class BetaManagedAgentsFileImageSource:`

            Image referenced by file ID.

            - `required string FileID`

              ID of a previously uploaded file.

            - `required Type Type`

              - `"file"File`

        - `required Type Type`

          - `"image"Image`

      - `class BetaManagedAgentsDocumentBlock:`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

        - `required Source Source`

          Union type for document source variants.

          - `class BetaManagedAgentsBase64DocumentSource:`

            Base64-encoded document data.

            - `required string Data`

              Base64-encoded document data.

            - `required string MediaType`

              MIME type of the document (e.g., "application/pdf").

            - `required Type Type`

              - `"base64"Base64`

          - `class BetaManagedAgentsPlainTextDocumentSource:`

            Plain text document content.

            - `required string Data`

              The plain text content.

            - `required MediaType MediaType`

              MIME type of the text content. Must be "text/plain".

              - `"text/plain"TextPlain`

            - `required Type Type`

              - `"text"Text`

          - `class BetaManagedAgentsUrlDocumentSource:`

            Document referenced by URL.

            - `required Type Type`

              - `"url"Url`

            - `required string Url`

              URL of the document to fetch.

          - `class BetaManagedAgentsFileDocumentSource:`

            Document referenced by file ID.

            - `required string FileID`

              ID of a previously uploaded file.

            - `required Type Type`

              - `"file"File`

        - `required Type Type`

          - `"document"Document`

        - `string? Context`

          Additional context about the document for the model.

        - `string? Title`

          The title of the document.

    - `required Type Type`

      - `"user.message"UserMessage`

    - `DateTimeOffset? ProcessedAt`

      A timestamp in RFC 3339 format

  - `class BetaManagedAgentsUserInterruptEvent:`

    An interrupt event that pauses agent execution and returns control to the user.

    - `required string ID`

      Unique identifier for this event.

    - `required Type Type`

      - `"user.interrupt"UserInterrupt`

    - `DateTimeOffset? ProcessedAt`

      A timestamp in RFC 3339 format

  - `class BetaManagedAgentsUserToolConfirmationEvent:`

    A tool confirmation event that approves or denies a pending tool execution.

    - `required string ID`

      Unique identifier for this event.

    - `required Result Result`

      UserToolConfirmationResult enum

      - `"allow"Allow`

      - `"deny"Deny`

    - `required string ToolUseID`

      The id of the `agent.tool_use` or `agent.mcp_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

    - `required Type Type`

      - `"user.tool_confirmation"UserToolConfirmation`

    - `string? DenyMessage`

      Optional message providing context for a 'deny' decision. Only allowed when result is 'deny'.

    - `DateTimeOffset? ProcessedAt`

      A timestamp in RFC 3339 format

  - `class BetaManagedAgentsUserCustomToolResultEvent:`

    Event sent by the client providing the result of a custom tool execution.

    - `required string ID`

      Unique identifier for this event.

    - `required string CustomToolUseID`

      The id of the `agent.custom_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

    - `required Type Type`

      - `"user.custom_tool_result"UserCustomToolResult`

    - `IReadOnlyList<Content> Content`

      The result content returned by the tool.

      - `class BetaManagedAgentsTextBlock:`

        Regular text content.

        - `required string Text`

          The text content.

        - `required Type Type`

          - `"text"Text`

      - `class BetaManagedAgentsImageBlock:`

        Image content specified directly as base64 data or as a reference via a URL.

        - `required Source Source`

          Union type for image source variants.

          - `class BetaManagedAgentsBase64ImageSource:`

            Base64-encoded image data.

            - `required string Data`

              Base64-encoded image data.

            - `required string MediaType`

              MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

            - `required Type Type`

              - `"base64"Base64`

          - `class BetaManagedAgentsUrlImageSource:`

            Image referenced by URL.

            - `required Type Type`

              - `"url"Url`

            - `required string Url`

              URL of the image to fetch.

          - `class BetaManagedAgentsFileImageSource:`

            Image referenced by file ID.

            - `required string FileID`

              ID of a previously uploaded file.

            - `required Type Type`

              - `"file"File`

        - `required Type Type`

          - `"image"Image`

      - `class BetaManagedAgentsDocumentBlock:`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

        - `required Source Source`

          Union type for document source variants.

          - `class BetaManagedAgentsBase64DocumentSource:`

            Base64-encoded document data.

            - `required string Data`

              Base64-encoded document data.

            - `required string MediaType`

              MIME type of the document (e.g., "application/pdf").

            - `required Type Type`

              - `"base64"Base64`

          - `class BetaManagedAgentsPlainTextDocumentSource:`

            Plain text document content.

            - `required string Data`

              The plain text content.

            - `required MediaType MediaType`

              MIME type of the text content. Must be "text/plain".

              - `"text/plain"TextPlain`

            - `required Type Type`

              - `"text"Text`

          - `class BetaManagedAgentsUrlDocumentSource:`

            Document referenced by URL.

            - `required Type Type`

              - `"url"Url`

            - `required string Url`

              URL of the document to fetch.

          - `class BetaManagedAgentsFileDocumentSource:`

            Document referenced by file ID.

            - `required string FileID`

              ID of a previously uploaded file.

            - `required Type Type`

              - `"file"File`

        - `required Type Type`

          - `"document"Document`

        - `string? Context`

          Additional context about the document for the model.

        - `string? Title`

          The title of the document.

    - `Boolean? IsError`

      Whether the tool execution resulted in an error.

    - `DateTimeOffset? ProcessedAt`

      A timestamp in RFC 3339 format

  - `class BetaManagedAgentsAgentCustomToolUseEvent:`

    Event emitted when the agent calls a custom tool. The session goes idle until the client sends a `user.custom_tool_result` event with the result.

    - `required string ID`

      Unique identifier for this event.

    - `required IReadOnlyDictionary<string, JsonElement> Input`

      Input parameters for the tool call.

    - `required string Name`

      Name of the custom tool being called.

    - `required DateTimeOffset ProcessedAt`

      A timestamp in RFC 3339 format

    - `required Type Type`

      - `"agent.custom_tool_use"AgentCustomToolUse`

  - `class BetaManagedAgentsAgentMessageEvent:`

    An agent response event in the session conversation.

    - `required string ID`

      Unique identifier for this event.

    - `required IReadOnlyList<BetaManagedAgentsTextBlock> Content`

      Array of text blocks comprising the agent response.

      - `required string Text`

        The text content.

      - `required Type Type`

        - `"text"Text`

    - `required DateTimeOffset ProcessedAt`

      A timestamp in RFC 3339 format

    - `required Type Type`

      - `"agent.message"AgentMessage`

  - `class BetaManagedAgentsAgentThinkingEvent:`

    Indicates the agent is making forward progress via extended thinking. A progress signal, not a content carrier.

    - `required string ID`

      Unique identifier for this event.

    - `required DateTimeOffset ProcessedAt`

      A timestamp in RFC 3339 format

    - `required Type Type`

      - `"agent.thinking"AgentThinking`

  - `class BetaManagedAgentsAgentMcpToolUseEvent:`

    Event emitted when the agent invokes a tool provided by an MCP server.

    - `required string ID`

      Unique identifier for this event.

    - `required IReadOnlyDictionary<string, JsonElement> Input`

      Input parameters for the tool call.

    - `required string McpServerName`

      Name of the MCP server providing the tool.

    - `required string Name`

      Name of the MCP tool being used.

    - `required DateTimeOffset ProcessedAt`

      A timestamp in RFC 3339 format

    - `required Type Type`

      - `"agent.mcp_tool_use"AgentMcpToolUse`

    - `EvaluatedPermission EvaluatedPermission`

      AgentEvaluatedPermission enum

      - `"allow"Allow`

      - `"ask"Ask`

      - `"deny"Deny`

  - `class BetaManagedAgentsAgentMcpToolResultEvent:`

    Event representing the result of an MCP tool execution.

    - `required string ID`

      Unique identifier for this event.

    - `required string McpToolUseID`

      The id of the `agent.mcp_tool_use` event this result corresponds to.

    - `required DateTimeOffset ProcessedAt`

      A timestamp in RFC 3339 format

    - `required Type Type`

      - `"agent.mcp_tool_result"AgentMcpToolResult`

    - `IReadOnlyList<Content> Content`

      The result content returned by the tool.

      - `class BetaManagedAgentsTextBlock:`

        Regular text content.

        - `required string Text`

          The text content.

        - `required Type Type`

          - `"text"Text`

      - `class BetaManagedAgentsImageBlock:`

        Image content specified directly as base64 data or as a reference via a URL.

        - `required Source Source`

          Union type for image source variants.

          - `class BetaManagedAgentsBase64ImageSource:`

            Base64-encoded image data.

            - `required string Data`

              Base64-encoded image data.

            - `required string MediaType`

              MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

            - `required Type Type`

              - `"base64"Base64`

          - `class BetaManagedAgentsUrlImageSource:`

            Image referenced by URL.

            - `required Type Type`

              - `"url"Url`

            - `required string Url`

              URL of the image to fetch.

          - `class BetaManagedAgentsFileImageSource:`

            Image referenced by file ID.

            - `required string FileID`

              ID of a previously uploaded file.

            - `required Type Type`

              - `"file"File`

        - `required Type Type`

          - `"image"Image`

      - `class BetaManagedAgentsDocumentBlock:`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

        - `required Source Source`

          Union type for document source variants.

          - `class BetaManagedAgentsBase64DocumentSource:`

            Base64-encoded document data.

            - `required string Data`

              Base64-encoded document data.

            - `required string MediaType`

              MIME type of the document (e.g., "application/pdf").

            - `required Type Type`

              - `"base64"Base64`

          - `class BetaManagedAgentsPlainTextDocumentSource:`

            Plain text document content.

            - `required string Data`

              The plain text content.

            - `required MediaType MediaType`

              MIME type of the text content. Must be "text/plain".

              - `"text/plain"TextPlain`

            - `required Type Type`

              - `"text"Text`

          - `class BetaManagedAgentsUrlDocumentSource:`

            Document referenced by URL.

            - `required Type Type`

              - `"url"Url`

            - `required string Url`

              URL of the document to fetch.

          - `class BetaManagedAgentsFileDocumentSource:`

            Document referenced by file ID.

            - `required string FileID`

              ID of a previously uploaded file.

            - `required Type Type`

              - `"file"File`

        - `required Type Type`

          - `"document"Document`

        - `string? Context`

          Additional context about the document for the model.

        - `string? Title`

          The title of the document.

    - `Boolean? IsError`

      Whether the tool execution resulted in an error.

  - `class BetaManagedAgentsAgentToolUseEvent:`

    Event emitted when the agent invokes a built-in agent tool.

    - `required string ID`

      Unique identifier for this event.

    - `required IReadOnlyDictionary<string, JsonElement> Input`

      Input parameters for the tool call.

    - `required string Name`

      Name of the agent tool being used.

    - `required DateTimeOffset ProcessedAt`

      A timestamp in RFC 3339 format

    - `required Type Type`

      - `"agent.tool_use"AgentToolUse`

    - `EvaluatedPermission EvaluatedPermission`

      AgentEvaluatedPermission enum

      - `"allow"Allow`

      - `"ask"Ask`

      - `"deny"Deny`

  - `class BetaManagedAgentsAgentToolResultEvent:`

    Event representing the result of an agent tool execution.

    - `required string ID`

      Unique identifier for this event.

    - `required DateTimeOffset ProcessedAt`

      A timestamp in RFC 3339 format

    - `required string ToolUseID`

      The id of the `agent.tool_use` event this result corresponds to.

    - `required Type Type`

      - `"agent.tool_result"AgentToolResult`

    - `IReadOnlyList<Content> Content`

      The result content returned by the tool.

      - `class BetaManagedAgentsTextBlock:`

        Regular text content.

        - `required string Text`

          The text content.

        - `required Type Type`

          - `"text"Text`

      - `class BetaManagedAgentsImageBlock:`

        Image content specified directly as base64 data or as a reference via a URL.

        - `required Source Source`

          Union type for image source variants.

          - `class BetaManagedAgentsBase64ImageSource:`

            Base64-encoded image data.

            - `required string Data`

              Base64-encoded image data.

            - `required string MediaType`

              MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

            - `required Type Type`

              - `"base64"Base64`

          - `class BetaManagedAgentsUrlImageSource:`

            Image referenced by URL.

            - `required Type Type`

              - `"url"Url`

            - `required string Url`

              URL of the image to fetch.

          - `class BetaManagedAgentsFileImageSource:`

            Image referenced by file ID.

            - `required string FileID`

              ID of a previously uploaded file.

            - `required Type Type`

              - `"file"File`

        - `required Type Type`

          - `"image"Image`

      - `class BetaManagedAgentsDocumentBlock:`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

        - `required Source Source`

          Union type for document source variants.

          - `class BetaManagedAgentsBase64DocumentSource:`

            Base64-encoded document data.

            - `required string Data`

              Base64-encoded document data.

            - `required string MediaType`

              MIME type of the document (e.g., "application/pdf").

            - `required Type Type`

              - `"base64"Base64`

          - `class BetaManagedAgentsPlainTextDocumentSource:`

            Plain text document content.

            - `required string Data`

              The plain text content.

            - `required MediaType MediaType`

              MIME type of the text content. Must be "text/plain".

              - `"text/plain"TextPlain`

            - `required Type Type`

              - `"text"Text`

          - `class BetaManagedAgentsUrlDocumentSource:`

            Document referenced by URL.

            - `required Type Type`

              - `"url"Url`

            - `required string Url`

              URL of the document to fetch.

          - `class BetaManagedAgentsFileDocumentSource:`

            Document referenced by file ID.

            - `required string FileID`

              ID of a previously uploaded file.

            - `required Type Type`

              - `"file"File`

        - `required Type Type`

          - `"document"Document`

        - `string? Context`

          Additional context about the document for the model.

        - `string? Title`

          The title of the document.

    - `Boolean? IsError`

      Whether the tool execution resulted in an error.

  - `class BetaManagedAgentsAgentThreadContextCompactedEvent:`

    Indicates that context compaction (summarization) occurred during the session.

    - `required string ID`

      Unique identifier for this event.

    - `required DateTimeOffset ProcessedAt`

      A timestamp in RFC 3339 format

    - `required Type Type`

      - `"agent.thread_context_compacted"AgentThreadContextCompacted`

  - `class BetaManagedAgentsSessionErrorEvent:`

    An error event indicating a problem occurred during session execution.

    - `required string ID`

      Unique identifier for this event.

    - `required Error Error`

      An unknown or unexpected error occurred during session execution. A fallback variant; clients that don't recognize a new error code can match on `retry_status` and `message` alone.

      - `class BetaManagedAgentsUnknownError:`

        An unknown or unexpected error occurred during session execution. A fallback variant; clients that don't recognize a new error code can match on `retry_status` and `message` alone.

        - `required string Message`

          Human-readable error description.

        - `required RetryStatus RetryStatus`

          What the client should do next in response to this error.

          - `class BetaManagedAgentsRetryStatusRetrying:`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

            - `required Type Type`

              - `"retrying"Retrying`

          - `class BetaManagedAgentsRetryStatusExhausted:`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

            - `required Type Type`

              - `"exhausted"Exhausted`

          - `class BetaManagedAgentsRetryStatusTerminal:`

            The session encountered a terminal error and will transition to `terminated` state.

            - `required Type Type`

              - `"terminal"Terminal`

        - `required Type Type`

          - `"unknown_error"UnknownError`

      - `class BetaManagedAgentsModelOverloadedError:`

        The model is currently overloaded. Emitted after automatic retries are exhausted.

        - `required string Message`

          Human-readable error description.

        - `required RetryStatus RetryStatus`

          What the client should do next in response to this error.

          - `class BetaManagedAgentsRetryStatusRetrying:`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

            - `required Type Type`

              - `"retrying"Retrying`

          - `class BetaManagedAgentsRetryStatusExhausted:`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

            - `required Type Type`

              - `"exhausted"Exhausted`

          - `class BetaManagedAgentsRetryStatusTerminal:`

            The session encountered a terminal error and will transition to `terminated` state.

            - `required Type Type`

              - `"terminal"Terminal`

        - `required Type Type`

          - `"model_overloaded_error"ModelOverloadedError`

      - `class BetaManagedAgentsModelRateLimitedError:`

        The model request was rate-limited.

        - `required string Message`

          Human-readable error description.

        - `required RetryStatus RetryStatus`

          What the client should do next in response to this error.

          - `class BetaManagedAgentsRetryStatusRetrying:`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

            - `required Type Type`

              - `"retrying"Retrying`

          - `class BetaManagedAgentsRetryStatusExhausted:`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

            - `required Type Type`

              - `"exhausted"Exhausted`

          - `class BetaManagedAgentsRetryStatusTerminal:`

            The session encountered a terminal error and will transition to `terminated` state.

            - `required Type Type`

              - `"terminal"Terminal`

        - `required Type Type`

          - `"model_rate_limited_error"ModelRateLimitedError`

      - `class BetaManagedAgentsModelRequestFailedError:`

        A model request failed for a reason other than overload or rate-limiting.

        - `required string Message`

          Human-readable error description.

        - `required RetryStatus RetryStatus`

          What the client should do next in response to this error.

          - `class BetaManagedAgentsRetryStatusRetrying:`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

            - `required Type Type`

              - `"retrying"Retrying`

          - `class BetaManagedAgentsRetryStatusExhausted:`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

            - `required Type Type`

              - `"exhausted"Exhausted`

          - `class BetaManagedAgentsRetryStatusTerminal:`

            The session encountered a terminal error and will transition to `terminated` state.

            - `required Type Type`

              - `"terminal"Terminal`

        - `required Type Type`

          - `"model_request_failed_error"ModelRequestFailedError`

      - `class BetaManagedAgentsMcpConnectionFailedError:`

        Failed to connect to an MCP server.

        - `required string McpServerName`

          Name of the MCP server that failed to connect.

        - `required string Message`

          Human-readable error description.

        - `required RetryStatus RetryStatus`

          What the client should do next in response to this error.

          - `class BetaManagedAgentsRetryStatusRetrying:`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

            - `required Type Type`

              - `"retrying"Retrying`

          - `class BetaManagedAgentsRetryStatusExhausted:`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

            - `required Type Type`

              - `"exhausted"Exhausted`

          - `class BetaManagedAgentsRetryStatusTerminal:`

            The session encountered a terminal error and will transition to `terminated` state.

            - `required Type Type`

              - `"terminal"Terminal`

        - `required Type Type`

          - `"mcp_connection_failed_error"McpConnectionFailedError`

      - `class BetaManagedAgentsMcpAuthenticationFailedError:`

        Authentication to an MCP server failed.

        - `required string McpServerName`

          Name of the MCP server that failed authentication.

        - `required string Message`

          Human-readable error description.

        - `required RetryStatus RetryStatus`

          What the client should do next in response to this error.

          - `class BetaManagedAgentsRetryStatusRetrying:`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

            - `required Type Type`

              - `"retrying"Retrying`

          - `class BetaManagedAgentsRetryStatusExhausted:`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

            - `required Type Type`

              - `"exhausted"Exhausted`

          - `class BetaManagedAgentsRetryStatusTerminal:`

            The session encountered a terminal error and will transition to `terminated` state.

            - `required Type Type`

              - `"terminal"Terminal`

        - `required Type Type`

          - `"mcp_authentication_failed_error"McpAuthenticationFailedError`

      - `class BetaManagedAgentsBillingError:`

        The caller's organization or workspace cannot make model requests — out of credits or spend limit reached. Retrying with the same credentials will not succeed; the caller must resolve the billing state.

        - `required string Message`

          Human-readable error description.

        - `required RetryStatus RetryStatus`

          What the client should do next in response to this error.

          - `class BetaManagedAgentsRetryStatusRetrying:`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

            - `required Type Type`

              - `"retrying"Retrying`

          - `class BetaManagedAgentsRetryStatusExhausted:`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

            - `required Type Type`

              - `"exhausted"Exhausted`

          - `class BetaManagedAgentsRetryStatusTerminal:`

            The session encountered a terminal error and will transition to `terminated` state.

            - `required Type Type`

              - `"terminal"Terminal`

        - `required Type Type`

          - `"billing_error"BillingError`

    - `required DateTimeOffset ProcessedAt`

      A timestamp in RFC 3339 format

    - `required Type Type`

      - `"session.error"SessionError`

  - `class BetaManagedAgentsSessionStatusRescheduledEvent:`

    Indicates the session is recovering from an error state and is rescheduled for execution.

    - `required string ID`

      Unique identifier for this event.

    - `required DateTimeOffset ProcessedAt`

      A timestamp in RFC 3339 format

    - `required Type Type`

      - `"session.status_rescheduled"SessionStatusRescheduled`

  - `class BetaManagedAgentsSessionStatusRunningEvent:`

    Indicates the session is actively running and the agent is working.

    - `required string ID`

      Unique identifier for this event.

    - `required DateTimeOffset ProcessedAt`

      A timestamp in RFC 3339 format

    - `required Type Type`

      - `"session.status_running"SessionStatusRunning`

  - `class BetaManagedAgentsSessionStatusIdleEvent:`

    Indicates the agent has paused and is awaiting user input.

    - `required string ID`

      Unique identifier for this event.

    - `required DateTimeOffset ProcessedAt`

      A timestamp in RFC 3339 format

    - `required StopReason StopReason`

      The agent completed its turn naturally and is ready for the next user message.

      - `class BetaManagedAgentsSessionEndTurn:`

        The agent completed its turn naturally and is ready for the next user message.

        - `required Type Type`

          - `"end_turn"EndTurn`

      - `class BetaManagedAgentsSessionRequiresAction:`

        The agent is idle waiting on one or more blocking user-input events (tool confirmation, custom tool result, etc.). Resolving all of them transitions the session back to running.

        - `required IReadOnlyList<string> EventIds`

          The ids of events the agent is blocked on. Resolving fewer than all re-emits `session.status_idle` with the remainder.

        - `required Type Type`

          - `"requires_action"RequiresAction`

      - `class BetaManagedAgentsSessionRetriesExhausted:`

        The turn ended because the retry budget was exhausted (`max_iterations` hit or an error escalated to `retry_status: 'exhausted'`).

        - `required Type Type`

          - `"retries_exhausted"RetriesExhausted`

    - `required Type Type`

      - `"session.status_idle"SessionStatusIdle`

  - `class BetaManagedAgentsSessionStatusTerminatedEvent:`

    Indicates the session has terminated, either due to an error or completion.

    - `required string ID`

      Unique identifier for this event.

    - `required DateTimeOffset ProcessedAt`

      A timestamp in RFC 3339 format

    - `required Type Type`

      - `"session.status_terminated"SessionStatusTerminated`

  - `class BetaManagedAgentsSpanModelRequestStartEvent:`

    Emitted when a model request is initiated by the agent.

    - `required string ID`

      Unique identifier for this event.

    - `required DateTimeOffset ProcessedAt`

      A timestamp in RFC 3339 format

    - `required Type Type`

      - `"span.model_request_start"SpanModelRequestStart`

  - `class BetaManagedAgentsSpanModelRequestEndEvent:`

    Emitted when a model request completes.

    - `required string ID`

      Unique identifier for this event.

    - `required Boolean? IsError`

      Whether the model request resulted in an error.

    - `required string ModelRequestStartID`

      The id of the corresponding `span.model_request_start` event.

    - `required BetaManagedAgentsSpanModelUsage ModelUsage`

      Token usage for a single model request.

      - `required Int CacheCreationInputTokens`

        Tokens used to create prompt cache in this request.

      - `required Int CacheReadInputTokens`

        Tokens read from prompt cache in this request.

      - `required Int InputTokens`

        Input tokens consumed by this request.

      - `required Int OutputTokens`

        Output tokens generated by this request.

      - `Speed? Speed`

        Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

        - `"standard"Standard`

        - `"fast"Fast`

    - `required DateTimeOffset ProcessedAt`

      A timestamp in RFC 3339 format

    - `required Type Type`

      - `"span.model_request_end"SpanModelRequestEnd`

  - `class BetaManagedAgentsSessionDeletedEvent:`

    Emitted when a session has been deleted. Terminates any active event stream — no further events will be emitted for this session.

    - `required string ID`

      Unique identifier for this event.

    - `required DateTimeOffset ProcessedAt`

      A timestamp in RFC 3339 format

    - `required Type Type`

      - `"session.deleted"SessionDeleted`

### Example

```csharp
EventStreamParams parameters = new()
{
    SessionID = "sesn_011CZkZAtmR3yMPDzynEDxu7"
};

await foreach (var betaManagedAgentsStreamSessionEvents in client.Beta.Sessions.Events.StreamStreaming(parameters))
{
    Console.WriteLine(betaManagedAgentsStreamSessionEvents);
}
```
