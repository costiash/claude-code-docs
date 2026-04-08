# Events

## List

`beta.sessions.events.list(session_id, **kwargs) -> PageCursor<BetaManagedAgentsSessionEvent>`

**get** `/v1/sessions/{session_id}/events`

List Events

### Parameters

- `session_id: String`

- `limit: Integer`

  Query parameter for limit

- `order: :asc | :desc`

  Sort direction for results, ordered by created_at. Defaults to asc (chronological).

  - `:asc`

  - `:desc`

- `page: String`

  Opaque pagination cursor from a previous response's next_page.

- `betas: Array[AnthropicBeta]`

  Optional header to specify the beta version(s) you want to use.

  - `String`

  - `:"message-batches-2024-09-24" | :"prompt-caching-2024-07-31" | :"computer-use-2024-10-22" | 18 more`

    - `:"message-batches-2024-09-24"`

    - `:"prompt-caching-2024-07-31"`

    - `:"computer-use-2024-10-22"`

    - `:"computer-use-2025-01-24"`

    - `:"pdfs-2024-09-25"`

    - `:"token-counting-2024-11-01"`

    - `:"token-efficient-tools-2025-02-19"`

    - `:"output-128k-2025-02-19"`

    - `:"files-api-2025-04-14"`

    - `:"mcp-client-2025-04-04"`

    - `:"mcp-client-2025-11-20"`

    - `:"dev-full-thinking-2025-05-14"`

    - `:"interleaved-thinking-2025-05-14"`

    - `:"code-execution-2025-05-22"`

    - `:"extended-cache-ttl-2025-04-11"`

    - `:"context-1m-2025-08-07"`

    - `:"context-management-2025-06-27"`

    - `:"model-context-window-exceeded-2025-08-26"`

    - `:"skills-2025-10-02"`

    - `:"fast-mode-2026-02-01"`

    - `:"output-300k-2026-03-24"`

### Returns

- `BetaManagedAgentsSessionEvent = BetaManagedAgentsUserMessageEvent | BetaManagedAgentsUserInterruptEvent | BetaManagedAgentsUserToolConfirmationEvent | 17 more`

  Union type for all event types in a session.

  - `class BetaManagedAgentsUserMessageEvent`

    A user message event in the session conversation.

    - `id: String`

      Unique identifier for this event.

    - `content: Array[BetaManagedAgentsTextBlock | BetaManagedAgentsImageBlock | BetaManagedAgentsDocumentBlock]`

      Array of content blocks comprising the user message.

      - `class BetaManagedAgentsTextBlock`

        Regular text content.

        - `text: String`

          The text content.

        - `type: :text`

          - `:text`

      - `class BetaManagedAgentsImageBlock`

        Image content specified directly as base64 data or as a reference via a URL.

        - `source: BetaManagedAgentsBase64ImageSource | BetaManagedAgentsURLImageSource | BetaManagedAgentsFileImageSource`

          Union type for image source variants.

          - `class BetaManagedAgentsBase64ImageSource`

            Base64-encoded image data.

            - `data: String`

              Base64-encoded image data.

            - `media_type: String`

              MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

            - `type: :base64`

              - `:base64`

          - `class BetaManagedAgentsURLImageSource`

            Image referenced by URL.

            - `type: :url`

              - `:url`

            - `url: String`

              URL of the image to fetch.

          - `class BetaManagedAgentsFileImageSource`

            Image referenced by file ID.

            - `file_id: String`

              ID of a previously uploaded file.

            - `type: :file`

              - `:file`

        - `type: :image`

          - `:image`

      - `class BetaManagedAgentsDocumentBlock`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

        - `source: BetaManagedAgentsBase64DocumentSource | BetaManagedAgentsPlainTextDocumentSource | BetaManagedAgentsURLDocumentSource | BetaManagedAgentsFileDocumentSource`

          Union type for document source variants.

          - `class BetaManagedAgentsBase64DocumentSource`

            Base64-encoded document data.

            - `data: String`

              Base64-encoded document data.

            - `media_type: String`

              MIME type of the document (e.g., "application/pdf").

            - `type: :base64`

              - `:base64`

          - `class BetaManagedAgentsPlainTextDocumentSource`

            Plain text document content.

            - `data: String`

              The plain text content.

            - `media_type: :"text/plain"`

              MIME type of the text content. Must be "text/plain".

              - `:"text/plain"`

            - `type: :text`

              - `:text`

          - `class BetaManagedAgentsURLDocumentSource`

            Document referenced by URL.

            - `type: :url`

              - `:url`

            - `url: String`

              URL of the document to fetch.

          - `class BetaManagedAgentsFileDocumentSource`

            Document referenced by file ID.

            - `file_id: String`

              ID of a previously uploaded file.

            - `type: :file`

              - `:file`

        - `type: :document`

          - `:document`

        - `context: String`

          Additional context about the document for the model.

        - `title: String`

          The title of the document.

    - `type: :"user.message"`

      - `:"user.message"`

    - `processed_at: Time`

      A timestamp in RFC 3339 format

  - `class BetaManagedAgentsUserInterruptEvent`

    An interrupt event that pauses agent execution and returns control to the user.

    - `id: String`

      Unique identifier for this event.

    - `type: :"user.interrupt"`

      - `:"user.interrupt"`

    - `processed_at: Time`

      A timestamp in RFC 3339 format

  - `class BetaManagedAgentsUserToolConfirmationEvent`

    A tool confirmation event that approves or denies a pending tool execution.

    - `id: String`

      Unique identifier for this event.

    - `result: :allow | :deny`

      UserToolConfirmationResult enum

      - `:allow`

      - `:deny`

    - `tool_use_id: String`

      The id of the `agent.tool_use` or `agent.mcp_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

    - `type: :"user.tool_confirmation"`

      - `:"user.tool_confirmation"`

    - `deny_message: String`

      Optional message providing context for a 'deny' decision. Only allowed when result is 'deny'.

    - `processed_at: Time`

      A timestamp in RFC 3339 format

  - `class BetaManagedAgentsUserCustomToolResultEvent`

    Event sent by the client providing the result of a custom tool execution.

    - `id: String`

      Unique identifier for this event.

    - `custom_tool_use_id: String`

      The id of the `agent.custom_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

    - `type: :"user.custom_tool_result"`

      - `:"user.custom_tool_result"`

    - `content: Array[BetaManagedAgentsTextBlock | BetaManagedAgentsImageBlock | BetaManagedAgentsDocumentBlock]`

      The result content returned by the tool.

      - `class BetaManagedAgentsTextBlock`

        Regular text content.

        - `text: String`

          The text content.

        - `type: :text`

          - `:text`

      - `class BetaManagedAgentsImageBlock`

        Image content specified directly as base64 data or as a reference via a URL.

        - `source: BetaManagedAgentsBase64ImageSource | BetaManagedAgentsURLImageSource | BetaManagedAgentsFileImageSource`

          Union type for image source variants.

          - `class BetaManagedAgentsBase64ImageSource`

            Base64-encoded image data.

            - `data: String`

              Base64-encoded image data.

            - `media_type: String`

              MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

            - `type: :base64`

              - `:base64`

          - `class BetaManagedAgentsURLImageSource`

            Image referenced by URL.

            - `type: :url`

              - `:url`

            - `url: String`

              URL of the image to fetch.

          - `class BetaManagedAgentsFileImageSource`

            Image referenced by file ID.

            - `file_id: String`

              ID of a previously uploaded file.

            - `type: :file`

              - `:file`

        - `type: :image`

          - `:image`

      - `class BetaManagedAgentsDocumentBlock`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

        - `source: BetaManagedAgentsBase64DocumentSource | BetaManagedAgentsPlainTextDocumentSource | BetaManagedAgentsURLDocumentSource | BetaManagedAgentsFileDocumentSource`

          Union type for document source variants.

          - `class BetaManagedAgentsBase64DocumentSource`

            Base64-encoded document data.

            - `data: String`

              Base64-encoded document data.

            - `media_type: String`

              MIME type of the document (e.g., "application/pdf").

            - `type: :base64`

              - `:base64`

          - `class BetaManagedAgentsPlainTextDocumentSource`

            Plain text document content.

            - `data: String`

              The plain text content.

            - `media_type: :"text/plain"`

              MIME type of the text content. Must be "text/plain".

              - `:"text/plain"`

            - `type: :text`

              - `:text`

          - `class BetaManagedAgentsURLDocumentSource`

            Document referenced by URL.

            - `type: :url`

              - `:url`

            - `url: String`

              URL of the document to fetch.

          - `class BetaManagedAgentsFileDocumentSource`

            Document referenced by file ID.

            - `file_id: String`

              ID of a previously uploaded file.

            - `type: :file`

              - `:file`

        - `type: :document`

          - `:document`

        - `context: String`

          Additional context about the document for the model.

        - `title: String`

          The title of the document.

    - `is_error: bool`

      Whether the tool execution resulted in an error.

    - `processed_at: Time`

      A timestamp in RFC 3339 format

  - `class BetaManagedAgentsAgentCustomToolUseEvent`

    Event emitted when the agent calls a custom tool. The session goes idle until the client sends a `user.custom_tool_result` event with the result.

    - `id: String`

      Unique identifier for this event.

    - `input: Hash[Symbol, untyped]`

      Input parameters for the tool call.

    - `name: String`

      Name of the custom tool being called.

    - `processed_at: Time`

      A timestamp in RFC 3339 format

    - `type: :"agent.custom_tool_use"`

      - `:"agent.custom_tool_use"`

  - `class BetaManagedAgentsAgentMessageEvent`

    An agent response event in the session conversation.

    - `id: String`

      Unique identifier for this event.

    - `content: Array[BetaManagedAgentsTextBlock]`

      Array of text blocks comprising the agent response.

      - `text: String`

        The text content.

      - `type: :text`

        - `:text`

    - `processed_at: Time`

      A timestamp in RFC 3339 format

    - `type: :"agent.message"`

      - `:"agent.message"`

  - `class BetaManagedAgentsAgentThinkingEvent`

    Indicates the agent is making forward progress via extended thinking. A progress signal, not a content carrier.

    - `id: String`

      Unique identifier for this event.

    - `processed_at: Time`

      A timestamp in RFC 3339 format

    - `type: :"agent.thinking"`

      - `:"agent.thinking"`

  - `class BetaManagedAgentsAgentMCPToolUseEvent`

    Event emitted when the agent invokes a tool provided by an MCP server.

    - `id: String`

      Unique identifier for this event.

    - `input: Hash[Symbol, untyped]`

      Input parameters for the tool call.

    - `mcp_server_name: String`

      Name of the MCP server providing the tool.

    - `name: String`

      Name of the MCP tool being used.

    - `processed_at: Time`

      A timestamp in RFC 3339 format

    - `type: :"agent.mcp_tool_use"`

      - `:"agent.mcp_tool_use"`

    - `evaluated_permission: :allow | :ask | :deny`

      AgentEvaluatedPermission enum

      - `:allow`

      - `:ask`

      - `:deny`

  - `class BetaManagedAgentsAgentMCPToolResultEvent`

    Event representing the result of an MCP tool execution.

    - `id: String`

      Unique identifier for this event.

    - `mcp_tool_use_id: String`

      The id of the `agent.mcp_tool_use` event this result corresponds to.

    - `processed_at: Time`

      A timestamp in RFC 3339 format

    - `type: :"agent.mcp_tool_result"`

      - `:"agent.mcp_tool_result"`

    - `content: Array[BetaManagedAgentsTextBlock | BetaManagedAgentsImageBlock | BetaManagedAgentsDocumentBlock]`

      The result content returned by the tool.

      - `class BetaManagedAgentsTextBlock`

        Regular text content.

        - `text: String`

          The text content.

        - `type: :text`

          - `:text`

      - `class BetaManagedAgentsImageBlock`

        Image content specified directly as base64 data or as a reference via a URL.

        - `source: BetaManagedAgentsBase64ImageSource | BetaManagedAgentsURLImageSource | BetaManagedAgentsFileImageSource`

          Union type for image source variants.

          - `class BetaManagedAgentsBase64ImageSource`

            Base64-encoded image data.

            - `data: String`

              Base64-encoded image data.

            - `media_type: String`

              MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

            - `type: :base64`

              - `:base64`

          - `class BetaManagedAgentsURLImageSource`

            Image referenced by URL.

            - `type: :url`

              - `:url`

            - `url: String`

              URL of the image to fetch.

          - `class BetaManagedAgentsFileImageSource`

            Image referenced by file ID.

            - `file_id: String`

              ID of a previously uploaded file.

            - `type: :file`

              - `:file`

        - `type: :image`

          - `:image`

      - `class BetaManagedAgentsDocumentBlock`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

        - `source: BetaManagedAgentsBase64DocumentSource | BetaManagedAgentsPlainTextDocumentSource | BetaManagedAgentsURLDocumentSource | BetaManagedAgentsFileDocumentSource`

          Union type for document source variants.

          - `class BetaManagedAgentsBase64DocumentSource`

            Base64-encoded document data.

            - `data: String`

              Base64-encoded document data.

            - `media_type: String`

              MIME type of the document (e.g., "application/pdf").

            - `type: :base64`

              - `:base64`

          - `class BetaManagedAgentsPlainTextDocumentSource`

            Plain text document content.

            - `data: String`

              The plain text content.

            - `media_type: :"text/plain"`

              MIME type of the text content. Must be "text/plain".

              - `:"text/plain"`

            - `type: :text`

              - `:text`

          - `class BetaManagedAgentsURLDocumentSource`

            Document referenced by URL.

            - `type: :url`

              - `:url`

            - `url: String`

              URL of the document to fetch.

          - `class BetaManagedAgentsFileDocumentSource`

            Document referenced by file ID.

            - `file_id: String`

              ID of a previously uploaded file.

            - `type: :file`

              - `:file`

        - `type: :document`

          - `:document`

        - `context: String`

          Additional context about the document for the model.

        - `title: String`

          The title of the document.

    - `is_error: bool`

      Whether the tool execution resulted in an error.

  - `class BetaManagedAgentsAgentToolUseEvent`

    Event emitted when the agent invokes a built-in agent tool.

    - `id: String`

      Unique identifier for this event.

    - `input: Hash[Symbol, untyped]`

      Input parameters for the tool call.

    - `name: String`

      Name of the agent tool being used.

    - `processed_at: Time`

      A timestamp in RFC 3339 format

    - `type: :"agent.tool_use"`

      - `:"agent.tool_use"`

    - `evaluated_permission: :allow | :ask | :deny`

      AgentEvaluatedPermission enum

      - `:allow`

      - `:ask`

      - `:deny`

  - `class BetaManagedAgentsAgentToolResultEvent`

    Event representing the result of an agent tool execution.

    - `id: String`

      Unique identifier for this event.

    - `processed_at: Time`

      A timestamp in RFC 3339 format

    - `tool_use_id: String`

      The id of the `agent.tool_use` event this result corresponds to.

    - `type: :"agent.tool_result"`

      - `:"agent.tool_result"`

    - `content: Array[BetaManagedAgentsTextBlock | BetaManagedAgentsImageBlock | BetaManagedAgentsDocumentBlock]`

      The result content returned by the tool.

      - `class BetaManagedAgentsTextBlock`

        Regular text content.

        - `text: String`

          The text content.

        - `type: :text`

          - `:text`

      - `class BetaManagedAgentsImageBlock`

        Image content specified directly as base64 data or as a reference via a URL.

        - `source: BetaManagedAgentsBase64ImageSource | BetaManagedAgentsURLImageSource | BetaManagedAgentsFileImageSource`

          Union type for image source variants.

          - `class BetaManagedAgentsBase64ImageSource`

            Base64-encoded image data.

            - `data: String`

              Base64-encoded image data.

            - `media_type: String`

              MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

            - `type: :base64`

              - `:base64`

          - `class BetaManagedAgentsURLImageSource`

            Image referenced by URL.

            - `type: :url`

              - `:url`

            - `url: String`

              URL of the image to fetch.

          - `class BetaManagedAgentsFileImageSource`

            Image referenced by file ID.

            - `file_id: String`

              ID of a previously uploaded file.

            - `type: :file`

              - `:file`

        - `type: :image`

          - `:image`

      - `class BetaManagedAgentsDocumentBlock`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

        - `source: BetaManagedAgentsBase64DocumentSource | BetaManagedAgentsPlainTextDocumentSource | BetaManagedAgentsURLDocumentSource | BetaManagedAgentsFileDocumentSource`

          Union type for document source variants.

          - `class BetaManagedAgentsBase64DocumentSource`

            Base64-encoded document data.

            - `data: String`

              Base64-encoded document data.

            - `media_type: String`

              MIME type of the document (e.g., "application/pdf").

            - `type: :base64`

              - `:base64`

          - `class BetaManagedAgentsPlainTextDocumentSource`

            Plain text document content.

            - `data: String`

              The plain text content.

            - `media_type: :"text/plain"`

              MIME type of the text content. Must be "text/plain".

              - `:"text/plain"`

            - `type: :text`

              - `:text`

          - `class BetaManagedAgentsURLDocumentSource`

            Document referenced by URL.

            - `type: :url`

              - `:url`

            - `url: String`

              URL of the document to fetch.

          - `class BetaManagedAgentsFileDocumentSource`

            Document referenced by file ID.

            - `file_id: String`

              ID of a previously uploaded file.

            - `type: :file`

              - `:file`

        - `type: :document`

          - `:document`

        - `context: String`

          Additional context about the document for the model.

        - `title: String`

          The title of the document.

    - `is_error: bool`

      Whether the tool execution resulted in an error.

  - `class BetaManagedAgentsAgentThreadContextCompactedEvent`

    Indicates that context compaction (summarization) occurred during the session.

    - `id: String`

      Unique identifier for this event.

    - `processed_at: Time`

      A timestamp in RFC 3339 format

    - `type: :"agent.thread_context_compacted"`

      - `:"agent.thread_context_compacted"`

  - `class BetaManagedAgentsSessionErrorEvent`

    An error event indicating a problem occurred during session execution.

    - `id: String`

      Unique identifier for this event.

    - `error: BetaManagedAgentsUnknownError | BetaManagedAgentsModelOverloadedError | BetaManagedAgentsModelRateLimitedError | 4 more`

      An unknown or unexpected error occurred during session execution. A fallback variant; clients that don't recognize a new error code can match on `retry_status` and `message` alone.

      - `class BetaManagedAgentsUnknownError`

        An unknown or unexpected error occurred during session execution. A fallback variant; clients that don't recognize a new error code can match on `retry_status` and `message` alone.

        - `message: String`

          Human-readable error description.

        - `retry_status: BetaManagedAgentsRetryStatusRetrying | BetaManagedAgentsRetryStatusExhausted | BetaManagedAgentsRetryStatusTerminal`

          What the client should do next in response to this error.

          - `class BetaManagedAgentsRetryStatusRetrying`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

            - `type: :retrying`

              - `:retrying`

          - `class BetaManagedAgentsRetryStatusExhausted`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

            - `type: :exhausted`

              - `:exhausted`

          - `class BetaManagedAgentsRetryStatusTerminal`

            The session encountered a terminal error and will transition to `terminated` state.

            - `type: :terminal`

              - `:terminal`

        - `type: :unknown_error`

          - `:unknown_error`

      - `class BetaManagedAgentsModelOverloadedError`

        The model is currently overloaded. Emitted after automatic retries are exhausted.

        - `message: String`

          Human-readable error description.

        - `retry_status: BetaManagedAgentsRetryStatusRetrying | BetaManagedAgentsRetryStatusExhausted | BetaManagedAgentsRetryStatusTerminal`

          What the client should do next in response to this error.

          - `class BetaManagedAgentsRetryStatusRetrying`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

            - `type: :retrying`

              - `:retrying`

          - `class BetaManagedAgentsRetryStatusExhausted`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

            - `type: :exhausted`

              - `:exhausted`

          - `class BetaManagedAgentsRetryStatusTerminal`

            The session encountered a terminal error and will transition to `terminated` state.

            - `type: :terminal`

              - `:terminal`

        - `type: :model_overloaded_error`

          - `:model_overloaded_error`

      - `class BetaManagedAgentsModelRateLimitedError`

        The model request was rate-limited.

        - `message: String`

          Human-readable error description.

        - `retry_status: BetaManagedAgentsRetryStatusRetrying | BetaManagedAgentsRetryStatusExhausted | BetaManagedAgentsRetryStatusTerminal`

          What the client should do next in response to this error.

          - `class BetaManagedAgentsRetryStatusRetrying`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

            - `type: :retrying`

              - `:retrying`

          - `class BetaManagedAgentsRetryStatusExhausted`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

            - `type: :exhausted`

              - `:exhausted`

          - `class BetaManagedAgentsRetryStatusTerminal`

            The session encountered a terminal error and will transition to `terminated` state.

            - `type: :terminal`

              - `:terminal`

        - `type: :model_rate_limited_error`

          - `:model_rate_limited_error`

      - `class BetaManagedAgentsModelRequestFailedError`

        A model request failed for a reason other than overload or rate-limiting.

        - `message: String`

          Human-readable error description.

        - `retry_status: BetaManagedAgentsRetryStatusRetrying | BetaManagedAgentsRetryStatusExhausted | BetaManagedAgentsRetryStatusTerminal`

          What the client should do next in response to this error.

          - `class BetaManagedAgentsRetryStatusRetrying`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

            - `type: :retrying`

              - `:retrying`

          - `class BetaManagedAgentsRetryStatusExhausted`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

            - `type: :exhausted`

              - `:exhausted`

          - `class BetaManagedAgentsRetryStatusTerminal`

            The session encountered a terminal error and will transition to `terminated` state.

            - `type: :terminal`

              - `:terminal`

        - `type: :model_request_failed_error`

          - `:model_request_failed_error`

      - `class BetaManagedAgentsMCPConnectionFailedError`

        Failed to connect to an MCP server.

        - `mcp_server_name: String`

          Name of the MCP server that failed to connect.

        - `message: String`

          Human-readable error description.

        - `retry_status: BetaManagedAgentsRetryStatusRetrying | BetaManagedAgentsRetryStatusExhausted | BetaManagedAgentsRetryStatusTerminal`

          What the client should do next in response to this error.

          - `class BetaManagedAgentsRetryStatusRetrying`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

            - `type: :retrying`

              - `:retrying`

          - `class BetaManagedAgentsRetryStatusExhausted`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

            - `type: :exhausted`

              - `:exhausted`

          - `class BetaManagedAgentsRetryStatusTerminal`

            The session encountered a terminal error and will transition to `terminated` state.

            - `type: :terminal`

              - `:terminal`

        - `type: :mcp_connection_failed_error`

          - `:mcp_connection_failed_error`

      - `class BetaManagedAgentsMCPAuthenticationFailedError`

        Authentication to an MCP server failed.

        - `mcp_server_name: String`

          Name of the MCP server that failed authentication.

        - `message: String`

          Human-readable error description.

        - `retry_status: BetaManagedAgentsRetryStatusRetrying | BetaManagedAgentsRetryStatusExhausted | BetaManagedAgentsRetryStatusTerminal`

          What the client should do next in response to this error.

          - `class BetaManagedAgentsRetryStatusRetrying`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

            - `type: :retrying`

              - `:retrying`

          - `class BetaManagedAgentsRetryStatusExhausted`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

            - `type: :exhausted`

              - `:exhausted`

          - `class BetaManagedAgentsRetryStatusTerminal`

            The session encountered a terminal error and will transition to `terminated` state.

            - `type: :terminal`

              - `:terminal`

        - `type: :mcp_authentication_failed_error`

          - `:mcp_authentication_failed_error`

      - `class BetaManagedAgentsBillingError`

        The caller's organization or workspace cannot make model requests — out of credits or spend limit reached. Retrying with the same credentials will not succeed; the caller must resolve the billing state.

        - `message: String`

          Human-readable error description.

        - `retry_status: BetaManagedAgentsRetryStatusRetrying | BetaManagedAgentsRetryStatusExhausted | BetaManagedAgentsRetryStatusTerminal`

          What the client should do next in response to this error.

          - `class BetaManagedAgentsRetryStatusRetrying`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

            - `type: :retrying`

              - `:retrying`

          - `class BetaManagedAgentsRetryStatusExhausted`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

            - `type: :exhausted`

              - `:exhausted`

          - `class BetaManagedAgentsRetryStatusTerminal`

            The session encountered a terminal error and will transition to `terminated` state.

            - `type: :terminal`

              - `:terminal`

        - `type: :billing_error`

          - `:billing_error`

    - `processed_at: Time`

      A timestamp in RFC 3339 format

    - `type: :"session.error"`

      - `:"session.error"`

  - `class BetaManagedAgentsSessionStatusRescheduledEvent`

    Indicates the session is recovering from an error state and is rescheduled for execution.

    - `id: String`

      Unique identifier for this event.

    - `processed_at: Time`

      A timestamp in RFC 3339 format

    - `type: :"session.status_rescheduled"`

      - `:"session.status_rescheduled"`

  - `class BetaManagedAgentsSessionStatusRunningEvent`

    Indicates the session is actively running and the agent is working.

    - `id: String`

      Unique identifier for this event.

    - `processed_at: Time`

      A timestamp in RFC 3339 format

    - `type: :"session.status_running"`

      - `:"session.status_running"`

  - `class BetaManagedAgentsSessionStatusIdleEvent`

    Indicates the agent has paused and is awaiting user input.

    - `id: String`

      Unique identifier for this event.

    - `processed_at: Time`

      A timestamp in RFC 3339 format

    - `stop_reason: BetaManagedAgentsSessionEndTurn | BetaManagedAgentsSessionRequiresAction | BetaManagedAgentsSessionRetriesExhausted`

      The agent completed its turn naturally and is ready for the next user message.

      - `class BetaManagedAgentsSessionEndTurn`

        The agent completed its turn naturally and is ready for the next user message.

        - `type: :end_turn`

          - `:end_turn`

      - `class BetaManagedAgentsSessionRequiresAction`

        The agent is idle waiting on one or more blocking user-input events (tool confirmation, custom tool result, etc.). Resolving all of them transitions the session back to running.

        - `event_ids: Array[String]`

          The ids of events the agent is blocked on. Resolving fewer than all re-emits `session.status_idle` with the remainder.

        - `type: :requires_action`

          - `:requires_action`

      - `class BetaManagedAgentsSessionRetriesExhausted`

        The turn ended because the retry budget was exhausted (`max_iterations` hit or an error escalated to `retry_status: 'exhausted'`).

        - `type: :retries_exhausted`

          - `:retries_exhausted`

    - `type: :"session.status_idle"`

      - `:"session.status_idle"`

  - `class BetaManagedAgentsSessionStatusTerminatedEvent`

    Indicates the session has terminated, either due to an error or completion.

    - `id: String`

      Unique identifier for this event.

    - `processed_at: Time`

      A timestamp in RFC 3339 format

    - `type: :"session.status_terminated"`

      - `:"session.status_terminated"`

  - `class BetaManagedAgentsSpanModelRequestStartEvent`

    Emitted when a model request is initiated by the agent.

    - `id: String`

      Unique identifier for this event.

    - `processed_at: Time`

      A timestamp in RFC 3339 format

    - `type: :"span.model_request_start"`

      - `:"span.model_request_start"`

  - `class BetaManagedAgentsSpanModelRequestEndEvent`

    Emitted when a model request completes.

    - `id: String`

      Unique identifier for this event.

    - `is_error: bool`

      Whether the model request resulted in an error.

    - `model_request_start_id: String`

      The id of the corresponding `span.model_request_start` event.

    - `model_usage: BetaManagedAgentsSpanModelUsage`

      Token usage for a single model request.

      - `cache_creation_input_tokens: Integer`

        Tokens used to create prompt cache in this request.

      - `cache_read_input_tokens: Integer`

        Tokens read from prompt cache in this request.

      - `input_tokens: Integer`

        Input tokens consumed by this request.

      - `output_tokens: Integer`

        Output tokens generated by this request.

      - `speed: :standard | :fast`

        Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

        - `:standard`

        - `:fast`

    - `processed_at: Time`

      A timestamp in RFC 3339 format

    - `type: :"span.model_request_end"`

      - `:"span.model_request_end"`

  - `class BetaManagedAgentsSessionDeletedEvent`

    Emitted when a session has been deleted. Terminates any active event stream — no further events will be emitted for this session.

    - `id: String`

      Unique identifier for this event.

    - `processed_at: Time`

      A timestamp in RFC 3339 format

    - `type: :"session.deleted"`

      - `:"session.deleted"`

### Example

```ruby
require "anthropic"

anthropic = Anthropic::Client.new(api_key: "my-anthropic-api-key")

page = anthropic.beta.sessions.events.list("sesn_011CZkZAtmR3yMPDzynEDxu7")

puts(page)
```

## Send

`beta.sessions.events.send_(session_id, **kwargs) -> BetaManagedAgentsSendSessionEvents`

**post** `/v1/sessions/{session_id}/events`

Send Events

### Parameters

- `session_id: String`

- `events: Array[BetaManagedAgentsEventParams]`

  Events to send to the `session`.

  - `class BetaManagedAgentsUserMessageEventParams`

    Parameters for sending a user message to the session.

    - `content: Array[BetaManagedAgentsTextBlock | BetaManagedAgentsImageBlock | BetaManagedAgentsDocumentBlock]`

      Array of content blocks for the user message.

      - `class BetaManagedAgentsTextBlock`

        Regular text content.

        - `text: String`

          The text content.

        - `type: :text`

          - `:text`

      - `class BetaManagedAgentsImageBlock`

        Image content specified directly as base64 data or as a reference via a URL.

        - `source: BetaManagedAgentsBase64ImageSource | BetaManagedAgentsURLImageSource | BetaManagedAgentsFileImageSource`

          Union type for image source variants.

          - `class BetaManagedAgentsBase64ImageSource`

            Base64-encoded image data.

            - `data: String`

              Base64-encoded image data.

            - `media_type: String`

              MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

            - `type: :base64`

              - `:base64`

          - `class BetaManagedAgentsURLImageSource`

            Image referenced by URL.

            - `type: :url`

              - `:url`

            - `url: String`

              URL of the image to fetch.

          - `class BetaManagedAgentsFileImageSource`

            Image referenced by file ID.

            - `file_id: String`

              ID of a previously uploaded file.

            - `type: :file`

              - `:file`

        - `type: :image`

          - `:image`

      - `class BetaManagedAgentsDocumentBlock`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

        - `source: BetaManagedAgentsBase64DocumentSource | BetaManagedAgentsPlainTextDocumentSource | BetaManagedAgentsURLDocumentSource | BetaManagedAgentsFileDocumentSource`

          Union type for document source variants.

          - `class BetaManagedAgentsBase64DocumentSource`

            Base64-encoded document data.

            - `data: String`

              Base64-encoded document data.

            - `media_type: String`

              MIME type of the document (e.g., "application/pdf").

            - `type: :base64`

              - `:base64`

          - `class BetaManagedAgentsPlainTextDocumentSource`

            Plain text document content.

            - `data: String`

              The plain text content.

            - `media_type: :"text/plain"`

              MIME type of the text content. Must be "text/plain".

              - `:"text/plain"`

            - `type: :text`

              - `:text`

          - `class BetaManagedAgentsURLDocumentSource`

            Document referenced by URL.

            - `type: :url`

              - `:url`

            - `url: String`

              URL of the document to fetch.

          - `class BetaManagedAgentsFileDocumentSource`

            Document referenced by file ID.

            - `file_id: String`

              ID of a previously uploaded file.

            - `type: :file`

              - `:file`

        - `type: :document`

          - `:document`

        - `context: String`

          Additional context about the document for the model.

        - `title: String`

          The title of the document.

    - `type: :"user.message"`

      - `:"user.message"`

  - `class BetaManagedAgentsUserInterruptEventParams`

    Parameters for sending an interrupt to pause the agent.

    - `type: :"user.interrupt"`

      - `:"user.interrupt"`

  - `class BetaManagedAgentsUserToolConfirmationEventParams`

    Parameters for confirming or denying a tool execution request.

    - `result: :allow | :deny`

      UserToolConfirmationResult enum

      - `:allow`

      - `:deny`

    - `tool_use_id: String`

      The id of the `agent.tool_use` or `agent.mcp_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

    - `type: :"user.tool_confirmation"`

      - `:"user.tool_confirmation"`

    - `deny_message: String`

      Optional message providing context for a 'deny' decision. Only allowed when result is 'deny'.

  - `class BetaManagedAgentsUserCustomToolResultEventParams`

    Parameters for providing the result of a custom tool execution.

    - `custom_tool_use_id: String`

      The id of the `agent.custom_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

    - `type: :"user.custom_tool_result"`

      - `:"user.custom_tool_result"`

    - `content: Array[BetaManagedAgentsTextBlock | BetaManagedAgentsImageBlock | BetaManagedAgentsDocumentBlock]`

      The result content returned by the tool.

      - `class BetaManagedAgentsTextBlock`

        Regular text content.

        - `text: String`

          The text content.

        - `type: :text`

          - `:text`

      - `class BetaManagedAgentsImageBlock`

        Image content specified directly as base64 data or as a reference via a URL.

        - `source: BetaManagedAgentsBase64ImageSource | BetaManagedAgentsURLImageSource | BetaManagedAgentsFileImageSource`

          Union type for image source variants.

          - `class BetaManagedAgentsBase64ImageSource`

            Base64-encoded image data.

            - `data: String`

              Base64-encoded image data.

            - `media_type: String`

              MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

            - `type: :base64`

              - `:base64`

          - `class BetaManagedAgentsURLImageSource`

            Image referenced by URL.

            - `type: :url`

              - `:url`

            - `url: String`

              URL of the image to fetch.

          - `class BetaManagedAgentsFileImageSource`

            Image referenced by file ID.

            - `file_id: String`

              ID of a previously uploaded file.

            - `type: :file`

              - `:file`

        - `type: :image`

          - `:image`

      - `class BetaManagedAgentsDocumentBlock`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

        - `source: BetaManagedAgentsBase64DocumentSource | BetaManagedAgentsPlainTextDocumentSource | BetaManagedAgentsURLDocumentSource | BetaManagedAgentsFileDocumentSource`

          Union type for document source variants.

          - `class BetaManagedAgentsBase64DocumentSource`

            Base64-encoded document data.

            - `data: String`

              Base64-encoded document data.

            - `media_type: String`

              MIME type of the document (e.g., "application/pdf").

            - `type: :base64`

              - `:base64`

          - `class BetaManagedAgentsPlainTextDocumentSource`

            Plain text document content.

            - `data: String`

              The plain text content.

            - `media_type: :"text/plain"`

              MIME type of the text content. Must be "text/plain".

              - `:"text/plain"`

            - `type: :text`

              - `:text`

          - `class BetaManagedAgentsURLDocumentSource`

            Document referenced by URL.

            - `type: :url`

              - `:url`

            - `url: String`

              URL of the document to fetch.

          - `class BetaManagedAgentsFileDocumentSource`

            Document referenced by file ID.

            - `file_id: String`

              ID of a previously uploaded file.

            - `type: :file`

              - `:file`

        - `type: :document`

          - `:document`

        - `context: String`

          Additional context about the document for the model.

        - `title: String`

          The title of the document.

    - `is_error: bool`

      Whether the tool execution resulted in an error.

- `betas: Array[AnthropicBeta]`

  Optional header to specify the beta version(s) you want to use.

  - `String`

  - `:"message-batches-2024-09-24" | :"prompt-caching-2024-07-31" | :"computer-use-2024-10-22" | 18 more`

    - `:"message-batches-2024-09-24"`

    - `:"prompt-caching-2024-07-31"`

    - `:"computer-use-2024-10-22"`

    - `:"computer-use-2025-01-24"`

    - `:"pdfs-2024-09-25"`

    - `:"token-counting-2024-11-01"`

    - `:"token-efficient-tools-2025-02-19"`

    - `:"output-128k-2025-02-19"`

    - `:"files-api-2025-04-14"`

    - `:"mcp-client-2025-04-04"`

    - `:"mcp-client-2025-11-20"`

    - `:"dev-full-thinking-2025-05-14"`

    - `:"interleaved-thinking-2025-05-14"`

    - `:"code-execution-2025-05-22"`

    - `:"extended-cache-ttl-2025-04-11"`

    - `:"context-1m-2025-08-07"`

    - `:"context-management-2025-06-27"`

    - `:"model-context-window-exceeded-2025-08-26"`

    - `:"skills-2025-10-02"`

    - `:"fast-mode-2026-02-01"`

    - `:"output-300k-2026-03-24"`

### Returns

- `class BetaManagedAgentsSendSessionEvents`

  Events that were successfully sent to the session.

  - `data: Array[BetaManagedAgentsUserMessageEvent | BetaManagedAgentsUserInterruptEvent | BetaManagedAgentsUserToolConfirmationEvent | BetaManagedAgentsUserCustomToolResultEvent]`

    Sent events

    - `class BetaManagedAgentsUserMessageEvent`

      A user message event in the session conversation.

      - `id: String`

        Unique identifier for this event.

      - `content: Array[BetaManagedAgentsTextBlock | BetaManagedAgentsImageBlock | BetaManagedAgentsDocumentBlock]`

        Array of content blocks comprising the user message.

        - `class BetaManagedAgentsTextBlock`

          Regular text content.

          - `text: String`

            The text content.

          - `type: :text`

            - `:text`

        - `class BetaManagedAgentsImageBlock`

          Image content specified directly as base64 data or as a reference via a URL.

          - `source: BetaManagedAgentsBase64ImageSource | BetaManagedAgentsURLImageSource | BetaManagedAgentsFileImageSource`

            Union type for image source variants.

            - `class BetaManagedAgentsBase64ImageSource`

              Base64-encoded image data.

              - `data: String`

                Base64-encoded image data.

              - `media_type: String`

                MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

              - `type: :base64`

                - `:base64`

            - `class BetaManagedAgentsURLImageSource`

              Image referenced by URL.

              - `type: :url`

                - `:url`

              - `url: String`

                URL of the image to fetch.

            - `class BetaManagedAgentsFileImageSource`

              Image referenced by file ID.

              - `file_id: String`

                ID of a previously uploaded file.

              - `type: :file`

                - `:file`

          - `type: :image`

            - `:image`

        - `class BetaManagedAgentsDocumentBlock`

          Document content, either specified directly as base64 data, as text, or as a reference via a URL.

          - `source: BetaManagedAgentsBase64DocumentSource | BetaManagedAgentsPlainTextDocumentSource | BetaManagedAgentsURLDocumentSource | BetaManagedAgentsFileDocumentSource`

            Union type for document source variants.

            - `class BetaManagedAgentsBase64DocumentSource`

              Base64-encoded document data.

              - `data: String`

                Base64-encoded document data.

              - `media_type: String`

                MIME type of the document (e.g., "application/pdf").

              - `type: :base64`

                - `:base64`

            - `class BetaManagedAgentsPlainTextDocumentSource`

              Plain text document content.

              - `data: String`

                The plain text content.

              - `media_type: :"text/plain"`

                MIME type of the text content. Must be "text/plain".

                - `:"text/plain"`

              - `type: :text`

                - `:text`

            - `class BetaManagedAgentsURLDocumentSource`

              Document referenced by URL.

              - `type: :url`

                - `:url`

              - `url: String`

                URL of the document to fetch.

            - `class BetaManagedAgentsFileDocumentSource`

              Document referenced by file ID.

              - `file_id: String`

                ID of a previously uploaded file.

              - `type: :file`

                - `:file`

          - `type: :document`

            - `:document`

          - `context: String`

            Additional context about the document for the model.

          - `title: String`

            The title of the document.

      - `type: :"user.message"`

        - `:"user.message"`

      - `processed_at: Time`

        A timestamp in RFC 3339 format

    - `class BetaManagedAgentsUserInterruptEvent`

      An interrupt event that pauses agent execution and returns control to the user.

      - `id: String`

        Unique identifier for this event.

      - `type: :"user.interrupt"`

        - `:"user.interrupt"`

      - `processed_at: Time`

        A timestamp in RFC 3339 format

    - `class BetaManagedAgentsUserToolConfirmationEvent`

      A tool confirmation event that approves or denies a pending tool execution.

      - `id: String`

        Unique identifier for this event.

      - `result: :allow | :deny`

        UserToolConfirmationResult enum

        - `:allow`

        - `:deny`

      - `tool_use_id: String`

        The id of the `agent.tool_use` or `agent.mcp_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

      - `type: :"user.tool_confirmation"`

        - `:"user.tool_confirmation"`

      - `deny_message: String`

        Optional message providing context for a 'deny' decision. Only allowed when result is 'deny'.

      - `processed_at: Time`

        A timestamp in RFC 3339 format

    - `class BetaManagedAgentsUserCustomToolResultEvent`

      Event sent by the client providing the result of a custom tool execution.

      - `id: String`

        Unique identifier for this event.

      - `custom_tool_use_id: String`

        The id of the `agent.custom_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

      - `type: :"user.custom_tool_result"`

        - `:"user.custom_tool_result"`

      - `content: Array[BetaManagedAgentsTextBlock | BetaManagedAgentsImageBlock | BetaManagedAgentsDocumentBlock]`

        The result content returned by the tool.

        - `class BetaManagedAgentsTextBlock`

          Regular text content.

          - `text: String`

            The text content.

          - `type: :text`

            - `:text`

        - `class BetaManagedAgentsImageBlock`

          Image content specified directly as base64 data or as a reference via a URL.

          - `source: BetaManagedAgentsBase64ImageSource | BetaManagedAgentsURLImageSource | BetaManagedAgentsFileImageSource`

            Union type for image source variants.

            - `class BetaManagedAgentsBase64ImageSource`

              Base64-encoded image data.

              - `data: String`

                Base64-encoded image data.

              - `media_type: String`

                MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

              - `type: :base64`

                - `:base64`

            - `class BetaManagedAgentsURLImageSource`

              Image referenced by URL.

              - `type: :url`

                - `:url`

              - `url: String`

                URL of the image to fetch.

            - `class BetaManagedAgentsFileImageSource`

              Image referenced by file ID.

              - `file_id: String`

                ID of a previously uploaded file.

              - `type: :file`

                - `:file`

          - `type: :image`

            - `:image`

        - `class BetaManagedAgentsDocumentBlock`

          Document content, either specified directly as base64 data, as text, or as a reference via a URL.

          - `source: BetaManagedAgentsBase64DocumentSource | BetaManagedAgentsPlainTextDocumentSource | BetaManagedAgentsURLDocumentSource | BetaManagedAgentsFileDocumentSource`

            Union type for document source variants.

            - `class BetaManagedAgentsBase64DocumentSource`

              Base64-encoded document data.

              - `data: String`

                Base64-encoded document data.

              - `media_type: String`

                MIME type of the document (e.g., "application/pdf").

              - `type: :base64`

                - `:base64`

            - `class BetaManagedAgentsPlainTextDocumentSource`

              Plain text document content.

              - `data: String`

                The plain text content.

              - `media_type: :"text/plain"`

                MIME type of the text content. Must be "text/plain".

                - `:"text/plain"`

              - `type: :text`

                - `:text`

            - `class BetaManagedAgentsURLDocumentSource`

              Document referenced by URL.

              - `type: :url`

                - `:url`

              - `url: String`

                URL of the document to fetch.

            - `class BetaManagedAgentsFileDocumentSource`

              Document referenced by file ID.

              - `file_id: String`

                ID of a previously uploaded file.

              - `type: :file`

                - `:file`

          - `type: :document`

            - `:document`

          - `context: String`

            Additional context about the document for the model.

          - `title: String`

            The title of the document.

      - `is_error: bool`

        Whether the tool execution resulted in an error.

      - `processed_at: Time`

        A timestamp in RFC 3339 format

### Example

```ruby
require "anthropic"

anthropic = Anthropic::Client.new(api_key: "my-anthropic-api-key")

beta_managed_agents_send_session_events = anthropic.beta.sessions.events.send_(
  "sesn_011CZkZAtmR3yMPDzynEDxu7",
  events: [{content: [{text: "Where is my order #1234?", type: :text}], type: :"user.message"}]
)

puts(beta_managed_agents_send_session_events)
```

## Stream

`beta.sessions.events.stream(session_id, **kwargs) -> BetaManagedAgentsStreamSessionEvents`

**get** `/v1/sessions/{session_id}/events/stream`

Stream Events

### Parameters

- `session_id: String`

- `betas: Array[AnthropicBeta]`

  Optional header to specify the beta version(s) you want to use.

  - `String`

  - `:"message-batches-2024-09-24" | :"prompt-caching-2024-07-31" | :"computer-use-2024-10-22" | 18 more`

    - `:"message-batches-2024-09-24"`

    - `:"prompt-caching-2024-07-31"`

    - `:"computer-use-2024-10-22"`

    - `:"computer-use-2025-01-24"`

    - `:"pdfs-2024-09-25"`

    - `:"token-counting-2024-11-01"`

    - `:"token-efficient-tools-2025-02-19"`

    - `:"output-128k-2025-02-19"`

    - `:"files-api-2025-04-14"`

    - `:"mcp-client-2025-04-04"`

    - `:"mcp-client-2025-11-20"`

    - `:"dev-full-thinking-2025-05-14"`

    - `:"interleaved-thinking-2025-05-14"`

    - `:"code-execution-2025-05-22"`

    - `:"extended-cache-ttl-2025-04-11"`

    - `:"context-1m-2025-08-07"`

    - `:"context-management-2025-06-27"`

    - `:"model-context-window-exceeded-2025-08-26"`

    - `:"skills-2025-10-02"`

    - `:"fast-mode-2026-02-01"`

    - `:"output-300k-2026-03-24"`

### Returns

- `BetaManagedAgentsStreamSessionEvents = BetaManagedAgentsUserMessageEvent | BetaManagedAgentsUserInterruptEvent | BetaManagedAgentsUserToolConfirmationEvent | 17 more`

  Server-sent event in the session stream.

  - `class BetaManagedAgentsUserMessageEvent`

    A user message event in the session conversation.

    - `id: String`

      Unique identifier for this event.

    - `content: Array[BetaManagedAgentsTextBlock | BetaManagedAgentsImageBlock | BetaManagedAgentsDocumentBlock]`

      Array of content blocks comprising the user message.

      - `class BetaManagedAgentsTextBlock`

        Regular text content.

        - `text: String`

          The text content.

        - `type: :text`

          - `:text`

      - `class BetaManagedAgentsImageBlock`

        Image content specified directly as base64 data or as a reference via a URL.

        - `source: BetaManagedAgentsBase64ImageSource | BetaManagedAgentsURLImageSource | BetaManagedAgentsFileImageSource`

          Union type for image source variants.

          - `class BetaManagedAgentsBase64ImageSource`

            Base64-encoded image data.

            - `data: String`

              Base64-encoded image data.

            - `media_type: String`

              MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

            - `type: :base64`

              - `:base64`

          - `class BetaManagedAgentsURLImageSource`

            Image referenced by URL.

            - `type: :url`

              - `:url`

            - `url: String`

              URL of the image to fetch.

          - `class BetaManagedAgentsFileImageSource`

            Image referenced by file ID.

            - `file_id: String`

              ID of a previously uploaded file.

            - `type: :file`

              - `:file`

        - `type: :image`

          - `:image`

      - `class BetaManagedAgentsDocumentBlock`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

        - `source: BetaManagedAgentsBase64DocumentSource | BetaManagedAgentsPlainTextDocumentSource | BetaManagedAgentsURLDocumentSource | BetaManagedAgentsFileDocumentSource`

          Union type for document source variants.

          - `class BetaManagedAgentsBase64DocumentSource`

            Base64-encoded document data.

            - `data: String`

              Base64-encoded document data.

            - `media_type: String`

              MIME type of the document (e.g., "application/pdf").

            - `type: :base64`

              - `:base64`

          - `class BetaManagedAgentsPlainTextDocumentSource`

            Plain text document content.

            - `data: String`

              The plain text content.

            - `media_type: :"text/plain"`

              MIME type of the text content. Must be "text/plain".

              - `:"text/plain"`

            - `type: :text`

              - `:text`

          - `class BetaManagedAgentsURLDocumentSource`

            Document referenced by URL.

            - `type: :url`

              - `:url`

            - `url: String`

              URL of the document to fetch.

          - `class BetaManagedAgentsFileDocumentSource`

            Document referenced by file ID.

            - `file_id: String`

              ID of a previously uploaded file.

            - `type: :file`

              - `:file`

        - `type: :document`

          - `:document`

        - `context: String`

          Additional context about the document for the model.

        - `title: String`

          The title of the document.

    - `type: :"user.message"`

      - `:"user.message"`

    - `processed_at: Time`

      A timestamp in RFC 3339 format

  - `class BetaManagedAgentsUserInterruptEvent`

    An interrupt event that pauses agent execution and returns control to the user.

    - `id: String`

      Unique identifier for this event.

    - `type: :"user.interrupt"`

      - `:"user.interrupt"`

    - `processed_at: Time`

      A timestamp in RFC 3339 format

  - `class BetaManagedAgentsUserToolConfirmationEvent`

    A tool confirmation event that approves or denies a pending tool execution.

    - `id: String`

      Unique identifier for this event.

    - `result: :allow | :deny`

      UserToolConfirmationResult enum

      - `:allow`

      - `:deny`

    - `tool_use_id: String`

      The id of the `agent.tool_use` or `agent.mcp_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

    - `type: :"user.tool_confirmation"`

      - `:"user.tool_confirmation"`

    - `deny_message: String`

      Optional message providing context for a 'deny' decision. Only allowed when result is 'deny'.

    - `processed_at: Time`

      A timestamp in RFC 3339 format

  - `class BetaManagedAgentsUserCustomToolResultEvent`

    Event sent by the client providing the result of a custom tool execution.

    - `id: String`

      Unique identifier for this event.

    - `custom_tool_use_id: String`

      The id of the `agent.custom_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

    - `type: :"user.custom_tool_result"`

      - `:"user.custom_tool_result"`

    - `content: Array[BetaManagedAgentsTextBlock | BetaManagedAgentsImageBlock | BetaManagedAgentsDocumentBlock]`

      The result content returned by the tool.

      - `class BetaManagedAgentsTextBlock`

        Regular text content.

        - `text: String`

          The text content.

        - `type: :text`

          - `:text`

      - `class BetaManagedAgentsImageBlock`

        Image content specified directly as base64 data or as a reference via a URL.

        - `source: BetaManagedAgentsBase64ImageSource | BetaManagedAgentsURLImageSource | BetaManagedAgentsFileImageSource`

          Union type for image source variants.

          - `class BetaManagedAgentsBase64ImageSource`

            Base64-encoded image data.

            - `data: String`

              Base64-encoded image data.

            - `media_type: String`

              MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

            - `type: :base64`

              - `:base64`

          - `class BetaManagedAgentsURLImageSource`

            Image referenced by URL.

            - `type: :url`

              - `:url`

            - `url: String`

              URL of the image to fetch.

          - `class BetaManagedAgentsFileImageSource`

            Image referenced by file ID.

            - `file_id: String`

              ID of a previously uploaded file.

            - `type: :file`

              - `:file`

        - `type: :image`

          - `:image`

      - `class BetaManagedAgentsDocumentBlock`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

        - `source: BetaManagedAgentsBase64DocumentSource | BetaManagedAgentsPlainTextDocumentSource | BetaManagedAgentsURLDocumentSource | BetaManagedAgentsFileDocumentSource`

          Union type for document source variants.

          - `class BetaManagedAgentsBase64DocumentSource`

            Base64-encoded document data.

            - `data: String`

              Base64-encoded document data.

            - `media_type: String`

              MIME type of the document (e.g., "application/pdf").

            - `type: :base64`

              - `:base64`

          - `class BetaManagedAgentsPlainTextDocumentSource`

            Plain text document content.

            - `data: String`

              The plain text content.

            - `media_type: :"text/plain"`

              MIME type of the text content. Must be "text/plain".

              - `:"text/plain"`

            - `type: :text`

              - `:text`

          - `class BetaManagedAgentsURLDocumentSource`

            Document referenced by URL.

            - `type: :url`

              - `:url`

            - `url: String`

              URL of the document to fetch.

          - `class BetaManagedAgentsFileDocumentSource`

            Document referenced by file ID.

            - `file_id: String`

              ID of a previously uploaded file.

            - `type: :file`

              - `:file`

        - `type: :document`

          - `:document`

        - `context: String`

          Additional context about the document for the model.

        - `title: String`

          The title of the document.

    - `is_error: bool`

      Whether the tool execution resulted in an error.

    - `processed_at: Time`

      A timestamp in RFC 3339 format

  - `class BetaManagedAgentsAgentCustomToolUseEvent`

    Event emitted when the agent calls a custom tool. The session goes idle until the client sends a `user.custom_tool_result` event with the result.

    - `id: String`

      Unique identifier for this event.

    - `input: Hash[Symbol, untyped]`

      Input parameters for the tool call.

    - `name: String`

      Name of the custom tool being called.

    - `processed_at: Time`

      A timestamp in RFC 3339 format

    - `type: :"agent.custom_tool_use"`

      - `:"agent.custom_tool_use"`

  - `class BetaManagedAgentsAgentMessageEvent`

    An agent response event in the session conversation.

    - `id: String`

      Unique identifier for this event.

    - `content: Array[BetaManagedAgentsTextBlock]`

      Array of text blocks comprising the agent response.

      - `text: String`

        The text content.

      - `type: :text`

        - `:text`

    - `processed_at: Time`

      A timestamp in RFC 3339 format

    - `type: :"agent.message"`

      - `:"agent.message"`

  - `class BetaManagedAgentsAgentThinkingEvent`

    Indicates the agent is making forward progress via extended thinking. A progress signal, not a content carrier.

    - `id: String`

      Unique identifier for this event.

    - `processed_at: Time`

      A timestamp in RFC 3339 format

    - `type: :"agent.thinking"`

      - `:"agent.thinking"`

  - `class BetaManagedAgentsAgentMCPToolUseEvent`

    Event emitted when the agent invokes a tool provided by an MCP server.

    - `id: String`

      Unique identifier for this event.

    - `input: Hash[Symbol, untyped]`

      Input parameters for the tool call.

    - `mcp_server_name: String`

      Name of the MCP server providing the tool.

    - `name: String`

      Name of the MCP tool being used.

    - `processed_at: Time`

      A timestamp in RFC 3339 format

    - `type: :"agent.mcp_tool_use"`

      - `:"agent.mcp_tool_use"`

    - `evaluated_permission: :allow | :ask | :deny`

      AgentEvaluatedPermission enum

      - `:allow`

      - `:ask`

      - `:deny`

  - `class BetaManagedAgentsAgentMCPToolResultEvent`

    Event representing the result of an MCP tool execution.

    - `id: String`

      Unique identifier for this event.

    - `mcp_tool_use_id: String`

      The id of the `agent.mcp_tool_use` event this result corresponds to.

    - `processed_at: Time`

      A timestamp in RFC 3339 format

    - `type: :"agent.mcp_tool_result"`

      - `:"agent.mcp_tool_result"`

    - `content: Array[BetaManagedAgentsTextBlock | BetaManagedAgentsImageBlock | BetaManagedAgentsDocumentBlock]`

      The result content returned by the tool.

      - `class BetaManagedAgentsTextBlock`

        Regular text content.

        - `text: String`

          The text content.

        - `type: :text`

          - `:text`

      - `class BetaManagedAgentsImageBlock`

        Image content specified directly as base64 data or as a reference via a URL.

        - `source: BetaManagedAgentsBase64ImageSource | BetaManagedAgentsURLImageSource | BetaManagedAgentsFileImageSource`

          Union type for image source variants.

          - `class BetaManagedAgentsBase64ImageSource`

            Base64-encoded image data.

            - `data: String`

              Base64-encoded image data.

            - `media_type: String`

              MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

            - `type: :base64`

              - `:base64`

          - `class BetaManagedAgentsURLImageSource`

            Image referenced by URL.

            - `type: :url`

              - `:url`

            - `url: String`

              URL of the image to fetch.

          - `class BetaManagedAgentsFileImageSource`

            Image referenced by file ID.

            - `file_id: String`

              ID of a previously uploaded file.

            - `type: :file`

              - `:file`

        - `type: :image`

          - `:image`

      - `class BetaManagedAgentsDocumentBlock`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

        - `source: BetaManagedAgentsBase64DocumentSource | BetaManagedAgentsPlainTextDocumentSource | BetaManagedAgentsURLDocumentSource | BetaManagedAgentsFileDocumentSource`

          Union type for document source variants.

          - `class BetaManagedAgentsBase64DocumentSource`

            Base64-encoded document data.

            - `data: String`

              Base64-encoded document data.

            - `media_type: String`

              MIME type of the document (e.g., "application/pdf").

            - `type: :base64`

              - `:base64`

          - `class BetaManagedAgentsPlainTextDocumentSource`

            Plain text document content.

            - `data: String`

              The plain text content.

            - `media_type: :"text/plain"`

              MIME type of the text content. Must be "text/plain".

              - `:"text/plain"`

            - `type: :text`

              - `:text`

          - `class BetaManagedAgentsURLDocumentSource`

            Document referenced by URL.

            - `type: :url`

              - `:url`

            - `url: String`

              URL of the document to fetch.

          - `class BetaManagedAgentsFileDocumentSource`

            Document referenced by file ID.

            - `file_id: String`

              ID of a previously uploaded file.

            - `type: :file`

              - `:file`

        - `type: :document`

          - `:document`

        - `context: String`

          Additional context about the document for the model.

        - `title: String`

          The title of the document.

    - `is_error: bool`

      Whether the tool execution resulted in an error.

  - `class BetaManagedAgentsAgentToolUseEvent`

    Event emitted when the agent invokes a built-in agent tool.

    - `id: String`

      Unique identifier for this event.

    - `input: Hash[Symbol, untyped]`

      Input parameters for the tool call.

    - `name: String`

      Name of the agent tool being used.

    - `processed_at: Time`

      A timestamp in RFC 3339 format

    - `type: :"agent.tool_use"`

      - `:"agent.tool_use"`

    - `evaluated_permission: :allow | :ask | :deny`

      AgentEvaluatedPermission enum

      - `:allow`

      - `:ask`

      - `:deny`

  - `class BetaManagedAgentsAgentToolResultEvent`

    Event representing the result of an agent tool execution.

    - `id: String`

      Unique identifier for this event.

    - `processed_at: Time`

      A timestamp in RFC 3339 format

    - `tool_use_id: String`

      The id of the `agent.tool_use` event this result corresponds to.

    - `type: :"agent.tool_result"`

      - `:"agent.tool_result"`

    - `content: Array[BetaManagedAgentsTextBlock | BetaManagedAgentsImageBlock | BetaManagedAgentsDocumentBlock]`

      The result content returned by the tool.

      - `class BetaManagedAgentsTextBlock`

        Regular text content.

        - `text: String`

          The text content.

        - `type: :text`

          - `:text`

      - `class BetaManagedAgentsImageBlock`

        Image content specified directly as base64 data or as a reference via a URL.

        - `source: BetaManagedAgentsBase64ImageSource | BetaManagedAgentsURLImageSource | BetaManagedAgentsFileImageSource`

          Union type for image source variants.

          - `class BetaManagedAgentsBase64ImageSource`

            Base64-encoded image data.

            - `data: String`

              Base64-encoded image data.

            - `media_type: String`

              MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

            - `type: :base64`

              - `:base64`

          - `class BetaManagedAgentsURLImageSource`

            Image referenced by URL.

            - `type: :url`

              - `:url`

            - `url: String`

              URL of the image to fetch.

          - `class BetaManagedAgentsFileImageSource`

            Image referenced by file ID.

            - `file_id: String`

              ID of a previously uploaded file.

            - `type: :file`

              - `:file`

        - `type: :image`

          - `:image`

      - `class BetaManagedAgentsDocumentBlock`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

        - `source: BetaManagedAgentsBase64DocumentSource | BetaManagedAgentsPlainTextDocumentSource | BetaManagedAgentsURLDocumentSource | BetaManagedAgentsFileDocumentSource`

          Union type for document source variants.

          - `class BetaManagedAgentsBase64DocumentSource`

            Base64-encoded document data.

            - `data: String`

              Base64-encoded document data.

            - `media_type: String`

              MIME type of the document (e.g., "application/pdf").

            - `type: :base64`

              - `:base64`

          - `class BetaManagedAgentsPlainTextDocumentSource`

            Plain text document content.

            - `data: String`

              The plain text content.

            - `media_type: :"text/plain"`

              MIME type of the text content. Must be "text/plain".

              - `:"text/plain"`

            - `type: :text`

              - `:text`

          - `class BetaManagedAgentsURLDocumentSource`

            Document referenced by URL.

            - `type: :url`

              - `:url`

            - `url: String`

              URL of the document to fetch.

          - `class BetaManagedAgentsFileDocumentSource`

            Document referenced by file ID.

            - `file_id: String`

              ID of a previously uploaded file.

            - `type: :file`

              - `:file`

        - `type: :document`

          - `:document`

        - `context: String`

          Additional context about the document for the model.

        - `title: String`

          The title of the document.

    - `is_error: bool`

      Whether the tool execution resulted in an error.

  - `class BetaManagedAgentsAgentThreadContextCompactedEvent`

    Indicates that context compaction (summarization) occurred during the session.

    - `id: String`

      Unique identifier for this event.

    - `processed_at: Time`

      A timestamp in RFC 3339 format

    - `type: :"agent.thread_context_compacted"`

      - `:"agent.thread_context_compacted"`

  - `class BetaManagedAgentsSessionErrorEvent`

    An error event indicating a problem occurred during session execution.

    - `id: String`

      Unique identifier for this event.

    - `error: BetaManagedAgentsUnknownError | BetaManagedAgentsModelOverloadedError | BetaManagedAgentsModelRateLimitedError | 4 more`

      An unknown or unexpected error occurred during session execution. A fallback variant; clients that don't recognize a new error code can match on `retry_status` and `message` alone.

      - `class BetaManagedAgentsUnknownError`

        An unknown or unexpected error occurred during session execution. A fallback variant; clients that don't recognize a new error code can match on `retry_status` and `message` alone.

        - `message: String`

          Human-readable error description.

        - `retry_status: BetaManagedAgentsRetryStatusRetrying | BetaManagedAgentsRetryStatusExhausted | BetaManagedAgentsRetryStatusTerminal`

          What the client should do next in response to this error.

          - `class BetaManagedAgentsRetryStatusRetrying`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

            - `type: :retrying`

              - `:retrying`

          - `class BetaManagedAgentsRetryStatusExhausted`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

            - `type: :exhausted`

              - `:exhausted`

          - `class BetaManagedAgentsRetryStatusTerminal`

            The session encountered a terminal error and will transition to `terminated` state.

            - `type: :terminal`

              - `:terminal`

        - `type: :unknown_error`

          - `:unknown_error`

      - `class BetaManagedAgentsModelOverloadedError`

        The model is currently overloaded. Emitted after automatic retries are exhausted.

        - `message: String`

          Human-readable error description.

        - `retry_status: BetaManagedAgentsRetryStatusRetrying | BetaManagedAgentsRetryStatusExhausted | BetaManagedAgentsRetryStatusTerminal`

          What the client should do next in response to this error.

          - `class BetaManagedAgentsRetryStatusRetrying`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

            - `type: :retrying`

              - `:retrying`

          - `class BetaManagedAgentsRetryStatusExhausted`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

            - `type: :exhausted`

              - `:exhausted`

          - `class BetaManagedAgentsRetryStatusTerminal`

            The session encountered a terminal error and will transition to `terminated` state.

            - `type: :terminal`

              - `:terminal`

        - `type: :model_overloaded_error`

          - `:model_overloaded_error`

      - `class BetaManagedAgentsModelRateLimitedError`

        The model request was rate-limited.

        - `message: String`

          Human-readable error description.

        - `retry_status: BetaManagedAgentsRetryStatusRetrying | BetaManagedAgentsRetryStatusExhausted | BetaManagedAgentsRetryStatusTerminal`

          What the client should do next in response to this error.

          - `class BetaManagedAgentsRetryStatusRetrying`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

            - `type: :retrying`

              - `:retrying`

          - `class BetaManagedAgentsRetryStatusExhausted`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

            - `type: :exhausted`

              - `:exhausted`

          - `class BetaManagedAgentsRetryStatusTerminal`

            The session encountered a terminal error and will transition to `terminated` state.

            - `type: :terminal`

              - `:terminal`

        - `type: :model_rate_limited_error`

          - `:model_rate_limited_error`

      - `class BetaManagedAgentsModelRequestFailedError`

        A model request failed for a reason other than overload or rate-limiting.

        - `message: String`

          Human-readable error description.

        - `retry_status: BetaManagedAgentsRetryStatusRetrying | BetaManagedAgentsRetryStatusExhausted | BetaManagedAgentsRetryStatusTerminal`

          What the client should do next in response to this error.

          - `class BetaManagedAgentsRetryStatusRetrying`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

            - `type: :retrying`

              - `:retrying`

          - `class BetaManagedAgentsRetryStatusExhausted`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

            - `type: :exhausted`

              - `:exhausted`

          - `class BetaManagedAgentsRetryStatusTerminal`

            The session encountered a terminal error and will transition to `terminated` state.

            - `type: :terminal`

              - `:terminal`

        - `type: :model_request_failed_error`

          - `:model_request_failed_error`

      - `class BetaManagedAgentsMCPConnectionFailedError`

        Failed to connect to an MCP server.

        - `mcp_server_name: String`

          Name of the MCP server that failed to connect.

        - `message: String`

          Human-readable error description.

        - `retry_status: BetaManagedAgentsRetryStatusRetrying | BetaManagedAgentsRetryStatusExhausted | BetaManagedAgentsRetryStatusTerminal`

          What the client should do next in response to this error.

          - `class BetaManagedAgentsRetryStatusRetrying`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

            - `type: :retrying`

              - `:retrying`

          - `class BetaManagedAgentsRetryStatusExhausted`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

            - `type: :exhausted`

              - `:exhausted`

          - `class BetaManagedAgentsRetryStatusTerminal`

            The session encountered a terminal error and will transition to `terminated` state.

            - `type: :terminal`

              - `:terminal`

        - `type: :mcp_connection_failed_error`

          - `:mcp_connection_failed_error`

      - `class BetaManagedAgentsMCPAuthenticationFailedError`

        Authentication to an MCP server failed.

        - `mcp_server_name: String`

          Name of the MCP server that failed authentication.

        - `message: String`

          Human-readable error description.

        - `retry_status: BetaManagedAgentsRetryStatusRetrying | BetaManagedAgentsRetryStatusExhausted | BetaManagedAgentsRetryStatusTerminal`

          What the client should do next in response to this error.

          - `class BetaManagedAgentsRetryStatusRetrying`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

            - `type: :retrying`

              - `:retrying`

          - `class BetaManagedAgentsRetryStatusExhausted`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

            - `type: :exhausted`

              - `:exhausted`

          - `class BetaManagedAgentsRetryStatusTerminal`

            The session encountered a terminal error and will transition to `terminated` state.

            - `type: :terminal`

              - `:terminal`

        - `type: :mcp_authentication_failed_error`

          - `:mcp_authentication_failed_error`

      - `class BetaManagedAgentsBillingError`

        The caller's organization or workspace cannot make model requests — out of credits or spend limit reached. Retrying with the same credentials will not succeed; the caller must resolve the billing state.

        - `message: String`

          Human-readable error description.

        - `retry_status: BetaManagedAgentsRetryStatusRetrying | BetaManagedAgentsRetryStatusExhausted | BetaManagedAgentsRetryStatusTerminal`

          What the client should do next in response to this error.

          - `class BetaManagedAgentsRetryStatusRetrying`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

            - `type: :retrying`

              - `:retrying`

          - `class BetaManagedAgentsRetryStatusExhausted`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

            - `type: :exhausted`

              - `:exhausted`

          - `class BetaManagedAgentsRetryStatusTerminal`

            The session encountered a terminal error and will transition to `terminated` state.

            - `type: :terminal`

              - `:terminal`

        - `type: :billing_error`

          - `:billing_error`

    - `processed_at: Time`

      A timestamp in RFC 3339 format

    - `type: :"session.error"`

      - `:"session.error"`

  - `class BetaManagedAgentsSessionStatusRescheduledEvent`

    Indicates the session is recovering from an error state and is rescheduled for execution.

    - `id: String`

      Unique identifier for this event.

    - `processed_at: Time`

      A timestamp in RFC 3339 format

    - `type: :"session.status_rescheduled"`

      - `:"session.status_rescheduled"`

  - `class BetaManagedAgentsSessionStatusRunningEvent`

    Indicates the session is actively running and the agent is working.

    - `id: String`

      Unique identifier for this event.

    - `processed_at: Time`

      A timestamp in RFC 3339 format

    - `type: :"session.status_running"`

      - `:"session.status_running"`

  - `class BetaManagedAgentsSessionStatusIdleEvent`

    Indicates the agent has paused and is awaiting user input.

    - `id: String`

      Unique identifier for this event.

    - `processed_at: Time`

      A timestamp in RFC 3339 format

    - `stop_reason: BetaManagedAgentsSessionEndTurn | BetaManagedAgentsSessionRequiresAction | BetaManagedAgentsSessionRetriesExhausted`

      The agent completed its turn naturally and is ready for the next user message.

      - `class BetaManagedAgentsSessionEndTurn`

        The agent completed its turn naturally and is ready for the next user message.

        - `type: :end_turn`

          - `:end_turn`

      - `class BetaManagedAgentsSessionRequiresAction`

        The agent is idle waiting on one or more blocking user-input events (tool confirmation, custom tool result, etc.). Resolving all of them transitions the session back to running.

        - `event_ids: Array[String]`

          The ids of events the agent is blocked on. Resolving fewer than all re-emits `session.status_idle` with the remainder.

        - `type: :requires_action`

          - `:requires_action`

      - `class BetaManagedAgentsSessionRetriesExhausted`

        The turn ended because the retry budget was exhausted (`max_iterations` hit or an error escalated to `retry_status: 'exhausted'`).

        - `type: :retries_exhausted`

          - `:retries_exhausted`

    - `type: :"session.status_idle"`

      - `:"session.status_idle"`

  - `class BetaManagedAgentsSessionStatusTerminatedEvent`

    Indicates the session has terminated, either due to an error or completion.

    - `id: String`

      Unique identifier for this event.

    - `processed_at: Time`

      A timestamp in RFC 3339 format

    - `type: :"session.status_terminated"`

      - `:"session.status_terminated"`

  - `class BetaManagedAgentsSpanModelRequestStartEvent`

    Emitted when a model request is initiated by the agent.

    - `id: String`

      Unique identifier for this event.

    - `processed_at: Time`

      A timestamp in RFC 3339 format

    - `type: :"span.model_request_start"`

      - `:"span.model_request_start"`

  - `class BetaManagedAgentsSpanModelRequestEndEvent`

    Emitted when a model request completes.

    - `id: String`

      Unique identifier for this event.

    - `is_error: bool`

      Whether the model request resulted in an error.

    - `model_request_start_id: String`

      The id of the corresponding `span.model_request_start` event.

    - `model_usage: BetaManagedAgentsSpanModelUsage`

      Token usage for a single model request.

      - `cache_creation_input_tokens: Integer`

        Tokens used to create prompt cache in this request.

      - `cache_read_input_tokens: Integer`

        Tokens read from prompt cache in this request.

      - `input_tokens: Integer`

        Input tokens consumed by this request.

      - `output_tokens: Integer`

        Output tokens generated by this request.

      - `speed: :standard | :fast`

        Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

        - `:standard`

        - `:fast`

    - `processed_at: Time`

      A timestamp in RFC 3339 format

    - `type: :"span.model_request_end"`

      - `:"span.model_request_end"`

  - `class BetaManagedAgentsSessionDeletedEvent`

    Emitted when a session has been deleted. Terminates any active event stream — no further events will be emitted for this session.

    - `id: String`

      Unique identifier for this event.

    - `processed_at: Time`

      A timestamp in RFC 3339 format

    - `type: :"session.deleted"`

      - `:"session.deleted"`

### Example

```ruby
require "anthropic"

anthropic = Anthropic::Client.new(api_key: "my-anthropic-api-key")

beta_managed_agents_stream_session_events = anthropic.beta.sessions.events.stream("sesn_011CZkZAtmR3yMPDzynEDxu7")

puts(beta_managed_agents_stream_session_events)
```

## Domain Types

### Beta Managed Agents Agent Custom Tool Use Event

- `class BetaManagedAgentsAgentCustomToolUseEvent`

  Event emitted when the agent calls a custom tool. The session goes idle until the client sends a `user.custom_tool_result` event with the result.

  - `id: String`

    Unique identifier for this event.

  - `input: Hash[Symbol, untyped]`

    Input parameters for the tool call.

  - `name: String`

    Name of the custom tool being called.

  - `processed_at: Time`

    A timestamp in RFC 3339 format

  - `type: :"agent.custom_tool_use"`

    - `:"agent.custom_tool_use"`

### Beta Managed Agents Agent MCP Tool Result Event

- `class BetaManagedAgentsAgentMCPToolResultEvent`

  Event representing the result of an MCP tool execution.

  - `id: String`

    Unique identifier for this event.

  - `mcp_tool_use_id: String`

    The id of the `agent.mcp_tool_use` event this result corresponds to.

  - `processed_at: Time`

    A timestamp in RFC 3339 format

  - `type: :"agent.mcp_tool_result"`

    - `:"agent.mcp_tool_result"`

  - `content: Array[BetaManagedAgentsTextBlock | BetaManagedAgentsImageBlock | BetaManagedAgentsDocumentBlock]`

    The result content returned by the tool.

    - `class BetaManagedAgentsTextBlock`

      Regular text content.

      - `text: String`

        The text content.

      - `type: :text`

        - `:text`

    - `class BetaManagedAgentsImageBlock`

      Image content specified directly as base64 data or as a reference via a URL.

      - `source: BetaManagedAgentsBase64ImageSource | BetaManagedAgentsURLImageSource | BetaManagedAgentsFileImageSource`

        Union type for image source variants.

        - `class BetaManagedAgentsBase64ImageSource`

          Base64-encoded image data.

          - `data: String`

            Base64-encoded image data.

          - `media_type: String`

            MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

          - `type: :base64`

            - `:base64`

        - `class BetaManagedAgentsURLImageSource`

          Image referenced by URL.

          - `type: :url`

            - `:url`

          - `url: String`

            URL of the image to fetch.

        - `class BetaManagedAgentsFileImageSource`

          Image referenced by file ID.

          - `file_id: String`

            ID of a previously uploaded file.

          - `type: :file`

            - `:file`

      - `type: :image`

        - `:image`

    - `class BetaManagedAgentsDocumentBlock`

      Document content, either specified directly as base64 data, as text, or as a reference via a URL.

      - `source: BetaManagedAgentsBase64DocumentSource | BetaManagedAgentsPlainTextDocumentSource | BetaManagedAgentsURLDocumentSource | BetaManagedAgentsFileDocumentSource`

        Union type for document source variants.

        - `class BetaManagedAgentsBase64DocumentSource`

          Base64-encoded document data.

          - `data: String`

            Base64-encoded document data.

          - `media_type: String`

            MIME type of the document (e.g., "application/pdf").

          - `type: :base64`

            - `:base64`

        - `class BetaManagedAgentsPlainTextDocumentSource`

          Plain text document content.

          - `data: String`

            The plain text content.

          - `media_type: :"text/plain"`

            MIME type of the text content. Must be "text/plain".

            - `:"text/plain"`

          - `type: :text`

            - `:text`

        - `class BetaManagedAgentsURLDocumentSource`

          Document referenced by URL.

          - `type: :url`

            - `:url`

          - `url: String`

            URL of the document to fetch.

        - `class BetaManagedAgentsFileDocumentSource`

          Document referenced by file ID.

          - `file_id: String`

            ID of a previously uploaded file.

          - `type: :file`

            - `:file`

      - `type: :document`

        - `:document`

      - `context: String`

        Additional context about the document for the model.

      - `title: String`

        The title of the document.

  - `is_error: bool`

    Whether the tool execution resulted in an error.

### Beta Managed Agents Agent MCP Tool Use Event

- `class BetaManagedAgentsAgentMCPToolUseEvent`

  Event emitted when the agent invokes a tool provided by an MCP server.

  - `id: String`

    Unique identifier for this event.

  - `input: Hash[Symbol, untyped]`

    Input parameters for the tool call.

  - `mcp_server_name: String`

    Name of the MCP server providing the tool.

  - `name: String`

    Name of the MCP tool being used.

  - `processed_at: Time`

    A timestamp in RFC 3339 format

  - `type: :"agent.mcp_tool_use"`

    - `:"agent.mcp_tool_use"`

  - `evaluated_permission: :allow | :ask | :deny`

    AgentEvaluatedPermission enum

    - `:allow`

    - `:ask`

    - `:deny`

### Beta Managed Agents Agent Message Event

- `class BetaManagedAgentsAgentMessageEvent`

  An agent response event in the session conversation.

  - `id: String`

    Unique identifier for this event.

  - `content: Array[BetaManagedAgentsTextBlock]`

    Array of text blocks comprising the agent response.

    - `text: String`

      The text content.

    - `type: :text`

      - `:text`

  - `processed_at: Time`

    A timestamp in RFC 3339 format

  - `type: :"agent.message"`

    - `:"agent.message"`

### Beta Managed Agents Agent Thinking Event

- `class BetaManagedAgentsAgentThinkingEvent`

  Indicates the agent is making forward progress via extended thinking. A progress signal, not a content carrier.

  - `id: String`

    Unique identifier for this event.

  - `processed_at: Time`

    A timestamp in RFC 3339 format

  - `type: :"agent.thinking"`

    - `:"agent.thinking"`

### Beta Managed Agents Agent Thread Context Compacted Event

- `class BetaManagedAgentsAgentThreadContextCompactedEvent`

  Indicates that context compaction (summarization) occurred during the session.

  - `id: String`

    Unique identifier for this event.

  - `processed_at: Time`

    A timestamp in RFC 3339 format

  - `type: :"agent.thread_context_compacted"`

    - `:"agent.thread_context_compacted"`

### Beta Managed Agents Agent Tool Result Event

- `class BetaManagedAgentsAgentToolResultEvent`

  Event representing the result of an agent tool execution.

  - `id: String`

    Unique identifier for this event.

  - `processed_at: Time`

    A timestamp in RFC 3339 format

  - `tool_use_id: String`

    The id of the `agent.tool_use` event this result corresponds to.

  - `type: :"agent.tool_result"`

    - `:"agent.tool_result"`

  - `content: Array[BetaManagedAgentsTextBlock | BetaManagedAgentsImageBlock | BetaManagedAgentsDocumentBlock]`

    The result content returned by the tool.

    - `class BetaManagedAgentsTextBlock`

      Regular text content.

      - `text: String`

        The text content.

      - `type: :text`

        - `:text`

    - `class BetaManagedAgentsImageBlock`

      Image content specified directly as base64 data or as a reference via a URL.

      - `source: BetaManagedAgentsBase64ImageSource | BetaManagedAgentsURLImageSource | BetaManagedAgentsFileImageSource`

        Union type for image source variants.

        - `class BetaManagedAgentsBase64ImageSource`

          Base64-encoded image data.

          - `data: String`

            Base64-encoded image data.

          - `media_type: String`

            MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

          - `type: :base64`

            - `:base64`

        - `class BetaManagedAgentsURLImageSource`

          Image referenced by URL.

          - `type: :url`

            - `:url`

          - `url: String`

            URL of the image to fetch.

        - `class BetaManagedAgentsFileImageSource`

          Image referenced by file ID.

          - `file_id: String`

            ID of a previously uploaded file.

          - `type: :file`

            - `:file`

      - `type: :image`

        - `:image`

    - `class BetaManagedAgentsDocumentBlock`

      Document content, either specified directly as base64 data, as text, or as a reference via a URL.

      - `source: BetaManagedAgentsBase64DocumentSource | BetaManagedAgentsPlainTextDocumentSource | BetaManagedAgentsURLDocumentSource | BetaManagedAgentsFileDocumentSource`

        Union type for document source variants.

        - `class BetaManagedAgentsBase64DocumentSource`

          Base64-encoded document data.

          - `data: String`

            Base64-encoded document data.

          - `media_type: String`

            MIME type of the document (e.g., "application/pdf").

          - `type: :base64`

            - `:base64`

        - `class BetaManagedAgentsPlainTextDocumentSource`

          Plain text document content.

          - `data: String`

            The plain text content.

          - `media_type: :"text/plain"`

            MIME type of the text content. Must be "text/plain".

            - `:"text/plain"`

          - `type: :text`

            - `:text`

        - `class BetaManagedAgentsURLDocumentSource`

          Document referenced by URL.

          - `type: :url`

            - `:url`

          - `url: String`

            URL of the document to fetch.

        - `class BetaManagedAgentsFileDocumentSource`

          Document referenced by file ID.

          - `file_id: String`

            ID of a previously uploaded file.

          - `type: :file`

            - `:file`

      - `type: :document`

        - `:document`

      - `context: String`

        Additional context about the document for the model.

      - `title: String`

        The title of the document.

  - `is_error: bool`

    Whether the tool execution resulted in an error.

### Beta Managed Agents Agent Tool Use Event

- `class BetaManagedAgentsAgentToolUseEvent`

  Event emitted when the agent invokes a built-in agent tool.

  - `id: String`

    Unique identifier for this event.

  - `input: Hash[Symbol, untyped]`

    Input parameters for the tool call.

  - `name: String`

    Name of the agent tool being used.

  - `processed_at: Time`

    A timestamp in RFC 3339 format

  - `type: :"agent.tool_use"`

    - `:"agent.tool_use"`

  - `evaluated_permission: :allow | :ask | :deny`

    AgentEvaluatedPermission enum

    - `:allow`

    - `:ask`

    - `:deny`

### Beta Managed Agents Base64 Document Source

- `class BetaManagedAgentsBase64DocumentSource`

  Base64-encoded document data.

  - `data: String`

    Base64-encoded document data.

  - `media_type: String`

    MIME type of the document (e.g., "application/pdf").

  - `type: :base64`

    - `:base64`

### Beta Managed Agents Base64 Image Source

- `class BetaManagedAgentsBase64ImageSource`

  Base64-encoded image data.

  - `data: String`

    Base64-encoded image data.

  - `media_type: String`

    MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

  - `type: :base64`

    - `:base64`

### Beta Managed Agents Billing Error

- `class BetaManagedAgentsBillingError`

  The caller's organization or workspace cannot make model requests — out of credits or spend limit reached. Retrying with the same credentials will not succeed; the caller must resolve the billing state.

  - `message: String`

    Human-readable error description.

  - `retry_status: BetaManagedAgentsRetryStatusRetrying | BetaManagedAgentsRetryStatusExhausted | BetaManagedAgentsRetryStatusTerminal`

    What the client should do next in response to this error.

    - `class BetaManagedAgentsRetryStatusRetrying`

      The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

      - `type: :retrying`

        - `:retrying`

    - `class BetaManagedAgentsRetryStatusExhausted`

      This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

      - `type: :exhausted`

        - `:exhausted`

    - `class BetaManagedAgentsRetryStatusTerminal`

      The session encountered a terminal error and will transition to `terminated` state.

      - `type: :terminal`

        - `:terminal`

  - `type: :billing_error`

    - `:billing_error`

### Beta Managed Agents Document Block

- `class BetaManagedAgentsDocumentBlock`

  Document content, either specified directly as base64 data, as text, or as a reference via a URL.

  - `source: BetaManagedAgentsBase64DocumentSource | BetaManagedAgentsPlainTextDocumentSource | BetaManagedAgentsURLDocumentSource | BetaManagedAgentsFileDocumentSource`

    Union type for document source variants.

    - `class BetaManagedAgentsBase64DocumentSource`

      Base64-encoded document data.

      - `data: String`

        Base64-encoded document data.

      - `media_type: String`

        MIME type of the document (e.g., "application/pdf").

      - `type: :base64`

        - `:base64`

    - `class BetaManagedAgentsPlainTextDocumentSource`

      Plain text document content.

      - `data: String`

        The plain text content.

      - `media_type: :"text/plain"`

        MIME type of the text content. Must be "text/plain".

        - `:"text/plain"`

      - `type: :text`

        - `:text`

    - `class BetaManagedAgentsURLDocumentSource`

      Document referenced by URL.

      - `type: :url`

        - `:url`

      - `url: String`

        URL of the document to fetch.

    - `class BetaManagedAgentsFileDocumentSource`

      Document referenced by file ID.

      - `file_id: String`

        ID of a previously uploaded file.

      - `type: :file`

        - `:file`

  - `type: :document`

    - `:document`

  - `context: String`

    Additional context about the document for the model.

  - `title: String`

    The title of the document.

### Beta Managed Agents Event Params

- `BetaManagedAgentsEventParams = BetaManagedAgentsUserMessageEventParams | BetaManagedAgentsUserInterruptEventParams | BetaManagedAgentsUserToolConfirmationEventParams | BetaManagedAgentsUserCustomToolResultEventParams`

  Union type for event parameters that can be sent to a session.

  - `class BetaManagedAgentsUserMessageEventParams`

    Parameters for sending a user message to the session.

    - `content: Array[BetaManagedAgentsTextBlock | BetaManagedAgentsImageBlock | BetaManagedAgentsDocumentBlock]`

      Array of content blocks for the user message.

      - `class BetaManagedAgentsTextBlock`

        Regular text content.

        - `text: String`

          The text content.

        - `type: :text`

          - `:text`

      - `class BetaManagedAgentsImageBlock`

        Image content specified directly as base64 data or as a reference via a URL.

        - `source: BetaManagedAgentsBase64ImageSource | BetaManagedAgentsURLImageSource | BetaManagedAgentsFileImageSource`

          Union type for image source variants.

          - `class BetaManagedAgentsBase64ImageSource`

            Base64-encoded image data.

            - `data: String`

              Base64-encoded image data.

            - `media_type: String`

              MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

            - `type: :base64`

              - `:base64`

          - `class BetaManagedAgentsURLImageSource`

            Image referenced by URL.

            - `type: :url`

              - `:url`

            - `url: String`

              URL of the image to fetch.

          - `class BetaManagedAgentsFileImageSource`

            Image referenced by file ID.

            - `file_id: String`

              ID of a previously uploaded file.

            - `type: :file`

              - `:file`

        - `type: :image`

          - `:image`

      - `class BetaManagedAgentsDocumentBlock`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

        - `source: BetaManagedAgentsBase64DocumentSource | BetaManagedAgentsPlainTextDocumentSource | BetaManagedAgentsURLDocumentSource | BetaManagedAgentsFileDocumentSource`

          Union type for document source variants.

          - `class BetaManagedAgentsBase64DocumentSource`

            Base64-encoded document data.

            - `data: String`

              Base64-encoded document data.

            - `media_type: String`

              MIME type of the document (e.g., "application/pdf").

            - `type: :base64`

              - `:base64`

          - `class BetaManagedAgentsPlainTextDocumentSource`

            Plain text document content.

            - `data: String`

              The plain text content.

            - `media_type: :"text/plain"`

              MIME type of the text content. Must be "text/plain".

              - `:"text/plain"`

            - `type: :text`

              - `:text`

          - `class BetaManagedAgentsURLDocumentSource`

            Document referenced by URL.

            - `type: :url`

              - `:url`

            - `url: String`

              URL of the document to fetch.

          - `class BetaManagedAgentsFileDocumentSource`

            Document referenced by file ID.

            - `file_id: String`

              ID of a previously uploaded file.

            - `type: :file`

              - `:file`

        - `type: :document`

          - `:document`

        - `context: String`

          Additional context about the document for the model.

        - `title: String`

          The title of the document.

    - `type: :"user.message"`

      - `:"user.message"`

  - `class BetaManagedAgentsUserInterruptEventParams`

    Parameters for sending an interrupt to pause the agent.

    - `type: :"user.interrupt"`

      - `:"user.interrupt"`

  - `class BetaManagedAgentsUserToolConfirmationEventParams`

    Parameters for confirming or denying a tool execution request.

    - `result: :allow | :deny`

      UserToolConfirmationResult enum

      - `:allow`

      - `:deny`

    - `tool_use_id: String`

      The id of the `agent.tool_use` or `agent.mcp_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

    - `type: :"user.tool_confirmation"`

      - `:"user.tool_confirmation"`

    - `deny_message: String`

      Optional message providing context for a 'deny' decision. Only allowed when result is 'deny'.

  - `class BetaManagedAgentsUserCustomToolResultEventParams`

    Parameters for providing the result of a custom tool execution.

    - `custom_tool_use_id: String`

      The id of the `agent.custom_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

    - `type: :"user.custom_tool_result"`

      - `:"user.custom_tool_result"`

    - `content: Array[BetaManagedAgentsTextBlock | BetaManagedAgentsImageBlock | BetaManagedAgentsDocumentBlock]`

      The result content returned by the tool.

      - `class BetaManagedAgentsTextBlock`

        Regular text content.

        - `text: String`

          The text content.

        - `type: :text`

          - `:text`

      - `class BetaManagedAgentsImageBlock`

        Image content specified directly as base64 data or as a reference via a URL.

        - `source: BetaManagedAgentsBase64ImageSource | BetaManagedAgentsURLImageSource | BetaManagedAgentsFileImageSource`

          Union type for image source variants.

          - `class BetaManagedAgentsBase64ImageSource`

            Base64-encoded image data.

            - `data: String`

              Base64-encoded image data.

            - `media_type: String`

              MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

            - `type: :base64`

              - `:base64`

          - `class BetaManagedAgentsURLImageSource`

            Image referenced by URL.

            - `type: :url`

              - `:url`

            - `url: String`

              URL of the image to fetch.

          - `class BetaManagedAgentsFileImageSource`

            Image referenced by file ID.

            - `file_id: String`

              ID of a previously uploaded file.

            - `type: :file`

              - `:file`

        - `type: :image`

          - `:image`

      - `class BetaManagedAgentsDocumentBlock`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

        - `source: BetaManagedAgentsBase64DocumentSource | BetaManagedAgentsPlainTextDocumentSource | BetaManagedAgentsURLDocumentSource | BetaManagedAgentsFileDocumentSource`

          Union type for document source variants.

          - `class BetaManagedAgentsBase64DocumentSource`

            Base64-encoded document data.

            - `data: String`

              Base64-encoded document data.

            - `media_type: String`

              MIME type of the document (e.g., "application/pdf").

            - `type: :base64`

              - `:base64`

          - `class BetaManagedAgentsPlainTextDocumentSource`

            Plain text document content.

            - `data: String`

              The plain text content.

            - `media_type: :"text/plain"`

              MIME type of the text content. Must be "text/plain".

              - `:"text/plain"`

            - `type: :text`

              - `:text`

          - `class BetaManagedAgentsURLDocumentSource`

            Document referenced by URL.

            - `type: :url`

              - `:url`

            - `url: String`

              URL of the document to fetch.

          - `class BetaManagedAgentsFileDocumentSource`

            Document referenced by file ID.

            - `file_id: String`

              ID of a previously uploaded file.

            - `type: :file`

              - `:file`

        - `type: :document`

          - `:document`

        - `context: String`

          Additional context about the document for the model.

        - `title: String`

          The title of the document.

    - `is_error: bool`

      Whether the tool execution resulted in an error.

### Beta Managed Agents File Document Source

- `class BetaManagedAgentsFileDocumentSource`

  Document referenced by file ID.

  - `file_id: String`

    ID of a previously uploaded file.

  - `type: :file`

    - `:file`

### Beta Managed Agents File Image Source

- `class BetaManagedAgentsFileImageSource`

  Image referenced by file ID.

  - `file_id: String`

    ID of a previously uploaded file.

  - `type: :file`

    - `:file`

### Beta Managed Agents Image Block

- `class BetaManagedAgentsImageBlock`

  Image content specified directly as base64 data or as a reference via a URL.

  - `source: BetaManagedAgentsBase64ImageSource | BetaManagedAgentsURLImageSource | BetaManagedAgentsFileImageSource`

    Union type for image source variants.

    - `class BetaManagedAgentsBase64ImageSource`

      Base64-encoded image data.

      - `data: String`

        Base64-encoded image data.

      - `media_type: String`

        MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

      - `type: :base64`

        - `:base64`

    - `class BetaManagedAgentsURLImageSource`

      Image referenced by URL.

      - `type: :url`

        - `:url`

      - `url: String`

        URL of the image to fetch.

    - `class BetaManagedAgentsFileImageSource`

      Image referenced by file ID.

      - `file_id: String`

        ID of a previously uploaded file.

      - `type: :file`

        - `:file`

  - `type: :image`

    - `:image`

### Beta Managed Agents MCP Authentication Failed Error

- `class BetaManagedAgentsMCPAuthenticationFailedError`

  Authentication to an MCP server failed.

  - `mcp_server_name: String`

    Name of the MCP server that failed authentication.

  - `message: String`

    Human-readable error description.

  - `retry_status: BetaManagedAgentsRetryStatusRetrying | BetaManagedAgentsRetryStatusExhausted | BetaManagedAgentsRetryStatusTerminal`

    What the client should do next in response to this error.

    - `class BetaManagedAgentsRetryStatusRetrying`

      The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

      - `type: :retrying`

        - `:retrying`

    - `class BetaManagedAgentsRetryStatusExhausted`

      This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

      - `type: :exhausted`

        - `:exhausted`

    - `class BetaManagedAgentsRetryStatusTerminal`

      The session encountered a terminal error and will transition to `terminated` state.

      - `type: :terminal`

        - `:terminal`

  - `type: :mcp_authentication_failed_error`

    - `:mcp_authentication_failed_error`

### Beta Managed Agents MCP Connection Failed Error

- `class BetaManagedAgentsMCPConnectionFailedError`

  Failed to connect to an MCP server.

  - `mcp_server_name: String`

    Name of the MCP server that failed to connect.

  - `message: String`

    Human-readable error description.

  - `retry_status: BetaManagedAgentsRetryStatusRetrying | BetaManagedAgentsRetryStatusExhausted | BetaManagedAgentsRetryStatusTerminal`

    What the client should do next in response to this error.

    - `class BetaManagedAgentsRetryStatusRetrying`

      The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

      - `type: :retrying`

        - `:retrying`

    - `class BetaManagedAgentsRetryStatusExhausted`

      This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

      - `type: :exhausted`

        - `:exhausted`

    - `class BetaManagedAgentsRetryStatusTerminal`

      The session encountered a terminal error and will transition to `terminated` state.

      - `type: :terminal`

        - `:terminal`

  - `type: :mcp_connection_failed_error`

    - `:mcp_connection_failed_error`

### Beta Managed Agents Model Overloaded Error

- `class BetaManagedAgentsModelOverloadedError`

  The model is currently overloaded. Emitted after automatic retries are exhausted.

  - `message: String`

    Human-readable error description.

  - `retry_status: BetaManagedAgentsRetryStatusRetrying | BetaManagedAgentsRetryStatusExhausted | BetaManagedAgentsRetryStatusTerminal`

    What the client should do next in response to this error.

    - `class BetaManagedAgentsRetryStatusRetrying`

      The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

      - `type: :retrying`

        - `:retrying`

    - `class BetaManagedAgentsRetryStatusExhausted`

      This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

      - `type: :exhausted`

        - `:exhausted`

    - `class BetaManagedAgentsRetryStatusTerminal`

      The session encountered a terminal error and will transition to `terminated` state.

      - `type: :terminal`

        - `:terminal`

  - `type: :model_overloaded_error`

    - `:model_overloaded_error`

### Beta Managed Agents Model Rate Limited Error

- `class BetaManagedAgentsModelRateLimitedError`

  The model request was rate-limited.

  - `message: String`

    Human-readable error description.

  - `retry_status: BetaManagedAgentsRetryStatusRetrying | BetaManagedAgentsRetryStatusExhausted | BetaManagedAgentsRetryStatusTerminal`

    What the client should do next in response to this error.

    - `class BetaManagedAgentsRetryStatusRetrying`

      The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

      - `type: :retrying`

        - `:retrying`

    - `class BetaManagedAgentsRetryStatusExhausted`

      This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

      - `type: :exhausted`

        - `:exhausted`

    - `class BetaManagedAgentsRetryStatusTerminal`

      The session encountered a terminal error and will transition to `terminated` state.

      - `type: :terminal`

        - `:terminal`

  - `type: :model_rate_limited_error`

    - `:model_rate_limited_error`

### Beta Managed Agents Model Request Failed Error

- `class BetaManagedAgentsModelRequestFailedError`

  A model request failed for a reason other than overload or rate-limiting.

  - `message: String`

    Human-readable error description.

  - `retry_status: BetaManagedAgentsRetryStatusRetrying | BetaManagedAgentsRetryStatusExhausted | BetaManagedAgentsRetryStatusTerminal`

    What the client should do next in response to this error.

    - `class BetaManagedAgentsRetryStatusRetrying`

      The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

      - `type: :retrying`

        - `:retrying`

    - `class BetaManagedAgentsRetryStatusExhausted`

      This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

      - `type: :exhausted`

        - `:exhausted`

    - `class BetaManagedAgentsRetryStatusTerminal`

      The session encountered a terminal error and will transition to `terminated` state.

      - `type: :terminal`

        - `:terminal`

  - `type: :model_request_failed_error`

    - `:model_request_failed_error`

### Beta Managed Agents Plain Text Document Source

- `class BetaManagedAgentsPlainTextDocumentSource`

  Plain text document content.

  - `data: String`

    The plain text content.

  - `media_type: :"text/plain"`

    MIME type of the text content. Must be "text/plain".

    - `:"text/plain"`

  - `type: :text`

    - `:text`

### Beta Managed Agents Retry Status Exhausted

- `class BetaManagedAgentsRetryStatusExhausted`

  This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

  - `type: :exhausted`

    - `:exhausted`

### Beta Managed Agents Retry Status Retrying

- `class BetaManagedAgentsRetryStatusRetrying`

  The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

  - `type: :retrying`

    - `:retrying`

### Beta Managed Agents Retry Status Terminal

- `class BetaManagedAgentsRetryStatusTerminal`

  The session encountered a terminal error and will transition to `terminated` state.

  - `type: :terminal`

    - `:terminal`

### Beta Managed Agents Send Session Events

- `class BetaManagedAgentsSendSessionEvents`

  Events that were successfully sent to the session.

  - `data: Array[BetaManagedAgentsUserMessageEvent | BetaManagedAgentsUserInterruptEvent | BetaManagedAgentsUserToolConfirmationEvent | BetaManagedAgentsUserCustomToolResultEvent]`

    Sent events

    - `class BetaManagedAgentsUserMessageEvent`

      A user message event in the session conversation.

      - `id: String`

        Unique identifier for this event.

      - `content: Array[BetaManagedAgentsTextBlock | BetaManagedAgentsImageBlock | BetaManagedAgentsDocumentBlock]`

        Array of content blocks comprising the user message.

        - `class BetaManagedAgentsTextBlock`

          Regular text content.

          - `text: String`

            The text content.

          - `type: :text`

            - `:text`

        - `class BetaManagedAgentsImageBlock`

          Image content specified directly as base64 data or as a reference via a URL.

          - `source: BetaManagedAgentsBase64ImageSource | BetaManagedAgentsURLImageSource | BetaManagedAgentsFileImageSource`

            Union type for image source variants.

            - `class BetaManagedAgentsBase64ImageSource`

              Base64-encoded image data.

              - `data: String`

                Base64-encoded image data.

              - `media_type: String`

                MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

              - `type: :base64`

                - `:base64`

            - `class BetaManagedAgentsURLImageSource`

              Image referenced by URL.

              - `type: :url`

                - `:url`

              - `url: String`

                URL of the image to fetch.

            - `class BetaManagedAgentsFileImageSource`

              Image referenced by file ID.

              - `file_id: String`

                ID of a previously uploaded file.

              - `type: :file`

                - `:file`

          - `type: :image`

            - `:image`

        - `class BetaManagedAgentsDocumentBlock`

          Document content, either specified directly as base64 data, as text, or as a reference via a URL.

          - `source: BetaManagedAgentsBase64DocumentSource | BetaManagedAgentsPlainTextDocumentSource | BetaManagedAgentsURLDocumentSource | BetaManagedAgentsFileDocumentSource`

            Union type for document source variants.

            - `class BetaManagedAgentsBase64DocumentSource`

              Base64-encoded document data.

              - `data: String`

                Base64-encoded document data.

              - `media_type: String`

                MIME type of the document (e.g., "application/pdf").

              - `type: :base64`

                - `:base64`

            - `class BetaManagedAgentsPlainTextDocumentSource`

              Plain text document content.

              - `data: String`

                The plain text content.

              - `media_type: :"text/plain"`

                MIME type of the text content. Must be "text/plain".

                - `:"text/plain"`

              - `type: :text`

                - `:text`

            - `class BetaManagedAgentsURLDocumentSource`

              Document referenced by URL.

              - `type: :url`

                - `:url`

              - `url: String`

                URL of the document to fetch.

            - `class BetaManagedAgentsFileDocumentSource`

              Document referenced by file ID.

              - `file_id: String`

                ID of a previously uploaded file.

              - `type: :file`

                - `:file`

          - `type: :document`

            - `:document`

          - `context: String`

            Additional context about the document for the model.

          - `title: String`

            The title of the document.

      - `type: :"user.message"`

        - `:"user.message"`

      - `processed_at: Time`

        A timestamp in RFC 3339 format

    - `class BetaManagedAgentsUserInterruptEvent`

      An interrupt event that pauses agent execution and returns control to the user.

      - `id: String`

        Unique identifier for this event.

      - `type: :"user.interrupt"`

        - `:"user.interrupt"`

      - `processed_at: Time`

        A timestamp in RFC 3339 format

    - `class BetaManagedAgentsUserToolConfirmationEvent`

      A tool confirmation event that approves or denies a pending tool execution.

      - `id: String`

        Unique identifier for this event.

      - `result: :allow | :deny`

        UserToolConfirmationResult enum

        - `:allow`

        - `:deny`

      - `tool_use_id: String`

        The id of the `agent.tool_use` or `agent.mcp_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

      - `type: :"user.tool_confirmation"`

        - `:"user.tool_confirmation"`

      - `deny_message: String`

        Optional message providing context for a 'deny' decision. Only allowed when result is 'deny'.

      - `processed_at: Time`

        A timestamp in RFC 3339 format

    - `class BetaManagedAgentsUserCustomToolResultEvent`

      Event sent by the client providing the result of a custom tool execution.

      - `id: String`

        Unique identifier for this event.

      - `custom_tool_use_id: String`

        The id of the `agent.custom_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

      - `type: :"user.custom_tool_result"`

        - `:"user.custom_tool_result"`

      - `content: Array[BetaManagedAgentsTextBlock | BetaManagedAgentsImageBlock | BetaManagedAgentsDocumentBlock]`

        The result content returned by the tool.

        - `class BetaManagedAgentsTextBlock`

          Regular text content.

          - `text: String`

            The text content.

          - `type: :text`

            - `:text`

        - `class BetaManagedAgentsImageBlock`

          Image content specified directly as base64 data or as a reference via a URL.

          - `source: BetaManagedAgentsBase64ImageSource | BetaManagedAgentsURLImageSource | BetaManagedAgentsFileImageSource`

            Union type for image source variants.

            - `class BetaManagedAgentsBase64ImageSource`

              Base64-encoded image data.

              - `data: String`

                Base64-encoded image data.

              - `media_type: String`

                MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

              - `type: :base64`

                - `:base64`

            - `class BetaManagedAgentsURLImageSource`

              Image referenced by URL.

              - `type: :url`

                - `:url`

              - `url: String`

                URL of the image to fetch.

            - `class BetaManagedAgentsFileImageSource`

              Image referenced by file ID.

              - `file_id: String`

                ID of a previously uploaded file.

              - `type: :file`

                - `:file`

          - `type: :image`

            - `:image`

        - `class BetaManagedAgentsDocumentBlock`

          Document content, either specified directly as base64 data, as text, or as a reference via a URL.

          - `source: BetaManagedAgentsBase64DocumentSource | BetaManagedAgentsPlainTextDocumentSource | BetaManagedAgentsURLDocumentSource | BetaManagedAgentsFileDocumentSource`

            Union type for document source variants.

            - `class BetaManagedAgentsBase64DocumentSource`

              Base64-encoded document data.

              - `data: String`

                Base64-encoded document data.

              - `media_type: String`

                MIME type of the document (e.g., "application/pdf").

              - `type: :base64`

                - `:base64`

            - `class BetaManagedAgentsPlainTextDocumentSource`

              Plain text document content.

              - `data: String`

                The plain text content.

              - `media_type: :"text/plain"`

                MIME type of the text content. Must be "text/plain".

                - `:"text/plain"`

              - `type: :text`

                - `:text`

            - `class BetaManagedAgentsURLDocumentSource`

              Document referenced by URL.

              - `type: :url`

                - `:url`

              - `url: String`

                URL of the document to fetch.

            - `class BetaManagedAgentsFileDocumentSource`

              Document referenced by file ID.

              - `file_id: String`

                ID of a previously uploaded file.

              - `type: :file`

                - `:file`

          - `type: :document`

            - `:document`

          - `context: String`

            Additional context about the document for the model.

          - `title: String`

            The title of the document.

      - `is_error: bool`

        Whether the tool execution resulted in an error.

      - `processed_at: Time`

        A timestamp in RFC 3339 format

### Beta Managed Agents Session Deleted Event

- `class BetaManagedAgentsSessionDeletedEvent`

  Emitted when a session has been deleted. Terminates any active event stream — no further events will be emitted for this session.

  - `id: String`

    Unique identifier for this event.

  - `processed_at: Time`

    A timestamp in RFC 3339 format

  - `type: :"session.deleted"`

    - `:"session.deleted"`

### Beta Managed Agents Session End Turn

- `class BetaManagedAgentsSessionEndTurn`

  The agent completed its turn naturally and is ready for the next user message.

  - `type: :end_turn`

    - `:end_turn`

### Beta Managed Agents Session Error Event

- `class BetaManagedAgentsSessionErrorEvent`

  An error event indicating a problem occurred during session execution.

  - `id: String`

    Unique identifier for this event.

  - `error: BetaManagedAgentsUnknownError | BetaManagedAgentsModelOverloadedError | BetaManagedAgentsModelRateLimitedError | 4 more`

    An unknown or unexpected error occurred during session execution. A fallback variant; clients that don't recognize a new error code can match on `retry_status` and `message` alone.

    - `class BetaManagedAgentsUnknownError`

      An unknown or unexpected error occurred during session execution. A fallback variant; clients that don't recognize a new error code can match on `retry_status` and `message` alone.

      - `message: String`

        Human-readable error description.

      - `retry_status: BetaManagedAgentsRetryStatusRetrying | BetaManagedAgentsRetryStatusExhausted | BetaManagedAgentsRetryStatusTerminal`

        What the client should do next in response to this error.

        - `class BetaManagedAgentsRetryStatusRetrying`

          The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

          - `type: :retrying`

            - `:retrying`

        - `class BetaManagedAgentsRetryStatusExhausted`

          This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

          - `type: :exhausted`

            - `:exhausted`

        - `class BetaManagedAgentsRetryStatusTerminal`

          The session encountered a terminal error and will transition to `terminated` state.

          - `type: :terminal`

            - `:terminal`

      - `type: :unknown_error`

        - `:unknown_error`

    - `class BetaManagedAgentsModelOverloadedError`

      The model is currently overloaded. Emitted after automatic retries are exhausted.

      - `message: String`

        Human-readable error description.

      - `retry_status: BetaManagedAgentsRetryStatusRetrying | BetaManagedAgentsRetryStatusExhausted | BetaManagedAgentsRetryStatusTerminal`

        What the client should do next in response to this error.

        - `class BetaManagedAgentsRetryStatusRetrying`

          The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

          - `type: :retrying`

            - `:retrying`

        - `class BetaManagedAgentsRetryStatusExhausted`

          This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

          - `type: :exhausted`

            - `:exhausted`

        - `class BetaManagedAgentsRetryStatusTerminal`

          The session encountered a terminal error and will transition to `terminated` state.

          - `type: :terminal`

            - `:terminal`

      - `type: :model_overloaded_error`

        - `:model_overloaded_error`

    - `class BetaManagedAgentsModelRateLimitedError`

      The model request was rate-limited.

      - `message: String`

        Human-readable error description.

      - `retry_status: BetaManagedAgentsRetryStatusRetrying | BetaManagedAgentsRetryStatusExhausted | BetaManagedAgentsRetryStatusTerminal`

        What the client should do next in response to this error.

        - `class BetaManagedAgentsRetryStatusRetrying`

          The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

          - `type: :retrying`

            - `:retrying`

        - `class BetaManagedAgentsRetryStatusExhausted`

          This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

          - `type: :exhausted`

            - `:exhausted`

        - `class BetaManagedAgentsRetryStatusTerminal`

          The session encountered a terminal error and will transition to `terminated` state.

          - `type: :terminal`

            - `:terminal`

      - `type: :model_rate_limited_error`

        - `:model_rate_limited_error`

    - `class BetaManagedAgentsModelRequestFailedError`

      A model request failed for a reason other than overload or rate-limiting.

      - `message: String`

        Human-readable error description.

      - `retry_status: BetaManagedAgentsRetryStatusRetrying | BetaManagedAgentsRetryStatusExhausted | BetaManagedAgentsRetryStatusTerminal`

        What the client should do next in response to this error.

        - `class BetaManagedAgentsRetryStatusRetrying`

          The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

          - `type: :retrying`

            - `:retrying`

        - `class BetaManagedAgentsRetryStatusExhausted`

          This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

          - `type: :exhausted`

            - `:exhausted`

        - `class BetaManagedAgentsRetryStatusTerminal`

          The session encountered a terminal error and will transition to `terminated` state.

          - `type: :terminal`

            - `:terminal`

      - `type: :model_request_failed_error`

        - `:model_request_failed_error`

    - `class BetaManagedAgentsMCPConnectionFailedError`

      Failed to connect to an MCP server.

      - `mcp_server_name: String`

        Name of the MCP server that failed to connect.

      - `message: String`

        Human-readable error description.

      - `retry_status: BetaManagedAgentsRetryStatusRetrying | BetaManagedAgentsRetryStatusExhausted | BetaManagedAgentsRetryStatusTerminal`

        What the client should do next in response to this error.

        - `class BetaManagedAgentsRetryStatusRetrying`

          The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

          - `type: :retrying`

            - `:retrying`

        - `class BetaManagedAgentsRetryStatusExhausted`

          This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

          - `type: :exhausted`

            - `:exhausted`

        - `class BetaManagedAgentsRetryStatusTerminal`

          The session encountered a terminal error and will transition to `terminated` state.

          - `type: :terminal`

            - `:terminal`

      - `type: :mcp_connection_failed_error`

        - `:mcp_connection_failed_error`

    - `class BetaManagedAgentsMCPAuthenticationFailedError`

      Authentication to an MCP server failed.

      - `mcp_server_name: String`

        Name of the MCP server that failed authentication.

      - `message: String`

        Human-readable error description.

      - `retry_status: BetaManagedAgentsRetryStatusRetrying | BetaManagedAgentsRetryStatusExhausted | BetaManagedAgentsRetryStatusTerminal`

        What the client should do next in response to this error.

        - `class BetaManagedAgentsRetryStatusRetrying`

          The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

          - `type: :retrying`

            - `:retrying`

        - `class BetaManagedAgentsRetryStatusExhausted`

          This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

          - `type: :exhausted`

            - `:exhausted`

        - `class BetaManagedAgentsRetryStatusTerminal`

          The session encountered a terminal error and will transition to `terminated` state.

          - `type: :terminal`

            - `:terminal`

      - `type: :mcp_authentication_failed_error`

        - `:mcp_authentication_failed_error`

    - `class BetaManagedAgentsBillingError`

      The caller's organization or workspace cannot make model requests — out of credits or spend limit reached. Retrying with the same credentials will not succeed; the caller must resolve the billing state.

      - `message: String`

        Human-readable error description.

      - `retry_status: BetaManagedAgentsRetryStatusRetrying | BetaManagedAgentsRetryStatusExhausted | BetaManagedAgentsRetryStatusTerminal`

        What the client should do next in response to this error.

        - `class BetaManagedAgentsRetryStatusRetrying`

          The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

          - `type: :retrying`

            - `:retrying`

        - `class BetaManagedAgentsRetryStatusExhausted`

          This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

          - `type: :exhausted`

            - `:exhausted`

        - `class BetaManagedAgentsRetryStatusTerminal`

          The session encountered a terminal error and will transition to `terminated` state.

          - `type: :terminal`

            - `:terminal`

      - `type: :billing_error`

        - `:billing_error`

  - `processed_at: Time`

    A timestamp in RFC 3339 format

  - `type: :"session.error"`

    - `:"session.error"`

### Beta Managed Agents Session Event

- `BetaManagedAgentsSessionEvent = BetaManagedAgentsUserMessageEvent | BetaManagedAgentsUserInterruptEvent | BetaManagedAgentsUserToolConfirmationEvent | 17 more`

  Union type for all event types in a session.

  - `class BetaManagedAgentsUserMessageEvent`

    A user message event in the session conversation.

    - `id: String`

      Unique identifier for this event.

    - `content: Array[BetaManagedAgentsTextBlock | BetaManagedAgentsImageBlock | BetaManagedAgentsDocumentBlock]`

      Array of content blocks comprising the user message.

      - `class BetaManagedAgentsTextBlock`

        Regular text content.

        - `text: String`

          The text content.

        - `type: :text`

          - `:text`

      - `class BetaManagedAgentsImageBlock`

        Image content specified directly as base64 data or as a reference via a URL.

        - `source: BetaManagedAgentsBase64ImageSource | BetaManagedAgentsURLImageSource | BetaManagedAgentsFileImageSource`

          Union type for image source variants.

          - `class BetaManagedAgentsBase64ImageSource`

            Base64-encoded image data.

            - `data: String`

              Base64-encoded image data.

            - `media_type: String`

              MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

            - `type: :base64`

              - `:base64`

          - `class BetaManagedAgentsURLImageSource`

            Image referenced by URL.

            - `type: :url`

              - `:url`

            - `url: String`

              URL of the image to fetch.

          - `class BetaManagedAgentsFileImageSource`

            Image referenced by file ID.

            - `file_id: String`

              ID of a previously uploaded file.

            - `type: :file`

              - `:file`

        - `type: :image`

          - `:image`

      - `class BetaManagedAgentsDocumentBlock`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

        - `source: BetaManagedAgentsBase64DocumentSource | BetaManagedAgentsPlainTextDocumentSource | BetaManagedAgentsURLDocumentSource | BetaManagedAgentsFileDocumentSource`

          Union type for document source variants.

          - `class BetaManagedAgentsBase64DocumentSource`

            Base64-encoded document data.

            - `data: String`

              Base64-encoded document data.

            - `media_type: String`

              MIME type of the document (e.g., "application/pdf").

            - `type: :base64`

              - `:base64`

          - `class BetaManagedAgentsPlainTextDocumentSource`

            Plain text document content.

            - `data: String`

              The plain text content.

            - `media_type: :"text/plain"`

              MIME type of the text content. Must be "text/plain".

              - `:"text/plain"`

            - `type: :text`

              - `:text`

          - `class BetaManagedAgentsURLDocumentSource`

            Document referenced by URL.

            - `type: :url`

              - `:url`

            - `url: String`

              URL of the document to fetch.

          - `class BetaManagedAgentsFileDocumentSource`

            Document referenced by file ID.

            - `file_id: String`

              ID of a previously uploaded file.

            - `type: :file`

              - `:file`

        - `type: :document`

          - `:document`

        - `context: String`

          Additional context about the document for the model.

        - `title: String`

          The title of the document.

    - `type: :"user.message"`

      - `:"user.message"`

    - `processed_at: Time`

      A timestamp in RFC 3339 format

  - `class BetaManagedAgentsUserInterruptEvent`

    An interrupt event that pauses agent execution and returns control to the user.

    - `id: String`

      Unique identifier for this event.

    - `type: :"user.interrupt"`

      - `:"user.interrupt"`

    - `processed_at: Time`

      A timestamp in RFC 3339 format

  - `class BetaManagedAgentsUserToolConfirmationEvent`

    A tool confirmation event that approves or denies a pending tool execution.

    - `id: String`

      Unique identifier for this event.

    - `result: :allow | :deny`

      UserToolConfirmationResult enum

      - `:allow`

      - `:deny`

    - `tool_use_id: String`

      The id of the `agent.tool_use` or `agent.mcp_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

    - `type: :"user.tool_confirmation"`

      - `:"user.tool_confirmation"`

    - `deny_message: String`

      Optional message providing context for a 'deny' decision. Only allowed when result is 'deny'.

    - `processed_at: Time`

      A timestamp in RFC 3339 format

  - `class BetaManagedAgentsUserCustomToolResultEvent`

    Event sent by the client providing the result of a custom tool execution.

    - `id: String`

      Unique identifier for this event.

    - `custom_tool_use_id: String`

      The id of the `agent.custom_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

    - `type: :"user.custom_tool_result"`

      - `:"user.custom_tool_result"`

    - `content: Array[BetaManagedAgentsTextBlock | BetaManagedAgentsImageBlock | BetaManagedAgentsDocumentBlock]`

      The result content returned by the tool.

      - `class BetaManagedAgentsTextBlock`

        Regular text content.

        - `text: String`

          The text content.

        - `type: :text`

          - `:text`

      - `class BetaManagedAgentsImageBlock`

        Image content specified directly as base64 data or as a reference via a URL.

        - `source: BetaManagedAgentsBase64ImageSource | BetaManagedAgentsURLImageSource | BetaManagedAgentsFileImageSource`

          Union type for image source variants.

          - `class BetaManagedAgentsBase64ImageSource`

            Base64-encoded image data.

            - `data: String`

              Base64-encoded image data.

            - `media_type: String`

              MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

            - `type: :base64`

              - `:base64`

          - `class BetaManagedAgentsURLImageSource`

            Image referenced by URL.

            - `type: :url`

              - `:url`

            - `url: String`

              URL of the image to fetch.

          - `class BetaManagedAgentsFileImageSource`

            Image referenced by file ID.

            - `file_id: String`

              ID of a previously uploaded file.

            - `type: :file`

              - `:file`

        - `type: :image`

          - `:image`

      - `class BetaManagedAgentsDocumentBlock`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

        - `source: BetaManagedAgentsBase64DocumentSource | BetaManagedAgentsPlainTextDocumentSource | BetaManagedAgentsURLDocumentSource | BetaManagedAgentsFileDocumentSource`

          Union type for document source variants.

          - `class BetaManagedAgentsBase64DocumentSource`

            Base64-encoded document data.

            - `data: String`

              Base64-encoded document data.

            - `media_type: String`

              MIME type of the document (e.g., "application/pdf").

            - `type: :base64`

              - `:base64`

          - `class BetaManagedAgentsPlainTextDocumentSource`

            Plain text document content.

            - `data: String`

              The plain text content.

            - `media_type: :"text/plain"`

              MIME type of the text content. Must be "text/plain".

              - `:"text/plain"`

            - `type: :text`

              - `:text`

          - `class BetaManagedAgentsURLDocumentSource`

            Document referenced by URL.

            - `type: :url`

              - `:url`

            - `url: String`

              URL of the document to fetch.

          - `class BetaManagedAgentsFileDocumentSource`

            Document referenced by file ID.

            - `file_id: String`

              ID of a previously uploaded file.

            - `type: :file`

              - `:file`

        - `type: :document`

          - `:document`

        - `context: String`

          Additional context about the document for the model.

        - `title: String`

          The title of the document.

    - `is_error: bool`

      Whether the tool execution resulted in an error.

    - `processed_at: Time`

      A timestamp in RFC 3339 format

  - `class BetaManagedAgentsAgentCustomToolUseEvent`

    Event emitted when the agent calls a custom tool. The session goes idle until the client sends a `user.custom_tool_result` event with the result.

    - `id: String`

      Unique identifier for this event.

    - `input: Hash[Symbol, untyped]`

      Input parameters for the tool call.

    - `name: String`

      Name of the custom tool being called.

    - `processed_at: Time`

      A timestamp in RFC 3339 format

    - `type: :"agent.custom_tool_use"`

      - `:"agent.custom_tool_use"`

  - `class BetaManagedAgentsAgentMessageEvent`

    An agent response event in the session conversation.

    - `id: String`

      Unique identifier for this event.

    - `content: Array[BetaManagedAgentsTextBlock]`

      Array of text blocks comprising the agent response.

      - `text: String`

        The text content.

      - `type: :text`

        - `:text`

    - `processed_at: Time`

      A timestamp in RFC 3339 format

    - `type: :"agent.message"`

      - `:"agent.message"`

  - `class BetaManagedAgentsAgentThinkingEvent`

    Indicates the agent is making forward progress via extended thinking. A progress signal, not a content carrier.

    - `id: String`

      Unique identifier for this event.

    - `processed_at: Time`

      A timestamp in RFC 3339 format

    - `type: :"agent.thinking"`

      - `:"agent.thinking"`

  - `class BetaManagedAgentsAgentMCPToolUseEvent`

    Event emitted when the agent invokes a tool provided by an MCP server.

    - `id: String`

      Unique identifier for this event.

    - `input: Hash[Symbol, untyped]`

      Input parameters for the tool call.

    - `mcp_server_name: String`

      Name of the MCP server providing the tool.

    - `name: String`

      Name of the MCP tool being used.

    - `processed_at: Time`

      A timestamp in RFC 3339 format

    - `type: :"agent.mcp_tool_use"`

      - `:"agent.mcp_tool_use"`

    - `evaluated_permission: :allow | :ask | :deny`

      AgentEvaluatedPermission enum

      - `:allow`

      - `:ask`

      - `:deny`

  - `class BetaManagedAgentsAgentMCPToolResultEvent`

    Event representing the result of an MCP tool execution.

    - `id: String`

      Unique identifier for this event.

    - `mcp_tool_use_id: String`

      The id of the `agent.mcp_tool_use` event this result corresponds to.

    - `processed_at: Time`

      A timestamp in RFC 3339 format

    - `type: :"agent.mcp_tool_result"`

      - `:"agent.mcp_tool_result"`

    - `content: Array[BetaManagedAgentsTextBlock | BetaManagedAgentsImageBlock | BetaManagedAgentsDocumentBlock]`

      The result content returned by the tool.

      - `class BetaManagedAgentsTextBlock`

        Regular text content.

        - `text: String`

          The text content.

        - `type: :text`

          - `:text`

      - `class BetaManagedAgentsImageBlock`

        Image content specified directly as base64 data or as a reference via a URL.

        - `source: BetaManagedAgentsBase64ImageSource | BetaManagedAgentsURLImageSource | BetaManagedAgentsFileImageSource`

          Union type for image source variants.

          - `class BetaManagedAgentsBase64ImageSource`

            Base64-encoded image data.

            - `data: String`

              Base64-encoded image data.

            - `media_type: String`

              MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

            - `type: :base64`

              - `:base64`

          - `class BetaManagedAgentsURLImageSource`

            Image referenced by URL.

            - `type: :url`

              - `:url`

            - `url: String`

              URL of the image to fetch.

          - `class BetaManagedAgentsFileImageSource`

            Image referenced by file ID.

            - `file_id: String`

              ID of a previously uploaded file.

            - `type: :file`

              - `:file`

        - `type: :image`

          - `:image`

      - `class BetaManagedAgentsDocumentBlock`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

        - `source: BetaManagedAgentsBase64DocumentSource | BetaManagedAgentsPlainTextDocumentSource | BetaManagedAgentsURLDocumentSource | BetaManagedAgentsFileDocumentSource`

          Union type for document source variants.

          - `class BetaManagedAgentsBase64DocumentSource`

            Base64-encoded document data.

            - `data: String`

              Base64-encoded document data.

            - `media_type: String`

              MIME type of the document (e.g., "application/pdf").

            - `type: :base64`

              - `:base64`

          - `class BetaManagedAgentsPlainTextDocumentSource`

            Plain text document content.

            - `data: String`

              The plain text content.

            - `media_type: :"text/plain"`

              MIME type of the text content. Must be "text/plain".

              - `:"text/plain"`

            - `type: :text`

              - `:text`

          - `class BetaManagedAgentsURLDocumentSource`

            Document referenced by URL.

            - `type: :url`

              - `:url`

            - `url: String`

              URL of the document to fetch.

          - `class BetaManagedAgentsFileDocumentSource`

            Document referenced by file ID.

            - `file_id: String`

              ID of a previously uploaded file.

            - `type: :file`

              - `:file`

        - `type: :document`

          - `:document`

        - `context: String`

          Additional context about the document for the model.

        - `title: String`

          The title of the document.

    - `is_error: bool`

      Whether the tool execution resulted in an error.

  - `class BetaManagedAgentsAgentToolUseEvent`

    Event emitted when the agent invokes a built-in agent tool.

    - `id: String`

      Unique identifier for this event.

    - `input: Hash[Symbol, untyped]`

      Input parameters for the tool call.

    - `name: String`

      Name of the agent tool being used.

    - `processed_at: Time`

      A timestamp in RFC 3339 format

    - `type: :"agent.tool_use"`

      - `:"agent.tool_use"`

    - `evaluated_permission: :allow | :ask | :deny`

      AgentEvaluatedPermission enum

      - `:allow`

      - `:ask`

      - `:deny`

  - `class BetaManagedAgentsAgentToolResultEvent`

    Event representing the result of an agent tool execution.

    - `id: String`

      Unique identifier for this event.

    - `processed_at: Time`

      A timestamp in RFC 3339 format

    - `tool_use_id: String`

      The id of the `agent.tool_use` event this result corresponds to.

    - `type: :"agent.tool_result"`

      - `:"agent.tool_result"`

    - `content: Array[BetaManagedAgentsTextBlock | BetaManagedAgentsImageBlock | BetaManagedAgentsDocumentBlock]`

      The result content returned by the tool.

      - `class BetaManagedAgentsTextBlock`

        Regular text content.

        - `text: String`

          The text content.

        - `type: :text`

          - `:text`

      - `class BetaManagedAgentsImageBlock`

        Image content specified directly as base64 data or as a reference via a URL.

        - `source: BetaManagedAgentsBase64ImageSource | BetaManagedAgentsURLImageSource | BetaManagedAgentsFileImageSource`

          Union type for image source variants.

          - `class BetaManagedAgentsBase64ImageSource`

            Base64-encoded image data.

            - `data: String`

              Base64-encoded image data.

            - `media_type: String`

              MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

            - `type: :base64`

              - `:base64`

          - `class BetaManagedAgentsURLImageSource`

            Image referenced by URL.

            - `type: :url`

              - `:url`

            - `url: String`

              URL of the image to fetch.

          - `class BetaManagedAgentsFileImageSource`

            Image referenced by file ID.

            - `file_id: String`

              ID of a previously uploaded file.

            - `type: :file`

              - `:file`

        - `type: :image`

          - `:image`

      - `class BetaManagedAgentsDocumentBlock`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

        - `source: BetaManagedAgentsBase64DocumentSource | BetaManagedAgentsPlainTextDocumentSource | BetaManagedAgentsURLDocumentSource | BetaManagedAgentsFileDocumentSource`

          Union type for document source variants.

          - `class BetaManagedAgentsBase64DocumentSource`

            Base64-encoded document data.

            - `data: String`

              Base64-encoded document data.

            - `media_type: String`

              MIME type of the document (e.g., "application/pdf").

            - `type: :base64`

              - `:base64`

          - `class BetaManagedAgentsPlainTextDocumentSource`

            Plain text document content.

            - `data: String`

              The plain text content.

            - `media_type: :"text/plain"`

              MIME type of the text content. Must be "text/plain".

              - `:"text/plain"`

            - `type: :text`

              - `:text`

          - `class BetaManagedAgentsURLDocumentSource`

            Document referenced by URL.

            - `type: :url`

              - `:url`

            - `url: String`

              URL of the document to fetch.

          - `class BetaManagedAgentsFileDocumentSource`

            Document referenced by file ID.

            - `file_id: String`

              ID of a previously uploaded file.

            - `type: :file`

              - `:file`

        - `type: :document`

          - `:document`

        - `context: String`

          Additional context about the document for the model.

        - `title: String`

          The title of the document.

    - `is_error: bool`

      Whether the tool execution resulted in an error.

  - `class BetaManagedAgentsAgentThreadContextCompactedEvent`

    Indicates that context compaction (summarization) occurred during the session.

    - `id: String`

      Unique identifier for this event.

    - `processed_at: Time`

      A timestamp in RFC 3339 format

    - `type: :"agent.thread_context_compacted"`

      - `:"agent.thread_context_compacted"`

  - `class BetaManagedAgentsSessionErrorEvent`

    An error event indicating a problem occurred during session execution.

    - `id: String`

      Unique identifier for this event.

    - `error: BetaManagedAgentsUnknownError | BetaManagedAgentsModelOverloadedError | BetaManagedAgentsModelRateLimitedError | 4 more`

      An unknown or unexpected error occurred during session execution. A fallback variant; clients that don't recognize a new error code can match on `retry_status` and `message` alone.

      - `class BetaManagedAgentsUnknownError`

        An unknown or unexpected error occurred during session execution. A fallback variant; clients that don't recognize a new error code can match on `retry_status` and `message` alone.

        - `message: String`

          Human-readable error description.

        - `retry_status: BetaManagedAgentsRetryStatusRetrying | BetaManagedAgentsRetryStatusExhausted | BetaManagedAgentsRetryStatusTerminal`

          What the client should do next in response to this error.

          - `class BetaManagedAgentsRetryStatusRetrying`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

            - `type: :retrying`

              - `:retrying`

          - `class BetaManagedAgentsRetryStatusExhausted`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

            - `type: :exhausted`

              - `:exhausted`

          - `class BetaManagedAgentsRetryStatusTerminal`

            The session encountered a terminal error and will transition to `terminated` state.

            - `type: :terminal`

              - `:terminal`

        - `type: :unknown_error`

          - `:unknown_error`

      - `class BetaManagedAgentsModelOverloadedError`

        The model is currently overloaded. Emitted after automatic retries are exhausted.

        - `message: String`

          Human-readable error description.

        - `retry_status: BetaManagedAgentsRetryStatusRetrying | BetaManagedAgentsRetryStatusExhausted | BetaManagedAgentsRetryStatusTerminal`

          What the client should do next in response to this error.

          - `class BetaManagedAgentsRetryStatusRetrying`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

            - `type: :retrying`

              - `:retrying`

          - `class BetaManagedAgentsRetryStatusExhausted`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

            - `type: :exhausted`

              - `:exhausted`

          - `class BetaManagedAgentsRetryStatusTerminal`

            The session encountered a terminal error and will transition to `terminated` state.

            - `type: :terminal`

              - `:terminal`

        - `type: :model_overloaded_error`

          - `:model_overloaded_error`

      - `class BetaManagedAgentsModelRateLimitedError`

        The model request was rate-limited.

        - `message: String`

          Human-readable error description.

        - `retry_status: BetaManagedAgentsRetryStatusRetrying | BetaManagedAgentsRetryStatusExhausted | BetaManagedAgentsRetryStatusTerminal`

          What the client should do next in response to this error.

          - `class BetaManagedAgentsRetryStatusRetrying`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

            - `type: :retrying`

              - `:retrying`

          - `class BetaManagedAgentsRetryStatusExhausted`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

            - `type: :exhausted`

              - `:exhausted`

          - `class BetaManagedAgentsRetryStatusTerminal`

            The session encountered a terminal error and will transition to `terminated` state.

            - `type: :terminal`

              - `:terminal`

        - `type: :model_rate_limited_error`

          - `:model_rate_limited_error`

      - `class BetaManagedAgentsModelRequestFailedError`

        A model request failed for a reason other than overload or rate-limiting.

        - `message: String`

          Human-readable error description.

        - `retry_status: BetaManagedAgentsRetryStatusRetrying | BetaManagedAgentsRetryStatusExhausted | BetaManagedAgentsRetryStatusTerminal`

          What the client should do next in response to this error.

          - `class BetaManagedAgentsRetryStatusRetrying`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

            - `type: :retrying`

              - `:retrying`

          - `class BetaManagedAgentsRetryStatusExhausted`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

            - `type: :exhausted`

              - `:exhausted`

          - `class BetaManagedAgentsRetryStatusTerminal`

            The session encountered a terminal error and will transition to `terminated` state.

            - `type: :terminal`

              - `:terminal`

        - `type: :model_request_failed_error`

          - `:model_request_failed_error`

      - `class BetaManagedAgentsMCPConnectionFailedError`

        Failed to connect to an MCP server.

        - `mcp_server_name: String`

          Name of the MCP server that failed to connect.

        - `message: String`

          Human-readable error description.

        - `retry_status: BetaManagedAgentsRetryStatusRetrying | BetaManagedAgentsRetryStatusExhausted | BetaManagedAgentsRetryStatusTerminal`

          What the client should do next in response to this error.

          - `class BetaManagedAgentsRetryStatusRetrying`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

            - `type: :retrying`

              - `:retrying`

          - `class BetaManagedAgentsRetryStatusExhausted`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

            - `type: :exhausted`

              - `:exhausted`

          - `class BetaManagedAgentsRetryStatusTerminal`

            The session encountered a terminal error and will transition to `terminated` state.

            - `type: :terminal`

              - `:terminal`

        - `type: :mcp_connection_failed_error`

          - `:mcp_connection_failed_error`

      - `class BetaManagedAgentsMCPAuthenticationFailedError`

        Authentication to an MCP server failed.

        - `mcp_server_name: String`

          Name of the MCP server that failed authentication.

        - `message: String`

          Human-readable error description.

        - `retry_status: BetaManagedAgentsRetryStatusRetrying | BetaManagedAgentsRetryStatusExhausted | BetaManagedAgentsRetryStatusTerminal`

          What the client should do next in response to this error.

          - `class BetaManagedAgentsRetryStatusRetrying`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

            - `type: :retrying`

              - `:retrying`

          - `class BetaManagedAgentsRetryStatusExhausted`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

            - `type: :exhausted`

              - `:exhausted`

          - `class BetaManagedAgentsRetryStatusTerminal`

            The session encountered a terminal error and will transition to `terminated` state.

            - `type: :terminal`

              - `:terminal`

        - `type: :mcp_authentication_failed_error`

          - `:mcp_authentication_failed_error`

      - `class BetaManagedAgentsBillingError`

        The caller's organization or workspace cannot make model requests — out of credits or spend limit reached. Retrying with the same credentials will not succeed; the caller must resolve the billing state.

        - `message: String`

          Human-readable error description.

        - `retry_status: BetaManagedAgentsRetryStatusRetrying | BetaManagedAgentsRetryStatusExhausted | BetaManagedAgentsRetryStatusTerminal`

          What the client should do next in response to this error.

          - `class BetaManagedAgentsRetryStatusRetrying`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

            - `type: :retrying`

              - `:retrying`

          - `class BetaManagedAgentsRetryStatusExhausted`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

            - `type: :exhausted`

              - `:exhausted`

          - `class BetaManagedAgentsRetryStatusTerminal`

            The session encountered a terminal error and will transition to `terminated` state.

            - `type: :terminal`

              - `:terminal`

        - `type: :billing_error`

          - `:billing_error`

    - `processed_at: Time`

      A timestamp in RFC 3339 format

    - `type: :"session.error"`

      - `:"session.error"`

  - `class BetaManagedAgentsSessionStatusRescheduledEvent`

    Indicates the session is recovering from an error state and is rescheduled for execution.

    - `id: String`

      Unique identifier for this event.

    - `processed_at: Time`

      A timestamp in RFC 3339 format

    - `type: :"session.status_rescheduled"`

      - `:"session.status_rescheduled"`

  - `class BetaManagedAgentsSessionStatusRunningEvent`

    Indicates the session is actively running and the agent is working.

    - `id: String`

      Unique identifier for this event.

    - `processed_at: Time`

      A timestamp in RFC 3339 format

    - `type: :"session.status_running"`

      - `:"session.status_running"`

  - `class BetaManagedAgentsSessionStatusIdleEvent`

    Indicates the agent has paused and is awaiting user input.

    - `id: String`

      Unique identifier for this event.

    - `processed_at: Time`

      A timestamp in RFC 3339 format

    - `stop_reason: BetaManagedAgentsSessionEndTurn | BetaManagedAgentsSessionRequiresAction | BetaManagedAgentsSessionRetriesExhausted`

      The agent completed its turn naturally and is ready for the next user message.

      - `class BetaManagedAgentsSessionEndTurn`

        The agent completed its turn naturally and is ready for the next user message.

        - `type: :end_turn`

          - `:end_turn`

      - `class BetaManagedAgentsSessionRequiresAction`

        The agent is idle waiting on one or more blocking user-input events (tool confirmation, custom tool result, etc.). Resolving all of them transitions the session back to running.

        - `event_ids: Array[String]`

          The ids of events the agent is blocked on. Resolving fewer than all re-emits `session.status_idle` with the remainder.

        - `type: :requires_action`

          - `:requires_action`

      - `class BetaManagedAgentsSessionRetriesExhausted`

        The turn ended because the retry budget was exhausted (`max_iterations` hit or an error escalated to `retry_status: 'exhausted'`).

        - `type: :retries_exhausted`

          - `:retries_exhausted`

    - `type: :"session.status_idle"`

      - `:"session.status_idle"`

  - `class BetaManagedAgentsSessionStatusTerminatedEvent`

    Indicates the session has terminated, either due to an error or completion.

    - `id: String`

      Unique identifier for this event.

    - `processed_at: Time`

      A timestamp in RFC 3339 format

    - `type: :"session.status_terminated"`

      - `:"session.status_terminated"`

  - `class BetaManagedAgentsSpanModelRequestStartEvent`

    Emitted when a model request is initiated by the agent.

    - `id: String`

      Unique identifier for this event.

    - `processed_at: Time`

      A timestamp in RFC 3339 format

    - `type: :"span.model_request_start"`

      - `:"span.model_request_start"`

  - `class BetaManagedAgentsSpanModelRequestEndEvent`

    Emitted when a model request completes.

    - `id: String`

      Unique identifier for this event.

    - `is_error: bool`

      Whether the model request resulted in an error.

    - `model_request_start_id: String`

      The id of the corresponding `span.model_request_start` event.

    - `model_usage: BetaManagedAgentsSpanModelUsage`

      Token usage for a single model request.

      - `cache_creation_input_tokens: Integer`

        Tokens used to create prompt cache in this request.

      - `cache_read_input_tokens: Integer`

        Tokens read from prompt cache in this request.

      - `input_tokens: Integer`

        Input tokens consumed by this request.

      - `output_tokens: Integer`

        Output tokens generated by this request.

      - `speed: :standard | :fast`

        Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

        - `:standard`

        - `:fast`

    - `processed_at: Time`

      A timestamp in RFC 3339 format

    - `type: :"span.model_request_end"`

      - `:"span.model_request_end"`

  - `class BetaManagedAgentsSessionDeletedEvent`

    Emitted when a session has been deleted. Terminates any active event stream — no further events will be emitted for this session.

    - `id: String`

      Unique identifier for this event.

    - `processed_at: Time`

      A timestamp in RFC 3339 format

    - `type: :"session.deleted"`

      - `:"session.deleted"`

### Beta Managed Agents Session Requires Action

- `class BetaManagedAgentsSessionRequiresAction`

  The agent is idle waiting on one or more blocking user-input events (tool confirmation, custom tool result, etc.). Resolving all of them transitions the session back to running.

  - `event_ids: Array[String]`

    The ids of events the agent is blocked on. Resolving fewer than all re-emits `session.status_idle` with the remainder.

  - `type: :requires_action`

    - `:requires_action`

### Beta Managed Agents Session Retries Exhausted

- `class BetaManagedAgentsSessionRetriesExhausted`

  The turn ended because the retry budget was exhausted (`max_iterations` hit or an error escalated to `retry_status: 'exhausted'`).

  - `type: :retries_exhausted`

    - `:retries_exhausted`

### Beta Managed Agents Session Status Idle Event

- `class BetaManagedAgentsSessionStatusIdleEvent`

  Indicates the agent has paused and is awaiting user input.

  - `id: String`

    Unique identifier for this event.

  - `processed_at: Time`

    A timestamp in RFC 3339 format

  - `stop_reason: BetaManagedAgentsSessionEndTurn | BetaManagedAgentsSessionRequiresAction | BetaManagedAgentsSessionRetriesExhausted`

    The agent completed its turn naturally and is ready for the next user message.

    - `class BetaManagedAgentsSessionEndTurn`

      The agent completed its turn naturally and is ready for the next user message.

      - `type: :end_turn`

        - `:end_turn`

    - `class BetaManagedAgentsSessionRequiresAction`

      The agent is idle waiting on one or more blocking user-input events (tool confirmation, custom tool result, etc.). Resolving all of them transitions the session back to running.

      - `event_ids: Array[String]`

        The ids of events the agent is blocked on. Resolving fewer than all re-emits `session.status_idle` with the remainder.

      - `type: :requires_action`

        - `:requires_action`

    - `class BetaManagedAgentsSessionRetriesExhausted`

      The turn ended because the retry budget was exhausted (`max_iterations` hit or an error escalated to `retry_status: 'exhausted'`).

      - `type: :retries_exhausted`

        - `:retries_exhausted`

  - `type: :"session.status_idle"`

    - `:"session.status_idle"`

### Beta Managed Agents Session Status Rescheduled Event

- `class BetaManagedAgentsSessionStatusRescheduledEvent`

  Indicates the session is recovering from an error state and is rescheduled for execution.

  - `id: String`

    Unique identifier for this event.

  - `processed_at: Time`

    A timestamp in RFC 3339 format

  - `type: :"session.status_rescheduled"`

    - `:"session.status_rescheduled"`

### Beta Managed Agents Session Status Running Event

- `class BetaManagedAgentsSessionStatusRunningEvent`

  Indicates the session is actively running and the agent is working.

  - `id: String`

    Unique identifier for this event.

  - `processed_at: Time`

    A timestamp in RFC 3339 format

  - `type: :"session.status_running"`

    - `:"session.status_running"`

### Beta Managed Agents Session Status Terminated Event

- `class BetaManagedAgentsSessionStatusTerminatedEvent`

  Indicates the session has terminated, either due to an error or completion.

  - `id: String`

    Unique identifier for this event.

  - `processed_at: Time`

    A timestamp in RFC 3339 format

  - `type: :"session.status_terminated"`

    - `:"session.status_terminated"`

### Beta Managed Agents Span Model Request End Event

- `class BetaManagedAgentsSpanModelRequestEndEvent`

  Emitted when a model request completes.

  - `id: String`

    Unique identifier for this event.

  - `is_error: bool`

    Whether the model request resulted in an error.

  - `model_request_start_id: String`

    The id of the corresponding `span.model_request_start` event.

  - `model_usage: BetaManagedAgentsSpanModelUsage`

    Token usage for a single model request.

    - `cache_creation_input_tokens: Integer`

      Tokens used to create prompt cache in this request.

    - `cache_read_input_tokens: Integer`

      Tokens read from prompt cache in this request.

    - `input_tokens: Integer`

      Input tokens consumed by this request.

    - `output_tokens: Integer`

      Output tokens generated by this request.

    - `speed: :standard | :fast`

      Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

      - `:standard`

      - `:fast`

  - `processed_at: Time`

    A timestamp in RFC 3339 format

  - `type: :"span.model_request_end"`

    - `:"span.model_request_end"`

### Beta Managed Agents Span Model Request Start Event

- `class BetaManagedAgentsSpanModelRequestStartEvent`

  Emitted when a model request is initiated by the agent.

  - `id: String`

    Unique identifier for this event.

  - `processed_at: Time`

    A timestamp in RFC 3339 format

  - `type: :"span.model_request_start"`

    - `:"span.model_request_start"`

### Beta Managed Agents Span Model Usage

- `class BetaManagedAgentsSpanModelUsage`

  Token usage for a single model request.

  - `cache_creation_input_tokens: Integer`

    Tokens used to create prompt cache in this request.

  - `cache_read_input_tokens: Integer`

    Tokens read from prompt cache in this request.

  - `input_tokens: Integer`

    Input tokens consumed by this request.

  - `output_tokens: Integer`

    Output tokens generated by this request.

  - `speed: :standard | :fast`

    Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

    - `:standard`

    - `:fast`

### Beta Managed Agents Stream Session Events

- `BetaManagedAgentsStreamSessionEvents = BetaManagedAgentsUserMessageEvent | BetaManagedAgentsUserInterruptEvent | BetaManagedAgentsUserToolConfirmationEvent | 17 more`

  Server-sent event in the session stream.

  - `class BetaManagedAgentsUserMessageEvent`

    A user message event in the session conversation.

    - `id: String`

      Unique identifier for this event.

    - `content: Array[BetaManagedAgentsTextBlock | BetaManagedAgentsImageBlock | BetaManagedAgentsDocumentBlock]`

      Array of content blocks comprising the user message.

      - `class BetaManagedAgentsTextBlock`

        Regular text content.

        - `text: String`

          The text content.

        - `type: :text`

          - `:text`

      - `class BetaManagedAgentsImageBlock`

        Image content specified directly as base64 data or as a reference via a URL.

        - `source: BetaManagedAgentsBase64ImageSource | BetaManagedAgentsURLImageSource | BetaManagedAgentsFileImageSource`

          Union type for image source variants.

          - `class BetaManagedAgentsBase64ImageSource`

            Base64-encoded image data.

            - `data: String`

              Base64-encoded image data.

            - `media_type: String`

              MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

            - `type: :base64`

              - `:base64`

          - `class BetaManagedAgentsURLImageSource`

            Image referenced by URL.

            - `type: :url`

              - `:url`

            - `url: String`

              URL of the image to fetch.

          - `class BetaManagedAgentsFileImageSource`

            Image referenced by file ID.

            - `file_id: String`

              ID of a previously uploaded file.

            - `type: :file`

              - `:file`

        - `type: :image`

          - `:image`

      - `class BetaManagedAgentsDocumentBlock`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

        - `source: BetaManagedAgentsBase64DocumentSource | BetaManagedAgentsPlainTextDocumentSource | BetaManagedAgentsURLDocumentSource | BetaManagedAgentsFileDocumentSource`

          Union type for document source variants.

          - `class BetaManagedAgentsBase64DocumentSource`

            Base64-encoded document data.

            - `data: String`

              Base64-encoded document data.

            - `media_type: String`

              MIME type of the document (e.g., "application/pdf").

            - `type: :base64`

              - `:base64`

          - `class BetaManagedAgentsPlainTextDocumentSource`

            Plain text document content.

            - `data: String`

              The plain text content.

            - `media_type: :"text/plain"`

              MIME type of the text content. Must be "text/plain".

              - `:"text/plain"`

            - `type: :text`

              - `:text`

          - `class BetaManagedAgentsURLDocumentSource`

            Document referenced by URL.

            - `type: :url`

              - `:url`

            - `url: String`

              URL of the document to fetch.

          - `class BetaManagedAgentsFileDocumentSource`

            Document referenced by file ID.

            - `file_id: String`

              ID of a previously uploaded file.

            - `type: :file`

              - `:file`

        - `type: :document`

          - `:document`

        - `context: String`

          Additional context about the document for the model.

        - `title: String`

          The title of the document.

    - `type: :"user.message"`

      - `:"user.message"`

    - `processed_at: Time`

      A timestamp in RFC 3339 format

  - `class BetaManagedAgentsUserInterruptEvent`

    An interrupt event that pauses agent execution and returns control to the user.

    - `id: String`

      Unique identifier for this event.

    - `type: :"user.interrupt"`

      - `:"user.interrupt"`

    - `processed_at: Time`

      A timestamp in RFC 3339 format

  - `class BetaManagedAgentsUserToolConfirmationEvent`

    A tool confirmation event that approves or denies a pending tool execution.

    - `id: String`

      Unique identifier for this event.

    - `result: :allow | :deny`

      UserToolConfirmationResult enum

      - `:allow`

      - `:deny`

    - `tool_use_id: String`

      The id of the `agent.tool_use` or `agent.mcp_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

    - `type: :"user.tool_confirmation"`

      - `:"user.tool_confirmation"`

    - `deny_message: String`

      Optional message providing context for a 'deny' decision. Only allowed when result is 'deny'.

    - `processed_at: Time`

      A timestamp in RFC 3339 format

  - `class BetaManagedAgentsUserCustomToolResultEvent`

    Event sent by the client providing the result of a custom tool execution.

    - `id: String`

      Unique identifier for this event.

    - `custom_tool_use_id: String`

      The id of the `agent.custom_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

    - `type: :"user.custom_tool_result"`

      - `:"user.custom_tool_result"`

    - `content: Array[BetaManagedAgentsTextBlock | BetaManagedAgentsImageBlock | BetaManagedAgentsDocumentBlock]`

      The result content returned by the tool.

      - `class BetaManagedAgentsTextBlock`

        Regular text content.

        - `text: String`

          The text content.

        - `type: :text`

          - `:text`

      - `class BetaManagedAgentsImageBlock`

        Image content specified directly as base64 data or as a reference via a URL.

        - `source: BetaManagedAgentsBase64ImageSource | BetaManagedAgentsURLImageSource | BetaManagedAgentsFileImageSource`

          Union type for image source variants.

          - `class BetaManagedAgentsBase64ImageSource`

            Base64-encoded image data.

            - `data: String`

              Base64-encoded image data.

            - `media_type: String`

              MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

            - `type: :base64`

              - `:base64`

          - `class BetaManagedAgentsURLImageSource`

            Image referenced by URL.

            - `type: :url`

              - `:url`

            - `url: String`

              URL of the image to fetch.

          - `class BetaManagedAgentsFileImageSource`

            Image referenced by file ID.

            - `file_id: String`

              ID of a previously uploaded file.

            - `type: :file`

              - `:file`

        - `type: :image`

          - `:image`

      - `class BetaManagedAgentsDocumentBlock`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

        - `source: BetaManagedAgentsBase64DocumentSource | BetaManagedAgentsPlainTextDocumentSource | BetaManagedAgentsURLDocumentSource | BetaManagedAgentsFileDocumentSource`

          Union type for document source variants.

          - `class BetaManagedAgentsBase64DocumentSource`

            Base64-encoded document data.

            - `data: String`

              Base64-encoded document data.

            - `media_type: String`

              MIME type of the document (e.g., "application/pdf").

            - `type: :base64`

              - `:base64`

          - `class BetaManagedAgentsPlainTextDocumentSource`

            Plain text document content.

            - `data: String`

              The plain text content.

            - `media_type: :"text/plain"`

              MIME type of the text content. Must be "text/plain".

              - `:"text/plain"`

            - `type: :text`

              - `:text`

          - `class BetaManagedAgentsURLDocumentSource`

            Document referenced by URL.

            - `type: :url`

              - `:url`

            - `url: String`

              URL of the document to fetch.

          - `class BetaManagedAgentsFileDocumentSource`

            Document referenced by file ID.

            - `file_id: String`

              ID of a previously uploaded file.

            - `type: :file`

              - `:file`

        - `type: :document`

          - `:document`

        - `context: String`

          Additional context about the document for the model.

        - `title: String`

          The title of the document.

    - `is_error: bool`

      Whether the tool execution resulted in an error.

    - `processed_at: Time`

      A timestamp in RFC 3339 format

  - `class BetaManagedAgentsAgentCustomToolUseEvent`

    Event emitted when the agent calls a custom tool. The session goes idle until the client sends a `user.custom_tool_result` event with the result.

    - `id: String`

      Unique identifier for this event.

    - `input: Hash[Symbol, untyped]`

      Input parameters for the tool call.

    - `name: String`

      Name of the custom tool being called.

    - `processed_at: Time`

      A timestamp in RFC 3339 format

    - `type: :"agent.custom_tool_use"`

      - `:"agent.custom_tool_use"`

  - `class BetaManagedAgentsAgentMessageEvent`

    An agent response event in the session conversation.

    - `id: String`

      Unique identifier for this event.

    - `content: Array[BetaManagedAgentsTextBlock]`

      Array of text blocks comprising the agent response.

      - `text: String`

        The text content.

      - `type: :text`

        - `:text`

    - `processed_at: Time`

      A timestamp in RFC 3339 format

    - `type: :"agent.message"`

      - `:"agent.message"`

  - `class BetaManagedAgentsAgentThinkingEvent`

    Indicates the agent is making forward progress via extended thinking. A progress signal, not a content carrier.

    - `id: String`

      Unique identifier for this event.

    - `processed_at: Time`

      A timestamp in RFC 3339 format

    - `type: :"agent.thinking"`

      - `:"agent.thinking"`

  - `class BetaManagedAgentsAgentMCPToolUseEvent`

    Event emitted when the agent invokes a tool provided by an MCP server.

    - `id: String`

      Unique identifier for this event.

    - `input: Hash[Symbol, untyped]`

      Input parameters for the tool call.

    - `mcp_server_name: String`

      Name of the MCP server providing the tool.

    - `name: String`

      Name of the MCP tool being used.

    - `processed_at: Time`

      A timestamp in RFC 3339 format

    - `type: :"agent.mcp_tool_use"`

      - `:"agent.mcp_tool_use"`

    - `evaluated_permission: :allow | :ask | :deny`

      AgentEvaluatedPermission enum

      - `:allow`

      - `:ask`

      - `:deny`

  - `class BetaManagedAgentsAgentMCPToolResultEvent`

    Event representing the result of an MCP tool execution.

    - `id: String`

      Unique identifier for this event.

    - `mcp_tool_use_id: String`

      The id of the `agent.mcp_tool_use` event this result corresponds to.

    - `processed_at: Time`

      A timestamp in RFC 3339 format

    - `type: :"agent.mcp_tool_result"`

      - `:"agent.mcp_tool_result"`

    - `content: Array[BetaManagedAgentsTextBlock | BetaManagedAgentsImageBlock | BetaManagedAgentsDocumentBlock]`

      The result content returned by the tool.

      - `class BetaManagedAgentsTextBlock`

        Regular text content.

        - `text: String`

          The text content.

        - `type: :text`

          - `:text`

      - `class BetaManagedAgentsImageBlock`

        Image content specified directly as base64 data or as a reference via a URL.

        - `source: BetaManagedAgentsBase64ImageSource | BetaManagedAgentsURLImageSource | BetaManagedAgentsFileImageSource`

          Union type for image source variants.

          - `class BetaManagedAgentsBase64ImageSource`

            Base64-encoded image data.

            - `data: String`

              Base64-encoded image data.

            - `media_type: String`

              MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

            - `type: :base64`

              - `:base64`

          - `class BetaManagedAgentsURLImageSource`

            Image referenced by URL.

            - `type: :url`

              - `:url`

            - `url: String`

              URL of the image to fetch.

          - `class BetaManagedAgentsFileImageSource`

            Image referenced by file ID.

            - `file_id: String`

              ID of a previously uploaded file.

            - `type: :file`

              - `:file`

        - `type: :image`

          - `:image`

      - `class BetaManagedAgentsDocumentBlock`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

        - `source: BetaManagedAgentsBase64DocumentSource | BetaManagedAgentsPlainTextDocumentSource | BetaManagedAgentsURLDocumentSource | BetaManagedAgentsFileDocumentSource`

          Union type for document source variants.

          - `class BetaManagedAgentsBase64DocumentSource`

            Base64-encoded document data.

            - `data: String`

              Base64-encoded document data.

            - `media_type: String`

              MIME type of the document (e.g., "application/pdf").

            - `type: :base64`

              - `:base64`

          - `class BetaManagedAgentsPlainTextDocumentSource`

            Plain text document content.

            - `data: String`

              The plain text content.

            - `media_type: :"text/plain"`

              MIME type of the text content. Must be "text/plain".

              - `:"text/plain"`

            - `type: :text`

              - `:text`

          - `class BetaManagedAgentsURLDocumentSource`

            Document referenced by URL.

            - `type: :url`

              - `:url`

            - `url: String`

              URL of the document to fetch.

          - `class BetaManagedAgentsFileDocumentSource`

            Document referenced by file ID.

            - `file_id: String`

              ID of a previously uploaded file.

            - `type: :file`

              - `:file`

        - `type: :document`

          - `:document`

        - `context: String`

          Additional context about the document for the model.

        - `title: String`

          The title of the document.

    - `is_error: bool`

      Whether the tool execution resulted in an error.

  - `class BetaManagedAgentsAgentToolUseEvent`

    Event emitted when the agent invokes a built-in agent tool.

    - `id: String`

      Unique identifier for this event.

    - `input: Hash[Symbol, untyped]`

      Input parameters for the tool call.

    - `name: String`

      Name of the agent tool being used.

    - `processed_at: Time`

      A timestamp in RFC 3339 format

    - `type: :"agent.tool_use"`

      - `:"agent.tool_use"`

    - `evaluated_permission: :allow | :ask | :deny`

      AgentEvaluatedPermission enum

      - `:allow`

      - `:ask`

      - `:deny`

  - `class BetaManagedAgentsAgentToolResultEvent`

    Event representing the result of an agent tool execution.

    - `id: String`

      Unique identifier for this event.

    - `processed_at: Time`

      A timestamp in RFC 3339 format

    - `tool_use_id: String`

      The id of the `agent.tool_use` event this result corresponds to.

    - `type: :"agent.tool_result"`

      - `:"agent.tool_result"`

    - `content: Array[BetaManagedAgentsTextBlock | BetaManagedAgentsImageBlock | BetaManagedAgentsDocumentBlock]`

      The result content returned by the tool.

      - `class BetaManagedAgentsTextBlock`

        Regular text content.

        - `text: String`

          The text content.

        - `type: :text`

          - `:text`

      - `class BetaManagedAgentsImageBlock`

        Image content specified directly as base64 data or as a reference via a URL.

        - `source: BetaManagedAgentsBase64ImageSource | BetaManagedAgentsURLImageSource | BetaManagedAgentsFileImageSource`

          Union type for image source variants.

          - `class BetaManagedAgentsBase64ImageSource`

            Base64-encoded image data.

            - `data: String`

              Base64-encoded image data.

            - `media_type: String`

              MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

            - `type: :base64`

              - `:base64`

          - `class BetaManagedAgentsURLImageSource`

            Image referenced by URL.

            - `type: :url`

              - `:url`

            - `url: String`

              URL of the image to fetch.

          - `class BetaManagedAgentsFileImageSource`

            Image referenced by file ID.

            - `file_id: String`

              ID of a previously uploaded file.

            - `type: :file`

              - `:file`

        - `type: :image`

          - `:image`

      - `class BetaManagedAgentsDocumentBlock`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

        - `source: BetaManagedAgentsBase64DocumentSource | BetaManagedAgentsPlainTextDocumentSource | BetaManagedAgentsURLDocumentSource | BetaManagedAgentsFileDocumentSource`

          Union type for document source variants.

          - `class BetaManagedAgentsBase64DocumentSource`

            Base64-encoded document data.

            - `data: String`

              Base64-encoded document data.

            - `media_type: String`

              MIME type of the document (e.g., "application/pdf").

            - `type: :base64`

              - `:base64`

          - `class BetaManagedAgentsPlainTextDocumentSource`

            Plain text document content.

            - `data: String`

              The plain text content.

            - `media_type: :"text/plain"`

              MIME type of the text content. Must be "text/plain".

              - `:"text/plain"`

            - `type: :text`

              - `:text`

          - `class BetaManagedAgentsURLDocumentSource`

            Document referenced by URL.

            - `type: :url`

              - `:url`

            - `url: String`

              URL of the document to fetch.

          - `class BetaManagedAgentsFileDocumentSource`

            Document referenced by file ID.

            - `file_id: String`

              ID of a previously uploaded file.

            - `type: :file`

              - `:file`

        - `type: :document`

          - `:document`

        - `context: String`

          Additional context about the document for the model.

        - `title: String`

          The title of the document.

    - `is_error: bool`

      Whether the tool execution resulted in an error.

  - `class BetaManagedAgentsAgentThreadContextCompactedEvent`

    Indicates that context compaction (summarization) occurred during the session.

    - `id: String`

      Unique identifier for this event.

    - `processed_at: Time`

      A timestamp in RFC 3339 format

    - `type: :"agent.thread_context_compacted"`

      - `:"agent.thread_context_compacted"`

  - `class BetaManagedAgentsSessionErrorEvent`

    An error event indicating a problem occurred during session execution.

    - `id: String`

      Unique identifier for this event.

    - `error: BetaManagedAgentsUnknownError | BetaManagedAgentsModelOverloadedError | BetaManagedAgentsModelRateLimitedError | 4 more`

      An unknown or unexpected error occurred during session execution. A fallback variant; clients that don't recognize a new error code can match on `retry_status` and `message` alone.

      - `class BetaManagedAgentsUnknownError`

        An unknown or unexpected error occurred during session execution. A fallback variant; clients that don't recognize a new error code can match on `retry_status` and `message` alone.

        - `message: String`

          Human-readable error description.

        - `retry_status: BetaManagedAgentsRetryStatusRetrying | BetaManagedAgentsRetryStatusExhausted | BetaManagedAgentsRetryStatusTerminal`

          What the client should do next in response to this error.

          - `class BetaManagedAgentsRetryStatusRetrying`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

            - `type: :retrying`

              - `:retrying`

          - `class BetaManagedAgentsRetryStatusExhausted`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

            - `type: :exhausted`

              - `:exhausted`

          - `class BetaManagedAgentsRetryStatusTerminal`

            The session encountered a terminal error and will transition to `terminated` state.

            - `type: :terminal`

              - `:terminal`

        - `type: :unknown_error`

          - `:unknown_error`

      - `class BetaManagedAgentsModelOverloadedError`

        The model is currently overloaded. Emitted after automatic retries are exhausted.

        - `message: String`

          Human-readable error description.

        - `retry_status: BetaManagedAgentsRetryStatusRetrying | BetaManagedAgentsRetryStatusExhausted | BetaManagedAgentsRetryStatusTerminal`

          What the client should do next in response to this error.

          - `class BetaManagedAgentsRetryStatusRetrying`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

            - `type: :retrying`

              - `:retrying`

          - `class BetaManagedAgentsRetryStatusExhausted`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

            - `type: :exhausted`

              - `:exhausted`

          - `class BetaManagedAgentsRetryStatusTerminal`

            The session encountered a terminal error and will transition to `terminated` state.

            - `type: :terminal`

              - `:terminal`

        - `type: :model_overloaded_error`

          - `:model_overloaded_error`

      - `class BetaManagedAgentsModelRateLimitedError`

        The model request was rate-limited.

        - `message: String`

          Human-readable error description.

        - `retry_status: BetaManagedAgentsRetryStatusRetrying | BetaManagedAgentsRetryStatusExhausted | BetaManagedAgentsRetryStatusTerminal`

          What the client should do next in response to this error.

          - `class BetaManagedAgentsRetryStatusRetrying`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

            - `type: :retrying`

              - `:retrying`

          - `class BetaManagedAgentsRetryStatusExhausted`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

            - `type: :exhausted`

              - `:exhausted`

          - `class BetaManagedAgentsRetryStatusTerminal`

            The session encountered a terminal error and will transition to `terminated` state.

            - `type: :terminal`

              - `:terminal`

        - `type: :model_rate_limited_error`

          - `:model_rate_limited_error`

      - `class BetaManagedAgentsModelRequestFailedError`

        A model request failed for a reason other than overload or rate-limiting.

        - `message: String`

          Human-readable error description.

        - `retry_status: BetaManagedAgentsRetryStatusRetrying | BetaManagedAgentsRetryStatusExhausted | BetaManagedAgentsRetryStatusTerminal`

          What the client should do next in response to this error.

          - `class BetaManagedAgentsRetryStatusRetrying`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

            - `type: :retrying`

              - `:retrying`

          - `class BetaManagedAgentsRetryStatusExhausted`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

            - `type: :exhausted`

              - `:exhausted`

          - `class BetaManagedAgentsRetryStatusTerminal`

            The session encountered a terminal error and will transition to `terminated` state.

            - `type: :terminal`

              - `:terminal`

        - `type: :model_request_failed_error`

          - `:model_request_failed_error`

      - `class BetaManagedAgentsMCPConnectionFailedError`

        Failed to connect to an MCP server.

        - `mcp_server_name: String`

          Name of the MCP server that failed to connect.

        - `message: String`

          Human-readable error description.

        - `retry_status: BetaManagedAgentsRetryStatusRetrying | BetaManagedAgentsRetryStatusExhausted | BetaManagedAgentsRetryStatusTerminal`

          What the client should do next in response to this error.

          - `class BetaManagedAgentsRetryStatusRetrying`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

            - `type: :retrying`

              - `:retrying`

          - `class BetaManagedAgentsRetryStatusExhausted`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

            - `type: :exhausted`

              - `:exhausted`

          - `class BetaManagedAgentsRetryStatusTerminal`

            The session encountered a terminal error and will transition to `terminated` state.

            - `type: :terminal`

              - `:terminal`

        - `type: :mcp_connection_failed_error`

          - `:mcp_connection_failed_error`

      - `class BetaManagedAgentsMCPAuthenticationFailedError`

        Authentication to an MCP server failed.

        - `mcp_server_name: String`

          Name of the MCP server that failed authentication.

        - `message: String`

          Human-readable error description.

        - `retry_status: BetaManagedAgentsRetryStatusRetrying | BetaManagedAgentsRetryStatusExhausted | BetaManagedAgentsRetryStatusTerminal`

          What the client should do next in response to this error.

          - `class BetaManagedAgentsRetryStatusRetrying`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

            - `type: :retrying`

              - `:retrying`

          - `class BetaManagedAgentsRetryStatusExhausted`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

            - `type: :exhausted`

              - `:exhausted`

          - `class BetaManagedAgentsRetryStatusTerminal`

            The session encountered a terminal error and will transition to `terminated` state.

            - `type: :terminal`

              - `:terminal`

        - `type: :mcp_authentication_failed_error`

          - `:mcp_authentication_failed_error`

      - `class BetaManagedAgentsBillingError`

        The caller's organization or workspace cannot make model requests — out of credits or spend limit reached. Retrying with the same credentials will not succeed; the caller must resolve the billing state.

        - `message: String`

          Human-readable error description.

        - `retry_status: BetaManagedAgentsRetryStatusRetrying | BetaManagedAgentsRetryStatusExhausted | BetaManagedAgentsRetryStatusTerminal`

          What the client should do next in response to this error.

          - `class BetaManagedAgentsRetryStatusRetrying`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

            - `type: :retrying`

              - `:retrying`

          - `class BetaManagedAgentsRetryStatusExhausted`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

            - `type: :exhausted`

              - `:exhausted`

          - `class BetaManagedAgentsRetryStatusTerminal`

            The session encountered a terminal error and will transition to `terminated` state.

            - `type: :terminal`

              - `:terminal`

        - `type: :billing_error`

          - `:billing_error`

    - `processed_at: Time`

      A timestamp in RFC 3339 format

    - `type: :"session.error"`

      - `:"session.error"`

  - `class BetaManagedAgentsSessionStatusRescheduledEvent`

    Indicates the session is recovering from an error state and is rescheduled for execution.

    - `id: String`

      Unique identifier for this event.

    - `processed_at: Time`

      A timestamp in RFC 3339 format

    - `type: :"session.status_rescheduled"`

      - `:"session.status_rescheduled"`

  - `class BetaManagedAgentsSessionStatusRunningEvent`

    Indicates the session is actively running and the agent is working.

    - `id: String`

      Unique identifier for this event.

    - `processed_at: Time`

      A timestamp in RFC 3339 format

    - `type: :"session.status_running"`

      - `:"session.status_running"`

  - `class BetaManagedAgentsSessionStatusIdleEvent`

    Indicates the agent has paused and is awaiting user input.

    - `id: String`

      Unique identifier for this event.

    - `processed_at: Time`

      A timestamp in RFC 3339 format

    - `stop_reason: BetaManagedAgentsSessionEndTurn | BetaManagedAgentsSessionRequiresAction | BetaManagedAgentsSessionRetriesExhausted`

      The agent completed its turn naturally and is ready for the next user message.

      - `class BetaManagedAgentsSessionEndTurn`

        The agent completed its turn naturally and is ready for the next user message.

        - `type: :end_turn`

          - `:end_turn`

      - `class BetaManagedAgentsSessionRequiresAction`

        The agent is idle waiting on one or more blocking user-input events (tool confirmation, custom tool result, etc.). Resolving all of them transitions the session back to running.

        - `event_ids: Array[String]`

          The ids of events the agent is blocked on. Resolving fewer than all re-emits `session.status_idle` with the remainder.

        - `type: :requires_action`

          - `:requires_action`

      - `class BetaManagedAgentsSessionRetriesExhausted`

        The turn ended because the retry budget was exhausted (`max_iterations` hit or an error escalated to `retry_status: 'exhausted'`).

        - `type: :retries_exhausted`

          - `:retries_exhausted`

    - `type: :"session.status_idle"`

      - `:"session.status_idle"`

  - `class BetaManagedAgentsSessionStatusTerminatedEvent`

    Indicates the session has terminated, either due to an error or completion.

    - `id: String`

      Unique identifier for this event.

    - `processed_at: Time`

      A timestamp in RFC 3339 format

    - `type: :"session.status_terminated"`

      - `:"session.status_terminated"`

  - `class BetaManagedAgentsSpanModelRequestStartEvent`

    Emitted when a model request is initiated by the agent.

    - `id: String`

      Unique identifier for this event.

    - `processed_at: Time`

      A timestamp in RFC 3339 format

    - `type: :"span.model_request_start"`

      - `:"span.model_request_start"`

  - `class BetaManagedAgentsSpanModelRequestEndEvent`

    Emitted when a model request completes.

    - `id: String`

      Unique identifier for this event.

    - `is_error: bool`

      Whether the model request resulted in an error.

    - `model_request_start_id: String`

      The id of the corresponding `span.model_request_start` event.

    - `model_usage: BetaManagedAgentsSpanModelUsage`

      Token usage for a single model request.

      - `cache_creation_input_tokens: Integer`

        Tokens used to create prompt cache in this request.

      - `cache_read_input_tokens: Integer`

        Tokens read from prompt cache in this request.

      - `input_tokens: Integer`

        Input tokens consumed by this request.

      - `output_tokens: Integer`

        Output tokens generated by this request.

      - `speed: :standard | :fast`

        Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

        - `:standard`

        - `:fast`

    - `processed_at: Time`

      A timestamp in RFC 3339 format

    - `type: :"span.model_request_end"`

      - `:"span.model_request_end"`

  - `class BetaManagedAgentsSessionDeletedEvent`

    Emitted when a session has been deleted. Terminates any active event stream — no further events will be emitted for this session.

    - `id: String`

      Unique identifier for this event.

    - `processed_at: Time`

      A timestamp in RFC 3339 format

    - `type: :"session.deleted"`

      - `:"session.deleted"`

### Beta Managed Agents Text Block

- `class BetaManagedAgentsTextBlock`

  Regular text content.

  - `text: String`

    The text content.

  - `type: :text`

    - `:text`

### Beta Managed Agents Unknown Error

- `class BetaManagedAgentsUnknownError`

  An unknown or unexpected error occurred during session execution. A fallback variant; clients that don't recognize a new error code can match on `retry_status` and `message` alone.

  - `message: String`

    Human-readable error description.

  - `retry_status: BetaManagedAgentsRetryStatusRetrying | BetaManagedAgentsRetryStatusExhausted | BetaManagedAgentsRetryStatusTerminal`

    What the client should do next in response to this error.

    - `class BetaManagedAgentsRetryStatusRetrying`

      The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

      - `type: :retrying`

        - `:retrying`

    - `class BetaManagedAgentsRetryStatusExhausted`

      This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

      - `type: :exhausted`

        - `:exhausted`

    - `class BetaManagedAgentsRetryStatusTerminal`

      The session encountered a terminal error and will transition to `terminated` state.

      - `type: :terminal`

        - `:terminal`

  - `type: :unknown_error`

    - `:unknown_error`

### Beta Managed Agents URL Document Source

- `class BetaManagedAgentsURLDocumentSource`

  Document referenced by URL.

  - `type: :url`

    - `:url`

  - `url: String`

    URL of the document to fetch.

### Beta Managed Agents URL Image Source

- `class BetaManagedAgentsURLImageSource`

  Image referenced by URL.

  - `type: :url`

    - `:url`

  - `url: String`

    URL of the image to fetch.

### Beta Managed Agents User Custom Tool Result Event

- `class BetaManagedAgentsUserCustomToolResultEvent`

  Event sent by the client providing the result of a custom tool execution.

  - `id: String`

    Unique identifier for this event.

  - `custom_tool_use_id: String`

    The id of the `agent.custom_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

  - `type: :"user.custom_tool_result"`

    - `:"user.custom_tool_result"`

  - `content: Array[BetaManagedAgentsTextBlock | BetaManagedAgentsImageBlock | BetaManagedAgentsDocumentBlock]`

    The result content returned by the tool.

    - `class BetaManagedAgentsTextBlock`

      Regular text content.

      - `text: String`

        The text content.

      - `type: :text`

        - `:text`

    - `class BetaManagedAgentsImageBlock`

      Image content specified directly as base64 data or as a reference via a URL.

      - `source: BetaManagedAgentsBase64ImageSource | BetaManagedAgentsURLImageSource | BetaManagedAgentsFileImageSource`

        Union type for image source variants.

        - `class BetaManagedAgentsBase64ImageSource`

          Base64-encoded image data.

          - `data: String`

            Base64-encoded image data.

          - `media_type: String`

            MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

          - `type: :base64`

            - `:base64`

        - `class BetaManagedAgentsURLImageSource`

          Image referenced by URL.

          - `type: :url`

            - `:url`

          - `url: String`

            URL of the image to fetch.

        - `class BetaManagedAgentsFileImageSource`

          Image referenced by file ID.

          - `file_id: String`

            ID of a previously uploaded file.

          - `type: :file`

            - `:file`

      - `type: :image`

        - `:image`

    - `class BetaManagedAgentsDocumentBlock`

      Document content, either specified directly as base64 data, as text, or as a reference via a URL.

      - `source: BetaManagedAgentsBase64DocumentSource | BetaManagedAgentsPlainTextDocumentSource | BetaManagedAgentsURLDocumentSource | BetaManagedAgentsFileDocumentSource`

        Union type for document source variants.

        - `class BetaManagedAgentsBase64DocumentSource`

          Base64-encoded document data.

          - `data: String`

            Base64-encoded document data.

          - `media_type: String`

            MIME type of the document (e.g., "application/pdf").

          - `type: :base64`

            - `:base64`

        - `class BetaManagedAgentsPlainTextDocumentSource`

          Plain text document content.

          - `data: String`

            The plain text content.

          - `media_type: :"text/plain"`

            MIME type of the text content. Must be "text/plain".

            - `:"text/plain"`

          - `type: :text`

            - `:text`

        - `class BetaManagedAgentsURLDocumentSource`

          Document referenced by URL.

          - `type: :url`

            - `:url`

          - `url: String`

            URL of the document to fetch.

        - `class BetaManagedAgentsFileDocumentSource`

          Document referenced by file ID.

          - `file_id: String`

            ID of a previously uploaded file.

          - `type: :file`

            - `:file`

      - `type: :document`

        - `:document`

      - `context: String`

        Additional context about the document for the model.

      - `title: String`

        The title of the document.

  - `is_error: bool`

    Whether the tool execution resulted in an error.

  - `processed_at: Time`

    A timestamp in RFC 3339 format

### Beta Managed Agents User Custom Tool Result Event Params

- `class BetaManagedAgentsUserCustomToolResultEventParams`

  Parameters for providing the result of a custom tool execution.

  - `custom_tool_use_id: String`

    The id of the `agent.custom_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

  - `type: :"user.custom_tool_result"`

    - `:"user.custom_tool_result"`

  - `content: Array[BetaManagedAgentsTextBlock | BetaManagedAgentsImageBlock | BetaManagedAgentsDocumentBlock]`

    The result content returned by the tool.

    - `class BetaManagedAgentsTextBlock`

      Regular text content.

      - `text: String`

        The text content.

      - `type: :text`

        - `:text`

    - `class BetaManagedAgentsImageBlock`

      Image content specified directly as base64 data or as a reference via a URL.

      - `source: BetaManagedAgentsBase64ImageSource | BetaManagedAgentsURLImageSource | BetaManagedAgentsFileImageSource`

        Union type for image source variants.

        - `class BetaManagedAgentsBase64ImageSource`

          Base64-encoded image data.

          - `data: String`

            Base64-encoded image data.

          - `media_type: String`

            MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

          - `type: :base64`

            - `:base64`

        - `class BetaManagedAgentsURLImageSource`

          Image referenced by URL.

          - `type: :url`

            - `:url`

          - `url: String`

            URL of the image to fetch.

        - `class BetaManagedAgentsFileImageSource`

          Image referenced by file ID.

          - `file_id: String`

            ID of a previously uploaded file.

          - `type: :file`

            - `:file`

      - `type: :image`

        - `:image`

    - `class BetaManagedAgentsDocumentBlock`

      Document content, either specified directly as base64 data, as text, or as a reference via a URL.

      - `source: BetaManagedAgentsBase64DocumentSource | BetaManagedAgentsPlainTextDocumentSource | BetaManagedAgentsURLDocumentSource | BetaManagedAgentsFileDocumentSource`

        Union type for document source variants.

        - `class BetaManagedAgentsBase64DocumentSource`

          Base64-encoded document data.

          - `data: String`

            Base64-encoded document data.

          - `media_type: String`

            MIME type of the document (e.g., "application/pdf").

          - `type: :base64`

            - `:base64`

        - `class BetaManagedAgentsPlainTextDocumentSource`

          Plain text document content.

          - `data: String`

            The plain text content.

          - `media_type: :"text/plain"`

            MIME type of the text content. Must be "text/plain".

            - `:"text/plain"`

          - `type: :text`

            - `:text`

        - `class BetaManagedAgentsURLDocumentSource`

          Document referenced by URL.

          - `type: :url`

            - `:url`

          - `url: String`

            URL of the document to fetch.

        - `class BetaManagedAgentsFileDocumentSource`

          Document referenced by file ID.

          - `file_id: String`

            ID of a previously uploaded file.

          - `type: :file`

            - `:file`

      - `type: :document`

        - `:document`

      - `context: String`

        Additional context about the document for the model.

      - `title: String`

        The title of the document.

  - `is_error: bool`

    Whether the tool execution resulted in an error.

### Beta Managed Agents User Interrupt Event

- `class BetaManagedAgentsUserInterruptEvent`

  An interrupt event that pauses agent execution and returns control to the user.

  - `id: String`

    Unique identifier for this event.

  - `type: :"user.interrupt"`

    - `:"user.interrupt"`

  - `processed_at: Time`

    A timestamp in RFC 3339 format

### Beta Managed Agents User Interrupt Event Params

- `class BetaManagedAgentsUserInterruptEventParams`

  Parameters for sending an interrupt to pause the agent.

  - `type: :"user.interrupt"`

    - `:"user.interrupt"`

### Beta Managed Agents User Message Event

- `class BetaManagedAgentsUserMessageEvent`

  A user message event in the session conversation.

  - `id: String`

    Unique identifier for this event.

  - `content: Array[BetaManagedAgentsTextBlock | BetaManagedAgentsImageBlock | BetaManagedAgentsDocumentBlock]`

    Array of content blocks comprising the user message.

    - `class BetaManagedAgentsTextBlock`

      Regular text content.

      - `text: String`

        The text content.

      - `type: :text`

        - `:text`

    - `class BetaManagedAgentsImageBlock`

      Image content specified directly as base64 data or as a reference via a URL.

      - `source: BetaManagedAgentsBase64ImageSource | BetaManagedAgentsURLImageSource | BetaManagedAgentsFileImageSource`

        Union type for image source variants.

        - `class BetaManagedAgentsBase64ImageSource`

          Base64-encoded image data.

          - `data: String`

            Base64-encoded image data.

          - `media_type: String`

            MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

          - `type: :base64`

            - `:base64`

        - `class BetaManagedAgentsURLImageSource`

          Image referenced by URL.

          - `type: :url`

            - `:url`

          - `url: String`

            URL of the image to fetch.

        - `class BetaManagedAgentsFileImageSource`

          Image referenced by file ID.

          - `file_id: String`

            ID of a previously uploaded file.

          - `type: :file`

            - `:file`

      - `type: :image`

        - `:image`

    - `class BetaManagedAgentsDocumentBlock`

      Document content, either specified directly as base64 data, as text, or as a reference via a URL.

      - `source: BetaManagedAgentsBase64DocumentSource | BetaManagedAgentsPlainTextDocumentSource | BetaManagedAgentsURLDocumentSource | BetaManagedAgentsFileDocumentSource`

        Union type for document source variants.

        - `class BetaManagedAgentsBase64DocumentSource`

          Base64-encoded document data.

          - `data: String`

            Base64-encoded document data.

          - `media_type: String`

            MIME type of the document (e.g., "application/pdf").

          - `type: :base64`

            - `:base64`

        - `class BetaManagedAgentsPlainTextDocumentSource`

          Plain text document content.

          - `data: String`

            The plain text content.

          - `media_type: :"text/plain"`

            MIME type of the text content. Must be "text/plain".

            - `:"text/plain"`

          - `type: :text`

            - `:text`

        - `class BetaManagedAgentsURLDocumentSource`

          Document referenced by URL.

          - `type: :url`

            - `:url`

          - `url: String`

            URL of the document to fetch.

        - `class BetaManagedAgentsFileDocumentSource`

          Document referenced by file ID.

          - `file_id: String`

            ID of a previously uploaded file.

          - `type: :file`

            - `:file`

      - `type: :document`

        - `:document`

      - `context: String`

        Additional context about the document for the model.

      - `title: String`

        The title of the document.

  - `type: :"user.message"`

    - `:"user.message"`

  - `processed_at: Time`

    A timestamp in RFC 3339 format

### Beta Managed Agents User Message Event Params

- `class BetaManagedAgentsUserMessageEventParams`

  Parameters for sending a user message to the session.

  - `content: Array[BetaManagedAgentsTextBlock | BetaManagedAgentsImageBlock | BetaManagedAgentsDocumentBlock]`

    Array of content blocks for the user message.

    - `class BetaManagedAgentsTextBlock`

      Regular text content.

      - `text: String`

        The text content.

      - `type: :text`

        - `:text`

    - `class BetaManagedAgentsImageBlock`

      Image content specified directly as base64 data or as a reference via a URL.

      - `source: BetaManagedAgentsBase64ImageSource | BetaManagedAgentsURLImageSource | BetaManagedAgentsFileImageSource`

        Union type for image source variants.

        - `class BetaManagedAgentsBase64ImageSource`

          Base64-encoded image data.

          - `data: String`

            Base64-encoded image data.

          - `media_type: String`

            MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

          - `type: :base64`

            - `:base64`

        - `class BetaManagedAgentsURLImageSource`

          Image referenced by URL.

          - `type: :url`

            - `:url`

          - `url: String`

            URL of the image to fetch.

        - `class BetaManagedAgentsFileImageSource`

          Image referenced by file ID.

          - `file_id: String`

            ID of a previously uploaded file.

          - `type: :file`

            - `:file`

      - `type: :image`

        - `:image`

    - `class BetaManagedAgentsDocumentBlock`

      Document content, either specified directly as base64 data, as text, or as a reference via a URL.

      - `source: BetaManagedAgentsBase64DocumentSource | BetaManagedAgentsPlainTextDocumentSource | BetaManagedAgentsURLDocumentSource | BetaManagedAgentsFileDocumentSource`

        Union type for document source variants.

        - `class BetaManagedAgentsBase64DocumentSource`

          Base64-encoded document data.

          - `data: String`

            Base64-encoded document data.

          - `media_type: String`

            MIME type of the document (e.g., "application/pdf").

          - `type: :base64`

            - `:base64`

        - `class BetaManagedAgentsPlainTextDocumentSource`

          Plain text document content.

          - `data: String`

            The plain text content.

          - `media_type: :"text/plain"`

            MIME type of the text content. Must be "text/plain".

            - `:"text/plain"`

          - `type: :text`

            - `:text`

        - `class BetaManagedAgentsURLDocumentSource`

          Document referenced by URL.

          - `type: :url`

            - `:url`

          - `url: String`

            URL of the document to fetch.

        - `class BetaManagedAgentsFileDocumentSource`

          Document referenced by file ID.

          - `file_id: String`

            ID of a previously uploaded file.

          - `type: :file`

            - `:file`

      - `type: :document`

        - `:document`

      - `context: String`

        Additional context about the document for the model.

      - `title: String`

        The title of the document.

  - `type: :"user.message"`

    - `:"user.message"`

### Beta Managed Agents User Tool Confirmation Event

- `class BetaManagedAgentsUserToolConfirmationEvent`

  A tool confirmation event that approves or denies a pending tool execution.

  - `id: String`

    Unique identifier for this event.

  - `result: :allow | :deny`

    UserToolConfirmationResult enum

    - `:allow`

    - `:deny`

  - `tool_use_id: String`

    The id of the `agent.tool_use` or `agent.mcp_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

  - `type: :"user.tool_confirmation"`

    - `:"user.tool_confirmation"`

  - `deny_message: String`

    Optional message providing context for a 'deny' decision. Only allowed when result is 'deny'.

  - `processed_at: Time`

    A timestamp in RFC 3339 format

### Beta Managed Agents User Tool Confirmation Event Params

- `class BetaManagedAgentsUserToolConfirmationEventParams`

  Parameters for confirming or denying a tool execution request.

  - `result: :allow | :deny`

    UserToolConfirmationResult enum

    - `:allow`

    - `:deny`

  - `tool_use_id: String`

    The id of the `agent.tool_use` or `agent.mcp_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

  - `type: :"user.tool_confirmation"`

    - `:"user.tool_confirmation"`

  - `deny_message: String`

    Optional message providing context for a 'deny' decision. Only allowed when result is 'deny'.
