## Send

`$ ant beta:sessions:events send`

**post** `/v1/sessions/{session_id}/events`

Send Events

### Parameters

- `--session-id: string`

  Path param: Path parameter session_id

- `--event: array of BetaManagedAgentsEventParams`

  Body param: Events to send to the `session`.

- `--beta: optional array of AnthropicBeta`

  Header param: Optional header to specify the beta version(s) you want to use.

### Returns

- `beta_managed_agents_send_session_events: object { data }`

  Events that were successfully sent to the session.

  - `data: optional array of BetaManagedAgentsUserMessageEvent or BetaManagedAgentsUserInterruptEvent or BetaManagedAgentsUserToolConfirmationEvent or BetaManagedAgentsUserCustomToolResultEvent`

    Sent events

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

### Example

```cli
ant beta:sessions:events send \
  --api-key my-anthropic-api-key \
  --session-id sesn_011CZkZAtmR3yMPDzynEDxu7 \
  --event "{content: [{text: 'Where is my order #1234?', type: text}], type: user.message}"
```
