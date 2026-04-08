## List

`$ ant beta:sessions:events list`

**get** `/v1/sessions/{session_id}/events`

List Events

### Parameters

- `--session-id: string`

  Path param: Path parameter session_id

- `--limit: optional number`

  Query param: Query parameter for limit

- `--order: optional "asc" or "desc"`

  Query param: Sort direction for results, ordered by created_at. Defaults to asc (chronological).

- `--page: optional string`

  Query param: Opaque pagination cursor from a previous response's next_page.

- `--beta: optional array of AnthropicBeta`

  Header param: Optional header to specify the beta version(s) you want to use.

### Returns

- `BetaManagedAgentsListSessionEvents: object { data, next_page }`

  Paginated list of events for a `session`.

  - `data: optional array of BetaManagedAgentsSessionEvent`

    Events for the session, ordered by `created_at`.

    - `beta_managed_agents_user_message_event: object { id, content, type, processed_at }`

      A user message event in the session conversation.

      - `id: string`

        Unique identifier for this event.

      - `content: array of BetaManagedAgentsTextBlock or BetaManagedAgentsImageBlock or BetaManagedAgentsDocumentBlock`

        Array of content blocks comprising the user message.

        - `beta_managed_agents_text_block: object { text, type }`

          Regular text content.

          - `text: string`

            The text content.

          - `type: "text"`

            - `"text"`

        - `beta_managed_agents_image_block: object { source, type }`

          Image content specified directly as base64 data or as a reference via a URL.

          - `source: BetaManagedAgentsBase64ImageSource or BetaManagedAgentsURLImageSource or BetaManagedAgentsFileImageSource`

            Union type for image source variants.

            - `beta_managed_agents_base64_image_source: object { data, media_type, type }`

              Base64-encoded image data.

              - `data: string`

                Base64-encoded image data.

              - `media_type: string`

                MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

              - `type: "base64"`

                - `"base64"`

            - `beta_managed_agents_url_image_source: object { type, url }`

              Image referenced by URL.

              - `type: "url"`

                - `"url"`

              - `url: string`

                URL of the image to fetch.

            - `beta_managed_agents_file_image_source: object { file_id, type }`

              Image referenced by file ID.

              - `file_id: string`

                ID of a previously uploaded file.

              - `type: "file"`

                - `"file"`

          - `type: "image"`

            - `"image"`

        - `beta_managed_agents_document_block: object { source, type, context, title }`

          Document content, either specified directly as base64 data, as text, or as a reference via a URL.

          - `source: BetaManagedAgentsBase64DocumentSource or BetaManagedAgentsPlainTextDocumentSource or BetaManagedAgentsURLDocumentSource or BetaManagedAgentsFileDocumentSource`

            Union type for document source variants.

            - `beta_managed_agents_base64_document_source: object { data, media_type, type }`

              Base64-encoded document data.

              - `data: string`

                Base64-encoded document data.

              - `media_type: string`

                MIME type of the document (e.g., "application/pdf").

              - `type: "base64"`

                - `"base64"`

            - `beta_managed_agents_plain_text_document_source: object { data, media_type, type }`

              Plain text document content.

              - `data: string`

                The plain text content.

              - `media_type: "text/plain"`

                MIME type of the text content. Must be "text/plain".

                - `"text/plain"`

              - `type: "text"`

                - `"text"`

            - `beta_managed_agents_url_document_source: object { type, url }`

              Document referenced by URL.

              - `type: "url"`

                - `"url"`

              - `url: string`

                URL of the document to fetch.

            - `beta_managed_agents_file_document_source: object { file_id, type }`

              Document referenced by file ID.

              - `file_id: string`

                ID of a previously uploaded file.

              - `type: "file"`

                - `"file"`

          - `type: "document"`

            - `"document"`

          - `context: optional string`

            Additional context about the document for the model.

          - `title: optional string`

            The title of the document.

      - `type: "user.message"`

        - `"user.message"`

      - `processed_at: optional string`

        A timestamp in RFC 3339 format

    - `beta_managed_agents_user_interrupt_event: object { id, type, processed_at }`

      An interrupt event that pauses agent execution and returns control to the user.

      - `id: string`

        Unique identifier for this event.

      - `type: "user.interrupt"`

        - `"user.interrupt"`

      - `processed_at: optional string`

        A timestamp in RFC 3339 format

    - `beta_managed_agents_user_tool_confirmation_event: object { id, result, tool_use_id, 3 more }`

      A tool confirmation event that approves or denies a pending tool execution.

      - `id: string`

        Unique identifier for this event.

      - `result: "allow" or "deny"`

        UserToolConfirmationResult enum

        - `"allow"`

        - `"deny"`

      - `tool_use_id: string`

        The id of the `agent.tool_use` or `agent.mcp_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

      - `type: "user.tool_confirmation"`

        - `"user.tool_confirmation"`

      - `deny_message: optional string`

        Optional message providing context for a 'deny' decision. Only allowed when result is 'deny'.

      - `processed_at: optional string`

        A timestamp in RFC 3339 format

    - `beta_managed_agents_user_custom_tool_result_event: object { id, custom_tool_use_id, type, 3 more }`

      Event sent by the client providing the result of a custom tool execution.

      - `id: string`

        Unique identifier for this event.

      - `custom_tool_use_id: string`

        The id of the `agent.custom_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

      - `type: "user.custom_tool_result"`

        - `"user.custom_tool_result"`

      - `content: optional array of BetaManagedAgentsTextBlock or BetaManagedAgentsImageBlock or BetaManagedAgentsDocumentBlock`

        The result content returned by the tool.

        - `beta_managed_agents_text_block: object { text, type }`

          Regular text content.

          - `text: string`

            The text content.

          - `type: "text"`

            - `"text"`

        - `beta_managed_agents_image_block: object { source, type }`

          Image content specified directly as base64 data or as a reference via a URL.

          - `source: BetaManagedAgentsBase64ImageSource or BetaManagedAgentsURLImageSource or BetaManagedAgentsFileImageSource`

            Union type for image source variants.

            - `beta_managed_agents_base64_image_source: object { data, media_type, type }`

              Base64-encoded image data.

              - `data: string`

                Base64-encoded image data.

              - `media_type: string`

                MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

              - `type: "base64"`

                - `"base64"`

            - `beta_managed_agents_url_image_source: object { type, url }`

              Image referenced by URL.

              - `type: "url"`

                - `"url"`

              - `url: string`

                URL of the image to fetch.

            - `beta_managed_agents_file_image_source: object { file_id, type }`

              Image referenced by file ID.

              - `file_id: string`

                ID of a previously uploaded file.

              - `type: "file"`

                - `"file"`

          - `type: "image"`

            - `"image"`

        - `beta_managed_agents_document_block: object { source, type, context, title }`

          Document content, either specified directly as base64 data, as text, or as a reference via a URL.

          - `source: BetaManagedAgentsBase64DocumentSource or BetaManagedAgentsPlainTextDocumentSource or BetaManagedAgentsURLDocumentSource or BetaManagedAgentsFileDocumentSource`

            Union type for document source variants.

            - `beta_managed_agents_base64_document_source: object { data, media_type, type }`

              Base64-encoded document data.

              - `data: string`

                Base64-encoded document data.

              - `media_type: string`

                MIME type of the document (e.g., "application/pdf").

              - `type: "base64"`

                - `"base64"`

            - `beta_managed_agents_plain_text_document_source: object { data, media_type, type }`

              Plain text document content.

              - `data: string`

                The plain text content.

              - `media_type: "text/plain"`

                MIME type of the text content. Must be "text/plain".

                - `"text/plain"`

              - `type: "text"`

                - `"text"`

            - `beta_managed_agents_url_document_source: object { type, url }`

              Document referenced by URL.

              - `type: "url"`

                - `"url"`

              - `url: string`

                URL of the document to fetch.

            - `beta_managed_agents_file_document_source: object { file_id, type }`

              Document referenced by file ID.

              - `file_id: string`

                ID of a previously uploaded file.

              - `type: "file"`

                - `"file"`

          - `type: "document"`

            - `"document"`

          - `context: optional string`

            Additional context about the document for the model.

          - `title: optional string`

            The title of the document.

      - `is_error: optional boolean`

        Whether the tool execution resulted in an error.

      - `processed_at: optional string`

        A timestamp in RFC 3339 format

    - `beta_managed_agents_agent_custom_tool_use_event: object { id, input, name, 2 more }`

      Event emitted when the agent calls a custom tool. The session goes idle until the client sends a `user.custom_tool_result` event with the result.

      - `id: string`

        Unique identifier for this event.

      - `input: map[unknown]`

        Input parameters for the tool call.

      - `name: string`

        Name of the custom tool being called.

      - `processed_at: string`

        A timestamp in RFC 3339 format

      - `type: "agent.custom_tool_use"`

        - `"agent.custom_tool_use"`

    - `beta_managed_agents_agent_message_event: object { id, content, processed_at, type }`

      An agent response event in the session conversation.

      - `id: string`

        Unique identifier for this event.

      - `content: array of BetaManagedAgentsTextBlock`

        Array of text blocks comprising the agent response.

        - `text: string`

          The text content.

        - `type: "text"`

          - `"text"`

      - `processed_at: string`

        A timestamp in RFC 3339 format

      - `type: "agent.message"`

        - `"agent.message"`

    - `beta_managed_agents_agent_thinking_event: object { id, processed_at, type }`

      Indicates the agent is making forward progress via extended thinking. A progress signal, not a content carrier.

      - `id: string`

        Unique identifier for this event.

      - `processed_at: string`

        A timestamp in RFC 3339 format

      - `type: "agent.thinking"`

        - `"agent.thinking"`

    - `beta_managed_agents_agent_mcp_tool_use_event: object { id, input, mcp_server_name, 4 more }`

      Event emitted when the agent invokes a tool provided by an MCP server.

      - `id: string`

        Unique identifier for this event.

      - `input: map[unknown]`

        Input parameters for the tool call.

      - `mcp_server_name: string`

        Name of the MCP server providing the tool.

      - `name: string`

        Name of the MCP tool being used.

      - `processed_at: string`

        A timestamp in RFC 3339 format

      - `type: "agent.mcp_tool_use"`

        - `"agent.mcp_tool_use"`

      - `evaluated_permission: optional "allow" or "ask" or "deny"`

        AgentEvaluatedPermission enum

        - `"allow"`

        - `"ask"`

        - `"deny"`

    - `beta_managed_agents_agent_mcp_tool_result_event: object { id, mcp_tool_use_id, processed_at, 3 more }`

      Event representing the result of an MCP tool execution.

      - `id: string`

        Unique identifier for this event.

      - `mcp_tool_use_id: string`

        The id of the `agent.mcp_tool_use` event this result corresponds to.

      - `processed_at: string`

        A timestamp in RFC 3339 format

      - `type: "agent.mcp_tool_result"`

        - `"agent.mcp_tool_result"`

      - `content: optional array of BetaManagedAgentsTextBlock or BetaManagedAgentsImageBlock or BetaManagedAgentsDocumentBlock`

        The result content returned by the tool.

        - `beta_managed_agents_text_block: object { text, type }`

          Regular text content.

          - `text: string`

            The text content.

          - `type: "text"`

            - `"text"`

        - `beta_managed_agents_image_block: object { source, type }`

          Image content specified directly as base64 data or as a reference via a URL.

          - `source: BetaManagedAgentsBase64ImageSource or BetaManagedAgentsURLImageSource or BetaManagedAgentsFileImageSource`

            Union type for image source variants.

            - `beta_managed_agents_base64_image_source: object { data, media_type, type }`

              Base64-encoded image data.

              - `data: string`

                Base64-encoded image data.

              - `media_type: string`

                MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

              - `type: "base64"`

                - `"base64"`

            - `beta_managed_agents_url_image_source: object { type, url }`

              Image referenced by URL.

              - `type: "url"`

                - `"url"`

              - `url: string`

                URL of the image to fetch.

            - `beta_managed_agents_file_image_source: object { file_id, type }`

              Image referenced by file ID.

              - `file_id: string`

                ID of a previously uploaded file.

              - `type: "file"`

                - `"file"`

          - `type: "image"`

            - `"image"`

        - `beta_managed_agents_document_block: object { source, type, context, title }`

          Document content, either specified directly as base64 data, as text, or as a reference via a URL.

          - `source: BetaManagedAgentsBase64DocumentSource or BetaManagedAgentsPlainTextDocumentSource or BetaManagedAgentsURLDocumentSource or BetaManagedAgentsFileDocumentSource`

            Union type for document source variants.

            - `beta_managed_agents_base64_document_source: object { data, media_type, type }`

              Base64-encoded document data.

              - `data: string`

                Base64-encoded document data.

              - `media_type: string`

                MIME type of the document (e.g., "application/pdf").

              - `type: "base64"`

                - `"base64"`

            - `beta_managed_agents_plain_text_document_source: object { data, media_type, type }`

              Plain text document content.

              - `data: string`

                The plain text content.

              - `media_type: "text/plain"`

                MIME type of the text content. Must be "text/plain".

                - `"text/plain"`

              - `type: "text"`

                - `"text"`

            - `beta_managed_agents_url_document_source: object { type, url }`

              Document referenced by URL.

              - `type: "url"`

                - `"url"`

              - `url: string`

                URL of the document to fetch.

            - `beta_managed_agents_file_document_source: object { file_id, type }`

              Document referenced by file ID.

              - `file_id: string`

                ID of a previously uploaded file.

              - `type: "file"`

                - `"file"`

          - `type: "document"`

            - `"document"`

          - `context: optional string`

            Additional context about the document for the model.

          - `title: optional string`

            The title of the document.

      - `is_error: optional boolean`

        Whether the tool execution resulted in an error.

    - `beta_managed_agents_agent_tool_use_event: object { id, input, name, 3 more }`

      Event emitted when the agent invokes a built-in agent tool.

      - `id: string`

        Unique identifier for this event.

      - `input: map[unknown]`

        Input parameters for the tool call.

      - `name: string`

        Name of the agent tool being used.

      - `processed_at: string`

        A timestamp in RFC 3339 format

      - `type: "agent.tool_use"`

        - `"agent.tool_use"`

      - `evaluated_permission: optional "allow" or "ask" or "deny"`

        AgentEvaluatedPermission enum

        - `"allow"`

        - `"ask"`

        - `"deny"`

    - `beta_managed_agents_agent_tool_result_event: object { id, processed_at, tool_use_id, 3 more }`

      Event representing the result of an agent tool execution.

      - `id: string`

        Unique identifier for this event.

      - `processed_at: string`

        A timestamp in RFC 3339 format

      - `tool_use_id: string`

        The id of the `agent.tool_use` event this result corresponds to.

      - `type: "agent.tool_result"`

        - `"agent.tool_result"`

      - `content: optional array of BetaManagedAgentsTextBlock or BetaManagedAgentsImageBlock or BetaManagedAgentsDocumentBlock`

        The result content returned by the tool.

        - `beta_managed_agents_text_block: object { text, type }`

          Regular text content.

          - `text: string`

            The text content.

          - `type: "text"`

            - `"text"`

        - `beta_managed_agents_image_block: object { source, type }`

          Image content specified directly as base64 data or as a reference via a URL.

          - `source: BetaManagedAgentsBase64ImageSource or BetaManagedAgentsURLImageSource or BetaManagedAgentsFileImageSource`

            Union type for image source variants.

            - `beta_managed_agents_base64_image_source: object { data, media_type, type }`

              Base64-encoded image data.

              - `data: string`

                Base64-encoded image data.

              - `media_type: string`

                MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

              - `type: "base64"`

                - `"base64"`

            - `beta_managed_agents_url_image_source: object { type, url }`

              Image referenced by URL.

              - `type: "url"`

                - `"url"`

              - `url: string`

                URL of the image to fetch.

            - `beta_managed_agents_file_image_source: object { file_id, type }`

              Image referenced by file ID.

              - `file_id: string`

                ID of a previously uploaded file.

              - `type: "file"`

                - `"file"`

          - `type: "image"`

            - `"image"`

        - `beta_managed_agents_document_block: object { source, type, context, title }`

          Document content, either specified directly as base64 data, as text, or as a reference via a URL.

          - `source: BetaManagedAgentsBase64DocumentSource or BetaManagedAgentsPlainTextDocumentSource or BetaManagedAgentsURLDocumentSource or BetaManagedAgentsFileDocumentSource`

            Union type for document source variants.

            - `beta_managed_agents_base64_document_source: object { data, media_type, type }`

              Base64-encoded document data.

              - `data: string`

                Base64-encoded document data.

              - `media_type: string`

                MIME type of the document (e.g., "application/pdf").

              - `type: "base64"`

                - `"base64"`

            - `beta_managed_agents_plain_text_document_source: object { data, media_type, type }`

              Plain text document content.

              - `data: string`

                The plain text content.

              - `media_type: "text/plain"`

                MIME type of the text content. Must be "text/plain".

                - `"text/plain"`

              - `type: "text"`

                - `"text"`

            - `beta_managed_agents_url_document_source: object { type, url }`

              Document referenced by URL.

              - `type: "url"`

                - `"url"`

              - `url: string`

                URL of the document to fetch.

            - `beta_managed_agents_file_document_source: object { file_id, type }`

              Document referenced by file ID.

              - `file_id: string`

                ID of a previously uploaded file.

              - `type: "file"`

                - `"file"`

          - `type: "document"`

            - `"document"`

          - `context: optional string`

            Additional context about the document for the model.

          - `title: optional string`

            The title of the document.

      - `is_error: optional boolean`

        Whether the tool execution resulted in an error.

    - `beta_managed_agents_agent_thread_context_compacted_event: object { id, processed_at, type }`

      Indicates that context compaction (summarization) occurred during the session.

      - `id: string`

        Unique identifier for this event.

      - `processed_at: string`

        A timestamp in RFC 3339 format

      - `type: "agent.thread_context_compacted"`

        - `"agent.thread_context_compacted"`

    - `beta_managed_agents_session_error_event: object { id, error, processed_at, type }`

      An error event indicating a problem occurred during session execution.

      - `id: string`

        Unique identifier for this event.

      - `error: BetaManagedAgentsUnknownError or BetaManagedAgentsModelOverloadedError or BetaManagedAgentsModelRateLimitedError or 4 more`

        An unknown or unexpected error occurred during session execution. A fallback variant; clients that don't recognize a new error code can match on `retry_status` and `message` alone.

        - `beta_managed_agents_unknown_error: object { message, retry_status, type }`

          An unknown or unexpected error occurred during session execution. A fallback variant; clients that don't recognize a new error code can match on `retry_status` and `message` alone.

          - `message: string`

            Human-readable error description.

          - `retry_status: BetaManagedAgentsRetryStatusRetrying or BetaManagedAgentsRetryStatusExhausted or BetaManagedAgentsRetryStatusTerminal`

            What the client should do next in response to this error.

            - `beta_managed_agents_retry_status_retrying: object { type }`

              The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

              - `type: "retrying"`

                - `"retrying"`

            - `beta_managed_agents_retry_status_exhausted: object { type }`

              This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

              - `type: "exhausted"`

                - `"exhausted"`

            - `beta_managed_agents_retry_status_terminal: object { type }`

              The session encountered a terminal error and will transition to `terminated` state.

              - `type: "terminal"`

                - `"terminal"`

          - `type: "unknown_error"`

            - `"unknown_error"`

        - `beta_managed_agents_model_overloaded_error: object { message, retry_status, type }`

          The model is currently overloaded. Emitted after automatic retries are exhausted.

          - `message: string`

            Human-readable error description.

          - `retry_status: BetaManagedAgentsRetryStatusRetrying or BetaManagedAgentsRetryStatusExhausted or BetaManagedAgentsRetryStatusTerminal`

            What the client should do next in response to this error.

            - `beta_managed_agents_retry_status_retrying: object { type }`

              The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

              - `type: "retrying"`

                - `"retrying"`

            - `beta_managed_agents_retry_status_exhausted: object { type }`

              This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

              - `type: "exhausted"`

                - `"exhausted"`

            - `beta_managed_agents_retry_status_terminal: object { type }`

              The session encountered a terminal error and will transition to `terminated` state.

              - `type: "terminal"`

                - `"terminal"`

          - `type: "model_overloaded_error"`

            - `"model_overloaded_error"`

        - `beta_managed_agents_model_rate_limited_error: object { message, retry_status, type }`

          The model request was rate-limited.

          - `message: string`

            Human-readable error description.

          - `retry_status: BetaManagedAgentsRetryStatusRetrying or BetaManagedAgentsRetryStatusExhausted or BetaManagedAgentsRetryStatusTerminal`

            What the client should do next in response to this error.

            - `beta_managed_agents_retry_status_retrying: object { type }`

              The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

              - `type: "retrying"`

                - `"retrying"`

            - `beta_managed_agents_retry_status_exhausted: object { type }`

              This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

              - `type: "exhausted"`

                - `"exhausted"`

            - `beta_managed_agents_retry_status_terminal: object { type }`

              The session encountered a terminal error and will transition to `terminated` state.

              - `type: "terminal"`

                - `"terminal"`

          - `type: "model_rate_limited_error"`

            - `"model_rate_limited_error"`

        - `beta_managed_agents_model_request_failed_error: object { message, retry_status, type }`

          A model request failed for a reason other than overload or rate-limiting.

          - `message: string`

            Human-readable error description.

          - `retry_status: BetaManagedAgentsRetryStatusRetrying or BetaManagedAgentsRetryStatusExhausted or BetaManagedAgentsRetryStatusTerminal`

            What the client should do next in response to this error.

            - `beta_managed_agents_retry_status_retrying: object { type }`

              The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

              - `type: "retrying"`

                - `"retrying"`

            - `beta_managed_agents_retry_status_exhausted: object { type }`

              This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

              - `type: "exhausted"`

                - `"exhausted"`

            - `beta_managed_agents_retry_status_terminal: object { type }`

              The session encountered a terminal error and will transition to `terminated` state.

              - `type: "terminal"`

                - `"terminal"`

          - `type: "model_request_failed_error"`

            - `"model_request_failed_error"`

        - `beta_managed_agents_mcp_connection_failed_error: object { mcp_server_name, message, retry_status, type }`

          Failed to connect to an MCP server.

          - `mcp_server_name: string`

            Name of the MCP server that failed to connect.

          - `message: string`

            Human-readable error description.

          - `retry_status: BetaManagedAgentsRetryStatusRetrying or BetaManagedAgentsRetryStatusExhausted or BetaManagedAgentsRetryStatusTerminal`

            What the client should do next in response to this error.

            - `beta_managed_agents_retry_status_retrying: object { type }`

              The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

              - `type: "retrying"`

                - `"retrying"`

            - `beta_managed_agents_retry_status_exhausted: object { type }`

              This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

              - `type: "exhausted"`

                - `"exhausted"`

            - `beta_managed_agents_retry_status_terminal: object { type }`

              The session encountered a terminal error and will transition to `terminated` state.

              - `type: "terminal"`

                - `"terminal"`

          - `type: "mcp_connection_failed_error"`

            - `"mcp_connection_failed_error"`

        - `beta_managed_agents_mcp_authentication_failed_error: object { mcp_server_name, message, retry_status, type }`

          Authentication to an MCP server failed.

          - `mcp_server_name: string`

            Name of the MCP server that failed authentication.

          - `message: string`

            Human-readable error description.

          - `retry_status: BetaManagedAgentsRetryStatusRetrying or BetaManagedAgentsRetryStatusExhausted or BetaManagedAgentsRetryStatusTerminal`

            What the client should do next in response to this error.

            - `beta_managed_agents_retry_status_retrying: object { type }`

              The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

              - `type: "retrying"`

                - `"retrying"`

            - `beta_managed_agents_retry_status_exhausted: object { type }`

              This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

              - `type: "exhausted"`

                - `"exhausted"`

            - `beta_managed_agents_retry_status_terminal: object { type }`

              The session encountered a terminal error and will transition to `terminated` state.

              - `type: "terminal"`

                - `"terminal"`

          - `type: "mcp_authentication_failed_error"`

            - `"mcp_authentication_failed_error"`

        - `beta_managed_agents_billing_error: object { message, retry_status, type }`

          The caller's organization or workspace cannot make model requests — out of credits or spend limit reached. Retrying with the same credentials will not succeed; the caller must resolve the billing state.

          - `message: string`

            Human-readable error description.

          - `retry_status: BetaManagedAgentsRetryStatusRetrying or BetaManagedAgentsRetryStatusExhausted or BetaManagedAgentsRetryStatusTerminal`

            What the client should do next in response to this error.

            - `beta_managed_agents_retry_status_retrying: object { type }`

              The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

              - `type: "retrying"`

                - `"retrying"`

            - `beta_managed_agents_retry_status_exhausted: object { type }`

              This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

              - `type: "exhausted"`

                - `"exhausted"`

            - `beta_managed_agents_retry_status_terminal: object { type }`

              The session encountered a terminal error and will transition to `terminated` state.

              - `type: "terminal"`

                - `"terminal"`

          - `type: "billing_error"`

            - `"billing_error"`

      - `processed_at: string`

        A timestamp in RFC 3339 format

      - `type: "session.error"`

        - `"session.error"`

    - `beta_managed_agents_session_status_rescheduled_event: object { id, processed_at, type }`

      Indicates the session is recovering from an error state and is rescheduled for execution.

      - `id: string`

        Unique identifier for this event.

      - `processed_at: string`

        A timestamp in RFC 3339 format

      - `type: "session.status_rescheduled"`

        - `"session.status_rescheduled"`

    - `beta_managed_agents_session_status_running_event: object { id, processed_at, type }`

      Indicates the session is actively running and the agent is working.

      - `id: string`

        Unique identifier for this event.

      - `processed_at: string`

        A timestamp in RFC 3339 format

      - `type: "session.status_running"`

        - `"session.status_running"`

    - `beta_managed_agents_session_status_idle_event: object { id, processed_at, stop_reason, type }`

      Indicates the agent has paused and is awaiting user input.

      - `id: string`

        Unique identifier for this event.

      - `processed_at: string`

        A timestamp in RFC 3339 format

      - `stop_reason: BetaManagedAgentsSessionEndTurn or BetaManagedAgentsSessionRequiresAction or BetaManagedAgentsSessionRetriesExhausted`

        The agent completed its turn naturally and is ready for the next user message.

        - `beta_managed_agents_session_end_turn: object { type }`

          The agent completed its turn naturally and is ready for the next user message.

          - `type: "end_turn"`

            - `"end_turn"`

        - `beta_managed_agents_session_requires_action: object { event_ids, type }`

          The agent is idle waiting on one or more blocking user-input events (tool confirmation, custom tool result, etc.). Resolving all of them transitions the session back to running.

          - `event_ids: array of string`

            The ids of events the agent is blocked on. Resolving fewer than all re-emits `session.status_idle` with the remainder.

          - `type: "requires_action"`

            - `"requires_action"`

        - `beta_managed_agents_session_retries_exhausted: object { type }`

          The turn ended because the retry budget was exhausted (`max_iterations` hit or an error escalated to `retry_status: 'exhausted'`).

          - `type: "retries_exhausted"`

            - `"retries_exhausted"`

      - `type: "session.status_idle"`

        - `"session.status_idle"`

    - `beta_managed_agents_session_status_terminated_event: object { id, processed_at, type }`

      Indicates the session has terminated, either due to an error or completion.

      - `id: string`

        Unique identifier for this event.

      - `processed_at: string`

        A timestamp in RFC 3339 format

      - `type: "session.status_terminated"`

        - `"session.status_terminated"`

    - `beta_managed_agents_span_model_request_start_event: object { id, processed_at, type }`

      Emitted when a model request is initiated by the agent.

      - `id: string`

        Unique identifier for this event.

      - `processed_at: string`

        A timestamp in RFC 3339 format

      - `type: "span.model_request_start"`

        - `"span.model_request_start"`

    - `beta_managed_agents_span_model_request_end_event: object { id, is_error, model_request_start_id, 3 more }`

      Emitted when a model request completes.

      - `id: string`

        Unique identifier for this event.

      - `is_error: boolean`

        Whether the model request resulted in an error.

      - `model_request_start_id: string`

        The id of the corresponding `span.model_request_start` event.

      - `model_usage: object { cache_creation_input_tokens, cache_read_input_tokens, input_tokens, 2 more }`

        Token usage for a single model request.

        - `cache_creation_input_tokens: number`

          Tokens used to create prompt cache in this request.

        - `cache_read_input_tokens: number`

          Tokens read from prompt cache in this request.

        - `input_tokens: number`

          Input tokens consumed by this request.

        - `output_tokens: number`

          Output tokens generated by this request.

        - `speed: optional "standard" or "fast"`

          Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

          - `"standard"`

          - `"fast"`

      - `processed_at: string`

        A timestamp in RFC 3339 format

      - `type: "span.model_request_end"`

        - `"span.model_request_end"`

    - `beta_managed_agents_session_deleted_event: object { id, processed_at, type }`

      Emitted when a session has been deleted. Terminates any active event stream — no further events will be emitted for this session.

      - `id: string`

        Unique identifier for this event.

      - `processed_at: string`

        A timestamp in RFC 3339 format

      - `type: "session.deleted"`

        - `"session.deleted"`

  - `next_page: optional string`

    Opaque cursor for the next page. Null when no more results.

### Example

```cli
ant beta:sessions:events list \
  --api-key my-anthropic-api-key \
  --session-id sesn_011CZkZAtmR3yMPDzynEDxu7
```
