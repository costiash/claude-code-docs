## Send

`BetaManagedAgentsSendSessionEvents Beta.Sessions.Events.Send(EventSendParamsparameters, CancellationTokencancellationToken = default)`

**post** `/v1/sessions/{session_id}/events`

Send Events

### Parameters

- `EventSendParams parameters`

  - `required string sessionID`

    Path param: Path parameter session_id

  - `required IReadOnlyList<BetaManagedAgentsEventParams> events`

    Body param: Events to send to the `session`.

    - `class BetaManagedAgentsUserMessageEventParams:`

      Parameters for sending a user message to the session.

      - `required IReadOnlyList<Content> Content`

        Array of content blocks for the user message.

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

    - `class BetaManagedAgentsUserInterruptEventParams:`

      Parameters for sending an interrupt to pause the agent.

      - `required Type Type`

        - `"user.interrupt"UserInterrupt`

    - `class BetaManagedAgentsUserToolConfirmationEventParams:`

      Parameters for confirming or denying a tool execution request.

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

    - `class BetaManagedAgentsUserCustomToolResultEventParams:`

      Parameters for providing the result of a custom tool execution.

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

    - `"advisor-tool-2026-03-01"AdvisorTool2026_03_01`

    - `"user-profiles-2026-03-24"UserProfiles2026_03_24`

### Returns

- `class BetaManagedAgentsSendSessionEvents:`

  Events that were successfully sent to the session.

  - `IReadOnlyList<Data> Data`

    Sent events

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

### Example

```csharp
EventSendParams parameters = new()
{
    SessionID = "sesn_011CZkZAtmR3yMPDzynEDxu7",
    Events =
    [
        new BetaManagedAgentsUserMessageEventParams()
        {
            Content =
            [
                new BetaManagedAgentsTextBlock()
                {
                    Text = "Where is my order #1234?",
                    Type = Type.Text,
                },
            ],
            Type = Type.UserMessage,
        },
    ],
};

var betaManagedAgentsSendSessionEvents = await client.Beta.Sessions.Events.Send(parameters);

Console.WriteLine(betaManagedAgentsSendSessionEvents);
```
