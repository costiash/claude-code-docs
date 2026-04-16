## Stream

`client.Beta.Sessions.Events.Stream(ctx, sessionID, query) (*BetaManagedAgentsStreamSessionEventsUnion, error)`

**get** `/v1/sessions/{session_id}/events/stream`

Stream Events

### Parameters

- `sessionID string`

- `query BetaSessionEventStreamParams`

  - `Betas param.Field[[]AnthropicBeta]`

    Optional header to specify the beta version(s) you want to use.

    - `string`

    - `type AnthropicBeta string`

      - `const AnthropicBetaMessageBatches2024_09_24 AnthropicBeta = "message-batches-2024-09-24"`

      - `const AnthropicBetaPromptCaching2024_07_31 AnthropicBeta = "prompt-caching-2024-07-31"`

      - `const AnthropicBetaComputerUse2024_10_22 AnthropicBeta = "computer-use-2024-10-22"`

      - `const AnthropicBetaComputerUse2025_01_24 AnthropicBeta = "computer-use-2025-01-24"`

      - `const AnthropicBetaPDFs2024_09_25 AnthropicBeta = "pdfs-2024-09-25"`

      - `const AnthropicBetaTokenCounting2024_11_01 AnthropicBeta = "token-counting-2024-11-01"`

      - `const AnthropicBetaTokenEfficientTools2025_02_19 AnthropicBeta = "token-efficient-tools-2025-02-19"`

      - `const AnthropicBetaOutput128k2025_02_19 AnthropicBeta = "output-128k-2025-02-19"`

      - `const AnthropicBetaFilesAPI2025_04_14 AnthropicBeta = "files-api-2025-04-14"`

      - `const AnthropicBetaMCPClient2025_04_04 AnthropicBeta = "mcp-client-2025-04-04"`

      - `const AnthropicBetaMCPClient2025_11_20 AnthropicBeta = "mcp-client-2025-11-20"`

      - `const AnthropicBetaDevFullThinking2025_05_14 AnthropicBeta = "dev-full-thinking-2025-05-14"`

      - `const AnthropicBetaInterleavedThinking2025_05_14 AnthropicBeta = "interleaved-thinking-2025-05-14"`

      - `const AnthropicBetaCodeExecution2025_05_22 AnthropicBeta = "code-execution-2025-05-22"`

      - `const AnthropicBetaExtendedCacheTTL2025_04_11 AnthropicBeta = "extended-cache-ttl-2025-04-11"`

      - `const AnthropicBetaContext1m2025_08_07 AnthropicBeta = "context-1m-2025-08-07"`

      - `const AnthropicBetaContextManagement2025_06_27 AnthropicBeta = "context-management-2025-06-27"`

      - `const AnthropicBetaModelContextWindowExceeded2025_08_26 AnthropicBeta = "model-context-window-exceeded-2025-08-26"`

      - `const AnthropicBetaSkills2025_10_02 AnthropicBeta = "skills-2025-10-02"`

      - `const AnthropicBetaFastMode2026_02_01 AnthropicBeta = "fast-mode-2026-02-01"`

      - `const AnthropicBetaOutput300k2026_03_24 AnthropicBeta = "output-300k-2026-03-24"`

      - `const AnthropicBetaAdvisorTool2026_03_01 AnthropicBeta = "advisor-tool-2026-03-01"`

      - `const AnthropicBetaUserProfiles2026_03_24 AnthropicBeta = "user-profiles-2026-03-24"`

### Returns

- `type BetaManagedAgentsStreamSessionEventsUnion interface{…}`

  Server-sent event in the session stream.

  - `type BetaManagedAgentsUserMessageEvent struct{…}`

    A user message event in the session conversation.

    - `ID string`

      Unique identifier for this event.

    - `Content []BetaManagedAgentsUserMessageEventContentUnion`

      Array of content blocks comprising the user message.

      - `type BetaManagedAgentsTextBlock struct{…}`

        Regular text content.

        - `Text string`

          The text content.

        - `Type BetaManagedAgentsTextBlockType`

          - `const BetaManagedAgentsTextBlockTypeText BetaManagedAgentsTextBlockType = "text"`

      - `type BetaManagedAgentsImageBlock struct{…}`

        Image content specified directly as base64 data or as a reference via a URL.

        - `Source BetaManagedAgentsImageBlockSourceUnion`

          Union type for image source variants.

          - `type BetaManagedAgentsBase64ImageSource struct{…}`

            Base64-encoded image data.

            - `Data string`

              Base64-encoded image data.

            - `MediaType string`

              MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

            - `Type BetaManagedAgentsBase64ImageSourceType`

              - `const BetaManagedAgentsBase64ImageSourceTypeBase64 BetaManagedAgentsBase64ImageSourceType = "base64"`

          - `type BetaManagedAgentsURLImageSource struct{…}`

            Image referenced by URL.

            - `Type BetaManagedAgentsURLImageSourceType`

              - `const BetaManagedAgentsURLImageSourceTypeURL BetaManagedAgentsURLImageSourceType = "url"`

            - `URL string`

              URL of the image to fetch.

          - `type BetaManagedAgentsFileImageSource struct{…}`

            Image referenced by file ID.

            - `FileID string`

              ID of a previously uploaded file.

            - `Type BetaManagedAgentsFileImageSourceType`

              - `const BetaManagedAgentsFileImageSourceTypeFile BetaManagedAgentsFileImageSourceType = "file"`

        - `Type BetaManagedAgentsImageBlockType`

          - `const BetaManagedAgentsImageBlockTypeImage BetaManagedAgentsImageBlockType = "image"`

      - `type BetaManagedAgentsDocumentBlock struct{…}`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

        - `Source BetaManagedAgentsDocumentBlockSourceUnion`

          Union type for document source variants.

          - `type BetaManagedAgentsBase64DocumentSource struct{…}`

            Base64-encoded document data.

            - `Data string`

              Base64-encoded document data.

            - `MediaType string`

              MIME type of the document (e.g., "application/pdf").

            - `Type BetaManagedAgentsBase64DocumentSourceType`

              - `const BetaManagedAgentsBase64DocumentSourceTypeBase64 BetaManagedAgentsBase64DocumentSourceType = "base64"`

          - `type BetaManagedAgentsPlainTextDocumentSource struct{…}`

            Plain text document content.

            - `Data string`

              The plain text content.

            - `MediaType BetaManagedAgentsPlainTextDocumentSourceMediaType`

              MIME type of the text content. Must be "text/plain".

              - `const BetaManagedAgentsPlainTextDocumentSourceMediaTypeTextPlain BetaManagedAgentsPlainTextDocumentSourceMediaType = "text/plain"`

            - `Type BetaManagedAgentsPlainTextDocumentSourceType`

              - `const BetaManagedAgentsPlainTextDocumentSourceTypeText BetaManagedAgentsPlainTextDocumentSourceType = "text"`

          - `type BetaManagedAgentsURLDocumentSource struct{…}`

            Document referenced by URL.

            - `Type BetaManagedAgentsURLDocumentSourceType`

              - `const BetaManagedAgentsURLDocumentSourceTypeURL BetaManagedAgentsURLDocumentSourceType = "url"`

            - `URL string`

              URL of the document to fetch.

          - `type BetaManagedAgentsFileDocumentSource struct{…}`

            Document referenced by file ID.

            - `FileID string`

              ID of a previously uploaded file.

            - `Type BetaManagedAgentsFileDocumentSourceType`

              - `const BetaManagedAgentsFileDocumentSourceTypeFile BetaManagedAgentsFileDocumentSourceType = "file"`

        - `Type BetaManagedAgentsDocumentBlockType`

          - `const BetaManagedAgentsDocumentBlockTypeDocument BetaManagedAgentsDocumentBlockType = "document"`

        - `Context string`

          Additional context about the document for the model.

        - `Title string`

          The title of the document.

    - `Type BetaManagedAgentsUserMessageEventType`

      - `const BetaManagedAgentsUserMessageEventTypeUserMessage BetaManagedAgentsUserMessageEventType = "user.message"`

    - `ProcessedAt Time`

      A timestamp in RFC 3339 format

  - `type BetaManagedAgentsUserInterruptEvent struct{…}`

    An interrupt event that pauses agent execution and returns control to the user.

    - `ID string`

      Unique identifier for this event.

    - `Type BetaManagedAgentsUserInterruptEventType`

      - `const BetaManagedAgentsUserInterruptEventTypeUserInterrupt BetaManagedAgentsUserInterruptEventType = "user.interrupt"`

    - `ProcessedAt Time`

      A timestamp in RFC 3339 format

  - `type BetaManagedAgentsUserToolConfirmationEvent struct{…}`

    A tool confirmation event that approves or denies a pending tool execution.

    - `ID string`

      Unique identifier for this event.

    - `Result BetaManagedAgentsUserToolConfirmationEventResult`

      UserToolConfirmationResult enum

      - `const BetaManagedAgentsUserToolConfirmationEventResultAllow BetaManagedAgentsUserToolConfirmationEventResult = "allow"`

      - `const BetaManagedAgentsUserToolConfirmationEventResultDeny BetaManagedAgentsUserToolConfirmationEventResult = "deny"`

    - `ToolUseID string`

      The id of the `agent.tool_use` or `agent.mcp_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

    - `Type BetaManagedAgentsUserToolConfirmationEventType`

      - `const BetaManagedAgentsUserToolConfirmationEventTypeUserToolConfirmation BetaManagedAgentsUserToolConfirmationEventType = "user.tool_confirmation"`

    - `DenyMessage string`

      Optional message providing context for a 'deny' decision. Only allowed when result is 'deny'.

    - `ProcessedAt Time`

      A timestamp in RFC 3339 format

  - `type BetaManagedAgentsUserCustomToolResultEvent struct{…}`

    Event sent by the client providing the result of a custom tool execution.

    - `ID string`

      Unique identifier for this event.

    - `CustomToolUseID string`

      The id of the `agent.custom_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

    - `Type BetaManagedAgentsUserCustomToolResultEventType`

      - `const BetaManagedAgentsUserCustomToolResultEventTypeUserCustomToolResult BetaManagedAgentsUserCustomToolResultEventType = "user.custom_tool_result"`

    - `Content []BetaManagedAgentsUserCustomToolResultEventContentUnion`

      The result content returned by the tool.

      - `type BetaManagedAgentsTextBlock struct{…}`

        Regular text content.

        - `Text string`

          The text content.

        - `Type BetaManagedAgentsTextBlockType`

          - `const BetaManagedAgentsTextBlockTypeText BetaManagedAgentsTextBlockType = "text"`

      - `type BetaManagedAgentsImageBlock struct{…}`

        Image content specified directly as base64 data or as a reference via a URL.

        - `Source BetaManagedAgentsImageBlockSourceUnion`

          Union type for image source variants.

          - `type BetaManagedAgentsBase64ImageSource struct{…}`

            Base64-encoded image data.

            - `Data string`

              Base64-encoded image data.

            - `MediaType string`

              MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

            - `Type BetaManagedAgentsBase64ImageSourceType`

              - `const BetaManagedAgentsBase64ImageSourceTypeBase64 BetaManagedAgentsBase64ImageSourceType = "base64"`

          - `type BetaManagedAgentsURLImageSource struct{…}`

            Image referenced by URL.

            - `Type BetaManagedAgentsURLImageSourceType`

              - `const BetaManagedAgentsURLImageSourceTypeURL BetaManagedAgentsURLImageSourceType = "url"`

            - `URL string`

              URL of the image to fetch.

          - `type BetaManagedAgentsFileImageSource struct{…}`

            Image referenced by file ID.

            - `FileID string`

              ID of a previously uploaded file.

            - `Type BetaManagedAgentsFileImageSourceType`

              - `const BetaManagedAgentsFileImageSourceTypeFile BetaManagedAgentsFileImageSourceType = "file"`

        - `Type BetaManagedAgentsImageBlockType`

          - `const BetaManagedAgentsImageBlockTypeImage BetaManagedAgentsImageBlockType = "image"`

      - `type BetaManagedAgentsDocumentBlock struct{…}`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

        - `Source BetaManagedAgentsDocumentBlockSourceUnion`

          Union type for document source variants.

          - `type BetaManagedAgentsBase64DocumentSource struct{…}`

            Base64-encoded document data.

            - `Data string`

              Base64-encoded document data.

            - `MediaType string`

              MIME type of the document (e.g., "application/pdf").

            - `Type BetaManagedAgentsBase64DocumentSourceType`

              - `const BetaManagedAgentsBase64DocumentSourceTypeBase64 BetaManagedAgentsBase64DocumentSourceType = "base64"`

          - `type BetaManagedAgentsPlainTextDocumentSource struct{…}`

            Plain text document content.

            - `Data string`

              The plain text content.

            - `MediaType BetaManagedAgentsPlainTextDocumentSourceMediaType`

              MIME type of the text content. Must be "text/plain".

              - `const BetaManagedAgentsPlainTextDocumentSourceMediaTypeTextPlain BetaManagedAgentsPlainTextDocumentSourceMediaType = "text/plain"`

            - `Type BetaManagedAgentsPlainTextDocumentSourceType`

              - `const BetaManagedAgentsPlainTextDocumentSourceTypeText BetaManagedAgentsPlainTextDocumentSourceType = "text"`

          - `type BetaManagedAgentsURLDocumentSource struct{…}`

            Document referenced by URL.

            - `Type BetaManagedAgentsURLDocumentSourceType`

              - `const BetaManagedAgentsURLDocumentSourceTypeURL BetaManagedAgentsURLDocumentSourceType = "url"`

            - `URL string`

              URL of the document to fetch.

          - `type BetaManagedAgentsFileDocumentSource struct{…}`

            Document referenced by file ID.

            - `FileID string`

              ID of a previously uploaded file.

            - `Type BetaManagedAgentsFileDocumentSourceType`

              - `const BetaManagedAgentsFileDocumentSourceTypeFile BetaManagedAgentsFileDocumentSourceType = "file"`

        - `Type BetaManagedAgentsDocumentBlockType`

          - `const BetaManagedAgentsDocumentBlockTypeDocument BetaManagedAgentsDocumentBlockType = "document"`

        - `Context string`

          Additional context about the document for the model.

        - `Title string`

          The title of the document.

    - `IsError bool`

      Whether the tool execution resulted in an error.

    - `ProcessedAt Time`

      A timestamp in RFC 3339 format

  - `type BetaManagedAgentsAgentCustomToolUseEvent struct{…}`

    Event emitted when the agent calls a custom tool. The session goes idle until the client sends a `user.custom_tool_result` event with the result.

    - `ID string`

      Unique identifier for this event.

    - `Input map[string, any]`

      Input parameters for the tool call.

    - `Name string`

      Name of the custom tool being called.

    - `ProcessedAt Time`

      A timestamp in RFC 3339 format

    - `Type BetaManagedAgentsAgentCustomToolUseEventType`

      - `const BetaManagedAgentsAgentCustomToolUseEventTypeAgentCustomToolUse BetaManagedAgentsAgentCustomToolUseEventType = "agent.custom_tool_use"`

  - `type BetaManagedAgentsAgentMessageEvent struct{…}`

    An agent response event in the session conversation.

    - `ID string`

      Unique identifier for this event.

    - `Content []BetaManagedAgentsTextBlock`

      Array of text blocks comprising the agent response.

      - `Text string`

        The text content.

      - `Type BetaManagedAgentsTextBlockType`

        - `const BetaManagedAgentsTextBlockTypeText BetaManagedAgentsTextBlockType = "text"`

    - `ProcessedAt Time`

      A timestamp in RFC 3339 format

    - `Type BetaManagedAgentsAgentMessageEventType`

      - `const BetaManagedAgentsAgentMessageEventTypeAgentMessage BetaManagedAgentsAgentMessageEventType = "agent.message"`

  - `type BetaManagedAgentsAgentThinkingEvent struct{…}`

    Indicates the agent is making forward progress via extended thinking. A progress signal, not a content carrier.

    - `ID string`

      Unique identifier for this event.

    - `ProcessedAt Time`

      A timestamp in RFC 3339 format

    - `Type BetaManagedAgentsAgentThinkingEventType`

      - `const BetaManagedAgentsAgentThinkingEventTypeAgentThinking BetaManagedAgentsAgentThinkingEventType = "agent.thinking"`

  - `type BetaManagedAgentsAgentMCPToolUseEvent struct{…}`

    Event emitted when the agent invokes a tool provided by an MCP server.

    - `ID string`

      Unique identifier for this event.

    - `Input map[string, any]`

      Input parameters for the tool call.

    - `MCPServerName string`

      Name of the MCP server providing the tool.

    - `Name string`

      Name of the MCP tool being used.

    - `ProcessedAt Time`

      A timestamp in RFC 3339 format

    - `Type BetaManagedAgentsAgentMCPToolUseEventType`

      - `const BetaManagedAgentsAgentMCPToolUseEventTypeAgentMCPToolUse BetaManagedAgentsAgentMCPToolUseEventType = "agent.mcp_tool_use"`

    - `EvaluatedPermission BetaManagedAgentsAgentMCPToolUseEventEvaluatedPermission`

      AgentEvaluatedPermission enum

      - `const BetaManagedAgentsAgentMCPToolUseEventEvaluatedPermissionAllow BetaManagedAgentsAgentMCPToolUseEventEvaluatedPermission = "allow"`

      - `const BetaManagedAgentsAgentMCPToolUseEventEvaluatedPermissionAsk BetaManagedAgentsAgentMCPToolUseEventEvaluatedPermission = "ask"`

      - `const BetaManagedAgentsAgentMCPToolUseEventEvaluatedPermissionDeny BetaManagedAgentsAgentMCPToolUseEventEvaluatedPermission = "deny"`

  - `type BetaManagedAgentsAgentMCPToolResultEvent struct{…}`

    Event representing the result of an MCP tool execution.

    - `ID string`

      Unique identifier for this event.

    - `MCPToolUseID string`

      The id of the `agent.mcp_tool_use` event this result corresponds to.

    - `ProcessedAt Time`

      A timestamp in RFC 3339 format

    - `Type BetaManagedAgentsAgentMCPToolResultEventType`

      - `const BetaManagedAgentsAgentMCPToolResultEventTypeAgentMCPToolResult BetaManagedAgentsAgentMCPToolResultEventType = "agent.mcp_tool_result"`

    - `Content []BetaManagedAgentsAgentMCPToolResultEventContentUnion`

      The result content returned by the tool.

      - `type BetaManagedAgentsTextBlock struct{…}`

        Regular text content.

        - `Text string`

          The text content.

        - `Type BetaManagedAgentsTextBlockType`

          - `const BetaManagedAgentsTextBlockTypeText BetaManagedAgentsTextBlockType = "text"`

      - `type BetaManagedAgentsImageBlock struct{…}`

        Image content specified directly as base64 data or as a reference via a URL.

        - `Source BetaManagedAgentsImageBlockSourceUnion`

          Union type for image source variants.

          - `type BetaManagedAgentsBase64ImageSource struct{…}`

            Base64-encoded image data.

            - `Data string`

              Base64-encoded image data.

            - `MediaType string`

              MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

            - `Type BetaManagedAgentsBase64ImageSourceType`

              - `const BetaManagedAgentsBase64ImageSourceTypeBase64 BetaManagedAgentsBase64ImageSourceType = "base64"`

          - `type BetaManagedAgentsURLImageSource struct{…}`

            Image referenced by URL.

            - `Type BetaManagedAgentsURLImageSourceType`

              - `const BetaManagedAgentsURLImageSourceTypeURL BetaManagedAgentsURLImageSourceType = "url"`

            - `URL string`

              URL of the image to fetch.

          - `type BetaManagedAgentsFileImageSource struct{…}`

            Image referenced by file ID.

            - `FileID string`

              ID of a previously uploaded file.

            - `Type BetaManagedAgentsFileImageSourceType`

              - `const BetaManagedAgentsFileImageSourceTypeFile BetaManagedAgentsFileImageSourceType = "file"`

        - `Type BetaManagedAgentsImageBlockType`

          - `const BetaManagedAgentsImageBlockTypeImage BetaManagedAgentsImageBlockType = "image"`

      - `type BetaManagedAgentsDocumentBlock struct{…}`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

        - `Source BetaManagedAgentsDocumentBlockSourceUnion`

          Union type for document source variants.

          - `type BetaManagedAgentsBase64DocumentSource struct{…}`

            Base64-encoded document data.

            - `Data string`

              Base64-encoded document data.

            - `MediaType string`

              MIME type of the document (e.g., "application/pdf").

            - `Type BetaManagedAgentsBase64DocumentSourceType`

              - `const BetaManagedAgentsBase64DocumentSourceTypeBase64 BetaManagedAgentsBase64DocumentSourceType = "base64"`

          - `type BetaManagedAgentsPlainTextDocumentSource struct{…}`

            Plain text document content.

            - `Data string`

              The plain text content.

            - `MediaType BetaManagedAgentsPlainTextDocumentSourceMediaType`

              MIME type of the text content. Must be "text/plain".

              - `const BetaManagedAgentsPlainTextDocumentSourceMediaTypeTextPlain BetaManagedAgentsPlainTextDocumentSourceMediaType = "text/plain"`

            - `Type BetaManagedAgentsPlainTextDocumentSourceType`

              - `const BetaManagedAgentsPlainTextDocumentSourceTypeText BetaManagedAgentsPlainTextDocumentSourceType = "text"`

          - `type BetaManagedAgentsURLDocumentSource struct{…}`

            Document referenced by URL.

            - `Type BetaManagedAgentsURLDocumentSourceType`

              - `const BetaManagedAgentsURLDocumentSourceTypeURL BetaManagedAgentsURLDocumentSourceType = "url"`

            - `URL string`

              URL of the document to fetch.

          - `type BetaManagedAgentsFileDocumentSource struct{…}`

            Document referenced by file ID.

            - `FileID string`

              ID of a previously uploaded file.

            - `Type BetaManagedAgentsFileDocumentSourceType`

              - `const BetaManagedAgentsFileDocumentSourceTypeFile BetaManagedAgentsFileDocumentSourceType = "file"`

        - `Type BetaManagedAgentsDocumentBlockType`

          - `const BetaManagedAgentsDocumentBlockTypeDocument BetaManagedAgentsDocumentBlockType = "document"`

        - `Context string`

          Additional context about the document for the model.

        - `Title string`

          The title of the document.

    - `IsError bool`

      Whether the tool execution resulted in an error.

  - `type BetaManagedAgentsAgentToolUseEvent struct{…}`

    Event emitted when the agent invokes a built-in agent tool.

    - `ID string`

      Unique identifier for this event.

    - `Input map[string, any]`

      Input parameters for the tool call.

    - `Name string`

      Name of the agent tool being used.

    - `ProcessedAt Time`

      A timestamp in RFC 3339 format

    - `Type BetaManagedAgentsAgentToolUseEventType`

      - `const BetaManagedAgentsAgentToolUseEventTypeAgentToolUse BetaManagedAgentsAgentToolUseEventType = "agent.tool_use"`

    - `EvaluatedPermission BetaManagedAgentsAgentToolUseEventEvaluatedPermission`

      AgentEvaluatedPermission enum

      - `const BetaManagedAgentsAgentToolUseEventEvaluatedPermissionAllow BetaManagedAgentsAgentToolUseEventEvaluatedPermission = "allow"`

      - `const BetaManagedAgentsAgentToolUseEventEvaluatedPermissionAsk BetaManagedAgentsAgentToolUseEventEvaluatedPermission = "ask"`

      - `const BetaManagedAgentsAgentToolUseEventEvaluatedPermissionDeny BetaManagedAgentsAgentToolUseEventEvaluatedPermission = "deny"`

  - `type BetaManagedAgentsAgentToolResultEvent struct{…}`

    Event representing the result of an agent tool execution.

    - `ID string`

      Unique identifier for this event.

    - `ProcessedAt Time`

      A timestamp in RFC 3339 format

    - `ToolUseID string`

      The id of the `agent.tool_use` event this result corresponds to.

    - `Type BetaManagedAgentsAgentToolResultEventType`

      - `const BetaManagedAgentsAgentToolResultEventTypeAgentToolResult BetaManagedAgentsAgentToolResultEventType = "agent.tool_result"`

    - `Content []BetaManagedAgentsAgentToolResultEventContentUnion`

      The result content returned by the tool.

      - `type BetaManagedAgentsTextBlock struct{…}`

        Regular text content.

        - `Text string`

          The text content.

        - `Type BetaManagedAgentsTextBlockType`

          - `const BetaManagedAgentsTextBlockTypeText BetaManagedAgentsTextBlockType = "text"`

      - `type BetaManagedAgentsImageBlock struct{…}`

        Image content specified directly as base64 data or as a reference via a URL.

        - `Source BetaManagedAgentsImageBlockSourceUnion`

          Union type for image source variants.

          - `type BetaManagedAgentsBase64ImageSource struct{…}`

            Base64-encoded image data.

            - `Data string`

              Base64-encoded image data.

            - `MediaType string`

              MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

            - `Type BetaManagedAgentsBase64ImageSourceType`

              - `const BetaManagedAgentsBase64ImageSourceTypeBase64 BetaManagedAgentsBase64ImageSourceType = "base64"`

          - `type BetaManagedAgentsURLImageSource struct{…}`

            Image referenced by URL.

            - `Type BetaManagedAgentsURLImageSourceType`

              - `const BetaManagedAgentsURLImageSourceTypeURL BetaManagedAgentsURLImageSourceType = "url"`

            - `URL string`

              URL of the image to fetch.

          - `type BetaManagedAgentsFileImageSource struct{…}`

            Image referenced by file ID.

            - `FileID string`

              ID of a previously uploaded file.

            - `Type BetaManagedAgentsFileImageSourceType`

              - `const BetaManagedAgentsFileImageSourceTypeFile BetaManagedAgentsFileImageSourceType = "file"`

        - `Type BetaManagedAgentsImageBlockType`

          - `const BetaManagedAgentsImageBlockTypeImage BetaManagedAgentsImageBlockType = "image"`

      - `type BetaManagedAgentsDocumentBlock struct{…}`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

        - `Source BetaManagedAgentsDocumentBlockSourceUnion`

          Union type for document source variants.

          - `type BetaManagedAgentsBase64DocumentSource struct{…}`

            Base64-encoded document data.

            - `Data string`

              Base64-encoded document data.

            - `MediaType string`

              MIME type of the document (e.g., "application/pdf").

            - `Type BetaManagedAgentsBase64DocumentSourceType`

              - `const BetaManagedAgentsBase64DocumentSourceTypeBase64 BetaManagedAgentsBase64DocumentSourceType = "base64"`

          - `type BetaManagedAgentsPlainTextDocumentSource struct{…}`

            Plain text document content.

            - `Data string`

              The plain text content.

            - `MediaType BetaManagedAgentsPlainTextDocumentSourceMediaType`

              MIME type of the text content. Must be "text/plain".

              - `const BetaManagedAgentsPlainTextDocumentSourceMediaTypeTextPlain BetaManagedAgentsPlainTextDocumentSourceMediaType = "text/plain"`

            - `Type BetaManagedAgentsPlainTextDocumentSourceType`

              - `const BetaManagedAgentsPlainTextDocumentSourceTypeText BetaManagedAgentsPlainTextDocumentSourceType = "text"`

          - `type BetaManagedAgentsURLDocumentSource struct{…}`

            Document referenced by URL.

            - `Type BetaManagedAgentsURLDocumentSourceType`

              - `const BetaManagedAgentsURLDocumentSourceTypeURL BetaManagedAgentsURLDocumentSourceType = "url"`

            - `URL string`

              URL of the document to fetch.

          - `type BetaManagedAgentsFileDocumentSource struct{…}`

            Document referenced by file ID.

            - `FileID string`

              ID of a previously uploaded file.

            - `Type BetaManagedAgentsFileDocumentSourceType`

              - `const BetaManagedAgentsFileDocumentSourceTypeFile BetaManagedAgentsFileDocumentSourceType = "file"`

        - `Type BetaManagedAgentsDocumentBlockType`

          - `const BetaManagedAgentsDocumentBlockTypeDocument BetaManagedAgentsDocumentBlockType = "document"`

        - `Context string`

          Additional context about the document for the model.

        - `Title string`

          The title of the document.

    - `IsError bool`

      Whether the tool execution resulted in an error.

  - `type BetaManagedAgentsAgentThreadContextCompactedEvent struct{…}`

    Indicates that context compaction (summarization) occurred during the session.

    - `ID string`

      Unique identifier for this event.

    - `ProcessedAt Time`

      A timestamp in RFC 3339 format

    - `Type BetaManagedAgentsAgentThreadContextCompactedEventType`

      - `const BetaManagedAgentsAgentThreadContextCompactedEventTypeAgentThreadContextCompacted BetaManagedAgentsAgentThreadContextCompactedEventType = "agent.thread_context_compacted"`

  - `type BetaManagedAgentsSessionErrorEvent struct{…}`

    An error event indicating a problem occurred during session execution.

    - `ID string`

      Unique identifier for this event.

    - `Error BetaManagedAgentsSessionErrorEventErrorUnion`

      An unknown or unexpected error occurred during session execution. A fallback variant; clients that don't recognize a new error code can match on `retry_status` and `message` alone.

      - `type BetaManagedAgentsUnknownError struct{…}`

        An unknown or unexpected error occurred during session execution. A fallback variant; clients that don't recognize a new error code can match on `retry_status` and `message` alone.

        - `Message string`

          Human-readable error description.

        - `RetryStatus BetaManagedAgentsUnknownErrorRetryStatusUnion`

          What the client should do next in response to this error.

          - `type BetaManagedAgentsRetryStatusRetrying struct{…}`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

            - `Type BetaManagedAgentsRetryStatusRetryingType`

              - `const BetaManagedAgentsRetryStatusRetryingTypeRetrying BetaManagedAgentsRetryStatusRetryingType = "retrying"`

          - `type BetaManagedAgentsRetryStatusExhausted struct{…}`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

            - `Type BetaManagedAgentsRetryStatusExhaustedType`

              - `const BetaManagedAgentsRetryStatusExhaustedTypeExhausted BetaManagedAgentsRetryStatusExhaustedType = "exhausted"`

          - `type BetaManagedAgentsRetryStatusTerminal struct{…}`

            The session encountered a terminal error and will transition to `terminated` state.

            - `Type BetaManagedAgentsRetryStatusTerminalType`

              - `const BetaManagedAgentsRetryStatusTerminalTypeTerminal BetaManagedAgentsRetryStatusTerminalType = "terminal"`

        - `Type BetaManagedAgentsUnknownErrorType`

          - `const BetaManagedAgentsUnknownErrorTypeUnknownError BetaManagedAgentsUnknownErrorType = "unknown_error"`

      - `type BetaManagedAgentsModelOverloadedError struct{…}`

        The model is currently overloaded. Emitted after automatic retries are exhausted.

        - `Message string`

          Human-readable error description.

        - `RetryStatus BetaManagedAgentsModelOverloadedErrorRetryStatusUnion`

          What the client should do next in response to this error.

          - `type BetaManagedAgentsRetryStatusRetrying struct{…}`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

            - `Type BetaManagedAgentsRetryStatusRetryingType`

              - `const BetaManagedAgentsRetryStatusRetryingTypeRetrying BetaManagedAgentsRetryStatusRetryingType = "retrying"`

          - `type BetaManagedAgentsRetryStatusExhausted struct{…}`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

            - `Type BetaManagedAgentsRetryStatusExhaustedType`

              - `const BetaManagedAgentsRetryStatusExhaustedTypeExhausted BetaManagedAgentsRetryStatusExhaustedType = "exhausted"`

          - `type BetaManagedAgentsRetryStatusTerminal struct{…}`

            The session encountered a terminal error and will transition to `terminated` state.

            - `Type BetaManagedAgentsRetryStatusTerminalType`

              - `const BetaManagedAgentsRetryStatusTerminalTypeTerminal BetaManagedAgentsRetryStatusTerminalType = "terminal"`

        - `Type BetaManagedAgentsModelOverloadedErrorType`

          - `const BetaManagedAgentsModelOverloadedErrorTypeModelOverloadedError BetaManagedAgentsModelOverloadedErrorType = "model_overloaded_error"`

      - `type BetaManagedAgentsModelRateLimitedError struct{…}`

        The model request was rate-limited.

        - `Message string`

          Human-readable error description.

        - `RetryStatus BetaManagedAgentsModelRateLimitedErrorRetryStatusUnion`

          What the client should do next in response to this error.

          - `type BetaManagedAgentsRetryStatusRetrying struct{…}`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

            - `Type BetaManagedAgentsRetryStatusRetryingType`

              - `const BetaManagedAgentsRetryStatusRetryingTypeRetrying BetaManagedAgentsRetryStatusRetryingType = "retrying"`

          - `type BetaManagedAgentsRetryStatusExhausted struct{…}`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

            - `Type BetaManagedAgentsRetryStatusExhaustedType`

              - `const BetaManagedAgentsRetryStatusExhaustedTypeExhausted BetaManagedAgentsRetryStatusExhaustedType = "exhausted"`

          - `type BetaManagedAgentsRetryStatusTerminal struct{…}`

            The session encountered a terminal error and will transition to `terminated` state.

            - `Type BetaManagedAgentsRetryStatusTerminalType`

              - `const BetaManagedAgentsRetryStatusTerminalTypeTerminal BetaManagedAgentsRetryStatusTerminalType = "terminal"`

        - `Type BetaManagedAgentsModelRateLimitedErrorType`

          - `const BetaManagedAgentsModelRateLimitedErrorTypeModelRateLimitedError BetaManagedAgentsModelRateLimitedErrorType = "model_rate_limited_error"`

      - `type BetaManagedAgentsModelRequestFailedError struct{…}`

        A model request failed for a reason other than overload or rate-limiting.

        - `Message string`

          Human-readable error description.

        - `RetryStatus BetaManagedAgentsModelRequestFailedErrorRetryStatusUnion`

          What the client should do next in response to this error.

          - `type BetaManagedAgentsRetryStatusRetrying struct{…}`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

            - `Type BetaManagedAgentsRetryStatusRetryingType`

              - `const BetaManagedAgentsRetryStatusRetryingTypeRetrying BetaManagedAgentsRetryStatusRetryingType = "retrying"`

          - `type BetaManagedAgentsRetryStatusExhausted struct{…}`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

            - `Type BetaManagedAgentsRetryStatusExhaustedType`

              - `const BetaManagedAgentsRetryStatusExhaustedTypeExhausted BetaManagedAgentsRetryStatusExhaustedType = "exhausted"`

          - `type BetaManagedAgentsRetryStatusTerminal struct{…}`

            The session encountered a terminal error and will transition to `terminated` state.

            - `Type BetaManagedAgentsRetryStatusTerminalType`

              - `const BetaManagedAgentsRetryStatusTerminalTypeTerminal BetaManagedAgentsRetryStatusTerminalType = "terminal"`

        - `Type BetaManagedAgentsModelRequestFailedErrorType`

          - `const BetaManagedAgentsModelRequestFailedErrorTypeModelRequestFailedError BetaManagedAgentsModelRequestFailedErrorType = "model_request_failed_error"`

      - `type BetaManagedAgentsMCPConnectionFailedError struct{…}`

        Failed to connect to an MCP server.

        - `MCPServerName string`

          Name of the MCP server that failed to connect.

        - `Message string`

          Human-readable error description.

        - `RetryStatus BetaManagedAgentsMCPConnectionFailedErrorRetryStatusUnion`

          What the client should do next in response to this error.

          - `type BetaManagedAgentsRetryStatusRetrying struct{…}`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

            - `Type BetaManagedAgentsRetryStatusRetryingType`

              - `const BetaManagedAgentsRetryStatusRetryingTypeRetrying BetaManagedAgentsRetryStatusRetryingType = "retrying"`

          - `type BetaManagedAgentsRetryStatusExhausted struct{…}`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

            - `Type BetaManagedAgentsRetryStatusExhaustedType`

              - `const BetaManagedAgentsRetryStatusExhaustedTypeExhausted BetaManagedAgentsRetryStatusExhaustedType = "exhausted"`

          - `type BetaManagedAgentsRetryStatusTerminal struct{…}`

            The session encountered a terminal error and will transition to `terminated` state.

            - `Type BetaManagedAgentsRetryStatusTerminalType`

              - `const BetaManagedAgentsRetryStatusTerminalTypeTerminal BetaManagedAgentsRetryStatusTerminalType = "terminal"`

        - `Type BetaManagedAgentsMCPConnectionFailedErrorType`

          - `const BetaManagedAgentsMCPConnectionFailedErrorTypeMCPConnectionFailedError BetaManagedAgentsMCPConnectionFailedErrorType = "mcp_connection_failed_error"`

      - `type BetaManagedAgentsMCPAuthenticationFailedError struct{…}`

        Authentication to an MCP server failed.

        - `MCPServerName string`

          Name of the MCP server that failed authentication.

        - `Message string`

          Human-readable error description.

        - `RetryStatus BetaManagedAgentsMCPAuthenticationFailedErrorRetryStatusUnion`

          What the client should do next in response to this error.

          - `type BetaManagedAgentsRetryStatusRetrying struct{…}`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

            - `Type BetaManagedAgentsRetryStatusRetryingType`

              - `const BetaManagedAgentsRetryStatusRetryingTypeRetrying BetaManagedAgentsRetryStatusRetryingType = "retrying"`

          - `type BetaManagedAgentsRetryStatusExhausted struct{…}`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

            - `Type BetaManagedAgentsRetryStatusExhaustedType`

              - `const BetaManagedAgentsRetryStatusExhaustedTypeExhausted BetaManagedAgentsRetryStatusExhaustedType = "exhausted"`

          - `type BetaManagedAgentsRetryStatusTerminal struct{…}`

            The session encountered a terminal error and will transition to `terminated` state.

            - `Type BetaManagedAgentsRetryStatusTerminalType`

              - `const BetaManagedAgentsRetryStatusTerminalTypeTerminal BetaManagedAgentsRetryStatusTerminalType = "terminal"`

        - `Type BetaManagedAgentsMCPAuthenticationFailedErrorType`

          - `const BetaManagedAgentsMCPAuthenticationFailedErrorTypeMCPAuthenticationFailedError BetaManagedAgentsMCPAuthenticationFailedErrorType = "mcp_authentication_failed_error"`

      - `type BetaManagedAgentsBillingError struct{…}`

        The caller's organization or workspace cannot make model requests — out of credits or spend limit reached. Retrying with the same credentials will not succeed; the caller must resolve the billing state.

        - `Message string`

          Human-readable error description.

        - `RetryStatus BetaManagedAgentsBillingErrorRetryStatusUnion`

          What the client should do next in response to this error.

          - `type BetaManagedAgentsRetryStatusRetrying struct{…}`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

            - `Type BetaManagedAgentsRetryStatusRetryingType`

              - `const BetaManagedAgentsRetryStatusRetryingTypeRetrying BetaManagedAgentsRetryStatusRetryingType = "retrying"`

          - `type BetaManagedAgentsRetryStatusExhausted struct{…}`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

            - `Type BetaManagedAgentsRetryStatusExhaustedType`

              - `const BetaManagedAgentsRetryStatusExhaustedTypeExhausted BetaManagedAgentsRetryStatusExhaustedType = "exhausted"`

          - `type BetaManagedAgentsRetryStatusTerminal struct{…}`

            The session encountered a terminal error and will transition to `terminated` state.

            - `Type BetaManagedAgentsRetryStatusTerminalType`

              - `const BetaManagedAgentsRetryStatusTerminalTypeTerminal BetaManagedAgentsRetryStatusTerminalType = "terminal"`

        - `Type BetaManagedAgentsBillingErrorType`

          - `const BetaManagedAgentsBillingErrorTypeBillingError BetaManagedAgentsBillingErrorType = "billing_error"`

    - `ProcessedAt Time`

      A timestamp in RFC 3339 format

    - `Type BetaManagedAgentsSessionErrorEventType`

      - `const BetaManagedAgentsSessionErrorEventTypeSessionError BetaManagedAgentsSessionErrorEventType = "session.error"`

  - `type BetaManagedAgentsSessionStatusRescheduledEvent struct{…}`

    Indicates the session is recovering from an error state and is rescheduled for execution.

    - `ID string`

      Unique identifier for this event.

    - `ProcessedAt Time`

      A timestamp in RFC 3339 format

    - `Type BetaManagedAgentsSessionStatusRescheduledEventType`

      - `const BetaManagedAgentsSessionStatusRescheduledEventTypeSessionStatusRescheduled BetaManagedAgentsSessionStatusRescheduledEventType = "session.status_rescheduled"`

  - `type BetaManagedAgentsSessionStatusRunningEvent struct{…}`

    Indicates the session is actively running and the agent is working.

    - `ID string`

      Unique identifier for this event.

    - `ProcessedAt Time`

      A timestamp in RFC 3339 format

    - `Type BetaManagedAgentsSessionStatusRunningEventType`

      - `const BetaManagedAgentsSessionStatusRunningEventTypeSessionStatusRunning BetaManagedAgentsSessionStatusRunningEventType = "session.status_running"`

  - `type BetaManagedAgentsSessionStatusIdleEvent struct{…}`

    Indicates the agent has paused and is awaiting user input.

    - `ID string`

      Unique identifier for this event.

    - `ProcessedAt Time`

      A timestamp in RFC 3339 format

    - `StopReason BetaManagedAgentsSessionStatusIdleEventStopReasonUnion`

      The agent completed its turn naturally and is ready for the next user message.

      - `type BetaManagedAgentsSessionEndTurn struct{…}`

        The agent completed its turn naturally and is ready for the next user message.

        - `Type BetaManagedAgentsSessionEndTurnType`

          - `const BetaManagedAgentsSessionEndTurnTypeEndTurn BetaManagedAgentsSessionEndTurnType = "end_turn"`

      - `type BetaManagedAgentsSessionRequiresAction struct{…}`

        The agent is idle waiting on one or more blocking user-input events (tool confirmation, custom tool result, etc.). Resolving all of them transitions the session back to running.

        - `EventIDs []string`

          The ids of events the agent is blocked on. Resolving fewer than all re-emits `session.status_idle` with the remainder.

        - `Type BetaManagedAgentsSessionRequiresActionType`

          - `const BetaManagedAgentsSessionRequiresActionTypeRequiresAction BetaManagedAgentsSessionRequiresActionType = "requires_action"`

      - `type BetaManagedAgentsSessionRetriesExhausted struct{…}`

        The turn ended because the retry budget was exhausted (`max_iterations` hit or an error escalated to `retry_status: 'exhausted'`).

        - `Type BetaManagedAgentsSessionRetriesExhaustedType`

          - `const BetaManagedAgentsSessionRetriesExhaustedTypeRetriesExhausted BetaManagedAgentsSessionRetriesExhaustedType = "retries_exhausted"`

    - `Type BetaManagedAgentsSessionStatusIdleEventType`

      - `const BetaManagedAgentsSessionStatusIdleEventTypeSessionStatusIdle BetaManagedAgentsSessionStatusIdleEventType = "session.status_idle"`

  - `type BetaManagedAgentsSessionStatusTerminatedEvent struct{…}`

    Indicates the session has terminated, either due to an error or completion.

    - `ID string`

      Unique identifier for this event.

    - `ProcessedAt Time`

      A timestamp in RFC 3339 format

    - `Type BetaManagedAgentsSessionStatusTerminatedEventType`

      - `const BetaManagedAgentsSessionStatusTerminatedEventTypeSessionStatusTerminated BetaManagedAgentsSessionStatusTerminatedEventType = "session.status_terminated"`

  - `type BetaManagedAgentsSpanModelRequestStartEvent struct{…}`

    Emitted when a model request is initiated by the agent.

    - `ID string`

      Unique identifier for this event.

    - `ProcessedAt Time`

      A timestamp in RFC 3339 format

    - `Type BetaManagedAgentsSpanModelRequestStartEventType`

      - `const BetaManagedAgentsSpanModelRequestStartEventTypeSpanModelRequestStart BetaManagedAgentsSpanModelRequestStartEventType = "span.model_request_start"`

  - `type BetaManagedAgentsSpanModelRequestEndEvent struct{…}`

    Emitted when a model request completes.

    - `ID string`

      Unique identifier for this event.

    - `IsError bool`

      Whether the model request resulted in an error.

    - `ModelRequestStartID string`

      The id of the corresponding `span.model_request_start` event.

    - `ModelUsage BetaManagedAgentsSpanModelUsage`

      Token usage for a single model request.

      - `CacheCreationInputTokens int64`

        Tokens used to create prompt cache in this request.

      - `CacheReadInputTokens int64`

        Tokens read from prompt cache in this request.

      - `InputTokens int64`

        Input tokens consumed by this request.

      - `OutputTokens int64`

        Output tokens generated by this request.

      - `Speed BetaManagedAgentsSpanModelUsageSpeed`

        Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

        - `const BetaManagedAgentsSpanModelUsageSpeedStandard BetaManagedAgentsSpanModelUsageSpeed = "standard"`

        - `const BetaManagedAgentsSpanModelUsageSpeedFast BetaManagedAgentsSpanModelUsageSpeed = "fast"`

    - `ProcessedAt Time`

      A timestamp in RFC 3339 format

    - `Type BetaManagedAgentsSpanModelRequestEndEventType`

      - `const BetaManagedAgentsSpanModelRequestEndEventTypeSpanModelRequestEnd BetaManagedAgentsSpanModelRequestEndEventType = "span.model_request_end"`

  - `type BetaManagedAgentsSessionDeletedEvent struct{…}`

    Emitted when a session has been deleted. Terminates any active event stream — no further events will be emitted for this session.

    - `ID string`

      Unique identifier for this event.

    - `ProcessedAt Time`

      A timestamp in RFC 3339 format

    - `Type BetaManagedAgentsSessionDeletedEventType`

      - `const BetaManagedAgentsSessionDeletedEventTypeSessionDeleted BetaManagedAgentsSessionDeletedEventType = "session.deleted"`

### Example

```go
package main

import (
  "context"
  "fmt"

  "github.com/anthropics/anthropic-sdk-go"
  "github.com/anthropics/anthropic-sdk-go/option"
)

func main() {
  client := anthropic.NewClient(
    option.WithAPIKey("my-anthropic-api-key"),
  )
  stream := client.Beta.Sessions.Events.StreamEvents(
    context.TODO(),
    "sesn_011CZkZAtmR3yMPDzynEDxu7",
    anthropic.BetaSessionEventStreamParams{

    },
  )
  for stream.Next() {
  fmt.Printf("%+v\n", stream.Current())
  }
  err := stream.Err()
  if err != nil {
    panic(err.Error())
  }
}
```
