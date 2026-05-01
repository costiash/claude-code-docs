# Events

## List

`EventListPage beta().sessions().events().list(EventListParamsparams = EventListParams.none(), RequestOptionsrequestOptions = RequestOptions.none())`

**get** `/v1/sessions/{session_id}/events`

List Events

### Parameters

- `EventListParams params`

  - `Optional<String> sessionId`

  - `Optional<Long> limit`

    Query parameter for limit

  - `Optional<Order> order`

    Sort direction for results, ordered by created_at. Defaults to asc (chronological).

    - `ASC("asc")`

    - `DESC("desc")`

  - `Optional<String> page`

    Opaque pagination cursor from a previous response's next_page.

  - `Optional<List<AnthropicBeta>> betas`

    Optional header to specify the beta version(s) you want to use.

    - `MESSAGE_BATCHES_2024_09_24("message-batches-2024-09-24")`

    - `PROMPT_CACHING_2024_07_31("prompt-caching-2024-07-31")`

    - `COMPUTER_USE_2024_10_22("computer-use-2024-10-22")`

    - `COMPUTER_USE_2025_01_24("computer-use-2025-01-24")`

    - `PDFS_2024_09_25("pdfs-2024-09-25")`

    - `TOKEN_COUNTING_2024_11_01("token-counting-2024-11-01")`

    - `TOKEN_EFFICIENT_TOOLS_2025_02_19("token-efficient-tools-2025-02-19")`

    - `OUTPUT_128K_2025_02_19("output-128k-2025-02-19")`

    - `FILES_API_2025_04_14("files-api-2025-04-14")`

    - `MCP_CLIENT_2025_04_04("mcp-client-2025-04-04")`

    - `MCP_CLIENT_2025_11_20("mcp-client-2025-11-20")`

    - `DEV_FULL_THINKING_2025_05_14("dev-full-thinking-2025-05-14")`

    - `INTERLEAVED_THINKING_2025_05_14("interleaved-thinking-2025-05-14")`

    - `CODE_EXECUTION_2025_05_22("code-execution-2025-05-22")`

    - `EXTENDED_CACHE_TTL_2025_04_11("extended-cache-ttl-2025-04-11")`

    - `CONTEXT_1M_2025_08_07("context-1m-2025-08-07")`

    - `CONTEXT_MANAGEMENT_2025_06_27("context-management-2025-06-27")`

    - `MODEL_CONTEXT_WINDOW_EXCEEDED_2025_08_26("model-context-window-exceeded-2025-08-26")`

    - `SKILLS_2025_10_02("skills-2025-10-02")`

    - `FAST_MODE_2026_02_01("fast-mode-2026-02-01")`

    - `OUTPUT_300K_2026_03_24("output-300k-2026-03-24")`

    - `USER_PROFILES_2026_03_24("user-profiles-2026-03-24")`

    - `ADVISOR_TOOL_2026_03_01("advisor-tool-2026-03-01")`

### Returns

- `class BetaManagedAgentsSessionEvent: A class that can be one of several variants.union`

  Union type for all event types in a session.

  - `class BetaManagedAgentsUserMessageEvent:`

    A user message event in the session conversation.

    - `String id`

      Unique identifier for this event.

    - `List<Content> content`

      Array of content blocks comprising the user message.

      - `class BetaManagedAgentsTextBlock:`

        Regular text content.

        - `String text`

          The text content.

        - `Type type`

          - `TEXT("text")`

      - `class BetaManagedAgentsImageBlock:`

        Image content specified directly as base64 data or as a reference via a URL.

        - `Source source`

          Union type for image source variants.

          - `class BetaManagedAgentsBase64ImageSource:`

            Base64-encoded image data.

            - `String data`

              Base64-encoded image data.

            - `String mediaType`

              MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

            - `Type type`

              - `BASE64("base64")`

          - `class BetaManagedAgentsUrlImageSource:`

            Image referenced by URL.

            - `Type type`

              - `URL("url")`

            - `String url`

              URL of the image to fetch.

          - `class BetaManagedAgentsFileImageSource:`

            Image referenced by file ID.

            - `String fileId`

              ID of a previously uploaded file.

            - `Type type`

              - `FILE("file")`

        - `Type type`

          - `IMAGE("image")`

      - `class BetaManagedAgentsDocumentBlock:`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

        - `Source source`

          Union type for document source variants.

          - `class BetaManagedAgentsBase64DocumentSource:`

            Base64-encoded document data.

            - `String data`

              Base64-encoded document data.

            - `String mediaType`

              MIME type of the document (e.g., "application/pdf").

            - `Type type`

              - `BASE64("base64")`

          - `class BetaManagedAgentsPlainTextDocumentSource:`

            Plain text document content.

            - `String data`

              The plain text content.

            - `MediaType mediaType`

              MIME type of the text content. Must be "text/plain".

              - `TEXT_PLAIN("text/plain")`

            - `Type type`

              - `TEXT("text")`

          - `class BetaManagedAgentsUrlDocumentSource:`

            Document referenced by URL.

            - `Type type`

              - `URL("url")`

            - `String url`

              URL of the document to fetch.

          - `class BetaManagedAgentsFileDocumentSource:`

            Document referenced by file ID.

            - `String fileId`

              ID of a previously uploaded file.

            - `Type type`

              - `FILE("file")`

        - `Type type`

          - `DOCUMENT("document")`

        - `Optional<String> context`

          Additional context about the document for the model.

        - `Optional<String> title`

          The title of the document.

    - `Type type`

      - `USER_MESSAGE("user.message")`

    - `Optional<LocalDateTime> processedAt`

      A timestamp in RFC 3339 format

  - `class BetaManagedAgentsUserInterruptEvent:`

    An interrupt event that pauses agent execution and returns control to the user.

    - `String id`

      Unique identifier for this event.

    - `Type type`

      - `USER_INTERRUPT("user.interrupt")`

    - `Optional<LocalDateTime> processedAt`

      A timestamp in RFC 3339 format

  - `class BetaManagedAgentsUserToolConfirmationEvent:`

    A tool confirmation event that approves or denies a pending tool execution.

    - `String id`

      Unique identifier for this event.

    - `Result result`

      UserToolConfirmationResult enum

      - `ALLOW("allow")`

      - `DENY("deny")`

    - `String toolUseId`

      The id of the `agent.tool_use` or `agent.mcp_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

    - `Type type`

      - `USER_TOOL_CONFIRMATION("user.tool_confirmation")`

    - `Optional<String> denyMessage`

      Optional message providing context for a 'deny' decision. Only allowed when result is 'deny'.

    - `Optional<LocalDateTime> processedAt`

      A timestamp in RFC 3339 format

  - `class BetaManagedAgentsUserCustomToolResultEvent:`

    Event sent by the client providing the result of a custom tool execution.

    - `String id`

      Unique identifier for this event.

    - `String customToolUseId`

      The id of the `agent.custom_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

    - `Type type`

      - `USER_CUSTOM_TOOL_RESULT("user.custom_tool_result")`

    - `Optional<List<Content>> content`

      The result content returned by the tool.

      - `class BetaManagedAgentsTextBlock:`

        Regular text content.

        - `String text`

          The text content.

        - `Type type`

          - `TEXT("text")`

      - `class BetaManagedAgentsImageBlock:`

        Image content specified directly as base64 data or as a reference via a URL.

        - `Source source`

          Union type for image source variants.

          - `class BetaManagedAgentsBase64ImageSource:`

            Base64-encoded image data.

            - `String data`

              Base64-encoded image data.

            - `String mediaType`

              MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

            - `Type type`

              - `BASE64("base64")`

          - `class BetaManagedAgentsUrlImageSource:`

            Image referenced by URL.

            - `Type type`

              - `URL("url")`

            - `String url`

              URL of the image to fetch.

          - `class BetaManagedAgentsFileImageSource:`

            Image referenced by file ID.

            - `String fileId`

              ID of a previously uploaded file.

            - `Type type`

              - `FILE("file")`

        - `Type type`

          - `IMAGE("image")`

      - `class BetaManagedAgentsDocumentBlock:`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

        - `Source source`

          Union type for document source variants.

          - `class BetaManagedAgentsBase64DocumentSource:`

            Base64-encoded document data.

            - `String data`

              Base64-encoded document data.

            - `String mediaType`

              MIME type of the document (e.g., "application/pdf").

            - `Type type`

              - `BASE64("base64")`

          - `class BetaManagedAgentsPlainTextDocumentSource:`

            Plain text document content.

            - `String data`

              The plain text content.

            - `MediaType mediaType`

              MIME type of the text content. Must be "text/plain".

              - `TEXT_PLAIN("text/plain")`

            - `Type type`

              - `TEXT("text")`

          - `class BetaManagedAgentsUrlDocumentSource:`

            Document referenced by URL.

            - `Type type`

              - `URL("url")`

            - `String url`

              URL of the document to fetch.

          - `class BetaManagedAgentsFileDocumentSource:`

            Document referenced by file ID.

            - `String fileId`

              ID of a previously uploaded file.

            - `Type type`

              - `FILE("file")`

        - `Type type`

          - `DOCUMENT("document")`

        - `Optional<String> context`

          Additional context about the document for the model.

        - `Optional<String> title`

          The title of the document.

    - `Optional<Boolean> isError`

      Whether the tool execution resulted in an error.

    - `Optional<LocalDateTime> processedAt`

      A timestamp in RFC 3339 format

  - `class BetaManagedAgentsAgentCustomToolUseEvent:`

    Event emitted when the agent calls a custom tool. The session goes idle until the client sends a `user.custom_tool_result` event with the result.

    - `String id`

      Unique identifier for this event.

    - `Input input`

      Input parameters for the tool call.

    - `String name`

      Name of the custom tool being called.

    - `LocalDateTime processedAt`

      A timestamp in RFC 3339 format

    - `Type type`

      - `AGENT_CUSTOM_TOOL_USE("agent.custom_tool_use")`

  - `class BetaManagedAgentsAgentMessageEvent:`

    An agent response event in the session conversation.

    - `String id`

      Unique identifier for this event.

    - `List<BetaManagedAgentsTextBlock> content`

      Array of text blocks comprising the agent response.

      - `String text`

        The text content.

      - `Type type`

        - `TEXT("text")`

    - `LocalDateTime processedAt`

      A timestamp in RFC 3339 format

    - `Type type`

      - `AGENT_MESSAGE("agent.message")`

  - `class BetaManagedAgentsAgentThinkingEvent:`

    Indicates the agent is making forward progress via extended thinking. A progress signal, not a content carrier.

    - `String id`

      Unique identifier for this event.

    - `LocalDateTime processedAt`

      A timestamp in RFC 3339 format

    - `Type type`

      - `AGENT_THINKING("agent.thinking")`

  - `class BetaManagedAgentsAgentMcpToolUseEvent:`

    Event emitted when the agent invokes a tool provided by an MCP server.

    - `String id`

      Unique identifier for this event.

    - `Input input`

      Input parameters for the tool call.

    - `String mcpServerName`

      Name of the MCP server providing the tool.

    - `String name`

      Name of the MCP tool being used.

    - `LocalDateTime processedAt`

      A timestamp in RFC 3339 format

    - `Type type`

      - `AGENT_MCP_TOOL_USE("agent.mcp_tool_use")`

    - `Optional<EvaluatedPermission> evaluatedPermission`

      AgentEvaluatedPermission enum

      - `ALLOW("allow")`

      - `ASK("ask")`

      - `DENY("deny")`

  - `class BetaManagedAgentsAgentMcpToolResultEvent:`

    Event representing the result of an MCP tool execution.

    - `String id`

      Unique identifier for this event.

    - `String mcpToolUseId`

      The id of the `agent.mcp_tool_use` event this result corresponds to.

    - `LocalDateTime processedAt`

      A timestamp in RFC 3339 format

    - `Type type`

      - `AGENT_MCP_TOOL_RESULT("agent.mcp_tool_result")`

    - `Optional<List<Content>> content`

      The result content returned by the tool.

      - `class BetaManagedAgentsTextBlock:`

        Regular text content.

        - `String text`

          The text content.

        - `Type type`

          - `TEXT("text")`

      - `class BetaManagedAgentsImageBlock:`

        Image content specified directly as base64 data or as a reference via a URL.

        - `Source source`

          Union type for image source variants.

          - `class BetaManagedAgentsBase64ImageSource:`

            Base64-encoded image data.

            - `String data`

              Base64-encoded image data.

            - `String mediaType`

              MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

            - `Type type`

              - `BASE64("base64")`

          - `class BetaManagedAgentsUrlImageSource:`

            Image referenced by URL.

            - `Type type`

              - `URL("url")`

            - `String url`

              URL of the image to fetch.

          - `class BetaManagedAgentsFileImageSource:`

            Image referenced by file ID.

            - `String fileId`

              ID of a previously uploaded file.

            - `Type type`

              - `FILE("file")`

        - `Type type`

          - `IMAGE("image")`

      - `class BetaManagedAgentsDocumentBlock:`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

        - `Source source`

          Union type for document source variants.

          - `class BetaManagedAgentsBase64DocumentSource:`

            Base64-encoded document data.

            - `String data`

              Base64-encoded document data.

            - `String mediaType`

              MIME type of the document (e.g., "application/pdf").

            - `Type type`

              - `BASE64("base64")`

          - `class BetaManagedAgentsPlainTextDocumentSource:`

            Plain text document content.

            - `String data`

              The plain text content.

            - `MediaType mediaType`

              MIME type of the text content. Must be "text/plain".

              - `TEXT_PLAIN("text/plain")`

            - `Type type`

              - `TEXT("text")`

          - `class BetaManagedAgentsUrlDocumentSource:`

            Document referenced by URL.

            - `Type type`

              - `URL("url")`

            - `String url`

              URL of the document to fetch.

          - `class BetaManagedAgentsFileDocumentSource:`

            Document referenced by file ID.

            - `String fileId`

              ID of a previously uploaded file.

            - `Type type`

              - `FILE("file")`

        - `Type type`

          - `DOCUMENT("document")`

        - `Optional<String> context`

          Additional context about the document for the model.

        - `Optional<String> title`

          The title of the document.

    - `Optional<Boolean> isError`

      Whether the tool execution resulted in an error.

  - `class BetaManagedAgentsAgentToolUseEvent:`

    Event emitted when the agent invokes a built-in agent tool.

    - `String id`

      Unique identifier for this event.

    - `Input input`

      Input parameters for the tool call.

    - `String name`

      Name of the agent tool being used.

    - `LocalDateTime processedAt`

      A timestamp in RFC 3339 format

    - `Type type`

      - `AGENT_TOOL_USE("agent.tool_use")`

    - `Optional<EvaluatedPermission> evaluatedPermission`

      AgentEvaluatedPermission enum

      - `ALLOW("allow")`

      - `ASK("ask")`

      - `DENY("deny")`

  - `class BetaManagedAgentsAgentToolResultEvent:`

    Event representing the result of an agent tool execution.

    - `String id`

      Unique identifier for this event.

    - `LocalDateTime processedAt`

      A timestamp in RFC 3339 format

    - `String toolUseId`

      The id of the `agent.tool_use` event this result corresponds to.

    - `Type type`

      - `AGENT_TOOL_RESULT("agent.tool_result")`

    - `Optional<List<Content>> content`

      The result content returned by the tool.

      - `class BetaManagedAgentsTextBlock:`

        Regular text content.

        - `String text`

          The text content.

        - `Type type`

          - `TEXT("text")`

      - `class BetaManagedAgentsImageBlock:`

        Image content specified directly as base64 data or as a reference via a URL.

        - `Source source`

          Union type for image source variants.

          - `class BetaManagedAgentsBase64ImageSource:`

            Base64-encoded image data.

            - `String data`

              Base64-encoded image data.

            - `String mediaType`

              MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

            - `Type type`

              - `BASE64("base64")`

          - `class BetaManagedAgentsUrlImageSource:`

            Image referenced by URL.

            - `Type type`

              - `URL("url")`

            - `String url`

              URL of the image to fetch.

          - `class BetaManagedAgentsFileImageSource:`

            Image referenced by file ID.

            - `String fileId`

              ID of a previously uploaded file.

            - `Type type`

              - `FILE("file")`

        - `Type type`

          - `IMAGE("image")`

      - `class BetaManagedAgentsDocumentBlock:`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

        - `Source source`

          Union type for document source variants.

          - `class BetaManagedAgentsBase64DocumentSource:`

            Base64-encoded document data.

            - `String data`

              Base64-encoded document data.

            - `String mediaType`

              MIME type of the document (e.g., "application/pdf").

            - `Type type`

              - `BASE64("base64")`

          - `class BetaManagedAgentsPlainTextDocumentSource:`

            Plain text document content.

            - `String data`

              The plain text content.

            - `MediaType mediaType`

              MIME type of the text content. Must be "text/plain".

              - `TEXT_PLAIN("text/plain")`

            - `Type type`

              - `TEXT("text")`

          - `class BetaManagedAgentsUrlDocumentSource:`

            Document referenced by URL.

            - `Type type`

              - `URL("url")`

            - `String url`

              URL of the document to fetch.

          - `class BetaManagedAgentsFileDocumentSource:`

            Document referenced by file ID.

            - `String fileId`

              ID of a previously uploaded file.

            - `Type type`

              - `FILE("file")`

        - `Type type`

          - `DOCUMENT("document")`

        - `Optional<String> context`

          Additional context about the document for the model.

        - `Optional<String> title`

          The title of the document.

    - `Optional<Boolean> isError`

      Whether the tool execution resulted in an error.

  - `class BetaManagedAgentsAgentThreadContextCompactedEvent:`

    Indicates that context compaction (summarization) occurred during the session.

    - `String id`

      Unique identifier for this event.

    - `LocalDateTime processedAt`

      A timestamp in RFC 3339 format

    - `Type type`

      - `AGENT_THREAD_CONTEXT_COMPACTED("agent.thread_context_compacted")`

  - `class BetaManagedAgentsSessionErrorEvent:`

    An error event indicating a problem occurred during session execution.

    - `String id`

      Unique identifier for this event.

    - `Error error`

      An unknown or unexpected error occurred during session execution. A fallback variant; clients that don't recognize a new error code can match on `retry_status` and `message` alone.

      - `class BetaManagedAgentsUnknownError:`

        An unknown or unexpected error occurred during session execution. A fallback variant; clients that don't recognize a new error code can match on `retry_status` and `message` alone.

        - `String message`

          Human-readable error description.

        - `RetryStatus retryStatus`

          What the client should do next in response to this error.

          - `class BetaManagedAgentsRetryStatusRetrying:`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

            - `Type type`

              - `RETRYING("retrying")`

          - `class BetaManagedAgentsRetryStatusExhausted:`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

            - `Type type`

              - `EXHAUSTED("exhausted")`

          - `class BetaManagedAgentsRetryStatusTerminal:`

            The session encountered a terminal error and will transition to `terminated` state.

            - `Type type`

              - `TERMINAL("terminal")`

        - `Type type`

          - `UNKNOWN_ERROR("unknown_error")`

      - `class BetaManagedAgentsModelOverloadedError:`

        The model is currently overloaded. Emitted after automatic retries are exhausted.

        - `String message`

          Human-readable error description.

        - `RetryStatus retryStatus`

          What the client should do next in response to this error.

          - `class BetaManagedAgentsRetryStatusRetrying:`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

            - `Type type`

              - `RETRYING("retrying")`

          - `class BetaManagedAgentsRetryStatusExhausted:`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

            - `Type type`

              - `EXHAUSTED("exhausted")`

          - `class BetaManagedAgentsRetryStatusTerminal:`

            The session encountered a terminal error and will transition to `terminated` state.

            - `Type type`

              - `TERMINAL("terminal")`

        - `Type type`

          - `MODEL_OVERLOADED_ERROR("model_overloaded_error")`

      - `class BetaManagedAgentsModelRateLimitedError:`

        The model request was rate-limited.

        - `String message`

          Human-readable error description.

        - `RetryStatus retryStatus`

          What the client should do next in response to this error.

          - `class BetaManagedAgentsRetryStatusRetrying:`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

            - `Type type`

              - `RETRYING("retrying")`

          - `class BetaManagedAgentsRetryStatusExhausted:`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

            - `Type type`

              - `EXHAUSTED("exhausted")`

          - `class BetaManagedAgentsRetryStatusTerminal:`

            The session encountered a terminal error and will transition to `terminated` state.

            - `Type type`

              - `TERMINAL("terminal")`

        - `Type type`

          - `MODEL_RATE_LIMITED_ERROR("model_rate_limited_error")`

      - `class BetaManagedAgentsModelRequestFailedError:`

        A model request failed for a reason other than overload or rate-limiting.

        - `String message`

          Human-readable error description.

        - `RetryStatus retryStatus`

          What the client should do next in response to this error.

          - `class BetaManagedAgentsRetryStatusRetrying:`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

            - `Type type`

              - `RETRYING("retrying")`

          - `class BetaManagedAgentsRetryStatusExhausted:`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

            - `Type type`

              - `EXHAUSTED("exhausted")`

          - `class BetaManagedAgentsRetryStatusTerminal:`

            The session encountered a terminal error and will transition to `terminated` state.

            - `Type type`

              - `TERMINAL("terminal")`

        - `Type type`

          - `MODEL_REQUEST_FAILED_ERROR("model_request_failed_error")`

      - `class BetaManagedAgentsMcpConnectionFailedError:`

        Failed to connect to an MCP server.

        - `String mcpServerName`

          Name of the MCP server that failed to connect.

        - `String message`

          Human-readable error description.

        - `RetryStatus retryStatus`

          What the client should do next in response to this error.

          - `class BetaManagedAgentsRetryStatusRetrying:`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

            - `Type type`

              - `RETRYING("retrying")`

          - `class BetaManagedAgentsRetryStatusExhausted:`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

            - `Type type`

              - `EXHAUSTED("exhausted")`

          - `class BetaManagedAgentsRetryStatusTerminal:`

            The session encountered a terminal error and will transition to `terminated` state.

            - `Type type`

              - `TERMINAL("terminal")`

        - `Type type`

          - `MCP_CONNECTION_FAILED_ERROR("mcp_connection_failed_error")`

      - `class BetaManagedAgentsMcpAuthenticationFailedError:`

        Authentication to an MCP server failed.

        - `String mcpServerName`

          Name of the MCP server that failed authentication.

        - `String message`

          Human-readable error description.

        - `RetryStatus retryStatus`

          What the client should do next in response to this error.

          - `class BetaManagedAgentsRetryStatusRetrying:`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

            - `Type type`

              - `RETRYING("retrying")`

          - `class BetaManagedAgentsRetryStatusExhausted:`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

            - `Type type`

              - `EXHAUSTED("exhausted")`

          - `class BetaManagedAgentsRetryStatusTerminal:`

            The session encountered a terminal error and will transition to `terminated` state.

            - `Type type`

              - `TERMINAL("terminal")`

        - `Type type`

          - `MCP_AUTHENTICATION_FAILED_ERROR("mcp_authentication_failed_error")`

      - `class BetaManagedAgentsBillingError:`

        The caller's organization or workspace cannot make model requests — out of credits or spend limit reached. Retrying with the same credentials will not succeed; the caller must resolve the billing state.

        - `String message`

          Human-readable error description.

        - `RetryStatus retryStatus`

          What the client should do next in response to this error.

          - `class BetaManagedAgentsRetryStatusRetrying:`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

            - `Type type`

              - `RETRYING("retrying")`

          - `class BetaManagedAgentsRetryStatusExhausted:`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

            - `Type type`

              - `EXHAUSTED("exhausted")`

          - `class BetaManagedAgentsRetryStatusTerminal:`

            The session encountered a terminal error and will transition to `terminated` state.

            - `Type type`

              - `TERMINAL("terminal")`

        - `Type type`

          - `BILLING_ERROR("billing_error")`

    - `LocalDateTime processedAt`

      A timestamp in RFC 3339 format

    - `Type type`

      - `SESSION_ERROR("session.error")`

  - `class BetaManagedAgentsSessionStatusRescheduledEvent:`

    Indicates the session is recovering from an error state and is rescheduled for execution.

    - `String id`

      Unique identifier for this event.

    - `LocalDateTime processedAt`

      A timestamp in RFC 3339 format

    - `Type type`

      - `SESSION_STATUS_RESCHEDULED("session.status_rescheduled")`

  - `class BetaManagedAgentsSessionStatusRunningEvent:`

    Indicates the session is actively running and the agent is working.

    - `String id`

      Unique identifier for this event.

    - `LocalDateTime processedAt`

      A timestamp in RFC 3339 format

    - `Type type`

      - `SESSION_STATUS_RUNNING("session.status_running")`

  - `class BetaManagedAgentsSessionStatusIdleEvent:`

    Indicates the agent has paused and is awaiting user input.

    - `String id`

      Unique identifier for this event.

    - `LocalDateTime processedAt`

      A timestamp in RFC 3339 format

    - `StopReason stopReason`

      The agent completed its turn naturally and is ready for the next user message.

      - `class BetaManagedAgentsSessionEndTurn:`

        The agent completed its turn naturally and is ready for the next user message.

        - `Type type`

          - `END_TURN("end_turn")`

      - `class BetaManagedAgentsSessionRequiresAction:`

        The agent is idle waiting on one or more blocking user-input events (tool confirmation, custom tool result, etc.). Resolving all of them transitions the session back to running.

        - `List<String> eventIds`

          The ids of events the agent is blocked on. Resolving fewer than all re-emits `session.status_idle` with the remainder.

        - `Type type`

          - `REQUIRES_ACTION("requires_action")`

      - `class BetaManagedAgentsSessionRetriesExhausted:`

        The turn ended because the retry budget was exhausted (`max_iterations` hit or an error escalated to `retry_status: 'exhausted'`).

        - `Type type`

          - `RETRIES_EXHAUSTED("retries_exhausted")`

    - `Type type`

      - `SESSION_STATUS_IDLE("session.status_idle")`

  - `class BetaManagedAgentsSessionStatusTerminatedEvent:`

    Indicates the session has terminated, either due to an error or completion.

    - `String id`

      Unique identifier for this event.

    - `LocalDateTime processedAt`

      A timestamp in RFC 3339 format

    - `Type type`

      - `SESSION_STATUS_TERMINATED("session.status_terminated")`

  - `class BetaManagedAgentsSpanModelRequestStartEvent:`

    Emitted when a model request is initiated by the agent.

    - `String id`

      Unique identifier for this event.

    - `LocalDateTime processedAt`

      A timestamp in RFC 3339 format

    - `Type type`

      - `SPAN_MODEL_REQUEST_START("span.model_request_start")`

  - `class BetaManagedAgentsSpanModelRequestEndEvent:`

    Emitted when a model request completes.

    - `String id`

      Unique identifier for this event.

    - `Optional<Boolean> isError`

      Whether the model request resulted in an error.

    - `String modelRequestStartId`

      The id of the corresponding `span.model_request_start` event.

    - `BetaManagedAgentsSpanModelUsage modelUsage`

      Token usage for a single model request.

      - `long cacheCreationInputTokens`

        Tokens used to create prompt cache in this request.

      - `long cacheReadInputTokens`

        Tokens read from prompt cache in this request.

      - `long inputTokens`

        Input tokens consumed by this request.

      - `long outputTokens`

        Output tokens generated by this request.

      - `Optional<Speed> speed`

        Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

        - `STANDARD("standard")`

        - `FAST("fast")`

    - `LocalDateTime processedAt`

      A timestamp in RFC 3339 format

    - `Type type`

      - `SPAN_MODEL_REQUEST_END("span.model_request_end")`

  - `class BetaManagedAgentsSessionDeletedEvent:`

    Emitted when a session has been deleted. Terminates any active event stream — no further events will be emitted for this session.

    - `String id`

      Unique identifier for this event.

    - `LocalDateTime processedAt`

      A timestamp in RFC 3339 format

    - `Type type`

      - `SESSION_DELETED("session.deleted")`

### Example

```java
package com.anthropic.example;

import com.anthropic.client.AnthropicClient;
import com.anthropic.client.okhttp.AnthropicOkHttpClient;
import com.anthropic.models.beta.sessions.events.EventListPage;
import com.anthropic.models.beta.sessions.events.EventListParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        AnthropicClient client = AnthropicOkHttpClient.fromEnv();

        EventListPage page = client.beta().sessions().events().list("sesn_011CZkZAtmR3yMPDzynEDxu7");
    }
}
```

## Send

`BetaManagedAgentsSendSessionEvents beta().sessions().events().send(EventSendParamsparams, RequestOptionsrequestOptions = RequestOptions.none())`

**post** `/v1/sessions/{session_id}/events`

Send Events

### Parameters

- `EventSendParams params`

  - `Optional<String> sessionId`

  - `Optional<List<AnthropicBeta>> betas`

    Optional header to specify the beta version(s) you want to use.

    - `MESSAGE_BATCHES_2024_09_24("message-batches-2024-09-24")`

    - `PROMPT_CACHING_2024_07_31("prompt-caching-2024-07-31")`

    - `COMPUTER_USE_2024_10_22("computer-use-2024-10-22")`

    - `COMPUTER_USE_2025_01_24("computer-use-2025-01-24")`

    - `PDFS_2024_09_25("pdfs-2024-09-25")`

    - `TOKEN_COUNTING_2024_11_01("token-counting-2024-11-01")`

    - `TOKEN_EFFICIENT_TOOLS_2025_02_19("token-efficient-tools-2025-02-19")`

    - `OUTPUT_128K_2025_02_19("output-128k-2025-02-19")`

    - `FILES_API_2025_04_14("files-api-2025-04-14")`

    - `MCP_CLIENT_2025_04_04("mcp-client-2025-04-04")`

    - `MCP_CLIENT_2025_11_20("mcp-client-2025-11-20")`

    - `DEV_FULL_THINKING_2025_05_14("dev-full-thinking-2025-05-14")`

    - `INTERLEAVED_THINKING_2025_05_14("interleaved-thinking-2025-05-14")`

    - `CODE_EXECUTION_2025_05_22("code-execution-2025-05-22")`

    - `EXTENDED_CACHE_TTL_2025_04_11("extended-cache-ttl-2025-04-11")`

    - `CONTEXT_1M_2025_08_07("context-1m-2025-08-07")`

    - `CONTEXT_MANAGEMENT_2025_06_27("context-management-2025-06-27")`

    - `MODEL_CONTEXT_WINDOW_EXCEEDED_2025_08_26("model-context-window-exceeded-2025-08-26")`

    - `SKILLS_2025_10_02("skills-2025-10-02")`

    - `FAST_MODE_2026_02_01("fast-mode-2026-02-01")`

    - `OUTPUT_300K_2026_03_24("output-300k-2026-03-24")`

    - `USER_PROFILES_2026_03_24("user-profiles-2026-03-24")`

    - `ADVISOR_TOOL_2026_03_01("advisor-tool-2026-03-01")`

  - `List<BetaManagedAgentsEventParams> events`

    Events to send to the `session`.

    - `class BetaManagedAgentsUserMessageEventParams:`

      Parameters for sending a user message to the session.

      - `List<Content> content`

        Array of content blocks for the user message.

        - `class BetaManagedAgentsTextBlock:`

          Regular text content.

          - `String text`

            The text content.

          - `Type type`

            - `TEXT("text")`

        - `class BetaManagedAgentsImageBlock:`

          Image content specified directly as base64 data or as a reference via a URL.

          - `Source source`

            Union type for image source variants.

            - `class BetaManagedAgentsBase64ImageSource:`

              Base64-encoded image data.

              - `String data`

                Base64-encoded image data.

              - `String mediaType`

                MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

              - `Type type`

                - `BASE64("base64")`

            - `class BetaManagedAgentsUrlImageSource:`

              Image referenced by URL.

              - `Type type`

                - `URL("url")`

              - `String url`

                URL of the image to fetch.

            - `class BetaManagedAgentsFileImageSource:`

              Image referenced by file ID.

              - `String fileId`

                ID of a previously uploaded file.

              - `Type type`

                - `FILE("file")`

          - `Type type`

            - `IMAGE("image")`

        - `class BetaManagedAgentsDocumentBlock:`

          Document content, either specified directly as base64 data, as text, or as a reference via a URL.

          - `Source source`

            Union type for document source variants.

            - `class BetaManagedAgentsBase64DocumentSource:`

              Base64-encoded document data.

              - `String data`

                Base64-encoded document data.

              - `String mediaType`

                MIME type of the document (e.g., "application/pdf").

              - `Type type`

                - `BASE64("base64")`

            - `class BetaManagedAgentsPlainTextDocumentSource:`

              Plain text document content.

              - `String data`

                The plain text content.

              - `MediaType mediaType`

                MIME type of the text content. Must be "text/plain".

                - `TEXT_PLAIN("text/plain")`

              - `Type type`

                - `TEXT("text")`

            - `class BetaManagedAgentsUrlDocumentSource:`

              Document referenced by URL.

              - `Type type`

                - `URL("url")`

              - `String url`

                URL of the document to fetch.

            - `class BetaManagedAgentsFileDocumentSource:`

              Document referenced by file ID.

              - `String fileId`

                ID of a previously uploaded file.

              - `Type type`

                - `FILE("file")`

          - `Type type`

            - `DOCUMENT("document")`

          - `Optional<String> context`

            Additional context about the document for the model.

          - `Optional<String> title`

            The title of the document.

      - `Type type`

        - `USER_MESSAGE("user.message")`

    - `class BetaManagedAgentsUserInterruptEventParams:`

      Parameters for sending an interrupt to pause the agent.

      - `Type type`

        - `USER_INTERRUPT("user.interrupt")`

    - `class BetaManagedAgentsUserToolConfirmationEventParams:`

      Parameters for confirming or denying a tool execution request.

      - `Result result`

        UserToolConfirmationResult enum

        - `ALLOW("allow")`

        - `DENY("deny")`

      - `String toolUseId`

        The id of the `agent.tool_use` or `agent.mcp_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

      - `Type type`

        - `USER_TOOL_CONFIRMATION("user.tool_confirmation")`

      - `Optional<String> denyMessage`

        Optional message providing context for a 'deny' decision. Only allowed when result is 'deny'.

    - `class BetaManagedAgentsUserCustomToolResultEventParams:`

      Parameters for providing the result of a custom tool execution.

      - `String customToolUseId`

        The id of the `agent.custom_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

      - `Type type`

        - `USER_CUSTOM_TOOL_RESULT("user.custom_tool_result")`

      - `Optional<List<Content>> content`

        The result content returned by the tool.

        - `class BetaManagedAgentsTextBlock:`

          Regular text content.

          - `String text`

            The text content.

          - `Type type`

            - `TEXT("text")`

        - `class BetaManagedAgentsImageBlock:`

          Image content specified directly as base64 data or as a reference via a URL.

          - `Source source`

            Union type for image source variants.

            - `class BetaManagedAgentsBase64ImageSource:`

              Base64-encoded image data.

              - `String data`

                Base64-encoded image data.

              - `String mediaType`

                MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

              - `Type type`

                - `BASE64("base64")`

            - `class BetaManagedAgentsUrlImageSource:`

              Image referenced by URL.

              - `Type type`

                - `URL("url")`

              - `String url`

                URL of the image to fetch.

            - `class BetaManagedAgentsFileImageSource:`

              Image referenced by file ID.

              - `String fileId`

                ID of a previously uploaded file.

              - `Type type`

                - `FILE("file")`

          - `Type type`

            - `IMAGE("image")`

        - `class BetaManagedAgentsDocumentBlock:`

          Document content, either specified directly as base64 data, as text, or as a reference via a URL.

          - `Source source`

            Union type for document source variants.

            - `class BetaManagedAgentsBase64DocumentSource:`

              Base64-encoded document data.

              - `String data`

                Base64-encoded document data.

              - `String mediaType`

                MIME type of the document (e.g., "application/pdf").

              - `Type type`

                - `BASE64("base64")`

            - `class BetaManagedAgentsPlainTextDocumentSource:`

              Plain text document content.

              - `String data`

                The plain text content.

              - `MediaType mediaType`

                MIME type of the text content. Must be "text/plain".

                - `TEXT_PLAIN("text/plain")`

              - `Type type`

                - `TEXT("text")`

            - `class BetaManagedAgentsUrlDocumentSource:`

              Document referenced by URL.

              - `Type type`

                - `URL("url")`

              - `String url`

                URL of the document to fetch.

            - `class BetaManagedAgentsFileDocumentSource:`

              Document referenced by file ID.

              - `String fileId`

                ID of a previously uploaded file.

              - `Type type`

                - `FILE("file")`

          - `Type type`

            - `DOCUMENT("document")`

          - `Optional<String> context`

            Additional context about the document for the model.

          - `Optional<String> title`

            The title of the document.

      - `Optional<Boolean> isError`

        Whether the tool execution resulted in an error.

### Returns

- `class BetaManagedAgentsSendSessionEvents:`

  Events that were successfully sent to the session.

  - `Optional<List<Data>> data`

    Sent events

    - `class BetaManagedAgentsUserMessageEvent:`

      A user message event in the session conversation.

      - `String id`

        Unique identifier for this event.

      - `List<Content> content`

        Array of content blocks comprising the user message.

        - `class BetaManagedAgentsTextBlock:`

          Regular text content.

          - `String text`

            The text content.

          - `Type type`

            - `TEXT("text")`

        - `class BetaManagedAgentsImageBlock:`

          Image content specified directly as base64 data or as a reference via a URL.

          - `Source source`

            Union type for image source variants.

            - `class BetaManagedAgentsBase64ImageSource:`

              Base64-encoded image data.

              - `String data`

                Base64-encoded image data.

              - `String mediaType`

                MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

              - `Type type`

                - `BASE64("base64")`

            - `class BetaManagedAgentsUrlImageSource:`

              Image referenced by URL.

              - `Type type`

                - `URL("url")`

              - `String url`

                URL of the image to fetch.

            - `class BetaManagedAgentsFileImageSource:`

              Image referenced by file ID.

              - `String fileId`

                ID of a previously uploaded file.

              - `Type type`

                - `FILE("file")`

          - `Type type`

            - `IMAGE("image")`

        - `class BetaManagedAgentsDocumentBlock:`

          Document content, either specified directly as base64 data, as text, or as a reference via a URL.

          - `Source source`

            Union type for document source variants.

            - `class BetaManagedAgentsBase64DocumentSource:`

              Base64-encoded document data.

              - `String data`

                Base64-encoded document data.

              - `String mediaType`

                MIME type of the document (e.g., "application/pdf").

              - `Type type`

                - `BASE64("base64")`

            - `class BetaManagedAgentsPlainTextDocumentSource:`

              Plain text document content.

              - `String data`

                The plain text content.

              - `MediaType mediaType`

                MIME type of the text content. Must be "text/plain".

                - `TEXT_PLAIN("text/plain")`

              - `Type type`

                - `TEXT("text")`

            - `class BetaManagedAgentsUrlDocumentSource:`

              Document referenced by URL.

              - `Type type`

                - `URL("url")`

              - `String url`

                URL of the document to fetch.

            - `class BetaManagedAgentsFileDocumentSource:`

              Document referenced by file ID.

              - `String fileId`

                ID of a previously uploaded file.

              - `Type type`

                - `FILE("file")`

          - `Type type`

            - `DOCUMENT("document")`

          - `Optional<String> context`

            Additional context about the document for the model.

          - `Optional<String> title`

            The title of the document.

      - `Type type`

        - `USER_MESSAGE("user.message")`

      - `Optional<LocalDateTime> processedAt`

        A timestamp in RFC 3339 format

    - `class BetaManagedAgentsUserInterruptEvent:`

      An interrupt event that pauses agent execution and returns control to the user.

      - `String id`

        Unique identifier for this event.

      - `Type type`

        - `USER_INTERRUPT("user.interrupt")`

      - `Optional<LocalDateTime> processedAt`

        A timestamp in RFC 3339 format

    - `class BetaManagedAgentsUserToolConfirmationEvent:`

      A tool confirmation event that approves or denies a pending tool execution.

      - `String id`

        Unique identifier for this event.

      - `Result result`

        UserToolConfirmationResult enum

        - `ALLOW("allow")`

        - `DENY("deny")`

      - `String toolUseId`

        The id of the `agent.tool_use` or `agent.mcp_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

      - `Type type`

        - `USER_TOOL_CONFIRMATION("user.tool_confirmation")`

      - `Optional<String> denyMessage`

        Optional message providing context for a 'deny' decision. Only allowed when result is 'deny'.

      - `Optional<LocalDateTime> processedAt`

        A timestamp in RFC 3339 format

    - `class BetaManagedAgentsUserCustomToolResultEvent:`

      Event sent by the client providing the result of a custom tool execution.

      - `String id`

        Unique identifier for this event.

      - `String customToolUseId`

        The id of the `agent.custom_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

      - `Type type`

        - `USER_CUSTOM_TOOL_RESULT("user.custom_tool_result")`

      - `Optional<List<Content>> content`

        The result content returned by the tool.

        - `class BetaManagedAgentsTextBlock:`

          Regular text content.

          - `String text`

            The text content.

          - `Type type`

            - `TEXT("text")`

        - `class BetaManagedAgentsImageBlock:`

          Image content specified directly as base64 data or as a reference via a URL.

          - `Source source`

            Union type for image source variants.

            - `class BetaManagedAgentsBase64ImageSource:`

              Base64-encoded image data.

              - `String data`

                Base64-encoded image data.

              - `String mediaType`

                MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

              - `Type type`

                - `BASE64("base64")`

            - `class BetaManagedAgentsUrlImageSource:`

              Image referenced by URL.

              - `Type type`

                - `URL("url")`

              - `String url`

                URL of the image to fetch.

            - `class BetaManagedAgentsFileImageSource:`

              Image referenced by file ID.

              - `String fileId`

                ID of a previously uploaded file.

              - `Type type`

                - `FILE("file")`

          - `Type type`

            - `IMAGE("image")`

        - `class BetaManagedAgentsDocumentBlock:`

          Document content, either specified directly as base64 data, as text, or as a reference via a URL.

          - `Source source`

            Union type for document source variants.

            - `class BetaManagedAgentsBase64DocumentSource:`

              Base64-encoded document data.

              - `String data`

                Base64-encoded document data.

              - `String mediaType`

                MIME type of the document (e.g., "application/pdf").

              - `Type type`

                - `BASE64("base64")`

            - `class BetaManagedAgentsPlainTextDocumentSource:`

              Plain text document content.

              - `String data`

                The plain text content.

              - `MediaType mediaType`

                MIME type of the text content. Must be "text/plain".

                - `TEXT_PLAIN("text/plain")`

              - `Type type`

                - `TEXT("text")`

            - `class BetaManagedAgentsUrlDocumentSource:`

              Document referenced by URL.

              - `Type type`

                - `URL("url")`

              - `String url`

                URL of the document to fetch.

            - `class BetaManagedAgentsFileDocumentSource:`

              Document referenced by file ID.

              - `String fileId`

                ID of a previously uploaded file.

              - `Type type`

                - `FILE("file")`

          - `Type type`

            - `DOCUMENT("document")`

          - `Optional<String> context`

            Additional context about the document for the model.

          - `Optional<String> title`

            The title of the document.

      - `Optional<Boolean> isError`

        Whether the tool execution resulted in an error.

      - `Optional<LocalDateTime> processedAt`

        A timestamp in RFC 3339 format

### Example

```java
package com.anthropic.example;

import com.anthropic.client.AnthropicClient;
import com.anthropic.client.okhttp.AnthropicOkHttpClient;
import com.anthropic.models.beta.sessions.events.BetaManagedAgentsSendSessionEvents;
import com.anthropic.models.beta.sessions.events.BetaManagedAgentsTextBlock;
import com.anthropic.models.beta.sessions.events.BetaManagedAgentsUserMessageEventParams;
import com.anthropic.models.beta.sessions.events.EventSendParams;
import java.util.List;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        AnthropicClient client = AnthropicOkHttpClient.fromEnv();

        EventSendParams params = EventSendParams.builder()
            .sessionId("sesn_011CZkZAtmR3yMPDzynEDxu7")
            .addUserMessageEvent(List.of(BetaManagedAgentsUserMessageEventParams.Content.ofText(BetaManagedAgentsTextBlock.builder()
                .text("Where is my order #1234?")
                .type(BetaManagedAgentsTextBlock.Type.TEXT)
                .build())))
            .build();
        BetaManagedAgentsSendSessionEvents betaManagedAgentsSendSessionEvents = client.beta().sessions().events().send(params);
    }
}
```

## Stream

`BetaManagedAgentsStreamSessionEvents beta().sessions().events().streamStreaming(EventStreamParamsparams = EventStreamParams.none(), RequestOptionsrequestOptions = RequestOptions.none())`

**get** `/v1/sessions/{session_id}/events/stream`

Stream Events

### Parameters

- `EventStreamParams params`

  - `Optional<String> sessionId`

  - `Optional<List<AnthropicBeta>> betas`

    Optional header to specify the beta version(s) you want to use.

    - `MESSAGE_BATCHES_2024_09_24("message-batches-2024-09-24")`

    - `PROMPT_CACHING_2024_07_31("prompt-caching-2024-07-31")`

    - `COMPUTER_USE_2024_10_22("computer-use-2024-10-22")`

    - `COMPUTER_USE_2025_01_24("computer-use-2025-01-24")`

    - `PDFS_2024_09_25("pdfs-2024-09-25")`

    - `TOKEN_COUNTING_2024_11_01("token-counting-2024-11-01")`

    - `TOKEN_EFFICIENT_TOOLS_2025_02_19("token-efficient-tools-2025-02-19")`

    - `OUTPUT_128K_2025_02_19("output-128k-2025-02-19")`

    - `FILES_API_2025_04_14("files-api-2025-04-14")`

    - `MCP_CLIENT_2025_04_04("mcp-client-2025-04-04")`

    - `MCP_CLIENT_2025_11_20("mcp-client-2025-11-20")`

    - `DEV_FULL_THINKING_2025_05_14("dev-full-thinking-2025-05-14")`

    - `INTERLEAVED_THINKING_2025_05_14("interleaved-thinking-2025-05-14")`

    - `CODE_EXECUTION_2025_05_22("code-execution-2025-05-22")`

    - `EXTENDED_CACHE_TTL_2025_04_11("extended-cache-ttl-2025-04-11")`

    - `CONTEXT_1M_2025_08_07("context-1m-2025-08-07")`

    - `CONTEXT_MANAGEMENT_2025_06_27("context-management-2025-06-27")`

    - `MODEL_CONTEXT_WINDOW_EXCEEDED_2025_08_26("model-context-window-exceeded-2025-08-26")`

    - `SKILLS_2025_10_02("skills-2025-10-02")`

    - `FAST_MODE_2026_02_01("fast-mode-2026-02-01")`

    - `OUTPUT_300K_2026_03_24("output-300k-2026-03-24")`

    - `USER_PROFILES_2026_03_24("user-profiles-2026-03-24")`

    - `ADVISOR_TOOL_2026_03_01("advisor-tool-2026-03-01")`

### Returns

- `class BetaManagedAgentsStreamSessionEvents: A class that can be one of several variants.union`

  Server-sent event in the session stream.

  - `class BetaManagedAgentsUserMessageEvent:`

    A user message event in the session conversation.

    - `String id`

      Unique identifier for this event.

    - `List<Content> content`

      Array of content blocks comprising the user message.

      - `class BetaManagedAgentsTextBlock:`

        Regular text content.

        - `String text`

          The text content.

        - `Type type`

          - `TEXT("text")`

      - `class BetaManagedAgentsImageBlock:`

        Image content specified directly as base64 data or as a reference via a URL.

        - `Source source`

          Union type for image source variants.

          - `class BetaManagedAgentsBase64ImageSource:`

            Base64-encoded image data.

            - `String data`

              Base64-encoded image data.

            - `String mediaType`

              MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

            - `Type type`

              - `BASE64("base64")`

          - `class BetaManagedAgentsUrlImageSource:`

            Image referenced by URL.

            - `Type type`

              - `URL("url")`

            - `String url`

              URL of the image to fetch.

          - `class BetaManagedAgentsFileImageSource:`

            Image referenced by file ID.

            - `String fileId`

              ID of a previously uploaded file.

            - `Type type`

              - `FILE("file")`

        - `Type type`

          - `IMAGE("image")`

      - `class BetaManagedAgentsDocumentBlock:`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

        - `Source source`

          Union type for document source variants.

          - `class BetaManagedAgentsBase64DocumentSource:`

            Base64-encoded document data.

            - `String data`

              Base64-encoded document data.

            - `String mediaType`

              MIME type of the document (e.g., "application/pdf").

            - `Type type`

              - `BASE64("base64")`

          - `class BetaManagedAgentsPlainTextDocumentSource:`

            Plain text document content.

            - `String data`

              The plain text content.

            - `MediaType mediaType`

              MIME type of the text content. Must be "text/plain".

              - `TEXT_PLAIN("text/plain")`

            - `Type type`

              - `TEXT("text")`

          - `class BetaManagedAgentsUrlDocumentSource:`

            Document referenced by URL.

            - `Type type`

              - `URL("url")`

            - `String url`

              URL of the document to fetch.

          - `class BetaManagedAgentsFileDocumentSource:`

            Document referenced by file ID.

            - `String fileId`

              ID of a previously uploaded file.

            - `Type type`

              - `FILE("file")`

        - `Type type`

          - `DOCUMENT("document")`

        - `Optional<String> context`

          Additional context about the document for the model.

        - `Optional<String> title`

          The title of the document.

    - `Type type`

      - `USER_MESSAGE("user.message")`

    - `Optional<LocalDateTime> processedAt`

      A timestamp in RFC 3339 format

  - `class BetaManagedAgentsUserInterruptEvent:`

    An interrupt event that pauses agent execution and returns control to the user.

    - `String id`

      Unique identifier for this event.

    - `Type type`

      - `USER_INTERRUPT("user.interrupt")`

    - `Optional<LocalDateTime> processedAt`

      A timestamp in RFC 3339 format

  - `class BetaManagedAgentsUserToolConfirmationEvent:`

    A tool confirmation event that approves or denies a pending tool execution.

    - `String id`

      Unique identifier for this event.

    - `Result result`

      UserToolConfirmationResult enum

      - `ALLOW("allow")`

      - `DENY("deny")`

    - `String toolUseId`

      The id of the `agent.tool_use` or `agent.mcp_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

    - `Type type`

      - `USER_TOOL_CONFIRMATION("user.tool_confirmation")`

    - `Optional<String> denyMessage`

      Optional message providing context for a 'deny' decision. Only allowed when result is 'deny'.

    - `Optional<LocalDateTime> processedAt`

      A timestamp in RFC 3339 format

  - `class BetaManagedAgentsUserCustomToolResultEvent:`

    Event sent by the client providing the result of a custom tool execution.

    - `String id`

      Unique identifier for this event.

    - `String customToolUseId`

      The id of the `agent.custom_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

    - `Type type`

      - `USER_CUSTOM_TOOL_RESULT("user.custom_tool_result")`

    - `Optional<List<Content>> content`

      The result content returned by the tool.

      - `class BetaManagedAgentsTextBlock:`

        Regular text content.

        - `String text`

          The text content.

        - `Type type`

          - `TEXT("text")`

      - `class BetaManagedAgentsImageBlock:`

        Image content specified directly as base64 data or as a reference via a URL.

        - `Source source`

          Union type for image source variants.

          - `class BetaManagedAgentsBase64ImageSource:`

            Base64-encoded image data.

            - `String data`

              Base64-encoded image data.

            - `String mediaType`

              MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

            - `Type type`

              - `BASE64("base64")`

          - `class BetaManagedAgentsUrlImageSource:`

            Image referenced by URL.

            - `Type type`

              - `URL("url")`

            - `String url`

              URL of the image to fetch.

          - `class BetaManagedAgentsFileImageSource:`

            Image referenced by file ID.

            - `String fileId`

              ID of a previously uploaded file.

            - `Type type`

              - `FILE("file")`

        - `Type type`

          - `IMAGE("image")`

      - `class BetaManagedAgentsDocumentBlock:`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

        - `Source source`

          Union type for document source variants.

          - `class BetaManagedAgentsBase64DocumentSource:`

            Base64-encoded document data.

            - `String data`

              Base64-encoded document data.

            - `String mediaType`

              MIME type of the document (e.g., "application/pdf").

            - `Type type`

              - `BASE64("base64")`

          - `class BetaManagedAgentsPlainTextDocumentSource:`

            Plain text document content.

            - `String data`

              The plain text content.

            - `MediaType mediaType`

              MIME type of the text content. Must be "text/plain".

              - `TEXT_PLAIN("text/plain")`

            - `Type type`

              - `TEXT("text")`

          - `class BetaManagedAgentsUrlDocumentSource:`

            Document referenced by URL.

            - `Type type`

              - `URL("url")`

            - `String url`

              URL of the document to fetch.

          - `class BetaManagedAgentsFileDocumentSource:`

            Document referenced by file ID.

            - `String fileId`

              ID of a previously uploaded file.

            - `Type type`

              - `FILE("file")`

        - `Type type`

          - `DOCUMENT("document")`

        - `Optional<String> context`

          Additional context about the document for the model.

        - `Optional<String> title`

          The title of the document.

    - `Optional<Boolean> isError`

      Whether the tool execution resulted in an error.

    - `Optional<LocalDateTime> processedAt`

      A timestamp in RFC 3339 format

  - `class BetaManagedAgentsAgentCustomToolUseEvent:`

    Event emitted when the agent calls a custom tool. The session goes idle until the client sends a `user.custom_tool_result` event with the result.

    - `String id`

      Unique identifier for this event.

    - `Input input`

      Input parameters for the tool call.

    - `String name`

      Name of the custom tool being called.

    - `LocalDateTime processedAt`

      A timestamp in RFC 3339 format

    - `Type type`

      - `AGENT_CUSTOM_TOOL_USE("agent.custom_tool_use")`

  - `class BetaManagedAgentsAgentMessageEvent:`

    An agent response event in the session conversation.

    - `String id`

      Unique identifier for this event.

    - `List<BetaManagedAgentsTextBlock> content`

      Array of text blocks comprising the agent response.

      - `String text`

        The text content.

      - `Type type`

        - `TEXT("text")`

    - `LocalDateTime processedAt`

      A timestamp in RFC 3339 format

    - `Type type`

      - `AGENT_MESSAGE("agent.message")`

  - `class BetaManagedAgentsAgentThinkingEvent:`

    Indicates the agent is making forward progress via extended thinking. A progress signal, not a content carrier.

    - `String id`

      Unique identifier for this event.

    - `LocalDateTime processedAt`

      A timestamp in RFC 3339 format

    - `Type type`

      - `AGENT_THINKING("agent.thinking")`

  - `class BetaManagedAgentsAgentMcpToolUseEvent:`

    Event emitted when the agent invokes a tool provided by an MCP server.

    - `String id`

      Unique identifier for this event.

    - `Input input`

      Input parameters for the tool call.

    - `String mcpServerName`

      Name of the MCP server providing the tool.

    - `String name`

      Name of the MCP tool being used.

    - `LocalDateTime processedAt`

      A timestamp in RFC 3339 format

    - `Type type`

      - `AGENT_MCP_TOOL_USE("agent.mcp_tool_use")`

    - `Optional<EvaluatedPermission> evaluatedPermission`

      AgentEvaluatedPermission enum

      - `ALLOW("allow")`

      - `ASK("ask")`

      - `DENY("deny")`

  - `class BetaManagedAgentsAgentMcpToolResultEvent:`

    Event representing the result of an MCP tool execution.

    - `String id`

      Unique identifier for this event.

    - `String mcpToolUseId`

      The id of the `agent.mcp_tool_use` event this result corresponds to.

    - `LocalDateTime processedAt`

      A timestamp in RFC 3339 format

    - `Type type`

      - `AGENT_MCP_TOOL_RESULT("agent.mcp_tool_result")`

    - `Optional<List<Content>> content`

      The result content returned by the tool.

      - `class BetaManagedAgentsTextBlock:`

        Regular text content.

        - `String text`

          The text content.

        - `Type type`

          - `TEXT("text")`

      - `class BetaManagedAgentsImageBlock:`

        Image content specified directly as base64 data or as a reference via a URL.

        - `Source source`

          Union type for image source variants.

          - `class BetaManagedAgentsBase64ImageSource:`

            Base64-encoded image data.

            - `String data`

              Base64-encoded image data.

            - `String mediaType`

              MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

            - `Type type`

              - `BASE64("base64")`

          - `class BetaManagedAgentsUrlImageSource:`

            Image referenced by URL.

            - `Type type`

              - `URL("url")`

            - `String url`

              URL of the image to fetch.

          - `class BetaManagedAgentsFileImageSource:`

            Image referenced by file ID.

            - `String fileId`

              ID of a previously uploaded file.

            - `Type type`

              - `FILE("file")`

        - `Type type`

          - `IMAGE("image")`

      - `class BetaManagedAgentsDocumentBlock:`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

        - `Source source`

          Union type for document source variants.

          - `class BetaManagedAgentsBase64DocumentSource:`

            Base64-encoded document data.

            - `String data`

              Base64-encoded document data.

            - `String mediaType`

              MIME type of the document (e.g., "application/pdf").

            - `Type type`

              - `BASE64("base64")`

          - `class BetaManagedAgentsPlainTextDocumentSource:`

            Plain text document content.

            - `String data`

              The plain text content.

            - `MediaType mediaType`

              MIME type of the text content. Must be "text/plain".

              - `TEXT_PLAIN("text/plain")`

            - `Type type`

              - `TEXT("text")`

          - `class BetaManagedAgentsUrlDocumentSource:`

            Document referenced by URL.

            - `Type type`

              - `URL("url")`

            - `String url`

              URL of the document to fetch.

          - `class BetaManagedAgentsFileDocumentSource:`

            Document referenced by file ID.

            - `String fileId`

              ID of a previously uploaded file.

            - `Type type`

              - `FILE("file")`

        - `Type type`

          - `DOCUMENT("document")`

        - `Optional<String> context`

          Additional context about the document for the model.

        - `Optional<String> title`

          The title of the document.

    - `Optional<Boolean> isError`

      Whether the tool execution resulted in an error.

  - `class BetaManagedAgentsAgentToolUseEvent:`

    Event emitted when the agent invokes a built-in agent tool.

    - `String id`

      Unique identifier for this event.

    - `Input input`

      Input parameters for the tool call.

    - `String name`

      Name of the agent tool being used.

    - `LocalDateTime processedAt`

      A timestamp in RFC 3339 format

    - `Type type`

      - `AGENT_TOOL_USE("agent.tool_use")`

    - `Optional<EvaluatedPermission> evaluatedPermission`

      AgentEvaluatedPermission enum

      - `ALLOW("allow")`

      - `ASK("ask")`

      - `DENY("deny")`

  - `class BetaManagedAgentsAgentToolResultEvent:`

    Event representing the result of an agent tool execution.

    - `String id`

      Unique identifier for this event.

    - `LocalDateTime processedAt`

      A timestamp in RFC 3339 format

    - `String toolUseId`

      The id of the `agent.tool_use` event this result corresponds to.

    - `Type type`

      - `AGENT_TOOL_RESULT("agent.tool_result")`

    - `Optional<List<Content>> content`

      The result content returned by the tool.

      - `class BetaManagedAgentsTextBlock:`

        Regular text content.

        - `String text`

          The text content.

        - `Type type`

          - `TEXT("text")`

      - `class BetaManagedAgentsImageBlock:`

        Image content specified directly as base64 data or as a reference via a URL.

        - `Source source`

          Union type for image source variants.

          - `class BetaManagedAgentsBase64ImageSource:`

            Base64-encoded image data.

            - `String data`

              Base64-encoded image data.

            - `String mediaType`

              MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

            - `Type type`

              - `BASE64("base64")`

          - `class BetaManagedAgentsUrlImageSource:`

            Image referenced by URL.

            - `Type type`

              - `URL("url")`

            - `String url`

              URL of the image to fetch.

          - `class BetaManagedAgentsFileImageSource:`

            Image referenced by file ID.

            - `String fileId`

              ID of a previously uploaded file.

            - `Type type`

              - `FILE("file")`

        - `Type type`

          - `IMAGE("image")`

      - `class BetaManagedAgentsDocumentBlock:`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

        - `Source source`

          Union type for document source variants.

          - `class BetaManagedAgentsBase64DocumentSource:`

            Base64-encoded document data.

            - `String data`

              Base64-encoded document data.

            - `String mediaType`

              MIME type of the document (e.g., "application/pdf").

            - `Type type`

              - `BASE64("base64")`

          - `class BetaManagedAgentsPlainTextDocumentSource:`

            Plain text document content.

            - `String data`

              The plain text content.

            - `MediaType mediaType`

              MIME type of the text content. Must be "text/plain".

              - `TEXT_PLAIN("text/plain")`

            - `Type type`

              - `TEXT("text")`

          - `class BetaManagedAgentsUrlDocumentSource:`

            Document referenced by URL.

            - `Type type`

              - `URL("url")`

            - `String url`

              URL of the document to fetch.

          - `class BetaManagedAgentsFileDocumentSource:`

            Document referenced by file ID.

            - `String fileId`

              ID of a previously uploaded file.

            - `Type type`

              - `FILE("file")`

        - `Type type`

          - `DOCUMENT("document")`

        - `Optional<String> context`

          Additional context about the document for the model.

        - `Optional<String> title`

          The title of the document.

    - `Optional<Boolean> isError`

      Whether the tool execution resulted in an error.

  - `class BetaManagedAgentsAgentThreadContextCompactedEvent:`

    Indicates that context compaction (summarization) occurred during the session.

    - `String id`

      Unique identifier for this event.

    - `LocalDateTime processedAt`

      A timestamp in RFC 3339 format

    - `Type type`

      - `AGENT_THREAD_CONTEXT_COMPACTED("agent.thread_context_compacted")`

  - `class BetaManagedAgentsSessionErrorEvent:`

    An error event indicating a problem occurred during session execution.

    - `String id`

      Unique identifier for this event.

    - `Error error`

      An unknown or unexpected error occurred during session execution. A fallback variant; clients that don't recognize a new error code can match on `retry_status` and `message` alone.

      - `class BetaManagedAgentsUnknownError:`

        An unknown or unexpected error occurred during session execution. A fallback variant; clients that don't recognize a new error code can match on `retry_status` and `message` alone.

        - `String message`

          Human-readable error description.

        - `RetryStatus retryStatus`

          What the client should do next in response to this error.

          - `class BetaManagedAgentsRetryStatusRetrying:`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

            - `Type type`

              - `RETRYING("retrying")`

          - `class BetaManagedAgentsRetryStatusExhausted:`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

            - `Type type`

              - `EXHAUSTED("exhausted")`

          - `class BetaManagedAgentsRetryStatusTerminal:`

            The session encountered a terminal error and will transition to `terminated` state.

            - `Type type`

              - `TERMINAL("terminal")`

        - `Type type`

          - `UNKNOWN_ERROR("unknown_error")`

      - `class BetaManagedAgentsModelOverloadedError:`

        The model is currently overloaded. Emitted after automatic retries are exhausted.

        - `String message`

          Human-readable error description.

        - `RetryStatus retryStatus`

          What the client should do next in response to this error.

          - `class BetaManagedAgentsRetryStatusRetrying:`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

            - `Type type`

              - `RETRYING("retrying")`

          - `class BetaManagedAgentsRetryStatusExhausted:`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

            - `Type type`

              - `EXHAUSTED("exhausted")`

          - `class BetaManagedAgentsRetryStatusTerminal:`

            The session encountered a terminal error and will transition to `terminated` state.

            - `Type type`

              - `TERMINAL("terminal")`

        - `Type type`

          - `MODEL_OVERLOADED_ERROR("model_overloaded_error")`

      - `class BetaManagedAgentsModelRateLimitedError:`

        The model request was rate-limited.

        - `String message`

          Human-readable error description.

        - `RetryStatus retryStatus`

          What the client should do next in response to this error.

          - `class BetaManagedAgentsRetryStatusRetrying:`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

            - `Type type`

              - `RETRYING("retrying")`

          - `class BetaManagedAgentsRetryStatusExhausted:`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

            - `Type type`

              - `EXHAUSTED("exhausted")`

          - `class BetaManagedAgentsRetryStatusTerminal:`

            The session encountered a terminal error and will transition to `terminated` state.

            - `Type type`

              - `TERMINAL("terminal")`

        - `Type type`

          - `MODEL_RATE_LIMITED_ERROR("model_rate_limited_error")`

      - `class BetaManagedAgentsModelRequestFailedError:`

        A model request failed for a reason other than overload or rate-limiting.

        - `String message`

          Human-readable error description.

        - `RetryStatus retryStatus`

          What the client should do next in response to this error.

          - `class BetaManagedAgentsRetryStatusRetrying:`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

            - `Type type`

              - `RETRYING("retrying")`

          - `class BetaManagedAgentsRetryStatusExhausted:`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

            - `Type type`

              - `EXHAUSTED("exhausted")`

          - `class BetaManagedAgentsRetryStatusTerminal:`

            The session encountered a terminal error and will transition to `terminated` state.

            - `Type type`

              - `TERMINAL("terminal")`

        - `Type type`

          - `MODEL_REQUEST_FAILED_ERROR("model_request_failed_error")`

      - `class BetaManagedAgentsMcpConnectionFailedError:`

        Failed to connect to an MCP server.

        - `String mcpServerName`

          Name of the MCP server that failed to connect.

        - `String message`

          Human-readable error description.

        - `RetryStatus retryStatus`

          What the client should do next in response to this error.

          - `class BetaManagedAgentsRetryStatusRetrying:`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

            - `Type type`

              - `RETRYING("retrying")`

          - `class BetaManagedAgentsRetryStatusExhausted:`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

            - `Type type`

              - `EXHAUSTED("exhausted")`

          - `class BetaManagedAgentsRetryStatusTerminal:`

            The session encountered a terminal error and will transition to `terminated` state.

            - `Type type`

              - `TERMINAL("terminal")`

        - `Type type`

          - `MCP_CONNECTION_FAILED_ERROR("mcp_connection_failed_error")`

      - `class BetaManagedAgentsMcpAuthenticationFailedError:`

        Authentication to an MCP server failed.

        - `String mcpServerName`

          Name of the MCP server that failed authentication.

        - `String message`

          Human-readable error description.

        - `RetryStatus retryStatus`

          What the client should do next in response to this error.

          - `class BetaManagedAgentsRetryStatusRetrying:`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

            - `Type type`

              - `RETRYING("retrying")`

          - `class BetaManagedAgentsRetryStatusExhausted:`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

            - `Type type`

              - `EXHAUSTED("exhausted")`

          - `class BetaManagedAgentsRetryStatusTerminal:`

            The session encountered a terminal error and will transition to `terminated` state.

            - `Type type`

              - `TERMINAL("terminal")`

        - `Type type`

          - `MCP_AUTHENTICATION_FAILED_ERROR("mcp_authentication_failed_error")`

      - `class BetaManagedAgentsBillingError:`

        The caller's organization or workspace cannot make model requests — out of credits or spend limit reached. Retrying with the same credentials will not succeed; the caller must resolve the billing state.

        - `String message`

          Human-readable error description.

        - `RetryStatus retryStatus`

          What the client should do next in response to this error.

          - `class BetaManagedAgentsRetryStatusRetrying:`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

            - `Type type`

              - `RETRYING("retrying")`

          - `class BetaManagedAgentsRetryStatusExhausted:`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

            - `Type type`

              - `EXHAUSTED("exhausted")`

          - `class BetaManagedAgentsRetryStatusTerminal:`

            The session encountered a terminal error and will transition to `terminated` state.

            - `Type type`

              - `TERMINAL("terminal")`

        - `Type type`

          - `BILLING_ERROR("billing_error")`

    - `LocalDateTime processedAt`

      A timestamp in RFC 3339 format

    - `Type type`

      - `SESSION_ERROR("session.error")`

  - `class BetaManagedAgentsSessionStatusRescheduledEvent:`

    Indicates the session is recovering from an error state and is rescheduled for execution.

    - `String id`

      Unique identifier for this event.

    - `LocalDateTime processedAt`

      A timestamp in RFC 3339 format

    - `Type type`

      - `SESSION_STATUS_RESCHEDULED("session.status_rescheduled")`

  - `class BetaManagedAgentsSessionStatusRunningEvent:`

    Indicates the session is actively running and the agent is working.

    - `String id`

      Unique identifier for this event.

    - `LocalDateTime processedAt`

      A timestamp in RFC 3339 format

    - `Type type`

      - `SESSION_STATUS_RUNNING("session.status_running")`

  - `class BetaManagedAgentsSessionStatusIdleEvent:`

    Indicates the agent has paused and is awaiting user input.

    - `String id`

      Unique identifier for this event.

    - `LocalDateTime processedAt`

      A timestamp in RFC 3339 format

    - `StopReason stopReason`

      The agent completed its turn naturally and is ready for the next user message.

      - `class BetaManagedAgentsSessionEndTurn:`

        The agent completed its turn naturally and is ready for the next user message.

        - `Type type`

          - `END_TURN("end_turn")`

      - `class BetaManagedAgentsSessionRequiresAction:`

        The agent is idle waiting on one or more blocking user-input events (tool confirmation, custom tool result, etc.). Resolving all of them transitions the session back to running.

        - `List<String> eventIds`

          The ids of events the agent is blocked on. Resolving fewer than all re-emits `session.status_idle` with the remainder.

        - `Type type`

          - `REQUIRES_ACTION("requires_action")`

      - `class BetaManagedAgentsSessionRetriesExhausted:`

        The turn ended because the retry budget was exhausted (`max_iterations` hit or an error escalated to `retry_status: 'exhausted'`).

        - `Type type`

          - `RETRIES_EXHAUSTED("retries_exhausted")`

    - `Type type`

      - `SESSION_STATUS_IDLE("session.status_idle")`

  - `class BetaManagedAgentsSessionStatusTerminatedEvent:`

    Indicates the session has terminated, either due to an error or completion.

    - `String id`

      Unique identifier for this event.

    - `LocalDateTime processedAt`

      A timestamp in RFC 3339 format

    - `Type type`

      - `SESSION_STATUS_TERMINATED("session.status_terminated")`

  - `class BetaManagedAgentsSpanModelRequestStartEvent:`

    Emitted when a model request is initiated by the agent.

    - `String id`

      Unique identifier for this event.

    - `LocalDateTime processedAt`

      A timestamp in RFC 3339 format

    - `Type type`

      - `SPAN_MODEL_REQUEST_START("span.model_request_start")`

  - `class BetaManagedAgentsSpanModelRequestEndEvent:`

    Emitted when a model request completes.

    - `String id`

      Unique identifier for this event.

    - `Optional<Boolean> isError`

      Whether the model request resulted in an error.

    - `String modelRequestStartId`

      The id of the corresponding `span.model_request_start` event.

    - `BetaManagedAgentsSpanModelUsage modelUsage`

      Token usage for a single model request.

      - `long cacheCreationInputTokens`

        Tokens used to create prompt cache in this request.

      - `long cacheReadInputTokens`

        Tokens read from prompt cache in this request.

      - `long inputTokens`

        Input tokens consumed by this request.

      - `long outputTokens`

        Output tokens generated by this request.

      - `Optional<Speed> speed`

        Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

        - `STANDARD("standard")`

        - `FAST("fast")`

    - `LocalDateTime processedAt`

      A timestamp in RFC 3339 format

    - `Type type`

      - `SPAN_MODEL_REQUEST_END("span.model_request_end")`

  - `class BetaManagedAgentsSessionDeletedEvent:`

    Emitted when a session has been deleted. Terminates any active event stream — no further events will be emitted for this session.

    - `String id`

      Unique identifier for this event.

    - `LocalDateTime processedAt`

      A timestamp in RFC 3339 format

    - `Type type`

      - `SESSION_DELETED("session.deleted")`

### Example

```java
package com.anthropic.example;

import com.anthropic.client.AnthropicClient;
import com.anthropic.client.okhttp.AnthropicOkHttpClient;
import com.anthropic.core.http.StreamResponse;
import com.anthropic.models.beta.sessions.events.BetaManagedAgentsStreamSessionEvents;
import com.anthropic.models.beta.sessions.events.EventStreamParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        AnthropicClient client = AnthropicOkHttpClient.fromEnv();

        StreamResponse<BetaManagedAgentsStreamSessionEvents> betaManagedAgentsStreamSessionEvents = client.beta().sessions().events().streamStreaming("sesn_011CZkZAtmR3yMPDzynEDxu7");
    }
}
```

## Domain Types

### Beta Managed Agents Agent Custom Tool Use Event

- `class BetaManagedAgentsAgentCustomToolUseEvent:`

  Event emitted when the agent calls a custom tool. The session goes idle until the client sends a `user.custom_tool_result` event with the result.

  - `String id`

    Unique identifier for this event.

  - `Input input`

    Input parameters for the tool call.

  - `String name`

    Name of the custom tool being called.

  - `LocalDateTime processedAt`

    A timestamp in RFC 3339 format

  - `Type type`

    - `AGENT_CUSTOM_TOOL_USE("agent.custom_tool_use")`

### Beta Managed Agents Agent MCP Tool Result Event

- `class BetaManagedAgentsAgentMcpToolResultEvent:`

  Event representing the result of an MCP tool execution.

  - `String id`

    Unique identifier for this event.

  - `String mcpToolUseId`

    The id of the `agent.mcp_tool_use` event this result corresponds to.

  - `LocalDateTime processedAt`

    A timestamp in RFC 3339 format

  - `Type type`

    - `AGENT_MCP_TOOL_RESULT("agent.mcp_tool_result")`

  - `Optional<List<Content>> content`

    The result content returned by the tool.

    - `class BetaManagedAgentsTextBlock:`

      Regular text content.

      - `String text`

        The text content.

      - `Type type`

        - `TEXT("text")`

    - `class BetaManagedAgentsImageBlock:`

      Image content specified directly as base64 data or as a reference via a URL.

      - `Source source`

        Union type for image source variants.

        - `class BetaManagedAgentsBase64ImageSource:`

          Base64-encoded image data.

          - `String data`

            Base64-encoded image data.

          - `String mediaType`

            MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

          - `Type type`

            - `BASE64("base64")`

        - `class BetaManagedAgentsUrlImageSource:`

          Image referenced by URL.

          - `Type type`

            - `URL("url")`

          - `String url`

            URL of the image to fetch.

        - `class BetaManagedAgentsFileImageSource:`

          Image referenced by file ID.

          - `String fileId`

            ID of a previously uploaded file.

          - `Type type`

            - `FILE("file")`

      - `Type type`

        - `IMAGE("image")`

    - `class BetaManagedAgentsDocumentBlock:`

      Document content, either specified directly as base64 data, as text, or as a reference via a URL.

      - `Source source`

        Union type for document source variants.

        - `class BetaManagedAgentsBase64DocumentSource:`

          Base64-encoded document data.

          - `String data`

            Base64-encoded document data.

          - `String mediaType`

            MIME type of the document (e.g., "application/pdf").

          - `Type type`

            - `BASE64("base64")`

        - `class BetaManagedAgentsPlainTextDocumentSource:`

          Plain text document content.

          - `String data`

            The plain text content.

          - `MediaType mediaType`

            MIME type of the text content. Must be "text/plain".

            - `TEXT_PLAIN("text/plain")`

          - `Type type`

            - `TEXT("text")`

        - `class BetaManagedAgentsUrlDocumentSource:`

          Document referenced by URL.

          - `Type type`

            - `URL("url")`

          - `String url`

            URL of the document to fetch.

        - `class BetaManagedAgentsFileDocumentSource:`

          Document referenced by file ID.

          - `String fileId`

            ID of a previously uploaded file.

          - `Type type`

            - `FILE("file")`

      - `Type type`

        - `DOCUMENT("document")`

      - `Optional<String> context`

        Additional context about the document for the model.

      - `Optional<String> title`

        The title of the document.

  - `Optional<Boolean> isError`

    Whether the tool execution resulted in an error.

### Beta Managed Agents Agent MCP Tool Use Event

- `class BetaManagedAgentsAgentMcpToolUseEvent:`

  Event emitted when the agent invokes a tool provided by an MCP server.

  - `String id`

    Unique identifier for this event.

  - `Input input`

    Input parameters for the tool call.

  - `String mcpServerName`

    Name of the MCP server providing the tool.

  - `String name`

    Name of the MCP tool being used.

  - `LocalDateTime processedAt`

    A timestamp in RFC 3339 format

  - `Type type`

    - `AGENT_MCP_TOOL_USE("agent.mcp_tool_use")`

  - `Optional<EvaluatedPermission> evaluatedPermission`

    AgentEvaluatedPermission enum

    - `ALLOW("allow")`

    - `ASK("ask")`

    - `DENY("deny")`

### Beta Managed Agents Agent Message Event

- `class BetaManagedAgentsAgentMessageEvent:`

  An agent response event in the session conversation.

  - `String id`

    Unique identifier for this event.

  - `List<BetaManagedAgentsTextBlock> content`

    Array of text blocks comprising the agent response.

    - `String text`

      The text content.

    - `Type type`

      - `TEXT("text")`

  - `LocalDateTime processedAt`

    A timestamp in RFC 3339 format

  - `Type type`

    - `AGENT_MESSAGE("agent.message")`

### Beta Managed Agents Agent Thinking Event

- `class BetaManagedAgentsAgentThinkingEvent:`

  Indicates the agent is making forward progress via extended thinking. A progress signal, not a content carrier.

  - `String id`

    Unique identifier for this event.

  - `LocalDateTime processedAt`

    A timestamp in RFC 3339 format

  - `Type type`

    - `AGENT_THINKING("agent.thinking")`

### Beta Managed Agents Agent Thread Context Compacted Event

- `class BetaManagedAgentsAgentThreadContextCompactedEvent:`

  Indicates that context compaction (summarization) occurred during the session.

  - `String id`

    Unique identifier for this event.

  - `LocalDateTime processedAt`

    A timestamp in RFC 3339 format

  - `Type type`

    - `AGENT_THREAD_CONTEXT_COMPACTED("agent.thread_context_compacted")`

### Beta Managed Agents Agent Tool Result Event

- `class BetaManagedAgentsAgentToolResultEvent:`

  Event representing the result of an agent tool execution.

  - `String id`

    Unique identifier for this event.

  - `LocalDateTime processedAt`

    A timestamp in RFC 3339 format

  - `String toolUseId`

    The id of the `agent.tool_use` event this result corresponds to.

  - `Type type`

    - `AGENT_TOOL_RESULT("agent.tool_result")`

  - `Optional<List<Content>> content`

    The result content returned by the tool.

    - `class BetaManagedAgentsTextBlock:`

      Regular text content.

      - `String text`

        The text content.

      - `Type type`

        - `TEXT("text")`

    - `class BetaManagedAgentsImageBlock:`

      Image content specified directly as base64 data or as a reference via a URL.

      - `Source source`

        Union type for image source variants.

        - `class BetaManagedAgentsBase64ImageSource:`

          Base64-encoded image data.

          - `String data`

            Base64-encoded image data.

          - `String mediaType`

            MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

          - `Type type`

            - `BASE64("base64")`

        - `class BetaManagedAgentsUrlImageSource:`

          Image referenced by URL.

          - `Type type`

            - `URL("url")`

          - `String url`

            URL of the image to fetch.

        - `class BetaManagedAgentsFileImageSource:`

          Image referenced by file ID.

          - `String fileId`

            ID of a previously uploaded file.

          - `Type type`

            - `FILE("file")`

      - `Type type`

        - `IMAGE("image")`

    - `class BetaManagedAgentsDocumentBlock:`

      Document content, either specified directly as base64 data, as text, or as a reference via a URL.

      - `Source source`

        Union type for document source variants.

        - `class BetaManagedAgentsBase64DocumentSource:`

          Base64-encoded document data.

          - `String data`

            Base64-encoded document data.

          - `String mediaType`

            MIME type of the document (e.g., "application/pdf").

          - `Type type`

            - `BASE64("base64")`

        - `class BetaManagedAgentsPlainTextDocumentSource:`

          Plain text document content.

          - `String data`

            The plain text content.

          - `MediaType mediaType`

            MIME type of the text content. Must be "text/plain".

            - `TEXT_PLAIN("text/plain")`

          - `Type type`

            - `TEXT("text")`

        - `class BetaManagedAgentsUrlDocumentSource:`

          Document referenced by URL.

          - `Type type`

            - `URL("url")`

          - `String url`

            URL of the document to fetch.

        - `class BetaManagedAgentsFileDocumentSource:`

          Document referenced by file ID.

          - `String fileId`

            ID of a previously uploaded file.

          - `Type type`

            - `FILE("file")`

      - `Type type`

        - `DOCUMENT("document")`

      - `Optional<String> context`

        Additional context about the document for the model.

      - `Optional<String> title`

        The title of the document.

  - `Optional<Boolean> isError`

    Whether the tool execution resulted in an error.

### Beta Managed Agents Agent Tool Use Event

- `class BetaManagedAgentsAgentToolUseEvent:`

  Event emitted when the agent invokes a built-in agent tool.

  - `String id`

    Unique identifier for this event.

  - `Input input`

    Input parameters for the tool call.

  - `String name`

    Name of the agent tool being used.

  - `LocalDateTime processedAt`

    A timestamp in RFC 3339 format

  - `Type type`

    - `AGENT_TOOL_USE("agent.tool_use")`

  - `Optional<EvaluatedPermission> evaluatedPermission`

    AgentEvaluatedPermission enum

    - `ALLOW("allow")`

    - `ASK("ask")`

    - `DENY("deny")`

### Beta Managed Agents Base64 Document Source

- `class BetaManagedAgentsBase64DocumentSource:`

  Base64-encoded document data.

  - `String data`

    Base64-encoded document data.

  - `String mediaType`

    MIME type of the document (e.g., "application/pdf").

  - `Type type`

    - `BASE64("base64")`

### Beta Managed Agents Base64 Image Source

- `class BetaManagedAgentsBase64ImageSource:`

  Base64-encoded image data.

  - `String data`

    Base64-encoded image data.

  - `String mediaType`

    MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

  - `Type type`

    - `BASE64("base64")`

### Beta Managed Agents Billing Error

- `class BetaManagedAgentsBillingError:`

  The caller's organization or workspace cannot make model requests — out of credits or spend limit reached. Retrying with the same credentials will not succeed; the caller must resolve the billing state.

  - `String message`

    Human-readable error description.

  - `RetryStatus retryStatus`

    What the client should do next in response to this error.

    - `class BetaManagedAgentsRetryStatusRetrying:`

      The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

      - `Type type`

        - `RETRYING("retrying")`

    - `class BetaManagedAgentsRetryStatusExhausted:`

      This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

      - `Type type`

        - `EXHAUSTED("exhausted")`

    - `class BetaManagedAgentsRetryStatusTerminal:`

      The session encountered a terminal error and will transition to `terminated` state.

      - `Type type`

        - `TERMINAL("terminal")`

  - `Type type`

    - `BILLING_ERROR("billing_error")`

### Beta Managed Agents Document Block

- `class BetaManagedAgentsDocumentBlock:`

  Document content, either specified directly as base64 data, as text, or as a reference via a URL.

  - `Source source`

    Union type for document source variants.

    - `class BetaManagedAgentsBase64DocumentSource:`

      Base64-encoded document data.

      - `String data`

        Base64-encoded document data.

      - `String mediaType`

        MIME type of the document (e.g., "application/pdf").

      - `Type type`

        - `BASE64("base64")`

    - `class BetaManagedAgentsPlainTextDocumentSource:`

      Plain text document content.

      - `String data`

        The plain text content.

      - `MediaType mediaType`

        MIME type of the text content. Must be "text/plain".

        - `TEXT_PLAIN("text/plain")`

      - `Type type`

        - `TEXT("text")`

    - `class BetaManagedAgentsUrlDocumentSource:`

      Document referenced by URL.

      - `Type type`

        - `URL("url")`

      - `String url`

        URL of the document to fetch.

    - `class BetaManagedAgentsFileDocumentSource:`

      Document referenced by file ID.

      - `String fileId`

        ID of a previously uploaded file.

      - `Type type`

        - `FILE("file")`

  - `Type type`

    - `DOCUMENT("document")`

  - `Optional<String> context`

    Additional context about the document for the model.

  - `Optional<String> title`

    The title of the document.

### Beta Managed Agents Event Params

- `class BetaManagedAgentsEventParams: A class that can be one of several variants.union`

  Union type for event parameters that can be sent to a session.

  - `class BetaManagedAgentsUserMessageEventParams:`

    Parameters for sending a user message to the session.

    - `List<Content> content`

      Array of content blocks for the user message.

      - `class BetaManagedAgentsTextBlock:`

        Regular text content.

        - `String text`

          The text content.

        - `Type type`

          - `TEXT("text")`

      - `class BetaManagedAgentsImageBlock:`

        Image content specified directly as base64 data or as a reference via a URL.

        - `Source source`

          Union type for image source variants.

          - `class BetaManagedAgentsBase64ImageSource:`

            Base64-encoded image data.

            - `String data`

              Base64-encoded image data.

            - `String mediaType`

              MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

            - `Type type`

              - `BASE64("base64")`

          - `class BetaManagedAgentsUrlImageSource:`

            Image referenced by URL.

            - `Type type`

              - `URL("url")`

            - `String url`

              URL of the image to fetch.

          - `class BetaManagedAgentsFileImageSource:`

            Image referenced by file ID.

            - `String fileId`

              ID of a previously uploaded file.

            - `Type type`

              - `FILE("file")`

        - `Type type`

          - `IMAGE("image")`

      - `class BetaManagedAgentsDocumentBlock:`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

        - `Source source`

          Union type for document source variants.

          - `class BetaManagedAgentsBase64DocumentSource:`

            Base64-encoded document data.

            - `String data`

              Base64-encoded document data.

            - `String mediaType`

              MIME type of the document (e.g., "application/pdf").

            - `Type type`

              - `BASE64("base64")`

          - `class BetaManagedAgentsPlainTextDocumentSource:`

            Plain text document content.

            - `String data`

              The plain text content.

            - `MediaType mediaType`

              MIME type of the text content. Must be "text/plain".

              - `TEXT_PLAIN("text/plain")`

            - `Type type`

              - `TEXT("text")`

          - `class BetaManagedAgentsUrlDocumentSource:`

            Document referenced by URL.

            - `Type type`

              - `URL("url")`

            - `String url`

              URL of the document to fetch.

          - `class BetaManagedAgentsFileDocumentSource:`

            Document referenced by file ID.

            - `String fileId`

              ID of a previously uploaded file.

            - `Type type`

              - `FILE("file")`

        - `Type type`

          - `DOCUMENT("document")`

        - `Optional<String> context`

          Additional context about the document for the model.

        - `Optional<String> title`

          The title of the document.

    - `Type type`

      - `USER_MESSAGE("user.message")`

  - `class BetaManagedAgentsUserInterruptEventParams:`

    Parameters for sending an interrupt to pause the agent.

    - `Type type`

      - `USER_INTERRUPT("user.interrupt")`

  - `class BetaManagedAgentsUserToolConfirmationEventParams:`

    Parameters for confirming or denying a tool execution request.

    - `Result result`

      UserToolConfirmationResult enum

      - `ALLOW("allow")`

      - `DENY("deny")`

    - `String toolUseId`

      The id of the `agent.tool_use` or `agent.mcp_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

    - `Type type`

      - `USER_TOOL_CONFIRMATION("user.tool_confirmation")`

    - `Optional<String> denyMessage`

      Optional message providing context for a 'deny' decision. Only allowed when result is 'deny'.

  - `class BetaManagedAgentsUserCustomToolResultEventParams:`

    Parameters for providing the result of a custom tool execution.

    - `String customToolUseId`

      The id of the `agent.custom_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

    - `Type type`

      - `USER_CUSTOM_TOOL_RESULT("user.custom_tool_result")`

    - `Optional<List<Content>> content`

      The result content returned by the tool.

      - `class BetaManagedAgentsTextBlock:`

        Regular text content.

        - `String text`

          The text content.

        - `Type type`

          - `TEXT("text")`

      - `class BetaManagedAgentsImageBlock:`

        Image content specified directly as base64 data or as a reference via a URL.

        - `Source source`

          Union type for image source variants.

          - `class BetaManagedAgentsBase64ImageSource:`

            Base64-encoded image data.

            - `String data`

              Base64-encoded image data.

            - `String mediaType`

              MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

            - `Type type`

              - `BASE64("base64")`

          - `class BetaManagedAgentsUrlImageSource:`

            Image referenced by URL.

            - `Type type`

              - `URL("url")`

            - `String url`

              URL of the image to fetch.

          - `class BetaManagedAgentsFileImageSource:`

            Image referenced by file ID.

            - `String fileId`

              ID of a previously uploaded file.

            - `Type type`

              - `FILE("file")`

        - `Type type`

          - `IMAGE("image")`

      - `class BetaManagedAgentsDocumentBlock:`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

        - `Source source`

          Union type for document source variants.

          - `class BetaManagedAgentsBase64DocumentSource:`

            Base64-encoded document data.

            - `String data`

              Base64-encoded document data.

            - `String mediaType`

              MIME type of the document (e.g., "application/pdf").

            - `Type type`

              - `BASE64("base64")`

          - `class BetaManagedAgentsPlainTextDocumentSource:`

            Plain text document content.

            - `String data`

              The plain text content.

            - `MediaType mediaType`

              MIME type of the text content. Must be "text/plain".

              - `TEXT_PLAIN("text/plain")`

            - `Type type`

              - `TEXT("text")`

          - `class BetaManagedAgentsUrlDocumentSource:`

            Document referenced by URL.

            - `Type type`

              - `URL("url")`

            - `String url`

              URL of the document to fetch.

          - `class BetaManagedAgentsFileDocumentSource:`

            Document referenced by file ID.

            - `String fileId`

              ID of a previously uploaded file.

            - `Type type`

              - `FILE("file")`

        - `Type type`

          - `DOCUMENT("document")`

        - `Optional<String> context`

          Additional context about the document for the model.

        - `Optional<String> title`

          The title of the document.

    - `Optional<Boolean> isError`

      Whether the tool execution resulted in an error.

### Beta Managed Agents File Document Source

- `class BetaManagedAgentsFileDocumentSource:`

  Document referenced by file ID.

  - `String fileId`

    ID of a previously uploaded file.

  - `Type type`

    - `FILE("file")`

### Beta Managed Agents File Image Source

- `class BetaManagedAgentsFileImageSource:`

  Image referenced by file ID.

  - `String fileId`

    ID of a previously uploaded file.

  - `Type type`

    - `FILE("file")`

### Beta Managed Agents Image Block

- `class BetaManagedAgentsImageBlock:`

  Image content specified directly as base64 data or as a reference via a URL.

  - `Source source`

    Union type for image source variants.

    - `class BetaManagedAgentsBase64ImageSource:`

      Base64-encoded image data.

      - `String data`

        Base64-encoded image data.

      - `String mediaType`

        MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

      - `Type type`

        - `BASE64("base64")`

    - `class BetaManagedAgentsUrlImageSource:`

      Image referenced by URL.

      - `Type type`

        - `URL("url")`

      - `String url`

        URL of the image to fetch.

    - `class BetaManagedAgentsFileImageSource:`

      Image referenced by file ID.

      - `String fileId`

        ID of a previously uploaded file.

      - `Type type`

        - `FILE("file")`

  - `Type type`

    - `IMAGE("image")`

### Beta Managed Agents MCP Authentication Failed Error

- `class BetaManagedAgentsMcpAuthenticationFailedError:`

  Authentication to an MCP server failed.

  - `String mcpServerName`

    Name of the MCP server that failed authentication.

  - `String message`

    Human-readable error description.

  - `RetryStatus retryStatus`

    What the client should do next in response to this error.

    - `class BetaManagedAgentsRetryStatusRetrying:`

      The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

      - `Type type`

        - `RETRYING("retrying")`

    - `class BetaManagedAgentsRetryStatusExhausted:`

      This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

      - `Type type`

        - `EXHAUSTED("exhausted")`

    - `class BetaManagedAgentsRetryStatusTerminal:`

      The session encountered a terminal error and will transition to `terminated` state.

      - `Type type`

        - `TERMINAL("terminal")`

  - `Type type`

    - `MCP_AUTHENTICATION_FAILED_ERROR("mcp_authentication_failed_error")`

### Beta Managed Agents MCP Connection Failed Error

- `class BetaManagedAgentsMcpConnectionFailedError:`

  Failed to connect to an MCP server.

  - `String mcpServerName`

    Name of the MCP server that failed to connect.

  - `String message`

    Human-readable error description.

  - `RetryStatus retryStatus`

    What the client should do next in response to this error.

    - `class BetaManagedAgentsRetryStatusRetrying:`

      The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

      - `Type type`

        - `RETRYING("retrying")`

    - `class BetaManagedAgentsRetryStatusExhausted:`

      This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

      - `Type type`

        - `EXHAUSTED("exhausted")`

    - `class BetaManagedAgentsRetryStatusTerminal:`

      The session encountered a terminal error and will transition to `terminated` state.

      - `Type type`

        - `TERMINAL("terminal")`

  - `Type type`

    - `MCP_CONNECTION_FAILED_ERROR("mcp_connection_failed_error")`

### Beta Managed Agents Model Overloaded Error

- `class BetaManagedAgentsModelOverloadedError:`

  The model is currently overloaded. Emitted after automatic retries are exhausted.

  - `String message`

    Human-readable error description.

  - `RetryStatus retryStatus`

    What the client should do next in response to this error.

    - `class BetaManagedAgentsRetryStatusRetrying:`

      The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

      - `Type type`

        - `RETRYING("retrying")`

    - `class BetaManagedAgentsRetryStatusExhausted:`

      This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

      - `Type type`

        - `EXHAUSTED("exhausted")`

    - `class BetaManagedAgentsRetryStatusTerminal:`

      The session encountered a terminal error and will transition to `terminated` state.

      - `Type type`

        - `TERMINAL("terminal")`

  - `Type type`

    - `MODEL_OVERLOADED_ERROR("model_overloaded_error")`

### Beta Managed Agents Model Rate Limited Error

- `class BetaManagedAgentsModelRateLimitedError:`

  The model request was rate-limited.

  - `String message`

    Human-readable error description.

  - `RetryStatus retryStatus`

    What the client should do next in response to this error.

    - `class BetaManagedAgentsRetryStatusRetrying:`

      The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

      - `Type type`

        - `RETRYING("retrying")`

    - `class BetaManagedAgentsRetryStatusExhausted:`

      This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

      - `Type type`

        - `EXHAUSTED("exhausted")`

    - `class BetaManagedAgentsRetryStatusTerminal:`

      The session encountered a terminal error and will transition to `terminated` state.

      - `Type type`

        - `TERMINAL("terminal")`

  - `Type type`

    - `MODEL_RATE_LIMITED_ERROR("model_rate_limited_error")`

### Beta Managed Agents Model Request Failed Error

- `class BetaManagedAgentsModelRequestFailedError:`

  A model request failed for a reason other than overload or rate-limiting.

  - `String message`

    Human-readable error description.

  - `RetryStatus retryStatus`

    What the client should do next in response to this error.

    - `class BetaManagedAgentsRetryStatusRetrying:`

      The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

      - `Type type`

        - `RETRYING("retrying")`

    - `class BetaManagedAgentsRetryStatusExhausted:`

      This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

      - `Type type`

        - `EXHAUSTED("exhausted")`

    - `class BetaManagedAgentsRetryStatusTerminal:`

      The session encountered a terminal error and will transition to `terminated` state.

      - `Type type`

        - `TERMINAL("terminal")`

  - `Type type`

    - `MODEL_REQUEST_FAILED_ERROR("model_request_failed_error")`

### Beta Managed Agents Plain Text Document Source

- `class BetaManagedAgentsPlainTextDocumentSource:`

  Plain text document content.

  - `String data`

    The plain text content.

  - `MediaType mediaType`

    MIME type of the text content. Must be "text/plain".

    - `TEXT_PLAIN("text/plain")`

  - `Type type`

    - `TEXT("text")`

### Beta Managed Agents Retry Status Exhausted

- `class BetaManagedAgentsRetryStatusExhausted:`

  This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

  - `Type type`

    - `EXHAUSTED("exhausted")`

### Beta Managed Agents Retry Status Retrying

- `class BetaManagedAgentsRetryStatusRetrying:`

  The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

  - `Type type`

    - `RETRYING("retrying")`

### Beta Managed Agents Retry Status Terminal

- `class BetaManagedAgentsRetryStatusTerminal:`

  The session encountered a terminal error and will transition to `terminated` state.

  - `Type type`

    - `TERMINAL("terminal")`

### Beta Managed Agents Send Session Events

- `class BetaManagedAgentsSendSessionEvents:`

  Events that were successfully sent to the session.

  - `Optional<List<Data>> data`

    Sent events

    - `class BetaManagedAgentsUserMessageEvent:`

      A user message event in the session conversation.

      - `String id`

        Unique identifier for this event.

      - `List<Content> content`

        Array of content blocks comprising the user message.

        - `class BetaManagedAgentsTextBlock:`

          Regular text content.

          - `String text`

            The text content.

          - `Type type`

            - `TEXT("text")`

        - `class BetaManagedAgentsImageBlock:`

          Image content specified directly as base64 data or as a reference via a URL.

          - `Source source`

            Union type for image source variants.

            - `class BetaManagedAgentsBase64ImageSource:`

              Base64-encoded image data.

              - `String data`

                Base64-encoded image data.

              - `String mediaType`

                MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

              - `Type type`

                - `BASE64("base64")`

            - `class BetaManagedAgentsUrlImageSource:`

              Image referenced by URL.

              - `Type type`

                - `URL("url")`

              - `String url`

                URL of the image to fetch.

            - `class BetaManagedAgentsFileImageSource:`

              Image referenced by file ID.

              - `String fileId`

                ID of a previously uploaded file.

              - `Type type`

                - `FILE("file")`

          - `Type type`

            - `IMAGE("image")`

        - `class BetaManagedAgentsDocumentBlock:`

          Document content, either specified directly as base64 data, as text, or as a reference via a URL.

          - `Source source`

            Union type for document source variants.

            - `class BetaManagedAgentsBase64DocumentSource:`

              Base64-encoded document data.

              - `String data`

                Base64-encoded document data.

              - `String mediaType`

                MIME type of the document (e.g., "application/pdf").

              - `Type type`

                - `BASE64("base64")`

            - `class BetaManagedAgentsPlainTextDocumentSource:`

              Plain text document content.

              - `String data`

                The plain text content.

              - `MediaType mediaType`

                MIME type of the text content. Must be "text/plain".

                - `TEXT_PLAIN("text/plain")`

              - `Type type`

                - `TEXT("text")`

            - `class BetaManagedAgentsUrlDocumentSource:`

              Document referenced by URL.

              - `Type type`

                - `URL("url")`

              - `String url`

                URL of the document to fetch.

            - `class BetaManagedAgentsFileDocumentSource:`

              Document referenced by file ID.

              - `String fileId`

                ID of a previously uploaded file.

              - `Type type`

                - `FILE("file")`

          - `Type type`

            - `DOCUMENT("document")`

          - `Optional<String> context`

            Additional context about the document for the model.

          - `Optional<String> title`

            The title of the document.

      - `Type type`

        - `USER_MESSAGE("user.message")`

      - `Optional<LocalDateTime> processedAt`

        A timestamp in RFC 3339 format

    - `class BetaManagedAgentsUserInterruptEvent:`

      An interrupt event that pauses agent execution and returns control to the user.

      - `String id`

        Unique identifier for this event.

      - `Type type`

        - `USER_INTERRUPT("user.interrupt")`

      - `Optional<LocalDateTime> processedAt`

        A timestamp in RFC 3339 format

    - `class BetaManagedAgentsUserToolConfirmationEvent:`

      A tool confirmation event that approves or denies a pending tool execution.

      - `String id`

        Unique identifier for this event.

      - `Result result`

        UserToolConfirmationResult enum

        - `ALLOW("allow")`

        - `DENY("deny")`

      - `String toolUseId`

        The id of the `agent.tool_use` or `agent.mcp_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

      - `Type type`

        - `USER_TOOL_CONFIRMATION("user.tool_confirmation")`

      - `Optional<String> denyMessage`

        Optional message providing context for a 'deny' decision. Only allowed when result is 'deny'.

      - `Optional<LocalDateTime> processedAt`

        A timestamp in RFC 3339 format

    - `class BetaManagedAgentsUserCustomToolResultEvent:`

      Event sent by the client providing the result of a custom tool execution.

      - `String id`

        Unique identifier for this event.

      - `String customToolUseId`

        The id of the `agent.custom_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

      - `Type type`

        - `USER_CUSTOM_TOOL_RESULT("user.custom_tool_result")`

      - `Optional<List<Content>> content`

        The result content returned by the tool.

        - `class BetaManagedAgentsTextBlock:`

          Regular text content.

          - `String text`

            The text content.

          - `Type type`

            - `TEXT("text")`

        - `class BetaManagedAgentsImageBlock:`

          Image content specified directly as base64 data or as a reference via a URL.

          - `Source source`

            Union type for image source variants.

            - `class BetaManagedAgentsBase64ImageSource:`

              Base64-encoded image data.

              - `String data`

                Base64-encoded image data.

              - `String mediaType`

                MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

              - `Type type`

                - `BASE64("base64")`

            - `class BetaManagedAgentsUrlImageSource:`

              Image referenced by URL.

              - `Type type`

                - `URL("url")`

              - `String url`

                URL of the image to fetch.

            - `class BetaManagedAgentsFileImageSource:`

              Image referenced by file ID.

              - `String fileId`

                ID of a previously uploaded file.

              - `Type type`

                - `FILE("file")`

          - `Type type`

            - `IMAGE("image")`

        - `class BetaManagedAgentsDocumentBlock:`

          Document content, either specified directly as base64 data, as text, or as a reference via a URL.

          - `Source source`

            Union type for document source variants.

            - `class BetaManagedAgentsBase64DocumentSource:`

              Base64-encoded document data.

              - `String data`

                Base64-encoded document data.

              - `String mediaType`

                MIME type of the document (e.g., "application/pdf").

              - `Type type`

                - `BASE64("base64")`

            - `class BetaManagedAgentsPlainTextDocumentSource:`

              Plain text document content.

              - `String data`

                The plain text content.

              - `MediaType mediaType`

                MIME type of the text content. Must be "text/plain".

                - `TEXT_PLAIN("text/plain")`

              - `Type type`

                - `TEXT("text")`

            - `class BetaManagedAgentsUrlDocumentSource:`

              Document referenced by URL.

              - `Type type`

                - `URL("url")`

              - `String url`

                URL of the document to fetch.

            - `class BetaManagedAgentsFileDocumentSource:`

              Document referenced by file ID.

              - `String fileId`

                ID of a previously uploaded file.

              - `Type type`

                - `FILE("file")`

          - `Type type`

            - `DOCUMENT("document")`

          - `Optional<String> context`

            Additional context about the document for the model.

          - `Optional<String> title`

            The title of the document.

      - `Optional<Boolean> isError`

        Whether the tool execution resulted in an error.

      - `Optional<LocalDateTime> processedAt`

        A timestamp in RFC 3339 format

### Beta Managed Agents Session Deleted Event

- `class BetaManagedAgentsSessionDeletedEvent:`

  Emitted when a session has been deleted. Terminates any active event stream — no further events will be emitted for this session.

  - `String id`

    Unique identifier for this event.

  - `LocalDateTime processedAt`

    A timestamp in RFC 3339 format

  - `Type type`

    - `SESSION_DELETED("session.deleted")`

### Beta Managed Agents Session End Turn

- `class BetaManagedAgentsSessionEndTurn:`

  The agent completed its turn naturally and is ready for the next user message.

  - `Type type`

    - `END_TURN("end_turn")`

### Beta Managed Agents Session Error Event

- `class BetaManagedAgentsSessionErrorEvent:`

  An error event indicating a problem occurred during session execution.

  - `String id`

    Unique identifier for this event.

  - `Error error`

    An unknown or unexpected error occurred during session execution. A fallback variant; clients that don't recognize a new error code can match on `retry_status` and `message` alone.

    - `class BetaManagedAgentsUnknownError:`

      An unknown or unexpected error occurred during session execution. A fallback variant; clients that don't recognize a new error code can match on `retry_status` and `message` alone.

      - `String message`

        Human-readable error description.

      - `RetryStatus retryStatus`

        What the client should do next in response to this error.

        - `class BetaManagedAgentsRetryStatusRetrying:`

          The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

          - `Type type`

            - `RETRYING("retrying")`

        - `class BetaManagedAgentsRetryStatusExhausted:`

          This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

          - `Type type`

            - `EXHAUSTED("exhausted")`

        - `class BetaManagedAgentsRetryStatusTerminal:`

          The session encountered a terminal error and will transition to `terminated` state.

          - `Type type`

            - `TERMINAL("terminal")`

      - `Type type`

        - `UNKNOWN_ERROR("unknown_error")`

    - `class BetaManagedAgentsModelOverloadedError:`

      The model is currently overloaded. Emitted after automatic retries are exhausted.

      - `String message`

        Human-readable error description.

      - `RetryStatus retryStatus`

        What the client should do next in response to this error.

        - `class BetaManagedAgentsRetryStatusRetrying:`

          The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

          - `Type type`

            - `RETRYING("retrying")`

        - `class BetaManagedAgentsRetryStatusExhausted:`

          This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

          - `Type type`

            - `EXHAUSTED("exhausted")`

        - `class BetaManagedAgentsRetryStatusTerminal:`

          The session encountered a terminal error and will transition to `terminated` state.

          - `Type type`

            - `TERMINAL("terminal")`

      - `Type type`

        - `MODEL_OVERLOADED_ERROR("model_overloaded_error")`

    - `class BetaManagedAgentsModelRateLimitedError:`

      The model request was rate-limited.

      - `String message`

        Human-readable error description.

      - `RetryStatus retryStatus`

        What the client should do next in response to this error.

        - `class BetaManagedAgentsRetryStatusRetrying:`

          The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

          - `Type type`

            - `RETRYING("retrying")`

        - `class BetaManagedAgentsRetryStatusExhausted:`

          This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

          - `Type type`

            - `EXHAUSTED("exhausted")`

        - `class BetaManagedAgentsRetryStatusTerminal:`

          The session encountered a terminal error and will transition to `terminated` state.

          - `Type type`

            - `TERMINAL("terminal")`

      - `Type type`

        - `MODEL_RATE_LIMITED_ERROR("model_rate_limited_error")`

    - `class BetaManagedAgentsModelRequestFailedError:`

      A model request failed for a reason other than overload or rate-limiting.

      - `String message`

        Human-readable error description.

      - `RetryStatus retryStatus`

        What the client should do next in response to this error.

        - `class BetaManagedAgentsRetryStatusRetrying:`

          The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

          - `Type type`

            - `RETRYING("retrying")`

        - `class BetaManagedAgentsRetryStatusExhausted:`

          This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

          - `Type type`

            - `EXHAUSTED("exhausted")`

        - `class BetaManagedAgentsRetryStatusTerminal:`

          The session encountered a terminal error and will transition to `terminated` state.

          - `Type type`

            - `TERMINAL("terminal")`

      - `Type type`

        - `MODEL_REQUEST_FAILED_ERROR("model_request_failed_error")`

    - `class BetaManagedAgentsMcpConnectionFailedError:`

      Failed to connect to an MCP server.

      - `String mcpServerName`

        Name of the MCP server that failed to connect.

      - `String message`

        Human-readable error description.

      - `RetryStatus retryStatus`

        What the client should do next in response to this error.

        - `class BetaManagedAgentsRetryStatusRetrying:`

          The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

          - `Type type`

            - `RETRYING("retrying")`

        - `class BetaManagedAgentsRetryStatusExhausted:`

          This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

          - `Type type`

            - `EXHAUSTED("exhausted")`

        - `class BetaManagedAgentsRetryStatusTerminal:`

          The session encountered a terminal error and will transition to `terminated` state.

          - `Type type`

            - `TERMINAL("terminal")`

      - `Type type`

        - `MCP_CONNECTION_FAILED_ERROR("mcp_connection_failed_error")`

    - `class BetaManagedAgentsMcpAuthenticationFailedError:`

      Authentication to an MCP server failed.

      - `String mcpServerName`

        Name of the MCP server that failed authentication.

      - `String message`

        Human-readable error description.

      - `RetryStatus retryStatus`

        What the client should do next in response to this error.

        - `class BetaManagedAgentsRetryStatusRetrying:`

          The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

          - `Type type`

            - `RETRYING("retrying")`

        - `class BetaManagedAgentsRetryStatusExhausted:`

          This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

          - `Type type`

            - `EXHAUSTED("exhausted")`

        - `class BetaManagedAgentsRetryStatusTerminal:`

          The session encountered a terminal error and will transition to `terminated` state.

          - `Type type`

            - `TERMINAL("terminal")`

      - `Type type`

        - `MCP_AUTHENTICATION_FAILED_ERROR("mcp_authentication_failed_error")`

    - `class BetaManagedAgentsBillingError:`

      The caller's organization or workspace cannot make model requests — out of credits or spend limit reached. Retrying with the same credentials will not succeed; the caller must resolve the billing state.

      - `String message`

        Human-readable error description.

      - `RetryStatus retryStatus`

        What the client should do next in response to this error.

        - `class BetaManagedAgentsRetryStatusRetrying:`

          The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

          - `Type type`

            - `RETRYING("retrying")`

        - `class BetaManagedAgentsRetryStatusExhausted:`

          This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

          - `Type type`

            - `EXHAUSTED("exhausted")`

        - `class BetaManagedAgentsRetryStatusTerminal:`

          The session encountered a terminal error and will transition to `terminated` state.

          - `Type type`

            - `TERMINAL("terminal")`

      - `Type type`

        - `BILLING_ERROR("billing_error")`

  - `LocalDateTime processedAt`

    A timestamp in RFC 3339 format

  - `Type type`

    - `SESSION_ERROR("session.error")`

### Beta Managed Agents Session Event

- `class BetaManagedAgentsSessionEvent: A class that can be one of several variants.union`

  Union type for all event types in a session.

  - `class BetaManagedAgentsUserMessageEvent:`

    A user message event in the session conversation.

    - `String id`

      Unique identifier for this event.

    - `List<Content> content`

      Array of content blocks comprising the user message.

      - `class BetaManagedAgentsTextBlock:`

        Regular text content.

        - `String text`

          The text content.

        - `Type type`

          - `TEXT("text")`

      - `class BetaManagedAgentsImageBlock:`

        Image content specified directly as base64 data or as a reference via a URL.

        - `Source source`

          Union type for image source variants.

          - `class BetaManagedAgentsBase64ImageSource:`

            Base64-encoded image data.

            - `String data`

              Base64-encoded image data.

            - `String mediaType`

              MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

            - `Type type`

              - `BASE64("base64")`

          - `class BetaManagedAgentsUrlImageSource:`

            Image referenced by URL.

            - `Type type`

              - `URL("url")`

            - `String url`

              URL of the image to fetch.

          - `class BetaManagedAgentsFileImageSource:`

            Image referenced by file ID.

            - `String fileId`

              ID of a previously uploaded file.

            - `Type type`

              - `FILE("file")`

        - `Type type`

          - `IMAGE("image")`

      - `class BetaManagedAgentsDocumentBlock:`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

        - `Source source`

          Union type for document source variants.

          - `class BetaManagedAgentsBase64DocumentSource:`

            Base64-encoded document data.

            - `String data`

              Base64-encoded document data.

            - `String mediaType`

              MIME type of the document (e.g., "application/pdf").

            - `Type type`

              - `BASE64("base64")`

          - `class BetaManagedAgentsPlainTextDocumentSource:`

            Plain text document content.

            - `String data`

              The plain text content.

            - `MediaType mediaType`

              MIME type of the text content. Must be "text/plain".

              - `TEXT_PLAIN("text/plain")`

            - `Type type`

              - `TEXT("text")`

          - `class BetaManagedAgentsUrlDocumentSource:`

            Document referenced by URL.

            - `Type type`

              - `URL("url")`

            - `String url`

              URL of the document to fetch.

          - `class BetaManagedAgentsFileDocumentSource:`

            Document referenced by file ID.

            - `String fileId`

              ID of a previously uploaded file.

            - `Type type`

              - `FILE("file")`

        - `Type type`

          - `DOCUMENT("document")`

        - `Optional<String> context`

          Additional context about the document for the model.

        - `Optional<String> title`

          The title of the document.

    - `Type type`

      - `USER_MESSAGE("user.message")`

    - `Optional<LocalDateTime> processedAt`

      A timestamp in RFC 3339 format

  - `class BetaManagedAgentsUserInterruptEvent:`

    An interrupt event that pauses agent execution and returns control to the user.

    - `String id`

      Unique identifier for this event.

    - `Type type`

      - `USER_INTERRUPT("user.interrupt")`

    - `Optional<LocalDateTime> processedAt`

      A timestamp in RFC 3339 format

  - `class BetaManagedAgentsUserToolConfirmationEvent:`

    A tool confirmation event that approves or denies a pending tool execution.

    - `String id`

      Unique identifier for this event.

    - `Result result`

      UserToolConfirmationResult enum

      - `ALLOW("allow")`

      - `DENY("deny")`

    - `String toolUseId`

      The id of the `agent.tool_use` or `agent.mcp_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

    - `Type type`

      - `USER_TOOL_CONFIRMATION("user.tool_confirmation")`

    - `Optional<String> denyMessage`

      Optional message providing context for a 'deny' decision. Only allowed when result is 'deny'.

    - `Optional<LocalDateTime> processedAt`

      A timestamp in RFC 3339 format

  - `class BetaManagedAgentsUserCustomToolResultEvent:`

    Event sent by the client providing the result of a custom tool execution.

    - `String id`

      Unique identifier for this event.

    - `String customToolUseId`

      The id of the `agent.custom_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

    - `Type type`

      - `USER_CUSTOM_TOOL_RESULT("user.custom_tool_result")`

    - `Optional<List<Content>> content`

      The result content returned by the tool.

      - `class BetaManagedAgentsTextBlock:`

        Regular text content.

        - `String text`

          The text content.

        - `Type type`

          - `TEXT("text")`

      - `class BetaManagedAgentsImageBlock:`

        Image content specified directly as base64 data or as a reference via a URL.

        - `Source source`

          Union type for image source variants.

          - `class BetaManagedAgentsBase64ImageSource:`

            Base64-encoded image data.

            - `String data`

              Base64-encoded image data.

            - `String mediaType`

              MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

            - `Type type`

              - `BASE64("base64")`

          - `class BetaManagedAgentsUrlImageSource:`

            Image referenced by URL.

            - `Type type`

              - `URL("url")`

            - `String url`

              URL of the image to fetch.

          - `class BetaManagedAgentsFileImageSource:`

            Image referenced by file ID.

            - `String fileId`

              ID of a previously uploaded file.

            - `Type type`

              - `FILE("file")`

        - `Type type`

          - `IMAGE("image")`

      - `class BetaManagedAgentsDocumentBlock:`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

        - `Source source`

          Union type for document source variants.

          - `class BetaManagedAgentsBase64DocumentSource:`

            Base64-encoded document data.

            - `String data`

              Base64-encoded document data.

            - `String mediaType`

              MIME type of the document (e.g., "application/pdf").

            - `Type type`

              - `BASE64("base64")`

          - `class BetaManagedAgentsPlainTextDocumentSource:`

            Plain text document content.

            - `String data`

              The plain text content.

            - `MediaType mediaType`

              MIME type of the text content. Must be "text/plain".

              - `TEXT_PLAIN("text/plain")`

            - `Type type`

              - `TEXT("text")`

          - `class BetaManagedAgentsUrlDocumentSource:`

            Document referenced by URL.

            - `Type type`

              - `URL("url")`

            - `String url`

              URL of the document to fetch.

          - `class BetaManagedAgentsFileDocumentSource:`

            Document referenced by file ID.

            - `String fileId`

              ID of a previously uploaded file.

            - `Type type`

              - `FILE("file")`

        - `Type type`

          - `DOCUMENT("document")`

        - `Optional<String> context`

          Additional context about the document for the model.

        - `Optional<String> title`

          The title of the document.

    - `Optional<Boolean> isError`

      Whether the tool execution resulted in an error.

    - `Optional<LocalDateTime> processedAt`

      A timestamp in RFC 3339 format

  - `class BetaManagedAgentsAgentCustomToolUseEvent:`

    Event emitted when the agent calls a custom tool. The session goes idle until the client sends a `user.custom_tool_result` event with the result.

    - `String id`

      Unique identifier for this event.

    - `Input input`

      Input parameters for the tool call.

    - `String name`

      Name of the custom tool being called.

    - `LocalDateTime processedAt`

      A timestamp in RFC 3339 format

    - `Type type`

      - `AGENT_CUSTOM_TOOL_USE("agent.custom_tool_use")`

  - `class BetaManagedAgentsAgentMessageEvent:`

    An agent response event in the session conversation.

    - `String id`

      Unique identifier for this event.

    - `List<BetaManagedAgentsTextBlock> content`

      Array of text blocks comprising the agent response.

      - `String text`

        The text content.

      - `Type type`

        - `TEXT("text")`

    - `LocalDateTime processedAt`

      A timestamp in RFC 3339 format

    - `Type type`

      - `AGENT_MESSAGE("agent.message")`

  - `class BetaManagedAgentsAgentThinkingEvent:`

    Indicates the agent is making forward progress via extended thinking. A progress signal, not a content carrier.

    - `String id`

      Unique identifier for this event.

    - `LocalDateTime processedAt`

      A timestamp in RFC 3339 format

    - `Type type`

      - `AGENT_THINKING("agent.thinking")`

  - `class BetaManagedAgentsAgentMcpToolUseEvent:`

    Event emitted when the agent invokes a tool provided by an MCP server.

    - `String id`

      Unique identifier for this event.

    - `Input input`

      Input parameters for the tool call.

    - `String mcpServerName`

      Name of the MCP server providing the tool.

    - `String name`

      Name of the MCP tool being used.

    - `LocalDateTime processedAt`

      A timestamp in RFC 3339 format

    - `Type type`

      - `AGENT_MCP_TOOL_USE("agent.mcp_tool_use")`

    - `Optional<EvaluatedPermission> evaluatedPermission`

      AgentEvaluatedPermission enum

      - `ALLOW("allow")`

      - `ASK("ask")`

      - `DENY("deny")`

  - `class BetaManagedAgentsAgentMcpToolResultEvent:`

    Event representing the result of an MCP tool execution.

    - `String id`

      Unique identifier for this event.

    - `String mcpToolUseId`

      The id of the `agent.mcp_tool_use` event this result corresponds to.

    - `LocalDateTime processedAt`

      A timestamp in RFC 3339 format

    - `Type type`

      - `AGENT_MCP_TOOL_RESULT("agent.mcp_tool_result")`

    - `Optional<List<Content>> content`

      The result content returned by the tool.

      - `class BetaManagedAgentsTextBlock:`

        Regular text content.

        - `String text`

          The text content.

        - `Type type`

          - `TEXT("text")`

      - `class BetaManagedAgentsImageBlock:`

        Image content specified directly as base64 data or as a reference via a URL.

        - `Source source`

          Union type for image source variants.

          - `class BetaManagedAgentsBase64ImageSource:`

            Base64-encoded image data.

            - `String data`

              Base64-encoded image data.

            - `String mediaType`

              MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

            - `Type type`

              - `BASE64("base64")`

          - `class BetaManagedAgentsUrlImageSource:`

            Image referenced by URL.

            - `Type type`

              - `URL("url")`

            - `String url`

              URL of the image to fetch.

          - `class BetaManagedAgentsFileImageSource:`

            Image referenced by file ID.

            - `String fileId`

              ID of a previously uploaded file.

            - `Type type`

              - `FILE("file")`

        - `Type type`

          - `IMAGE("image")`

      - `class BetaManagedAgentsDocumentBlock:`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

        - `Source source`

          Union type for document source variants.

          - `class BetaManagedAgentsBase64DocumentSource:`

            Base64-encoded document data.

            - `String data`

              Base64-encoded document data.

            - `String mediaType`

              MIME type of the document (e.g., "application/pdf").

            - `Type type`

              - `BASE64("base64")`

          - `class BetaManagedAgentsPlainTextDocumentSource:`

            Plain text document content.

            - `String data`

              The plain text content.

            - `MediaType mediaType`

              MIME type of the text content. Must be "text/plain".

              - `TEXT_PLAIN("text/plain")`

            - `Type type`

              - `TEXT("text")`

          - `class BetaManagedAgentsUrlDocumentSource:`

            Document referenced by URL.

            - `Type type`

              - `URL("url")`

            - `String url`

              URL of the document to fetch.

          - `class BetaManagedAgentsFileDocumentSource:`

            Document referenced by file ID.

            - `String fileId`

              ID of a previously uploaded file.

            - `Type type`

              - `FILE("file")`

        - `Type type`

          - `DOCUMENT("document")`

        - `Optional<String> context`

          Additional context about the document for the model.

        - `Optional<String> title`

          The title of the document.

    - `Optional<Boolean> isError`

      Whether the tool execution resulted in an error.

  - `class BetaManagedAgentsAgentToolUseEvent:`

    Event emitted when the agent invokes a built-in agent tool.

    - `String id`

      Unique identifier for this event.

    - `Input input`

      Input parameters for the tool call.

    - `String name`

      Name of the agent tool being used.

    - `LocalDateTime processedAt`

      A timestamp in RFC 3339 format

    - `Type type`

      - `AGENT_TOOL_USE("agent.tool_use")`

    - `Optional<EvaluatedPermission> evaluatedPermission`

      AgentEvaluatedPermission enum

      - `ALLOW("allow")`

      - `ASK("ask")`

      - `DENY("deny")`

  - `class BetaManagedAgentsAgentToolResultEvent:`

    Event representing the result of an agent tool execution.

    - `String id`

      Unique identifier for this event.

    - `LocalDateTime processedAt`

      A timestamp in RFC 3339 format

    - `String toolUseId`

      The id of the `agent.tool_use` event this result corresponds to.

    - `Type type`

      - `AGENT_TOOL_RESULT("agent.tool_result")`

    - `Optional<List<Content>> content`

      The result content returned by the tool.

      - `class BetaManagedAgentsTextBlock:`

        Regular text content.

        - `String text`

          The text content.

        - `Type type`

          - `TEXT("text")`

      - `class BetaManagedAgentsImageBlock:`

        Image content specified directly as base64 data or as a reference via a URL.

        - `Source source`

          Union type for image source variants.

          - `class BetaManagedAgentsBase64ImageSource:`

            Base64-encoded image data.

            - `String data`

              Base64-encoded image data.

            - `String mediaType`

              MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

            - `Type type`

              - `BASE64("base64")`

          - `class BetaManagedAgentsUrlImageSource:`

            Image referenced by URL.

            - `Type type`

              - `URL("url")`

            - `String url`

              URL of the image to fetch.

          - `class BetaManagedAgentsFileImageSource:`

            Image referenced by file ID.

            - `String fileId`

              ID of a previously uploaded file.

            - `Type type`

              - `FILE("file")`

        - `Type type`

          - `IMAGE("image")`

      - `class BetaManagedAgentsDocumentBlock:`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

        - `Source source`

          Union type for document source variants.

          - `class BetaManagedAgentsBase64DocumentSource:`

            Base64-encoded document data.

            - `String data`

              Base64-encoded document data.

            - `String mediaType`

              MIME type of the document (e.g., "application/pdf").

            - `Type type`

              - `BASE64("base64")`

          - `class BetaManagedAgentsPlainTextDocumentSource:`

            Plain text document content.

            - `String data`

              The plain text content.

            - `MediaType mediaType`

              MIME type of the text content. Must be "text/plain".

              - `TEXT_PLAIN("text/plain")`

            - `Type type`

              - `TEXT("text")`

          - `class BetaManagedAgentsUrlDocumentSource:`

            Document referenced by URL.

            - `Type type`

              - `URL("url")`

            - `String url`

              URL of the document to fetch.

          - `class BetaManagedAgentsFileDocumentSource:`

            Document referenced by file ID.

            - `String fileId`

              ID of a previously uploaded file.

            - `Type type`

              - `FILE("file")`

        - `Type type`

          - `DOCUMENT("document")`

        - `Optional<String> context`

          Additional context about the document for the model.

        - `Optional<String> title`

          The title of the document.

    - `Optional<Boolean> isError`

      Whether the tool execution resulted in an error.

  - `class BetaManagedAgentsAgentThreadContextCompactedEvent:`

    Indicates that context compaction (summarization) occurred during the session.

    - `String id`

      Unique identifier for this event.

    - `LocalDateTime processedAt`

      A timestamp in RFC 3339 format

    - `Type type`

      - `AGENT_THREAD_CONTEXT_COMPACTED("agent.thread_context_compacted")`

  - `class BetaManagedAgentsSessionErrorEvent:`

    An error event indicating a problem occurred during session execution.

    - `String id`

      Unique identifier for this event.

    - `Error error`

      An unknown or unexpected error occurred during session execution. A fallback variant; clients that don't recognize a new error code can match on `retry_status` and `message` alone.

      - `class BetaManagedAgentsUnknownError:`

        An unknown or unexpected error occurred during session execution. A fallback variant; clients that don't recognize a new error code can match on `retry_status` and `message` alone.

        - `String message`

          Human-readable error description.

        - `RetryStatus retryStatus`

          What the client should do next in response to this error.

          - `class BetaManagedAgentsRetryStatusRetrying:`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

            - `Type type`

              - `RETRYING("retrying")`

          - `class BetaManagedAgentsRetryStatusExhausted:`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

            - `Type type`

              - `EXHAUSTED("exhausted")`

          - `class BetaManagedAgentsRetryStatusTerminal:`

            The session encountered a terminal error and will transition to `terminated` state.

            - `Type type`

              - `TERMINAL("terminal")`

        - `Type type`

          - `UNKNOWN_ERROR("unknown_error")`

      - `class BetaManagedAgentsModelOverloadedError:`

        The model is currently overloaded. Emitted after automatic retries are exhausted.

        - `String message`

          Human-readable error description.

        - `RetryStatus retryStatus`

          What the client should do next in response to this error.

          - `class BetaManagedAgentsRetryStatusRetrying:`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

            - `Type type`

              - `RETRYING("retrying")`

          - `class BetaManagedAgentsRetryStatusExhausted:`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

            - `Type type`

              - `EXHAUSTED("exhausted")`

          - `class BetaManagedAgentsRetryStatusTerminal:`

            The session encountered a terminal error and will transition to `terminated` state.

            - `Type type`

              - `TERMINAL("terminal")`

        - `Type type`

          - `MODEL_OVERLOADED_ERROR("model_overloaded_error")`

      - `class BetaManagedAgentsModelRateLimitedError:`

        The model request was rate-limited.

        - `String message`

          Human-readable error description.

        - `RetryStatus retryStatus`

          What the client should do next in response to this error.

          - `class BetaManagedAgentsRetryStatusRetrying:`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

            - `Type type`

              - `RETRYING("retrying")`

          - `class BetaManagedAgentsRetryStatusExhausted:`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

            - `Type type`

              - `EXHAUSTED("exhausted")`

          - `class BetaManagedAgentsRetryStatusTerminal:`

            The session encountered a terminal error and will transition to `terminated` state.

            - `Type type`

              - `TERMINAL("terminal")`

        - `Type type`

          - `MODEL_RATE_LIMITED_ERROR("model_rate_limited_error")`

      - `class BetaManagedAgentsModelRequestFailedError:`

        A model request failed for a reason other than overload or rate-limiting.

        - `String message`

          Human-readable error description.

        - `RetryStatus retryStatus`

          What the client should do next in response to this error.

          - `class BetaManagedAgentsRetryStatusRetrying:`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

            - `Type type`

              - `RETRYING("retrying")`

          - `class BetaManagedAgentsRetryStatusExhausted:`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

            - `Type type`

              - `EXHAUSTED("exhausted")`

          - `class BetaManagedAgentsRetryStatusTerminal:`

            The session encountered a terminal error and will transition to `terminated` state.

            - `Type type`

              - `TERMINAL("terminal")`

        - `Type type`

          - `MODEL_REQUEST_FAILED_ERROR("model_request_failed_error")`

      - `class BetaManagedAgentsMcpConnectionFailedError:`

        Failed to connect to an MCP server.

        - `String mcpServerName`

          Name of the MCP server that failed to connect.

        - `String message`

          Human-readable error description.

        - `RetryStatus retryStatus`

          What the client should do next in response to this error.

          - `class BetaManagedAgentsRetryStatusRetrying:`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

            - `Type type`

              - `RETRYING("retrying")`

          - `class BetaManagedAgentsRetryStatusExhausted:`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

            - `Type type`

              - `EXHAUSTED("exhausted")`

          - `class BetaManagedAgentsRetryStatusTerminal:`

            The session encountered a terminal error and will transition to `terminated` state.

            - `Type type`

              - `TERMINAL("terminal")`

        - `Type type`

          - `MCP_CONNECTION_FAILED_ERROR("mcp_connection_failed_error")`

      - `class BetaManagedAgentsMcpAuthenticationFailedError:`

        Authentication to an MCP server failed.

        - `String mcpServerName`

          Name of the MCP server that failed authentication.

        - `String message`

          Human-readable error description.

        - `RetryStatus retryStatus`

          What the client should do next in response to this error.

          - `class BetaManagedAgentsRetryStatusRetrying:`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

            - `Type type`

              - `RETRYING("retrying")`

          - `class BetaManagedAgentsRetryStatusExhausted:`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

            - `Type type`

              - `EXHAUSTED("exhausted")`

          - `class BetaManagedAgentsRetryStatusTerminal:`

            The session encountered a terminal error and will transition to `terminated` state.

            - `Type type`

              - `TERMINAL("terminal")`

        - `Type type`

          - `MCP_AUTHENTICATION_FAILED_ERROR("mcp_authentication_failed_error")`

      - `class BetaManagedAgentsBillingError:`

        The caller's organization or workspace cannot make model requests — out of credits or spend limit reached. Retrying with the same credentials will not succeed; the caller must resolve the billing state.

        - `String message`

          Human-readable error description.

        - `RetryStatus retryStatus`

          What the client should do next in response to this error.

          - `class BetaManagedAgentsRetryStatusRetrying:`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

            - `Type type`

              - `RETRYING("retrying")`

          - `class BetaManagedAgentsRetryStatusExhausted:`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

            - `Type type`

              - `EXHAUSTED("exhausted")`

          - `class BetaManagedAgentsRetryStatusTerminal:`

            The session encountered a terminal error and will transition to `terminated` state.

            - `Type type`

              - `TERMINAL("terminal")`

        - `Type type`

          - `BILLING_ERROR("billing_error")`

    - `LocalDateTime processedAt`

      A timestamp in RFC 3339 format

    - `Type type`

      - `SESSION_ERROR("session.error")`

  - `class BetaManagedAgentsSessionStatusRescheduledEvent:`

    Indicates the session is recovering from an error state and is rescheduled for execution.

    - `String id`

      Unique identifier for this event.

    - `LocalDateTime processedAt`

      A timestamp in RFC 3339 format

    - `Type type`

      - `SESSION_STATUS_RESCHEDULED("session.status_rescheduled")`

  - `class BetaManagedAgentsSessionStatusRunningEvent:`

    Indicates the session is actively running and the agent is working.

    - `String id`

      Unique identifier for this event.

    - `LocalDateTime processedAt`

      A timestamp in RFC 3339 format

    - `Type type`

      - `SESSION_STATUS_RUNNING("session.status_running")`

  - `class BetaManagedAgentsSessionStatusIdleEvent:`

    Indicates the agent has paused and is awaiting user input.

    - `String id`

      Unique identifier for this event.

    - `LocalDateTime processedAt`

      A timestamp in RFC 3339 format

    - `StopReason stopReason`

      The agent completed its turn naturally and is ready for the next user message.

      - `class BetaManagedAgentsSessionEndTurn:`

        The agent completed its turn naturally and is ready for the next user message.

        - `Type type`

          - `END_TURN("end_turn")`

      - `class BetaManagedAgentsSessionRequiresAction:`

        The agent is idle waiting on one or more blocking user-input events (tool confirmation, custom tool result, etc.). Resolving all of them transitions the session back to running.

        - `List<String> eventIds`

          The ids of events the agent is blocked on. Resolving fewer than all re-emits `session.status_idle` with the remainder.

        - `Type type`

          - `REQUIRES_ACTION("requires_action")`

      - `class BetaManagedAgentsSessionRetriesExhausted:`

        The turn ended because the retry budget was exhausted (`max_iterations` hit or an error escalated to `retry_status: 'exhausted'`).

        - `Type type`

          - `RETRIES_EXHAUSTED("retries_exhausted")`

    - `Type type`

      - `SESSION_STATUS_IDLE("session.status_idle")`

  - `class BetaManagedAgentsSessionStatusTerminatedEvent:`

    Indicates the session has terminated, either due to an error or completion.

    - `String id`

      Unique identifier for this event.

    - `LocalDateTime processedAt`

      A timestamp in RFC 3339 format

    - `Type type`

      - `SESSION_STATUS_TERMINATED("session.status_terminated")`

  - `class BetaManagedAgentsSpanModelRequestStartEvent:`

    Emitted when a model request is initiated by the agent.

    - `String id`

      Unique identifier for this event.

    - `LocalDateTime processedAt`

      A timestamp in RFC 3339 format

    - `Type type`

      - `SPAN_MODEL_REQUEST_START("span.model_request_start")`

  - `class BetaManagedAgentsSpanModelRequestEndEvent:`

    Emitted when a model request completes.

    - `String id`

      Unique identifier for this event.

    - `Optional<Boolean> isError`

      Whether the model request resulted in an error.

    - `String modelRequestStartId`

      The id of the corresponding `span.model_request_start` event.

    - `BetaManagedAgentsSpanModelUsage modelUsage`

      Token usage for a single model request.

      - `long cacheCreationInputTokens`

        Tokens used to create prompt cache in this request.

      - `long cacheReadInputTokens`

        Tokens read from prompt cache in this request.

      - `long inputTokens`

        Input tokens consumed by this request.

      - `long outputTokens`

        Output tokens generated by this request.

      - `Optional<Speed> speed`

        Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

        - `STANDARD("standard")`

        - `FAST("fast")`

    - `LocalDateTime processedAt`

      A timestamp in RFC 3339 format

    - `Type type`

      - `SPAN_MODEL_REQUEST_END("span.model_request_end")`

  - `class BetaManagedAgentsSessionDeletedEvent:`

    Emitted when a session has been deleted. Terminates any active event stream — no further events will be emitted for this session.

    - `String id`

      Unique identifier for this event.

    - `LocalDateTime processedAt`

      A timestamp in RFC 3339 format

    - `Type type`

      - `SESSION_DELETED("session.deleted")`

### Beta Managed Agents Session Requires Action

- `class BetaManagedAgentsSessionRequiresAction:`

  The agent is idle waiting on one or more blocking user-input events (tool confirmation, custom tool result, etc.). Resolving all of them transitions the session back to running.

  - `List<String> eventIds`

    The ids of events the agent is blocked on. Resolving fewer than all re-emits `session.status_idle` with the remainder.

  - `Type type`

    - `REQUIRES_ACTION("requires_action")`

### Beta Managed Agents Session Retries Exhausted

- `class BetaManagedAgentsSessionRetriesExhausted:`

  The turn ended because the retry budget was exhausted (`max_iterations` hit or an error escalated to `retry_status: 'exhausted'`).

  - `Type type`

    - `RETRIES_EXHAUSTED("retries_exhausted")`

### Beta Managed Agents Session Status Idle Event

- `class BetaManagedAgentsSessionStatusIdleEvent:`

  Indicates the agent has paused and is awaiting user input.

  - `String id`

    Unique identifier for this event.

  - `LocalDateTime processedAt`

    A timestamp in RFC 3339 format

  - `StopReason stopReason`

    The agent completed its turn naturally and is ready for the next user message.

    - `class BetaManagedAgentsSessionEndTurn:`

      The agent completed its turn naturally and is ready for the next user message.

      - `Type type`

        - `END_TURN("end_turn")`

    - `class BetaManagedAgentsSessionRequiresAction:`

      The agent is idle waiting on one or more blocking user-input events (tool confirmation, custom tool result, etc.). Resolving all of them transitions the session back to running.

      - `List<String> eventIds`

        The ids of events the agent is blocked on. Resolving fewer than all re-emits `session.status_idle` with the remainder.

      - `Type type`

        - `REQUIRES_ACTION("requires_action")`

    - `class BetaManagedAgentsSessionRetriesExhausted:`

      The turn ended because the retry budget was exhausted (`max_iterations` hit or an error escalated to `retry_status: 'exhausted'`).

      - `Type type`

        - `RETRIES_EXHAUSTED("retries_exhausted")`

  - `Type type`

    - `SESSION_STATUS_IDLE("session.status_idle")`

### Beta Managed Agents Session Status Rescheduled Event

- `class BetaManagedAgentsSessionStatusRescheduledEvent:`

  Indicates the session is recovering from an error state and is rescheduled for execution.

  - `String id`

    Unique identifier for this event.

  - `LocalDateTime processedAt`

    A timestamp in RFC 3339 format

  - `Type type`

    - `SESSION_STATUS_RESCHEDULED("session.status_rescheduled")`

### Beta Managed Agents Session Status Running Event

- `class BetaManagedAgentsSessionStatusRunningEvent:`

  Indicates the session is actively running and the agent is working.

  - `String id`

    Unique identifier for this event.

  - `LocalDateTime processedAt`

    A timestamp in RFC 3339 format

  - `Type type`

    - `SESSION_STATUS_RUNNING("session.status_running")`

### Beta Managed Agents Session Status Terminated Event

- `class BetaManagedAgentsSessionStatusTerminatedEvent:`

  Indicates the session has terminated, either due to an error or completion.

  - `String id`

    Unique identifier for this event.

  - `LocalDateTime processedAt`

    A timestamp in RFC 3339 format

  - `Type type`

    - `SESSION_STATUS_TERMINATED("session.status_terminated")`

### Beta Managed Agents Span Model Request End Event

- `class BetaManagedAgentsSpanModelRequestEndEvent:`

  Emitted when a model request completes.

  - `String id`

    Unique identifier for this event.

  - `Optional<Boolean> isError`

    Whether the model request resulted in an error.

  - `String modelRequestStartId`

    The id of the corresponding `span.model_request_start` event.

  - `BetaManagedAgentsSpanModelUsage modelUsage`

    Token usage for a single model request.

    - `long cacheCreationInputTokens`

      Tokens used to create prompt cache in this request.

    - `long cacheReadInputTokens`

      Tokens read from prompt cache in this request.

    - `long inputTokens`

      Input tokens consumed by this request.

    - `long outputTokens`

      Output tokens generated by this request.

    - `Optional<Speed> speed`

      Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

      - `STANDARD("standard")`

      - `FAST("fast")`

  - `LocalDateTime processedAt`

    A timestamp in RFC 3339 format

  - `Type type`

    - `SPAN_MODEL_REQUEST_END("span.model_request_end")`

### Beta Managed Agents Span Model Request Start Event

- `class BetaManagedAgentsSpanModelRequestStartEvent:`

  Emitted when a model request is initiated by the agent.

  - `String id`

    Unique identifier for this event.

  - `LocalDateTime processedAt`

    A timestamp in RFC 3339 format

  - `Type type`

    - `SPAN_MODEL_REQUEST_START("span.model_request_start")`

### Beta Managed Agents Span Model Usage

- `class BetaManagedAgentsSpanModelUsage:`

  Token usage for a single model request.

  - `long cacheCreationInputTokens`

    Tokens used to create prompt cache in this request.

  - `long cacheReadInputTokens`

    Tokens read from prompt cache in this request.

  - `long inputTokens`

    Input tokens consumed by this request.

  - `long outputTokens`

    Output tokens generated by this request.

  - `Optional<Speed> speed`

    Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

    - `STANDARD("standard")`

    - `FAST("fast")`

### Beta Managed Agents Stream Session Events

- `class BetaManagedAgentsStreamSessionEvents: A class that can be one of several variants.union`

  Server-sent event in the session stream.

  - `class BetaManagedAgentsUserMessageEvent:`

    A user message event in the session conversation.

    - `String id`

      Unique identifier for this event.

    - `List<Content> content`

      Array of content blocks comprising the user message.

      - `class BetaManagedAgentsTextBlock:`

        Regular text content.

        - `String text`

          The text content.

        - `Type type`

          - `TEXT("text")`

      - `class BetaManagedAgentsImageBlock:`

        Image content specified directly as base64 data or as a reference via a URL.

        - `Source source`

          Union type for image source variants.

          - `class BetaManagedAgentsBase64ImageSource:`

            Base64-encoded image data.

            - `String data`

              Base64-encoded image data.

            - `String mediaType`

              MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

            - `Type type`

              - `BASE64("base64")`

          - `class BetaManagedAgentsUrlImageSource:`

            Image referenced by URL.

            - `Type type`

              - `URL("url")`

            - `String url`

              URL of the image to fetch.

          - `class BetaManagedAgentsFileImageSource:`

            Image referenced by file ID.

            - `String fileId`

              ID of a previously uploaded file.

            - `Type type`

              - `FILE("file")`

        - `Type type`

          - `IMAGE("image")`

      - `class BetaManagedAgentsDocumentBlock:`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

        - `Source source`

          Union type for document source variants.

          - `class BetaManagedAgentsBase64DocumentSource:`

            Base64-encoded document data.

            - `String data`

              Base64-encoded document data.

            - `String mediaType`

              MIME type of the document (e.g., "application/pdf").

            - `Type type`

              - `BASE64("base64")`

          - `class BetaManagedAgentsPlainTextDocumentSource:`

            Plain text document content.

            - `String data`

              The plain text content.

            - `MediaType mediaType`

              MIME type of the text content. Must be "text/plain".

              - `TEXT_PLAIN("text/plain")`

            - `Type type`

              - `TEXT("text")`

          - `class BetaManagedAgentsUrlDocumentSource:`

            Document referenced by URL.

            - `Type type`

              - `URL("url")`

            - `String url`

              URL of the document to fetch.

          - `class BetaManagedAgentsFileDocumentSource:`

            Document referenced by file ID.

            - `String fileId`

              ID of a previously uploaded file.

            - `Type type`

              - `FILE("file")`

        - `Type type`

          - `DOCUMENT("document")`

        - `Optional<String> context`

          Additional context about the document for the model.

        - `Optional<String> title`

          The title of the document.

    - `Type type`

      - `USER_MESSAGE("user.message")`

    - `Optional<LocalDateTime> processedAt`

      A timestamp in RFC 3339 format

  - `class BetaManagedAgentsUserInterruptEvent:`

    An interrupt event that pauses agent execution and returns control to the user.

    - `String id`

      Unique identifier for this event.

    - `Type type`

      - `USER_INTERRUPT("user.interrupt")`

    - `Optional<LocalDateTime> processedAt`

      A timestamp in RFC 3339 format

  - `class BetaManagedAgentsUserToolConfirmationEvent:`

    A tool confirmation event that approves or denies a pending tool execution.

    - `String id`

      Unique identifier for this event.

    - `Result result`

      UserToolConfirmationResult enum

      - `ALLOW("allow")`

      - `DENY("deny")`

    - `String toolUseId`

      The id of the `agent.tool_use` or `agent.mcp_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

    - `Type type`

      - `USER_TOOL_CONFIRMATION("user.tool_confirmation")`

    - `Optional<String> denyMessage`

      Optional message providing context for a 'deny' decision. Only allowed when result is 'deny'.

    - `Optional<LocalDateTime> processedAt`

      A timestamp in RFC 3339 format

  - `class BetaManagedAgentsUserCustomToolResultEvent:`

    Event sent by the client providing the result of a custom tool execution.

    - `String id`

      Unique identifier for this event.

    - `String customToolUseId`

      The id of the `agent.custom_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

    - `Type type`

      - `USER_CUSTOM_TOOL_RESULT("user.custom_tool_result")`

    - `Optional<List<Content>> content`

      The result content returned by the tool.

      - `class BetaManagedAgentsTextBlock:`

        Regular text content.

        - `String text`

          The text content.

        - `Type type`

          - `TEXT("text")`

      - `class BetaManagedAgentsImageBlock:`

        Image content specified directly as base64 data or as a reference via a URL.

        - `Source source`

          Union type for image source variants.

          - `class BetaManagedAgentsBase64ImageSource:`

            Base64-encoded image data.

            - `String data`

              Base64-encoded image data.

            - `String mediaType`

              MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

            - `Type type`

              - `BASE64("base64")`

          - `class BetaManagedAgentsUrlImageSource:`

            Image referenced by URL.

            - `Type type`

              - `URL("url")`

            - `String url`

              URL of the image to fetch.

          - `class BetaManagedAgentsFileImageSource:`

            Image referenced by file ID.

            - `String fileId`

              ID of a previously uploaded file.

            - `Type type`

              - `FILE("file")`

        - `Type type`

          - `IMAGE("image")`

      - `class BetaManagedAgentsDocumentBlock:`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

        - `Source source`

          Union type for document source variants.

          - `class BetaManagedAgentsBase64DocumentSource:`

            Base64-encoded document data.

            - `String data`

              Base64-encoded document data.

            - `String mediaType`

              MIME type of the document (e.g., "application/pdf").

            - `Type type`

              - `BASE64("base64")`

          - `class BetaManagedAgentsPlainTextDocumentSource:`

            Plain text document content.

            - `String data`

              The plain text content.

            - `MediaType mediaType`

              MIME type of the text content. Must be "text/plain".

              - `TEXT_PLAIN("text/plain")`

            - `Type type`

              - `TEXT("text")`

          - `class BetaManagedAgentsUrlDocumentSource:`

            Document referenced by URL.

            - `Type type`

              - `URL("url")`

            - `String url`

              URL of the document to fetch.

          - `class BetaManagedAgentsFileDocumentSource:`

            Document referenced by file ID.

            - `String fileId`

              ID of a previously uploaded file.

            - `Type type`

              - `FILE("file")`

        - `Type type`

          - `DOCUMENT("document")`

        - `Optional<String> context`

          Additional context about the document for the model.

        - `Optional<String> title`

          The title of the document.

    - `Optional<Boolean> isError`

      Whether the tool execution resulted in an error.

    - `Optional<LocalDateTime> processedAt`

      A timestamp in RFC 3339 format

  - `class BetaManagedAgentsAgentCustomToolUseEvent:`

    Event emitted when the agent calls a custom tool. The session goes idle until the client sends a `user.custom_tool_result` event with the result.

    - `String id`

      Unique identifier for this event.

    - `Input input`

      Input parameters for the tool call.

    - `String name`

      Name of the custom tool being called.

    - `LocalDateTime processedAt`

      A timestamp in RFC 3339 format

    - `Type type`

      - `AGENT_CUSTOM_TOOL_USE("agent.custom_tool_use")`

  - `class BetaManagedAgentsAgentMessageEvent:`

    An agent response event in the session conversation.

    - `String id`

      Unique identifier for this event.

    - `List<BetaManagedAgentsTextBlock> content`

      Array of text blocks comprising the agent response.

      - `String text`

        The text content.

      - `Type type`

        - `TEXT("text")`

    - `LocalDateTime processedAt`

      A timestamp in RFC 3339 format

    - `Type type`

      - `AGENT_MESSAGE("agent.message")`

  - `class BetaManagedAgentsAgentThinkingEvent:`

    Indicates the agent is making forward progress via extended thinking. A progress signal, not a content carrier.

    - `String id`

      Unique identifier for this event.

    - `LocalDateTime processedAt`

      A timestamp in RFC 3339 format

    - `Type type`

      - `AGENT_THINKING("agent.thinking")`

  - `class BetaManagedAgentsAgentMcpToolUseEvent:`

    Event emitted when the agent invokes a tool provided by an MCP server.

    - `String id`

      Unique identifier for this event.

    - `Input input`

      Input parameters for the tool call.

    - `String mcpServerName`

      Name of the MCP server providing the tool.

    - `String name`

      Name of the MCP tool being used.

    - `LocalDateTime processedAt`

      A timestamp in RFC 3339 format

    - `Type type`

      - `AGENT_MCP_TOOL_USE("agent.mcp_tool_use")`

    - `Optional<EvaluatedPermission> evaluatedPermission`

      AgentEvaluatedPermission enum

      - `ALLOW("allow")`

      - `ASK("ask")`

      - `DENY("deny")`

  - `class BetaManagedAgentsAgentMcpToolResultEvent:`

    Event representing the result of an MCP tool execution.

    - `String id`

      Unique identifier for this event.

    - `String mcpToolUseId`

      The id of the `agent.mcp_tool_use` event this result corresponds to.

    - `LocalDateTime processedAt`

      A timestamp in RFC 3339 format

    - `Type type`

      - `AGENT_MCP_TOOL_RESULT("agent.mcp_tool_result")`

    - `Optional<List<Content>> content`

      The result content returned by the tool.

      - `class BetaManagedAgentsTextBlock:`

        Regular text content.

        - `String text`

          The text content.

        - `Type type`

          - `TEXT("text")`

      - `class BetaManagedAgentsImageBlock:`

        Image content specified directly as base64 data or as a reference via a URL.

        - `Source source`

          Union type for image source variants.

          - `class BetaManagedAgentsBase64ImageSource:`

            Base64-encoded image data.

            - `String data`

              Base64-encoded image data.

            - `String mediaType`

              MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

            - `Type type`

              - `BASE64("base64")`

          - `class BetaManagedAgentsUrlImageSource:`

            Image referenced by URL.

            - `Type type`

              - `URL("url")`

            - `String url`

              URL of the image to fetch.

          - `class BetaManagedAgentsFileImageSource:`

            Image referenced by file ID.

            - `String fileId`

              ID of a previously uploaded file.

            - `Type type`

              - `FILE("file")`

        - `Type type`

          - `IMAGE("image")`

      - `class BetaManagedAgentsDocumentBlock:`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

        - `Source source`

          Union type for document source variants.

          - `class BetaManagedAgentsBase64DocumentSource:`

            Base64-encoded document data.

            - `String data`

              Base64-encoded document data.

            - `String mediaType`

              MIME type of the document (e.g., "application/pdf").

            - `Type type`

              - `BASE64("base64")`

          - `class BetaManagedAgentsPlainTextDocumentSource:`

            Plain text document content.

            - `String data`

              The plain text content.

            - `MediaType mediaType`

              MIME type of the text content. Must be "text/plain".

              - `TEXT_PLAIN("text/plain")`

            - `Type type`

              - `TEXT("text")`

          - `class BetaManagedAgentsUrlDocumentSource:`

            Document referenced by URL.

            - `Type type`

              - `URL("url")`

            - `String url`

              URL of the document to fetch.

          - `class BetaManagedAgentsFileDocumentSource:`

            Document referenced by file ID.

            - `String fileId`

              ID of a previously uploaded file.

            - `Type type`

              - `FILE("file")`

        - `Type type`

          - `DOCUMENT("document")`

        - `Optional<String> context`

          Additional context about the document for the model.

        - `Optional<String> title`

          The title of the document.

    - `Optional<Boolean> isError`

      Whether the tool execution resulted in an error.

  - `class BetaManagedAgentsAgentToolUseEvent:`

    Event emitted when the agent invokes a built-in agent tool.

    - `String id`

      Unique identifier for this event.

    - `Input input`

      Input parameters for the tool call.

    - `String name`

      Name of the agent tool being used.

    - `LocalDateTime processedAt`

      A timestamp in RFC 3339 format

    - `Type type`

      - `AGENT_TOOL_USE("agent.tool_use")`

    - `Optional<EvaluatedPermission> evaluatedPermission`

      AgentEvaluatedPermission enum

      - `ALLOW("allow")`

      - `ASK("ask")`

      - `DENY("deny")`

  - `class BetaManagedAgentsAgentToolResultEvent:`

    Event representing the result of an agent tool execution.

    - `String id`

      Unique identifier for this event.

    - `LocalDateTime processedAt`

      A timestamp in RFC 3339 format

    - `String toolUseId`

      The id of the `agent.tool_use` event this result corresponds to.

    - `Type type`

      - `AGENT_TOOL_RESULT("agent.tool_result")`

    - `Optional<List<Content>> content`

      The result content returned by the tool.

      - `class BetaManagedAgentsTextBlock:`

        Regular text content.

        - `String text`

          The text content.

        - `Type type`

          - `TEXT("text")`

      - `class BetaManagedAgentsImageBlock:`

        Image content specified directly as base64 data or as a reference via a URL.

        - `Source source`

          Union type for image source variants.

          - `class BetaManagedAgentsBase64ImageSource:`

            Base64-encoded image data.

            - `String data`

              Base64-encoded image data.

            - `String mediaType`

              MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

            - `Type type`

              - `BASE64("base64")`

          - `class BetaManagedAgentsUrlImageSource:`

            Image referenced by URL.

            - `Type type`

              - `URL("url")`

            - `String url`

              URL of the image to fetch.

          - `class BetaManagedAgentsFileImageSource:`

            Image referenced by file ID.

            - `String fileId`

              ID of a previously uploaded file.

            - `Type type`

              - `FILE("file")`

        - `Type type`

          - `IMAGE("image")`

      - `class BetaManagedAgentsDocumentBlock:`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

        - `Source source`

          Union type for document source variants.

          - `class BetaManagedAgentsBase64DocumentSource:`

            Base64-encoded document data.

            - `String data`

              Base64-encoded document data.

            - `String mediaType`

              MIME type of the document (e.g., "application/pdf").

            - `Type type`

              - `BASE64("base64")`

          - `class BetaManagedAgentsPlainTextDocumentSource:`

            Plain text document content.

            - `String data`

              The plain text content.

            - `MediaType mediaType`

              MIME type of the text content. Must be "text/plain".

              - `TEXT_PLAIN("text/plain")`

            - `Type type`

              - `TEXT("text")`

          - `class BetaManagedAgentsUrlDocumentSource:`

            Document referenced by URL.

            - `Type type`

              - `URL("url")`

            - `String url`

              URL of the document to fetch.

          - `class BetaManagedAgentsFileDocumentSource:`

            Document referenced by file ID.

            - `String fileId`

              ID of a previously uploaded file.

            - `Type type`

              - `FILE("file")`

        - `Type type`

          - `DOCUMENT("document")`

        - `Optional<String> context`

          Additional context about the document for the model.

        - `Optional<String> title`

          The title of the document.

    - `Optional<Boolean> isError`

      Whether the tool execution resulted in an error.

  - `class BetaManagedAgentsAgentThreadContextCompactedEvent:`

    Indicates that context compaction (summarization) occurred during the session.

    - `String id`

      Unique identifier for this event.

    - `LocalDateTime processedAt`

      A timestamp in RFC 3339 format

    - `Type type`

      - `AGENT_THREAD_CONTEXT_COMPACTED("agent.thread_context_compacted")`

  - `class BetaManagedAgentsSessionErrorEvent:`

    An error event indicating a problem occurred during session execution.

    - `String id`

      Unique identifier for this event.

    - `Error error`

      An unknown or unexpected error occurred during session execution. A fallback variant; clients that don't recognize a new error code can match on `retry_status` and `message` alone.

      - `class BetaManagedAgentsUnknownError:`

        An unknown or unexpected error occurred during session execution. A fallback variant; clients that don't recognize a new error code can match on `retry_status` and `message` alone.

        - `String message`

          Human-readable error description.

        - `RetryStatus retryStatus`

          What the client should do next in response to this error.

          - `class BetaManagedAgentsRetryStatusRetrying:`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

            - `Type type`

              - `RETRYING("retrying")`

          - `class BetaManagedAgentsRetryStatusExhausted:`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

            - `Type type`

              - `EXHAUSTED("exhausted")`

          - `class BetaManagedAgentsRetryStatusTerminal:`

            The session encountered a terminal error and will transition to `terminated` state.

            - `Type type`

              - `TERMINAL("terminal")`

        - `Type type`

          - `UNKNOWN_ERROR("unknown_error")`

      - `class BetaManagedAgentsModelOverloadedError:`

        The model is currently overloaded. Emitted after automatic retries are exhausted.

        - `String message`

          Human-readable error description.

        - `RetryStatus retryStatus`

          What the client should do next in response to this error.

          - `class BetaManagedAgentsRetryStatusRetrying:`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

            - `Type type`

              - `RETRYING("retrying")`

          - `class BetaManagedAgentsRetryStatusExhausted:`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

            - `Type type`

              - `EXHAUSTED("exhausted")`

          - `class BetaManagedAgentsRetryStatusTerminal:`

            The session encountered a terminal error and will transition to `terminated` state.

            - `Type type`

              - `TERMINAL("terminal")`

        - `Type type`

          - `MODEL_OVERLOADED_ERROR("model_overloaded_error")`

      - `class BetaManagedAgentsModelRateLimitedError:`

        The model request was rate-limited.

        - `String message`

          Human-readable error description.

        - `RetryStatus retryStatus`

          What the client should do next in response to this error.

          - `class BetaManagedAgentsRetryStatusRetrying:`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

            - `Type type`

              - `RETRYING("retrying")`

          - `class BetaManagedAgentsRetryStatusExhausted:`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

            - `Type type`

              - `EXHAUSTED("exhausted")`

          - `class BetaManagedAgentsRetryStatusTerminal:`

            The session encountered a terminal error and will transition to `terminated` state.

            - `Type type`

              - `TERMINAL("terminal")`

        - `Type type`

          - `MODEL_RATE_LIMITED_ERROR("model_rate_limited_error")`

      - `class BetaManagedAgentsModelRequestFailedError:`

        A model request failed for a reason other than overload or rate-limiting.

        - `String message`

          Human-readable error description.

        - `RetryStatus retryStatus`

          What the client should do next in response to this error.

          - `class BetaManagedAgentsRetryStatusRetrying:`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

            - `Type type`

              - `RETRYING("retrying")`

          - `class BetaManagedAgentsRetryStatusExhausted:`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

            - `Type type`

              - `EXHAUSTED("exhausted")`

          - `class BetaManagedAgentsRetryStatusTerminal:`

            The session encountered a terminal error and will transition to `terminated` state.

            - `Type type`

              - `TERMINAL("terminal")`

        - `Type type`

          - `MODEL_REQUEST_FAILED_ERROR("model_request_failed_error")`

      - `class BetaManagedAgentsMcpConnectionFailedError:`

        Failed to connect to an MCP server.

        - `String mcpServerName`

          Name of the MCP server that failed to connect.

        - `String message`

          Human-readable error description.

        - `RetryStatus retryStatus`

          What the client should do next in response to this error.

          - `class BetaManagedAgentsRetryStatusRetrying:`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

            - `Type type`

              - `RETRYING("retrying")`

          - `class BetaManagedAgentsRetryStatusExhausted:`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

            - `Type type`

              - `EXHAUSTED("exhausted")`

          - `class BetaManagedAgentsRetryStatusTerminal:`

            The session encountered a terminal error and will transition to `terminated` state.

            - `Type type`

              - `TERMINAL("terminal")`

        - `Type type`

          - `MCP_CONNECTION_FAILED_ERROR("mcp_connection_failed_error")`

      - `class BetaManagedAgentsMcpAuthenticationFailedError:`

        Authentication to an MCP server failed.

        - `String mcpServerName`

          Name of the MCP server that failed authentication.

        - `String message`

          Human-readable error description.

        - `RetryStatus retryStatus`

          What the client should do next in response to this error.

          - `class BetaManagedAgentsRetryStatusRetrying:`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

            - `Type type`

              - `RETRYING("retrying")`

          - `class BetaManagedAgentsRetryStatusExhausted:`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

            - `Type type`

              - `EXHAUSTED("exhausted")`

          - `class BetaManagedAgentsRetryStatusTerminal:`

            The session encountered a terminal error and will transition to `terminated` state.

            - `Type type`

              - `TERMINAL("terminal")`

        - `Type type`

          - `MCP_AUTHENTICATION_FAILED_ERROR("mcp_authentication_failed_error")`

      - `class BetaManagedAgentsBillingError:`

        The caller's organization or workspace cannot make model requests — out of credits or spend limit reached. Retrying with the same credentials will not succeed; the caller must resolve the billing state.

        - `String message`

          Human-readable error description.

        - `RetryStatus retryStatus`

          What the client should do next in response to this error.

          - `class BetaManagedAgentsRetryStatusRetrying:`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

            - `Type type`

              - `RETRYING("retrying")`

          - `class BetaManagedAgentsRetryStatusExhausted:`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

            - `Type type`

              - `EXHAUSTED("exhausted")`

          - `class BetaManagedAgentsRetryStatusTerminal:`

            The session encountered a terminal error and will transition to `terminated` state.

            - `Type type`

              - `TERMINAL("terminal")`

        - `Type type`

          - `BILLING_ERROR("billing_error")`

    - `LocalDateTime processedAt`

      A timestamp in RFC 3339 format

    - `Type type`

      - `SESSION_ERROR("session.error")`

  - `class BetaManagedAgentsSessionStatusRescheduledEvent:`

    Indicates the session is recovering from an error state and is rescheduled for execution.

    - `String id`

      Unique identifier for this event.

    - `LocalDateTime processedAt`

      A timestamp in RFC 3339 format

    - `Type type`

      - `SESSION_STATUS_RESCHEDULED("session.status_rescheduled")`

  - `class BetaManagedAgentsSessionStatusRunningEvent:`

    Indicates the session is actively running and the agent is working.

    - `String id`

      Unique identifier for this event.

    - `LocalDateTime processedAt`

      A timestamp in RFC 3339 format

    - `Type type`

      - `SESSION_STATUS_RUNNING("session.status_running")`

  - `class BetaManagedAgentsSessionStatusIdleEvent:`

    Indicates the agent has paused and is awaiting user input.

    - `String id`

      Unique identifier for this event.

    - `LocalDateTime processedAt`

      A timestamp in RFC 3339 format

    - `StopReason stopReason`

      The agent completed its turn naturally and is ready for the next user message.

      - `class BetaManagedAgentsSessionEndTurn:`

        The agent completed its turn naturally and is ready for the next user message.

        - `Type type`

          - `END_TURN("end_turn")`

      - `class BetaManagedAgentsSessionRequiresAction:`

        The agent is idle waiting on one or more blocking user-input events (tool confirmation, custom tool result, etc.). Resolving all of them transitions the session back to running.

        - `List<String> eventIds`

          The ids of events the agent is blocked on. Resolving fewer than all re-emits `session.status_idle` with the remainder.

        - `Type type`

          - `REQUIRES_ACTION("requires_action")`

      - `class BetaManagedAgentsSessionRetriesExhausted:`

        The turn ended because the retry budget was exhausted (`max_iterations` hit or an error escalated to `retry_status: 'exhausted'`).

        - `Type type`

          - `RETRIES_EXHAUSTED("retries_exhausted")`

    - `Type type`

      - `SESSION_STATUS_IDLE("session.status_idle")`

  - `class BetaManagedAgentsSessionStatusTerminatedEvent:`

    Indicates the session has terminated, either due to an error or completion.

    - `String id`

      Unique identifier for this event.

    - `LocalDateTime processedAt`

      A timestamp in RFC 3339 format

    - `Type type`

      - `SESSION_STATUS_TERMINATED("session.status_terminated")`

  - `class BetaManagedAgentsSpanModelRequestStartEvent:`

    Emitted when a model request is initiated by the agent.

    - `String id`

      Unique identifier for this event.

    - `LocalDateTime processedAt`

      A timestamp in RFC 3339 format

    - `Type type`

      - `SPAN_MODEL_REQUEST_START("span.model_request_start")`

  - `class BetaManagedAgentsSpanModelRequestEndEvent:`

    Emitted when a model request completes.

    - `String id`

      Unique identifier for this event.

    - `Optional<Boolean> isError`

      Whether the model request resulted in an error.

    - `String modelRequestStartId`

      The id of the corresponding `span.model_request_start` event.

    - `BetaManagedAgentsSpanModelUsage modelUsage`

      Token usage for a single model request.

      - `long cacheCreationInputTokens`

        Tokens used to create prompt cache in this request.

      - `long cacheReadInputTokens`

        Tokens read from prompt cache in this request.

      - `long inputTokens`

        Input tokens consumed by this request.

      - `long outputTokens`

        Output tokens generated by this request.

      - `Optional<Speed> speed`

        Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

        - `STANDARD("standard")`

        - `FAST("fast")`

    - `LocalDateTime processedAt`

      A timestamp in RFC 3339 format

    - `Type type`

      - `SPAN_MODEL_REQUEST_END("span.model_request_end")`

  - `class BetaManagedAgentsSessionDeletedEvent:`

    Emitted when a session has been deleted. Terminates any active event stream — no further events will be emitted for this session.

    - `String id`

      Unique identifier for this event.

    - `LocalDateTime processedAt`

      A timestamp in RFC 3339 format

    - `Type type`

      - `SESSION_DELETED("session.deleted")`

### Beta Managed Agents Text Block

- `class BetaManagedAgentsTextBlock:`

  Regular text content.

  - `String text`

    The text content.

  - `Type type`

    - `TEXT("text")`

### Beta Managed Agents Unknown Error

- `class BetaManagedAgentsUnknownError:`

  An unknown or unexpected error occurred during session execution. A fallback variant; clients that don't recognize a new error code can match on `retry_status` and `message` alone.

  - `String message`

    Human-readable error description.

  - `RetryStatus retryStatus`

    What the client should do next in response to this error.

    - `class BetaManagedAgentsRetryStatusRetrying:`

      The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

      - `Type type`

        - `RETRYING("retrying")`

    - `class BetaManagedAgentsRetryStatusExhausted:`

      This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

      - `Type type`

        - `EXHAUSTED("exhausted")`

    - `class BetaManagedAgentsRetryStatusTerminal:`

      The session encountered a terminal error and will transition to `terminated` state.

      - `Type type`

        - `TERMINAL("terminal")`

  - `Type type`

    - `UNKNOWN_ERROR("unknown_error")`

### Beta Managed Agents URL Document Source

- `class BetaManagedAgentsUrlDocumentSource:`

  Document referenced by URL.

  - `Type type`

    - `URL("url")`

  - `String url`

    URL of the document to fetch.

### Beta Managed Agents URL Image Source

- `class BetaManagedAgentsUrlImageSource:`

  Image referenced by URL.

  - `Type type`

    - `URL("url")`

  - `String url`

    URL of the image to fetch.

### Beta Managed Agents User Custom Tool Result Event

- `class BetaManagedAgentsUserCustomToolResultEvent:`

  Event sent by the client providing the result of a custom tool execution.

  - `String id`

    Unique identifier for this event.

  - `String customToolUseId`

    The id of the `agent.custom_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

  - `Type type`

    - `USER_CUSTOM_TOOL_RESULT("user.custom_tool_result")`

  - `Optional<List<Content>> content`

    The result content returned by the tool.

    - `class BetaManagedAgentsTextBlock:`

      Regular text content.

      - `String text`

        The text content.

      - `Type type`

        - `TEXT("text")`

    - `class BetaManagedAgentsImageBlock:`

      Image content specified directly as base64 data or as a reference via a URL.

      - `Source source`

        Union type for image source variants.

        - `class BetaManagedAgentsBase64ImageSource:`

          Base64-encoded image data.

          - `String data`

            Base64-encoded image data.

          - `String mediaType`

            MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

          - `Type type`

            - `BASE64("base64")`

        - `class BetaManagedAgentsUrlImageSource:`

          Image referenced by URL.

          - `Type type`

            - `URL("url")`

          - `String url`

            URL of the image to fetch.

        - `class BetaManagedAgentsFileImageSource:`

          Image referenced by file ID.

          - `String fileId`

            ID of a previously uploaded file.

          - `Type type`

            - `FILE("file")`

      - `Type type`

        - `IMAGE("image")`

    - `class BetaManagedAgentsDocumentBlock:`

      Document content, either specified directly as base64 data, as text, or as a reference via a URL.

      - `Source source`

        Union type for document source variants.

        - `class BetaManagedAgentsBase64DocumentSource:`

          Base64-encoded document data.

          - `String data`

            Base64-encoded document data.

          - `String mediaType`

            MIME type of the document (e.g., "application/pdf").

          - `Type type`

            - `BASE64("base64")`

        - `class BetaManagedAgentsPlainTextDocumentSource:`

          Plain text document content.

          - `String data`

            The plain text content.

          - `MediaType mediaType`

            MIME type of the text content. Must be "text/plain".

            - `TEXT_PLAIN("text/plain")`

          - `Type type`

            - `TEXT("text")`

        - `class BetaManagedAgentsUrlDocumentSource:`

          Document referenced by URL.

          - `Type type`

            - `URL("url")`

          - `String url`

            URL of the document to fetch.

        - `class BetaManagedAgentsFileDocumentSource:`

          Document referenced by file ID.

          - `String fileId`

            ID of a previously uploaded file.

          - `Type type`

            - `FILE("file")`

      - `Type type`

        - `DOCUMENT("document")`

      - `Optional<String> context`

        Additional context about the document for the model.

      - `Optional<String> title`

        The title of the document.

  - `Optional<Boolean> isError`

    Whether the tool execution resulted in an error.

  - `Optional<LocalDateTime> processedAt`

    A timestamp in RFC 3339 format

### Beta Managed Agents User Custom Tool Result Event Params

- `class BetaManagedAgentsUserCustomToolResultEventParams:`

  Parameters for providing the result of a custom tool execution.

  - `String customToolUseId`

    The id of the `agent.custom_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

  - `Type type`

    - `USER_CUSTOM_TOOL_RESULT("user.custom_tool_result")`

  - `Optional<List<Content>> content`

    The result content returned by the tool.

    - `class BetaManagedAgentsTextBlock:`

      Regular text content.

      - `String text`

        The text content.

      - `Type type`

        - `TEXT("text")`

    - `class BetaManagedAgentsImageBlock:`

      Image content specified directly as base64 data or as a reference via a URL.

      - `Source source`

        Union type for image source variants.

        - `class BetaManagedAgentsBase64ImageSource:`

          Base64-encoded image data.

          - `String data`

            Base64-encoded image data.

          - `String mediaType`

            MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

          - `Type type`

            - `BASE64("base64")`

        - `class BetaManagedAgentsUrlImageSource:`

          Image referenced by URL.

          - `Type type`

            - `URL("url")`

          - `String url`

            URL of the image to fetch.

        - `class BetaManagedAgentsFileImageSource:`

          Image referenced by file ID.

          - `String fileId`

            ID of a previously uploaded file.

          - `Type type`

            - `FILE("file")`

      - `Type type`

        - `IMAGE("image")`

    - `class BetaManagedAgentsDocumentBlock:`

      Document content, either specified directly as base64 data, as text, or as a reference via a URL.

      - `Source source`

        Union type for document source variants.

        - `class BetaManagedAgentsBase64DocumentSource:`

          Base64-encoded document data.

          - `String data`

            Base64-encoded document data.

          - `String mediaType`

            MIME type of the document (e.g., "application/pdf").

          - `Type type`

            - `BASE64("base64")`

        - `class BetaManagedAgentsPlainTextDocumentSource:`

          Plain text document content.

          - `String data`

            The plain text content.

          - `MediaType mediaType`

            MIME type of the text content. Must be "text/plain".

            - `TEXT_PLAIN("text/plain")`

          - `Type type`

            - `TEXT("text")`

        - `class BetaManagedAgentsUrlDocumentSource:`

          Document referenced by URL.

          - `Type type`

            - `URL("url")`

          - `String url`

            URL of the document to fetch.

        - `class BetaManagedAgentsFileDocumentSource:`

          Document referenced by file ID.

          - `String fileId`

            ID of a previously uploaded file.

          - `Type type`

            - `FILE("file")`

      - `Type type`

        - `DOCUMENT("document")`

      - `Optional<String> context`

        Additional context about the document for the model.

      - `Optional<String> title`

        The title of the document.

  - `Optional<Boolean> isError`

    Whether the tool execution resulted in an error.

### Beta Managed Agents User Interrupt Event

- `class BetaManagedAgentsUserInterruptEvent:`

  An interrupt event that pauses agent execution and returns control to the user.

  - `String id`

    Unique identifier for this event.

  - `Type type`

    - `USER_INTERRUPT("user.interrupt")`

  - `Optional<LocalDateTime> processedAt`

    A timestamp in RFC 3339 format

### Beta Managed Agents User Interrupt Event Params

- `class BetaManagedAgentsUserInterruptEventParams:`

  Parameters for sending an interrupt to pause the agent.

  - `Type type`

    - `USER_INTERRUPT("user.interrupt")`

### Beta Managed Agents User Message Event

- `class BetaManagedAgentsUserMessageEvent:`

  A user message event in the session conversation.

  - `String id`

    Unique identifier for this event.

  - `List<Content> content`

    Array of content blocks comprising the user message.

    - `class BetaManagedAgentsTextBlock:`

      Regular text content.

      - `String text`

        The text content.

      - `Type type`

        - `TEXT("text")`

    - `class BetaManagedAgentsImageBlock:`

      Image content specified directly as base64 data or as a reference via a URL.

      - `Source source`

        Union type for image source variants.

        - `class BetaManagedAgentsBase64ImageSource:`

          Base64-encoded image data.

          - `String data`

            Base64-encoded image data.

          - `String mediaType`

            MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

          - `Type type`

            - `BASE64("base64")`

        - `class BetaManagedAgentsUrlImageSource:`

          Image referenced by URL.

          - `Type type`

            - `URL("url")`

          - `String url`

            URL of the image to fetch.

        - `class BetaManagedAgentsFileImageSource:`

          Image referenced by file ID.

          - `String fileId`

            ID of a previously uploaded file.

          - `Type type`

            - `FILE("file")`

      - `Type type`

        - `IMAGE("image")`

    - `class BetaManagedAgentsDocumentBlock:`

      Document content, either specified directly as base64 data, as text, or as a reference via a URL.

      - `Source source`

        Union type for document source variants.

        - `class BetaManagedAgentsBase64DocumentSource:`

          Base64-encoded document data.

          - `String data`

            Base64-encoded document data.

          - `String mediaType`

            MIME type of the document (e.g., "application/pdf").

          - `Type type`

            - `BASE64("base64")`

        - `class BetaManagedAgentsPlainTextDocumentSource:`

          Plain text document content.

          - `String data`

            The plain text content.

          - `MediaType mediaType`

            MIME type of the text content. Must be "text/plain".

            - `TEXT_PLAIN("text/plain")`

          - `Type type`

            - `TEXT("text")`

        - `class BetaManagedAgentsUrlDocumentSource:`

          Document referenced by URL.

          - `Type type`

            - `URL("url")`

          - `String url`

            URL of the document to fetch.

        - `class BetaManagedAgentsFileDocumentSource:`

          Document referenced by file ID.

          - `String fileId`

            ID of a previously uploaded file.

          - `Type type`

            - `FILE("file")`

      - `Type type`

        - `DOCUMENT("document")`

      - `Optional<String> context`

        Additional context about the document for the model.

      - `Optional<String> title`

        The title of the document.

  - `Type type`

    - `USER_MESSAGE("user.message")`

  - `Optional<LocalDateTime> processedAt`

    A timestamp in RFC 3339 format

### Beta Managed Agents User Message Event Params

- `class BetaManagedAgentsUserMessageEventParams:`

  Parameters for sending a user message to the session.

  - `List<Content> content`

    Array of content blocks for the user message.

    - `class BetaManagedAgentsTextBlock:`

      Regular text content.

      - `String text`

        The text content.

      - `Type type`

        - `TEXT("text")`

    - `class BetaManagedAgentsImageBlock:`

      Image content specified directly as base64 data or as a reference via a URL.

      - `Source source`

        Union type for image source variants.

        - `class BetaManagedAgentsBase64ImageSource:`

          Base64-encoded image data.

          - `String data`

            Base64-encoded image data.

          - `String mediaType`

            MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

          - `Type type`

            - `BASE64("base64")`

        - `class BetaManagedAgentsUrlImageSource:`

          Image referenced by URL.

          - `Type type`

            - `URL("url")`

          - `String url`

            URL of the image to fetch.

        - `class BetaManagedAgentsFileImageSource:`

          Image referenced by file ID.

          - `String fileId`

            ID of a previously uploaded file.

          - `Type type`

            - `FILE("file")`

      - `Type type`

        - `IMAGE("image")`

    - `class BetaManagedAgentsDocumentBlock:`

      Document content, either specified directly as base64 data, as text, or as a reference via a URL.

      - `Source source`

        Union type for document source variants.

        - `class BetaManagedAgentsBase64DocumentSource:`

          Base64-encoded document data.

          - `String data`

            Base64-encoded document data.

          - `String mediaType`

            MIME type of the document (e.g., "application/pdf").

          - `Type type`

            - `BASE64("base64")`

        - `class BetaManagedAgentsPlainTextDocumentSource:`

          Plain text document content.

          - `String data`

            The plain text content.

          - `MediaType mediaType`

            MIME type of the text content. Must be "text/plain".

            - `TEXT_PLAIN("text/plain")`

          - `Type type`

            - `TEXT("text")`

        - `class BetaManagedAgentsUrlDocumentSource:`

          Document referenced by URL.

          - `Type type`

            - `URL("url")`

          - `String url`

            URL of the document to fetch.

        - `class BetaManagedAgentsFileDocumentSource:`

          Document referenced by file ID.

          - `String fileId`

            ID of a previously uploaded file.

          - `Type type`

            - `FILE("file")`

      - `Type type`

        - `DOCUMENT("document")`

      - `Optional<String> context`

        Additional context about the document for the model.

      - `Optional<String> title`

        The title of the document.

  - `Type type`

    - `USER_MESSAGE("user.message")`

### Beta Managed Agents User Tool Confirmation Event

- `class BetaManagedAgentsUserToolConfirmationEvent:`

  A tool confirmation event that approves or denies a pending tool execution.

  - `String id`

    Unique identifier for this event.

  - `Result result`

    UserToolConfirmationResult enum

    - `ALLOW("allow")`

    - `DENY("deny")`

  - `String toolUseId`

    The id of the `agent.tool_use` or `agent.mcp_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

  - `Type type`

    - `USER_TOOL_CONFIRMATION("user.tool_confirmation")`

  - `Optional<String> denyMessage`

    Optional message providing context for a 'deny' decision. Only allowed when result is 'deny'.

  - `Optional<LocalDateTime> processedAt`

    A timestamp in RFC 3339 format

### Beta Managed Agents User Tool Confirmation Event Params

- `class BetaManagedAgentsUserToolConfirmationEventParams:`

  Parameters for confirming or denying a tool execution request.

  - `Result result`

    UserToolConfirmationResult enum

    - `ALLOW("allow")`

    - `DENY("deny")`

  - `String toolUseId`

    The id of the `agent.tool_use` or `agent.mcp_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

  - `Type type`

    - `USER_TOOL_CONFIRMATION("user.tool_confirmation")`

  - `Optional<String> denyMessage`

    Optional message providing context for a 'deny' decision. Only allowed when result is 'deny'.
