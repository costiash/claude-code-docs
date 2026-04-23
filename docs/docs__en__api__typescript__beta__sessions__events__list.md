## List

`client.beta.sessions.events.list(stringsessionID, EventListParamsparams?, RequestOptionsoptions?): PageCursor<BetaManagedAgentsSessionEvent>`

**get** `/v1/sessions/{session_id}/events`

List Events

### Parameters

- `sessionID: string`

- `params: EventListParams`

  - `limit?: number`

    Query param: Query parameter for limit

  - `order?: "asc" | "desc"`

    Query param: Sort direction for results, ordered by created_at. Defaults to asc (chronological).

    - `"asc"`

    - `"desc"`

  - `page?: string`

    Query param: Opaque pagination cursor from a previous response's next_page.

  - `betas?: Array<AnthropicBeta>`

    Header param: Optional header to specify the beta version(s) you want to use.

    - `(string & {})`

    - `"message-batches-2024-09-24" | "prompt-caching-2024-07-31" | "computer-use-2024-10-22" | 19 more`

      - `"message-batches-2024-09-24"`

      - `"prompt-caching-2024-07-31"`

      - `"computer-use-2024-10-22"`

      - `"computer-use-2025-01-24"`

      - `"pdfs-2024-09-25"`

      - `"token-counting-2024-11-01"`

      - `"token-efficient-tools-2025-02-19"`

      - `"output-128k-2025-02-19"`

      - `"files-api-2025-04-14"`

      - `"mcp-client-2025-04-04"`

      - `"mcp-client-2025-11-20"`

      - `"dev-full-thinking-2025-05-14"`

      - `"interleaved-thinking-2025-05-14"`

      - `"code-execution-2025-05-22"`

      - `"extended-cache-ttl-2025-04-11"`

      - `"context-1m-2025-08-07"`

      - `"context-management-2025-06-27"`

      - `"model-context-window-exceeded-2025-08-26"`

      - `"skills-2025-10-02"`

      - `"fast-mode-2026-02-01"`

      - `"output-300k-2026-03-24"`

      - `"advisor-tool-2026-03-01"`

### Returns

- `BetaManagedAgentsSessionEvent = BetaManagedAgentsUserMessageEvent | BetaManagedAgentsUserInterruptEvent | BetaManagedAgentsUserToolConfirmationEvent | 17 more`

  Union type for all event types in a session.

  - `BetaManagedAgentsUserMessageEvent`

    A user message event in the session conversation.

    - `id: string`

      Unique identifier for this event.

    - `content: Array<BetaManagedAgentsTextBlock | BetaManagedAgentsImageBlock | BetaManagedAgentsDocumentBlock>`

      Array of content blocks comprising the user message.

      - `BetaManagedAgentsTextBlock`

        Regular text content.

        - `text: string`

          The text content.

        - `type: "text"`

          - `"text"`

      - `BetaManagedAgentsImageBlock`

        Image content specified directly as base64 data or as a reference via a URL.

        - `source: BetaManagedAgentsBase64ImageSource | BetaManagedAgentsURLImageSource | BetaManagedAgentsFileImageSource`

          Union type for image source variants.

          - `BetaManagedAgentsBase64ImageSource`

            Base64-encoded image data.

            - `data: string`

              Base64-encoded image data.

            - `media_type: string`

              MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

            - `type: "base64"`

              - `"base64"`

          - `BetaManagedAgentsURLImageSource`

            Image referenced by URL.

            - `type: "url"`

              - `"url"`

            - `url: string`

              URL of the image to fetch.

          - `BetaManagedAgentsFileImageSource`

            Image referenced by file ID.

            - `file_id: string`

              ID of a previously uploaded file.

            - `type: "file"`

              - `"file"`

        - `type: "image"`

          - `"image"`

      - `BetaManagedAgentsDocumentBlock`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

        - `source: BetaManagedAgentsBase64DocumentSource | BetaManagedAgentsPlainTextDocumentSource | BetaManagedAgentsURLDocumentSource | BetaManagedAgentsFileDocumentSource`

          Union type for document source variants.

          - `BetaManagedAgentsBase64DocumentSource`

            Base64-encoded document data.

            - `data: string`

              Base64-encoded document data.

            - `media_type: string`

              MIME type of the document (e.g., "application/pdf").

            - `type: "base64"`

              - `"base64"`

          - `BetaManagedAgentsPlainTextDocumentSource`

            Plain text document content.

            - `data: string`

              The plain text content.

            - `media_type: "text/plain"`

              MIME type of the text content. Must be "text/plain".

              - `"text/plain"`

            - `type: "text"`

              - `"text"`

          - `BetaManagedAgentsURLDocumentSource`

            Document referenced by URL.

            - `type: "url"`

              - `"url"`

            - `url: string`

              URL of the document to fetch.

          - `BetaManagedAgentsFileDocumentSource`

            Document referenced by file ID.

            - `file_id: string`

              ID of a previously uploaded file.

            - `type: "file"`

              - `"file"`

        - `type: "document"`

          - `"document"`

        - `context?: string | null`

          Additional context about the document for the model.

        - `title?: string | null`

          The title of the document.

    - `type: "user.message"`

      - `"user.message"`

    - `processed_at?: string | null`

      A timestamp in RFC 3339 format

  - `BetaManagedAgentsUserInterruptEvent`

    An interrupt event that pauses agent execution and returns control to the user.

    - `id: string`

      Unique identifier for this event.

    - `type: "user.interrupt"`

      - `"user.interrupt"`

    - `processed_at?: string | null`

      A timestamp in RFC 3339 format

  - `BetaManagedAgentsUserToolConfirmationEvent`

    A tool confirmation event that approves or denies a pending tool execution.

    - `id: string`

      Unique identifier for this event.

    - `result: "allow" | "deny"`

      UserToolConfirmationResult enum

      - `"allow"`

      - `"deny"`

    - `tool_use_id: string`

      The id of the `agent.tool_use` or `agent.mcp_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

    - `type: "user.tool_confirmation"`

      - `"user.tool_confirmation"`

    - `deny_message?: string | null`

      Optional message providing context for a 'deny' decision. Only allowed when result is 'deny'.

    - `processed_at?: string | null`

      A timestamp in RFC 3339 format

  - `BetaManagedAgentsUserCustomToolResultEvent`

    Event sent by the client providing the result of a custom tool execution.

    - `id: string`

      Unique identifier for this event.

    - `custom_tool_use_id: string`

      The id of the `agent.custom_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

    - `type: "user.custom_tool_result"`

      - `"user.custom_tool_result"`

    - `content?: Array<BetaManagedAgentsTextBlock | BetaManagedAgentsImageBlock | BetaManagedAgentsDocumentBlock>`

      The result content returned by the tool.

      - `BetaManagedAgentsTextBlock`

        Regular text content.

        - `text: string`

          The text content.

        - `type: "text"`

          - `"text"`

      - `BetaManagedAgentsImageBlock`

        Image content specified directly as base64 data or as a reference via a URL.

        - `source: BetaManagedAgentsBase64ImageSource | BetaManagedAgentsURLImageSource | BetaManagedAgentsFileImageSource`

          Union type for image source variants.

          - `BetaManagedAgentsBase64ImageSource`

            Base64-encoded image data.

            - `data: string`

              Base64-encoded image data.

            - `media_type: string`

              MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

            - `type: "base64"`

              - `"base64"`

          - `BetaManagedAgentsURLImageSource`

            Image referenced by URL.

            - `type: "url"`

              - `"url"`

            - `url: string`

              URL of the image to fetch.

          - `BetaManagedAgentsFileImageSource`

            Image referenced by file ID.

            - `file_id: string`

              ID of a previously uploaded file.

            - `type: "file"`

              - `"file"`

        - `type: "image"`

          - `"image"`

      - `BetaManagedAgentsDocumentBlock`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

        - `source: BetaManagedAgentsBase64DocumentSource | BetaManagedAgentsPlainTextDocumentSource | BetaManagedAgentsURLDocumentSource | BetaManagedAgentsFileDocumentSource`

          Union type for document source variants.

          - `BetaManagedAgentsBase64DocumentSource`

            Base64-encoded document data.

            - `data: string`

              Base64-encoded document data.

            - `media_type: string`

              MIME type of the document (e.g., "application/pdf").

            - `type: "base64"`

              - `"base64"`

          - `BetaManagedAgentsPlainTextDocumentSource`

            Plain text document content.

            - `data: string`

              The plain text content.

            - `media_type: "text/plain"`

              MIME type of the text content. Must be "text/plain".

              - `"text/plain"`

            - `type: "text"`

              - `"text"`

          - `BetaManagedAgentsURLDocumentSource`

            Document referenced by URL.

            - `type: "url"`

              - `"url"`

            - `url: string`

              URL of the document to fetch.

          - `BetaManagedAgentsFileDocumentSource`

            Document referenced by file ID.

            - `file_id: string`

              ID of a previously uploaded file.

            - `type: "file"`

              - `"file"`

        - `type: "document"`

          - `"document"`

        - `context?: string | null`

          Additional context about the document for the model.

        - `title?: string | null`

          The title of the document.

    - `is_error?: boolean | null`

      Whether the tool execution resulted in an error.

    - `processed_at?: string | null`

      A timestamp in RFC 3339 format

  - `BetaManagedAgentsAgentCustomToolUseEvent`

    Event emitted when the agent calls a custom tool. The session goes idle until the client sends a `user.custom_tool_result` event with the result.

    - `id: string`

      Unique identifier for this event.

    - `input: Record<string, unknown>`

      Input parameters for the tool call.

    - `name: string`

      Name of the custom tool being called.

    - `processed_at: string`

      A timestamp in RFC 3339 format

    - `type: "agent.custom_tool_use"`

      - `"agent.custom_tool_use"`

  - `BetaManagedAgentsAgentMessageEvent`

    An agent response event in the session conversation.

    - `id: string`

      Unique identifier for this event.

    - `content: Array<BetaManagedAgentsTextBlock>`

      Array of text blocks comprising the agent response.

      - `text: string`

        The text content.

      - `type: "text"`

        - `"text"`

    - `processed_at: string`

      A timestamp in RFC 3339 format

    - `type: "agent.message"`

      - `"agent.message"`

  - `BetaManagedAgentsAgentThinkingEvent`

    Indicates the agent is making forward progress via extended thinking. A progress signal, not a content carrier.

    - `id: string`

      Unique identifier for this event.

    - `processed_at: string`

      A timestamp in RFC 3339 format

    - `type: "agent.thinking"`

      - `"agent.thinking"`

  - `BetaManagedAgentsAgentMCPToolUseEvent`

    Event emitted when the agent invokes a tool provided by an MCP server.

    - `id: string`

      Unique identifier for this event.

    - `input: Record<string, unknown>`

      Input parameters for the tool call.

    - `mcp_server_name: string`

      Name of the MCP server providing the tool.

    - `name: string`

      Name of the MCP tool being used.

    - `processed_at: string`

      A timestamp in RFC 3339 format

    - `type: "agent.mcp_tool_use"`

      - `"agent.mcp_tool_use"`

    - `evaluated_permission?: "allow" | "ask" | "deny"`

      AgentEvaluatedPermission enum

      - `"allow"`

      - `"ask"`

      - `"deny"`

  - `BetaManagedAgentsAgentMCPToolResultEvent`

    Event representing the result of an MCP tool execution.

    - `id: string`

      Unique identifier for this event.

    - `mcp_tool_use_id: string`

      The id of the `agent.mcp_tool_use` event this result corresponds to.

    - `processed_at: string`

      A timestamp in RFC 3339 format

    - `type: "agent.mcp_tool_result"`

      - `"agent.mcp_tool_result"`

    - `content?: Array<BetaManagedAgentsTextBlock | BetaManagedAgentsImageBlock | BetaManagedAgentsDocumentBlock>`

      The result content returned by the tool.

      - `BetaManagedAgentsTextBlock`

        Regular text content.

        - `text: string`

          The text content.

        - `type: "text"`

          - `"text"`

      - `BetaManagedAgentsImageBlock`

        Image content specified directly as base64 data or as a reference via a URL.

        - `source: BetaManagedAgentsBase64ImageSource | BetaManagedAgentsURLImageSource | BetaManagedAgentsFileImageSource`

          Union type for image source variants.

          - `BetaManagedAgentsBase64ImageSource`

            Base64-encoded image data.

            - `data: string`

              Base64-encoded image data.

            - `media_type: string`

              MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

            - `type: "base64"`

              - `"base64"`

          - `BetaManagedAgentsURLImageSource`

            Image referenced by URL.

            - `type: "url"`

              - `"url"`

            - `url: string`

              URL of the image to fetch.

          - `BetaManagedAgentsFileImageSource`

            Image referenced by file ID.

            - `file_id: string`

              ID of a previously uploaded file.

            - `type: "file"`

              - `"file"`

        - `type: "image"`

          - `"image"`

      - `BetaManagedAgentsDocumentBlock`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

        - `source: BetaManagedAgentsBase64DocumentSource | BetaManagedAgentsPlainTextDocumentSource | BetaManagedAgentsURLDocumentSource | BetaManagedAgentsFileDocumentSource`

          Union type for document source variants.

          - `BetaManagedAgentsBase64DocumentSource`

            Base64-encoded document data.

            - `data: string`

              Base64-encoded document data.

            - `media_type: string`

              MIME type of the document (e.g., "application/pdf").

            - `type: "base64"`

              - `"base64"`

          - `BetaManagedAgentsPlainTextDocumentSource`

            Plain text document content.

            - `data: string`

              The plain text content.

            - `media_type: "text/plain"`

              MIME type of the text content. Must be "text/plain".

              - `"text/plain"`

            - `type: "text"`

              - `"text"`

          - `BetaManagedAgentsURLDocumentSource`

            Document referenced by URL.

            - `type: "url"`

              - `"url"`

            - `url: string`

              URL of the document to fetch.

          - `BetaManagedAgentsFileDocumentSource`

            Document referenced by file ID.

            - `file_id: string`

              ID of a previously uploaded file.

            - `type: "file"`

              - `"file"`

        - `type: "document"`

          - `"document"`

        - `context?: string | null`

          Additional context about the document for the model.

        - `title?: string | null`

          The title of the document.

    - `is_error?: boolean | null`

      Whether the tool execution resulted in an error.

  - `BetaManagedAgentsAgentToolUseEvent`

    Event emitted when the agent invokes a built-in agent tool.

    - `id: string`

      Unique identifier for this event.

    - `input: Record<string, unknown>`

      Input parameters for the tool call.

    - `name: string`

      Name of the agent tool being used.

    - `processed_at: string`

      A timestamp in RFC 3339 format

    - `type: "agent.tool_use"`

      - `"agent.tool_use"`

    - `evaluated_permission?: "allow" | "ask" | "deny"`

      AgentEvaluatedPermission enum

      - `"allow"`

      - `"ask"`

      - `"deny"`

  - `BetaManagedAgentsAgentToolResultEvent`

    Event representing the result of an agent tool execution.

    - `id: string`

      Unique identifier for this event.

    - `processed_at: string`

      A timestamp in RFC 3339 format

    - `tool_use_id: string`

      The id of the `agent.tool_use` event this result corresponds to.

    - `type: "agent.tool_result"`

      - `"agent.tool_result"`

    - `content?: Array<BetaManagedAgentsTextBlock | BetaManagedAgentsImageBlock | BetaManagedAgentsDocumentBlock>`

      The result content returned by the tool.

      - `BetaManagedAgentsTextBlock`

        Regular text content.

        - `text: string`

          The text content.

        - `type: "text"`

          - `"text"`

      - `BetaManagedAgentsImageBlock`

        Image content specified directly as base64 data or as a reference via a URL.

        - `source: BetaManagedAgentsBase64ImageSource | BetaManagedAgentsURLImageSource | BetaManagedAgentsFileImageSource`

          Union type for image source variants.

          - `BetaManagedAgentsBase64ImageSource`

            Base64-encoded image data.

            - `data: string`

              Base64-encoded image data.

            - `media_type: string`

              MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

            - `type: "base64"`

              - `"base64"`

          - `BetaManagedAgentsURLImageSource`

            Image referenced by URL.

            - `type: "url"`

              - `"url"`

            - `url: string`

              URL of the image to fetch.

          - `BetaManagedAgentsFileImageSource`

            Image referenced by file ID.

            - `file_id: string`

              ID of a previously uploaded file.

            - `type: "file"`

              - `"file"`

        - `type: "image"`

          - `"image"`

      - `BetaManagedAgentsDocumentBlock`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

        - `source: BetaManagedAgentsBase64DocumentSource | BetaManagedAgentsPlainTextDocumentSource | BetaManagedAgentsURLDocumentSource | BetaManagedAgentsFileDocumentSource`

          Union type for document source variants.

          - `BetaManagedAgentsBase64DocumentSource`

            Base64-encoded document data.

            - `data: string`

              Base64-encoded document data.

            - `media_type: string`

              MIME type of the document (e.g., "application/pdf").

            - `type: "base64"`

              - `"base64"`

          - `BetaManagedAgentsPlainTextDocumentSource`

            Plain text document content.

            - `data: string`

              The plain text content.

            - `media_type: "text/plain"`

              MIME type of the text content. Must be "text/plain".

              - `"text/plain"`

            - `type: "text"`

              - `"text"`

          - `BetaManagedAgentsURLDocumentSource`

            Document referenced by URL.

            - `type: "url"`

              - `"url"`

            - `url: string`

              URL of the document to fetch.

          - `BetaManagedAgentsFileDocumentSource`

            Document referenced by file ID.

            - `file_id: string`

              ID of a previously uploaded file.

            - `type: "file"`

              - `"file"`

        - `type: "document"`

          - `"document"`

        - `context?: string | null`

          Additional context about the document for the model.

        - `title?: string | null`

          The title of the document.

    - `is_error?: boolean | null`

      Whether the tool execution resulted in an error.

  - `BetaManagedAgentsAgentThreadContextCompactedEvent`

    Indicates that context compaction (summarization) occurred during the session.

    - `id: string`

      Unique identifier for this event.

    - `processed_at: string`

      A timestamp in RFC 3339 format

    - `type: "agent.thread_context_compacted"`

      - `"agent.thread_context_compacted"`

  - `BetaManagedAgentsSessionErrorEvent`

    An error event indicating a problem occurred during session execution.

    - `id: string`

      Unique identifier for this event.

    - `error: BetaManagedAgentsUnknownError | BetaManagedAgentsModelOverloadedError | BetaManagedAgentsModelRateLimitedError | 4 more`

      An unknown or unexpected error occurred during session execution. A fallback variant; clients that don't recognize a new error code can match on `retry_status` and `message` alone.

      - `BetaManagedAgentsUnknownError`

        An unknown or unexpected error occurred during session execution. A fallback variant; clients that don't recognize a new error code can match on `retry_status` and `message` alone.

        - `message: string`

          Human-readable error description.

        - `retry_status: BetaManagedAgentsRetryStatusRetrying | BetaManagedAgentsRetryStatusExhausted | BetaManagedAgentsRetryStatusTerminal`

          What the client should do next in response to this error.

          - `BetaManagedAgentsRetryStatusRetrying`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

            - `type: "retrying"`

              - `"retrying"`

          - `BetaManagedAgentsRetryStatusExhausted`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

            - `type: "exhausted"`

              - `"exhausted"`

          - `BetaManagedAgentsRetryStatusTerminal`

            The session encountered a terminal error and will transition to `terminated` state.

            - `type: "terminal"`

              - `"terminal"`

        - `type: "unknown_error"`

          - `"unknown_error"`

      - `BetaManagedAgentsModelOverloadedError`

        The model is currently overloaded. Emitted after automatic retries are exhausted.

        - `message: string`

          Human-readable error description.

        - `retry_status: BetaManagedAgentsRetryStatusRetrying | BetaManagedAgentsRetryStatusExhausted | BetaManagedAgentsRetryStatusTerminal`

          What the client should do next in response to this error.

          - `BetaManagedAgentsRetryStatusRetrying`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

            - `type: "retrying"`

              - `"retrying"`

          - `BetaManagedAgentsRetryStatusExhausted`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

            - `type: "exhausted"`

              - `"exhausted"`

          - `BetaManagedAgentsRetryStatusTerminal`

            The session encountered a terminal error and will transition to `terminated` state.

            - `type: "terminal"`

              - `"terminal"`

        - `type: "model_overloaded_error"`

          - `"model_overloaded_error"`

      - `BetaManagedAgentsModelRateLimitedError`

        The model request was rate-limited.

        - `message: string`

          Human-readable error description.

        - `retry_status: BetaManagedAgentsRetryStatusRetrying | BetaManagedAgentsRetryStatusExhausted | BetaManagedAgentsRetryStatusTerminal`

          What the client should do next in response to this error.

          - `BetaManagedAgentsRetryStatusRetrying`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

            - `type: "retrying"`

              - `"retrying"`

          - `BetaManagedAgentsRetryStatusExhausted`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

            - `type: "exhausted"`

              - `"exhausted"`

          - `BetaManagedAgentsRetryStatusTerminal`

            The session encountered a terminal error and will transition to `terminated` state.

            - `type: "terminal"`

              - `"terminal"`

        - `type: "model_rate_limited_error"`

          - `"model_rate_limited_error"`

      - `BetaManagedAgentsModelRequestFailedError`

        A model request failed for a reason other than overload or rate-limiting.

        - `message: string`

          Human-readable error description.

        - `retry_status: BetaManagedAgentsRetryStatusRetrying | BetaManagedAgentsRetryStatusExhausted | BetaManagedAgentsRetryStatusTerminal`

          What the client should do next in response to this error.

          - `BetaManagedAgentsRetryStatusRetrying`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

            - `type: "retrying"`

              - `"retrying"`

          - `BetaManagedAgentsRetryStatusExhausted`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

            - `type: "exhausted"`

              - `"exhausted"`

          - `BetaManagedAgentsRetryStatusTerminal`

            The session encountered a terminal error and will transition to `terminated` state.

            - `type: "terminal"`

              - `"terminal"`

        - `type: "model_request_failed_error"`

          - `"model_request_failed_error"`

      - `BetaManagedAgentsMCPConnectionFailedError`

        Failed to connect to an MCP server.

        - `mcp_server_name: string`

          Name of the MCP server that failed to connect.

        - `message: string`

          Human-readable error description.

        - `retry_status: BetaManagedAgentsRetryStatusRetrying | BetaManagedAgentsRetryStatusExhausted | BetaManagedAgentsRetryStatusTerminal`

          What the client should do next in response to this error.

          - `BetaManagedAgentsRetryStatusRetrying`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

            - `type: "retrying"`

              - `"retrying"`

          - `BetaManagedAgentsRetryStatusExhausted`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

            - `type: "exhausted"`

              - `"exhausted"`

          - `BetaManagedAgentsRetryStatusTerminal`

            The session encountered a terminal error and will transition to `terminated` state.

            - `type: "terminal"`

              - `"terminal"`

        - `type: "mcp_connection_failed_error"`

          - `"mcp_connection_failed_error"`

      - `BetaManagedAgentsMCPAuthenticationFailedError`

        Authentication to an MCP server failed.

        - `mcp_server_name: string`

          Name of the MCP server that failed authentication.

        - `message: string`

          Human-readable error description.

        - `retry_status: BetaManagedAgentsRetryStatusRetrying | BetaManagedAgentsRetryStatusExhausted | BetaManagedAgentsRetryStatusTerminal`

          What the client should do next in response to this error.

          - `BetaManagedAgentsRetryStatusRetrying`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

            - `type: "retrying"`

              - `"retrying"`

          - `BetaManagedAgentsRetryStatusExhausted`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

            - `type: "exhausted"`

              - `"exhausted"`

          - `BetaManagedAgentsRetryStatusTerminal`

            The session encountered a terminal error and will transition to `terminated` state.

            - `type: "terminal"`

              - `"terminal"`

        - `type: "mcp_authentication_failed_error"`

          - `"mcp_authentication_failed_error"`

      - `BetaManagedAgentsBillingError`

        The caller's organization or workspace cannot make model requests — out of credits or spend limit reached. Retrying with the same credentials will not succeed; the caller must resolve the billing state.

        - `message: string`

          Human-readable error description.

        - `retry_status: BetaManagedAgentsRetryStatusRetrying | BetaManagedAgentsRetryStatusExhausted | BetaManagedAgentsRetryStatusTerminal`

          What the client should do next in response to this error.

          - `BetaManagedAgentsRetryStatusRetrying`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

            - `type: "retrying"`

              - `"retrying"`

          - `BetaManagedAgentsRetryStatusExhausted`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

            - `type: "exhausted"`

              - `"exhausted"`

          - `BetaManagedAgentsRetryStatusTerminal`

            The session encountered a terminal error and will transition to `terminated` state.

            - `type: "terminal"`

              - `"terminal"`

        - `type: "billing_error"`

          - `"billing_error"`

    - `processed_at: string`

      A timestamp in RFC 3339 format

    - `type: "session.error"`

      - `"session.error"`

  - `BetaManagedAgentsSessionStatusRescheduledEvent`

    Indicates the session is recovering from an error state and is rescheduled for execution.

    - `id: string`

      Unique identifier for this event.

    - `processed_at: string`

      A timestamp in RFC 3339 format

    - `type: "session.status_rescheduled"`

      - `"session.status_rescheduled"`

  - `BetaManagedAgentsSessionStatusRunningEvent`

    Indicates the session is actively running and the agent is working.

    - `id: string`

      Unique identifier for this event.

    - `processed_at: string`

      A timestamp in RFC 3339 format

    - `type: "session.status_running"`

      - `"session.status_running"`

  - `BetaManagedAgentsSessionStatusIdleEvent`

    Indicates the agent has paused and is awaiting user input.

    - `id: string`

      Unique identifier for this event.

    - `processed_at: string`

      A timestamp in RFC 3339 format

    - `stop_reason: BetaManagedAgentsSessionEndTurn | BetaManagedAgentsSessionRequiresAction | BetaManagedAgentsSessionRetriesExhausted`

      The agent completed its turn naturally and is ready for the next user message.

      - `BetaManagedAgentsSessionEndTurn`

        The agent completed its turn naturally and is ready for the next user message.

        - `type: "end_turn"`

          - `"end_turn"`

      - `BetaManagedAgentsSessionRequiresAction`

        The agent is idle waiting on one or more blocking user-input events (tool confirmation, custom tool result, etc.). Resolving all of them transitions the session back to running.

        - `event_ids: Array<string>`

          The ids of events the agent is blocked on. Resolving fewer than all re-emits `session.status_idle` with the remainder.

        - `type: "requires_action"`

          - `"requires_action"`

      - `BetaManagedAgentsSessionRetriesExhausted`

        The turn ended because the retry budget was exhausted (`max_iterations` hit or an error escalated to `retry_status: 'exhausted'`).

        - `type: "retries_exhausted"`

          - `"retries_exhausted"`

    - `type: "session.status_idle"`

      - `"session.status_idle"`

  - `BetaManagedAgentsSessionStatusTerminatedEvent`

    Indicates the session has terminated, either due to an error or completion.

    - `id: string`

      Unique identifier for this event.

    - `processed_at: string`

      A timestamp in RFC 3339 format

    - `type: "session.status_terminated"`

      - `"session.status_terminated"`

  - `BetaManagedAgentsSpanModelRequestStartEvent`

    Emitted when a model request is initiated by the agent.

    - `id: string`

      Unique identifier for this event.

    - `processed_at: string`

      A timestamp in RFC 3339 format

    - `type: "span.model_request_start"`

      - `"span.model_request_start"`

  - `BetaManagedAgentsSpanModelRequestEndEvent`

    Emitted when a model request completes.

    - `id: string`

      Unique identifier for this event.

    - `is_error: boolean | null`

      Whether the model request resulted in an error.

    - `model_request_start_id: string`

      The id of the corresponding `span.model_request_start` event.

    - `model_usage: BetaManagedAgentsSpanModelUsage`

      Token usage for a single model request.

      - `cache_creation_input_tokens: number`

        Tokens used to create prompt cache in this request.

      - `cache_read_input_tokens: number`

        Tokens read from prompt cache in this request.

      - `input_tokens: number`

        Input tokens consumed by this request.

      - `output_tokens: number`

        Output tokens generated by this request.

      - `speed?: "standard" | "fast" | null`

        Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

        - `"standard"`

        - `"fast"`

    - `processed_at: string`

      A timestamp in RFC 3339 format

    - `type: "span.model_request_end"`

      - `"span.model_request_end"`

  - `BetaManagedAgentsSessionDeletedEvent`

    Emitted when a session has been deleted. Terminates any active event stream — no further events will be emitted for this session.

    - `id: string`

      Unique identifier for this event.

    - `processed_at: string`

      A timestamp in RFC 3339 format

    - `type: "session.deleted"`

      - `"session.deleted"`

### Example

```typescript
import Anthropic from '@anthropic-ai/sdk';

const client = new Anthropic({
  apiKey: process.env['ANTHROPIC_API_KEY'], // This is the default and can be omitted
});

// Automatically fetches more pages as needed.
for await (const betaManagedAgentsSessionEvent of client.beta.sessions.events.list(
  'sesn_011CZkZAtmR3yMPDzynEDxu7',
)) {
  console.log(betaManagedAgentsSessionEvent);
}
```
