## Create

`messages.create(MessageCreateParams**kwargs)  -> Message`

**post** `/v1/messages`

Send a structured list of input messages with text and/or image content, and the model will generate the next message in the conversation.

The Messages API can be used for either single queries or stateless multi-turn conversations.

Learn more about the Messages API in our [user guide](https://docs.claude.com/en/docs/initial-setup)

### Parameters

- `max_tokens: int`

  The maximum number of tokens to generate before stopping.

  Note that our models may stop _before_ reaching this maximum. This parameter only specifies the absolute maximum number of tokens to generate.

  Different models have different maximum values for this parameter.  See [models](https://docs.claude.com/en/docs/models-overview) for details.

- `messages: Iterable[MessageParam]`

  Input messages.

  Our models are trained to operate on alternating `user` and `assistant` conversational turns. When creating a new `Message`, you specify the prior conversational turns with the `messages` parameter, and the model then generates the next `Message` in the conversation. Consecutive `user` or `assistant` turns in your request will be combined into a single turn.

  Each input message must be an object with a `role` and `content`. You can specify a single `user`-role message, or you can include multiple `user` and `assistant` messages.

  If the final message uses the `assistant` role, the response content will continue immediately from the content in that message. This can be used to constrain part of the model's response.

  Example with a single `user` message:

  ```json
  [{"role": "user", "content": "Hello, Claude"}]
  ```

  Example with multiple conversational turns:

  ```json
  [
    {"role": "user", "content": "Hello there."},
    {"role": "assistant", "content": "Hi, I'm Claude. How can I help you?"},
    {"role": "user", "content": "Can you explain LLMs in plain English?"},
  ]
  ```

  Example with a partially-filled response from Claude:

  ```json
  [
    {"role": "user", "content": "What's the Greek name for Sun? (A) Sol (B) Helios (C) Sun"},
    {"role": "assistant", "content": "The best answer is ("},
  ]
  ```

  Each input message `content` may be either a single `string` or an array of content blocks, where each block has a specific `type`. Using a `string` for `content` is shorthand for an array of one content block of type `"text"`. The following input messages are equivalent:

  ```json
  {"role": "user", "content": "Hello, Claude"}
  ```

  ```json
  {"role": "user", "content": [{"type": "text", "text": "Hello, Claude"}]}
  ```

  See [input examples](https://docs.claude.com/en/api/messages-examples).

  Note that if you want to include a [system prompt](https://docs.claude.com/en/docs/system-prompts), you can use the top-level `system` parameter — there is no `"system"` role for input messages in the Messages API.

  There is a limit of 100,000 messages in a single request.

  - `content: Union[str, List[Union[TextBlockParam, ImageBlockParam, DocumentBlockParam, 14 more]]]`

    - `str`

    - `List[Union[TextBlockParam, ImageBlockParam, DocumentBlockParam, 14 more]]`

      - `class TextBlockParam: …`

        - `text: str`

        - `type: Literal["text"]`

          - `"text"`

        - `cache_control: Optional[CacheControlEphemeral]`

          Create a cache control breakpoint at this content block.

          - `type: Literal["ephemeral"]`

            - `"ephemeral"`

          - `ttl: Optional[Literal["5m", "1h"]]`

            The time-to-live for the cache control breakpoint.

            This may be one the following values:

            - `5m`: 5 minutes
            - `1h`: 1 hour

            Defaults to `5m`.

            - `"5m"`

            - `"1h"`

        - `citations: Optional[List[TextCitationParam]]`

          - `class CitationCharLocationParam: …`

            - `cited_text: str`

            - `document_index: int`

            - `document_title: Optional[str]`

            - `end_char_index: int`

            - `start_char_index: int`

            - `type: Literal["char_location"]`

              - `"char_location"`

          - `class CitationPageLocationParam: …`

            - `cited_text: str`

            - `document_index: int`

            - `document_title: Optional[str]`

            - `end_page_number: int`

            - `start_page_number: int`

            - `type: Literal["page_location"]`

              - `"page_location"`

          - `class CitationContentBlockLocationParam: …`

            - `cited_text: str`

            - `document_index: int`

            - `document_title: Optional[str]`

            - `end_block_index: int`

            - `start_block_index: int`

            - `type: Literal["content_block_location"]`

              - `"content_block_location"`

          - `class CitationWebSearchResultLocationParam: …`

            - `cited_text: str`

            - `encrypted_index: str`

            - `title: Optional[str]`

            - `type: Literal["web_search_result_location"]`

              - `"web_search_result_location"`

            - `url: str`

          - `class CitationSearchResultLocationParam: …`

            - `cited_text: str`

            - `end_block_index: int`

            - `search_result_index: int`

            - `source: str`

            - `start_block_index: int`

            - `title: Optional[str]`

            - `type: Literal["search_result_location"]`

              - `"search_result_location"`

      - `class ImageBlockParam: …`

        - `source: Source`

          - `class Base64ImageSource: …`

            - `data: str`

            - `media_type: Literal["image/jpeg", "image/png", "image/gif", "image/webp"]`

              - `"image/jpeg"`

              - `"image/png"`

              - `"image/gif"`

              - `"image/webp"`

            - `type: Literal["base64"]`

              - `"base64"`

          - `class URLImageSource: …`

            - `type: Literal["url"]`

              - `"url"`

            - `url: str`

        - `type: Literal["image"]`

          - `"image"`

        - `cache_control: Optional[CacheControlEphemeral]`

          Create a cache control breakpoint at this content block.

          - `type: Literal["ephemeral"]`

            - `"ephemeral"`

          - `ttl: Optional[Literal["5m", "1h"]]`

            The time-to-live for the cache control breakpoint.

            This may be one the following values:

            - `5m`: 5 minutes
            - `1h`: 1 hour

            Defaults to `5m`.

            - `"5m"`

            - `"1h"`

      - `class DocumentBlockParam: …`

        - `source: Source`

          - `class Base64PDFSource: …`

            - `data: str`

            - `media_type: Literal["application/pdf"]`

              - `"application/pdf"`

            - `type: Literal["base64"]`

              - `"base64"`

          - `class PlainTextSource: …`

            - `data: str`

            - `media_type: Literal["text/plain"]`

              - `"text/plain"`

            - `type: Literal["text"]`

              - `"text"`

          - `class ContentBlockSource: …`

            - `content: Union[str, List[ContentBlockSourceContent]]`

              - `str`

              - `List[ContentBlockSourceContent]`

                - `class TextBlockParam: …`

                  - `text: str`

                  - `type: Literal["text"]`

                    - `"text"`

                  - `cache_control: Optional[CacheControlEphemeral]`

                    Create a cache control breakpoint at this content block.

                    - `type: Literal["ephemeral"]`

                      - `"ephemeral"`

                    - `ttl: Optional[Literal["5m", "1h"]]`

                      The time-to-live for the cache control breakpoint.

                      This may be one the following values:

                      - `5m`: 5 minutes
                      - `1h`: 1 hour

                      Defaults to `5m`.

                      - `"5m"`

                      - `"1h"`

                  - `citations: Optional[List[TextCitationParam]]`

                    - `class CitationCharLocationParam: …`

                      - `cited_text: str`

                      - `document_index: int`

                      - `document_title: Optional[str]`

                      - `end_char_index: int`

                      - `start_char_index: int`

                      - `type: Literal["char_location"]`

                        - `"char_location"`

                    - `class CitationPageLocationParam: …`

                      - `cited_text: str`

                      - `document_index: int`

                      - `document_title: Optional[str]`

                      - `end_page_number: int`

                      - `start_page_number: int`

                      - `type: Literal["page_location"]`

                        - `"page_location"`

                    - `class CitationContentBlockLocationParam: …`

                      - `cited_text: str`

                      - `document_index: int`

                      - `document_title: Optional[str]`

                      - `end_block_index: int`

                      - `start_block_index: int`

                      - `type: Literal["content_block_location"]`

                        - `"content_block_location"`

                    - `class CitationWebSearchResultLocationParam: …`

                      - `cited_text: str`

                      - `encrypted_index: str`

                      - `title: Optional[str]`

                      - `type: Literal["web_search_result_location"]`

                        - `"web_search_result_location"`

                      - `url: str`

                    - `class CitationSearchResultLocationParam: …`

                      - `cited_text: str`

                      - `end_block_index: int`

                      - `search_result_index: int`

                      - `source: str`

                      - `start_block_index: int`

                      - `title: Optional[str]`

                      - `type: Literal["search_result_location"]`

                        - `"search_result_location"`

                - `class ImageBlockParam: …`

                  - `source: Source`

                    - `class Base64ImageSource: …`

                      - `data: str`

                      - `media_type: Literal["image/jpeg", "image/png", "image/gif", "image/webp"]`

                        - `"image/jpeg"`

                        - `"image/png"`

                        - `"image/gif"`

                        - `"image/webp"`

                      - `type: Literal["base64"]`

                        - `"base64"`

                    - `class URLImageSource: …`

                      - `type: Literal["url"]`

                        - `"url"`

                      - `url: str`

                  - `type: Literal["image"]`

                    - `"image"`

                  - `cache_control: Optional[CacheControlEphemeral]`

                    Create a cache control breakpoint at this content block.

                    - `type: Literal["ephemeral"]`

                      - `"ephemeral"`

                    - `ttl: Optional[Literal["5m", "1h"]]`

                      The time-to-live for the cache control breakpoint.

                      This may be one the following values:

                      - `5m`: 5 minutes
                      - `1h`: 1 hour

                      Defaults to `5m`.

                      - `"5m"`

                      - `"1h"`

            - `type: Literal["content"]`

              - `"content"`

          - `class URLPDFSource: …`

            - `type: Literal["url"]`

              - `"url"`

            - `url: str`

        - `type: Literal["document"]`

          - `"document"`

        - `cache_control: Optional[CacheControlEphemeral]`

          Create a cache control breakpoint at this content block.

          - `type: Literal["ephemeral"]`

            - `"ephemeral"`

          - `ttl: Optional[Literal["5m", "1h"]]`

            The time-to-live for the cache control breakpoint.

            This may be one the following values:

            - `5m`: 5 minutes
            - `1h`: 1 hour

            Defaults to `5m`.

            - `"5m"`

            - `"1h"`

        - `citations: Optional[CitationsConfigParam]`

          - `enabled: Optional[bool]`

        - `context: Optional[str]`

        - `title: Optional[str]`

      - `class SearchResultBlockParam: …`

        - `content: List[TextBlockParam]`

          - `text: str`

          - `type: Literal["text"]`

            - `"text"`

          - `cache_control: Optional[CacheControlEphemeral]`

            Create a cache control breakpoint at this content block.

            - `type: Literal["ephemeral"]`

              - `"ephemeral"`

            - `ttl: Optional[Literal["5m", "1h"]]`

              The time-to-live for the cache control breakpoint.

              This may be one the following values:

              - `5m`: 5 minutes
              - `1h`: 1 hour

              Defaults to `5m`.

              - `"5m"`

              - `"1h"`

          - `citations: Optional[List[TextCitationParam]]`

            - `class CitationCharLocationParam: …`

              - `cited_text: str`

              - `document_index: int`

              - `document_title: Optional[str]`

              - `end_char_index: int`

              - `start_char_index: int`

              - `type: Literal["char_location"]`

                - `"char_location"`

            - `class CitationPageLocationParam: …`

              - `cited_text: str`

              - `document_index: int`

              - `document_title: Optional[str]`

              - `end_page_number: int`

              - `start_page_number: int`

              - `type: Literal["page_location"]`

                - `"page_location"`

            - `class CitationContentBlockLocationParam: …`

              - `cited_text: str`

              - `document_index: int`

              - `document_title: Optional[str]`

              - `end_block_index: int`

              - `start_block_index: int`

              - `type: Literal["content_block_location"]`

                - `"content_block_location"`

            - `class CitationWebSearchResultLocationParam: …`

              - `cited_text: str`

              - `encrypted_index: str`

              - `title: Optional[str]`

              - `type: Literal["web_search_result_location"]`

                - `"web_search_result_location"`

              - `url: str`

            - `class CitationSearchResultLocationParam: …`

              - `cited_text: str`

              - `end_block_index: int`

              - `search_result_index: int`

              - `source: str`

              - `start_block_index: int`

              - `title: Optional[str]`

              - `type: Literal["search_result_location"]`

                - `"search_result_location"`

        - `source: str`

        - `title: str`

        - `type: Literal["search_result"]`

          - `"search_result"`

        - `cache_control: Optional[CacheControlEphemeral]`

          Create a cache control breakpoint at this content block.

          - `type: Literal["ephemeral"]`

            - `"ephemeral"`

          - `ttl: Optional[Literal["5m", "1h"]]`

            The time-to-live for the cache control breakpoint.

            This may be one the following values:

            - `5m`: 5 minutes
            - `1h`: 1 hour

            Defaults to `5m`.

            - `"5m"`

            - `"1h"`

        - `citations: Optional[CitationsConfigParam]`

          - `enabled: Optional[bool]`

      - `class ThinkingBlockParam: …`

        - `signature: str`

        - `thinking: str`

        - `type: Literal["thinking"]`

          - `"thinking"`

      - `class RedactedThinkingBlockParam: …`

        - `data: str`

        - `type: Literal["redacted_thinking"]`

          - `"redacted_thinking"`

      - `class ToolUseBlockParam: …`

        - `id: str`

        - `input: Dict[str, object]`

        - `name: str`

        - `type: Literal["tool_use"]`

          - `"tool_use"`

        - `cache_control: Optional[CacheControlEphemeral]`

          Create a cache control breakpoint at this content block.

          - `type: Literal["ephemeral"]`

            - `"ephemeral"`

          - `ttl: Optional[Literal["5m", "1h"]]`

            The time-to-live for the cache control breakpoint.

            This may be one the following values:

            - `5m`: 5 minutes
            - `1h`: 1 hour

            Defaults to `5m`.

            - `"5m"`

            - `"1h"`

        - `caller: Optional[Caller]`

          Tool invocation directly from the model.

          - `class DirectCaller: …`

            Tool invocation directly from the model.

            - `type: Literal["direct"]`

              - `"direct"`

          - `class ServerToolCaller: …`

            Tool invocation generated by a server-side tool.

            - `tool_id: str`

            - `type: Literal["code_execution_20250825"]`

              - `"code_execution_20250825"`

          - `class ServerToolCaller20260120: …`

            - `tool_id: str`

            - `type: Literal["code_execution_20260120"]`

              - `"code_execution_20260120"`

      - `class ToolResultBlockParam: …`

        - `tool_use_id: str`

        - `type: Literal["tool_result"]`

          - `"tool_result"`

        - `cache_control: Optional[CacheControlEphemeral]`

          Create a cache control breakpoint at this content block.

          - `type: Literal["ephemeral"]`

            - `"ephemeral"`

          - `ttl: Optional[Literal["5m", "1h"]]`

            The time-to-live for the cache control breakpoint.

            This may be one the following values:

            - `5m`: 5 minutes
            - `1h`: 1 hour

            Defaults to `5m`.

            - `"5m"`

            - `"1h"`

        - `content: Optional[Union[str, List[Content], null]]`

          - `str`

          - `List[Content]`

            - `class TextBlockParam: …`

              - `text: str`

              - `type: Literal["text"]`

                - `"text"`

              - `cache_control: Optional[CacheControlEphemeral]`

                Create a cache control breakpoint at this content block.

                - `type: Literal["ephemeral"]`

                  - `"ephemeral"`

                - `ttl: Optional[Literal["5m", "1h"]]`

                  The time-to-live for the cache control breakpoint.

                  This may be one the following values:

                  - `5m`: 5 minutes
                  - `1h`: 1 hour

                  Defaults to `5m`.

                  - `"5m"`

                  - `"1h"`

              - `citations: Optional[List[TextCitationParam]]`

                - `class CitationCharLocationParam: …`

                  - `cited_text: str`

                  - `document_index: int`

                  - `document_title: Optional[str]`

                  - `end_char_index: int`

                  - `start_char_index: int`

                  - `type: Literal["char_location"]`

                    - `"char_location"`

                - `class CitationPageLocationParam: …`

                  - `cited_text: str`

                  - `document_index: int`

                  - `document_title: Optional[str]`

                  - `end_page_number: int`

                  - `start_page_number: int`

                  - `type: Literal["page_location"]`

                    - `"page_location"`

                - `class CitationContentBlockLocationParam: …`

                  - `cited_text: str`

                  - `document_index: int`

                  - `document_title: Optional[str]`

                  - `end_block_index: int`

                  - `start_block_index: int`

                  - `type: Literal["content_block_location"]`

                    - `"content_block_location"`

                - `class CitationWebSearchResultLocationParam: …`

                  - `cited_text: str`

                  - `encrypted_index: str`

                  - `title: Optional[str]`

                  - `type: Literal["web_search_result_location"]`

                    - `"web_search_result_location"`

                  - `url: str`

                - `class CitationSearchResultLocationParam: …`

                  - `cited_text: str`

                  - `end_block_index: int`

                  - `search_result_index: int`

                  - `source: str`

                  - `start_block_index: int`

                  - `title: Optional[str]`

                  - `type: Literal["search_result_location"]`

                    - `"search_result_location"`

            - `class ImageBlockParam: …`

              - `source: Source`

                - `class Base64ImageSource: …`

                  - `data: str`

                  - `media_type: Literal["image/jpeg", "image/png", "image/gif", "image/webp"]`

                    - `"image/jpeg"`

                    - `"image/png"`

                    - `"image/gif"`

                    - `"image/webp"`

                  - `type: Literal["base64"]`

                    - `"base64"`

                - `class URLImageSource: …`

                  - `type: Literal["url"]`

                    - `"url"`

                  - `url: str`

              - `type: Literal["image"]`

                - `"image"`

              - `cache_control: Optional[CacheControlEphemeral]`

                Create a cache control breakpoint at this content block.

                - `type: Literal["ephemeral"]`

                  - `"ephemeral"`

                - `ttl: Optional[Literal["5m", "1h"]]`

                  The time-to-live for the cache control breakpoint.

                  This may be one the following values:

                  - `5m`: 5 minutes
                  - `1h`: 1 hour

                  Defaults to `5m`.

                  - `"5m"`

                  - `"1h"`

            - `class SearchResultBlockParam: …`

              - `content: List[TextBlockParam]`

                - `text: str`

                - `type: Literal["text"]`

                  - `"text"`

                - `cache_control: Optional[CacheControlEphemeral]`

                  Create a cache control breakpoint at this content block.

                  - `type: Literal["ephemeral"]`

                    - `"ephemeral"`

                  - `ttl: Optional[Literal["5m", "1h"]]`

                    The time-to-live for the cache control breakpoint.

                    This may be one the following values:

                    - `5m`: 5 minutes
                    - `1h`: 1 hour

                    Defaults to `5m`.

                    - `"5m"`

                    - `"1h"`

                - `citations: Optional[List[TextCitationParam]]`

                  - `class CitationCharLocationParam: …`

                    - `cited_text: str`

                    - `document_index: int`

                    - `document_title: Optional[str]`

                    - `end_char_index: int`

                    - `start_char_index: int`

                    - `type: Literal["char_location"]`

                      - `"char_location"`

                  - `class CitationPageLocationParam: …`

                    - `cited_text: str`

                    - `document_index: int`

                    - `document_title: Optional[str]`

                    - `end_page_number: int`

                    - `start_page_number: int`

                    - `type: Literal["page_location"]`

                      - `"page_location"`

                  - `class CitationContentBlockLocationParam: …`

                    - `cited_text: str`

                    - `document_index: int`

                    - `document_title: Optional[str]`

                    - `end_block_index: int`

                    - `start_block_index: int`

                    - `type: Literal["content_block_location"]`

                      - `"content_block_location"`

                  - `class CitationWebSearchResultLocationParam: …`

                    - `cited_text: str`

                    - `encrypted_index: str`

                    - `title: Optional[str]`

                    - `type: Literal["web_search_result_location"]`

                      - `"web_search_result_location"`

                    - `url: str`

                  - `class CitationSearchResultLocationParam: …`

                    - `cited_text: str`

                    - `end_block_index: int`

                    - `search_result_index: int`

                    - `source: str`

                    - `start_block_index: int`

                    - `title: Optional[str]`

                    - `type: Literal["search_result_location"]`

                      - `"search_result_location"`

              - `source: str`

              - `title: str`

              - `type: Literal["search_result"]`

                - `"search_result"`

              - `cache_control: Optional[CacheControlEphemeral]`

                Create a cache control breakpoint at this content block.

                - `type: Literal["ephemeral"]`

                  - `"ephemeral"`

                - `ttl: Optional[Literal["5m", "1h"]]`

                  The time-to-live for the cache control breakpoint.

                  This may be one the following values:

                  - `5m`: 5 minutes
                  - `1h`: 1 hour

                  Defaults to `5m`.

                  - `"5m"`

                  - `"1h"`

              - `citations: Optional[CitationsConfigParam]`

                - `enabled: Optional[bool]`

            - `class DocumentBlockParam: …`

              - `source: Source`

                - `class Base64PDFSource: …`

                  - `data: str`

                  - `media_type: Literal["application/pdf"]`

                    - `"application/pdf"`

                  - `type: Literal["base64"]`

                    - `"base64"`

                - `class PlainTextSource: …`

                  - `data: str`

                  - `media_type: Literal["text/plain"]`

                    - `"text/plain"`

                  - `type: Literal["text"]`

                    - `"text"`

                - `class ContentBlockSource: …`

                  - `content: Union[str, List[ContentBlockSourceContent]]`

                    - `str`

                    - `List[ContentBlockSourceContent]`

                      - `class TextBlockParam: …`

                        - `text: str`

                        - `type: Literal["text"]`

                          - `"text"`

                        - `cache_control: Optional[CacheControlEphemeral]`

                          Create a cache control breakpoint at this content block.

                          - `type: Literal["ephemeral"]`

                            - `"ephemeral"`

                          - `ttl: Optional[Literal["5m", "1h"]]`

                            The time-to-live for the cache control breakpoint.

                            This may be one the following values:

                            - `5m`: 5 minutes
                            - `1h`: 1 hour

                            Defaults to `5m`.

                            - `"5m"`

                            - `"1h"`

                        - `citations: Optional[List[TextCitationParam]]`

                          - `class CitationCharLocationParam: …`

                            - `cited_text: str`

                            - `document_index: int`

                            - `document_title: Optional[str]`

                            - `end_char_index: int`

                            - `start_char_index: int`

                            - `type: Literal["char_location"]`

                              - `"char_location"`

                          - `class CitationPageLocationParam: …`

                            - `cited_text: str`

                            - `document_index: int`

                            - `document_title: Optional[str]`

                            - `end_page_number: int`

                            - `start_page_number: int`

                            - `type: Literal["page_location"]`

                              - `"page_location"`

                          - `class CitationContentBlockLocationParam: …`

                            - `cited_text: str`

                            - `document_index: int`

                            - `document_title: Optional[str]`

                            - `end_block_index: int`

                            - `start_block_index: int`

                            - `type: Literal["content_block_location"]`

                              - `"content_block_location"`

                          - `class CitationWebSearchResultLocationParam: …`

                            - `cited_text: str`

                            - `encrypted_index: str`

                            - `title: Optional[str]`

                            - `type: Literal["web_search_result_location"]`

                              - `"web_search_result_location"`

                            - `url: str`

                          - `class CitationSearchResultLocationParam: …`

                            - `cited_text: str`

                            - `end_block_index: int`

                            - `search_result_index: int`

                            - `source: str`

                            - `start_block_index: int`

                            - `title: Optional[str]`

                            - `type: Literal["search_result_location"]`

                              - `"search_result_location"`

                      - `class ImageBlockParam: …`

                        - `source: Source`

                          - `class Base64ImageSource: …`

                            - `data: str`

                            - `media_type: Literal["image/jpeg", "image/png", "image/gif", "image/webp"]`

                              - `"image/jpeg"`

                              - `"image/png"`

                              - `"image/gif"`

                              - `"image/webp"`

                            - `type: Literal["base64"]`

                              - `"base64"`

                          - `class URLImageSource: …`

                            - `type: Literal["url"]`

                              - `"url"`

                            - `url: str`

                        - `type: Literal["image"]`

                          - `"image"`

                        - `cache_control: Optional[CacheControlEphemeral]`

                          Create a cache control breakpoint at this content block.

                          - `type: Literal["ephemeral"]`

                            - `"ephemeral"`

                          - `ttl: Optional[Literal["5m", "1h"]]`

                            The time-to-live for the cache control breakpoint.

                            This may be one the following values:

                            - `5m`: 5 minutes
                            - `1h`: 1 hour

                            Defaults to `5m`.

                            - `"5m"`

                            - `"1h"`

                  - `type: Literal["content"]`

                    - `"content"`

                - `class URLPDFSource: …`

                  - `type: Literal["url"]`

                    - `"url"`

                  - `url: str`

              - `type: Literal["document"]`

                - `"document"`

              - `cache_control: Optional[CacheControlEphemeral]`

                Create a cache control breakpoint at this content block.

                - `type: Literal["ephemeral"]`

                  - `"ephemeral"`

                - `ttl: Optional[Literal["5m", "1h"]]`

                  The time-to-live for the cache control breakpoint.

                  This may be one the following values:

                  - `5m`: 5 minutes
                  - `1h`: 1 hour

                  Defaults to `5m`.

                  - `"5m"`

                  - `"1h"`

              - `citations: Optional[CitationsConfigParam]`

                - `enabled: Optional[bool]`

              - `context: Optional[str]`

              - `title: Optional[str]`

            - `class ToolReferenceBlockParam: …`

              Tool reference block that can be included in tool_result content.

              - `tool_name: str`

              - `type: Literal["tool_reference"]`

                - `"tool_reference"`

              - `cache_control: Optional[CacheControlEphemeral]`

                Create a cache control breakpoint at this content block.

                - `type: Literal["ephemeral"]`

                  - `"ephemeral"`

                - `ttl: Optional[Literal["5m", "1h"]]`

                  The time-to-live for the cache control breakpoint.

                  This may be one the following values:

                  - `5m`: 5 minutes
                  - `1h`: 1 hour

                  Defaults to `5m`.

                  - `"5m"`

                  - `"1h"`

        - `is_error: Optional[bool]`

      - `class ServerToolUseBlockParam: …`

        - `id: str`

        - `input: Dict[str, object]`

        - `name: Literal["web_search", "web_fetch", "code_execution", 4 more]`

          - `"web_search"`

          - `"web_fetch"`

          - `"code_execution"`

          - `"bash_code_execution"`

          - `"text_editor_code_execution"`

          - `"tool_search_tool_regex"`

          - `"tool_search_tool_bm25"`

        - `type: Literal["server_tool_use"]`

          - `"server_tool_use"`

        - `cache_control: Optional[CacheControlEphemeral]`

          Create a cache control breakpoint at this content block.

          - `type: Literal["ephemeral"]`

            - `"ephemeral"`

          - `ttl: Optional[Literal["5m", "1h"]]`

            The time-to-live for the cache control breakpoint.

            This may be one the following values:

            - `5m`: 5 minutes
            - `1h`: 1 hour

            Defaults to `5m`.

            - `"5m"`

            - `"1h"`

        - `caller: Optional[Caller]`

          Tool invocation directly from the model.

          - `class DirectCaller: …`

            Tool invocation directly from the model.

            - `type: Literal["direct"]`

              - `"direct"`

          - `class ServerToolCaller: …`

            Tool invocation generated by a server-side tool.

            - `tool_id: str`

            - `type: Literal["code_execution_20250825"]`

              - `"code_execution_20250825"`

          - `class ServerToolCaller20260120: …`

            - `tool_id: str`

            - `type: Literal["code_execution_20260120"]`

              - `"code_execution_20260120"`

      - `class WebSearchToolResultBlockParam: …`

        - `content: WebSearchToolResultBlockParamContent`

          - `List[WebSearchResultBlockParam]`

            - `encrypted_content: str`

            - `title: str`

            - `type: Literal["web_search_result"]`

              - `"web_search_result"`

            - `url: str`

            - `page_age: Optional[str]`

          - `class WebSearchToolRequestError: …`

            - `error_code: WebSearchToolResultErrorCode`

              - `"invalid_tool_input"`

              - `"unavailable"`

              - `"max_uses_exceeded"`

              - `"too_many_requests"`

              - `"query_too_long"`

              - `"request_too_large"`

            - `type: Literal["web_search_tool_result_error"]`

              - `"web_search_tool_result_error"`

        - `tool_use_id: str`

        - `type: Literal["web_search_tool_result"]`

          - `"web_search_tool_result"`

        - `cache_control: Optional[CacheControlEphemeral]`

          Create a cache control breakpoint at this content block.

          - `type: Literal["ephemeral"]`

            - `"ephemeral"`

          - `ttl: Optional[Literal["5m", "1h"]]`

            The time-to-live for the cache control breakpoint.

            This may be one the following values:

            - `5m`: 5 minutes
            - `1h`: 1 hour

            Defaults to `5m`.

            - `"5m"`

            - `"1h"`

        - `caller: Optional[Caller]`

          Tool invocation directly from the model.

          - `class DirectCaller: …`

            Tool invocation directly from the model.

            - `type: Literal["direct"]`

              - `"direct"`

          - `class ServerToolCaller: …`

            Tool invocation generated by a server-side tool.

            - `tool_id: str`

            - `type: Literal["code_execution_20250825"]`

              - `"code_execution_20250825"`

          - `class ServerToolCaller20260120: …`

            - `tool_id: str`

            - `type: Literal["code_execution_20260120"]`

              - `"code_execution_20260120"`

      - `class WebFetchToolResultBlockParam: …`

        - `content: Content`

          - `class WebFetchToolResultErrorBlockParam: …`

            - `error_code: WebFetchToolResultErrorCode`

              - `"invalid_tool_input"`

              - `"url_too_long"`

              - `"url_not_allowed"`

              - `"url_not_accessible"`

              - `"unsupported_content_type"`

              - `"too_many_requests"`

              - `"max_uses_exceeded"`

              - `"unavailable"`

            - `type: Literal["web_fetch_tool_result_error"]`

              - `"web_fetch_tool_result_error"`

          - `class WebFetchBlockParam: …`

            - `content: DocumentBlockParam`

              - `source: Source`

                - `class Base64PDFSource: …`

                  - `data: str`

                  - `media_type: Literal["application/pdf"]`

                    - `"application/pdf"`

                  - `type: Literal["base64"]`

                    - `"base64"`

                - `class PlainTextSource: …`

                  - `data: str`

                  - `media_type: Literal["text/plain"]`

                    - `"text/plain"`

                  - `type: Literal["text"]`

                    - `"text"`

                - `class ContentBlockSource: …`

                  - `content: Union[str, List[ContentBlockSourceContent]]`

                    - `str`

                    - `List[ContentBlockSourceContent]`

                      - `class TextBlockParam: …`

                        - `text: str`

                        - `type: Literal["text"]`

                          - `"text"`

                        - `cache_control: Optional[CacheControlEphemeral]`

                          Create a cache control breakpoint at this content block.

                          - `type: Literal["ephemeral"]`

                            - `"ephemeral"`

                          - `ttl: Optional[Literal["5m", "1h"]]`

                            The time-to-live for the cache control breakpoint.

                            This may be one the following values:

                            - `5m`: 5 minutes
                            - `1h`: 1 hour

                            Defaults to `5m`.

                            - `"5m"`

                            - `"1h"`

                        - `citations: Optional[List[TextCitationParam]]`

                          - `class CitationCharLocationParam: …`

                            - `cited_text: str`

                            - `document_index: int`

                            - `document_title: Optional[str]`

                            - `end_char_index: int`

                            - `start_char_index: int`

                            - `type: Literal["char_location"]`

                              - `"char_location"`

                          - `class CitationPageLocationParam: …`

                            - `cited_text: str`

                            - `document_index: int`

                            - `document_title: Optional[str]`

                            - `end_page_number: int`

                            - `start_page_number: int`

                            - `type: Literal["page_location"]`

                              - `"page_location"`

                          - `class CitationContentBlockLocationParam: …`

                            - `cited_text: str`

                            - `document_index: int`

                            - `document_title: Optional[str]`

                            - `end_block_index: int`

                            - `start_block_index: int`

                            - `type: Literal["content_block_location"]`

                              - `"content_block_location"`

                          - `class CitationWebSearchResultLocationParam: …`

                            - `cited_text: str`

                            - `encrypted_index: str`

                            - `title: Optional[str]`

                            - `type: Literal["web_search_result_location"]`

                              - `"web_search_result_location"`

                            - `url: str`

                          - `class CitationSearchResultLocationParam: …`

                            - `cited_text: str`

                            - `end_block_index: int`

                            - `search_result_index: int`

                            - `source: str`

                            - `start_block_index: int`

                            - `title: Optional[str]`

                            - `type: Literal["search_result_location"]`

                              - `"search_result_location"`

                      - `class ImageBlockParam: …`

                        - `source: Source`

                          - `class Base64ImageSource: …`

                            - `data: str`

                            - `media_type: Literal["image/jpeg", "image/png", "image/gif", "image/webp"]`

                              - `"image/jpeg"`

                              - `"image/png"`

                              - `"image/gif"`

                              - `"image/webp"`

                            - `type: Literal["base64"]`

                              - `"base64"`

                          - `class URLImageSource: …`

                            - `type: Literal["url"]`

                              - `"url"`

                            - `url: str`

                        - `type: Literal["image"]`

                          - `"image"`

                        - `cache_control: Optional[CacheControlEphemeral]`

                          Create a cache control breakpoint at this content block.

                          - `type: Literal["ephemeral"]`

                            - `"ephemeral"`

                          - `ttl: Optional[Literal["5m", "1h"]]`

                            The time-to-live for the cache control breakpoint.

                            This may be one the following values:

                            - `5m`: 5 minutes
                            - `1h`: 1 hour

                            Defaults to `5m`.

                            - `"5m"`

                            - `"1h"`

                  - `type: Literal["content"]`

                    - `"content"`

                - `class URLPDFSource: …`

                  - `type: Literal["url"]`

                    - `"url"`

                  - `url: str`

              - `type: Literal["document"]`

                - `"document"`

              - `cache_control: Optional[CacheControlEphemeral]`

                Create a cache control breakpoint at this content block.

                - `type: Literal["ephemeral"]`

                  - `"ephemeral"`

                - `ttl: Optional[Literal["5m", "1h"]]`

                  The time-to-live for the cache control breakpoint.

                  This may be one the following values:

                  - `5m`: 5 minutes
                  - `1h`: 1 hour

                  Defaults to `5m`.

                  - `"5m"`

                  - `"1h"`

              - `citations: Optional[CitationsConfigParam]`

                - `enabled: Optional[bool]`

              - `context: Optional[str]`

              - `title: Optional[str]`

            - `type: Literal["web_fetch_result"]`

              - `"web_fetch_result"`

            - `url: str`

              Fetched content URL

            - `retrieved_at: Optional[str]`

              ISO 8601 timestamp when the content was retrieved

        - `tool_use_id: str`

        - `type: Literal["web_fetch_tool_result"]`

          - `"web_fetch_tool_result"`

        - `cache_control: Optional[CacheControlEphemeral]`

          Create a cache control breakpoint at this content block.

          - `type: Literal["ephemeral"]`

            - `"ephemeral"`

          - `ttl: Optional[Literal["5m", "1h"]]`

            The time-to-live for the cache control breakpoint.

            This may be one the following values:

            - `5m`: 5 minutes
            - `1h`: 1 hour

            Defaults to `5m`.

            - `"5m"`

            - `"1h"`

        - `caller: Optional[Caller]`

          Tool invocation directly from the model.

          - `class DirectCaller: …`

            Tool invocation directly from the model.

            - `type: Literal["direct"]`

              - `"direct"`

          - `class ServerToolCaller: …`

            Tool invocation generated by a server-side tool.

            - `tool_id: str`

            - `type: Literal["code_execution_20250825"]`

              - `"code_execution_20250825"`

          - `class ServerToolCaller20260120: …`

            - `tool_id: str`

            - `type: Literal["code_execution_20260120"]`

              - `"code_execution_20260120"`

      - `class CodeExecutionToolResultBlockParam: …`

        - `content: CodeExecutionToolResultBlockParamContent`

          Code execution result with encrypted stdout for PFC + web_search results.

          - `class CodeExecutionToolResultErrorParam: …`

            - `error_code: CodeExecutionToolResultErrorCode`

              - `"invalid_tool_input"`

              - `"unavailable"`

              - `"too_many_requests"`

              - `"execution_time_exceeded"`

            - `type: Literal["code_execution_tool_result_error"]`

              - `"code_execution_tool_result_error"`

          - `class CodeExecutionResultBlockParam: …`

            - `content: List[CodeExecutionOutputBlockParam]`

              - `file_id: str`

              - `type: Literal["code_execution_output"]`

                - `"code_execution_output"`

            - `return_code: int`

            - `stderr: str`

            - `stdout: str`

            - `type: Literal["code_execution_result"]`

              - `"code_execution_result"`

          - `class EncryptedCodeExecutionResultBlockParam: …`

            Code execution result with encrypted stdout for PFC + web_search results.

            - `content: List[CodeExecutionOutputBlockParam]`

              - `file_id: str`

              - `type: Literal["code_execution_output"]`

                - `"code_execution_output"`

            - `encrypted_stdout: str`

            - `return_code: int`

            - `stderr: str`

            - `type: Literal["encrypted_code_execution_result"]`

              - `"encrypted_code_execution_result"`

        - `tool_use_id: str`

        - `type: Literal["code_execution_tool_result"]`

          - `"code_execution_tool_result"`

        - `cache_control: Optional[CacheControlEphemeral]`

          Create a cache control breakpoint at this content block.

          - `type: Literal["ephemeral"]`

            - `"ephemeral"`

          - `ttl: Optional[Literal["5m", "1h"]]`

            The time-to-live for the cache control breakpoint.

            This may be one the following values:

            - `5m`: 5 minutes
            - `1h`: 1 hour

            Defaults to `5m`.

            - `"5m"`

            - `"1h"`

      - `class BashCodeExecutionToolResultBlockParam: …`

        - `content: Content`

          - `class BashCodeExecutionToolResultErrorParam: …`

            - `error_code: BashCodeExecutionToolResultErrorCode`

              - `"invalid_tool_input"`

              - `"unavailable"`

              - `"too_many_requests"`

              - `"execution_time_exceeded"`

              - `"output_file_too_large"`

            - `type: Literal["bash_code_execution_tool_result_error"]`

              - `"bash_code_execution_tool_result_error"`

          - `class BashCodeExecutionResultBlockParam: …`

            - `content: List[BashCodeExecutionOutputBlockParam]`

              - `file_id: str`

              - `type: Literal["bash_code_execution_output"]`

                - `"bash_code_execution_output"`

            - `return_code: int`

            - `stderr: str`

            - `stdout: str`

            - `type: Literal["bash_code_execution_result"]`

              - `"bash_code_execution_result"`

        - `tool_use_id: str`

        - `type: Literal["bash_code_execution_tool_result"]`

          - `"bash_code_execution_tool_result"`

        - `cache_control: Optional[CacheControlEphemeral]`

          Create a cache control breakpoint at this content block.

          - `type: Literal["ephemeral"]`

            - `"ephemeral"`

          - `ttl: Optional[Literal["5m", "1h"]]`

            The time-to-live for the cache control breakpoint.

            This may be one the following values:

            - `5m`: 5 minutes
            - `1h`: 1 hour

            Defaults to `5m`.

            - `"5m"`

            - `"1h"`

      - `class TextEditorCodeExecutionToolResultBlockParam: …`

        - `content: Content`

          - `class TextEditorCodeExecutionToolResultErrorParam: …`

            - `error_code: TextEditorCodeExecutionToolResultErrorCode`

              - `"invalid_tool_input"`

              - `"unavailable"`

              - `"too_many_requests"`

              - `"execution_time_exceeded"`

              - `"file_not_found"`

            - `type: Literal["text_editor_code_execution_tool_result_error"]`

              - `"text_editor_code_execution_tool_result_error"`

            - `error_message: Optional[str]`

          - `class TextEditorCodeExecutionViewResultBlockParam: …`

            - `content: str`

            - `file_type: Literal["text", "image", "pdf"]`

              - `"text"`

              - `"image"`

              - `"pdf"`

            - `type: Literal["text_editor_code_execution_view_result"]`

              - `"text_editor_code_execution_view_result"`

            - `num_lines: Optional[int]`

            - `start_line: Optional[int]`

            - `total_lines: Optional[int]`

          - `class TextEditorCodeExecutionCreateResultBlockParam: …`

            - `is_file_update: bool`

            - `type: Literal["text_editor_code_execution_create_result"]`

              - `"text_editor_code_execution_create_result"`

          - `class TextEditorCodeExecutionStrReplaceResultBlockParam: …`

            - `type: Literal["text_editor_code_execution_str_replace_result"]`

              - `"text_editor_code_execution_str_replace_result"`

            - `lines: Optional[List[str]]`

            - `new_lines: Optional[int]`

            - `new_start: Optional[int]`

            - `old_lines: Optional[int]`

            - `old_start: Optional[int]`

        - `tool_use_id: str`

        - `type: Literal["text_editor_code_execution_tool_result"]`

          - `"text_editor_code_execution_tool_result"`

        - `cache_control: Optional[CacheControlEphemeral]`

          Create a cache control breakpoint at this content block.

          - `type: Literal["ephemeral"]`

            - `"ephemeral"`

          - `ttl: Optional[Literal["5m", "1h"]]`

            The time-to-live for the cache control breakpoint.

            This may be one the following values:

            - `5m`: 5 minutes
            - `1h`: 1 hour

            Defaults to `5m`.

            - `"5m"`

            - `"1h"`

      - `class ToolSearchToolResultBlockParam: …`

        - `content: Content`

          - `class ToolSearchToolResultErrorParam: …`

            - `error_code: ToolSearchToolResultErrorCode`

              - `"invalid_tool_input"`

              - `"unavailable"`

              - `"too_many_requests"`

              - `"execution_time_exceeded"`

            - `type: Literal["tool_search_tool_result_error"]`

              - `"tool_search_tool_result_error"`

          - `class ToolSearchToolSearchResultBlockParam: …`

            - `tool_references: List[ToolReferenceBlockParam]`

              - `tool_name: str`

              - `type: Literal["tool_reference"]`

                - `"tool_reference"`

              - `cache_control: Optional[CacheControlEphemeral]`

                Create a cache control breakpoint at this content block.

                - `type: Literal["ephemeral"]`

                  - `"ephemeral"`

                - `ttl: Optional[Literal["5m", "1h"]]`

                  The time-to-live for the cache control breakpoint.

                  This may be one the following values:

                  - `5m`: 5 minutes
                  - `1h`: 1 hour

                  Defaults to `5m`.

                  - `"5m"`

                  - `"1h"`

            - `type: Literal["tool_search_tool_search_result"]`

              - `"tool_search_tool_search_result"`

        - `tool_use_id: str`

        - `type: Literal["tool_search_tool_result"]`

          - `"tool_search_tool_result"`

        - `cache_control: Optional[CacheControlEphemeral]`

          Create a cache control breakpoint at this content block.

          - `type: Literal["ephemeral"]`

            - `"ephemeral"`

          - `ttl: Optional[Literal["5m", "1h"]]`

            The time-to-live for the cache control breakpoint.

            This may be one the following values:

            - `5m`: 5 minutes
            - `1h`: 1 hour

            Defaults to `5m`.

            - `"5m"`

            - `"1h"`

      - `class ContainerUploadBlockParam: …`

        A content block that represents a file to be uploaded to the container
        Files uploaded via this block will be available in the container's input directory.

        - `file_id: str`

        - `type: Literal["container_upload"]`

          - `"container_upload"`

        - `cache_control: Optional[CacheControlEphemeral]`

          Create a cache control breakpoint at this content block.

          - `type: Literal["ephemeral"]`

            - `"ephemeral"`

          - `ttl: Optional[Literal["5m", "1h"]]`

            The time-to-live for the cache control breakpoint.

            This may be one the following values:

            - `5m`: 5 minutes
            - `1h`: 1 hour

            Defaults to `5m`.

            - `"5m"`

            - `"1h"`

  - `role: Literal["user", "assistant"]`

    - `"user"`

    - `"assistant"`

- `model: ModelParam`

  The model that will complete your prompt.

  See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

  - `Literal["claude-opus-4-6", "claude-sonnet-4-6", "claude-opus-4-5-20251101", 19 more]`

    The model that will complete your prompt.

    See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

    - `claude-opus-4-6` - Most intelligent model for building agents and coding
    - `claude-sonnet-4-6` - Frontier intelligence at scale — built for coding, agents, and enterprise workflows
    - `claude-opus-4-5-20251101` - Premium model combining maximum intelligence with practical performance
    - `claude-opus-4-5` - Premium model combining maximum intelligence with practical performance
    - `claude-3-7-sonnet-latest` - Deprecated: Will reach end-of-life on February 19th, 2026. Please migrate to a newer model. Visit https://docs.anthropic.com/en/docs/resources/model-deprecations for more information.
    - `claude-3-7-sonnet-20250219` - Deprecated: Will reach end-of-life on February 19th, 2026. Please migrate to a newer model. Visit https://docs.anthropic.com/en/docs/resources/model-deprecations for more information.
    - `claude-3-5-haiku-latest` - Deprecated: Will reach end-of-life on February 19th, 2026. Please migrate to a newer model. Visit https://docs.anthropic.com/en/docs/resources/model-deprecations for more information.
    - `claude-3-5-haiku-20241022` - Deprecated: Will reach end-of-life on February 19th, 2026. Please migrate to a newer model. Visit https://docs.anthropic.com/en/docs/resources/model-deprecations for more information.
    - `claude-haiku-4-5` - Hybrid model, capable of near-instant responses and extended thinking
    - `claude-haiku-4-5-20251001` - Hybrid model, capable of near-instant responses and extended thinking
    - `claude-sonnet-4-20250514` - High-performance model with extended thinking
    - `claude-sonnet-4-0` - High-performance model with extended thinking
    - `claude-4-sonnet-20250514` - High-performance model with extended thinking
    - `claude-sonnet-4-5` - Our best model for real-world agents and coding
    - `claude-sonnet-4-5-20250929` - Our best model for real-world agents and coding
    - `claude-opus-4-0` - Our most capable model
    - `claude-opus-4-20250514` - Our most capable model
    - `claude-4-opus-20250514` - Our most capable model
    - `claude-opus-4-1-20250805` - Our most capable model
    - `claude-3-opus-latest` - Deprecated: Will reach end-of-life on January 5th, 2026. Please migrate to a newer model. Visit https://docs.anthropic.com/en/docs/resources/model-deprecations for more information.
    - `claude-3-opus-20240229` - Deprecated: Will reach end-of-life on January 5th, 2026. Please migrate to a newer model. Visit https://docs.anthropic.com/en/docs/resources/model-deprecations for more information.
    - `claude-3-haiku-20240307` - Our previous most fast and cost-effective

    - `"claude-opus-4-6"`

      Most intelligent model for building agents and coding

    - `"claude-sonnet-4-6"`

      Frontier intelligence at scale — built for coding, agents, and enterprise workflows

    - `"claude-opus-4-5-20251101"`

      Premium model combining maximum intelligence with practical performance

    - `"claude-opus-4-5"`

      Premium model combining maximum intelligence with practical performance

    - `"claude-3-7-sonnet-latest"`

      High-performance model with early extended thinking

    - `"claude-3-7-sonnet-20250219"`

      High-performance model with early extended thinking

    - `"claude-3-5-haiku-latest"`

      Fastest and most compact model for near-instant responsiveness

    - `"claude-3-5-haiku-20241022"`

      Our fastest model

    - `"claude-haiku-4-5"`

      Hybrid model, capable of near-instant responses and extended thinking

    - `"claude-haiku-4-5-20251001"`

      Hybrid model, capable of near-instant responses and extended thinking

    - `"claude-sonnet-4-20250514"`

      High-performance model with extended thinking

    - `"claude-sonnet-4-0"`

      High-performance model with extended thinking

    - `"claude-4-sonnet-20250514"`

      High-performance model with extended thinking

    - `"claude-sonnet-4-5"`

      Our best model for real-world agents and coding

    - `"claude-sonnet-4-5-20250929"`

      Our best model for real-world agents and coding

    - `"claude-opus-4-0"`

      Our most capable model

    - `"claude-opus-4-20250514"`

      Our most capable model

    - `"claude-4-opus-20250514"`

      Our most capable model

    - `"claude-opus-4-1-20250805"`

      Our most capable model

    - `"claude-3-opus-latest"`

      Excels at writing and complex tasks

    - `"claude-3-opus-20240229"`

      Excels at writing and complex tasks

    - `"claude-3-haiku-20240307"`

      Our previous most fast and cost-effective

  - `str`

- `cache_control: Optional[CacheControlEphemeralParam]`

  Top-level cache control automatically applies a cache_control marker to the last cacheable block in the request.

  - `type: Literal["ephemeral"]`

    - `"ephemeral"`

  - `ttl: Optional[Literal["5m", "1h"]]`

    The time-to-live for the cache control breakpoint.

    This may be one the following values:

    - `5m`: 5 minutes
    - `1h`: 1 hour

    Defaults to `5m`.

    - `"5m"`

    - `"1h"`

- `container: Optional[str]`

  Container identifier for reuse across requests.

- `inference_geo: Optional[str]`

  Specifies the geographic region for inference processing. If not specified, the workspace's `default_inference_geo` is used.

- `metadata: Optional[MetadataParam]`

  An object describing metadata about the request.

  - `user_id: Optional[str]`

    An external identifier for the user who is associated with the request.

    This should be a uuid, hash value, or other opaque identifier. Anthropic may use this id to help detect abuse. Do not include any identifying information such as name, email address, or phone number.

- `output_config: Optional[OutputConfigParam]`

  Configuration options for the model's output, such as the output format.

  - `effort: Optional[Literal["low", "medium", "high", "max"]]`

    All possible effort levels.

    - `"low"`

    - `"medium"`

    - `"high"`

    - `"max"`

  - `format: Optional[JSONOutputFormat]`

    A schema to specify Claude's output format in responses. See [structured outputs](https://platform.claude.com/docs/en/build-with-claude/structured-outputs)

    - `schema: Dict[str, object]`

      The JSON schema of the format

    - `type: Literal["json_schema"]`

      - `"json_schema"`

- `service_tier: Optional[Literal["auto", "standard_only"]]`

  Determines whether to use priority capacity (if available) or standard capacity for this request.

  Anthropic offers different levels of service for your API requests. See [service-tiers](https://docs.claude.com/en/api/service-tiers) for details.

  - `"auto"`

  - `"standard_only"`

- `stop_sequences: Optional[SequenceNotStr[str]]`

  Custom text sequences that will cause the model to stop generating.

  Our models will normally stop when they have naturally completed their turn, which will result in a response `stop_reason` of `"end_turn"`.

  If you want the model to stop generating when it encounters custom strings of text, you can use the `stop_sequences` parameter. If the model encounters one of the custom sequences, the response `stop_reason` value will be `"stop_sequence"` and the response `stop_sequence` value will contain the matched stop sequence.

- `stream: Optional[Literal[false]]`

  Whether to incrementally stream the response using server-sent events.

  See [streaming](https://docs.claude.com/en/api/messages-streaming) for details.

  - `false`

- `system: Optional[Union[str, Iterable[TextBlockParam]]]`

  System prompt.

  A system prompt is a way of providing context and instructions to Claude, such as specifying a particular goal or role. See our [guide to system prompts](https://docs.claude.com/en/docs/system-prompts).

  - `str`

  - `Iterable[TextBlockParam]`

    - `text: str`

    - `type: Literal["text"]`

      - `"text"`

    - `cache_control: Optional[CacheControlEphemeral]`

      Create a cache control breakpoint at this content block.

      - `type: Literal["ephemeral"]`

        - `"ephemeral"`

      - `ttl: Optional[Literal["5m", "1h"]]`

        The time-to-live for the cache control breakpoint.

        This may be one the following values:

        - `5m`: 5 minutes
        - `1h`: 1 hour

        Defaults to `5m`.

        - `"5m"`

        - `"1h"`

    - `citations: Optional[List[TextCitationParam]]`

      - `class CitationCharLocationParam: …`

        - `cited_text: str`

        - `document_index: int`

        - `document_title: Optional[str]`

        - `end_char_index: int`

        - `start_char_index: int`

        - `type: Literal["char_location"]`

          - `"char_location"`

      - `class CitationPageLocationParam: …`

        - `cited_text: str`

        - `document_index: int`

        - `document_title: Optional[str]`

        - `end_page_number: int`

        - `start_page_number: int`

        - `type: Literal["page_location"]`

          - `"page_location"`

      - `class CitationContentBlockLocationParam: …`

        - `cited_text: str`

        - `document_index: int`

        - `document_title: Optional[str]`

        - `end_block_index: int`

        - `start_block_index: int`

        - `type: Literal["content_block_location"]`

          - `"content_block_location"`

      - `class CitationWebSearchResultLocationParam: …`

        - `cited_text: str`

        - `encrypted_index: str`

        - `title: Optional[str]`

        - `type: Literal["web_search_result_location"]`

          - `"web_search_result_location"`

        - `url: str`

      - `class CitationSearchResultLocationParam: …`

        - `cited_text: str`

        - `end_block_index: int`

        - `search_result_index: int`

        - `source: str`

        - `start_block_index: int`

        - `title: Optional[str]`

        - `type: Literal["search_result_location"]`

          - `"search_result_location"`

- `temperature: Optional[float]`

  Amount of randomness injected into the response.

  Defaults to `1.0`. Ranges from `0.0` to `1.0`. Use `temperature` closer to `0.0` for analytical / multiple choice, and closer to `1.0` for creative and generative tasks.

  Note that even with `temperature` of `0.0`, the results will not be fully deterministic.

- `thinking: Optional[ThinkingConfigParam]`

  Configuration for enabling Claude's extended thinking.

  When enabled, responses include `thinking` content blocks showing Claude's thinking process before the final answer. Requires a minimum budget of 1,024 tokens and counts towards your `max_tokens` limit.

  See [extended thinking](https://docs.claude.com/en/docs/build-with-claude/extended-thinking) for details.

  - `class ThinkingConfigEnabled: …`

    - `budget_tokens: int`

      Determines how many tokens Claude can use for its internal reasoning process. Larger budgets can enable more thorough analysis for complex problems, improving response quality.

      Must be ≥1024 and less than `max_tokens`.

      See [extended thinking](https://docs.claude.com/en/docs/build-with-claude/extended-thinking) for details.

    - `type: Literal["enabled"]`

      - `"enabled"`

  - `class ThinkingConfigDisabled: …`

    - `type: Literal["disabled"]`

      - `"disabled"`

  - `class ThinkingConfigAdaptive: …`

    - `type: Literal["adaptive"]`

      - `"adaptive"`

- `tool_choice: Optional[ToolChoiceParam]`

  How the model should use the provided tools. The model can use a specific tool, any available tool, decide by itself, or not use tools at all.

  - `class ToolChoiceAuto: …`

    The model will automatically decide whether to use tools.

    - `type: Literal["auto"]`

      - `"auto"`

    - `disable_parallel_tool_use: Optional[bool]`

      Whether to disable parallel tool use.

      Defaults to `false`. If set to `true`, the model will output at most one tool use.

  - `class ToolChoiceAny: …`

    The model will use any available tools.

    - `type: Literal["any"]`

      - `"any"`

    - `disable_parallel_tool_use: Optional[bool]`

      Whether to disable parallel tool use.

      Defaults to `false`. If set to `true`, the model will output exactly one tool use.

  - `class ToolChoiceTool: …`

    The model will use the specified tool with `tool_choice.name`.

    - `name: str`

      The name of the tool to use.

    - `type: Literal["tool"]`

      - `"tool"`

    - `disable_parallel_tool_use: Optional[bool]`

      Whether to disable parallel tool use.

      Defaults to `false`. If set to `true`, the model will output exactly one tool use.

  - `class ToolChoiceNone: …`

    The model will not be allowed to use tools.

    - `type: Literal["none"]`

      - `"none"`

- `tools: Optional[Iterable[ToolUnionParam]]`

  Definitions of tools that the model may use.

  If you include `tools` in your API request, the model may return `tool_use` content blocks that represent the model's use of those tools. You can then run those tools using the tool input generated by the model and then optionally return results back to the model using `tool_result` content blocks.

  There are two types of tools: **client tools** and **server tools**. The behavior described below applies to client tools. For [server tools](https://docs.claude.com/en/docs/agents-and-tools/tool-use/overview#server-tools), see their individual documentation as each has its own behavior (e.g., the [web search tool](https://docs.claude.com/en/docs/agents-and-tools/tool-use/web-search-tool)).

  Each tool definition includes:

  * `name`: Name of the tool.
  * `description`: Optional, but strongly-recommended description of the tool.
  * `input_schema`: [JSON schema](https://json-schema.org/draft/2020-12) for the tool `input` shape that the model will produce in `tool_use` output content blocks.

  For example, if you defined `tools` as:

  ```json
  [
    {
      "name": "get_stock_price",
      "description": "Get the current stock price for a given ticker symbol.",
      "input_schema": {
        "type": "object",
        "properties": {
          "ticker": {
            "type": "string",
            "description": "The stock ticker symbol, e.g. AAPL for Apple Inc."
          }
        },
        "required": ["ticker"]
      }
    }
  ]
  ```

  And then asked the model "What's the S&P 500 at today?", the model might produce `tool_use` content blocks in the response like this:

  ```json
  [
    {
      "type": "tool_use",
      "id": "toolu_01D7FLrfh4GYq7yT1ULFeyMV",
      "name": "get_stock_price",
      "input": { "ticker": "^GSPC" }
    }
  ]
  ```

  You might then run your `get_stock_price` tool with `{"ticker": "^GSPC"}` as an input, and return the following back to the model in a subsequent `user` message:

  ```json
  [
    {
      "type": "tool_result",
      "tool_use_id": "toolu_01D7FLrfh4GYq7yT1ULFeyMV",
      "content": "259.75 USD"
    }
  ]
  ```

  Tools can be used for workflows that include running client-side tools and functions, or more generally whenever you want the model to produce a particular JSON structure of output.

  See our [guide](https://docs.claude.com/en/docs/tool-use) for more details.

  - `class Tool: …`

    - `input_schema: InputSchema`

      [JSON schema](https://json-schema.org/draft/2020-12) for this tool's input.

      This defines the shape of the `input` that your tool accepts and that the model will produce.

      - `type: Literal["object"]`

        - `"object"`

      - `properties: Optional[Dict[str, object]]`

      - `required: Optional[List[str]]`

    - `name: str`

      Name of the tool.

      This is how the tool will be called by the model and in `tool_use` blocks.

    - `allowed_callers: Optional[List[Literal["direct", "code_execution_20250825", "code_execution_20260120"]]]`

      - `"direct"`

      - `"code_execution_20250825"`

      - `"code_execution_20260120"`

    - `cache_control: Optional[CacheControlEphemeral]`

      Create a cache control breakpoint at this content block.

      - `type: Literal["ephemeral"]`

        - `"ephemeral"`

      - `ttl: Optional[Literal["5m", "1h"]]`

        The time-to-live for the cache control breakpoint.

        This may be one the following values:

        - `5m`: 5 minutes
        - `1h`: 1 hour

        Defaults to `5m`.

        - `"5m"`

        - `"1h"`

    - `defer_loading: Optional[bool]`

      If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

    - `description: Optional[str]`

      Description of what this tool does.

      Tool descriptions should be as detailed as possible. The more information that the model has about what the tool is and how to use it, the better it will perform. You can use natural language descriptions to reinforce important aspects of the tool input JSON schema.

    - `eager_input_streaming: Optional[bool]`

      Enable eager input streaming for this tool. When true, tool input parameters will be streamed incrementally as they are generated, and types will be inferred on-the-fly rather than buffering the full JSON output. When false, streaming is disabled for this tool even if the fine-grained-tool-streaming beta is active. When null (default), uses the default behavior based on beta headers.

    - `input_examples: Optional[List[Dict[str, object]]]`

    - `strict: Optional[bool]`

      When true, guarantees schema validation on tool names and inputs

    - `type: Optional[Literal["custom"]]`

      - `"custom"`

  - `class ToolBash20250124: …`

    - `name: Literal["bash"]`

      Name of the tool.

      This is how the tool will be called by the model and in `tool_use` blocks.

      - `"bash"`

    - `type: Literal["bash_20250124"]`

      - `"bash_20250124"`

    - `allowed_callers: Optional[List[Literal["direct", "code_execution_20250825", "code_execution_20260120"]]]`

      - `"direct"`

      - `"code_execution_20250825"`

      - `"code_execution_20260120"`

    - `cache_control: Optional[CacheControlEphemeral]`

      Create a cache control breakpoint at this content block.

      - `type: Literal["ephemeral"]`

        - `"ephemeral"`

      - `ttl: Optional[Literal["5m", "1h"]]`

        The time-to-live for the cache control breakpoint.

        This may be one the following values:

        - `5m`: 5 minutes
        - `1h`: 1 hour

        Defaults to `5m`.

        - `"5m"`

        - `"1h"`

    - `defer_loading: Optional[bool]`

      If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

    - `input_examples: Optional[List[Dict[str, object]]]`

    - `strict: Optional[bool]`

      When true, guarantees schema validation on tool names and inputs

  - `class CodeExecutionTool20250522: …`

    - `name: Literal["code_execution"]`

      Name of the tool.

      This is how the tool will be called by the model and in `tool_use` blocks.

      - `"code_execution"`

    - `type: Literal["code_execution_20250522"]`

      - `"code_execution_20250522"`

    - `allowed_callers: Optional[List[Literal["direct", "code_execution_20250825", "code_execution_20260120"]]]`

      - `"direct"`

      - `"code_execution_20250825"`

      - `"code_execution_20260120"`

    - `cache_control: Optional[CacheControlEphemeral]`

      Create a cache control breakpoint at this content block.

      - `type: Literal["ephemeral"]`

        - `"ephemeral"`

      - `ttl: Optional[Literal["5m", "1h"]]`

        The time-to-live for the cache control breakpoint.

        This may be one the following values:

        - `5m`: 5 minutes
        - `1h`: 1 hour

        Defaults to `5m`.

        - `"5m"`

        - `"1h"`

    - `defer_loading: Optional[bool]`

      If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

    - `strict: Optional[bool]`

      When true, guarantees schema validation on tool names and inputs

  - `class CodeExecutionTool20250825: …`

    - `name: Literal["code_execution"]`

      Name of the tool.

      This is how the tool will be called by the model and in `tool_use` blocks.

      - `"code_execution"`

    - `type: Literal["code_execution_20250825"]`

      - `"code_execution_20250825"`

    - `allowed_callers: Optional[List[Literal["direct", "code_execution_20250825", "code_execution_20260120"]]]`

      - `"direct"`

      - `"code_execution_20250825"`

      - `"code_execution_20260120"`

    - `cache_control: Optional[CacheControlEphemeral]`

      Create a cache control breakpoint at this content block.

      - `type: Literal["ephemeral"]`

        - `"ephemeral"`

      - `ttl: Optional[Literal["5m", "1h"]]`

        The time-to-live for the cache control breakpoint.

        This may be one the following values:

        - `5m`: 5 minutes
        - `1h`: 1 hour

        Defaults to `5m`.

        - `"5m"`

        - `"1h"`

    - `defer_loading: Optional[bool]`

      If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

    - `strict: Optional[bool]`

      When true, guarantees schema validation on tool names and inputs

  - `class CodeExecutionTool20260120: …`

    Code execution tool with REPL state persistence (daemon mode + gVisor checkpoint).

    - `name: Literal["code_execution"]`

      Name of the tool.

      This is how the tool will be called by the model and in `tool_use` blocks.

      - `"code_execution"`

    - `type: Literal["code_execution_20260120"]`

      - `"code_execution_20260120"`

    - `allowed_callers: Optional[List[Literal["direct", "code_execution_20250825", "code_execution_20260120"]]]`

      - `"direct"`

      - `"code_execution_20250825"`

      - `"code_execution_20260120"`

    - `cache_control: Optional[CacheControlEphemeral]`

      Create a cache control breakpoint at this content block.

      - `type: Literal["ephemeral"]`

        - `"ephemeral"`

      - `ttl: Optional[Literal["5m", "1h"]]`

        The time-to-live for the cache control breakpoint.

        This may be one the following values:

        - `5m`: 5 minutes
        - `1h`: 1 hour

        Defaults to `5m`.

        - `"5m"`

        - `"1h"`

    - `defer_loading: Optional[bool]`

      If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

    - `strict: Optional[bool]`

      When true, guarantees schema validation on tool names and inputs

  - `class MemoryTool20250818: …`

    - `name: Literal["memory"]`

      Name of the tool.

      This is how the tool will be called by the model and in `tool_use` blocks.

      - `"memory"`

    - `type: Literal["memory_20250818"]`

      - `"memory_20250818"`

    - `allowed_callers: Optional[List[Literal["direct", "code_execution_20250825", "code_execution_20260120"]]]`

      - `"direct"`

      - `"code_execution_20250825"`

      - `"code_execution_20260120"`

    - `cache_control: Optional[CacheControlEphemeral]`

      Create a cache control breakpoint at this content block.

      - `type: Literal["ephemeral"]`

        - `"ephemeral"`

      - `ttl: Optional[Literal["5m", "1h"]]`

        The time-to-live for the cache control breakpoint.

        This may be one the following values:

        - `5m`: 5 minutes
        - `1h`: 1 hour

        Defaults to `5m`.

        - `"5m"`

        - `"1h"`

    - `defer_loading: Optional[bool]`

      If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

    - `input_examples: Optional[List[Dict[str, object]]]`

    - `strict: Optional[bool]`

      When true, guarantees schema validation on tool names and inputs

  - `class ToolTextEditor20250124: …`

    - `name: Literal["str_replace_editor"]`

      Name of the tool.

      This is how the tool will be called by the model and in `tool_use` blocks.

      - `"str_replace_editor"`

    - `type: Literal["text_editor_20250124"]`

      - `"text_editor_20250124"`

    - `allowed_callers: Optional[List[Literal["direct", "code_execution_20250825", "code_execution_20260120"]]]`

      - `"direct"`

      - `"code_execution_20250825"`

      - `"code_execution_20260120"`

    - `cache_control: Optional[CacheControlEphemeral]`

      Create a cache control breakpoint at this content block.

      - `type: Literal["ephemeral"]`

        - `"ephemeral"`

      - `ttl: Optional[Literal["5m", "1h"]]`

        The time-to-live for the cache control breakpoint.

        This may be one the following values:

        - `5m`: 5 minutes
        - `1h`: 1 hour

        Defaults to `5m`.

        - `"5m"`

        - `"1h"`

    - `defer_loading: Optional[bool]`

      If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

    - `input_examples: Optional[List[Dict[str, object]]]`

    - `strict: Optional[bool]`

      When true, guarantees schema validation on tool names and inputs

  - `class ToolTextEditor20250429: …`

    - `name: Literal["str_replace_based_edit_tool"]`

      Name of the tool.

      This is how the tool will be called by the model and in `tool_use` blocks.

      - `"str_replace_based_edit_tool"`

    - `type: Literal["text_editor_20250429"]`

      - `"text_editor_20250429"`

    - `allowed_callers: Optional[List[Literal["direct", "code_execution_20250825", "code_execution_20260120"]]]`

      - `"direct"`

      - `"code_execution_20250825"`

      - `"code_execution_20260120"`

    - `cache_control: Optional[CacheControlEphemeral]`

      Create a cache control breakpoint at this content block.

      - `type: Literal["ephemeral"]`

        - `"ephemeral"`

      - `ttl: Optional[Literal["5m", "1h"]]`

        The time-to-live for the cache control breakpoint.

        This may be one the following values:

        - `5m`: 5 minutes
        - `1h`: 1 hour

        Defaults to `5m`.

        - `"5m"`

        - `"1h"`

    - `defer_loading: Optional[bool]`

      If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

    - `input_examples: Optional[List[Dict[str, object]]]`

    - `strict: Optional[bool]`

      When true, guarantees schema validation on tool names and inputs

  - `class ToolTextEditor20250728: …`

    - `name: Literal["str_replace_based_edit_tool"]`

      Name of the tool.

      This is how the tool will be called by the model and in `tool_use` blocks.

      - `"str_replace_based_edit_tool"`

    - `type: Literal["text_editor_20250728"]`

      - `"text_editor_20250728"`

    - `allowed_callers: Optional[List[Literal["direct", "code_execution_20250825", "code_execution_20260120"]]]`

      - `"direct"`

      - `"code_execution_20250825"`

      - `"code_execution_20260120"`

    - `cache_control: Optional[CacheControlEphemeral]`

      Create a cache control breakpoint at this content block.

      - `type: Literal["ephemeral"]`

        - `"ephemeral"`

      - `ttl: Optional[Literal["5m", "1h"]]`

        The time-to-live for the cache control breakpoint.

        This may be one the following values:

        - `5m`: 5 minutes
        - `1h`: 1 hour

        Defaults to `5m`.

        - `"5m"`

        - `"1h"`

    - `defer_loading: Optional[bool]`

      If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

    - `input_examples: Optional[List[Dict[str, object]]]`

    - `max_characters: Optional[int]`

      Maximum number of characters to display when viewing a file. If not specified, defaults to displaying the full file.

    - `strict: Optional[bool]`

      When true, guarantees schema validation on tool names and inputs

  - `class WebSearchTool20250305: …`

    - `name: Literal["web_search"]`

      Name of the tool.

      This is how the tool will be called by the model and in `tool_use` blocks.

      - `"web_search"`

    - `type: Literal["web_search_20250305"]`

      - `"web_search_20250305"`

    - `allowed_callers: Optional[List[Literal["direct", "code_execution_20250825", "code_execution_20260120"]]]`

      - `"direct"`

      - `"code_execution_20250825"`

      - `"code_execution_20260120"`

    - `allowed_domains: Optional[List[str]]`

      If provided, only these domains will be included in results. Cannot be used alongside `blocked_domains`.

    - `blocked_domains: Optional[List[str]]`

      If provided, these domains will never appear in results. Cannot be used alongside `allowed_domains`.

    - `cache_control: Optional[CacheControlEphemeral]`

      Create a cache control breakpoint at this content block.

      - `type: Literal["ephemeral"]`

        - `"ephemeral"`

      - `ttl: Optional[Literal["5m", "1h"]]`

        The time-to-live for the cache control breakpoint.

        This may be one the following values:

        - `5m`: 5 minutes
        - `1h`: 1 hour

        Defaults to `5m`.

        - `"5m"`

        - `"1h"`

    - `defer_loading: Optional[bool]`

      If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

    - `max_uses: Optional[int]`

      Maximum number of times the tool can be used in the API request.

    - `strict: Optional[bool]`

      When true, guarantees schema validation on tool names and inputs

    - `user_location: Optional[UserLocation]`

      Parameters for the user's location. Used to provide more relevant search results.

      - `type: Literal["approximate"]`

        - `"approximate"`

      - `city: Optional[str]`

        The city of the user.

      - `country: Optional[str]`

        The two letter [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) of the user.

      - `region: Optional[str]`

        The region of the user.

      - `timezone: Optional[str]`

        The [IANA timezone](https://nodatime.org/TimeZones) of the user.

  - `class WebFetchTool20250910: …`

    - `name: Literal["web_fetch"]`

      Name of the tool.

      This is how the tool will be called by the model and in `tool_use` blocks.

      - `"web_fetch"`

    - `type: Literal["web_fetch_20250910"]`

      - `"web_fetch_20250910"`

    - `allowed_callers: Optional[List[Literal["direct", "code_execution_20250825", "code_execution_20260120"]]]`

      - `"direct"`

      - `"code_execution_20250825"`

      - `"code_execution_20260120"`

    - `allowed_domains: Optional[List[str]]`

      List of domains to allow fetching from

    - `blocked_domains: Optional[List[str]]`

      List of domains to block fetching from

    - `cache_control: Optional[CacheControlEphemeral]`

      Create a cache control breakpoint at this content block.

      - `type: Literal["ephemeral"]`

        - `"ephemeral"`

      - `ttl: Optional[Literal["5m", "1h"]]`

        The time-to-live for the cache control breakpoint.

        This may be one the following values:

        - `5m`: 5 minutes
        - `1h`: 1 hour

        Defaults to `5m`.

        - `"5m"`

        - `"1h"`

    - `citations: Optional[CitationsConfigParam]`

      Citations configuration for fetched documents. Citations are disabled by default.

      - `enabled: Optional[bool]`

    - `defer_loading: Optional[bool]`

      If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

    - `max_content_tokens: Optional[int]`

      Maximum number of tokens used by including web page text content in the context. The limit is approximate and does not apply to binary content such as PDFs.

    - `max_uses: Optional[int]`

      Maximum number of times the tool can be used in the API request.

    - `strict: Optional[bool]`

      When true, guarantees schema validation on tool names and inputs

  - `class WebSearchTool20260209: …`

    - `name: Literal["web_search"]`

      Name of the tool.

      This is how the tool will be called by the model and in `tool_use` blocks.

      - `"web_search"`

    - `type: Literal["web_search_20260209"]`

      - `"web_search_20260209"`

    - `allowed_callers: Optional[List[Literal["direct", "code_execution_20250825", "code_execution_20260120"]]]`

      - `"direct"`

      - `"code_execution_20250825"`

      - `"code_execution_20260120"`

    - `allowed_domains: Optional[List[str]]`

      If provided, only these domains will be included in results. Cannot be used alongside `blocked_domains`.

    - `blocked_domains: Optional[List[str]]`

      If provided, these domains will never appear in results. Cannot be used alongside `allowed_domains`.

    - `cache_control: Optional[CacheControlEphemeral]`

      Create a cache control breakpoint at this content block.

      - `type: Literal["ephemeral"]`

        - `"ephemeral"`

      - `ttl: Optional[Literal["5m", "1h"]]`

        The time-to-live for the cache control breakpoint.

        This may be one the following values:

        - `5m`: 5 minutes
        - `1h`: 1 hour

        Defaults to `5m`.

        - `"5m"`

        - `"1h"`

    - `defer_loading: Optional[bool]`

      If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

    - `max_uses: Optional[int]`

      Maximum number of times the tool can be used in the API request.

    - `strict: Optional[bool]`

      When true, guarantees schema validation on tool names and inputs

    - `user_location: Optional[UserLocation]`

      Parameters for the user's location. Used to provide more relevant search results.

      - `type: Literal["approximate"]`

        - `"approximate"`

      - `city: Optional[str]`

        The city of the user.

      - `country: Optional[str]`

        The two letter [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) of the user.

      - `region: Optional[str]`

        The region of the user.

      - `timezone: Optional[str]`

        The [IANA timezone](https://nodatime.org/TimeZones) of the user.

  - `class WebFetchTool20260209: …`

    - `name: Literal["web_fetch"]`

      Name of the tool.

      This is how the tool will be called by the model and in `tool_use` blocks.

      - `"web_fetch"`

    - `type: Literal["web_fetch_20260209"]`

      - `"web_fetch_20260209"`

    - `allowed_callers: Optional[List[Literal["direct", "code_execution_20250825", "code_execution_20260120"]]]`

      - `"direct"`

      - `"code_execution_20250825"`

      - `"code_execution_20260120"`

    - `allowed_domains: Optional[List[str]]`

      List of domains to allow fetching from

    - `blocked_domains: Optional[List[str]]`

      List of domains to block fetching from

    - `cache_control: Optional[CacheControlEphemeral]`

      Create a cache control breakpoint at this content block.

      - `type: Literal["ephemeral"]`

        - `"ephemeral"`

      - `ttl: Optional[Literal["5m", "1h"]]`

        The time-to-live for the cache control breakpoint.

        This may be one the following values:

        - `5m`: 5 minutes
        - `1h`: 1 hour

        Defaults to `5m`.

        - `"5m"`

        - `"1h"`

    - `citations: Optional[CitationsConfigParam]`

      Citations configuration for fetched documents. Citations are disabled by default.

      - `enabled: Optional[bool]`

    - `defer_loading: Optional[bool]`

      If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

    - `max_content_tokens: Optional[int]`

      Maximum number of tokens used by including web page text content in the context. The limit is approximate and does not apply to binary content such as PDFs.

    - `max_uses: Optional[int]`

      Maximum number of times the tool can be used in the API request.

    - `strict: Optional[bool]`

      When true, guarantees schema validation on tool names and inputs

  - `class ToolSearchToolBm25_20251119: …`

    - `name: Literal["tool_search_tool_bm25"]`

      Name of the tool.

      This is how the tool will be called by the model and in `tool_use` blocks.

      - `"tool_search_tool_bm25"`

    - `type: Literal["tool_search_tool_bm25_20251119", "tool_search_tool_bm25"]`

      - `"tool_search_tool_bm25_20251119"`

      - `"tool_search_tool_bm25"`

    - `allowed_callers: Optional[List[Literal["direct", "code_execution_20250825", "code_execution_20260120"]]]`

      - `"direct"`

      - `"code_execution_20250825"`

      - `"code_execution_20260120"`

    - `cache_control: Optional[CacheControlEphemeral]`

      Create a cache control breakpoint at this content block.

      - `type: Literal["ephemeral"]`

        - `"ephemeral"`

      - `ttl: Optional[Literal["5m", "1h"]]`

        The time-to-live for the cache control breakpoint.

        This may be one the following values:

        - `5m`: 5 minutes
        - `1h`: 1 hour

        Defaults to `5m`.

        - `"5m"`

        - `"1h"`

    - `defer_loading: Optional[bool]`

      If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

    - `strict: Optional[bool]`

      When true, guarantees schema validation on tool names and inputs

  - `class ToolSearchToolRegex20251119: …`

    - `name: Literal["tool_search_tool_regex"]`

      Name of the tool.

      This is how the tool will be called by the model and in `tool_use` blocks.

      - `"tool_search_tool_regex"`

    - `type: Literal["tool_search_tool_regex_20251119", "tool_search_tool_regex"]`

      - `"tool_search_tool_regex_20251119"`

      - `"tool_search_tool_regex"`

    - `allowed_callers: Optional[List[Literal["direct", "code_execution_20250825", "code_execution_20260120"]]]`

      - `"direct"`

      - `"code_execution_20250825"`

      - `"code_execution_20260120"`

    - `cache_control: Optional[CacheControlEphemeral]`

      Create a cache control breakpoint at this content block.

      - `type: Literal["ephemeral"]`

        - `"ephemeral"`

      - `ttl: Optional[Literal["5m", "1h"]]`

        The time-to-live for the cache control breakpoint.

        This may be one the following values:

        - `5m`: 5 minutes
        - `1h`: 1 hour

        Defaults to `5m`.

        - `"5m"`

        - `"1h"`

    - `defer_loading: Optional[bool]`

      If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

    - `strict: Optional[bool]`

      When true, guarantees schema validation on tool names and inputs

- `top_k: Optional[int]`

  Only sample from the top K options for each subsequent token.

  Used to remove "long tail" low probability responses. [Learn more technical details here](https://towardsdatascience.com/how-to-sample-from-language-models-682bceb97277).

  Recommended for advanced use cases only. You usually only need to use `temperature`.

- `top_p: Optional[float]`

  Use nucleus sampling.

  In nucleus sampling, we compute the cumulative distribution over all the options for each subsequent token in decreasing probability order and cut it off once it reaches a particular probability specified by `top_p`. You should either alter `temperature` or `top_p`, but not both.

  Recommended for advanced use cases only. You usually only need to use `temperature`.

### Returns

- `class Message: …`

  - `id: str`

    Unique object identifier.

    The format and length of IDs may change over time.

  - `container: Optional[Container]`

    Information about the container used in the request (for the code execution tool)

    - `id: str`

      Identifier for the container used in this request

    - `expires_at: datetime`

      The time at which the container will expire.

  - `content: List[ContentBlock]`

    Content generated by the model.

    This is an array of content blocks, each of which has a `type` that determines its shape.

    Example:

    ```json
    [{"type": "text", "text": "Hi, I'm Claude."}]
    ```

    If the request input `messages` ended with an `assistant` turn, then the response `content` will continue directly from that last turn. You can use this to constrain the model's output.

    For example, if the input `messages` were:

    ```json
    [
      {"role": "user", "content": "What's the Greek name for Sun? (A) Sol (B) Helios (C) Sun"},
      {"role": "assistant", "content": "The best answer is ("}
    ]
    ```

    Then the response `content` might be:

    ```json
    [{"type": "text", "text": "B)"}]
    ```

    - `class TextBlock: …`

      - `citations: Optional[List[TextCitation]]`

        Citations supporting the text block.

        The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

        - `class CitationCharLocation: …`

          - `cited_text: str`

          - `document_index: int`

          - `document_title: Optional[str]`

          - `end_char_index: int`

          - `file_id: Optional[str]`

          - `start_char_index: int`

          - `type: Literal["char_location"]`

            - `"char_location"`

        - `class CitationPageLocation: …`

          - `cited_text: str`

          - `document_index: int`

          - `document_title: Optional[str]`

          - `end_page_number: int`

          - `file_id: Optional[str]`

          - `start_page_number: int`

          - `type: Literal["page_location"]`

            - `"page_location"`

        - `class CitationContentBlockLocation: …`

          - `cited_text: str`

          - `document_index: int`

          - `document_title: Optional[str]`

          - `end_block_index: int`

          - `file_id: Optional[str]`

          - `start_block_index: int`

          - `type: Literal["content_block_location"]`

            - `"content_block_location"`

        - `class CitationsWebSearchResultLocation: …`

          - `cited_text: str`

          - `encrypted_index: str`

          - `title: Optional[str]`

          - `type: Literal["web_search_result_location"]`

            - `"web_search_result_location"`

          - `url: str`

        - `class CitationsSearchResultLocation: …`

          - `cited_text: str`

          - `end_block_index: int`

          - `search_result_index: int`

          - `source: str`

          - `start_block_index: int`

          - `title: Optional[str]`

          - `type: Literal["search_result_location"]`

            - `"search_result_location"`

      - `text: str`

      - `type: Literal["text"]`

        - `"text"`

    - `class ThinkingBlock: …`

      - `signature: str`

      - `thinking: str`

      - `type: Literal["thinking"]`

        - `"thinking"`

    - `class RedactedThinkingBlock: …`

      - `data: str`

      - `type: Literal["redacted_thinking"]`

        - `"redacted_thinking"`

    - `class ToolUseBlock: …`

      - `id: str`

      - `caller: Caller`

        Tool invocation directly from the model.

        - `class DirectCaller: …`

          Tool invocation directly from the model.

          - `type: Literal["direct"]`

            - `"direct"`

        - `class ServerToolCaller: …`

          Tool invocation generated by a server-side tool.

          - `tool_id: str`

          - `type: Literal["code_execution_20250825"]`

            - `"code_execution_20250825"`

        - `class ServerToolCaller20260120: …`

          - `tool_id: str`

          - `type: Literal["code_execution_20260120"]`

            - `"code_execution_20260120"`

      - `input: Dict[str, object]`

      - `name: str`

      - `type: Literal["tool_use"]`

        - `"tool_use"`

    - `class ServerToolUseBlock: …`

      - `id: str`

      - `caller: Caller`

        Tool invocation directly from the model.

        - `class DirectCaller: …`

          Tool invocation directly from the model.

          - `type: Literal["direct"]`

            - `"direct"`

        - `class ServerToolCaller: …`

          Tool invocation generated by a server-side tool.

          - `tool_id: str`

          - `type: Literal["code_execution_20250825"]`

            - `"code_execution_20250825"`

        - `class ServerToolCaller20260120: …`

          - `tool_id: str`

          - `type: Literal["code_execution_20260120"]`

            - `"code_execution_20260120"`

      - `input: Dict[str, object]`

      - `name: Literal["web_search", "web_fetch", "code_execution", 4 more]`

        - `"web_search"`

        - `"web_fetch"`

        - `"code_execution"`

        - `"bash_code_execution"`

        - `"text_editor_code_execution"`

        - `"tool_search_tool_regex"`

        - `"tool_search_tool_bm25"`

      - `type: Literal["server_tool_use"]`

        - `"server_tool_use"`

    - `class WebSearchToolResultBlock: …`

      - `caller: Caller`

        Tool invocation directly from the model.

        - `class DirectCaller: …`

          Tool invocation directly from the model.

          - `type: Literal["direct"]`

            - `"direct"`

        - `class ServerToolCaller: …`

          Tool invocation generated by a server-side tool.

          - `tool_id: str`

          - `type: Literal["code_execution_20250825"]`

            - `"code_execution_20250825"`

        - `class ServerToolCaller20260120: …`

          - `tool_id: str`

          - `type: Literal["code_execution_20260120"]`

            - `"code_execution_20260120"`

      - `content: WebSearchToolResultBlockContent`

        - `class WebSearchToolResultError: …`

          - `error_code: WebSearchToolResultErrorCode`

            - `"invalid_tool_input"`

            - `"unavailable"`

            - `"max_uses_exceeded"`

            - `"too_many_requests"`

            - `"query_too_long"`

            - `"request_too_large"`

          - `type: Literal["web_search_tool_result_error"]`

            - `"web_search_tool_result_error"`

        - `List[WebSearchResultBlock]`

          - `encrypted_content: str`

          - `page_age: Optional[str]`

          - `title: str`

          - `type: Literal["web_search_result"]`

            - `"web_search_result"`

          - `url: str`

      - `tool_use_id: str`

      - `type: Literal["web_search_tool_result"]`

        - `"web_search_tool_result"`

    - `class WebFetchToolResultBlock: …`

      - `caller: Caller`

        Tool invocation directly from the model.

        - `class DirectCaller: …`

          Tool invocation directly from the model.

          - `type: Literal["direct"]`

            - `"direct"`

        - `class ServerToolCaller: …`

          Tool invocation generated by a server-side tool.

          - `tool_id: str`

          - `type: Literal["code_execution_20250825"]`

            - `"code_execution_20250825"`

        - `class ServerToolCaller20260120: …`

          - `tool_id: str`

          - `type: Literal["code_execution_20260120"]`

            - `"code_execution_20260120"`

      - `content: Content`

        - `class WebFetchToolResultErrorBlock: …`

          - `error_code: WebFetchToolResultErrorCode`

            - `"invalid_tool_input"`

            - `"url_too_long"`

            - `"url_not_allowed"`

            - `"url_not_accessible"`

            - `"unsupported_content_type"`

            - `"too_many_requests"`

            - `"max_uses_exceeded"`

            - `"unavailable"`

          - `type: Literal["web_fetch_tool_result_error"]`

            - `"web_fetch_tool_result_error"`

        - `class WebFetchBlock: …`

          - `content: DocumentBlock`

            - `citations: Optional[CitationsConfig]`

              Citation configuration for the document

              - `enabled: bool`

            - `source: Source`

              - `class Base64PDFSource: …`

                - `data: str`

                - `media_type: Literal["application/pdf"]`

                  - `"application/pdf"`

                - `type: Literal["base64"]`

                  - `"base64"`

              - `class PlainTextSource: …`

                - `data: str`

                - `media_type: Literal["text/plain"]`

                  - `"text/plain"`

                - `type: Literal["text"]`

                  - `"text"`

            - `title: Optional[str]`

              The title of the document

            - `type: Literal["document"]`

              - `"document"`

          - `retrieved_at: Optional[str]`

            ISO 8601 timestamp when the content was retrieved

          - `type: Literal["web_fetch_result"]`

            - `"web_fetch_result"`

          - `url: str`

            Fetched content URL

      - `tool_use_id: str`

      - `type: Literal["web_fetch_tool_result"]`

        - `"web_fetch_tool_result"`

    - `class CodeExecutionToolResultBlock: …`

      - `content: CodeExecutionToolResultBlockContent`

        Code execution result with encrypted stdout for PFC + web_search results.

        - `class CodeExecutionToolResultError: …`

          - `error_code: CodeExecutionToolResultErrorCode`

            - `"invalid_tool_input"`

            - `"unavailable"`

            - `"too_many_requests"`

            - `"execution_time_exceeded"`

          - `type: Literal["code_execution_tool_result_error"]`

            - `"code_execution_tool_result_error"`

        - `class CodeExecutionResultBlock: …`

          - `content: List[CodeExecutionOutputBlock]`

            - `file_id: str`

            - `type: Literal["code_execution_output"]`

              - `"code_execution_output"`

          - `return_code: int`

          - `stderr: str`

          - `stdout: str`

          - `type: Literal["code_execution_result"]`

            - `"code_execution_result"`

        - `class EncryptedCodeExecutionResultBlock: …`

          Code execution result with encrypted stdout for PFC + web_search results.

          - `content: List[CodeExecutionOutputBlock]`

            - `file_id: str`

            - `type: Literal["code_execution_output"]`

              - `"code_execution_output"`

          - `encrypted_stdout: str`

          - `return_code: int`

          - `stderr: str`

          - `type: Literal["encrypted_code_execution_result"]`

            - `"encrypted_code_execution_result"`

      - `tool_use_id: str`

      - `type: Literal["code_execution_tool_result"]`

        - `"code_execution_tool_result"`

    - `class BashCodeExecutionToolResultBlock: …`

      - `content: Content`

        - `class BashCodeExecutionToolResultError: …`

          - `error_code: BashCodeExecutionToolResultErrorCode`

            - `"invalid_tool_input"`

            - `"unavailable"`

            - `"too_many_requests"`

            - `"execution_time_exceeded"`

            - `"output_file_too_large"`

          - `type: Literal["bash_code_execution_tool_result_error"]`

            - `"bash_code_execution_tool_result_error"`

        - `class BashCodeExecutionResultBlock: …`

          - `content: List[BashCodeExecutionOutputBlock]`

            - `file_id: str`

            - `type: Literal["bash_code_execution_output"]`

              - `"bash_code_execution_output"`

          - `return_code: int`

          - `stderr: str`

          - `stdout: str`

          - `type: Literal["bash_code_execution_result"]`

            - `"bash_code_execution_result"`

      - `tool_use_id: str`

      - `type: Literal["bash_code_execution_tool_result"]`

        - `"bash_code_execution_tool_result"`

    - `class TextEditorCodeExecutionToolResultBlock: …`

      - `content: Content`

        - `class TextEditorCodeExecutionToolResultError: …`

          - `error_code: TextEditorCodeExecutionToolResultErrorCode`

            - `"invalid_tool_input"`

            - `"unavailable"`

            - `"too_many_requests"`

            - `"execution_time_exceeded"`

            - `"file_not_found"`

          - `error_message: Optional[str]`

          - `type: Literal["text_editor_code_execution_tool_result_error"]`

            - `"text_editor_code_execution_tool_result_error"`

        - `class TextEditorCodeExecutionViewResultBlock: …`

          - `content: str`

          - `file_type: Literal["text", "image", "pdf"]`

            - `"text"`

            - `"image"`

            - `"pdf"`

          - `num_lines: Optional[int]`

          - `start_line: Optional[int]`

          - `total_lines: Optional[int]`

          - `type: Literal["text_editor_code_execution_view_result"]`

            - `"text_editor_code_execution_view_result"`

        - `class TextEditorCodeExecutionCreateResultBlock: …`

          - `is_file_update: bool`

          - `type: Literal["text_editor_code_execution_create_result"]`

            - `"text_editor_code_execution_create_result"`

        - `class TextEditorCodeExecutionStrReplaceResultBlock: …`

          - `lines: Optional[List[str]]`

          - `new_lines: Optional[int]`

          - `new_start: Optional[int]`

          - `old_lines: Optional[int]`

          - `old_start: Optional[int]`

          - `type: Literal["text_editor_code_execution_str_replace_result"]`

            - `"text_editor_code_execution_str_replace_result"`

      - `tool_use_id: str`

      - `type: Literal["text_editor_code_execution_tool_result"]`

        - `"text_editor_code_execution_tool_result"`

    - `class ToolSearchToolResultBlock: …`

      - `content: Content`

        - `class ToolSearchToolResultError: …`

          - `error_code: ToolSearchToolResultErrorCode`

            - `"invalid_tool_input"`

            - `"unavailable"`

            - `"too_many_requests"`

            - `"execution_time_exceeded"`

          - `error_message: Optional[str]`

          - `type: Literal["tool_search_tool_result_error"]`

            - `"tool_search_tool_result_error"`

        - `class ToolSearchToolSearchResultBlock: …`

          - `tool_references: List[ToolReferenceBlock]`

            - `tool_name: str`

            - `type: Literal["tool_reference"]`

              - `"tool_reference"`

          - `type: Literal["tool_search_tool_search_result"]`

            - `"tool_search_tool_search_result"`

      - `tool_use_id: str`

      - `type: Literal["tool_search_tool_result"]`

        - `"tool_search_tool_result"`

    - `class ContainerUploadBlock: …`

      Response model for a file uploaded to the container.

      - `file_id: str`

      - `type: Literal["container_upload"]`

        - `"container_upload"`

  - `model: Model`

    The model that will complete your prompt.

    See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

    - `Literal["claude-opus-4-6", "claude-sonnet-4-6", "claude-opus-4-5-20251101", 19 more]`

      The model that will complete your prompt.

      See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

      - `claude-opus-4-6` - Most intelligent model for building agents and coding
      - `claude-sonnet-4-6` - Frontier intelligence at scale — built for coding, agents, and enterprise workflows
      - `claude-opus-4-5-20251101` - Premium model combining maximum intelligence with practical performance
      - `claude-opus-4-5` - Premium model combining maximum intelligence with practical performance
      - `claude-3-7-sonnet-latest` - Deprecated: Will reach end-of-life on February 19th, 2026. Please migrate to a newer model. Visit https://docs.anthropic.com/en/docs/resources/model-deprecations for more information.
      - `claude-3-7-sonnet-20250219` - Deprecated: Will reach end-of-life on February 19th, 2026. Please migrate to a newer model. Visit https://docs.anthropic.com/en/docs/resources/model-deprecations for more information.
      - `claude-3-5-haiku-latest` - Deprecated: Will reach end-of-life on February 19th, 2026. Please migrate to a newer model. Visit https://docs.anthropic.com/en/docs/resources/model-deprecations for more information.
      - `claude-3-5-haiku-20241022` - Deprecated: Will reach end-of-life on February 19th, 2026. Please migrate to a newer model. Visit https://docs.anthropic.com/en/docs/resources/model-deprecations for more information.
      - `claude-haiku-4-5` - Hybrid model, capable of near-instant responses and extended thinking
      - `claude-haiku-4-5-20251001` - Hybrid model, capable of near-instant responses and extended thinking
      - `claude-sonnet-4-20250514` - High-performance model with extended thinking
      - `claude-sonnet-4-0` - High-performance model with extended thinking
      - `claude-4-sonnet-20250514` - High-performance model with extended thinking
      - `claude-sonnet-4-5` - Our best model for real-world agents and coding
      - `claude-sonnet-4-5-20250929` - Our best model for real-world agents and coding
      - `claude-opus-4-0` - Our most capable model
      - `claude-opus-4-20250514` - Our most capable model
      - `claude-4-opus-20250514` - Our most capable model
      - `claude-opus-4-1-20250805` - Our most capable model
      - `claude-3-opus-latest` - Deprecated: Will reach end-of-life on January 5th, 2026. Please migrate to a newer model. Visit https://docs.anthropic.com/en/docs/resources/model-deprecations for more information.
      - `claude-3-opus-20240229` - Deprecated: Will reach end-of-life on January 5th, 2026. Please migrate to a newer model. Visit https://docs.anthropic.com/en/docs/resources/model-deprecations for more information.
      - `claude-3-haiku-20240307` - Our previous most fast and cost-effective

      - `"claude-opus-4-6"`

        Most intelligent model for building agents and coding

      - `"claude-sonnet-4-6"`

        Frontier intelligence at scale — built for coding, agents, and enterprise workflows

      - `"claude-opus-4-5-20251101"`

        Premium model combining maximum intelligence with practical performance

      - `"claude-opus-4-5"`

        Premium model combining maximum intelligence with practical performance

      - `"claude-3-7-sonnet-latest"`

        High-performance model with early extended thinking

      - `"claude-3-7-sonnet-20250219"`

        High-performance model with early extended thinking

      - `"claude-3-5-haiku-latest"`

        Fastest and most compact model for near-instant responsiveness

      - `"claude-3-5-haiku-20241022"`

        Our fastest model

      - `"claude-haiku-4-5"`

        Hybrid model, capable of near-instant responses and extended thinking

      - `"claude-haiku-4-5-20251001"`

        Hybrid model, capable of near-instant responses and extended thinking

      - `"claude-sonnet-4-20250514"`

        High-performance model with extended thinking

      - `"claude-sonnet-4-0"`

        High-performance model with extended thinking

      - `"claude-4-sonnet-20250514"`

        High-performance model with extended thinking

      - `"claude-sonnet-4-5"`

        Our best model for real-world agents and coding

      - `"claude-sonnet-4-5-20250929"`

        Our best model for real-world agents and coding

      - `"claude-opus-4-0"`

        Our most capable model

      - `"claude-opus-4-20250514"`

        Our most capable model

      - `"claude-4-opus-20250514"`

        Our most capable model

      - `"claude-opus-4-1-20250805"`

        Our most capable model

      - `"claude-3-opus-latest"`

        Excels at writing and complex tasks

      - `"claude-3-opus-20240229"`

        Excels at writing and complex tasks

      - `"claude-3-haiku-20240307"`

        Our previous most fast and cost-effective

    - `str`

  - `role: Literal["assistant"]`

    Conversational role of the generated message.

    This will always be `"assistant"`.

    - `"assistant"`

  - `stop_reason: Optional[StopReason]`

    The reason that we stopped.

    This may be one the following values:

    * `"end_turn"`: the model reached a natural stopping point
    * `"max_tokens"`: we exceeded the requested `max_tokens` or the model's maximum
    * `"stop_sequence"`: one of your provided custom `stop_sequences` was generated
    * `"tool_use"`: the model invoked one or more tools
    * `"pause_turn"`: we paused a long-running turn. You may provide the response back as-is in a subsequent request to let the model continue.
    * `"refusal"`: when streaming classifiers intervene to handle potential policy violations

    In non-streaming mode this value is always non-null. In streaming mode, it is null in the `message_start` event and non-null otherwise.

    - `"end_turn"`

    - `"max_tokens"`

    - `"stop_sequence"`

    - `"tool_use"`

    - `"pause_turn"`

    - `"refusal"`

  - `stop_sequence: Optional[str]`

    Which custom stop sequence was generated, if any.

    This value will be a non-null string if one of your custom stop sequences was generated.

  - `type: Literal["message"]`

    Object type.

    For Messages, this is always `"message"`.

    - `"message"`

  - `usage: Usage`

    Billing and rate-limit usage.

    Anthropic's API bills and rate-limits by token counts, as tokens represent the underlying cost to our systems.

    Under the hood, the API transforms requests into a format suitable for the model. The model's output then goes through a parsing stage before becoming an API response. As a result, the token counts in `usage` will not match one-to-one with the exact visible content of an API request or response.

    For example, `output_tokens` will be non-zero, even for an empty string response from Claude.

    Total input tokens in a request is the summation of `input_tokens`, `cache_creation_input_tokens`, and `cache_read_input_tokens`.

    - `cache_creation: Optional[CacheCreation]`

      Breakdown of cached tokens by TTL

      - `ephemeral_1h_input_tokens: int`

        The number of input tokens used to create the 1 hour cache entry.

      - `ephemeral_5m_input_tokens: int`

        The number of input tokens used to create the 5 minute cache entry.

    - `cache_creation_input_tokens: Optional[int]`

      The number of input tokens used to create the cache entry.

    - `cache_read_input_tokens: Optional[int]`

      The number of input tokens read from the cache.

    - `inference_geo: Optional[str]`

      The geographic region where inference was performed for this request.

    - `input_tokens: int`

      The number of input tokens which were used.

    - `output_tokens: int`

      The number of output tokens which were used.

    - `server_tool_use: Optional[ServerToolUsage]`

      The number of server tool requests.

      - `web_fetch_requests: int`

        The number of web fetch tool requests.

      - `web_search_requests: int`

        The number of web search tool requests.

    - `service_tier: Optional[Literal["standard", "priority", "batch"]]`

      If the request used the priority, standard, or batch tier.

      - `"standard"`

      - `"priority"`

      - `"batch"`

### Example

```python
import os
from anthropic import Anthropic

client = Anthropic(
    api_key=os.environ.get("ANTHROPIC_API_KEY"),  # This is the default and can be omitted
)
message = client.messages.create(
    max_tokens=1024,
    messages=[{
        "content": "Hello, world",
        "role": "user",
    }],
    model="claude-opus-4-6",
)
print(message.id)
```
