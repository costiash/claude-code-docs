## Send

`beta.sessions.events.send(strsession_id, EventSendParams**kwargs)  -> BetaManagedAgentsSendSessionEvents`

**post** `/v1/sessions/{session_id}/events`

Send Events

### Parameters

- `session_id: str`

- `events: Iterable[BetaManagedAgentsEventParams]`

  Events to send to the `session`.

  - `class BetaManagedAgentsUserMessageEventParams: …`

    Parameters for sending a user message to the session.

    - `content: List[Content]`

      Array of content blocks for the user message.

      - `class BetaManagedAgentsTextBlock: …`

        Regular text content.

        - `text: str`

          The text content.

        - `type: Literal["text"]`

          - `"text"`

      - `class BetaManagedAgentsImageBlock: …`

        Image content specified directly as base64 data or as a reference via a URL.

        - `source: Source`

          Union type for image source variants.

          - `class BetaManagedAgentsBase64ImageSource: …`

            Base64-encoded image data.

            - `data: str`

              Base64-encoded image data.

            - `media_type: str`

              MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

            - `type: Literal["base64"]`

              - `"base64"`

          - `class BetaManagedAgentsURLImageSource: …`

            Image referenced by URL.

            - `type: Literal["url"]`

              - `"url"`

            - `url: str`

              URL of the image to fetch.

          - `class BetaManagedAgentsFileImageSource: …`

            Image referenced by file ID.

            - `file_id: str`

              ID of a previously uploaded file.

            - `type: Literal["file"]`

              - `"file"`

        - `type: Literal["image"]`

          - `"image"`

      - `class BetaManagedAgentsDocumentBlock: …`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

        - `source: Source`

          Union type for document source variants.

          - `class BetaManagedAgentsBase64DocumentSource: …`

            Base64-encoded document data.

            - `data: str`

              Base64-encoded document data.

            - `media_type: str`

              MIME type of the document (e.g., "application/pdf").

            - `type: Literal["base64"]`

              - `"base64"`

          - `class BetaManagedAgentsPlainTextDocumentSource: …`

            Plain text document content.

            - `data: str`

              The plain text content.

            - `media_type: Literal["text/plain"]`

              MIME type of the text content. Must be "text/plain".

              - `"text/plain"`

            - `type: Literal["text"]`

              - `"text"`

          - `class BetaManagedAgentsURLDocumentSource: …`

            Document referenced by URL.

            - `type: Literal["url"]`

              - `"url"`

            - `url: str`

              URL of the document to fetch.

          - `class BetaManagedAgentsFileDocumentSource: …`

            Document referenced by file ID.

            - `file_id: str`

              ID of a previously uploaded file.

            - `type: Literal["file"]`

              - `"file"`

        - `type: Literal["document"]`

          - `"document"`

        - `context: Optional[str]`

          Additional context about the document for the model.

        - `title: Optional[str]`

          The title of the document.

    - `type: Literal["user.message"]`

      - `"user.message"`

  - `class BetaManagedAgentsUserInterruptEventParams: …`

    Parameters for sending an interrupt to pause the agent.

    - `type: Literal["user.interrupt"]`

      - `"user.interrupt"`

  - `class BetaManagedAgentsUserToolConfirmationEventParams: …`

    Parameters for confirming or denying a tool execution request.

    - `result: Literal["allow", "deny"]`

      UserToolConfirmationResult enum

      - `"allow"`

      - `"deny"`

    - `tool_use_id: str`

      The id of the `agent.tool_use` or `agent.mcp_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

    - `type: Literal["user.tool_confirmation"]`

      - `"user.tool_confirmation"`

    - `deny_message: Optional[str]`

      Optional message providing context for a 'deny' decision. Only allowed when result is 'deny'.

  - `class BetaManagedAgentsUserCustomToolResultEventParams: …`

    Parameters for providing the result of a custom tool execution.

    - `custom_tool_use_id: str`

      The id of the `agent.custom_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

    - `type: Literal["user.custom_tool_result"]`

      - `"user.custom_tool_result"`

    - `content: Optional[List[Content]]`

      The result content returned by the tool.

      - `class BetaManagedAgentsTextBlock: …`

        Regular text content.

        - `text: str`

          The text content.

        - `type: Literal["text"]`

          - `"text"`

      - `class BetaManagedAgentsImageBlock: …`

        Image content specified directly as base64 data or as a reference via a URL.

        - `source: Source`

          Union type for image source variants.

          - `class BetaManagedAgentsBase64ImageSource: …`

            Base64-encoded image data.

            - `data: str`

              Base64-encoded image data.

            - `media_type: str`

              MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

            - `type: Literal["base64"]`

              - `"base64"`

          - `class BetaManagedAgentsURLImageSource: …`

            Image referenced by URL.

            - `type: Literal["url"]`

              - `"url"`

            - `url: str`

              URL of the image to fetch.

          - `class BetaManagedAgentsFileImageSource: …`

            Image referenced by file ID.

            - `file_id: str`

              ID of a previously uploaded file.

            - `type: Literal["file"]`

              - `"file"`

        - `type: Literal["image"]`

          - `"image"`

      - `class BetaManagedAgentsDocumentBlock: …`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

        - `source: Source`

          Union type for document source variants.

          - `class BetaManagedAgentsBase64DocumentSource: …`

            Base64-encoded document data.

            - `data: str`

              Base64-encoded document data.

            - `media_type: str`

              MIME type of the document (e.g., "application/pdf").

            - `type: Literal["base64"]`

              - `"base64"`

          - `class BetaManagedAgentsPlainTextDocumentSource: …`

            Plain text document content.

            - `data: str`

              The plain text content.

            - `media_type: Literal["text/plain"]`

              MIME type of the text content. Must be "text/plain".

              - `"text/plain"`

            - `type: Literal["text"]`

              - `"text"`

          - `class BetaManagedAgentsURLDocumentSource: …`

            Document referenced by URL.

            - `type: Literal["url"]`

              - `"url"`

            - `url: str`

              URL of the document to fetch.

          - `class BetaManagedAgentsFileDocumentSource: …`

            Document referenced by file ID.

            - `file_id: str`

              ID of a previously uploaded file.

            - `type: Literal["file"]`

              - `"file"`

        - `type: Literal["document"]`

          - `"document"`

        - `context: Optional[str]`

          Additional context about the document for the model.

        - `title: Optional[str]`

          The title of the document.

    - `is_error: Optional[bool]`

      Whether the tool execution resulted in an error.

- `betas: Optional[List[AnthropicBetaParam]]`

  Optional header to specify the beta version(s) you want to use.

  - `str`

  - `Literal["message-batches-2024-09-24", "prompt-caching-2024-07-31", "computer-use-2024-10-22", 19 more]`

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

- `class BetaManagedAgentsSendSessionEvents: …`

  Events that were successfully sent to the session.

  - `data: Optional[List[Data]]`

    Sent events

    - `class BetaManagedAgentsUserMessageEvent: …`

      A user message event in the session conversation.

      - `id: str`

        Unique identifier for this event.

      - `content: List[Content]`

        Array of content blocks comprising the user message.

        - `class BetaManagedAgentsTextBlock: …`

          Regular text content.

          - `text: str`

            The text content.

          - `type: Literal["text"]`

            - `"text"`

        - `class BetaManagedAgentsImageBlock: …`

          Image content specified directly as base64 data or as a reference via a URL.

          - `source: Source`

            Union type for image source variants.

            - `class BetaManagedAgentsBase64ImageSource: …`

              Base64-encoded image data.

              - `data: str`

                Base64-encoded image data.

              - `media_type: str`

                MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

              - `type: Literal["base64"]`

                - `"base64"`

            - `class BetaManagedAgentsURLImageSource: …`

              Image referenced by URL.

              - `type: Literal["url"]`

                - `"url"`

              - `url: str`

                URL of the image to fetch.

            - `class BetaManagedAgentsFileImageSource: …`

              Image referenced by file ID.

              - `file_id: str`

                ID of a previously uploaded file.

              - `type: Literal["file"]`

                - `"file"`

          - `type: Literal["image"]`

            - `"image"`

        - `class BetaManagedAgentsDocumentBlock: …`

          Document content, either specified directly as base64 data, as text, or as a reference via a URL.

          - `source: Source`

            Union type for document source variants.

            - `class BetaManagedAgentsBase64DocumentSource: …`

              Base64-encoded document data.

              - `data: str`

                Base64-encoded document data.

              - `media_type: str`

                MIME type of the document (e.g., "application/pdf").

              - `type: Literal["base64"]`

                - `"base64"`

            - `class BetaManagedAgentsPlainTextDocumentSource: …`

              Plain text document content.

              - `data: str`

                The plain text content.

              - `media_type: Literal["text/plain"]`

                MIME type of the text content. Must be "text/plain".

                - `"text/plain"`

              - `type: Literal["text"]`

                - `"text"`

            - `class BetaManagedAgentsURLDocumentSource: …`

              Document referenced by URL.

              - `type: Literal["url"]`

                - `"url"`

              - `url: str`

                URL of the document to fetch.

            - `class BetaManagedAgentsFileDocumentSource: …`

              Document referenced by file ID.

              - `file_id: str`

                ID of a previously uploaded file.

              - `type: Literal["file"]`

                - `"file"`

          - `type: Literal["document"]`

            - `"document"`

          - `context: Optional[str]`

            Additional context about the document for the model.

          - `title: Optional[str]`

            The title of the document.

      - `type: Literal["user.message"]`

        - `"user.message"`

      - `processed_at: Optional[datetime]`

        A timestamp in RFC 3339 format

    - `class BetaManagedAgentsUserInterruptEvent: …`

      An interrupt event that pauses agent execution and returns control to the user.

      - `id: str`

        Unique identifier for this event.

      - `type: Literal["user.interrupt"]`

        - `"user.interrupt"`

      - `processed_at: Optional[datetime]`

        A timestamp in RFC 3339 format

    - `class BetaManagedAgentsUserToolConfirmationEvent: …`

      A tool confirmation event that approves or denies a pending tool execution.

      - `id: str`

        Unique identifier for this event.

      - `result: Literal["allow", "deny"]`

        UserToolConfirmationResult enum

        - `"allow"`

        - `"deny"`

      - `tool_use_id: str`

        The id of the `agent.tool_use` or `agent.mcp_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

      - `type: Literal["user.tool_confirmation"]`

        - `"user.tool_confirmation"`

      - `deny_message: Optional[str]`

        Optional message providing context for a 'deny' decision. Only allowed when result is 'deny'.

      - `processed_at: Optional[datetime]`

        A timestamp in RFC 3339 format

    - `class BetaManagedAgentsUserCustomToolResultEvent: …`

      Event sent by the client providing the result of a custom tool execution.

      - `id: str`

        Unique identifier for this event.

      - `custom_tool_use_id: str`

        The id of the `agent.custom_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

      - `type: Literal["user.custom_tool_result"]`

        - `"user.custom_tool_result"`

      - `content: Optional[List[Content]]`

        The result content returned by the tool.

        - `class BetaManagedAgentsTextBlock: …`

          Regular text content.

          - `text: str`

            The text content.

          - `type: Literal["text"]`

            - `"text"`

        - `class BetaManagedAgentsImageBlock: …`

          Image content specified directly as base64 data or as a reference via a URL.

          - `source: Source`

            Union type for image source variants.

            - `class BetaManagedAgentsBase64ImageSource: …`

              Base64-encoded image data.

              - `data: str`

                Base64-encoded image data.

              - `media_type: str`

                MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

              - `type: Literal["base64"]`

                - `"base64"`

            - `class BetaManagedAgentsURLImageSource: …`

              Image referenced by URL.

              - `type: Literal["url"]`

                - `"url"`

              - `url: str`

                URL of the image to fetch.

            - `class BetaManagedAgentsFileImageSource: …`

              Image referenced by file ID.

              - `file_id: str`

                ID of a previously uploaded file.

              - `type: Literal["file"]`

                - `"file"`

          - `type: Literal["image"]`

            - `"image"`

        - `class BetaManagedAgentsDocumentBlock: …`

          Document content, either specified directly as base64 data, as text, or as a reference via a URL.

          - `source: Source`

            Union type for document source variants.

            - `class BetaManagedAgentsBase64DocumentSource: …`

              Base64-encoded document data.

              - `data: str`

                Base64-encoded document data.

              - `media_type: str`

                MIME type of the document (e.g., "application/pdf").

              - `type: Literal["base64"]`

                - `"base64"`

            - `class BetaManagedAgentsPlainTextDocumentSource: …`

              Plain text document content.

              - `data: str`

                The plain text content.

              - `media_type: Literal["text/plain"]`

                MIME type of the text content. Must be "text/plain".

                - `"text/plain"`

              - `type: Literal["text"]`

                - `"text"`

            - `class BetaManagedAgentsURLDocumentSource: …`

              Document referenced by URL.

              - `type: Literal["url"]`

                - `"url"`

              - `url: str`

                URL of the document to fetch.

            - `class BetaManagedAgentsFileDocumentSource: …`

              Document referenced by file ID.

              - `file_id: str`

                ID of a previously uploaded file.

              - `type: Literal["file"]`

                - `"file"`

          - `type: Literal["document"]`

            - `"document"`

          - `context: Optional[str]`

            Additional context about the document for the model.

          - `title: Optional[str]`

            The title of the document.

      - `is_error: Optional[bool]`

        Whether the tool execution resulted in an error.

      - `processed_at: Optional[datetime]`

        A timestamp in RFC 3339 format

### Example

```python
import os
from anthropic import Anthropic

client = Anthropic(
    api_key=os.environ.get("ANTHROPIC_API_KEY"),  # This is the default and can be omitted
)
beta_managed_agents_send_session_events = client.beta.sessions.events.send(
    session_id="sesn_011CZkZAtmR3yMPDzynEDxu7",
    events=[{
        "content": [{
            "text": "Where is my order #1234?",
            "type": "text",
        }],
        "type": "user.message",
    }],
)
print(beta_managed_agents_send_session_events.data)
```
