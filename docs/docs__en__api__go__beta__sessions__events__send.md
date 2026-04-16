## Send

`client.Beta.Sessions.Events.Send(ctx, sessionID, params) (*BetaManagedAgentsSendSessionEvents, error)`

**post** `/v1/sessions/{session_id}/events`

Send Events

### Parameters

- `sessionID string`

- `params BetaSessionEventSendParams`

  - `Events param.Field[[]BetaManagedAgentsEventParamsUnionResp]`

    Body param: Events to send to the `session`.

    - `type BetaManagedAgentsUserMessageEventParamsResp struct{…}`

      Parameters for sending a user message to the session.

      - `Content []BetaManagedAgentsUserMessageEventParamsContentUnionResp`

        Array of content blocks for the user message.

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

      - `Type BetaManagedAgentsUserMessageEventParamsType`

        - `const BetaManagedAgentsUserMessageEventParamsTypeUserMessage BetaManagedAgentsUserMessageEventParamsType = "user.message"`

    - `type BetaManagedAgentsUserInterruptEventParamsResp struct{…}`

      Parameters for sending an interrupt to pause the agent.

      - `Type BetaManagedAgentsUserInterruptEventParamsType`

        - `const BetaManagedAgentsUserInterruptEventParamsTypeUserInterrupt BetaManagedAgentsUserInterruptEventParamsType = "user.interrupt"`

    - `type BetaManagedAgentsUserToolConfirmationEventParamsResp struct{…}`

      Parameters for confirming or denying a tool execution request.

      - `Result BetaManagedAgentsUserToolConfirmationEventParamsResult`

        UserToolConfirmationResult enum

        - `const BetaManagedAgentsUserToolConfirmationEventParamsResultAllow BetaManagedAgentsUserToolConfirmationEventParamsResult = "allow"`

        - `const BetaManagedAgentsUserToolConfirmationEventParamsResultDeny BetaManagedAgentsUserToolConfirmationEventParamsResult = "deny"`

      - `ToolUseID string`

        The id of the `agent.tool_use` or `agent.mcp_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

      - `Type BetaManagedAgentsUserToolConfirmationEventParamsType`

        - `const BetaManagedAgentsUserToolConfirmationEventParamsTypeUserToolConfirmation BetaManagedAgentsUserToolConfirmationEventParamsType = "user.tool_confirmation"`

      - `DenyMessage string`

        Optional message providing context for a 'deny' decision. Only allowed when result is 'deny'.

    - `type BetaManagedAgentsUserCustomToolResultEventParamsResp struct{…}`

      Parameters for providing the result of a custom tool execution.

      - `CustomToolUseID string`

        The id of the `agent.custom_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

      - `Type BetaManagedAgentsUserCustomToolResultEventParamsType`

        - `const BetaManagedAgentsUserCustomToolResultEventParamsTypeUserCustomToolResult BetaManagedAgentsUserCustomToolResultEventParamsType = "user.custom_tool_result"`

      - `Content []BetaManagedAgentsUserCustomToolResultEventParamsContentUnionResp`

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

  - `Betas param.Field[[]AnthropicBeta]`

    Header param: Optional header to specify the beta version(s) you want to use.

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

- `type BetaManagedAgentsSendSessionEvents struct{…}`

  Events that were successfully sent to the session.

  - `Data []BetaManagedAgentsSendSessionEventsDataUnion`

    Sent events

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
  betaManagedAgentsSendSessionEvents, err := client.Beta.Sessions.Events.Send(
    context.TODO(),
    "sesn_011CZkZAtmR3yMPDzynEDxu7",
    anthropic.BetaSessionEventSendParams{
      Events: []anthropic.BetaManagedAgentsEventParamsUnion{anthropic.BetaManagedAgentsEventParamsUnion{
        OfUserMessage: &anthropic.BetaManagedAgentsUserMessageEventParams{
          Content: []anthropic.BetaManagedAgentsUserMessageEventParamsContentUnion{anthropic.BetaManagedAgentsUserMessageEventParamsContentUnion{
            OfText: &anthropic.BetaManagedAgentsTextBlockParam{
              Text: "Where is my order #1234?",
              Type: anthropic.BetaManagedAgentsTextBlockTypeText,
            },
          }},
          Type: anthropic.BetaManagedAgentsUserMessageEventParamsTypeUserMessage,
        },
      }},
    },
  )
  if err != nil {
    panic(err.Error())
  }
  fmt.Printf("%+v\n", betaManagedAgentsSendSessionEvents.Data)
}
```
