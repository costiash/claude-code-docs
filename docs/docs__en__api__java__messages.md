# Messages

## Create

`Message messages().create(MessageCreateParamsparams, RequestOptionsrequestOptions = RequestOptions.none())`

**post** `/v1/messages`

Send a structured list of input messages with text and/or image content, and the model will generate the next message in the conversation.

The Messages API can be used for either single queries or stateless multi-turn conversations.

Learn more about the Messages API in our [user guide](https://docs.claude.com/en/docs/initial-setup)

### Parameters

- `MessageCreateParams params`

  - `long maxTokens`

    The maximum number of tokens to generate before stopping.

    Note that our models may stop _before_ reaching this maximum. This parameter only specifies the absolute maximum number of tokens to generate.

    Different models have different maximum values for this parameter.  See [models](https://docs.claude.com/en/docs/models-overview) for details.

  - `List<MessageParam> messages`

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

    - `Content content`

      - `String`

      - `List<ContentBlockParam>`

        - `class TextBlockParam:`

          - `String text`

          - `JsonValue; type "text"constant`

            - `TEXT("text")`

          - `Optional<CacheControlEphemeral> cacheControl`

            Create a cache control breakpoint at this content block.

            - `JsonValue; type "ephemeral"constant`

              - `EPHEMERAL("ephemeral")`

            - `Optional<Ttl> ttl`

              The time-to-live for the cache control breakpoint.

              This may be one the following values:

              - `5m`: 5 minutes
              - `1h`: 1 hour

              Defaults to `5m`.

              - `TTL_5M("5m")`

              - `TTL_1H("1h")`

          - `Optional<List<TextCitationParam>> citations`

            - `class CitationCharLocationParam:`

              - `String citedText`

              - `long documentIndex`

              - `Optional<String> documentTitle`

              - `long endCharIndex`

              - `long startCharIndex`

              - `JsonValue; type "char_location"constant`

                - `CHAR_LOCATION("char_location")`

            - `class CitationPageLocationParam:`

              - `String citedText`

              - `long documentIndex`

              - `Optional<String> documentTitle`

              - `long endPageNumber`

              - `long startPageNumber`

              - `JsonValue; type "page_location"constant`

                - `PAGE_LOCATION("page_location")`

            - `class CitationContentBlockLocationParam:`

              - `String citedText`

              - `long documentIndex`

              - `Optional<String> documentTitle`

              - `long endBlockIndex`

              - `long startBlockIndex`

              - `JsonValue; type "content_block_location"constant`

                - `CONTENT_BLOCK_LOCATION("content_block_location")`

            - `class CitationWebSearchResultLocationParam:`

              - `String citedText`

              - `String encryptedIndex`

              - `Optional<String> title`

              - `JsonValue; type "web_search_result_location"constant`

                - `WEB_SEARCH_RESULT_LOCATION("web_search_result_location")`

              - `String url`

            - `class CitationSearchResultLocationParam:`

              - `String citedText`

              - `long endBlockIndex`

              - `long searchResultIndex`

              - `String source`

              - `long startBlockIndex`

              - `Optional<String> title`

              - `JsonValue; type "search_result_location"constant`

                - `SEARCH_RESULT_LOCATION("search_result_location")`

        - `class ImageBlockParam:`

          - `Source source`

            - `class Base64ImageSource:`

              - `String data`

              - `MediaType mediaType`

                - `IMAGE_JPEG("image/jpeg")`

                - `IMAGE_PNG("image/png")`

                - `IMAGE_GIF("image/gif")`

                - `IMAGE_WEBP("image/webp")`

              - `JsonValue; type "base64"constant`

                - `BASE64("base64")`

            - `class UrlImageSource:`

              - `JsonValue; type "url"constant`

                - `URL("url")`

              - `String url`

          - `JsonValue; type "image"constant`

            - `IMAGE("image")`

          - `Optional<CacheControlEphemeral> cacheControl`

            Create a cache control breakpoint at this content block.

            - `JsonValue; type "ephemeral"constant`

              - `EPHEMERAL("ephemeral")`

            - `Optional<Ttl> ttl`

              The time-to-live for the cache control breakpoint.

              This may be one the following values:

              - `5m`: 5 minutes
              - `1h`: 1 hour

              Defaults to `5m`.

              - `TTL_5M("5m")`

              - `TTL_1H("1h")`

        - `class DocumentBlockParam:`

          - `Source source`

            - `class Base64PdfSource:`

              - `String data`

              - `JsonValue; mediaType "application/pdf"constant`

                - `APPLICATION_PDF("application/pdf")`

              - `JsonValue; type "base64"constant`

                - `BASE64("base64")`

            - `class PlainTextSource:`

              - `String data`

              - `JsonValue; mediaType "text/plain"constant`

                - `TEXT_PLAIN("text/plain")`

              - `JsonValue; type "text"constant`

                - `TEXT("text")`

            - `class ContentBlockSource:`

              - `Content content`

                - `String`

                - `List<ContentBlockSourceContent>`

                  - `class TextBlockParam:`

                    - `String text`

                    - `JsonValue; type "text"constant`

                      - `TEXT("text")`

                    - `Optional<CacheControlEphemeral> cacheControl`

                      Create a cache control breakpoint at this content block.

                      - `JsonValue; type "ephemeral"constant`

                        - `EPHEMERAL("ephemeral")`

                      - `Optional<Ttl> ttl`

                        The time-to-live for the cache control breakpoint.

                        This may be one the following values:

                        - `5m`: 5 minutes
                        - `1h`: 1 hour

                        Defaults to `5m`.

                        - `TTL_5M("5m")`

                        - `TTL_1H("1h")`

                    - `Optional<List<TextCitationParam>> citations`

                      - `class CitationCharLocationParam:`

                        - `String citedText`

                        - `long documentIndex`

                        - `Optional<String> documentTitle`

                        - `long endCharIndex`

                        - `long startCharIndex`

                        - `JsonValue; type "char_location"constant`

                          - `CHAR_LOCATION("char_location")`

                      - `class CitationPageLocationParam:`

                        - `String citedText`

                        - `long documentIndex`

                        - `Optional<String> documentTitle`

                        - `long endPageNumber`

                        - `long startPageNumber`

                        - `JsonValue; type "page_location"constant`

                          - `PAGE_LOCATION("page_location")`

                      - `class CitationContentBlockLocationParam:`

                        - `String citedText`

                        - `long documentIndex`

                        - `Optional<String> documentTitle`

                        - `long endBlockIndex`

                        - `long startBlockIndex`

                        - `JsonValue; type "content_block_location"constant`

                          - `CONTENT_BLOCK_LOCATION("content_block_location")`

                      - `class CitationWebSearchResultLocationParam:`

                        - `String citedText`

                        - `String encryptedIndex`

                        - `Optional<String> title`

                        - `JsonValue; type "web_search_result_location"constant`

                          - `WEB_SEARCH_RESULT_LOCATION("web_search_result_location")`

                        - `String url`

                      - `class CitationSearchResultLocationParam:`

                        - `String citedText`

                        - `long endBlockIndex`

                        - `long searchResultIndex`

                        - `String source`

                        - `long startBlockIndex`

                        - `Optional<String> title`

                        - `JsonValue; type "search_result_location"constant`

                          - `SEARCH_RESULT_LOCATION("search_result_location")`

                  - `class ImageBlockParam:`

                    - `Source source`

                      - `class Base64ImageSource:`

                        - `String data`

                        - `MediaType mediaType`

                          - `IMAGE_JPEG("image/jpeg")`

                          - `IMAGE_PNG("image/png")`

                          - `IMAGE_GIF("image/gif")`

                          - `IMAGE_WEBP("image/webp")`

                        - `JsonValue; type "base64"constant`

                          - `BASE64("base64")`

                      - `class UrlImageSource:`

                        - `JsonValue; type "url"constant`

                          - `URL("url")`

                        - `String url`

                    - `JsonValue; type "image"constant`

                      - `IMAGE("image")`

                    - `Optional<CacheControlEphemeral> cacheControl`

                      Create a cache control breakpoint at this content block.

                      - `JsonValue; type "ephemeral"constant`

                        - `EPHEMERAL("ephemeral")`

                      - `Optional<Ttl> ttl`

                        The time-to-live for the cache control breakpoint.

                        This may be one the following values:

                        - `5m`: 5 minutes
                        - `1h`: 1 hour

                        Defaults to `5m`.

                        - `TTL_5M("5m")`

                        - `TTL_1H("1h")`

              - `JsonValue; type "content"constant`

                - `CONTENT("content")`

            - `class UrlPdfSource:`

              - `JsonValue; type "url"constant`

                - `URL("url")`

              - `String url`

          - `JsonValue; type "document"constant`

            - `DOCUMENT("document")`

          - `Optional<CacheControlEphemeral> cacheControl`

            Create a cache control breakpoint at this content block.

            - `JsonValue; type "ephemeral"constant`

              - `EPHEMERAL("ephemeral")`

            - `Optional<Ttl> ttl`

              The time-to-live for the cache control breakpoint.

              This may be one the following values:

              - `5m`: 5 minutes
              - `1h`: 1 hour

              Defaults to `5m`.

              - `TTL_5M("5m")`

              - `TTL_1H("1h")`

          - `Optional<CitationsConfigParam> citations`

            - `Optional<Boolean> enabled`

          - `Optional<String> context`

          - `Optional<String> title`

        - `class SearchResultBlockParam:`

          - `List<TextBlockParam> content`

            - `String text`

            - `JsonValue; type "text"constant`

              - `TEXT("text")`

            - `Optional<CacheControlEphemeral> cacheControl`

              Create a cache control breakpoint at this content block.

              - `JsonValue; type "ephemeral"constant`

                - `EPHEMERAL("ephemeral")`

              - `Optional<Ttl> ttl`

                The time-to-live for the cache control breakpoint.

                This may be one the following values:

                - `5m`: 5 minutes
                - `1h`: 1 hour

                Defaults to `5m`.

                - `TTL_5M("5m")`

                - `TTL_1H("1h")`

            - `Optional<List<TextCitationParam>> citations`

              - `class CitationCharLocationParam:`

                - `String citedText`

                - `long documentIndex`

                - `Optional<String> documentTitle`

                - `long endCharIndex`

                - `long startCharIndex`

                - `JsonValue; type "char_location"constant`

                  - `CHAR_LOCATION("char_location")`

              - `class CitationPageLocationParam:`

                - `String citedText`

                - `long documentIndex`

                - `Optional<String> documentTitle`

                - `long endPageNumber`

                - `long startPageNumber`

                - `JsonValue; type "page_location"constant`

                  - `PAGE_LOCATION("page_location")`

              - `class CitationContentBlockLocationParam:`

                - `String citedText`

                - `long documentIndex`

                - `Optional<String> documentTitle`

                - `long endBlockIndex`

                - `long startBlockIndex`

                - `JsonValue; type "content_block_location"constant`

                  - `CONTENT_BLOCK_LOCATION("content_block_location")`

              - `class CitationWebSearchResultLocationParam:`

                - `String citedText`

                - `String encryptedIndex`

                - `Optional<String> title`

                - `JsonValue; type "web_search_result_location"constant`

                  - `WEB_SEARCH_RESULT_LOCATION("web_search_result_location")`

                - `String url`

              - `class CitationSearchResultLocationParam:`

                - `String citedText`

                - `long endBlockIndex`

                - `long searchResultIndex`

                - `String source`

                - `long startBlockIndex`

                - `Optional<String> title`

                - `JsonValue; type "search_result_location"constant`

                  - `SEARCH_RESULT_LOCATION("search_result_location")`

          - `String source`

          - `String title`

          - `JsonValue; type "search_result"constant`

            - `SEARCH_RESULT("search_result")`

          - `Optional<CacheControlEphemeral> cacheControl`

            Create a cache control breakpoint at this content block.

            - `JsonValue; type "ephemeral"constant`

              - `EPHEMERAL("ephemeral")`

            - `Optional<Ttl> ttl`

              The time-to-live for the cache control breakpoint.

              This may be one the following values:

              - `5m`: 5 minutes
              - `1h`: 1 hour

              Defaults to `5m`.

              - `TTL_5M("5m")`

              - `TTL_1H("1h")`

          - `Optional<CitationsConfigParam> citations`

            - `Optional<Boolean> enabled`

        - `class ThinkingBlockParam:`

          - `String signature`

          - `String thinking`

          - `JsonValue; type "thinking"constant`

            - `THINKING("thinking")`

        - `class RedactedThinkingBlockParam:`

          - `String data`

          - `JsonValue; type "redacted_thinking"constant`

            - `REDACTED_THINKING("redacted_thinking")`

        - `class ToolUseBlockParam:`

          - `String id`

          - `Input input`

          - `String name`

          - `JsonValue; type "tool_use"constant`

            - `TOOL_USE("tool_use")`

          - `Optional<CacheControlEphemeral> cacheControl`

            Create a cache control breakpoint at this content block.

            - `JsonValue; type "ephemeral"constant`

              - `EPHEMERAL("ephemeral")`

            - `Optional<Ttl> ttl`

              The time-to-live for the cache control breakpoint.

              This may be one the following values:

              - `5m`: 5 minutes
              - `1h`: 1 hour

              Defaults to `5m`.

              - `TTL_5M("5m")`

              - `TTL_1H("1h")`

          - `Optional<Caller> caller`

            Tool invocation directly from the model.

            - `class DirectCaller:`

              Tool invocation directly from the model.

              - `JsonValue; type "direct"constant`

                - `DIRECT("direct")`

            - `class ServerToolCaller:`

              Tool invocation generated by a server-side tool.

              - `String toolId`

              - `JsonValue; type "code_execution_20250825"constant`

                - `CODE_EXECUTION_20250825("code_execution_20250825")`

            - `class ServerToolCaller20260120:`

              - `String toolId`

              - `JsonValue; type "code_execution_20260120"constant`

                - `CODE_EXECUTION_20260120("code_execution_20260120")`

        - `class ToolResultBlockParam:`

          - `String toolUseId`

          - `JsonValue; type "tool_result"constant`

            - `TOOL_RESULT("tool_result")`

          - `Optional<CacheControlEphemeral> cacheControl`

            Create a cache control breakpoint at this content block.

            - `JsonValue; type "ephemeral"constant`

              - `EPHEMERAL("ephemeral")`

            - `Optional<Ttl> ttl`

              The time-to-live for the cache control breakpoint.

              This may be one the following values:

              - `5m`: 5 minutes
              - `1h`: 1 hour

              Defaults to `5m`.

              - `TTL_5M("5m")`

              - `TTL_1H("1h")`

          - `Optional<Content> content`

            - `String`

            - `List<Block>`

              - `class TextBlockParam:`

                - `String text`

                - `JsonValue; type "text"constant`

                  - `TEXT("text")`

                - `Optional<CacheControlEphemeral> cacheControl`

                  Create a cache control breakpoint at this content block.

                  - `JsonValue; type "ephemeral"constant`

                    - `EPHEMERAL("ephemeral")`

                  - `Optional<Ttl> ttl`

                    The time-to-live for the cache control breakpoint.

                    This may be one the following values:

                    - `5m`: 5 minutes
                    - `1h`: 1 hour

                    Defaults to `5m`.

                    - `TTL_5M("5m")`

                    - `TTL_1H("1h")`

                - `Optional<List<TextCitationParam>> citations`

                  - `class CitationCharLocationParam:`

                    - `String citedText`

                    - `long documentIndex`

                    - `Optional<String> documentTitle`

                    - `long endCharIndex`

                    - `long startCharIndex`

                    - `JsonValue; type "char_location"constant`

                      - `CHAR_LOCATION("char_location")`

                  - `class CitationPageLocationParam:`

                    - `String citedText`

                    - `long documentIndex`

                    - `Optional<String> documentTitle`

                    - `long endPageNumber`

                    - `long startPageNumber`

                    - `JsonValue; type "page_location"constant`

                      - `PAGE_LOCATION("page_location")`

                  - `class CitationContentBlockLocationParam:`

                    - `String citedText`

                    - `long documentIndex`

                    - `Optional<String> documentTitle`

                    - `long endBlockIndex`

                    - `long startBlockIndex`

                    - `JsonValue; type "content_block_location"constant`

                      - `CONTENT_BLOCK_LOCATION("content_block_location")`

                  - `class CitationWebSearchResultLocationParam:`

                    - `String citedText`

                    - `String encryptedIndex`

                    - `Optional<String> title`

                    - `JsonValue; type "web_search_result_location"constant`

                      - `WEB_SEARCH_RESULT_LOCATION("web_search_result_location")`

                    - `String url`

                  - `class CitationSearchResultLocationParam:`

                    - `String citedText`

                    - `long endBlockIndex`

                    - `long searchResultIndex`

                    - `String source`

                    - `long startBlockIndex`

                    - `Optional<String> title`

                    - `JsonValue; type "search_result_location"constant`

                      - `SEARCH_RESULT_LOCATION("search_result_location")`

              - `class ImageBlockParam:`

                - `Source source`

                  - `class Base64ImageSource:`

                    - `String data`

                    - `MediaType mediaType`

                      - `IMAGE_JPEG("image/jpeg")`

                      - `IMAGE_PNG("image/png")`

                      - `IMAGE_GIF("image/gif")`

                      - `IMAGE_WEBP("image/webp")`

                    - `JsonValue; type "base64"constant`

                      - `BASE64("base64")`

                  - `class UrlImageSource:`

                    - `JsonValue; type "url"constant`

                      - `URL("url")`

                    - `String url`

                - `JsonValue; type "image"constant`

                  - `IMAGE("image")`

                - `Optional<CacheControlEphemeral> cacheControl`

                  Create a cache control breakpoint at this content block.

                  - `JsonValue; type "ephemeral"constant`

                    - `EPHEMERAL("ephemeral")`

                  - `Optional<Ttl> ttl`

                    The time-to-live for the cache control breakpoint.

                    This may be one the following values:

                    - `5m`: 5 minutes
                    - `1h`: 1 hour

                    Defaults to `5m`.

                    - `TTL_5M("5m")`

                    - `TTL_1H("1h")`

              - `class SearchResultBlockParam:`

                - `List<TextBlockParam> content`

                  - `String text`

                  - `JsonValue; type "text"constant`

                    - `TEXT("text")`

                  - `Optional<CacheControlEphemeral> cacheControl`

                    Create a cache control breakpoint at this content block.

                    - `JsonValue; type "ephemeral"constant`

                      - `EPHEMERAL("ephemeral")`

                    - `Optional<Ttl> ttl`

                      The time-to-live for the cache control breakpoint.

                      This may be one the following values:

                      - `5m`: 5 minutes
                      - `1h`: 1 hour

                      Defaults to `5m`.

                      - `TTL_5M("5m")`

                      - `TTL_1H("1h")`

                  - `Optional<List<TextCitationParam>> citations`

                    - `class CitationCharLocationParam:`

                      - `String citedText`

                      - `long documentIndex`

                      - `Optional<String> documentTitle`

                      - `long endCharIndex`

                      - `long startCharIndex`

                      - `JsonValue; type "char_location"constant`

                        - `CHAR_LOCATION("char_location")`

                    - `class CitationPageLocationParam:`

                      - `String citedText`

                      - `long documentIndex`

                      - `Optional<String> documentTitle`

                      - `long endPageNumber`

                      - `long startPageNumber`

                      - `JsonValue; type "page_location"constant`

                        - `PAGE_LOCATION("page_location")`

                    - `class CitationContentBlockLocationParam:`

                      - `String citedText`

                      - `long documentIndex`

                      - `Optional<String> documentTitle`

                      - `long endBlockIndex`

                      - `long startBlockIndex`

                      - `JsonValue; type "content_block_location"constant`

                        - `CONTENT_BLOCK_LOCATION("content_block_location")`

                    - `class CitationWebSearchResultLocationParam:`

                      - `String citedText`

                      - `String encryptedIndex`

                      - `Optional<String> title`

                      - `JsonValue; type "web_search_result_location"constant`

                        - `WEB_SEARCH_RESULT_LOCATION("web_search_result_location")`

                      - `String url`

                    - `class CitationSearchResultLocationParam:`

                      - `String citedText`

                      - `long endBlockIndex`

                      - `long searchResultIndex`

                      - `String source`

                      - `long startBlockIndex`

                      - `Optional<String> title`

                      - `JsonValue; type "search_result_location"constant`

                        - `SEARCH_RESULT_LOCATION("search_result_location")`

                - `String source`

                - `String title`

                - `JsonValue; type "search_result"constant`

                  - `SEARCH_RESULT("search_result")`

                - `Optional<CacheControlEphemeral> cacheControl`

                  Create a cache control breakpoint at this content block.

                  - `JsonValue; type "ephemeral"constant`

                    - `EPHEMERAL("ephemeral")`

                  - `Optional<Ttl> ttl`

                    The time-to-live for the cache control breakpoint.

                    This may be one the following values:

                    - `5m`: 5 minutes
                    - `1h`: 1 hour

                    Defaults to `5m`.

                    - `TTL_5M("5m")`

                    - `TTL_1H("1h")`

                - `Optional<CitationsConfigParam> citations`

                  - `Optional<Boolean> enabled`

              - `class DocumentBlockParam:`

                - `Source source`

                  - `class Base64PdfSource:`

                    - `String data`

                    - `JsonValue; mediaType "application/pdf"constant`

                      - `APPLICATION_PDF("application/pdf")`

                    - `JsonValue; type "base64"constant`

                      - `BASE64("base64")`

                  - `class PlainTextSource:`

                    - `String data`

                    - `JsonValue; mediaType "text/plain"constant`

                      - `TEXT_PLAIN("text/plain")`

                    - `JsonValue; type "text"constant`

                      - `TEXT("text")`

                  - `class ContentBlockSource:`

                    - `Content content`

                      - `String`

                      - `List<ContentBlockSourceContent>`

                        - `class TextBlockParam:`

                          - `String text`

                          - `JsonValue; type "text"constant`

                            - `TEXT("text")`

                          - `Optional<CacheControlEphemeral> cacheControl`

                            Create a cache control breakpoint at this content block.

                            - `JsonValue; type "ephemeral"constant`

                              - `EPHEMERAL("ephemeral")`

                            - `Optional<Ttl> ttl`

                              The time-to-live for the cache control breakpoint.

                              This may be one the following values:

                              - `5m`: 5 minutes
                              - `1h`: 1 hour

                              Defaults to `5m`.

                              - `TTL_5M("5m")`

                              - `TTL_1H("1h")`

                          - `Optional<List<TextCitationParam>> citations`

                            - `class CitationCharLocationParam:`

                              - `String citedText`

                              - `long documentIndex`

                              - `Optional<String> documentTitle`

                              - `long endCharIndex`

                              - `long startCharIndex`

                              - `JsonValue; type "char_location"constant`

                                - `CHAR_LOCATION("char_location")`

                            - `class CitationPageLocationParam:`

                              - `String citedText`

                              - `long documentIndex`

                              - `Optional<String> documentTitle`

                              - `long endPageNumber`

                              - `long startPageNumber`

                              - `JsonValue; type "page_location"constant`

                                - `PAGE_LOCATION("page_location")`

                            - `class CitationContentBlockLocationParam:`

                              - `String citedText`

                              - `long documentIndex`

                              - `Optional<String> documentTitle`

                              - `long endBlockIndex`

                              - `long startBlockIndex`

                              - `JsonValue; type "content_block_location"constant`

                                - `CONTENT_BLOCK_LOCATION("content_block_location")`

                            - `class CitationWebSearchResultLocationParam:`

                              - `String citedText`

                              - `String encryptedIndex`

                              - `Optional<String> title`

                              - `JsonValue; type "web_search_result_location"constant`

                                - `WEB_SEARCH_RESULT_LOCATION("web_search_result_location")`

                              - `String url`

                            - `class CitationSearchResultLocationParam:`

                              - `String citedText`

                              - `long endBlockIndex`

                              - `long searchResultIndex`

                              - `String source`

                              - `long startBlockIndex`

                              - `Optional<String> title`

                              - `JsonValue; type "search_result_location"constant`

                                - `SEARCH_RESULT_LOCATION("search_result_location")`

                        - `class ImageBlockParam:`

                          - `Source source`

                            - `class Base64ImageSource:`

                              - `String data`

                              - `MediaType mediaType`

                                - `IMAGE_JPEG("image/jpeg")`

                                - `IMAGE_PNG("image/png")`

                                - `IMAGE_GIF("image/gif")`

                                - `IMAGE_WEBP("image/webp")`

                              - `JsonValue; type "base64"constant`

                                - `BASE64("base64")`

                            - `class UrlImageSource:`

                              - `JsonValue; type "url"constant`

                                - `URL("url")`

                              - `String url`

                          - `JsonValue; type "image"constant`

                            - `IMAGE("image")`

                          - `Optional<CacheControlEphemeral> cacheControl`

                            Create a cache control breakpoint at this content block.

                            - `JsonValue; type "ephemeral"constant`

                              - `EPHEMERAL("ephemeral")`

                            - `Optional<Ttl> ttl`

                              The time-to-live for the cache control breakpoint.

                              This may be one the following values:

                              - `5m`: 5 minutes
                              - `1h`: 1 hour

                              Defaults to `5m`.

                              - `TTL_5M("5m")`

                              - `TTL_1H("1h")`

                    - `JsonValue; type "content"constant`

                      - `CONTENT("content")`

                  - `class UrlPdfSource:`

                    - `JsonValue; type "url"constant`

                      - `URL("url")`

                    - `String url`

                - `JsonValue; type "document"constant`

                  - `DOCUMENT("document")`

                - `Optional<CacheControlEphemeral> cacheControl`

                  Create a cache control breakpoint at this content block.

                  - `JsonValue; type "ephemeral"constant`

                    - `EPHEMERAL("ephemeral")`

                  - `Optional<Ttl> ttl`

                    The time-to-live for the cache control breakpoint.

                    This may be one the following values:

                    - `5m`: 5 minutes
                    - `1h`: 1 hour

                    Defaults to `5m`.

                    - `TTL_5M("5m")`

                    - `TTL_1H("1h")`

                - `Optional<CitationsConfigParam> citations`

                  - `Optional<Boolean> enabled`

                - `Optional<String> context`

                - `Optional<String> title`

              - `class ToolReferenceBlockParam:`

                Tool reference block that can be included in tool_result content.

                - `String toolName`

                - `JsonValue; type "tool_reference"constant`

                  - `TOOL_REFERENCE("tool_reference")`

                - `Optional<CacheControlEphemeral> cacheControl`

                  Create a cache control breakpoint at this content block.

                  - `JsonValue; type "ephemeral"constant`

                    - `EPHEMERAL("ephemeral")`

                  - `Optional<Ttl> ttl`

                    The time-to-live for the cache control breakpoint.

                    This may be one the following values:

                    - `5m`: 5 minutes
                    - `1h`: 1 hour

                    Defaults to `5m`.

                    - `TTL_5M("5m")`

                    - `TTL_1H("1h")`

          - `Optional<Boolean> isError`

        - `class ServerToolUseBlockParam:`

          - `String id`

          - `Input input`

          - `Name name`

            - `WEB_SEARCH("web_search")`

            - `WEB_FETCH("web_fetch")`

            - `CODE_EXECUTION("code_execution")`

            - `BASH_CODE_EXECUTION("bash_code_execution")`

            - `TEXT_EDITOR_CODE_EXECUTION("text_editor_code_execution")`

            - `TOOL_SEARCH_TOOL_REGEX("tool_search_tool_regex")`

            - `TOOL_SEARCH_TOOL_BM25("tool_search_tool_bm25")`

          - `JsonValue; type "server_tool_use"constant`

            - `SERVER_TOOL_USE("server_tool_use")`

          - `Optional<CacheControlEphemeral> cacheControl`

            Create a cache control breakpoint at this content block.

            - `JsonValue; type "ephemeral"constant`

              - `EPHEMERAL("ephemeral")`

            - `Optional<Ttl> ttl`

              The time-to-live for the cache control breakpoint.

              This may be one the following values:

              - `5m`: 5 minutes
              - `1h`: 1 hour

              Defaults to `5m`.

              - `TTL_5M("5m")`

              - `TTL_1H("1h")`

          - `Optional<Caller> caller`

            Tool invocation directly from the model.

            - `class DirectCaller:`

              Tool invocation directly from the model.

              - `JsonValue; type "direct"constant`

                - `DIRECT("direct")`

            - `class ServerToolCaller:`

              Tool invocation generated by a server-side tool.

              - `String toolId`

              - `JsonValue; type "code_execution_20250825"constant`

                - `CODE_EXECUTION_20250825("code_execution_20250825")`

            - `class ServerToolCaller20260120:`

              - `String toolId`

              - `JsonValue; type "code_execution_20260120"constant`

                - `CODE_EXECUTION_20260120("code_execution_20260120")`

        - `class WebSearchToolResultBlockParam:`

          - `WebSearchToolResultBlockParamContent content`

            - `List<WebSearchResultBlockParam>`

              - `String encryptedContent`

              - `String title`

              - `JsonValue; type "web_search_result"constant`

                - `WEB_SEARCH_RESULT("web_search_result")`

              - `String url`

              - `Optional<String> pageAge`

            - `class WebSearchToolRequestError:`

              - `WebSearchToolResultErrorCode errorCode`

                - `INVALID_TOOL_INPUT("invalid_tool_input")`

                - `UNAVAILABLE("unavailable")`

                - `MAX_USES_EXCEEDED("max_uses_exceeded")`

                - `TOO_MANY_REQUESTS("too_many_requests")`

                - `QUERY_TOO_LONG("query_too_long")`

                - `REQUEST_TOO_LARGE("request_too_large")`

              - `JsonValue; type "web_search_tool_result_error"constant`

                - `WEB_SEARCH_TOOL_RESULT_ERROR("web_search_tool_result_error")`

          - `String toolUseId`

          - `JsonValue; type "web_search_tool_result"constant`

            - `WEB_SEARCH_TOOL_RESULT("web_search_tool_result")`

          - `Optional<CacheControlEphemeral> cacheControl`

            Create a cache control breakpoint at this content block.

            - `JsonValue; type "ephemeral"constant`

              - `EPHEMERAL("ephemeral")`

            - `Optional<Ttl> ttl`

              The time-to-live for the cache control breakpoint.

              This may be one the following values:

              - `5m`: 5 minutes
              - `1h`: 1 hour

              Defaults to `5m`.

              - `TTL_5M("5m")`

              - `TTL_1H("1h")`

          - `Optional<Caller> caller`

            Tool invocation directly from the model.

            - `class DirectCaller:`

              Tool invocation directly from the model.

              - `JsonValue; type "direct"constant`

                - `DIRECT("direct")`

            - `class ServerToolCaller:`

              Tool invocation generated by a server-side tool.

              - `String toolId`

              - `JsonValue; type "code_execution_20250825"constant`

                - `CODE_EXECUTION_20250825("code_execution_20250825")`

            - `class ServerToolCaller20260120:`

              - `String toolId`

              - `JsonValue; type "code_execution_20260120"constant`

                - `CODE_EXECUTION_20260120("code_execution_20260120")`

        - `class WebFetchToolResultBlockParam:`

          - `Content content`

            - `class WebFetchToolResultErrorBlockParam:`

              - `WebFetchToolResultErrorCode errorCode`

                - `INVALID_TOOL_INPUT("invalid_tool_input")`

                - `URL_TOO_LONG("url_too_long")`

                - `URL_NOT_ALLOWED("url_not_allowed")`

                - `URL_NOT_ACCESSIBLE("url_not_accessible")`

                - `UNSUPPORTED_CONTENT_TYPE("unsupported_content_type")`

                - `TOO_MANY_REQUESTS("too_many_requests")`

                - `MAX_USES_EXCEEDED("max_uses_exceeded")`

                - `UNAVAILABLE("unavailable")`

              - `JsonValue; type "web_fetch_tool_result_error"constant`

                - `WEB_FETCH_TOOL_RESULT_ERROR("web_fetch_tool_result_error")`

            - `class WebFetchBlockParam:`

              - `DocumentBlockParam content`

                - `Source source`

                  - `class Base64PdfSource:`

                    - `String data`

                    - `JsonValue; mediaType "application/pdf"constant`

                      - `APPLICATION_PDF("application/pdf")`

                    - `JsonValue; type "base64"constant`

                      - `BASE64("base64")`

                  - `class PlainTextSource:`

                    - `String data`

                    - `JsonValue; mediaType "text/plain"constant`

                      - `TEXT_PLAIN("text/plain")`

                    - `JsonValue; type "text"constant`

                      - `TEXT("text")`

                  - `class ContentBlockSource:`

                    - `Content content`

                      - `String`

                      - `List<ContentBlockSourceContent>`

                        - `class TextBlockParam:`

                          - `String text`

                          - `JsonValue; type "text"constant`

                            - `TEXT("text")`

                          - `Optional<CacheControlEphemeral> cacheControl`

                            Create a cache control breakpoint at this content block.

                            - `JsonValue; type "ephemeral"constant`

                              - `EPHEMERAL("ephemeral")`

                            - `Optional<Ttl> ttl`

                              The time-to-live for the cache control breakpoint.

                              This may be one the following values:

                              - `5m`: 5 minutes
                              - `1h`: 1 hour

                              Defaults to `5m`.

                              - `TTL_5M("5m")`

                              - `TTL_1H("1h")`

                          - `Optional<List<TextCitationParam>> citations`

                            - `class CitationCharLocationParam:`

                              - `String citedText`

                              - `long documentIndex`

                              - `Optional<String> documentTitle`

                              - `long endCharIndex`

                              - `long startCharIndex`

                              - `JsonValue; type "char_location"constant`

                                - `CHAR_LOCATION("char_location")`

                            - `class CitationPageLocationParam:`

                              - `String citedText`

                              - `long documentIndex`

                              - `Optional<String> documentTitle`

                              - `long endPageNumber`

                              - `long startPageNumber`

                              - `JsonValue; type "page_location"constant`

                                - `PAGE_LOCATION("page_location")`

                            - `class CitationContentBlockLocationParam:`

                              - `String citedText`

                              - `long documentIndex`

                              - `Optional<String> documentTitle`

                              - `long endBlockIndex`

                              - `long startBlockIndex`

                              - `JsonValue; type "content_block_location"constant`

                                - `CONTENT_BLOCK_LOCATION("content_block_location")`

                            - `class CitationWebSearchResultLocationParam:`

                              - `String citedText`

                              - `String encryptedIndex`

                              - `Optional<String> title`

                              - `JsonValue; type "web_search_result_location"constant`

                                - `WEB_SEARCH_RESULT_LOCATION("web_search_result_location")`

                              - `String url`

                            - `class CitationSearchResultLocationParam:`

                              - `String citedText`

                              - `long endBlockIndex`

                              - `long searchResultIndex`

                              - `String source`

                              - `long startBlockIndex`

                              - `Optional<String> title`

                              - `JsonValue; type "search_result_location"constant`

                                - `SEARCH_RESULT_LOCATION("search_result_location")`

                        - `class ImageBlockParam:`

                          - `Source source`

                            - `class Base64ImageSource:`

                              - `String data`

                              - `MediaType mediaType`

                                - `IMAGE_JPEG("image/jpeg")`

                                - `IMAGE_PNG("image/png")`

                                - `IMAGE_GIF("image/gif")`

                                - `IMAGE_WEBP("image/webp")`

                              - `JsonValue; type "base64"constant`

                                - `BASE64("base64")`

                            - `class UrlImageSource:`

                              - `JsonValue; type "url"constant`

                                - `URL("url")`

                              - `String url`

                          - `JsonValue; type "image"constant`

                            - `IMAGE("image")`

                          - `Optional<CacheControlEphemeral> cacheControl`

                            Create a cache control breakpoint at this content block.

                            - `JsonValue; type "ephemeral"constant`

                              - `EPHEMERAL("ephemeral")`

                            - `Optional<Ttl> ttl`

                              The time-to-live for the cache control breakpoint.

                              This may be one the following values:

                              - `5m`: 5 minutes
                              - `1h`: 1 hour

                              Defaults to `5m`.

                              - `TTL_5M("5m")`

                              - `TTL_1H("1h")`

                    - `JsonValue; type "content"constant`

                      - `CONTENT("content")`

                  - `class UrlPdfSource:`

                    - `JsonValue; type "url"constant`

                      - `URL("url")`

                    - `String url`

                - `JsonValue; type "document"constant`

                  - `DOCUMENT("document")`

                - `Optional<CacheControlEphemeral> cacheControl`

                  Create a cache control breakpoint at this content block.

                  - `JsonValue; type "ephemeral"constant`

                    - `EPHEMERAL("ephemeral")`

                  - `Optional<Ttl> ttl`

                    The time-to-live for the cache control breakpoint.

                    This may be one the following values:

                    - `5m`: 5 minutes
                    - `1h`: 1 hour

                    Defaults to `5m`.

                    - `TTL_5M("5m")`

                    - `TTL_1H("1h")`

                - `Optional<CitationsConfigParam> citations`

                  - `Optional<Boolean> enabled`

                - `Optional<String> context`

                - `Optional<String> title`

              - `JsonValue; type "web_fetch_result"constant`

                - `WEB_FETCH_RESULT("web_fetch_result")`

              - `String url`

                Fetched content URL

              - `Optional<String> retrievedAt`

                ISO 8601 timestamp when the content was retrieved

          - `String toolUseId`

          - `JsonValue; type "web_fetch_tool_result"constant`

            - `WEB_FETCH_TOOL_RESULT("web_fetch_tool_result")`

          - `Optional<CacheControlEphemeral> cacheControl`

            Create a cache control breakpoint at this content block.

            - `JsonValue; type "ephemeral"constant`

              - `EPHEMERAL("ephemeral")`

            - `Optional<Ttl> ttl`

              The time-to-live for the cache control breakpoint.

              This may be one the following values:

              - `5m`: 5 minutes
              - `1h`: 1 hour

              Defaults to `5m`.

              - `TTL_5M("5m")`

              - `TTL_1H("1h")`

          - `Optional<Caller> caller`

            Tool invocation directly from the model.

            - `class DirectCaller:`

              Tool invocation directly from the model.

              - `JsonValue; type "direct"constant`

                - `DIRECT("direct")`

            - `class ServerToolCaller:`

              Tool invocation generated by a server-side tool.

              - `String toolId`

              - `JsonValue; type "code_execution_20250825"constant`

                - `CODE_EXECUTION_20250825("code_execution_20250825")`

            - `class ServerToolCaller20260120:`

              - `String toolId`

              - `JsonValue; type "code_execution_20260120"constant`

                - `CODE_EXECUTION_20260120("code_execution_20260120")`

        - `class CodeExecutionToolResultBlockParam:`

          - `CodeExecutionToolResultBlockParamContent content`

            Code execution result with encrypted stdout for PFC + web_search results.

            - `class CodeExecutionToolResultErrorParam:`

              - `CodeExecutionToolResultErrorCode errorCode`

                - `INVALID_TOOL_INPUT("invalid_tool_input")`

                - `UNAVAILABLE("unavailable")`

                - `TOO_MANY_REQUESTS("too_many_requests")`

                - `EXECUTION_TIME_EXCEEDED("execution_time_exceeded")`

              - `JsonValue; type "code_execution_tool_result_error"constant`

                - `CODE_EXECUTION_TOOL_RESULT_ERROR("code_execution_tool_result_error")`

            - `class CodeExecutionResultBlockParam:`

              - `List<CodeExecutionOutputBlockParam> content`

                - `String fileId`

                - `JsonValue; type "code_execution_output"constant`

                  - `CODE_EXECUTION_OUTPUT("code_execution_output")`

              - `long returnCode`

              - `String stderr`

              - `String stdout`

              - `JsonValue; type "code_execution_result"constant`

                - `CODE_EXECUTION_RESULT("code_execution_result")`

            - `class EncryptedCodeExecutionResultBlockParam:`

              Code execution result with encrypted stdout for PFC + web_search results.

              - `List<CodeExecutionOutputBlockParam> content`

                - `String fileId`

                - `JsonValue; type "code_execution_output"constant`

                  - `CODE_EXECUTION_OUTPUT("code_execution_output")`

              - `String encryptedStdout`

              - `long returnCode`

              - `String stderr`

              - `JsonValue; type "encrypted_code_execution_result"constant`

                - `ENCRYPTED_CODE_EXECUTION_RESULT("encrypted_code_execution_result")`

          - `String toolUseId`

          - `JsonValue; type "code_execution_tool_result"constant`

            - `CODE_EXECUTION_TOOL_RESULT("code_execution_tool_result")`

          - `Optional<CacheControlEphemeral> cacheControl`

            Create a cache control breakpoint at this content block.

            - `JsonValue; type "ephemeral"constant`

              - `EPHEMERAL("ephemeral")`

            - `Optional<Ttl> ttl`

              The time-to-live for the cache control breakpoint.

              This may be one the following values:

              - `5m`: 5 minutes
              - `1h`: 1 hour

              Defaults to `5m`.

              - `TTL_5M("5m")`

              - `TTL_1H("1h")`

        - `class BashCodeExecutionToolResultBlockParam:`

          - `Content content`

            - `class BashCodeExecutionToolResultErrorParam:`

              - `BashCodeExecutionToolResultErrorCode errorCode`

                - `INVALID_TOOL_INPUT("invalid_tool_input")`

                - `UNAVAILABLE("unavailable")`

                - `TOO_MANY_REQUESTS("too_many_requests")`

                - `EXECUTION_TIME_EXCEEDED("execution_time_exceeded")`

                - `OUTPUT_FILE_TOO_LARGE("output_file_too_large")`

              - `JsonValue; type "bash_code_execution_tool_result_error"constant`

                - `BASH_CODE_EXECUTION_TOOL_RESULT_ERROR("bash_code_execution_tool_result_error")`

            - `class BashCodeExecutionResultBlockParam:`

              - `List<BashCodeExecutionOutputBlockParam> content`

                - `String fileId`

                - `JsonValue; type "bash_code_execution_output"constant`

                  - `BASH_CODE_EXECUTION_OUTPUT("bash_code_execution_output")`

              - `long returnCode`

              - `String stderr`

              - `String stdout`

              - `JsonValue; type "bash_code_execution_result"constant`

                - `BASH_CODE_EXECUTION_RESULT("bash_code_execution_result")`

          - `String toolUseId`

          - `JsonValue; type "bash_code_execution_tool_result"constant`

            - `BASH_CODE_EXECUTION_TOOL_RESULT("bash_code_execution_tool_result")`

          - `Optional<CacheControlEphemeral> cacheControl`

            Create a cache control breakpoint at this content block.

            - `JsonValue; type "ephemeral"constant`

              - `EPHEMERAL("ephemeral")`

            - `Optional<Ttl> ttl`

              The time-to-live for the cache control breakpoint.

              This may be one the following values:

              - `5m`: 5 minutes
              - `1h`: 1 hour

              Defaults to `5m`.

              - `TTL_5M("5m")`

              - `TTL_1H("1h")`

        - `class TextEditorCodeExecutionToolResultBlockParam:`

          - `Content content`

            - `class TextEditorCodeExecutionToolResultErrorParam:`

              - `TextEditorCodeExecutionToolResultErrorCode errorCode`

                - `INVALID_TOOL_INPUT("invalid_tool_input")`

                - `UNAVAILABLE("unavailable")`

                - `TOO_MANY_REQUESTS("too_many_requests")`

                - `EXECUTION_TIME_EXCEEDED("execution_time_exceeded")`

                - `FILE_NOT_FOUND("file_not_found")`

              - `JsonValue; type "text_editor_code_execution_tool_result_error"constant`

                - `TEXT_EDITOR_CODE_EXECUTION_TOOL_RESULT_ERROR("text_editor_code_execution_tool_result_error")`

              - `Optional<String> errorMessage`

            - `class TextEditorCodeExecutionViewResultBlockParam:`

              - `String content`

              - `FileType fileType`

                - `TEXT("text")`

                - `IMAGE("image")`

                - `PDF("pdf")`

              - `JsonValue; type "text_editor_code_execution_view_result"constant`

                - `TEXT_EDITOR_CODE_EXECUTION_VIEW_RESULT("text_editor_code_execution_view_result")`

              - `Optional<Long> numLines`

              - `Optional<Long> startLine`

              - `Optional<Long> totalLines`

            - `class TextEditorCodeExecutionCreateResultBlockParam:`

              - `boolean isFileUpdate`

              - `JsonValue; type "text_editor_code_execution_create_result"constant`

                - `TEXT_EDITOR_CODE_EXECUTION_CREATE_RESULT("text_editor_code_execution_create_result")`

            - `class TextEditorCodeExecutionStrReplaceResultBlockParam:`

              - `JsonValue; type "text_editor_code_execution_str_replace_result"constant`

                - `TEXT_EDITOR_CODE_EXECUTION_STR_REPLACE_RESULT("text_editor_code_execution_str_replace_result")`

              - `Optional<List<String>> lines`

              - `Optional<Long> newLines`

              - `Optional<Long> newStart`

              - `Optional<Long> oldLines`

              - `Optional<Long> oldStart`

          - `String toolUseId`

          - `JsonValue; type "text_editor_code_execution_tool_result"constant`

            - `TEXT_EDITOR_CODE_EXECUTION_TOOL_RESULT("text_editor_code_execution_tool_result")`

          - `Optional<CacheControlEphemeral> cacheControl`

            Create a cache control breakpoint at this content block.

            - `JsonValue; type "ephemeral"constant`

              - `EPHEMERAL("ephemeral")`

            - `Optional<Ttl> ttl`

              The time-to-live for the cache control breakpoint.

              This may be one the following values:

              - `5m`: 5 minutes
              - `1h`: 1 hour

              Defaults to `5m`.

              - `TTL_5M("5m")`

              - `TTL_1H("1h")`

        - `class ToolSearchToolResultBlockParam:`

          - `Content content`

            - `class ToolSearchToolResultErrorParam:`

              - `ToolSearchToolResultErrorCode errorCode`

                - `INVALID_TOOL_INPUT("invalid_tool_input")`

                - `UNAVAILABLE("unavailable")`

                - `TOO_MANY_REQUESTS("too_many_requests")`

                - `EXECUTION_TIME_EXCEEDED("execution_time_exceeded")`

              - `JsonValue; type "tool_search_tool_result_error"constant`

                - `TOOL_SEARCH_TOOL_RESULT_ERROR("tool_search_tool_result_error")`

            - `class ToolSearchToolSearchResultBlockParam:`

              - `List<ToolReferenceBlockParam> toolReferences`

                - `String toolName`

                - `JsonValue; type "tool_reference"constant`

                  - `TOOL_REFERENCE("tool_reference")`

                - `Optional<CacheControlEphemeral> cacheControl`

                  Create a cache control breakpoint at this content block.

                  - `JsonValue; type "ephemeral"constant`

                    - `EPHEMERAL("ephemeral")`

                  - `Optional<Ttl> ttl`

                    The time-to-live for the cache control breakpoint.

                    This may be one the following values:

                    - `5m`: 5 minutes
                    - `1h`: 1 hour

                    Defaults to `5m`.

                    - `TTL_5M("5m")`

                    - `TTL_1H("1h")`

              - `JsonValue; type "tool_search_tool_search_result"constant`

                - `TOOL_SEARCH_TOOL_SEARCH_RESULT("tool_search_tool_search_result")`

          - `String toolUseId`

          - `JsonValue; type "tool_search_tool_result"constant`

            - `TOOL_SEARCH_TOOL_RESULT("tool_search_tool_result")`

          - `Optional<CacheControlEphemeral> cacheControl`

            Create a cache control breakpoint at this content block.

            - `JsonValue; type "ephemeral"constant`

              - `EPHEMERAL("ephemeral")`

            - `Optional<Ttl> ttl`

              The time-to-live for the cache control breakpoint.

              This may be one the following values:

              - `5m`: 5 minutes
              - `1h`: 1 hour

              Defaults to `5m`.

              - `TTL_5M("5m")`

              - `TTL_1H("1h")`

        - `class ContainerUploadBlockParam:`

          A content block that represents a file to be uploaded to the container
          Files uploaded via this block will be available in the container's input directory.

          - `String fileId`

          - `JsonValue; type "container_upload"constant`

            - `CONTAINER_UPLOAD("container_upload")`

          - `Optional<CacheControlEphemeral> cacheControl`

            Create a cache control breakpoint at this content block.

            - `JsonValue; type "ephemeral"constant`

              - `EPHEMERAL("ephemeral")`

            - `Optional<Ttl> ttl`

              The time-to-live for the cache control breakpoint.

              This may be one the following values:

              - `5m`: 5 minutes
              - `1h`: 1 hour

              Defaults to `5m`.

              - `TTL_5M("5m")`

              - `TTL_1H("1h")`

    - `Role role`

      - `USER("user")`

      - `ASSISTANT("assistant")`

  - `Model model`

    The model that will complete your prompt.

    See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

  - `Optional<CacheControlEphemeral> cacheControl`

    Top-level cache control automatically applies a cache_control marker to the last cacheable block in the request.

  - `Optional<String> container`

    Container identifier for reuse across requests.

  - `Optional<String> inferenceGeo`

    Specifies the geographic region for inference processing. If not specified, the workspace's `default_inference_geo` is used.

  - `Optional<Metadata> metadata`

    An object describing metadata about the request.

  - `Optional<OutputConfig> outputConfig`

    Configuration options for the model's output, such as the output format.

  - `Optional<ServiceTier> serviceTier`

    Determines whether to use priority capacity (if available) or standard capacity for this request.

    Anthropic offers different levels of service for your API requests. See [service-tiers](https://docs.claude.com/en/api/service-tiers) for details.

    - `AUTO("auto")`

    - `STANDARD_ONLY("standard_only")`

  - `Optional<List<String>> stopSequences`

    Custom text sequences that will cause the model to stop generating.

    Our models will normally stop when they have naturally completed their turn, which will result in a response `stop_reason` of `"end_turn"`.

    If you want the model to stop generating when it encounters custom strings of text, you can use the `stop_sequences` parameter. If the model encounters one of the custom sequences, the response `stop_reason` value will be `"stop_sequence"` and the response `stop_sequence` value will contain the matched stop sequence.

  - `Optional<System> system`

    System prompt.

    A system prompt is a way of providing context and instructions to Claude, such as specifying a particular goal or role. See our [guide to system prompts](https://docs.claude.com/en/docs/system-prompts).

    - `String`

    - `List<TextBlockParam>`

      - `String text`

      - `JsonValue; type "text"constant`

        - `TEXT("text")`

      - `Optional<CacheControlEphemeral> cacheControl`

        Create a cache control breakpoint at this content block.

        - `JsonValue; type "ephemeral"constant`

          - `EPHEMERAL("ephemeral")`

        - `Optional<Ttl> ttl`

          The time-to-live for the cache control breakpoint.

          This may be one the following values:

          - `5m`: 5 minutes
          - `1h`: 1 hour

          Defaults to `5m`.

          - `TTL_5M("5m")`

          - `TTL_1H("1h")`

      - `Optional<List<TextCitationParam>> citations`

        - `class CitationCharLocationParam:`

          - `String citedText`

          - `long documentIndex`

          - `Optional<String> documentTitle`

          - `long endCharIndex`

          - `long startCharIndex`

          - `JsonValue; type "char_location"constant`

            - `CHAR_LOCATION("char_location")`

        - `class CitationPageLocationParam:`

          - `String citedText`

          - `long documentIndex`

          - `Optional<String> documentTitle`

          - `long endPageNumber`

          - `long startPageNumber`

          - `JsonValue; type "page_location"constant`

            - `PAGE_LOCATION("page_location")`

        - `class CitationContentBlockLocationParam:`

          - `String citedText`

          - `long documentIndex`

          - `Optional<String> documentTitle`

          - `long endBlockIndex`

          - `long startBlockIndex`

          - `JsonValue; type "content_block_location"constant`

            - `CONTENT_BLOCK_LOCATION("content_block_location")`

        - `class CitationWebSearchResultLocationParam:`

          - `String citedText`

          - `String encryptedIndex`

          - `Optional<String> title`

          - `JsonValue; type "web_search_result_location"constant`

            - `WEB_SEARCH_RESULT_LOCATION("web_search_result_location")`

          - `String url`

        - `class CitationSearchResultLocationParam:`

          - `String citedText`

          - `long endBlockIndex`

          - `long searchResultIndex`

          - `String source`

          - `long startBlockIndex`

          - `Optional<String> title`

          - `JsonValue; type "search_result_location"constant`

            - `SEARCH_RESULT_LOCATION("search_result_location")`

  - `Optional<Double> temperature`

    Amount of randomness injected into the response.

    Defaults to `1.0`. Ranges from `0.0` to `1.0`. Use `temperature` closer to `0.0` for analytical / multiple choice, and closer to `1.0` for creative and generative tasks.

    Note that even with `temperature` of `0.0`, the results will not be fully deterministic.

  - `Optional<ThinkingConfigParam> thinking`

    Configuration for enabling Claude's extended thinking.

    When enabled, responses include `thinking` content blocks showing Claude's thinking process before the final answer. Requires a minimum budget of 1,024 tokens and counts towards your `max_tokens` limit.

    See [extended thinking](https://docs.claude.com/en/docs/build-with-claude/extended-thinking) for details.

  - `Optional<ToolChoice> toolChoice`

    How the model should use the provided tools. The model can use a specific tool, any available tool, decide by itself, or not use tools at all.

  - `Optional<List<ToolUnion>> tools`

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

    - `class Tool:`

      - `InputSchema inputSchema`

        [JSON schema](https://json-schema.org/draft/2020-12) for this tool's input.

        This defines the shape of the `input` that your tool accepts and that the model will produce.

        - `JsonValue; type "object"constant`

          - `OBJECT("object")`

        - `Optional<Properties> properties`

        - `Optional<List<String>> required`

      - `String name`

        Name of the tool.

        This is how the tool will be called by the model and in `tool_use` blocks.

      - `Optional<List<AllowedCaller>> allowedCallers`

        - `DIRECT("direct")`

        - `CODE_EXECUTION_20250825("code_execution_20250825")`

        - `CODE_EXECUTION_20260120("code_execution_20260120")`

      - `Optional<CacheControlEphemeral> cacheControl`

        Create a cache control breakpoint at this content block.

        - `JsonValue; type "ephemeral"constant`

          - `EPHEMERAL("ephemeral")`

        - `Optional<Ttl> ttl`

          The time-to-live for the cache control breakpoint.

          This may be one the following values:

          - `5m`: 5 minutes
          - `1h`: 1 hour

          Defaults to `5m`.

          - `TTL_5M("5m")`

          - `TTL_1H("1h")`

      - `Optional<Boolean> deferLoading`

        If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

      - `Optional<String> description`

        Description of what this tool does.

        Tool descriptions should be as detailed as possible. The more information that the model has about what the tool is and how to use it, the better it will perform. You can use natural language descriptions to reinforce important aspects of the tool input JSON schema.

      - `Optional<Boolean> eagerInputStreaming`

        Enable eager input streaming for this tool. When true, tool input parameters will be streamed incrementally as they are generated, and types will be inferred on-the-fly rather than buffering the full JSON output. When false, streaming is disabled for this tool even if the fine-grained-tool-streaming beta is active. When null (default), uses the default behavior based on beta headers.

      - `Optional<List<InputExample>> inputExamples`

      - `Optional<Boolean> strict`

        When true, guarantees schema validation on tool names and inputs

      - `Optional<Type> type`

        - `CUSTOM("custom")`

    - `class ToolBash20250124:`

      - `JsonValue; name "bash"constant`

        Name of the tool.

        This is how the tool will be called by the model and in `tool_use` blocks.

        - `BASH("bash")`

      - `JsonValue; type "bash_20250124"constant`

        - `BASH_20250124("bash_20250124")`

      - `Optional<List<AllowedCaller>> allowedCallers`

        - `DIRECT("direct")`

        - `CODE_EXECUTION_20250825("code_execution_20250825")`

        - `CODE_EXECUTION_20260120("code_execution_20260120")`

      - `Optional<CacheControlEphemeral> cacheControl`

        Create a cache control breakpoint at this content block.

        - `JsonValue; type "ephemeral"constant`

          - `EPHEMERAL("ephemeral")`

        - `Optional<Ttl> ttl`

          The time-to-live for the cache control breakpoint.

          This may be one the following values:

          - `5m`: 5 minutes
          - `1h`: 1 hour

          Defaults to `5m`.

          - `TTL_5M("5m")`

          - `TTL_1H("1h")`

      - `Optional<Boolean> deferLoading`

        If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

      - `Optional<List<InputExample>> inputExamples`

      - `Optional<Boolean> strict`

        When true, guarantees schema validation on tool names and inputs

    - `class CodeExecutionTool20250522:`

      - `JsonValue; name "code_execution"constant`

        Name of the tool.

        This is how the tool will be called by the model and in `tool_use` blocks.

        - `CODE_EXECUTION("code_execution")`

      - `JsonValue; type "code_execution_20250522"constant`

        - `CODE_EXECUTION_20250522("code_execution_20250522")`

      - `Optional<List<AllowedCaller>> allowedCallers`

        - `DIRECT("direct")`

        - `CODE_EXECUTION_20250825("code_execution_20250825")`

        - `CODE_EXECUTION_20260120("code_execution_20260120")`

      - `Optional<CacheControlEphemeral> cacheControl`

        Create a cache control breakpoint at this content block.

        - `JsonValue; type "ephemeral"constant`

          - `EPHEMERAL("ephemeral")`

        - `Optional<Ttl> ttl`

          The time-to-live for the cache control breakpoint.

          This may be one the following values:

          - `5m`: 5 minutes
          - `1h`: 1 hour

          Defaults to `5m`.

          - `TTL_5M("5m")`

          - `TTL_1H("1h")`

      - `Optional<Boolean> deferLoading`

        If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

      - `Optional<Boolean> strict`

        When true, guarantees schema validation on tool names and inputs

    - `class CodeExecutionTool20250825:`

      - `JsonValue; name "code_execution"constant`

        Name of the tool.

        This is how the tool will be called by the model and in `tool_use` blocks.

        - `CODE_EXECUTION("code_execution")`

      - `JsonValue; type "code_execution_20250825"constant`

        - `CODE_EXECUTION_20250825("code_execution_20250825")`

      - `Optional<List<AllowedCaller>> allowedCallers`

        - `DIRECT("direct")`

        - `CODE_EXECUTION_20250825("code_execution_20250825")`

        - `CODE_EXECUTION_20260120("code_execution_20260120")`

      - `Optional<CacheControlEphemeral> cacheControl`

        Create a cache control breakpoint at this content block.

        - `JsonValue; type "ephemeral"constant`

          - `EPHEMERAL("ephemeral")`

        - `Optional<Ttl> ttl`

          The time-to-live for the cache control breakpoint.

          This may be one the following values:

          - `5m`: 5 minutes
          - `1h`: 1 hour

          Defaults to `5m`.

          - `TTL_5M("5m")`

          - `TTL_1H("1h")`

      - `Optional<Boolean> deferLoading`

        If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

      - `Optional<Boolean> strict`

        When true, guarantees schema validation on tool names and inputs

    - `class CodeExecutionTool20260120:`

      Code execution tool with REPL state persistence (daemon mode + gVisor checkpoint).

      - `JsonValue; name "code_execution"constant`

        Name of the tool.

        This is how the tool will be called by the model and in `tool_use` blocks.

        - `CODE_EXECUTION("code_execution")`

      - `JsonValue; type "code_execution_20260120"constant`

        - `CODE_EXECUTION_20260120("code_execution_20260120")`

      - `Optional<List<AllowedCaller>> allowedCallers`

        - `DIRECT("direct")`

        - `CODE_EXECUTION_20250825("code_execution_20250825")`

        - `CODE_EXECUTION_20260120("code_execution_20260120")`

      - `Optional<CacheControlEphemeral> cacheControl`

        Create a cache control breakpoint at this content block.

        - `JsonValue; type "ephemeral"constant`

          - `EPHEMERAL("ephemeral")`

        - `Optional<Ttl> ttl`

          The time-to-live for the cache control breakpoint.

          This may be one the following values:

          - `5m`: 5 minutes
          - `1h`: 1 hour

          Defaults to `5m`.

          - `TTL_5M("5m")`

          - `TTL_1H("1h")`

      - `Optional<Boolean> deferLoading`

        If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

      - `Optional<Boolean> strict`

        When true, guarantees schema validation on tool names and inputs

    - `class MemoryTool20250818:`

      - `JsonValue; name "memory"constant`

        Name of the tool.

        This is how the tool will be called by the model and in `tool_use` blocks.

        - `MEMORY("memory")`

      - `JsonValue; type "memory_20250818"constant`

        - `MEMORY_20250818("memory_20250818")`

      - `Optional<List<AllowedCaller>> allowedCallers`

        - `DIRECT("direct")`

        - `CODE_EXECUTION_20250825("code_execution_20250825")`

        - `CODE_EXECUTION_20260120("code_execution_20260120")`

      - `Optional<CacheControlEphemeral> cacheControl`

        Create a cache control breakpoint at this content block.

        - `JsonValue; type "ephemeral"constant`

          - `EPHEMERAL("ephemeral")`

        - `Optional<Ttl> ttl`

          The time-to-live for the cache control breakpoint.

          This may be one the following values:

          - `5m`: 5 minutes
          - `1h`: 1 hour

          Defaults to `5m`.

          - `TTL_5M("5m")`

          - `TTL_1H("1h")`

      - `Optional<Boolean> deferLoading`

        If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

      - `Optional<List<InputExample>> inputExamples`

      - `Optional<Boolean> strict`

        When true, guarantees schema validation on tool names and inputs

    - `class ToolTextEditor20250124:`

      - `JsonValue; name "str_replace_editor"constant`

        Name of the tool.

        This is how the tool will be called by the model and in `tool_use` blocks.

        - `STR_REPLACE_EDITOR("str_replace_editor")`

      - `JsonValue; type "text_editor_20250124"constant`

        - `TEXT_EDITOR_20250124("text_editor_20250124")`

      - `Optional<List<AllowedCaller>> allowedCallers`

        - `DIRECT("direct")`

        - `CODE_EXECUTION_20250825("code_execution_20250825")`

        - `CODE_EXECUTION_20260120("code_execution_20260120")`

      - `Optional<CacheControlEphemeral> cacheControl`

        Create a cache control breakpoint at this content block.

        - `JsonValue; type "ephemeral"constant`

          - `EPHEMERAL("ephemeral")`

        - `Optional<Ttl> ttl`

          The time-to-live for the cache control breakpoint.

          This may be one the following values:

          - `5m`: 5 minutes
          - `1h`: 1 hour

          Defaults to `5m`.

          - `TTL_5M("5m")`

          - `TTL_1H("1h")`

      - `Optional<Boolean> deferLoading`

        If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

      - `Optional<List<InputExample>> inputExamples`

      - `Optional<Boolean> strict`

        When true, guarantees schema validation on tool names and inputs

    - `class ToolTextEditor20250429:`

      - `JsonValue; name "str_replace_based_edit_tool"constant`

        Name of the tool.

        This is how the tool will be called by the model and in `tool_use` blocks.

        - `STR_REPLACE_BASED_EDIT_TOOL("str_replace_based_edit_tool")`

      - `JsonValue; type "text_editor_20250429"constant`

        - `TEXT_EDITOR_20250429("text_editor_20250429")`

      - `Optional<List<AllowedCaller>> allowedCallers`

        - `DIRECT("direct")`

        - `CODE_EXECUTION_20250825("code_execution_20250825")`

        - `CODE_EXECUTION_20260120("code_execution_20260120")`

      - `Optional<CacheControlEphemeral> cacheControl`

        Create a cache control breakpoint at this content block.

        - `JsonValue; type "ephemeral"constant`

          - `EPHEMERAL("ephemeral")`

        - `Optional<Ttl> ttl`

          The time-to-live for the cache control breakpoint.

          This may be one the following values:

          - `5m`: 5 minutes
          - `1h`: 1 hour

          Defaults to `5m`.

          - `TTL_5M("5m")`

          - `TTL_1H("1h")`

      - `Optional<Boolean> deferLoading`

        If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

      - `Optional<List<InputExample>> inputExamples`

      - `Optional<Boolean> strict`

        When true, guarantees schema validation on tool names and inputs

    - `class ToolTextEditor20250728:`

      - `JsonValue; name "str_replace_based_edit_tool"constant`

        Name of the tool.

        This is how the tool will be called by the model and in `tool_use` blocks.

        - `STR_REPLACE_BASED_EDIT_TOOL("str_replace_based_edit_tool")`

      - `JsonValue; type "text_editor_20250728"constant`

        - `TEXT_EDITOR_20250728("text_editor_20250728")`

      - `Optional<List<AllowedCaller>> allowedCallers`

        - `DIRECT("direct")`

        - `CODE_EXECUTION_20250825("code_execution_20250825")`

        - `CODE_EXECUTION_20260120("code_execution_20260120")`

      - `Optional<CacheControlEphemeral> cacheControl`

        Create a cache control breakpoint at this content block.

        - `JsonValue; type "ephemeral"constant`

          - `EPHEMERAL("ephemeral")`

        - `Optional<Ttl> ttl`

          The time-to-live for the cache control breakpoint.

          This may be one the following values:

          - `5m`: 5 minutes
          - `1h`: 1 hour

          Defaults to `5m`.

          - `TTL_5M("5m")`

          - `TTL_1H("1h")`

      - `Optional<Boolean> deferLoading`

        If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

      - `Optional<List<InputExample>> inputExamples`

      - `Optional<Long> maxCharacters`

        Maximum number of characters to display when viewing a file. If not specified, defaults to displaying the full file.

      - `Optional<Boolean> strict`

        When true, guarantees schema validation on tool names and inputs

    - `class WebSearchTool20250305:`

      - `JsonValue; name "web_search"constant`

        Name of the tool.

        This is how the tool will be called by the model and in `tool_use` blocks.

        - `WEB_SEARCH("web_search")`

      - `JsonValue; type "web_search_20250305"constant`

        - `WEB_SEARCH_20250305("web_search_20250305")`

      - `Optional<List<AllowedCaller>> allowedCallers`

        - `DIRECT("direct")`

        - `CODE_EXECUTION_20250825("code_execution_20250825")`

        - `CODE_EXECUTION_20260120("code_execution_20260120")`

      - `Optional<List<String>> allowedDomains`

        If provided, only these domains will be included in results. Cannot be used alongside `blocked_domains`.

      - `Optional<List<String>> blockedDomains`

        If provided, these domains will never appear in results. Cannot be used alongside `allowed_domains`.

      - `Optional<CacheControlEphemeral> cacheControl`

        Create a cache control breakpoint at this content block.

        - `JsonValue; type "ephemeral"constant`

          - `EPHEMERAL("ephemeral")`

        - `Optional<Ttl> ttl`

          The time-to-live for the cache control breakpoint.

          This may be one the following values:

          - `5m`: 5 minutes
          - `1h`: 1 hour

          Defaults to `5m`.

          - `TTL_5M("5m")`

          - `TTL_1H("1h")`

      - `Optional<Boolean> deferLoading`

        If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

      - `Optional<Long> maxUses`

        Maximum number of times the tool can be used in the API request.

      - `Optional<Boolean> strict`

        When true, guarantees schema validation on tool names and inputs

      - `Optional<UserLocation> userLocation`

        Parameters for the user's location. Used to provide more relevant search results.

        - `JsonValue; type "approximate"constant`

          - `APPROXIMATE("approximate")`

        - `Optional<String> city`

          The city of the user.

        - `Optional<String> country`

          The two letter [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) of the user.

        - `Optional<String> region`

          The region of the user.

        - `Optional<String> timezone`

          The [IANA timezone](https://nodatime.org/TimeZones) of the user.

    - `class WebFetchTool20250910:`

      - `JsonValue; name "web_fetch"constant`

        Name of the tool.

        This is how the tool will be called by the model and in `tool_use` blocks.

        - `WEB_FETCH("web_fetch")`

      - `JsonValue; type "web_fetch_20250910"constant`

        - `WEB_FETCH_20250910("web_fetch_20250910")`

      - `Optional<List<AllowedCaller>> allowedCallers`

        - `DIRECT("direct")`

        - `CODE_EXECUTION_20250825("code_execution_20250825")`

        - `CODE_EXECUTION_20260120("code_execution_20260120")`

      - `Optional<List<String>> allowedDomains`

        List of domains to allow fetching from

      - `Optional<List<String>> blockedDomains`

        List of domains to block fetching from

      - `Optional<CacheControlEphemeral> cacheControl`

        Create a cache control breakpoint at this content block.

        - `JsonValue; type "ephemeral"constant`

          - `EPHEMERAL("ephemeral")`

        - `Optional<Ttl> ttl`

          The time-to-live for the cache control breakpoint.

          This may be one the following values:

          - `5m`: 5 minutes
          - `1h`: 1 hour

          Defaults to `5m`.

          - `TTL_5M("5m")`

          - `TTL_1H("1h")`

      - `Optional<CitationsConfigParam> citations`

        Citations configuration for fetched documents. Citations are disabled by default.

        - `Optional<Boolean> enabled`

      - `Optional<Boolean> deferLoading`

        If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

      - `Optional<Long> maxContentTokens`

        Maximum number of tokens used by including web page text content in the context. The limit is approximate and does not apply to binary content such as PDFs.

      - `Optional<Long> maxUses`

        Maximum number of times the tool can be used in the API request.

      - `Optional<Boolean> strict`

        When true, guarantees schema validation on tool names and inputs

    - `class WebSearchTool20260209:`

      - `JsonValue; name "web_search"constant`

        Name of the tool.

        This is how the tool will be called by the model and in `tool_use` blocks.

        - `WEB_SEARCH("web_search")`

      - `JsonValue; type "web_search_20260209"constant`

        - `WEB_SEARCH_20260209("web_search_20260209")`

      - `Optional<List<AllowedCaller>> allowedCallers`

        - `DIRECT("direct")`

        - `CODE_EXECUTION_20250825("code_execution_20250825")`

        - `CODE_EXECUTION_20260120("code_execution_20260120")`

      - `Optional<List<String>> allowedDomains`

        If provided, only these domains will be included in results. Cannot be used alongside `blocked_domains`.

      - `Optional<List<String>> blockedDomains`

        If provided, these domains will never appear in results. Cannot be used alongside `allowed_domains`.

      - `Optional<CacheControlEphemeral> cacheControl`

        Create a cache control breakpoint at this content block.

        - `JsonValue; type "ephemeral"constant`

          - `EPHEMERAL("ephemeral")`

        - `Optional<Ttl> ttl`

          The time-to-live for the cache control breakpoint.

          This may be one the following values:

          - `5m`: 5 minutes
          - `1h`: 1 hour

          Defaults to `5m`.

          - `TTL_5M("5m")`

          - `TTL_1H("1h")`

      - `Optional<Boolean> deferLoading`

        If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

      - `Optional<Long> maxUses`

        Maximum number of times the tool can be used in the API request.

      - `Optional<Boolean> strict`

        When true, guarantees schema validation on tool names and inputs

      - `Optional<UserLocation> userLocation`

        Parameters for the user's location. Used to provide more relevant search results.

        - `JsonValue; type "approximate"constant`

          - `APPROXIMATE("approximate")`

        - `Optional<String> city`

          The city of the user.

        - `Optional<String> country`

          The two letter [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) of the user.

        - `Optional<String> region`

          The region of the user.

        - `Optional<String> timezone`

          The [IANA timezone](https://nodatime.org/TimeZones) of the user.

    - `class WebFetchTool20260209:`

      - `JsonValue; name "web_fetch"constant`

        Name of the tool.

        This is how the tool will be called by the model and in `tool_use` blocks.

        - `WEB_FETCH("web_fetch")`

      - `JsonValue; type "web_fetch_20260209"constant`

        - `WEB_FETCH_20260209("web_fetch_20260209")`

      - `Optional<List<AllowedCaller>> allowedCallers`

        - `DIRECT("direct")`

        - `CODE_EXECUTION_20250825("code_execution_20250825")`

        - `CODE_EXECUTION_20260120("code_execution_20260120")`

      - `Optional<List<String>> allowedDomains`

        List of domains to allow fetching from

      - `Optional<List<String>> blockedDomains`

        List of domains to block fetching from

      - `Optional<CacheControlEphemeral> cacheControl`

        Create a cache control breakpoint at this content block.

        - `JsonValue; type "ephemeral"constant`

          - `EPHEMERAL("ephemeral")`

        - `Optional<Ttl> ttl`

          The time-to-live for the cache control breakpoint.

          This may be one the following values:

          - `5m`: 5 minutes
          - `1h`: 1 hour

          Defaults to `5m`.

          - `TTL_5M("5m")`

          - `TTL_1H("1h")`

      - `Optional<CitationsConfigParam> citations`

        Citations configuration for fetched documents. Citations are disabled by default.

        - `Optional<Boolean> enabled`

      - `Optional<Boolean> deferLoading`

        If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

      - `Optional<Long> maxContentTokens`

        Maximum number of tokens used by including web page text content in the context. The limit is approximate and does not apply to binary content such as PDFs.

      - `Optional<Long> maxUses`

        Maximum number of times the tool can be used in the API request.

      - `Optional<Boolean> strict`

        When true, guarantees schema validation on tool names and inputs

    - `class ToolSearchToolBm25_20251119:`

      - `JsonValue; name "tool_search_tool_bm25"constant`

        Name of the tool.

        This is how the tool will be called by the model and in `tool_use` blocks.

        - `TOOL_SEARCH_TOOL_BM25("tool_search_tool_bm25")`

      - `Type type`

        - `TOOL_SEARCH_TOOL_BM25_20251119("tool_search_tool_bm25_20251119")`

        - `TOOL_SEARCH_TOOL_BM25("tool_search_tool_bm25")`

      - `Optional<List<AllowedCaller>> allowedCallers`

        - `DIRECT("direct")`

        - `CODE_EXECUTION_20250825("code_execution_20250825")`

        - `CODE_EXECUTION_20260120("code_execution_20260120")`

      - `Optional<CacheControlEphemeral> cacheControl`

        Create a cache control breakpoint at this content block.

        - `JsonValue; type "ephemeral"constant`

          - `EPHEMERAL("ephemeral")`

        - `Optional<Ttl> ttl`

          The time-to-live for the cache control breakpoint.

          This may be one the following values:

          - `5m`: 5 minutes
          - `1h`: 1 hour

          Defaults to `5m`.

          - `TTL_5M("5m")`

          - `TTL_1H("1h")`

      - `Optional<Boolean> deferLoading`

        If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

      - `Optional<Boolean> strict`

        When true, guarantees schema validation on tool names and inputs

    - `class ToolSearchToolRegex20251119:`

      - `JsonValue; name "tool_search_tool_regex"constant`

        Name of the tool.

        This is how the tool will be called by the model and in `tool_use` blocks.

        - `TOOL_SEARCH_TOOL_REGEX("tool_search_tool_regex")`

      - `Type type`

        - `TOOL_SEARCH_TOOL_REGEX_20251119("tool_search_tool_regex_20251119")`

        - `TOOL_SEARCH_TOOL_REGEX("tool_search_tool_regex")`

      - `Optional<List<AllowedCaller>> allowedCallers`

        - `DIRECT("direct")`

        - `CODE_EXECUTION_20250825("code_execution_20250825")`

        - `CODE_EXECUTION_20260120("code_execution_20260120")`

      - `Optional<CacheControlEphemeral> cacheControl`

        Create a cache control breakpoint at this content block.

        - `JsonValue; type "ephemeral"constant`

          - `EPHEMERAL("ephemeral")`

        - `Optional<Ttl> ttl`

          The time-to-live for the cache control breakpoint.

          This may be one the following values:

          - `5m`: 5 minutes
          - `1h`: 1 hour

          Defaults to `5m`.

          - `TTL_5M("5m")`

          - `TTL_1H("1h")`

      - `Optional<Boolean> deferLoading`

        If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

      - `Optional<Boolean> strict`

        When true, guarantees schema validation on tool names and inputs

  - `Optional<Long> topK`

    Only sample from the top K options for each subsequent token.

    Used to remove "long tail" low probability responses. [Learn more technical details here](https://towardsdatascience.com/how-to-sample-from-language-models-682bceb97277).

    Recommended for advanced use cases only. You usually only need to use `temperature`.

  - `Optional<Double> topP`

    Use nucleus sampling.

    In nucleus sampling, we compute the cumulative distribution over all the options for each subsequent token in decreasing probability order and cut it off once it reaches a particular probability specified by `top_p`. You should either alter `temperature` or `top_p`, but not both.

    Recommended for advanced use cases only. You usually only need to use `temperature`.

### Returns

- `class Message:`

  - `String id`

    Unique object identifier.

    The format and length of IDs may change over time.

  - `Optional<Container> container`

    Information about the container used in the request (for the code execution tool)

    - `String id`

      Identifier for the container used in this request

    - `LocalDateTime expiresAt`

      The time at which the container will expire.

  - `List<ContentBlock> content`

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

    - `class TextBlock:`

      - `Optional<List<TextCitation>> citations`

        Citations supporting the text block.

        The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

        - `class CitationCharLocation:`

          - `String citedText`

          - `long documentIndex`

          - `Optional<String> documentTitle`

          - `long endCharIndex`

          - `Optional<String> fileId`

          - `long startCharIndex`

          - `JsonValue; type "char_location"constant`

            - `CHAR_LOCATION("char_location")`

        - `class CitationPageLocation:`

          - `String citedText`

          - `long documentIndex`

          - `Optional<String> documentTitle`

          - `long endPageNumber`

          - `Optional<String> fileId`

          - `long startPageNumber`

          - `JsonValue; type "page_location"constant`

            - `PAGE_LOCATION("page_location")`

        - `class CitationContentBlockLocation:`

          - `String citedText`

          - `long documentIndex`

          - `Optional<String> documentTitle`

          - `long endBlockIndex`

          - `Optional<String> fileId`

          - `long startBlockIndex`

          - `JsonValue; type "content_block_location"constant`

            - `CONTENT_BLOCK_LOCATION("content_block_location")`

        - `class CitationsWebSearchResultLocation:`

          - `String citedText`

          - `String encryptedIndex`

          - `Optional<String> title`

          - `JsonValue; type "web_search_result_location"constant`

            - `WEB_SEARCH_RESULT_LOCATION("web_search_result_location")`

          - `String url`

        - `class CitationsSearchResultLocation:`

          - `String citedText`

          - `long endBlockIndex`

          - `long searchResultIndex`

          - `String source`

          - `long startBlockIndex`

          - `Optional<String> title`

          - `JsonValue; type "search_result_location"constant`

            - `SEARCH_RESULT_LOCATION("search_result_location")`

      - `String text`

      - `JsonValue; type "text"constant`

        - `TEXT("text")`

    - `class ThinkingBlock:`

      - `String signature`

      - `String thinking`

      - `JsonValue; type "thinking"constant`

        - `THINKING("thinking")`

    - `class RedactedThinkingBlock:`

      - `String data`

      - `JsonValue; type "redacted_thinking"constant`

        - `REDACTED_THINKING("redacted_thinking")`

    - `class ToolUseBlock:`

      - `String id`

      - `Caller caller`

        Tool invocation directly from the model.

        - `class DirectCaller:`

          Tool invocation directly from the model.

          - `JsonValue; type "direct"constant`

            - `DIRECT("direct")`

        - `class ServerToolCaller:`

          Tool invocation generated by a server-side tool.

          - `String toolId`

          - `JsonValue; type "code_execution_20250825"constant`

            - `CODE_EXECUTION_20250825("code_execution_20250825")`

        - `class ServerToolCaller20260120:`

          - `String toolId`

          - `JsonValue; type "code_execution_20260120"constant`

            - `CODE_EXECUTION_20260120("code_execution_20260120")`

      - `Input input`

      - `String name`

      - `JsonValue; type "tool_use"constant`

        - `TOOL_USE("tool_use")`

    - `class ServerToolUseBlock:`

      - `String id`

      - `Caller caller`

        Tool invocation directly from the model.

        - `class DirectCaller:`

          Tool invocation directly from the model.

          - `JsonValue; type "direct"constant`

            - `DIRECT("direct")`

        - `class ServerToolCaller:`

          Tool invocation generated by a server-side tool.

          - `String toolId`

          - `JsonValue; type "code_execution_20250825"constant`

            - `CODE_EXECUTION_20250825("code_execution_20250825")`

        - `class ServerToolCaller20260120:`

          - `String toolId`

          - `JsonValue; type "code_execution_20260120"constant`

            - `CODE_EXECUTION_20260120("code_execution_20260120")`

      - `Input input`

      - `Name name`

        - `WEB_SEARCH("web_search")`

        - `WEB_FETCH("web_fetch")`

        - `CODE_EXECUTION("code_execution")`

        - `BASH_CODE_EXECUTION("bash_code_execution")`

        - `TEXT_EDITOR_CODE_EXECUTION("text_editor_code_execution")`

        - `TOOL_SEARCH_TOOL_REGEX("tool_search_tool_regex")`

        - `TOOL_SEARCH_TOOL_BM25("tool_search_tool_bm25")`

      - `JsonValue; type "server_tool_use"constant`

        - `SERVER_TOOL_USE("server_tool_use")`

    - `class WebSearchToolResultBlock:`

      - `Caller caller`

        Tool invocation directly from the model.

        - `class DirectCaller:`

          Tool invocation directly from the model.

          - `JsonValue; type "direct"constant`

            - `DIRECT("direct")`

        - `class ServerToolCaller:`

          Tool invocation generated by a server-side tool.

          - `String toolId`

          - `JsonValue; type "code_execution_20250825"constant`

            - `CODE_EXECUTION_20250825("code_execution_20250825")`

        - `class ServerToolCaller20260120:`

          - `String toolId`

          - `JsonValue; type "code_execution_20260120"constant`

            - `CODE_EXECUTION_20260120("code_execution_20260120")`

      - `WebSearchToolResultBlockContent content`

        - `class WebSearchToolResultError:`

          - `WebSearchToolResultErrorCode errorCode`

            - `INVALID_TOOL_INPUT("invalid_tool_input")`

            - `UNAVAILABLE("unavailable")`

            - `MAX_USES_EXCEEDED("max_uses_exceeded")`

            - `TOO_MANY_REQUESTS("too_many_requests")`

            - `QUERY_TOO_LONG("query_too_long")`

            - `REQUEST_TOO_LARGE("request_too_large")`

          - `JsonValue; type "web_search_tool_result_error"constant`

            - `WEB_SEARCH_TOOL_RESULT_ERROR("web_search_tool_result_error")`

        - `List<WebSearchResultBlock>`

          - `String encryptedContent`

          - `Optional<String> pageAge`

          - `String title`

          - `JsonValue; type "web_search_result"constant`

            - `WEB_SEARCH_RESULT("web_search_result")`

          - `String url`

      - `String toolUseId`

      - `JsonValue; type "web_search_tool_result"constant`

        - `WEB_SEARCH_TOOL_RESULT("web_search_tool_result")`

    - `class WebFetchToolResultBlock:`

      - `Caller caller`

        Tool invocation directly from the model.

        - `class DirectCaller:`

          Tool invocation directly from the model.

          - `JsonValue; type "direct"constant`

            - `DIRECT("direct")`

        - `class ServerToolCaller:`

          Tool invocation generated by a server-side tool.

          - `String toolId`

          - `JsonValue; type "code_execution_20250825"constant`

            - `CODE_EXECUTION_20250825("code_execution_20250825")`

        - `class ServerToolCaller20260120:`

          - `String toolId`

          - `JsonValue; type "code_execution_20260120"constant`

            - `CODE_EXECUTION_20260120("code_execution_20260120")`

      - `Content content`

        - `class WebFetchToolResultErrorBlock:`

          - `WebFetchToolResultErrorCode errorCode`

            - `INVALID_TOOL_INPUT("invalid_tool_input")`

            - `URL_TOO_LONG("url_too_long")`

            - `URL_NOT_ALLOWED("url_not_allowed")`

            - `URL_NOT_ACCESSIBLE("url_not_accessible")`

            - `UNSUPPORTED_CONTENT_TYPE("unsupported_content_type")`

            - `TOO_MANY_REQUESTS("too_many_requests")`

            - `MAX_USES_EXCEEDED("max_uses_exceeded")`

            - `UNAVAILABLE("unavailable")`

          - `JsonValue; type "web_fetch_tool_result_error"constant`

            - `WEB_FETCH_TOOL_RESULT_ERROR("web_fetch_tool_result_error")`

        - `class WebFetchBlock:`

          - `DocumentBlock content`

            - `Optional<CitationsConfig> citations`

              Citation configuration for the document

              - `boolean enabled`

            - `Source source`

              - `class Base64PdfSource:`

                - `String data`

                - `JsonValue; mediaType "application/pdf"constant`

                  - `APPLICATION_PDF("application/pdf")`

                - `JsonValue; type "base64"constant`

                  - `BASE64("base64")`

              - `class PlainTextSource:`

                - `String data`

                - `JsonValue; mediaType "text/plain"constant`

                  - `TEXT_PLAIN("text/plain")`

                - `JsonValue; type "text"constant`

                  - `TEXT("text")`

            - `Optional<String> title`

              The title of the document

            - `JsonValue; type "document"constant`

              - `DOCUMENT("document")`

          - `Optional<String> retrievedAt`

            ISO 8601 timestamp when the content was retrieved

          - `JsonValue; type "web_fetch_result"constant`

            - `WEB_FETCH_RESULT("web_fetch_result")`

          - `String url`

            Fetched content URL

      - `String toolUseId`

      - `JsonValue; type "web_fetch_tool_result"constant`

        - `WEB_FETCH_TOOL_RESULT("web_fetch_tool_result")`

    - `class CodeExecutionToolResultBlock:`

      - `CodeExecutionToolResultBlockContent content`

        Code execution result with encrypted stdout for PFC + web_search results.

        - `class CodeExecutionToolResultError:`

          - `CodeExecutionToolResultErrorCode errorCode`

            - `INVALID_TOOL_INPUT("invalid_tool_input")`

            - `UNAVAILABLE("unavailable")`

            - `TOO_MANY_REQUESTS("too_many_requests")`

            - `EXECUTION_TIME_EXCEEDED("execution_time_exceeded")`

          - `JsonValue; type "code_execution_tool_result_error"constant`

            - `CODE_EXECUTION_TOOL_RESULT_ERROR("code_execution_tool_result_error")`

        - `class CodeExecutionResultBlock:`

          - `List<CodeExecutionOutputBlock> content`

            - `String fileId`

            - `JsonValue; type "code_execution_output"constant`

              - `CODE_EXECUTION_OUTPUT("code_execution_output")`

          - `long returnCode`

          - `String stderr`

          - `String stdout`

          - `JsonValue; type "code_execution_result"constant`

            - `CODE_EXECUTION_RESULT("code_execution_result")`

        - `class EncryptedCodeExecutionResultBlock:`

          Code execution result with encrypted stdout for PFC + web_search results.

          - `List<CodeExecutionOutputBlock> content`

            - `String fileId`

            - `JsonValue; type "code_execution_output"constant`

              - `CODE_EXECUTION_OUTPUT("code_execution_output")`

          - `String encryptedStdout`

          - `long returnCode`

          - `String stderr`

          - `JsonValue; type "encrypted_code_execution_result"constant`

            - `ENCRYPTED_CODE_EXECUTION_RESULT("encrypted_code_execution_result")`

      - `String toolUseId`

      - `JsonValue; type "code_execution_tool_result"constant`

        - `CODE_EXECUTION_TOOL_RESULT("code_execution_tool_result")`

    - `class BashCodeExecutionToolResultBlock:`

      - `Content content`

        - `class BashCodeExecutionToolResultError:`

          - `BashCodeExecutionToolResultErrorCode errorCode`

            - `INVALID_TOOL_INPUT("invalid_tool_input")`

            - `UNAVAILABLE("unavailable")`

            - `TOO_MANY_REQUESTS("too_many_requests")`

            - `EXECUTION_TIME_EXCEEDED("execution_time_exceeded")`

            - `OUTPUT_FILE_TOO_LARGE("output_file_too_large")`

          - `JsonValue; type "bash_code_execution_tool_result_error"constant`

            - `BASH_CODE_EXECUTION_TOOL_RESULT_ERROR("bash_code_execution_tool_result_error")`

        - `class BashCodeExecutionResultBlock:`

          - `List<BashCodeExecutionOutputBlock> content`

            - `String fileId`

            - `JsonValue; type "bash_code_execution_output"constant`

              - `BASH_CODE_EXECUTION_OUTPUT("bash_code_execution_output")`

          - `long returnCode`

          - `String stderr`

          - `String stdout`

          - `JsonValue; type "bash_code_execution_result"constant`

            - `BASH_CODE_EXECUTION_RESULT("bash_code_execution_result")`

      - `String toolUseId`

      - `JsonValue; type "bash_code_execution_tool_result"constant`

        - `BASH_CODE_EXECUTION_TOOL_RESULT("bash_code_execution_tool_result")`

    - `class TextEditorCodeExecutionToolResultBlock:`

      - `Content content`

        - `class TextEditorCodeExecutionToolResultError:`

          - `TextEditorCodeExecutionToolResultErrorCode errorCode`

            - `INVALID_TOOL_INPUT("invalid_tool_input")`

            - `UNAVAILABLE("unavailable")`

            - `TOO_MANY_REQUESTS("too_many_requests")`

            - `EXECUTION_TIME_EXCEEDED("execution_time_exceeded")`

            - `FILE_NOT_FOUND("file_not_found")`

          - `Optional<String> errorMessage`

          - `JsonValue; type "text_editor_code_execution_tool_result_error"constant`

            - `TEXT_EDITOR_CODE_EXECUTION_TOOL_RESULT_ERROR("text_editor_code_execution_tool_result_error")`

        - `class TextEditorCodeExecutionViewResultBlock:`

          - `String content`

          - `FileType fileType`

            - `TEXT("text")`

            - `IMAGE("image")`

            - `PDF("pdf")`

          - `Optional<Long> numLines`

          - `Optional<Long> startLine`

          - `Optional<Long> totalLines`

          - `JsonValue; type "text_editor_code_execution_view_result"constant`

            - `TEXT_EDITOR_CODE_EXECUTION_VIEW_RESULT("text_editor_code_execution_view_result")`

        - `class TextEditorCodeExecutionCreateResultBlock:`

          - `boolean isFileUpdate`

          - `JsonValue; type "text_editor_code_execution_create_result"constant`

            - `TEXT_EDITOR_CODE_EXECUTION_CREATE_RESULT("text_editor_code_execution_create_result")`

        - `class TextEditorCodeExecutionStrReplaceResultBlock:`

          - `Optional<List<String>> lines`

          - `Optional<Long> newLines`

          - `Optional<Long> newStart`

          - `Optional<Long> oldLines`

          - `Optional<Long> oldStart`

          - `JsonValue; type "text_editor_code_execution_str_replace_result"constant`

            - `TEXT_EDITOR_CODE_EXECUTION_STR_REPLACE_RESULT("text_editor_code_execution_str_replace_result")`

      - `String toolUseId`

      - `JsonValue; type "text_editor_code_execution_tool_result"constant`

        - `TEXT_EDITOR_CODE_EXECUTION_TOOL_RESULT("text_editor_code_execution_tool_result")`

    - `class ToolSearchToolResultBlock:`

      - `Content content`

        - `class ToolSearchToolResultError:`

          - `ToolSearchToolResultErrorCode errorCode`

            - `INVALID_TOOL_INPUT("invalid_tool_input")`

            - `UNAVAILABLE("unavailable")`

            - `TOO_MANY_REQUESTS("too_many_requests")`

            - `EXECUTION_TIME_EXCEEDED("execution_time_exceeded")`

          - `Optional<String> errorMessage`

          - `JsonValue; type "tool_search_tool_result_error"constant`

            - `TOOL_SEARCH_TOOL_RESULT_ERROR("tool_search_tool_result_error")`

        - `class ToolSearchToolSearchResultBlock:`

          - `List<ToolReferenceBlock> toolReferences`

            - `String toolName`

            - `JsonValue; type "tool_reference"constant`

              - `TOOL_REFERENCE("tool_reference")`

          - `JsonValue; type "tool_search_tool_search_result"constant`

            - `TOOL_SEARCH_TOOL_SEARCH_RESULT("tool_search_tool_search_result")`

      - `String toolUseId`

      - `JsonValue; type "tool_search_tool_result"constant`

        - `TOOL_SEARCH_TOOL_RESULT("tool_search_tool_result")`

    - `class ContainerUploadBlock:`

      Response model for a file uploaded to the container.

      - `String fileId`

      - `JsonValue; type "container_upload"constant`

        - `CONTAINER_UPLOAD("container_upload")`

  - `Model model`

    The model that will complete your prompt.

    See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

    - `CLAUDE_OPUS_4_6("claude-opus-4-6")`

      Most intelligent model for building agents and coding

    - `CLAUDE_SONNET_4_6("claude-sonnet-4-6")`

      Frontier intelligence at scale — built for coding, agents, and enterprise workflows

    - `CLAUDE_OPUS_4_5_20251101("claude-opus-4-5-20251101")`

      Premium model combining maximum intelligence with practical performance

    - `CLAUDE_OPUS_4_5("claude-opus-4-5")`

      Premium model combining maximum intelligence with practical performance

    - `CLAUDE_3_7_SONNET_LATEST("claude-3-7-sonnet-latest")`

      High-performance model with early extended thinking

    - `CLAUDE_3_7_SONNET_20250219("claude-3-7-sonnet-20250219")`

      High-performance model with early extended thinking

    - `CLAUDE_3_5_HAIKU_LATEST("claude-3-5-haiku-latest")`

      Fastest and most compact model for near-instant responsiveness

    - `CLAUDE_3_5_HAIKU_20241022("claude-3-5-haiku-20241022")`

      Our fastest model

    - `CLAUDE_HAIKU_4_5("claude-haiku-4-5")`

      Hybrid model, capable of near-instant responses and extended thinking

    - `CLAUDE_HAIKU_4_5_20251001("claude-haiku-4-5-20251001")`

      Hybrid model, capable of near-instant responses and extended thinking

    - `CLAUDE_SONNET_4_20250514("claude-sonnet-4-20250514")`

      High-performance model with extended thinking

    - `CLAUDE_SONNET_4_0("claude-sonnet-4-0")`

      High-performance model with extended thinking

    - `CLAUDE_4_SONNET_20250514("claude-4-sonnet-20250514")`

      High-performance model with extended thinking

    - `CLAUDE_SONNET_4_5("claude-sonnet-4-5")`

      Our best model for real-world agents and coding

    - `CLAUDE_SONNET_4_5_20250929("claude-sonnet-4-5-20250929")`

      Our best model for real-world agents and coding

    - `CLAUDE_OPUS_4_0("claude-opus-4-0")`

      Our most capable model

    - `CLAUDE_OPUS_4_20250514("claude-opus-4-20250514")`

      Our most capable model

    - `CLAUDE_4_OPUS_20250514("claude-4-opus-20250514")`

      Our most capable model

    - `CLAUDE_OPUS_4_1_20250805("claude-opus-4-1-20250805")`

      Our most capable model

    - `CLAUDE_3_OPUS_LATEST("claude-3-opus-latest")`

      Excels at writing and complex tasks

    - `CLAUDE_3_OPUS_20240229("claude-3-opus-20240229")`

      Excels at writing and complex tasks

    - `CLAUDE_3_HAIKU_20240307("claude-3-haiku-20240307")`

      Our previous most fast and cost-effective

  - `JsonValue; role "assistant"constant`

    Conversational role of the generated message.

    This will always be `"assistant"`.

    - `ASSISTANT("assistant")`

  - `Optional<StopReason> stopReason`

    The reason that we stopped.

    This may be one the following values:

    * `"end_turn"`: the model reached a natural stopping point
    * `"max_tokens"`: we exceeded the requested `max_tokens` or the model's maximum
    * `"stop_sequence"`: one of your provided custom `stop_sequences` was generated
    * `"tool_use"`: the model invoked one or more tools
    * `"pause_turn"`: we paused a long-running turn. You may provide the response back as-is in a subsequent request to let the model continue.
    * `"refusal"`: when streaming classifiers intervene to handle potential policy violations

    In non-streaming mode this value is always non-null. In streaming mode, it is null in the `message_start` event and non-null otherwise.

    - `END_TURN("end_turn")`

    - `MAX_TOKENS("max_tokens")`

    - `STOP_SEQUENCE("stop_sequence")`

    - `TOOL_USE("tool_use")`

    - `PAUSE_TURN("pause_turn")`

    - `REFUSAL("refusal")`

  - `Optional<String> stopSequence`

    Which custom stop sequence was generated, if any.

    This value will be a non-null string if one of your custom stop sequences was generated.

  - `JsonValue; type "message"constant`

    Object type.

    For Messages, this is always `"message"`.

    - `MESSAGE("message")`

  - `Usage usage`

    Billing and rate-limit usage.

    Anthropic's API bills and rate-limits by token counts, as tokens represent the underlying cost to our systems.

    Under the hood, the API transforms requests into a format suitable for the model. The model's output then goes through a parsing stage before becoming an API response. As a result, the token counts in `usage` will not match one-to-one with the exact visible content of an API request or response.

    For example, `output_tokens` will be non-zero, even for an empty string response from Claude.

    Total input tokens in a request is the summation of `input_tokens`, `cache_creation_input_tokens`, and `cache_read_input_tokens`.

    - `Optional<CacheCreation> cacheCreation`

      Breakdown of cached tokens by TTL

      - `long ephemeral1hInputTokens`

        The number of input tokens used to create the 1 hour cache entry.

      - `long ephemeral5mInputTokens`

        The number of input tokens used to create the 5 minute cache entry.

    - `Optional<Long> cacheCreationInputTokens`

      The number of input tokens used to create the cache entry.

    - `Optional<Long> cacheReadInputTokens`

      The number of input tokens read from the cache.

    - `Optional<String> inferenceGeo`

      The geographic region where inference was performed for this request.

    - `long inputTokens`

      The number of input tokens which were used.

    - `long outputTokens`

      The number of output tokens which were used.

    - `Optional<ServerToolUsage> serverToolUse`

      The number of server tool requests.

      - `long webFetchRequests`

        The number of web fetch tool requests.

      - `long webSearchRequests`

        The number of web search tool requests.

    - `Optional<ServiceTier> serviceTier`

      If the request used the priority, standard, or batch tier.

      - `STANDARD("standard")`

      - `PRIORITY("priority")`

      - `BATCH("batch")`

### Example

```java
package com.anthropic.example;

import com.anthropic.client.AnthropicClient;
import com.anthropic.client.okhttp.AnthropicOkHttpClient;
import com.anthropic.models.messages.Message;
import com.anthropic.models.messages.MessageCreateParams;
import com.anthropic.models.messages.Model;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        AnthropicClient client = AnthropicOkHttpClient.fromEnv();

        MessageCreateParams params = MessageCreateParams.builder()
            .maxTokens(1024L)
            .addUserMessage("Hello, world")
            .model(Model.CLAUDE_OPUS_4_6)
            .build();
        Message message = client.messages().create(params);
    }
}
```

## Count Tokens

`MessageTokensCount messages().countTokens(MessageCountTokensParamsparams, RequestOptionsrequestOptions = RequestOptions.none())`

**post** `/v1/messages/count_tokens`

Count the number of tokens in a Message.

The Token Count API can be used to count the number of tokens in a Message, including tools, images, and documents, without creating it.

Learn more about token counting in our [user guide](https://docs.claude.com/en/docs/build-with-claude/token-counting)

### Parameters

- `MessageCountTokensParams params`

  - `List<MessageParam> messages`

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

    - `Content content`

      - `String`

      - `List<ContentBlockParam>`

        - `class TextBlockParam:`

          - `String text`

          - `JsonValue; type "text"constant`

            - `TEXT("text")`

          - `Optional<CacheControlEphemeral> cacheControl`

            Create a cache control breakpoint at this content block.

            - `JsonValue; type "ephemeral"constant`

              - `EPHEMERAL("ephemeral")`

            - `Optional<Ttl> ttl`

              The time-to-live for the cache control breakpoint.

              This may be one the following values:

              - `5m`: 5 minutes
              - `1h`: 1 hour

              Defaults to `5m`.

              - `TTL_5M("5m")`

              - `TTL_1H("1h")`

          - `Optional<List<TextCitationParam>> citations`

            - `class CitationCharLocationParam:`

              - `String citedText`

              - `long documentIndex`

              - `Optional<String> documentTitle`

              - `long endCharIndex`

              - `long startCharIndex`

              - `JsonValue; type "char_location"constant`

                - `CHAR_LOCATION("char_location")`

            - `class CitationPageLocationParam:`

              - `String citedText`

              - `long documentIndex`

              - `Optional<String> documentTitle`

              - `long endPageNumber`

              - `long startPageNumber`

              - `JsonValue; type "page_location"constant`

                - `PAGE_LOCATION("page_location")`

            - `class CitationContentBlockLocationParam:`

              - `String citedText`

              - `long documentIndex`

              - `Optional<String> documentTitle`

              - `long endBlockIndex`

              - `long startBlockIndex`

              - `JsonValue; type "content_block_location"constant`

                - `CONTENT_BLOCK_LOCATION("content_block_location")`

            - `class CitationWebSearchResultLocationParam:`

              - `String citedText`

              - `String encryptedIndex`

              - `Optional<String> title`

              - `JsonValue; type "web_search_result_location"constant`

                - `WEB_SEARCH_RESULT_LOCATION("web_search_result_location")`

              - `String url`

            - `class CitationSearchResultLocationParam:`

              - `String citedText`

              - `long endBlockIndex`

              - `long searchResultIndex`

              - `String source`

              - `long startBlockIndex`

              - `Optional<String> title`

              - `JsonValue; type "search_result_location"constant`

                - `SEARCH_RESULT_LOCATION("search_result_location")`

        - `class ImageBlockParam:`

          - `Source source`

            - `class Base64ImageSource:`

              - `String data`

              - `MediaType mediaType`

                - `IMAGE_JPEG("image/jpeg")`

                - `IMAGE_PNG("image/png")`

                - `IMAGE_GIF("image/gif")`

                - `IMAGE_WEBP("image/webp")`

              - `JsonValue; type "base64"constant`

                - `BASE64("base64")`

            - `class UrlImageSource:`

              - `JsonValue; type "url"constant`

                - `URL("url")`

              - `String url`

          - `JsonValue; type "image"constant`

            - `IMAGE("image")`

          - `Optional<CacheControlEphemeral> cacheControl`

            Create a cache control breakpoint at this content block.

            - `JsonValue; type "ephemeral"constant`

              - `EPHEMERAL("ephemeral")`

            - `Optional<Ttl> ttl`

              The time-to-live for the cache control breakpoint.

              This may be one the following values:

              - `5m`: 5 minutes
              - `1h`: 1 hour

              Defaults to `5m`.

              - `TTL_5M("5m")`

              - `TTL_1H("1h")`

        - `class DocumentBlockParam:`

          - `Source source`

            - `class Base64PdfSource:`

              - `String data`

              - `JsonValue; mediaType "application/pdf"constant`

                - `APPLICATION_PDF("application/pdf")`

              - `JsonValue; type "base64"constant`

                - `BASE64("base64")`

            - `class PlainTextSource:`

              - `String data`

              - `JsonValue; mediaType "text/plain"constant`

                - `TEXT_PLAIN("text/plain")`

              - `JsonValue; type "text"constant`

                - `TEXT("text")`

            - `class ContentBlockSource:`

              - `Content content`

                - `String`

                - `List<ContentBlockSourceContent>`

                  - `class TextBlockParam:`

                    - `String text`

                    - `JsonValue; type "text"constant`

                      - `TEXT("text")`

                    - `Optional<CacheControlEphemeral> cacheControl`

                      Create a cache control breakpoint at this content block.

                      - `JsonValue; type "ephemeral"constant`

                        - `EPHEMERAL("ephemeral")`

                      - `Optional<Ttl> ttl`

                        The time-to-live for the cache control breakpoint.

                        This may be one the following values:

                        - `5m`: 5 minutes
                        - `1h`: 1 hour

                        Defaults to `5m`.

                        - `TTL_5M("5m")`

                        - `TTL_1H("1h")`

                    - `Optional<List<TextCitationParam>> citations`

                      - `class CitationCharLocationParam:`

                        - `String citedText`

                        - `long documentIndex`

                        - `Optional<String> documentTitle`

                        - `long endCharIndex`

                        - `long startCharIndex`

                        - `JsonValue; type "char_location"constant`

                          - `CHAR_LOCATION("char_location")`

                      - `class CitationPageLocationParam:`

                        - `String citedText`

                        - `long documentIndex`

                        - `Optional<String> documentTitle`

                        - `long endPageNumber`

                        - `long startPageNumber`

                        - `JsonValue; type "page_location"constant`

                          - `PAGE_LOCATION("page_location")`

                      - `class CitationContentBlockLocationParam:`

                        - `String citedText`

                        - `long documentIndex`

                        - `Optional<String> documentTitle`

                        - `long endBlockIndex`

                        - `long startBlockIndex`

                        - `JsonValue; type "content_block_location"constant`

                          - `CONTENT_BLOCK_LOCATION("content_block_location")`

                      - `class CitationWebSearchResultLocationParam:`

                        - `String citedText`

                        - `String encryptedIndex`

                        - `Optional<String> title`

                        - `JsonValue; type "web_search_result_location"constant`

                          - `WEB_SEARCH_RESULT_LOCATION("web_search_result_location")`

                        - `String url`

                      - `class CitationSearchResultLocationParam:`

                        - `String citedText`

                        - `long endBlockIndex`

                        - `long searchResultIndex`

                        - `String source`

                        - `long startBlockIndex`

                        - `Optional<String> title`

                        - `JsonValue; type "search_result_location"constant`

                          - `SEARCH_RESULT_LOCATION("search_result_location")`

                  - `class ImageBlockParam:`

                    - `Source source`

                      - `class Base64ImageSource:`

                        - `String data`

                        - `MediaType mediaType`

                          - `IMAGE_JPEG("image/jpeg")`

                          - `IMAGE_PNG("image/png")`

                          - `IMAGE_GIF("image/gif")`

                          - `IMAGE_WEBP("image/webp")`

                        - `JsonValue; type "base64"constant`

                          - `BASE64("base64")`

                      - `class UrlImageSource:`

                        - `JsonValue; type "url"constant`

                          - `URL("url")`

                        - `String url`

                    - `JsonValue; type "image"constant`

                      - `IMAGE("image")`

                    - `Optional<CacheControlEphemeral> cacheControl`

                      Create a cache control breakpoint at this content block.

                      - `JsonValue; type "ephemeral"constant`

                        - `EPHEMERAL("ephemeral")`

                      - `Optional<Ttl> ttl`

                        The time-to-live for the cache control breakpoint.

                        This may be one the following values:

                        - `5m`: 5 minutes
                        - `1h`: 1 hour

                        Defaults to `5m`.

                        - `TTL_5M("5m")`

                        - `TTL_1H("1h")`

              - `JsonValue; type "content"constant`

                - `CONTENT("content")`

            - `class UrlPdfSource:`

              - `JsonValue; type "url"constant`

                - `URL("url")`

              - `String url`

          - `JsonValue; type "document"constant`

            - `DOCUMENT("document")`

          - `Optional<CacheControlEphemeral> cacheControl`

            Create a cache control breakpoint at this content block.

            - `JsonValue; type "ephemeral"constant`

              - `EPHEMERAL("ephemeral")`

            - `Optional<Ttl> ttl`

              The time-to-live for the cache control breakpoint.

              This may be one the following values:

              - `5m`: 5 minutes
              - `1h`: 1 hour

              Defaults to `5m`.

              - `TTL_5M("5m")`

              - `TTL_1H("1h")`

          - `Optional<CitationsConfigParam> citations`

            - `Optional<Boolean> enabled`

          - `Optional<String> context`

          - `Optional<String> title`

        - `class SearchResultBlockParam:`

          - `List<TextBlockParam> content`

            - `String text`

            - `JsonValue; type "text"constant`

              - `TEXT("text")`

            - `Optional<CacheControlEphemeral> cacheControl`

              Create a cache control breakpoint at this content block.

              - `JsonValue; type "ephemeral"constant`

                - `EPHEMERAL("ephemeral")`

              - `Optional<Ttl> ttl`

                The time-to-live for the cache control breakpoint.

                This may be one the following values:

                - `5m`: 5 minutes
                - `1h`: 1 hour

                Defaults to `5m`.

                - `TTL_5M("5m")`

                - `TTL_1H("1h")`

            - `Optional<List<TextCitationParam>> citations`

              - `class CitationCharLocationParam:`

                - `String citedText`

                - `long documentIndex`

                - `Optional<String> documentTitle`

                - `long endCharIndex`

                - `long startCharIndex`

                - `JsonValue; type "char_location"constant`

                  - `CHAR_LOCATION("char_location")`

              - `class CitationPageLocationParam:`

                - `String citedText`

                - `long documentIndex`

                - `Optional<String> documentTitle`

                - `long endPageNumber`

                - `long startPageNumber`

                - `JsonValue; type "page_location"constant`

                  - `PAGE_LOCATION("page_location")`

              - `class CitationContentBlockLocationParam:`

                - `String citedText`

                - `long documentIndex`

                - `Optional<String> documentTitle`

                - `long endBlockIndex`

                - `long startBlockIndex`

                - `JsonValue; type "content_block_location"constant`

                  - `CONTENT_BLOCK_LOCATION("content_block_location")`

              - `class CitationWebSearchResultLocationParam:`

                - `String citedText`

                - `String encryptedIndex`

                - `Optional<String> title`

                - `JsonValue; type "web_search_result_location"constant`

                  - `WEB_SEARCH_RESULT_LOCATION("web_search_result_location")`

                - `String url`

              - `class CitationSearchResultLocationParam:`

                - `String citedText`

                - `long endBlockIndex`

                - `long searchResultIndex`

                - `String source`

                - `long startBlockIndex`

                - `Optional<String> title`

                - `JsonValue; type "search_result_location"constant`

                  - `SEARCH_RESULT_LOCATION("search_result_location")`

          - `String source`

          - `String title`

          - `JsonValue; type "search_result"constant`

            - `SEARCH_RESULT("search_result")`

          - `Optional<CacheControlEphemeral> cacheControl`

            Create a cache control breakpoint at this content block.

            - `JsonValue; type "ephemeral"constant`

              - `EPHEMERAL("ephemeral")`

            - `Optional<Ttl> ttl`

              The time-to-live for the cache control breakpoint.

              This may be one the following values:

              - `5m`: 5 minutes
              - `1h`: 1 hour

              Defaults to `5m`.

              - `TTL_5M("5m")`

              - `TTL_1H("1h")`

          - `Optional<CitationsConfigParam> citations`

            - `Optional<Boolean> enabled`

        - `class ThinkingBlockParam:`

          - `String signature`

          - `String thinking`

          - `JsonValue; type "thinking"constant`

            - `THINKING("thinking")`

        - `class RedactedThinkingBlockParam:`

          - `String data`

          - `JsonValue; type "redacted_thinking"constant`

            - `REDACTED_THINKING("redacted_thinking")`

        - `class ToolUseBlockParam:`

          - `String id`

          - `Input input`

          - `String name`

          - `JsonValue; type "tool_use"constant`

            - `TOOL_USE("tool_use")`

          - `Optional<CacheControlEphemeral> cacheControl`

            Create a cache control breakpoint at this content block.

            - `JsonValue; type "ephemeral"constant`

              - `EPHEMERAL("ephemeral")`

            - `Optional<Ttl> ttl`

              The time-to-live for the cache control breakpoint.

              This may be one the following values:

              - `5m`: 5 minutes
              - `1h`: 1 hour

              Defaults to `5m`.

              - `TTL_5M("5m")`

              - `TTL_1H("1h")`

          - `Optional<Caller> caller`

            Tool invocation directly from the model.

            - `class DirectCaller:`

              Tool invocation directly from the model.

              - `JsonValue; type "direct"constant`

                - `DIRECT("direct")`

            - `class ServerToolCaller:`

              Tool invocation generated by a server-side tool.

              - `String toolId`

              - `JsonValue; type "code_execution_20250825"constant`

                - `CODE_EXECUTION_20250825("code_execution_20250825")`

            - `class ServerToolCaller20260120:`

              - `String toolId`

              - `JsonValue; type "code_execution_20260120"constant`

                - `CODE_EXECUTION_20260120("code_execution_20260120")`

        - `class ToolResultBlockParam:`

          - `String toolUseId`

          - `JsonValue; type "tool_result"constant`

            - `TOOL_RESULT("tool_result")`

          - `Optional<CacheControlEphemeral> cacheControl`

            Create a cache control breakpoint at this content block.

            - `JsonValue; type "ephemeral"constant`

              - `EPHEMERAL("ephemeral")`

            - `Optional<Ttl> ttl`

              The time-to-live for the cache control breakpoint.

              This may be one the following values:

              - `5m`: 5 minutes
              - `1h`: 1 hour

              Defaults to `5m`.

              - `TTL_5M("5m")`

              - `TTL_1H("1h")`

          - `Optional<Content> content`

            - `String`

            - `List<Block>`

              - `class TextBlockParam:`

                - `String text`

                - `JsonValue; type "text"constant`

                  - `TEXT("text")`

                - `Optional<CacheControlEphemeral> cacheControl`

                  Create a cache control breakpoint at this content block.

                  - `JsonValue; type "ephemeral"constant`

                    - `EPHEMERAL("ephemeral")`

                  - `Optional<Ttl> ttl`

                    The time-to-live for the cache control breakpoint.

                    This may be one the following values:

                    - `5m`: 5 minutes
                    - `1h`: 1 hour

                    Defaults to `5m`.

                    - `TTL_5M("5m")`

                    - `TTL_1H("1h")`

                - `Optional<List<TextCitationParam>> citations`

                  - `class CitationCharLocationParam:`

                    - `String citedText`

                    - `long documentIndex`

                    - `Optional<String> documentTitle`

                    - `long endCharIndex`

                    - `long startCharIndex`

                    - `JsonValue; type "char_location"constant`

                      - `CHAR_LOCATION("char_location")`

                  - `class CitationPageLocationParam:`

                    - `String citedText`

                    - `long documentIndex`

                    - `Optional<String> documentTitle`

                    - `long endPageNumber`

                    - `long startPageNumber`

                    - `JsonValue; type "page_location"constant`

                      - `PAGE_LOCATION("page_location")`

                  - `class CitationContentBlockLocationParam:`

                    - `String citedText`

                    - `long documentIndex`

                    - `Optional<String> documentTitle`

                    - `long endBlockIndex`

                    - `long startBlockIndex`

                    - `JsonValue; type "content_block_location"constant`

                      - `CONTENT_BLOCK_LOCATION("content_block_location")`

                  - `class CitationWebSearchResultLocationParam:`

                    - `String citedText`

                    - `String encryptedIndex`

                    - `Optional<String> title`

                    - `JsonValue; type "web_search_result_location"constant`

                      - `WEB_SEARCH_RESULT_LOCATION("web_search_result_location")`

                    - `String url`

                  - `class CitationSearchResultLocationParam:`

                    - `String citedText`

                    - `long endBlockIndex`

                    - `long searchResultIndex`

                    - `String source`

                    - `long startBlockIndex`

                    - `Optional<String> title`

                    - `JsonValue; type "search_result_location"constant`

                      - `SEARCH_RESULT_LOCATION("search_result_location")`

              - `class ImageBlockParam:`

                - `Source source`

                  - `class Base64ImageSource:`

                    - `String data`

                    - `MediaType mediaType`

                      - `IMAGE_JPEG("image/jpeg")`

                      - `IMAGE_PNG("image/png")`

                      - `IMAGE_GIF("image/gif")`

                      - `IMAGE_WEBP("image/webp")`

                    - `JsonValue; type "base64"constant`

                      - `BASE64("base64")`

                  - `class UrlImageSource:`

                    - `JsonValue; type "url"constant`

                      - `URL("url")`

                    - `String url`

                - `JsonValue; type "image"constant`

                  - `IMAGE("image")`

                - `Optional<CacheControlEphemeral> cacheControl`

                  Create a cache control breakpoint at this content block.

                  - `JsonValue; type "ephemeral"constant`

                    - `EPHEMERAL("ephemeral")`

                  - `Optional<Ttl> ttl`

                    The time-to-live for the cache control breakpoint.

                    This may be one the following values:

                    - `5m`: 5 minutes
                    - `1h`: 1 hour

                    Defaults to `5m`.

                    - `TTL_5M("5m")`

                    - `TTL_1H("1h")`

              - `class SearchResultBlockParam:`

                - `List<TextBlockParam> content`

                  - `String text`

                  - `JsonValue; type "text"constant`

                    - `TEXT("text")`

                  - `Optional<CacheControlEphemeral> cacheControl`

                    Create a cache control breakpoint at this content block.

                    - `JsonValue; type "ephemeral"constant`

                      - `EPHEMERAL("ephemeral")`

                    - `Optional<Ttl> ttl`

                      The time-to-live for the cache control breakpoint.

                      This may be one the following values:

                      - `5m`: 5 minutes
                      - `1h`: 1 hour

                      Defaults to `5m`.

                      - `TTL_5M("5m")`

                      - `TTL_1H("1h")`

                  - `Optional<List<TextCitationParam>> citations`

                    - `class CitationCharLocationParam:`

                      - `String citedText`

                      - `long documentIndex`

                      - `Optional<String> documentTitle`

                      - `long endCharIndex`

                      - `long startCharIndex`

                      - `JsonValue; type "char_location"constant`

                        - `CHAR_LOCATION("char_location")`

                    - `class CitationPageLocationParam:`

                      - `String citedText`

                      - `long documentIndex`

                      - `Optional<String> documentTitle`

                      - `long endPageNumber`

                      - `long startPageNumber`

                      - `JsonValue; type "page_location"constant`

                        - `PAGE_LOCATION("page_location")`

                    - `class CitationContentBlockLocationParam:`

                      - `String citedText`

                      - `long documentIndex`

                      - `Optional<String> documentTitle`

                      - `long endBlockIndex`

                      - `long startBlockIndex`

                      - `JsonValue; type "content_block_location"constant`

                        - `CONTENT_BLOCK_LOCATION("content_block_location")`

                    - `class CitationWebSearchResultLocationParam:`

                      - `String citedText`

                      - `String encryptedIndex`

                      - `Optional<String> title`

                      - `JsonValue; type "web_search_result_location"constant`

                        - `WEB_SEARCH_RESULT_LOCATION("web_search_result_location")`

                      - `String url`

                    - `class CitationSearchResultLocationParam:`

                      - `String citedText`

                      - `long endBlockIndex`

                      - `long searchResultIndex`

                      - `String source`

                      - `long startBlockIndex`

                      - `Optional<String> title`

                      - `JsonValue; type "search_result_location"constant`

                        - `SEARCH_RESULT_LOCATION("search_result_location")`

                - `String source`

                - `String title`

                - `JsonValue; type "search_result"constant`

                  - `SEARCH_RESULT("search_result")`

                - `Optional<CacheControlEphemeral> cacheControl`

                  Create a cache control breakpoint at this content block.

                  - `JsonValue; type "ephemeral"constant`

                    - `EPHEMERAL("ephemeral")`

                  - `Optional<Ttl> ttl`

                    The time-to-live for the cache control breakpoint.

                    This may be one the following values:

                    - `5m`: 5 minutes
                    - `1h`: 1 hour

                    Defaults to `5m`.

                    - `TTL_5M("5m")`

                    - `TTL_1H("1h")`

                - `Optional<CitationsConfigParam> citations`

                  - `Optional<Boolean> enabled`

              - `class DocumentBlockParam:`

                - `Source source`

                  - `class Base64PdfSource:`

                    - `String data`

                    - `JsonValue; mediaType "application/pdf"constant`

                      - `APPLICATION_PDF("application/pdf")`

                    - `JsonValue; type "base64"constant`

                      - `BASE64("base64")`

                  - `class PlainTextSource:`

                    - `String data`

                    - `JsonValue; mediaType "text/plain"constant`

                      - `TEXT_PLAIN("text/plain")`

                    - `JsonValue; type "text"constant`

                      - `TEXT("text")`

                  - `class ContentBlockSource:`

                    - `Content content`

                      - `String`

                      - `List<ContentBlockSourceContent>`

                        - `class TextBlockParam:`

                          - `String text`

                          - `JsonValue; type "text"constant`

                            - `TEXT("text")`

                          - `Optional<CacheControlEphemeral> cacheControl`

                            Create a cache control breakpoint at this content block.

                            - `JsonValue; type "ephemeral"constant`

                              - `EPHEMERAL("ephemeral")`

                            - `Optional<Ttl> ttl`

                              The time-to-live for the cache control breakpoint.

                              This may be one the following values:

                              - `5m`: 5 minutes
                              - `1h`: 1 hour

                              Defaults to `5m`.

                              - `TTL_5M("5m")`

                              - `TTL_1H("1h")`

                          - `Optional<List<TextCitationParam>> citations`

                            - `class CitationCharLocationParam:`

                              - `String citedText`

                              - `long documentIndex`

                              - `Optional<String> documentTitle`

                              - `long endCharIndex`

                              - `long startCharIndex`

                              - `JsonValue; type "char_location"constant`

                                - `CHAR_LOCATION("char_location")`

                            - `class CitationPageLocationParam:`

                              - `String citedText`

                              - `long documentIndex`

                              - `Optional<String> documentTitle`

                              - `long endPageNumber`

                              - `long startPageNumber`

                              - `JsonValue; type "page_location"constant`

                                - `PAGE_LOCATION("page_location")`

                            - `class CitationContentBlockLocationParam:`

                              - `String citedText`

                              - `long documentIndex`

                              - `Optional<String> documentTitle`

                              - `long endBlockIndex`

                              - `long startBlockIndex`

                              - `JsonValue; type "content_block_location"constant`

                                - `CONTENT_BLOCK_LOCATION("content_block_location")`

                            - `class CitationWebSearchResultLocationParam:`

                              - `String citedText`

                              - `String encryptedIndex`

                              - `Optional<String> title`

                              - `JsonValue; type "web_search_result_location"constant`

                                - `WEB_SEARCH_RESULT_LOCATION("web_search_result_location")`

                              - `String url`

                            - `class CitationSearchResultLocationParam:`

                              - `String citedText`

                              - `long endBlockIndex`

                              - `long searchResultIndex`

                              - `String source`

                              - `long startBlockIndex`

                              - `Optional<String> title`

                              - `JsonValue; type "search_result_location"constant`

                                - `SEARCH_RESULT_LOCATION("search_result_location")`

                        - `class ImageBlockParam:`

                          - `Source source`

                            - `class Base64ImageSource:`

                              - `String data`

                              - `MediaType mediaType`

                                - `IMAGE_JPEG("image/jpeg")`

                                - `IMAGE_PNG("image/png")`

                                - `IMAGE_GIF("image/gif")`

                                - `IMAGE_WEBP("image/webp")`

                              - `JsonValue; type "base64"constant`

                                - `BASE64("base64")`

                            - `class UrlImageSource:`

                              - `JsonValue; type "url"constant`

                                - `URL("url")`

                              - `String url`

                          - `JsonValue; type "image"constant`

                            - `IMAGE("image")`

                          - `Optional<CacheControlEphemeral> cacheControl`

                            Create a cache control breakpoint at this content block.

                            - `JsonValue; type "ephemeral"constant`

                              - `EPHEMERAL("ephemeral")`

                            - `Optional<Ttl> ttl`

                              The time-to-live for the cache control breakpoint.

                              This may be one the following values:

                              - `5m`: 5 minutes
                              - `1h`: 1 hour

                              Defaults to `5m`.

                              - `TTL_5M("5m")`

                              - `TTL_1H("1h")`

                    - `JsonValue; type "content"constant`

                      - `CONTENT("content")`

                  - `class UrlPdfSource:`

                    - `JsonValue; type "url"constant`

                      - `URL("url")`

                    - `String url`

                - `JsonValue; type "document"constant`

                  - `DOCUMENT("document")`

                - `Optional<CacheControlEphemeral> cacheControl`

                  Create a cache control breakpoint at this content block.

                  - `JsonValue; type "ephemeral"constant`

                    - `EPHEMERAL("ephemeral")`

                  - `Optional<Ttl> ttl`

                    The time-to-live for the cache control breakpoint.

                    This may be one the following values:

                    - `5m`: 5 minutes
                    - `1h`: 1 hour

                    Defaults to `5m`.

                    - `TTL_5M("5m")`

                    - `TTL_1H("1h")`

                - `Optional<CitationsConfigParam> citations`

                  - `Optional<Boolean> enabled`

                - `Optional<String> context`

                - `Optional<String> title`

              - `class ToolReferenceBlockParam:`

                Tool reference block that can be included in tool_result content.

                - `String toolName`

                - `JsonValue; type "tool_reference"constant`

                  - `TOOL_REFERENCE("tool_reference")`

                - `Optional<CacheControlEphemeral> cacheControl`

                  Create a cache control breakpoint at this content block.

                  - `JsonValue; type "ephemeral"constant`

                    - `EPHEMERAL("ephemeral")`

                  - `Optional<Ttl> ttl`

                    The time-to-live for the cache control breakpoint.

                    This may be one the following values:

                    - `5m`: 5 minutes
                    - `1h`: 1 hour

                    Defaults to `5m`.

                    - `TTL_5M("5m")`

                    - `TTL_1H("1h")`

          - `Optional<Boolean> isError`

        - `class ServerToolUseBlockParam:`

          - `String id`

          - `Input input`

          - `Name name`

            - `WEB_SEARCH("web_search")`

            - `WEB_FETCH("web_fetch")`

            - `CODE_EXECUTION("code_execution")`

            - `BASH_CODE_EXECUTION("bash_code_execution")`

            - `TEXT_EDITOR_CODE_EXECUTION("text_editor_code_execution")`

            - `TOOL_SEARCH_TOOL_REGEX("tool_search_tool_regex")`

            - `TOOL_SEARCH_TOOL_BM25("tool_search_tool_bm25")`

          - `JsonValue; type "server_tool_use"constant`

            - `SERVER_TOOL_USE("server_tool_use")`

          - `Optional<CacheControlEphemeral> cacheControl`

            Create a cache control breakpoint at this content block.

            - `JsonValue; type "ephemeral"constant`

              - `EPHEMERAL("ephemeral")`

            - `Optional<Ttl> ttl`

              The time-to-live for the cache control breakpoint.

              This may be one the following values:

              - `5m`: 5 minutes
              - `1h`: 1 hour

              Defaults to `5m`.

              - `TTL_5M("5m")`

              - `TTL_1H("1h")`

          - `Optional<Caller> caller`

            Tool invocation directly from the model.

            - `class DirectCaller:`

              Tool invocation directly from the model.

              - `JsonValue; type "direct"constant`

                - `DIRECT("direct")`

            - `class ServerToolCaller:`

              Tool invocation generated by a server-side tool.

              - `String toolId`

              - `JsonValue; type "code_execution_20250825"constant`

                - `CODE_EXECUTION_20250825("code_execution_20250825")`

            - `class ServerToolCaller20260120:`

              - `String toolId`

              - `JsonValue; type "code_execution_20260120"constant`

                - `CODE_EXECUTION_20260120("code_execution_20260120")`

        - `class WebSearchToolResultBlockParam:`

          - `WebSearchToolResultBlockParamContent content`

            - `List<WebSearchResultBlockParam>`

              - `String encryptedContent`

              - `String title`

              - `JsonValue; type "web_search_result"constant`

                - `WEB_SEARCH_RESULT("web_search_result")`

              - `String url`

              - `Optional<String> pageAge`

            - `class WebSearchToolRequestError:`

              - `WebSearchToolResultErrorCode errorCode`

                - `INVALID_TOOL_INPUT("invalid_tool_input")`

                - `UNAVAILABLE("unavailable")`

                - `MAX_USES_EXCEEDED("max_uses_exceeded")`

                - `TOO_MANY_REQUESTS("too_many_requests")`

                - `QUERY_TOO_LONG("query_too_long")`

                - `REQUEST_TOO_LARGE("request_too_large")`

              - `JsonValue; type "web_search_tool_result_error"constant`

                - `WEB_SEARCH_TOOL_RESULT_ERROR("web_search_tool_result_error")`

          - `String toolUseId`

          - `JsonValue; type "web_search_tool_result"constant`

            - `WEB_SEARCH_TOOL_RESULT("web_search_tool_result")`

          - `Optional<CacheControlEphemeral> cacheControl`

            Create a cache control breakpoint at this content block.

            - `JsonValue; type "ephemeral"constant`

              - `EPHEMERAL("ephemeral")`

            - `Optional<Ttl> ttl`

              The time-to-live for the cache control breakpoint.

              This may be one the following values:

              - `5m`: 5 minutes
              - `1h`: 1 hour

              Defaults to `5m`.

              - `TTL_5M("5m")`

              - `TTL_1H("1h")`

          - `Optional<Caller> caller`

            Tool invocation directly from the model.

            - `class DirectCaller:`

              Tool invocation directly from the model.

              - `JsonValue; type "direct"constant`

                - `DIRECT("direct")`

            - `class ServerToolCaller:`

              Tool invocation generated by a server-side tool.

              - `String toolId`

              - `JsonValue; type "code_execution_20250825"constant`

                - `CODE_EXECUTION_20250825("code_execution_20250825")`

            - `class ServerToolCaller20260120:`

              - `String toolId`

              - `JsonValue; type "code_execution_20260120"constant`

                - `CODE_EXECUTION_20260120("code_execution_20260120")`

        - `class WebFetchToolResultBlockParam:`

          - `Content content`

            - `class WebFetchToolResultErrorBlockParam:`

              - `WebFetchToolResultErrorCode errorCode`

                - `INVALID_TOOL_INPUT("invalid_tool_input")`

                - `URL_TOO_LONG("url_too_long")`

                - `URL_NOT_ALLOWED("url_not_allowed")`

                - `URL_NOT_ACCESSIBLE("url_not_accessible")`

                - `UNSUPPORTED_CONTENT_TYPE("unsupported_content_type")`

                - `TOO_MANY_REQUESTS("too_many_requests")`

                - `MAX_USES_EXCEEDED("max_uses_exceeded")`

                - `UNAVAILABLE("unavailable")`

              - `JsonValue; type "web_fetch_tool_result_error"constant`

                - `WEB_FETCH_TOOL_RESULT_ERROR("web_fetch_tool_result_error")`

            - `class WebFetchBlockParam:`

              - `DocumentBlockParam content`

                - `Source source`

                  - `class Base64PdfSource:`

                    - `String data`

                    - `JsonValue; mediaType "application/pdf"constant`

                      - `APPLICATION_PDF("application/pdf")`

                    - `JsonValue; type "base64"constant`

                      - `BASE64("base64")`

                  - `class PlainTextSource:`

                    - `String data`

                    - `JsonValue; mediaType "text/plain"constant`

                      - `TEXT_PLAIN("text/plain")`

                    - `JsonValue; type "text"constant`

                      - `TEXT("text")`

                  - `class ContentBlockSource:`

                    - `Content content`

                      - `String`

                      - `List<ContentBlockSourceContent>`

                        - `class TextBlockParam:`

                          - `String text`

                          - `JsonValue; type "text"constant`

                            - `TEXT("text")`

                          - `Optional<CacheControlEphemeral> cacheControl`

                            Create a cache control breakpoint at this content block.

                            - `JsonValue; type "ephemeral"constant`

                              - `EPHEMERAL("ephemeral")`

                            - `Optional<Ttl> ttl`

                              The time-to-live for the cache control breakpoint.

                              This may be one the following values:

                              - `5m`: 5 minutes
                              - `1h`: 1 hour

                              Defaults to `5m`.

                              - `TTL_5M("5m")`

                              - `TTL_1H("1h")`

                          - `Optional<List<TextCitationParam>> citations`

                            - `class CitationCharLocationParam:`

                              - `String citedText`

                              - `long documentIndex`

                              - `Optional<String> documentTitle`

                              - `long endCharIndex`

                              - `long startCharIndex`

                              - `JsonValue; type "char_location"constant`

                                - `CHAR_LOCATION("char_location")`

                            - `class CitationPageLocationParam:`

                              - `String citedText`

                              - `long documentIndex`

                              - `Optional<String> documentTitle`

                              - `long endPageNumber`

                              - `long startPageNumber`

                              - `JsonValue; type "page_location"constant`

                                - `PAGE_LOCATION("page_location")`

                            - `class CitationContentBlockLocationParam:`

                              - `String citedText`

                              - `long documentIndex`

                              - `Optional<String> documentTitle`

                              - `long endBlockIndex`

                              - `long startBlockIndex`

                              - `JsonValue; type "content_block_location"constant`

                                - `CONTENT_BLOCK_LOCATION("content_block_location")`

                            - `class CitationWebSearchResultLocationParam:`

                              - `String citedText`

                              - `String encryptedIndex`

                              - `Optional<String> title`

                              - `JsonValue; type "web_search_result_location"constant`

                                - `WEB_SEARCH_RESULT_LOCATION("web_search_result_location")`

                              - `String url`

                            - `class CitationSearchResultLocationParam:`

                              - `String citedText`

                              - `long endBlockIndex`

                              - `long searchResultIndex`

                              - `String source`

                              - `long startBlockIndex`

                              - `Optional<String> title`

                              - `JsonValue; type "search_result_location"constant`

                                - `SEARCH_RESULT_LOCATION("search_result_location")`

                        - `class ImageBlockParam:`

                          - `Source source`

                            - `class Base64ImageSource:`

                              - `String data`

                              - `MediaType mediaType`

                                - `IMAGE_JPEG("image/jpeg")`

                                - `IMAGE_PNG("image/png")`

                                - `IMAGE_GIF("image/gif")`

                                - `IMAGE_WEBP("image/webp")`

                              - `JsonValue; type "base64"constant`

                                - `BASE64("base64")`

                            - `class UrlImageSource:`

                              - `JsonValue; type "url"constant`

                                - `URL("url")`

                              - `String url`

                          - `JsonValue; type "image"constant`

                            - `IMAGE("image")`

                          - `Optional<CacheControlEphemeral> cacheControl`

                            Create a cache control breakpoint at this content block.

                            - `JsonValue; type "ephemeral"constant`

                              - `EPHEMERAL("ephemeral")`

                            - `Optional<Ttl> ttl`

                              The time-to-live for the cache control breakpoint.

                              This may be one the following values:

                              - `5m`: 5 minutes
                              - `1h`: 1 hour

                              Defaults to `5m`.

                              - `TTL_5M("5m")`

                              - `TTL_1H("1h")`

                    - `JsonValue; type "content"constant`

                      - `CONTENT("content")`

                  - `class UrlPdfSource:`

                    - `JsonValue; type "url"constant`

                      - `URL("url")`

                    - `String url`

                - `JsonValue; type "document"constant`

                  - `DOCUMENT("document")`

                - `Optional<CacheControlEphemeral> cacheControl`

                  Create a cache control breakpoint at this content block.

                  - `JsonValue; type "ephemeral"constant`

                    - `EPHEMERAL("ephemeral")`

                  - `Optional<Ttl> ttl`

                    The time-to-live for the cache control breakpoint.

                    This may be one the following values:

                    - `5m`: 5 minutes
                    - `1h`: 1 hour

                    Defaults to `5m`.

                    - `TTL_5M("5m")`

                    - `TTL_1H("1h")`

                - `Optional<CitationsConfigParam> citations`

                  - `Optional<Boolean> enabled`

                - `Optional<String> context`

                - `Optional<String> title`

              - `JsonValue; type "web_fetch_result"constant`

                - `WEB_FETCH_RESULT("web_fetch_result")`

              - `String url`

                Fetched content URL

              - `Optional<String> retrievedAt`

                ISO 8601 timestamp when the content was retrieved

          - `String toolUseId`

          - `JsonValue; type "web_fetch_tool_result"constant`

            - `WEB_FETCH_TOOL_RESULT("web_fetch_tool_result")`

          - `Optional<CacheControlEphemeral> cacheControl`

            Create a cache control breakpoint at this content block.

            - `JsonValue; type "ephemeral"constant`

              - `EPHEMERAL("ephemeral")`

            - `Optional<Ttl> ttl`

              The time-to-live for the cache control breakpoint.

              This may be one the following values:

              - `5m`: 5 minutes
              - `1h`: 1 hour

              Defaults to `5m`.

              - `TTL_5M("5m")`

              - `TTL_1H("1h")`

          - `Optional<Caller> caller`

            Tool invocation directly from the model.

            - `class DirectCaller:`

              Tool invocation directly from the model.

              - `JsonValue; type "direct"constant`

                - `DIRECT("direct")`

            - `class ServerToolCaller:`

              Tool invocation generated by a server-side tool.

              - `String toolId`

              - `JsonValue; type "code_execution_20250825"constant`

                - `CODE_EXECUTION_20250825("code_execution_20250825")`

            - `class ServerToolCaller20260120:`

              - `String toolId`

              - `JsonValue; type "code_execution_20260120"constant`

                - `CODE_EXECUTION_20260120("code_execution_20260120")`

        - `class CodeExecutionToolResultBlockParam:`

          - `CodeExecutionToolResultBlockParamContent content`

            Code execution result with encrypted stdout for PFC + web_search results.

            - `class CodeExecutionToolResultErrorParam:`

              - `CodeExecutionToolResultErrorCode errorCode`

                - `INVALID_TOOL_INPUT("invalid_tool_input")`

                - `UNAVAILABLE("unavailable")`

                - `TOO_MANY_REQUESTS("too_many_requests")`

                - `EXECUTION_TIME_EXCEEDED("execution_time_exceeded")`

              - `JsonValue; type "code_execution_tool_result_error"constant`

                - `CODE_EXECUTION_TOOL_RESULT_ERROR("code_execution_tool_result_error")`

            - `class CodeExecutionResultBlockParam:`

              - `List<CodeExecutionOutputBlockParam> content`

                - `String fileId`

                - `JsonValue; type "code_execution_output"constant`

                  - `CODE_EXECUTION_OUTPUT("code_execution_output")`

              - `long returnCode`

              - `String stderr`

              - `String stdout`

              - `JsonValue; type "code_execution_result"constant`

                - `CODE_EXECUTION_RESULT("code_execution_result")`

            - `class EncryptedCodeExecutionResultBlockParam:`

              Code execution result with encrypted stdout for PFC + web_search results.

              - `List<CodeExecutionOutputBlockParam> content`

                - `String fileId`

                - `JsonValue; type "code_execution_output"constant`

                  - `CODE_EXECUTION_OUTPUT("code_execution_output")`

              - `String encryptedStdout`

              - `long returnCode`

              - `String stderr`

              - `JsonValue; type "encrypted_code_execution_result"constant`

                - `ENCRYPTED_CODE_EXECUTION_RESULT("encrypted_code_execution_result")`

          - `String toolUseId`

          - `JsonValue; type "code_execution_tool_result"constant`

            - `CODE_EXECUTION_TOOL_RESULT("code_execution_tool_result")`

          - `Optional<CacheControlEphemeral> cacheControl`

            Create a cache control breakpoint at this content block.

            - `JsonValue; type "ephemeral"constant`

              - `EPHEMERAL("ephemeral")`

            - `Optional<Ttl> ttl`

              The time-to-live for the cache control breakpoint.

              This may be one the following values:

              - `5m`: 5 minutes
              - `1h`: 1 hour

              Defaults to `5m`.

              - `TTL_5M("5m")`

              - `TTL_1H("1h")`

        - `class BashCodeExecutionToolResultBlockParam:`

          - `Content content`

            - `class BashCodeExecutionToolResultErrorParam:`

              - `BashCodeExecutionToolResultErrorCode errorCode`

                - `INVALID_TOOL_INPUT("invalid_tool_input")`

                - `UNAVAILABLE("unavailable")`

                - `TOO_MANY_REQUESTS("too_many_requests")`

                - `EXECUTION_TIME_EXCEEDED("execution_time_exceeded")`

                - `OUTPUT_FILE_TOO_LARGE("output_file_too_large")`

              - `JsonValue; type "bash_code_execution_tool_result_error"constant`

                - `BASH_CODE_EXECUTION_TOOL_RESULT_ERROR("bash_code_execution_tool_result_error")`

            - `class BashCodeExecutionResultBlockParam:`

              - `List<BashCodeExecutionOutputBlockParam> content`

                - `String fileId`

                - `JsonValue; type "bash_code_execution_output"constant`

                  - `BASH_CODE_EXECUTION_OUTPUT("bash_code_execution_output")`

              - `long returnCode`

              - `String stderr`

              - `String stdout`

              - `JsonValue; type "bash_code_execution_result"constant`

                - `BASH_CODE_EXECUTION_RESULT("bash_code_execution_result")`

          - `String toolUseId`

          - `JsonValue; type "bash_code_execution_tool_result"constant`

            - `BASH_CODE_EXECUTION_TOOL_RESULT("bash_code_execution_tool_result")`

          - `Optional<CacheControlEphemeral> cacheControl`

            Create a cache control breakpoint at this content block.

            - `JsonValue; type "ephemeral"constant`

              - `EPHEMERAL("ephemeral")`

            - `Optional<Ttl> ttl`

              The time-to-live for the cache control breakpoint.

              This may be one the following values:

              - `5m`: 5 minutes
              - `1h`: 1 hour

              Defaults to `5m`.

              - `TTL_5M("5m")`

              - `TTL_1H("1h")`

        - `class TextEditorCodeExecutionToolResultBlockParam:`

          - `Content content`

            - `class TextEditorCodeExecutionToolResultErrorParam:`

              - `TextEditorCodeExecutionToolResultErrorCode errorCode`

                - `INVALID_TOOL_INPUT("invalid_tool_input")`

                - `UNAVAILABLE("unavailable")`

                - `TOO_MANY_REQUESTS("too_many_requests")`

                - `EXECUTION_TIME_EXCEEDED("execution_time_exceeded")`

                - `FILE_NOT_FOUND("file_not_found")`

              - `JsonValue; type "text_editor_code_execution_tool_result_error"constant`

                - `TEXT_EDITOR_CODE_EXECUTION_TOOL_RESULT_ERROR("text_editor_code_execution_tool_result_error")`

              - `Optional<String> errorMessage`

            - `class TextEditorCodeExecutionViewResultBlockParam:`

              - `String content`

              - `FileType fileType`

                - `TEXT("text")`

                - `IMAGE("image")`

                - `PDF("pdf")`

              - `JsonValue; type "text_editor_code_execution_view_result"constant`

                - `TEXT_EDITOR_CODE_EXECUTION_VIEW_RESULT("text_editor_code_execution_view_result")`

              - `Optional<Long> numLines`

              - `Optional<Long> startLine`

              - `Optional<Long> totalLines`

            - `class TextEditorCodeExecutionCreateResultBlockParam:`

              - `boolean isFileUpdate`

              - `JsonValue; type "text_editor_code_execution_create_result"constant`

                - `TEXT_EDITOR_CODE_EXECUTION_CREATE_RESULT("text_editor_code_execution_create_result")`

            - `class TextEditorCodeExecutionStrReplaceResultBlockParam:`

              - `JsonValue; type "text_editor_code_execution_str_replace_result"constant`

                - `TEXT_EDITOR_CODE_EXECUTION_STR_REPLACE_RESULT("text_editor_code_execution_str_replace_result")`

              - `Optional<List<String>> lines`

              - `Optional<Long> newLines`

              - `Optional<Long> newStart`

              - `Optional<Long> oldLines`

              - `Optional<Long> oldStart`

          - `String toolUseId`

          - `JsonValue; type "text_editor_code_execution_tool_result"constant`

            - `TEXT_EDITOR_CODE_EXECUTION_TOOL_RESULT("text_editor_code_execution_tool_result")`

          - `Optional<CacheControlEphemeral> cacheControl`

            Create a cache control breakpoint at this content block.

            - `JsonValue; type "ephemeral"constant`

              - `EPHEMERAL("ephemeral")`

            - `Optional<Ttl> ttl`

              The time-to-live for the cache control breakpoint.

              This may be one the following values:

              - `5m`: 5 minutes
              - `1h`: 1 hour

              Defaults to `5m`.

              - `TTL_5M("5m")`

              - `TTL_1H("1h")`

        - `class ToolSearchToolResultBlockParam:`

          - `Content content`

            - `class ToolSearchToolResultErrorParam:`

              - `ToolSearchToolResultErrorCode errorCode`

                - `INVALID_TOOL_INPUT("invalid_tool_input")`

                - `UNAVAILABLE("unavailable")`

                - `TOO_MANY_REQUESTS("too_many_requests")`

                - `EXECUTION_TIME_EXCEEDED("execution_time_exceeded")`

              - `JsonValue; type "tool_search_tool_result_error"constant`

                - `TOOL_SEARCH_TOOL_RESULT_ERROR("tool_search_tool_result_error")`

            - `class ToolSearchToolSearchResultBlockParam:`

              - `List<ToolReferenceBlockParam> toolReferences`

                - `String toolName`

                - `JsonValue; type "tool_reference"constant`

                  - `TOOL_REFERENCE("tool_reference")`

                - `Optional<CacheControlEphemeral> cacheControl`

                  Create a cache control breakpoint at this content block.

                  - `JsonValue; type "ephemeral"constant`

                    - `EPHEMERAL("ephemeral")`

                  - `Optional<Ttl> ttl`

                    The time-to-live for the cache control breakpoint.

                    This may be one the following values:

                    - `5m`: 5 minutes
                    - `1h`: 1 hour

                    Defaults to `5m`.

                    - `TTL_5M("5m")`

                    - `TTL_1H("1h")`

              - `JsonValue; type "tool_search_tool_search_result"constant`

                - `TOOL_SEARCH_TOOL_SEARCH_RESULT("tool_search_tool_search_result")`

          - `String toolUseId`

          - `JsonValue; type "tool_search_tool_result"constant`

            - `TOOL_SEARCH_TOOL_RESULT("tool_search_tool_result")`

          - `Optional<CacheControlEphemeral> cacheControl`

            Create a cache control breakpoint at this content block.

            - `JsonValue; type "ephemeral"constant`

              - `EPHEMERAL("ephemeral")`

            - `Optional<Ttl> ttl`

              The time-to-live for the cache control breakpoint.

              This may be one the following values:

              - `5m`: 5 minutes
              - `1h`: 1 hour

              Defaults to `5m`.

              - `TTL_5M("5m")`

              - `TTL_1H("1h")`

        - `class ContainerUploadBlockParam:`

          A content block that represents a file to be uploaded to the container
          Files uploaded via this block will be available in the container's input directory.

          - `String fileId`

          - `JsonValue; type "container_upload"constant`

            - `CONTAINER_UPLOAD("container_upload")`

          - `Optional<CacheControlEphemeral> cacheControl`

            Create a cache control breakpoint at this content block.

            - `JsonValue; type "ephemeral"constant`

              - `EPHEMERAL("ephemeral")`

            - `Optional<Ttl> ttl`

              The time-to-live for the cache control breakpoint.

              This may be one the following values:

              - `5m`: 5 minutes
              - `1h`: 1 hour

              Defaults to `5m`.

              - `TTL_5M("5m")`

              - `TTL_1H("1h")`

    - `Role role`

      - `USER("user")`

      - `ASSISTANT("assistant")`

  - `Model model`

    The model that will complete your prompt.

    See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

  - `Optional<CacheControlEphemeral> cacheControl`

    Top-level cache control automatically applies a cache_control marker to the last cacheable block in the request.

  - `Optional<OutputConfig> outputConfig`

    Configuration options for the model's output, such as the output format.

  - `Optional<System> system`

    System prompt.

    A system prompt is a way of providing context and instructions to Claude, such as specifying a particular goal or role. See our [guide to system prompts](https://docs.claude.com/en/docs/system-prompts).

    - `String`

    - `List<TextBlockParam>`

      - `String text`

      - `JsonValue; type "text"constant`

        - `TEXT("text")`

      - `Optional<CacheControlEphemeral> cacheControl`

        Create a cache control breakpoint at this content block.

        - `JsonValue; type "ephemeral"constant`

          - `EPHEMERAL("ephemeral")`

        - `Optional<Ttl> ttl`

          The time-to-live for the cache control breakpoint.

          This may be one the following values:

          - `5m`: 5 minutes
          - `1h`: 1 hour

          Defaults to `5m`.

          - `TTL_5M("5m")`

          - `TTL_1H("1h")`

      - `Optional<List<TextCitationParam>> citations`

        - `class CitationCharLocationParam:`

          - `String citedText`

          - `long documentIndex`

          - `Optional<String> documentTitle`

          - `long endCharIndex`

          - `long startCharIndex`

          - `JsonValue; type "char_location"constant`

            - `CHAR_LOCATION("char_location")`

        - `class CitationPageLocationParam:`

          - `String citedText`

          - `long documentIndex`

          - `Optional<String> documentTitle`

          - `long endPageNumber`

          - `long startPageNumber`

          - `JsonValue; type "page_location"constant`

            - `PAGE_LOCATION("page_location")`

        - `class CitationContentBlockLocationParam:`

          - `String citedText`

          - `long documentIndex`

          - `Optional<String> documentTitle`

          - `long endBlockIndex`

          - `long startBlockIndex`

          - `JsonValue; type "content_block_location"constant`

            - `CONTENT_BLOCK_LOCATION("content_block_location")`

        - `class CitationWebSearchResultLocationParam:`

          - `String citedText`

          - `String encryptedIndex`

          - `Optional<String> title`

          - `JsonValue; type "web_search_result_location"constant`

            - `WEB_SEARCH_RESULT_LOCATION("web_search_result_location")`

          - `String url`

        - `class CitationSearchResultLocationParam:`

          - `String citedText`

          - `long endBlockIndex`

          - `long searchResultIndex`

          - `String source`

          - `long startBlockIndex`

          - `Optional<String> title`

          - `JsonValue; type "search_result_location"constant`

            - `SEARCH_RESULT_LOCATION("search_result_location")`

  - `Optional<ThinkingConfigParam> thinking`

    Configuration for enabling Claude's extended thinking.

    When enabled, responses include `thinking` content blocks showing Claude's thinking process before the final answer. Requires a minimum budget of 1,024 tokens and counts towards your `max_tokens` limit.

    See [extended thinking](https://docs.claude.com/en/docs/build-with-claude/extended-thinking) for details.

  - `Optional<ToolChoice> toolChoice`

    How the model should use the provided tools. The model can use a specific tool, any available tool, decide by itself, or not use tools at all.

  - `Optional<List<MessageCountTokensTool>> tools`

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

    - `class Tool:`

      - `InputSchema inputSchema`

        [JSON schema](https://json-schema.org/draft/2020-12) for this tool's input.

        This defines the shape of the `input` that your tool accepts and that the model will produce.

        - `JsonValue; type "object"constant`

          - `OBJECT("object")`

        - `Optional<Properties> properties`

        - `Optional<List<String>> required`

      - `String name`

        Name of the tool.

        This is how the tool will be called by the model and in `tool_use` blocks.

      - `Optional<List<AllowedCaller>> allowedCallers`

        - `DIRECT("direct")`

        - `CODE_EXECUTION_20250825("code_execution_20250825")`

        - `CODE_EXECUTION_20260120("code_execution_20260120")`

      - `Optional<CacheControlEphemeral> cacheControl`

        Create a cache control breakpoint at this content block.

        - `JsonValue; type "ephemeral"constant`

          - `EPHEMERAL("ephemeral")`

        - `Optional<Ttl> ttl`

          The time-to-live for the cache control breakpoint.

          This may be one the following values:

          - `5m`: 5 minutes
          - `1h`: 1 hour

          Defaults to `5m`.

          - `TTL_5M("5m")`

          - `TTL_1H("1h")`

      - `Optional<Boolean> deferLoading`

        If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

      - `Optional<String> description`

        Description of what this tool does.

        Tool descriptions should be as detailed as possible. The more information that the model has about what the tool is and how to use it, the better it will perform. You can use natural language descriptions to reinforce important aspects of the tool input JSON schema.

      - `Optional<Boolean> eagerInputStreaming`

        Enable eager input streaming for this tool. When true, tool input parameters will be streamed incrementally as they are generated, and types will be inferred on-the-fly rather than buffering the full JSON output. When false, streaming is disabled for this tool even if the fine-grained-tool-streaming beta is active. When null (default), uses the default behavior based on beta headers.

      - `Optional<List<InputExample>> inputExamples`

      - `Optional<Boolean> strict`

        When true, guarantees schema validation on tool names and inputs

      - `Optional<Type> type`

        - `CUSTOM("custom")`

    - `class ToolBash20250124:`

      - `JsonValue; name "bash"constant`

        Name of the tool.

        This is how the tool will be called by the model and in `tool_use` blocks.

        - `BASH("bash")`

      - `JsonValue; type "bash_20250124"constant`

        - `BASH_20250124("bash_20250124")`

      - `Optional<List<AllowedCaller>> allowedCallers`

        - `DIRECT("direct")`

        - `CODE_EXECUTION_20250825("code_execution_20250825")`

        - `CODE_EXECUTION_20260120("code_execution_20260120")`

      - `Optional<CacheControlEphemeral> cacheControl`

        Create a cache control breakpoint at this content block.

        - `JsonValue; type "ephemeral"constant`

          - `EPHEMERAL("ephemeral")`

        - `Optional<Ttl> ttl`

          The time-to-live for the cache control breakpoint.

          This may be one the following values:

          - `5m`: 5 minutes
          - `1h`: 1 hour

          Defaults to `5m`.

          - `TTL_5M("5m")`

          - `TTL_1H("1h")`

      - `Optional<Boolean> deferLoading`

        If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

      - `Optional<List<InputExample>> inputExamples`

      - `Optional<Boolean> strict`

        When true, guarantees schema validation on tool names and inputs

    - `class CodeExecutionTool20250522:`

      - `JsonValue; name "code_execution"constant`

        Name of the tool.

        This is how the tool will be called by the model and in `tool_use` blocks.

        - `CODE_EXECUTION("code_execution")`

      - `JsonValue; type "code_execution_20250522"constant`

        - `CODE_EXECUTION_20250522("code_execution_20250522")`

      - `Optional<List<AllowedCaller>> allowedCallers`

        - `DIRECT("direct")`

        - `CODE_EXECUTION_20250825("code_execution_20250825")`

        - `CODE_EXECUTION_20260120("code_execution_20260120")`

      - `Optional<CacheControlEphemeral> cacheControl`

        Create a cache control breakpoint at this content block.

        - `JsonValue; type "ephemeral"constant`

          - `EPHEMERAL("ephemeral")`

        - `Optional<Ttl> ttl`

          The time-to-live for the cache control breakpoint.

          This may be one the following values:

          - `5m`: 5 minutes
          - `1h`: 1 hour

          Defaults to `5m`.

          - `TTL_5M("5m")`

          - `TTL_1H("1h")`

      - `Optional<Boolean> deferLoading`

        If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

      - `Optional<Boolean> strict`

        When true, guarantees schema validation on tool names and inputs

    - `class CodeExecutionTool20250825:`

      - `JsonValue; name "code_execution"constant`

        Name of the tool.

        This is how the tool will be called by the model and in `tool_use` blocks.

        - `CODE_EXECUTION("code_execution")`

      - `JsonValue; type "code_execution_20250825"constant`

        - `CODE_EXECUTION_20250825("code_execution_20250825")`

      - `Optional<List<AllowedCaller>> allowedCallers`

        - `DIRECT("direct")`

        - `CODE_EXECUTION_20250825("code_execution_20250825")`

        - `CODE_EXECUTION_20260120("code_execution_20260120")`

      - `Optional<CacheControlEphemeral> cacheControl`

        Create a cache control breakpoint at this content block.

        - `JsonValue; type "ephemeral"constant`

          - `EPHEMERAL("ephemeral")`

        - `Optional<Ttl> ttl`

          The time-to-live for the cache control breakpoint.

          This may be one the following values:

          - `5m`: 5 minutes
          - `1h`: 1 hour

          Defaults to `5m`.

          - `TTL_5M("5m")`

          - `TTL_1H("1h")`

      - `Optional<Boolean> deferLoading`

        If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

      - `Optional<Boolean> strict`

        When true, guarantees schema validation on tool names and inputs

    - `class CodeExecutionTool20260120:`

      Code execution tool with REPL state persistence (daemon mode + gVisor checkpoint).

      - `JsonValue; name "code_execution"constant`

        Name of the tool.

        This is how the tool will be called by the model and in `tool_use` blocks.

        - `CODE_EXECUTION("code_execution")`

      - `JsonValue; type "code_execution_20260120"constant`

        - `CODE_EXECUTION_20260120("code_execution_20260120")`

      - `Optional<List<AllowedCaller>> allowedCallers`

        - `DIRECT("direct")`

        - `CODE_EXECUTION_20250825("code_execution_20250825")`

        - `CODE_EXECUTION_20260120("code_execution_20260120")`

      - `Optional<CacheControlEphemeral> cacheControl`

        Create a cache control breakpoint at this content block.

        - `JsonValue; type "ephemeral"constant`

          - `EPHEMERAL("ephemeral")`

        - `Optional<Ttl> ttl`

          The time-to-live for the cache control breakpoint.

          This may be one the following values:

          - `5m`: 5 minutes
          - `1h`: 1 hour

          Defaults to `5m`.

          - `TTL_5M("5m")`

          - `TTL_1H("1h")`

      - `Optional<Boolean> deferLoading`

        If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

      - `Optional<Boolean> strict`

        When true, guarantees schema validation on tool names and inputs

    - `class MemoryTool20250818:`

      - `JsonValue; name "memory"constant`

        Name of the tool.

        This is how the tool will be called by the model and in `tool_use` blocks.

        - `MEMORY("memory")`

      - `JsonValue; type "memory_20250818"constant`

        - `MEMORY_20250818("memory_20250818")`

      - `Optional<List<AllowedCaller>> allowedCallers`

        - `DIRECT("direct")`

        - `CODE_EXECUTION_20250825("code_execution_20250825")`

        - `CODE_EXECUTION_20260120("code_execution_20260120")`

      - `Optional<CacheControlEphemeral> cacheControl`

        Create a cache control breakpoint at this content block.

        - `JsonValue; type "ephemeral"constant`

          - `EPHEMERAL("ephemeral")`

        - `Optional<Ttl> ttl`

          The time-to-live for the cache control breakpoint.

          This may be one the following values:

          - `5m`: 5 minutes
          - `1h`: 1 hour

          Defaults to `5m`.

          - `TTL_5M("5m")`

          - `TTL_1H("1h")`

      - `Optional<Boolean> deferLoading`

        If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

      - `Optional<List<InputExample>> inputExamples`

      - `Optional<Boolean> strict`

        When true, guarantees schema validation on tool names and inputs

    - `class ToolTextEditor20250124:`

      - `JsonValue; name "str_replace_editor"constant`

        Name of the tool.

        This is how the tool will be called by the model and in `tool_use` blocks.

        - `STR_REPLACE_EDITOR("str_replace_editor")`

      - `JsonValue; type "text_editor_20250124"constant`

        - `TEXT_EDITOR_20250124("text_editor_20250124")`

      - `Optional<List<AllowedCaller>> allowedCallers`

        - `DIRECT("direct")`

        - `CODE_EXECUTION_20250825("code_execution_20250825")`

        - `CODE_EXECUTION_20260120("code_execution_20260120")`

      - `Optional<CacheControlEphemeral> cacheControl`

        Create a cache control breakpoint at this content block.

        - `JsonValue; type "ephemeral"constant`

          - `EPHEMERAL("ephemeral")`

        - `Optional<Ttl> ttl`

          The time-to-live for the cache control breakpoint.

          This may be one the following values:

          - `5m`: 5 minutes
          - `1h`: 1 hour

          Defaults to `5m`.

          - `TTL_5M("5m")`

          - `TTL_1H("1h")`

      - `Optional<Boolean> deferLoading`

        If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

      - `Optional<List<InputExample>> inputExamples`

      - `Optional<Boolean> strict`

        When true, guarantees schema validation on tool names and inputs

    - `class ToolTextEditor20250429:`

      - `JsonValue; name "str_replace_based_edit_tool"constant`

        Name of the tool.

        This is how the tool will be called by the model and in `tool_use` blocks.

        - `STR_REPLACE_BASED_EDIT_TOOL("str_replace_based_edit_tool")`

      - `JsonValue; type "text_editor_20250429"constant`

        - `TEXT_EDITOR_20250429("text_editor_20250429")`

      - `Optional<List<AllowedCaller>> allowedCallers`

        - `DIRECT("direct")`

        - `CODE_EXECUTION_20250825("code_execution_20250825")`

        - `CODE_EXECUTION_20260120("code_execution_20260120")`

      - `Optional<CacheControlEphemeral> cacheControl`

        Create a cache control breakpoint at this content block.

        - `JsonValue; type "ephemeral"constant`

          - `EPHEMERAL("ephemeral")`

        - `Optional<Ttl> ttl`

          The time-to-live for the cache control breakpoint.

          This may be one the following values:

          - `5m`: 5 minutes
          - `1h`: 1 hour

          Defaults to `5m`.

          - `TTL_5M("5m")`

          - `TTL_1H("1h")`

      - `Optional<Boolean> deferLoading`

        If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

      - `Optional<List<InputExample>> inputExamples`

      - `Optional<Boolean> strict`

        When true, guarantees schema validation on tool names and inputs

    - `class ToolTextEditor20250728:`

      - `JsonValue; name "str_replace_based_edit_tool"constant`

        Name of the tool.

        This is how the tool will be called by the model and in `tool_use` blocks.

        - `STR_REPLACE_BASED_EDIT_TOOL("str_replace_based_edit_tool")`

      - `JsonValue; type "text_editor_20250728"constant`

        - `TEXT_EDITOR_20250728("text_editor_20250728")`

      - `Optional<List<AllowedCaller>> allowedCallers`

        - `DIRECT("direct")`

        - `CODE_EXECUTION_20250825("code_execution_20250825")`

        - `CODE_EXECUTION_20260120("code_execution_20260120")`

      - `Optional<CacheControlEphemeral> cacheControl`

        Create a cache control breakpoint at this content block.

        - `JsonValue; type "ephemeral"constant`

          - `EPHEMERAL("ephemeral")`

        - `Optional<Ttl> ttl`

          The time-to-live for the cache control breakpoint.

          This may be one the following values:

          - `5m`: 5 minutes
          - `1h`: 1 hour

          Defaults to `5m`.

          - `TTL_5M("5m")`

          - `TTL_1H("1h")`

      - `Optional<Boolean> deferLoading`

        If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

      - `Optional<List<InputExample>> inputExamples`

      - `Optional<Long> maxCharacters`

        Maximum number of characters to display when viewing a file. If not specified, defaults to displaying the full file.

      - `Optional<Boolean> strict`

        When true, guarantees schema validation on tool names and inputs

    - `class WebSearchTool20250305:`

      - `JsonValue; name "web_search"constant`

        Name of the tool.

        This is how the tool will be called by the model and in `tool_use` blocks.

        - `WEB_SEARCH("web_search")`

      - `JsonValue; type "web_search_20250305"constant`

        - `WEB_SEARCH_20250305("web_search_20250305")`

      - `Optional<List<AllowedCaller>> allowedCallers`

        - `DIRECT("direct")`

        - `CODE_EXECUTION_20250825("code_execution_20250825")`

        - `CODE_EXECUTION_20260120("code_execution_20260120")`

      - `Optional<List<String>> allowedDomains`

        If provided, only these domains will be included in results. Cannot be used alongside `blocked_domains`.

      - `Optional<List<String>> blockedDomains`

        If provided, these domains will never appear in results. Cannot be used alongside `allowed_domains`.

      - `Optional<CacheControlEphemeral> cacheControl`

        Create a cache control breakpoint at this content block.

        - `JsonValue; type "ephemeral"constant`

          - `EPHEMERAL("ephemeral")`

        - `Optional<Ttl> ttl`

          The time-to-live for the cache control breakpoint.

          This may be one the following values:

          - `5m`: 5 minutes
          - `1h`: 1 hour

          Defaults to `5m`.

          - `TTL_5M("5m")`

          - `TTL_1H("1h")`

      - `Optional<Boolean> deferLoading`

        If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

      - `Optional<Long> maxUses`

        Maximum number of times the tool can be used in the API request.

      - `Optional<Boolean> strict`

        When true, guarantees schema validation on tool names and inputs

      - `Optional<UserLocation> userLocation`

        Parameters for the user's location. Used to provide more relevant search results.

        - `JsonValue; type "approximate"constant`

          - `APPROXIMATE("approximate")`

        - `Optional<String> city`

          The city of the user.

        - `Optional<String> country`

          The two letter [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) of the user.

        - `Optional<String> region`

          The region of the user.

        - `Optional<String> timezone`

          The [IANA timezone](https://nodatime.org/TimeZones) of the user.

    - `class WebFetchTool20250910:`

      - `JsonValue; name "web_fetch"constant`

        Name of the tool.

        This is how the tool will be called by the model and in `tool_use` blocks.

        - `WEB_FETCH("web_fetch")`

      - `JsonValue; type "web_fetch_20250910"constant`

        - `WEB_FETCH_20250910("web_fetch_20250910")`

      - `Optional<List<AllowedCaller>> allowedCallers`

        - `DIRECT("direct")`

        - `CODE_EXECUTION_20250825("code_execution_20250825")`

        - `CODE_EXECUTION_20260120("code_execution_20260120")`

      - `Optional<List<String>> allowedDomains`

        List of domains to allow fetching from

      - `Optional<List<String>> blockedDomains`

        List of domains to block fetching from

      - `Optional<CacheControlEphemeral> cacheControl`

        Create a cache control breakpoint at this content block.

        - `JsonValue; type "ephemeral"constant`

          - `EPHEMERAL("ephemeral")`

        - `Optional<Ttl> ttl`

          The time-to-live for the cache control breakpoint.

          This may be one the following values:

          - `5m`: 5 minutes
          - `1h`: 1 hour

          Defaults to `5m`.

          - `TTL_5M("5m")`

          - `TTL_1H("1h")`

      - `Optional<CitationsConfigParam> citations`

        Citations configuration for fetched documents. Citations are disabled by default.

        - `Optional<Boolean> enabled`

      - `Optional<Boolean> deferLoading`

        If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

      - `Optional<Long> maxContentTokens`

        Maximum number of tokens used by including web page text content in the context. The limit is approximate and does not apply to binary content such as PDFs.

      - `Optional<Long> maxUses`

        Maximum number of times the tool can be used in the API request.

      - `Optional<Boolean> strict`

        When true, guarantees schema validation on tool names and inputs

    - `class WebSearchTool20260209:`

      - `JsonValue; name "web_search"constant`

        Name of the tool.

        This is how the tool will be called by the model and in `tool_use` blocks.

        - `WEB_SEARCH("web_search")`

      - `JsonValue; type "web_search_20260209"constant`

        - `WEB_SEARCH_20260209("web_search_20260209")`

      - `Optional<List<AllowedCaller>> allowedCallers`

        - `DIRECT("direct")`

        - `CODE_EXECUTION_20250825("code_execution_20250825")`

        - `CODE_EXECUTION_20260120("code_execution_20260120")`

      - `Optional<List<String>> allowedDomains`

        If provided, only these domains will be included in results. Cannot be used alongside `blocked_domains`.

      - `Optional<List<String>> blockedDomains`

        If provided, these domains will never appear in results. Cannot be used alongside `allowed_domains`.

      - `Optional<CacheControlEphemeral> cacheControl`

        Create a cache control breakpoint at this content block.

        - `JsonValue; type "ephemeral"constant`

          - `EPHEMERAL("ephemeral")`

        - `Optional<Ttl> ttl`

          The time-to-live for the cache control breakpoint.

          This may be one the following values:

          - `5m`: 5 minutes
          - `1h`: 1 hour

          Defaults to `5m`.

          - `TTL_5M("5m")`

          - `TTL_1H("1h")`

      - `Optional<Boolean> deferLoading`

        If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

      - `Optional<Long> maxUses`

        Maximum number of times the tool can be used in the API request.

      - `Optional<Boolean> strict`

        When true, guarantees schema validation on tool names and inputs

      - `Optional<UserLocation> userLocation`

        Parameters for the user's location. Used to provide more relevant search results.

        - `JsonValue; type "approximate"constant`

          - `APPROXIMATE("approximate")`

        - `Optional<String> city`

          The city of the user.

        - `Optional<String> country`

          The two letter [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) of the user.

        - `Optional<String> region`

          The region of the user.

        - `Optional<String> timezone`

          The [IANA timezone](https://nodatime.org/TimeZones) of the user.

    - `class WebFetchTool20260209:`

      - `JsonValue; name "web_fetch"constant`

        Name of the tool.

        This is how the tool will be called by the model and in `tool_use` blocks.

        - `WEB_FETCH("web_fetch")`

      - `JsonValue; type "web_fetch_20260209"constant`

        - `WEB_FETCH_20260209("web_fetch_20260209")`

      - `Optional<List<AllowedCaller>> allowedCallers`

        - `DIRECT("direct")`

        - `CODE_EXECUTION_20250825("code_execution_20250825")`

        - `CODE_EXECUTION_20260120("code_execution_20260120")`

      - `Optional<List<String>> allowedDomains`

        List of domains to allow fetching from

      - `Optional<List<String>> blockedDomains`

        List of domains to block fetching from

      - `Optional<CacheControlEphemeral> cacheControl`

        Create a cache control breakpoint at this content block.

        - `JsonValue; type "ephemeral"constant`

          - `EPHEMERAL("ephemeral")`

        - `Optional<Ttl> ttl`

          The time-to-live for the cache control breakpoint.

          This may be one the following values:

          - `5m`: 5 minutes
          - `1h`: 1 hour

          Defaults to `5m`.

          - `TTL_5M("5m")`

          - `TTL_1H("1h")`

      - `Optional<CitationsConfigParam> citations`

        Citations configuration for fetched documents. Citations are disabled by default.

        - `Optional<Boolean> enabled`

      - `Optional<Boolean> deferLoading`

        If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

      - `Optional<Long> maxContentTokens`

        Maximum number of tokens used by including web page text content in the context. The limit is approximate and does not apply to binary content such as PDFs.

      - `Optional<Long> maxUses`

        Maximum number of times the tool can be used in the API request.

      - `Optional<Boolean> strict`

        When true, guarantees schema validation on tool names and inputs

    - `class ToolSearchToolBm25_20251119:`

      - `JsonValue; name "tool_search_tool_bm25"constant`

        Name of the tool.

        This is how the tool will be called by the model and in `tool_use` blocks.

        - `TOOL_SEARCH_TOOL_BM25("tool_search_tool_bm25")`

      - `Type type`

        - `TOOL_SEARCH_TOOL_BM25_20251119("tool_search_tool_bm25_20251119")`

        - `TOOL_SEARCH_TOOL_BM25("tool_search_tool_bm25")`

      - `Optional<List<AllowedCaller>> allowedCallers`

        - `DIRECT("direct")`

        - `CODE_EXECUTION_20250825("code_execution_20250825")`

        - `CODE_EXECUTION_20260120("code_execution_20260120")`

      - `Optional<CacheControlEphemeral> cacheControl`

        Create a cache control breakpoint at this content block.

        - `JsonValue; type "ephemeral"constant`

          - `EPHEMERAL("ephemeral")`

        - `Optional<Ttl> ttl`

          The time-to-live for the cache control breakpoint.

          This may be one the following values:

          - `5m`: 5 minutes
          - `1h`: 1 hour

          Defaults to `5m`.

          - `TTL_5M("5m")`

          - `TTL_1H("1h")`

      - `Optional<Boolean> deferLoading`

        If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

      - `Optional<Boolean> strict`

        When true, guarantees schema validation on tool names and inputs

    - `class ToolSearchToolRegex20251119:`

      - `JsonValue; name "tool_search_tool_regex"constant`

        Name of the tool.

        This is how the tool will be called by the model and in `tool_use` blocks.

        - `TOOL_SEARCH_TOOL_REGEX("tool_search_tool_regex")`

      - `Type type`

        - `TOOL_SEARCH_TOOL_REGEX_20251119("tool_search_tool_regex_20251119")`

        - `TOOL_SEARCH_TOOL_REGEX("tool_search_tool_regex")`

      - `Optional<List<AllowedCaller>> allowedCallers`

        - `DIRECT("direct")`

        - `CODE_EXECUTION_20250825("code_execution_20250825")`

        - `CODE_EXECUTION_20260120("code_execution_20260120")`

      - `Optional<CacheControlEphemeral> cacheControl`

        Create a cache control breakpoint at this content block.

        - `JsonValue; type "ephemeral"constant`

          - `EPHEMERAL("ephemeral")`

        - `Optional<Ttl> ttl`

          The time-to-live for the cache control breakpoint.

          This may be one the following values:

          - `5m`: 5 minutes
          - `1h`: 1 hour

          Defaults to `5m`.

          - `TTL_5M("5m")`

          - `TTL_1H("1h")`

      - `Optional<Boolean> deferLoading`

        If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

      - `Optional<Boolean> strict`

        When true, guarantees schema validation on tool names and inputs

### Returns

- `class MessageTokensCount:`

  - `long inputTokens`

    The total number of tokens across the provided list of messages, system prompt, and tools.

### Example

```java
package com.anthropic.example;

import com.anthropic.client.AnthropicClient;
import com.anthropic.client.okhttp.AnthropicOkHttpClient;
import com.anthropic.models.messages.MessageCountTokensParams;
import com.anthropic.models.messages.MessageTokensCount;
import com.anthropic.models.messages.Model;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        AnthropicClient client = AnthropicOkHttpClient.fromEnv();

        MessageCountTokensParams params = MessageCountTokensParams.builder()
            .addUserMessage("Hello, world")
            .model(Model.CLAUDE_OPUS_4_6)
            .build();
        MessageTokensCount messageTokensCount = client.messages().countTokens(params);
    }
}
```

## Domain Types

### Base64 Image Source

- `class Base64ImageSource:`

  - `String data`

  - `MediaType mediaType`

    - `IMAGE_JPEG("image/jpeg")`

    - `IMAGE_PNG("image/png")`

    - `IMAGE_GIF("image/gif")`

    - `IMAGE_WEBP("image/webp")`

  - `JsonValue; type "base64"constant`

    - `BASE64("base64")`

### Base64 PDF Source

- `class Base64PdfSource:`

  - `String data`

  - `JsonValue; mediaType "application/pdf"constant`

    - `APPLICATION_PDF("application/pdf")`

  - `JsonValue; type "base64"constant`

    - `BASE64("base64")`

### Bash Code Execution Output Block

- `class BashCodeExecutionOutputBlock:`

  - `String fileId`

  - `JsonValue; type "bash_code_execution_output"constant`

    - `BASH_CODE_EXECUTION_OUTPUT("bash_code_execution_output")`

### Bash Code Execution Output Block Param

- `class BashCodeExecutionOutputBlockParam:`

  - `String fileId`

  - `JsonValue; type "bash_code_execution_output"constant`

    - `BASH_CODE_EXECUTION_OUTPUT("bash_code_execution_output")`

### Bash Code Execution Result Block

- `class BashCodeExecutionResultBlock:`

  - `List<BashCodeExecutionOutputBlock> content`

    - `String fileId`

    - `JsonValue; type "bash_code_execution_output"constant`

      - `BASH_CODE_EXECUTION_OUTPUT("bash_code_execution_output")`

  - `long returnCode`

  - `String stderr`

  - `String stdout`

  - `JsonValue; type "bash_code_execution_result"constant`

    - `BASH_CODE_EXECUTION_RESULT("bash_code_execution_result")`

### Bash Code Execution Result Block Param

- `class BashCodeExecutionResultBlockParam:`

  - `List<BashCodeExecutionOutputBlockParam> content`

    - `String fileId`

    - `JsonValue; type "bash_code_execution_output"constant`

      - `BASH_CODE_EXECUTION_OUTPUT("bash_code_execution_output")`

  - `long returnCode`

  - `String stderr`

  - `String stdout`

  - `JsonValue; type "bash_code_execution_result"constant`

    - `BASH_CODE_EXECUTION_RESULT("bash_code_execution_result")`

### Bash Code Execution Tool Result Block

- `class BashCodeExecutionToolResultBlock:`

  - `Content content`

    - `class BashCodeExecutionToolResultError:`

      - `BashCodeExecutionToolResultErrorCode errorCode`

        - `INVALID_TOOL_INPUT("invalid_tool_input")`

        - `UNAVAILABLE("unavailable")`

        - `TOO_MANY_REQUESTS("too_many_requests")`

        - `EXECUTION_TIME_EXCEEDED("execution_time_exceeded")`

        - `OUTPUT_FILE_TOO_LARGE("output_file_too_large")`

      - `JsonValue; type "bash_code_execution_tool_result_error"constant`

        - `BASH_CODE_EXECUTION_TOOL_RESULT_ERROR("bash_code_execution_tool_result_error")`

    - `class BashCodeExecutionResultBlock:`

      - `List<BashCodeExecutionOutputBlock> content`

        - `String fileId`

        - `JsonValue; type "bash_code_execution_output"constant`

          - `BASH_CODE_EXECUTION_OUTPUT("bash_code_execution_output")`

      - `long returnCode`

      - `String stderr`

      - `String stdout`

      - `JsonValue; type "bash_code_execution_result"constant`

        - `BASH_CODE_EXECUTION_RESULT("bash_code_execution_result")`

  - `String toolUseId`

  - `JsonValue; type "bash_code_execution_tool_result"constant`

    - `BASH_CODE_EXECUTION_TOOL_RESULT("bash_code_execution_tool_result")`

### Bash Code Execution Tool Result Block Param

- `class BashCodeExecutionToolResultBlockParam:`

  - `Content content`

    - `class BashCodeExecutionToolResultErrorParam:`

      - `BashCodeExecutionToolResultErrorCode errorCode`

        - `INVALID_TOOL_INPUT("invalid_tool_input")`

        - `UNAVAILABLE("unavailable")`

        - `TOO_MANY_REQUESTS("too_many_requests")`

        - `EXECUTION_TIME_EXCEEDED("execution_time_exceeded")`

        - `OUTPUT_FILE_TOO_LARGE("output_file_too_large")`

      - `JsonValue; type "bash_code_execution_tool_result_error"constant`

        - `BASH_CODE_EXECUTION_TOOL_RESULT_ERROR("bash_code_execution_tool_result_error")`

    - `class BashCodeExecutionResultBlockParam:`

      - `List<BashCodeExecutionOutputBlockParam> content`

        - `String fileId`

        - `JsonValue; type "bash_code_execution_output"constant`

          - `BASH_CODE_EXECUTION_OUTPUT("bash_code_execution_output")`

      - `long returnCode`

      - `String stderr`

      - `String stdout`

      - `JsonValue; type "bash_code_execution_result"constant`

        - `BASH_CODE_EXECUTION_RESULT("bash_code_execution_result")`

  - `String toolUseId`

  - `JsonValue; type "bash_code_execution_tool_result"constant`

    - `BASH_CODE_EXECUTION_TOOL_RESULT("bash_code_execution_tool_result")`

  - `Optional<CacheControlEphemeral> cacheControl`

    Create a cache control breakpoint at this content block.

    - `JsonValue; type "ephemeral"constant`

      - `EPHEMERAL("ephemeral")`

    - `Optional<Ttl> ttl`

      The time-to-live for the cache control breakpoint.

      This may be one the following values:

      - `5m`: 5 minutes
      - `1h`: 1 hour

      Defaults to `5m`.

      - `TTL_5M("5m")`

      - `TTL_1H("1h")`

### Bash Code Execution Tool Result Error

- `class BashCodeExecutionToolResultError:`

  - `BashCodeExecutionToolResultErrorCode errorCode`

    - `INVALID_TOOL_INPUT("invalid_tool_input")`

    - `UNAVAILABLE("unavailable")`

    - `TOO_MANY_REQUESTS("too_many_requests")`

    - `EXECUTION_TIME_EXCEEDED("execution_time_exceeded")`

    - `OUTPUT_FILE_TOO_LARGE("output_file_too_large")`

  - `JsonValue; type "bash_code_execution_tool_result_error"constant`

    - `BASH_CODE_EXECUTION_TOOL_RESULT_ERROR("bash_code_execution_tool_result_error")`

### Bash Code Execution Tool Result Error Code

- `enum BashCodeExecutionToolResultErrorCode:`

  - `INVALID_TOOL_INPUT("invalid_tool_input")`

  - `UNAVAILABLE("unavailable")`

  - `TOO_MANY_REQUESTS("too_many_requests")`

  - `EXECUTION_TIME_EXCEEDED("execution_time_exceeded")`

  - `OUTPUT_FILE_TOO_LARGE("output_file_too_large")`

### Bash Code Execution Tool Result Error Param

- `class BashCodeExecutionToolResultErrorParam:`

  - `BashCodeExecutionToolResultErrorCode errorCode`

    - `INVALID_TOOL_INPUT("invalid_tool_input")`

    - `UNAVAILABLE("unavailable")`

    - `TOO_MANY_REQUESTS("too_many_requests")`

    - `EXECUTION_TIME_EXCEEDED("execution_time_exceeded")`

    - `OUTPUT_FILE_TOO_LARGE("output_file_too_large")`

  - `JsonValue; type "bash_code_execution_tool_result_error"constant`

    - `BASH_CODE_EXECUTION_TOOL_RESULT_ERROR("bash_code_execution_tool_result_error")`

### Cache Control Ephemeral

- `class CacheControlEphemeral:`

  - `JsonValue; type "ephemeral"constant`

    - `EPHEMERAL("ephemeral")`

  - `Optional<Ttl> ttl`

    The time-to-live for the cache control breakpoint.

    This may be one the following values:

    - `5m`: 5 minutes
    - `1h`: 1 hour

    Defaults to `5m`.

    - `TTL_5M("5m")`

    - `TTL_1H("1h")`

### Cache Creation

- `class CacheCreation:`

  - `long ephemeral1hInputTokens`

    The number of input tokens used to create the 1 hour cache entry.

  - `long ephemeral5mInputTokens`

    The number of input tokens used to create the 5 minute cache entry.

### Citation Char Location

- `class CitationCharLocation:`

  - `String citedText`

  - `long documentIndex`

  - `Optional<String> documentTitle`

  - `long endCharIndex`

  - `Optional<String> fileId`

  - `long startCharIndex`

  - `JsonValue; type "char_location"constant`

    - `CHAR_LOCATION("char_location")`

### Citation Char Location Param

- `class CitationCharLocationParam:`

  - `String citedText`

  - `long documentIndex`

  - `Optional<String> documentTitle`

  - `long endCharIndex`

  - `long startCharIndex`

  - `JsonValue; type "char_location"constant`

    - `CHAR_LOCATION("char_location")`

### Citation Content Block Location

- `class CitationContentBlockLocation:`

  - `String citedText`

  - `long documentIndex`

  - `Optional<String> documentTitle`

  - `long endBlockIndex`

  - `Optional<String> fileId`

  - `long startBlockIndex`

  - `JsonValue; type "content_block_location"constant`

    - `CONTENT_BLOCK_LOCATION("content_block_location")`

### Citation Content Block Location Param

- `class CitationContentBlockLocationParam:`

  - `String citedText`

  - `long documentIndex`

  - `Optional<String> documentTitle`

  - `long endBlockIndex`

  - `long startBlockIndex`

  - `JsonValue; type "content_block_location"constant`

    - `CONTENT_BLOCK_LOCATION("content_block_location")`

### Citation Page Location

- `class CitationPageLocation:`

  - `String citedText`

  - `long documentIndex`

  - `Optional<String> documentTitle`

  - `long endPageNumber`

  - `Optional<String> fileId`

  - `long startPageNumber`

  - `JsonValue; type "page_location"constant`

    - `PAGE_LOCATION("page_location")`

### Citation Page Location Param

- `class CitationPageLocationParam:`

  - `String citedText`

  - `long documentIndex`

  - `Optional<String> documentTitle`

  - `long endPageNumber`

  - `long startPageNumber`

  - `JsonValue; type "page_location"constant`

    - `PAGE_LOCATION("page_location")`

### Citation Search Result Location Param

- `class CitationSearchResultLocationParam:`

  - `String citedText`

  - `long endBlockIndex`

  - `long searchResultIndex`

  - `String source`

  - `long startBlockIndex`

  - `Optional<String> title`

  - `JsonValue; type "search_result_location"constant`

    - `SEARCH_RESULT_LOCATION("search_result_location")`

### Citation Web Search Result Location Param

- `class CitationWebSearchResultLocationParam:`

  - `String citedText`

  - `String encryptedIndex`

  - `Optional<String> title`

  - `JsonValue; type "web_search_result_location"constant`

    - `WEB_SEARCH_RESULT_LOCATION("web_search_result_location")`

  - `String url`

### Citations Config

- `class CitationsConfig:`

  - `boolean enabled`

### Citations Config Param

- `class CitationsConfigParam:`

  - `Optional<Boolean> enabled`

### Citations Delta

- `class CitationsDelta:`

  - `Citation citation`

    - `class CitationCharLocation:`

      - `String citedText`

      - `long documentIndex`

      - `Optional<String> documentTitle`

      - `long endCharIndex`

      - `Optional<String> fileId`

      - `long startCharIndex`

      - `JsonValue; type "char_location"constant`

        - `CHAR_LOCATION("char_location")`

    - `class CitationPageLocation:`

      - `String citedText`

      - `long documentIndex`

      - `Optional<String> documentTitle`

      - `long endPageNumber`

      - `Optional<String> fileId`

      - `long startPageNumber`

      - `JsonValue; type "page_location"constant`

        - `PAGE_LOCATION("page_location")`

    - `class CitationContentBlockLocation:`

      - `String citedText`

      - `long documentIndex`

      - `Optional<String> documentTitle`

      - `long endBlockIndex`

      - `Optional<String> fileId`

      - `long startBlockIndex`

      - `JsonValue; type "content_block_location"constant`

        - `CONTENT_BLOCK_LOCATION("content_block_location")`

    - `class CitationsWebSearchResultLocation:`

      - `String citedText`

      - `String encryptedIndex`

      - `Optional<String> title`

      - `JsonValue; type "web_search_result_location"constant`

        - `WEB_SEARCH_RESULT_LOCATION("web_search_result_location")`

      - `String url`

    - `class CitationsSearchResultLocation:`

      - `String citedText`

      - `long endBlockIndex`

      - `long searchResultIndex`

      - `String source`

      - `long startBlockIndex`

      - `Optional<String> title`

      - `JsonValue; type "search_result_location"constant`

        - `SEARCH_RESULT_LOCATION("search_result_location")`

  - `JsonValue; type "citations_delta"constant`

    - `CITATIONS_DELTA("citations_delta")`

### Citations Search Result Location

- `class CitationsSearchResultLocation:`

  - `String citedText`

  - `long endBlockIndex`

  - `long searchResultIndex`

  - `String source`

  - `long startBlockIndex`

  - `Optional<String> title`

  - `JsonValue; type "search_result_location"constant`

    - `SEARCH_RESULT_LOCATION("search_result_location")`

### Citations Web Search Result Location

- `class CitationsWebSearchResultLocation:`

  - `String citedText`

  - `String encryptedIndex`

  - `Optional<String> title`

  - `JsonValue; type "web_search_result_location"constant`

    - `WEB_SEARCH_RESULT_LOCATION("web_search_result_location")`

  - `String url`

### Code Execution Output Block

- `class CodeExecutionOutputBlock:`

  - `String fileId`

  - `JsonValue; type "code_execution_output"constant`

    - `CODE_EXECUTION_OUTPUT("code_execution_output")`

### Code Execution Output Block Param

- `class CodeExecutionOutputBlockParam:`

  - `String fileId`

  - `JsonValue; type "code_execution_output"constant`

    - `CODE_EXECUTION_OUTPUT("code_execution_output")`

### Code Execution Result Block

- `class CodeExecutionResultBlock:`

  - `List<CodeExecutionOutputBlock> content`

    - `String fileId`

    - `JsonValue; type "code_execution_output"constant`

      - `CODE_EXECUTION_OUTPUT("code_execution_output")`

  - `long returnCode`

  - `String stderr`

  - `String stdout`

  - `JsonValue; type "code_execution_result"constant`

    - `CODE_EXECUTION_RESULT("code_execution_result")`

### Code Execution Result Block Param

- `class CodeExecutionResultBlockParam:`

  - `List<CodeExecutionOutputBlockParam> content`

    - `String fileId`

    - `JsonValue; type "code_execution_output"constant`

      - `CODE_EXECUTION_OUTPUT("code_execution_output")`

  - `long returnCode`

  - `String stderr`

  - `String stdout`

  - `JsonValue; type "code_execution_result"constant`

    - `CODE_EXECUTION_RESULT("code_execution_result")`

### Code Execution Tool 20250522

- `class CodeExecutionTool20250522:`

  - `JsonValue; name "code_execution"constant`

    Name of the tool.

    This is how the tool will be called by the model and in `tool_use` blocks.

    - `CODE_EXECUTION("code_execution")`

  - `JsonValue; type "code_execution_20250522"constant`

    - `CODE_EXECUTION_20250522("code_execution_20250522")`

  - `Optional<List<AllowedCaller>> allowedCallers`

    - `DIRECT("direct")`

    - `CODE_EXECUTION_20250825("code_execution_20250825")`

    - `CODE_EXECUTION_20260120("code_execution_20260120")`

  - `Optional<CacheControlEphemeral> cacheControl`

    Create a cache control breakpoint at this content block.

    - `JsonValue; type "ephemeral"constant`

      - `EPHEMERAL("ephemeral")`

    - `Optional<Ttl> ttl`

      The time-to-live for the cache control breakpoint.

      This may be one the following values:

      - `5m`: 5 minutes
      - `1h`: 1 hour

      Defaults to `5m`.

      - `TTL_5M("5m")`

      - `TTL_1H("1h")`

  - `Optional<Boolean> deferLoading`

    If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

  - `Optional<Boolean> strict`

    When true, guarantees schema validation on tool names and inputs

### Code Execution Tool 20250825

- `class CodeExecutionTool20250825:`

  - `JsonValue; name "code_execution"constant`

    Name of the tool.

    This is how the tool will be called by the model and in `tool_use` blocks.

    - `CODE_EXECUTION("code_execution")`

  - `JsonValue; type "code_execution_20250825"constant`

    - `CODE_EXECUTION_20250825("code_execution_20250825")`

  - `Optional<List<AllowedCaller>> allowedCallers`

    - `DIRECT("direct")`

    - `CODE_EXECUTION_20250825("code_execution_20250825")`

    - `CODE_EXECUTION_20260120("code_execution_20260120")`

  - `Optional<CacheControlEphemeral> cacheControl`

    Create a cache control breakpoint at this content block.

    - `JsonValue; type "ephemeral"constant`

      - `EPHEMERAL("ephemeral")`

    - `Optional<Ttl> ttl`

      The time-to-live for the cache control breakpoint.

      This may be one the following values:

      - `5m`: 5 minutes
      - `1h`: 1 hour

      Defaults to `5m`.

      - `TTL_5M("5m")`

      - `TTL_1H("1h")`

  - `Optional<Boolean> deferLoading`

    If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

  - `Optional<Boolean> strict`

    When true, guarantees schema validation on tool names and inputs

### Code Execution Tool 20260120

- `class CodeExecutionTool20260120:`

  Code execution tool with REPL state persistence (daemon mode + gVisor checkpoint).

  - `JsonValue; name "code_execution"constant`

    Name of the tool.

    This is how the tool will be called by the model and in `tool_use` blocks.

    - `CODE_EXECUTION("code_execution")`

  - `JsonValue; type "code_execution_20260120"constant`

    - `CODE_EXECUTION_20260120("code_execution_20260120")`

  - `Optional<List<AllowedCaller>> allowedCallers`

    - `DIRECT("direct")`

    - `CODE_EXECUTION_20250825("code_execution_20250825")`

    - `CODE_EXECUTION_20260120("code_execution_20260120")`

  - `Optional<CacheControlEphemeral> cacheControl`

    Create a cache control breakpoint at this content block.

    - `JsonValue; type "ephemeral"constant`

      - `EPHEMERAL("ephemeral")`

    - `Optional<Ttl> ttl`

      The time-to-live for the cache control breakpoint.

      This may be one the following values:

      - `5m`: 5 minutes
      - `1h`: 1 hour

      Defaults to `5m`.

      - `TTL_5M("5m")`

      - `TTL_1H("1h")`

  - `Optional<Boolean> deferLoading`

    If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

  - `Optional<Boolean> strict`

    When true, guarantees schema validation on tool names and inputs

### Code Execution Tool Result Block

- `class CodeExecutionToolResultBlock:`

  - `CodeExecutionToolResultBlockContent content`

    Code execution result with encrypted stdout for PFC + web_search results.

    - `class CodeExecutionToolResultError:`

      - `CodeExecutionToolResultErrorCode errorCode`

        - `INVALID_TOOL_INPUT("invalid_tool_input")`

        - `UNAVAILABLE("unavailable")`

        - `TOO_MANY_REQUESTS("too_many_requests")`

        - `EXECUTION_TIME_EXCEEDED("execution_time_exceeded")`

      - `JsonValue; type "code_execution_tool_result_error"constant`

        - `CODE_EXECUTION_TOOL_RESULT_ERROR("code_execution_tool_result_error")`

    - `class CodeExecutionResultBlock:`

      - `List<CodeExecutionOutputBlock> content`

        - `String fileId`

        - `JsonValue; type "code_execution_output"constant`

          - `CODE_EXECUTION_OUTPUT("code_execution_output")`

      - `long returnCode`

      - `String stderr`

      - `String stdout`

      - `JsonValue; type "code_execution_result"constant`

        - `CODE_EXECUTION_RESULT("code_execution_result")`

    - `class EncryptedCodeExecutionResultBlock:`

      Code execution result with encrypted stdout for PFC + web_search results.

      - `List<CodeExecutionOutputBlock> content`

        - `String fileId`

        - `JsonValue; type "code_execution_output"constant`

          - `CODE_EXECUTION_OUTPUT("code_execution_output")`

      - `String encryptedStdout`

      - `long returnCode`

      - `String stderr`

      - `JsonValue; type "encrypted_code_execution_result"constant`

        - `ENCRYPTED_CODE_EXECUTION_RESULT("encrypted_code_execution_result")`

  - `String toolUseId`

  - `JsonValue; type "code_execution_tool_result"constant`

    - `CODE_EXECUTION_TOOL_RESULT("code_execution_tool_result")`

### Code Execution Tool Result Block Content

- `class CodeExecutionToolResultBlockContent: A class that can be one of several variants.union`

  Code execution result with encrypted stdout for PFC + web_search results.

  - `class CodeExecutionToolResultError:`

    - `CodeExecutionToolResultErrorCode errorCode`

      - `INVALID_TOOL_INPUT("invalid_tool_input")`

      - `UNAVAILABLE("unavailable")`

      - `TOO_MANY_REQUESTS("too_many_requests")`

      - `EXECUTION_TIME_EXCEEDED("execution_time_exceeded")`

    - `JsonValue; type "code_execution_tool_result_error"constant`

      - `CODE_EXECUTION_TOOL_RESULT_ERROR("code_execution_tool_result_error")`

  - `class CodeExecutionResultBlock:`

    - `List<CodeExecutionOutputBlock> content`

      - `String fileId`

      - `JsonValue; type "code_execution_output"constant`

        - `CODE_EXECUTION_OUTPUT("code_execution_output")`

    - `long returnCode`

    - `String stderr`

    - `String stdout`

    - `JsonValue; type "code_execution_result"constant`

      - `CODE_EXECUTION_RESULT("code_execution_result")`

  - `class EncryptedCodeExecutionResultBlock:`

    Code execution result with encrypted stdout for PFC + web_search results.

    - `List<CodeExecutionOutputBlock> content`

      - `String fileId`

      - `JsonValue; type "code_execution_output"constant`

        - `CODE_EXECUTION_OUTPUT("code_execution_output")`

    - `String encryptedStdout`

    - `long returnCode`

    - `String stderr`

    - `JsonValue; type "encrypted_code_execution_result"constant`

      - `ENCRYPTED_CODE_EXECUTION_RESULT("encrypted_code_execution_result")`

### Code Execution Tool Result Block Param

- `class CodeExecutionToolResultBlockParam:`

  - `CodeExecutionToolResultBlockParamContent content`

    Code execution result with encrypted stdout for PFC + web_search results.

    - `class CodeExecutionToolResultErrorParam:`

      - `CodeExecutionToolResultErrorCode errorCode`

        - `INVALID_TOOL_INPUT("invalid_tool_input")`

        - `UNAVAILABLE("unavailable")`

        - `TOO_MANY_REQUESTS("too_many_requests")`

        - `EXECUTION_TIME_EXCEEDED("execution_time_exceeded")`

      - `JsonValue; type "code_execution_tool_result_error"constant`

        - `CODE_EXECUTION_TOOL_RESULT_ERROR("code_execution_tool_result_error")`

    - `class CodeExecutionResultBlockParam:`

      - `List<CodeExecutionOutputBlockParam> content`

        - `String fileId`

        - `JsonValue; type "code_execution_output"constant`

          - `CODE_EXECUTION_OUTPUT("code_execution_output")`

      - `long returnCode`

      - `String stderr`

      - `String stdout`

      - `JsonValue; type "code_execution_result"constant`

        - `CODE_EXECUTION_RESULT("code_execution_result")`

    - `class EncryptedCodeExecutionResultBlockParam:`

      Code execution result with encrypted stdout for PFC + web_search results.

      - `List<CodeExecutionOutputBlockParam> content`

        - `String fileId`

        - `JsonValue; type "code_execution_output"constant`

          - `CODE_EXECUTION_OUTPUT("code_execution_output")`

      - `String encryptedStdout`

      - `long returnCode`

      - `String stderr`

      - `JsonValue; type "encrypted_code_execution_result"constant`

        - `ENCRYPTED_CODE_EXECUTION_RESULT("encrypted_code_execution_result")`

  - `String toolUseId`

  - `JsonValue; type "code_execution_tool_result"constant`

    - `CODE_EXECUTION_TOOL_RESULT("code_execution_tool_result")`

  - `Optional<CacheControlEphemeral> cacheControl`

    Create a cache control breakpoint at this content block.

    - `JsonValue; type "ephemeral"constant`

      - `EPHEMERAL("ephemeral")`

    - `Optional<Ttl> ttl`

      The time-to-live for the cache control breakpoint.

      This may be one the following values:

      - `5m`: 5 minutes
      - `1h`: 1 hour

      Defaults to `5m`.

      - `TTL_5M("5m")`

      - `TTL_1H("1h")`

### Code Execution Tool Result Block Param Content

- `class CodeExecutionToolResultBlockParamContent: A class that can be one of several variants.union`

  Code execution result with encrypted stdout for PFC + web_search results.

  - `class CodeExecutionToolResultErrorParam:`

    - `CodeExecutionToolResultErrorCode errorCode`

      - `INVALID_TOOL_INPUT("invalid_tool_input")`

      - `UNAVAILABLE("unavailable")`

      - `TOO_MANY_REQUESTS("too_many_requests")`

      - `EXECUTION_TIME_EXCEEDED("execution_time_exceeded")`

    - `JsonValue; type "code_execution_tool_result_error"constant`

      - `CODE_EXECUTION_TOOL_RESULT_ERROR("code_execution_tool_result_error")`

  - `class CodeExecutionResultBlockParam:`

    - `List<CodeExecutionOutputBlockParam> content`

      - `String fileId`

      - `JsonValue; type "code_execution_output"constant`

        - `CODE_EXECUTION_OUTPUT("code_execution_output")`

    - `long returnCode`

    - `String stderr`

    - `String stdout`

    - `JsonValue; type "code_execution_result"constant`

      - `CODE_EXECUTION_RESULT("code_execution_result")`

  - `class EncryptedCodeExecutionResultBlockParam:`

    Code execution result with encrypted stdout for PFC + web_search results.

    - `List<CodeExecutionOutputBlockParam> content`

      - `String fileId`

      - `JsonValue; type "code_execution_output"constant`

        - `CODE_EXECUTION_OUTPUT("code_execution_output")`

    - `String encryptedStdout`

    - `long returnCode`

    - `String stderr`

    - `JsonValue; type "encrypted_code_execution_result"constant`

      - `ENCRYPTED_CODE_EXECUTION_RESULT("encrypted_code_execution_result")`

### Code Execution Tool Result Error

- `class CodeExecutionToolResultError:`

  - `CodeExecutionToolResultErrorCode errorCode`

    - `INVALID_TOOL_INPUT("invalid_tool_input")`

    - `UNAVAILABLE("unavailable")`

    - `TOO_MANY_REQUESTS("too_many_requests")`

    - `EXECUTION_TIME_EXCEEDED("execution_time_exceeded")`

  - `JsonValue; type "code_execution_tool_result_error"constant`

    - `CODE_EXECUTION_TOOL_RESULT_ERROR("code_execution_tool_result_error")`

### Code Execution Tool Result Error Code

- `enum CodeExecutionToolResultErrorCode:`

  - `INVALID_TOOL_INPUT("invalid_tool_input")`

  - `UNAVAILABLE("unavailable")`

  - `TOO_MANY_REQUESTS("too_many_requests")`

  - `EXECUTION_TIME_EXCEEDED("execution_time_exceeded")`

### Code Execution Tool Result Error Param

- `class CodeExecutionToolResultErrorParam:`

  - `CodeExecutionToolResultErrorCode errorCode`

    - `INVALID_TOOL_INPUT("invalid_tool_input")`

    - `UNAVAILABLE("unavailable")`

    - `TOO_MANY_REQUESTS("too_many_requests")`

    - `EXECUTION_TIME_EXCEEDED("execution_time_exceeded")`

  - `JsonValue; type "code_execution_tool_result_error"constant`

    - `CODE_EXECUTION_TOOL_RESULT_ERROR("code_execution_tool_result_error")`

### Container

- `class Container:`

  Information about the container used in the request (for the code execution tool)

  - `String id`

    Identifier for the container used in this request

  - `LocalDateTime expiresAt`

    The time at which the container will expire.

### Container Upload Block

- `class ContainerUploadBlock:`

  Response model for a file uploaded to the container.

  - `String fileId`

  - `JsonValue; type "container_upload"constant`

    - `CONTAINER_UPLOAD("container_upload")`

### Container Upload Block Param

- `class ContainerUploadBlockParam:`

  A content block that represents a file to be uploaded to the container
  Files uploaded via this block will be available in the container's input directory.

  - `String fileId`

  - `JsonValue; type "container_upload"constant`

    - `CONTAINER_UPLOAD("container_upload")`

  - `Optional<CacheControlEphemeral> cacheControl`

    Create a cache control breakpoint at this content block.

    - `JsonValue; type "ephemeral"constant`

      - `EPHEMERAL("ephemeral")`

    - `Optional<Ttl> ttl`

      The time-to-live for the cache control breakpoint.

      This may be one the following values:

      - `5m`: 5 minutes
      - `1h`: 1 hour

      Defaults to `5m`.

      - `TTL_5M("5m")`

      - `TTL_1H("1h")`

### Content Block

- `class ContentBlock: A class that can be one of several variants.union`

  Response model for a file uploaded to the container.

  - `class TextBlock:`

    - `Optional<List<TextCitation>> citations`

      Citations supporting the text block.

      The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

      - `class CitationCharLocation:`

        - `String citedText`

        - `long documentIndex`

        - `Optional<String> documentTitle`

        - `long endCharIndex`

        - `Optional<String> fileId`

        - `long startCharIndex`

        - `JsonValue; type "char_location"constant`

          - `CHAR_LOCATION("char_location")`

      - `class CitationPageLocation:`

        - `String citedText`

        - `long documentIndex`

        - `Optional<String> documentTitle`

        - `long endPageNumber`

        - `Optional<String> fileId`

        - `long startPageNumber`

        - `JsonValue; type "page_location"constant`

          - `PAGE_LOCATION("page_location")`

      - `class CitationContentBlockLocation:`

        - `String citedText`

        - `long documentIndex`

        - `Optional<String> documentTitle`

        - `long endBlockIndex`

        - `Optional<String> fileId`

        - `long startBlockIndex`

        - `JsonValue; type "content_block_location"constant`

          - `CONTENT_BLOCK_LOCATION("content_block_location")`

      - `class CitationsWebSearchResultLocation:`

        - `String citedText`

        - `String encryptedIndex`

        - `Optional<String> title`

        - `JsonValue; type "web_search_result_location"constant`

          - `WEB_SEARCH_RESULT_LOCATION("web_search_result_location")`

        - `String url`

      - `class CitationsSearchResultLocation:`

        - `String citedText`

        - `long endBlockIndex`

        - `long searchResultIndex`

        - `String source`

        - `long startBlockIndex`

        - `Optional<String> title`

        - `JsonValue; type "search_result_location"constant`

          - `SEARCH_RESULT_LOCATION("search_result_location")`

    - `String text`

    - `JsonValue; type "text"constant`

      - `TEXT("text")`

  - `class ThinkingBlock:`

    - `String signature`

    - `String thinking`

    - `JsonValue; type "thinking"constant`

      - `THINKING("thinking")`

  - `class RedactedThinkingBlock:`

    - `String data`

    - `JsonValue; type "redacted_thinking"constant`

      - `REDACTED_THINKING("redacted_thinking")`

  - `class ToolUseBlock:`

    - `String id`

    - `Caller caller`

      Tool invocation directly from the model.

      - `class DirectCaller:`

        Tool invocation directly from the model.

        - `JsonValue; type "direct"constant`

          - `DIRECT("direct")`

      - `class ServerToolCaller:`

        Tool invocation generated by a server-side tool.

        - `String toolId`

        - `JsonValue; type "code_execution_20250825"constant`

          - `CODE_EXECUTION_20250825("code_execution_20250825")`

      - `class ServerToolCaller20260120:`

        - `String toolId`

        - `JsonValue; type "code_execution_20260120"constant`

          - `CODE_EXECUTION_20260120("code_execution_20260120")`

    - `Input input`

    - `String name`

    - `JsonValue; type "tool_use"constant`

      - `TOOL_USE("tool_use")`

  - `class ServerToolUseBlock:`

    - `String id`

    - `Caller caller`

      Tool invocation directly from the model.

      - `class DirectCaller:`

        Tool invocation directly from the model.

        - `JsonValue; type "direct"constant`

          - `DIRECT("direct")`

      - `class ServerToolCaller:`

        Tool invocation generated by a server-side tool.

        - `String toolId`

        - `JsonValue; type "code_execution_20250825"constant`

          - `CODE_EXECUTION_20250825("code_execution_20250825")`

      - `class ServerToolCaller20260120:`

        - `String toolId`

        - `JsonValue; type "code_execution_20260120"constant`

          - `CODE_EXECUTION_20260120("code_execution_20260120")`

    - `Input input`

    - `Name name`

      - `WEB_SEARCH("web_search")`

      - `WEB_FETCH("web_fetch")`

      - `CODE_EXECUTION("code_execution")`

      - `BASH_CODE_EXECUTION("bash_code_execution")`

      - `TEXT_EDITOR_CODE_EXECUTION("text_editor_code_execution")`

      - `TOOL_SEARCH_TOOL_REGEX("tool_search_tool_regex")`

      - `TOOL_SEARCH_TOOL_BM25("tool_search_tool_bm25")`

    - `JsonValue; type "server_tool_use"constant`

      - `SERVER_TOOL_USE("server_tool_use")`

  - `class WebSearchToolResultBlock:`

    - `Caller caller`

      Tool invocation directly from the model.

      - `class DirectCaller:`

        Tool invocation directly from the model.

        - `JsonValue; type "direct"constant`

          - `DIRECT("direct")`

      - `class ServerToolCaller:`

        Tool invocation generated by a server-side tool.

        - `String toolId`

        - `JsonValue; type "code_execution_20250825"constant`

          - `CODE_EXECUTION_20250825("code_execution_20250825")`

      - `class ServerToolCaller20260120:`

        - `String toolId`

        - `JsonValue; type "code_execution_20260120"constant`

          - `CODE_EXECUTION_20260120("code_execution_20260120")`

    - `WebSearchToolResultBlockContent content`

      - `class WebSearchToolResultError:`

        - `WebSearchToolResultErrorCode errorCode`

          - `INVALID_TOOL_INPUT("invalid_tool_input")`

          - `UNAVAILABLE("unavailable")`

          - `MAX_USES_EXCEEDED("max_uses_exceeded")`

          - `TOO_MANY_REQUESTS("too_many_requests")`

          - `QUERY_TOO_LONG("query_too_long")`

          - `REQUEST_TOO_LARGE("request_too_large")`

        - `JsonValue; type "web_search_tool_result_error"constant`

          - `WEB_SEARCH_TOOL_RESULT_ERROR("web_search_tool_result_error")`

      - `List<WebSearchResultBlock>`

        - `String encryptedContent`

        - `Optional<String> pageAge`

        - `String title`

        - `JsonValue; type "web_search_result"constant`

          - `WEB_SEARCH_RESULT("web_search_result")`

        - `String url`

    - `String toolUseId`

    - `JsonValue; type "web_search_tool_result"constant`

      - `WEB_SEARCH_TOOL_RESULT("web_search_tool_result")`

  - `class WebFetchToolResultBlock:`

    - `Caller caller`

      Tool invocation directly from the model.

      - `class DirectCaller:`

        Tool invocation directly from the model.

        - `JsonValue; type "direct"constant`

          - `DIRECT("direct")`

      - `class ServerToolCaller:`

        Tool invocation generated by a server-side tool.

        - `String toolId`

        - `JsonValue; type "code_execution_20250825"constant`

          - `CODE_EXECUTION_20250825("code_execution_20250825")`

      - `class ServerToolCaller20260120:`

        - `String toolId`

        - `JsonValue; type "code_execution_20260120"constant`

          - `CODE_EXECUTION_20260120("code_execution_20260120")`

    - `Content content`

      - `class WebFetchToolResultErrorBlock:`

        - `WebFetchToolResultErrorCode errorCode`

          - `INVALID_TOOL_INPUT("invalid_tool_input")`

          - `URL_TOO_LONG("url_too_long")`

          - `URL_NOT_ALLOWED("url_not_allowed")`

          - `URL_NOT_ACCESSIBLE("url_not_accessible")`

          - `UNSUPPORTED_CONTENT_TYPE("unsupported_content_type")`

          - `TOO_MANY_REQUESTS("too_many_requests")`

          - `MAX_USES_EXCEEDED("max_uses_exceeded")`

          - `UNAVAILABLE("unavailable")`

        - `JsonValue; type "web_fetch_tool_result_error"constant`

          - `WEB_FETCH_TOOL_RESULT_ERROR("web_fetch_tool_result_error")`

      - `class WebFetchBlock:`

        - `DocumentBlock content`

          - `Optional<CitationsConfig> citations`

            Citation configuration for the document

            - `boolean enabled`

          - `Source source`

            - `class Base64PdfSource:`

              - `String data`

              - `JsonValue; mediaType "application/pdf"constant`

                - `APPLICATION_PDF("application/pdf")`

              - `JsonValue; type "base64"constant`

                - `BASE64("base64")`

            - `class PlainTextSource:`

              - `String data`

              - `JsonValue; mediaType "text/plain"constant`

                - `TEXT_PLAIN("text/plain")`

              - `JsonValue; type "text"constant`

                - `TEXT("text")`

          - `Optional<String> title`

            The title of the document

          - `JsonValue; type "document"constant`

            - `DOCUMENT("document")`

        - `Optional<String> retrievedAt`

          ISO 8601 timestamp when the content was retrieved

        - `JsonValue; type "web_fetch_result"constant`

          - `WEB_FETCH_RESULT("web_fetch_result")`

        - `String url`

          Fetched content URL

    - `String toolUseId`

    - `JsonValue; type "web_fetch_tool_result"constant`

      - `WEB_FETCH_TOOL_RESULT("web_fetch_tool_result")`

  - `class CodeExecutionToolResultBlock:`

    - `CodeExecutionToolResultBlockContent content`

      Code execution result with encrypted stdout for PFC + web_search results.

      - `class CodeExecutionToolResultError:`

        - `CodeExecutionToolResultErrorCode errorCode`

          - `INVALID_TOOL_INPUT("invalid_tool_input")`

          - `UNAVAILABLE("unavailable")`

          - `TOO_MANY_REQUESTS("too_many_requests")`

          - `EXECUTION_TIME_EXCEEDED("execution_time_exceeded")`

        - `JsonValue; type "code_execution_tool_result_error"constant`

          - `CODE_EXECUTION_TOOL_RESULT_ERROR("code_execution_tool_result_error")`

      - `class CodeExecutionResultBlock:`

        - `List<CodeExecutionOutputBlock> content`

          - `String fileId`

          - `JsonValue; type "code_execution_output"constant`

            - `CODE_EXECUTION_OUTPUT("code_execution_output")`

        - `long returnCode`

        - `String stderr`

        - `String stdout`

        - `JsonValue; type "code_execution_result"constant`

          - `CODE_EXECUTION_RESULT("code_execution_result")`

      - `class EncryptedCodeExecutionResultBlock:`

        Code execution result with encrypted stdout for PFC + web_search results.

        - `List<CodeExecutionOutputBlock> content`

          - `String fileId`

          - `JsonValue; type "code_execution_output"constant`

            - `CODE_EXECUTION_OUTPUT("code_execution_output")`

        - `String encryptedStdout`

        - `long returnCode`

        - `String stderr`

        - `JsonValue; type "encrypted_code_execution_result"constant`

          - `ENCRYPTED_CODE_EXECUTION_RESULT("encrypted_code_execution_result")`

    - `String toolUseId`

    - `JsonValue; type "code_execution_tool_result"constant`

      - `CODE_EXECUTION_TOOL_RESULT("code_execution_tool_result")`

  - `class BashCodeExecutionToolResultBlock:`

    - `Content content`

      - `class BashCodeExecutionToolResultError:`

        - `BashCodeExecutionToolResultErrorCode errorCode`

          - `INVALID_TOOL_INPUT("invalid_tool_input")`

          - `UNAVAILABLE("unavailable")`

          - `TOO_MANY_REQUESTS("too_many_requests")`

          - `EXECUTION_TIME_EXCEEDED("execution_time_exceeded")`

          - `OUTPUT_FILE_TOO_LARGE("output_file_too_large")`

        - `JsonValue; type "bash_code_execution_tool_result_error"constant`

          - `BASH_CODE_EXECUTION_TOOL_RESULT_ERROR("bash_code_execution_tool_result_error")`

      - `class BashCodeExecutionResultBlock:`

        - `List<BashCodeExecutionOutputBlock> content`

          - `String fileId`

          - `JsonValue; type "bash_code_execution_output"constant`

            - `BASH_CODE_EXECUTION_OUTPUT("bash_code_execution_output")`

        - `long returnCode`

        - `String stderr`

        - `String stdout`

        - `JsonValue; type "bash_code_execution_result"constant`

          - `BASH_CODE_EXECUTION_RESULT("bash_code_execution_result")`

    - `String toolUseId`

    - `JsonValue; type "bash_code_execution_tool_result"constant`

      - `BASH_CODE_EXECUTION_TOOL_RESULT("bash_code_execution_tool_result")`

  - `class TextEditorCodeExecutionToolResultBlock:`

    - `Content content`

      - `class TextEditorCodeExecutionToolResultError:`

        - `TextEditorCodeExecutionToolResultErrorCode errorCode`

          - `INVALID_TOOL_INPUT("invalid_tool_input")`

          - `UNAVAILABLE("unavailable")`

          - `TOO_MANY_REQUESTS("too_many_requests")`

          - `EXECUTION_TIME_EXCEEDED("execution_time_exceeded")`

          - `FILE_NOT_FOUND("file_not_found")`

        - `Optional<String> errorMessage`

        - `JsonValue; type "text_editor_code_execution_tool_result_error"constant`

          - `TEXT_EDITOR_CODE_EXECUTION_TOOL_RESULT_ERROR("text_editor_code_execution_tool_result_error")`

      - `class TextEditorCodeExecutionViewResultBlock:`

        - `String content`

        - `FileType fileType`

          - `TEXT("text")`

          - `IMAGE("image")`

          - `PDF("pdf")`

        - `Optional<Long> numLines`

        - `Optional<Long> startLine`

        - `Optional<Long> totalLines`

        - `JsonValue; type "text_editor_code_execution_view_result"constant`

          - `TEXT_EDITOR_CODE_EXECUTION_VIEW_RESULT("text_editor_code_execution_view_result")`

      - `class TextEditorCodeExecutionCreateResultBlock:`

        - `boolean isFileUpdate`

        - `JsonValue; type "text_editor_code_execution_create_result"constant`

          - `TEXT_EDITOR_CODE_EXECUTION_CREATE_RESULT("text_editor_code_execution_create_result")`

      - `class TextEditorCodeExecutionStrReplaceResultBlock:`

        - `Optional<List<String>> lines`

        - `Optional<Long> newLines`

        - `Optional<Long> newStart`

        - `Optional<Long> oldLines`

        - `Optional<Long> oldStart`

        - `JsonValue; type "text_editor_code_execution_str_replace_result"constant`

          - `TEXT_EDITOR_CODE_EXECUTION_STR_REPLACE_RESULT("text_editor_code_execution_str_replace_result")`

    - `String toolUseId`

    - `JsonValue; type "text_editor_code_execution_tool_result"constant`

      - `TEXT_EDITOR_CODE_EXECUTION_TOOL_RESULT("text_editor_code_execution_tool_result")`

  - `class ToolSearchToolResultBlock:`

    - `Content content`

      - `class ToolSearchToolResultError:`

        - `ToolSearchToolResultErrorCode errorCode`

          - `INVALID_TOOL_INPUT("invalid_tool_input")`

          - `UNAVAILABLE("unavailable")`

          - `TOO_MANY_REQUESTS("too_many_requests")`

          - `EXECUTION_TIME_EXCEEDED("execution_time_exceeded")`

        - `Optional<String> errorMessage`

        - `JsonValue; type "tool_search_tool_result_error"constant`

          - `TOOL_SEARCH_TOOL_RESULT_ERROR("tool_search_tool_result_error")`

      - `class ToolSearchToolSearchResultBlock:`

        - `List<ToolReferenceBlock> toolReferences`

          - `String toolName`

          - `JsonValue; type "tool_reference"constant`

            - `TOOL_REFERENCE("tool_reference")`

        - `JsonValue; type "tool_search_tool_search_result"constant`

          - `TOOL_SEARCH_TOOL_SEARCH_RESULT("tool_search_tool_search_result")`

    - `String toolUseId`

    - `JsonValue; type "tool_search_tool_result"constant`

      - `TOOL_SEARCH_TOOL_RESULT("tool_search_tool_result")`

  - `class ContainerUploadBlock:`

    Response model for a file uploaded to the container.

    - `String fileId`

    - `JsonValue; type "container_upload"constant`

      - `CONTAINER_UPLOAD("container_upload")`

### Content Block Param

- `class ContentBlockParam: A class that can be one of several variants.union`

  Regular text content.

  - `class TextBlockParam:`

    - `String text`

    - `JsonValue; type "text"constant`

      - `TEXT("text")`

    - `Optional<CacheControlEphemeral> cacheControl`

      Create a cache control breakpoint at this content block.

      - `JsonValue; type "ephemeral"constant`

        - `EPHEMERAL("ephemeral")`

      - `Optional<Ttl> ttl`

        The time-to-live for the cache control breakpoint.

        This may be one the following values:

        - `5m`: 5 minutes
        - `1h`: 1 hour

        Defaults to `5m`.

        - `TTL_5M("5m")`

        - `TTL_1H("1h")`

    - `Optional<List<TextCitationParam>> citations`

      - `class CitationCharLocationParam:`

        - `String citedText`

        - `long documentIndex`

        - `Optional<String> documentTitle`

        - `long endCharIndex`

        - `long startCharIndex`

        - `JsonValue; type "char_location"constant`

          - `CHAR_LOCATION("char_location")`

      - `class CitationPageLocationParam:`

        - `String citedText`

        - `long documentIndex`

        - `Optional<String> documentTitle`

        - `long endPageNumber`

        - `long startPageNumber`

        - `JsonValue; type "page_location"constant`

          - `PAGE_LOCATION("page_location")`

      - `class CitationContentBlockLocationParam:`

        - `String citedText`

        - `long documentIndex`

        - `Optional<String> documentTitle`

        - `long endBlockIndex`

        - `long startBlockIndex`

        - `JsonValue; type "content_block_location"constant`

          - `CONTENT_BLOCK_LOCATION("content_block_location")`

      - `class CitationWebSearchResultLocationParam:`

        - `String citedText`

        - `String encryptedIndex`

        - `Optional<String> title`

        - `JsonValue; type "web_search_result_location"constant`

          - `WEB_SEARCH_RESULT_LOCATION("web_search_result_location")`

        - `String url`

      - `class CitationSearchResultLocationParam:`

        - `String citedText`

        - `long endBlockIndex`

        - `long searchResultIndex`

        - `String source`

        - `long startBlockIndex`

        - `Optional<String> title`

        - `JsonValue; type "search_result_location"constant`

          - `SEARCH_RESULT_LOCATION("search_result_location")`

  - `class ImageBlockParam:`

    - `Source source`

      - `class Base64ImageSource:`

        - `String data`

        - `MediaType mediaType`

          - `IMAGE_JPEG("image/jpeg")`

          - `IMAGE_PNG("image/png")`

          - `IMAGE_GIF("image/gif")`

          - `IMAGE_WEBP("image/webp")`

        - `JsonValue; type "base64"constant`

          - `BASE64("base64")`

      - `class UrlImageSource:`

        - `JsonValue; type "url"constant`

          - `URL("url")`

        - `String url`

    - `JsonValue; type "image"constant`

      - `IMAGE("image")`

    - `Optional<CacheControlEphemeral> cacheControl`

      Create a cache control breakpoint at this content block.

      - `JsonValue; type "ephemeral"constant`

        - `EPHEMERAL("ephemeral")`

      - `Optional<Ttl> ttl`

        The time-to-live for the cache control breakpoint.

        This may be one the following values:

        - `5m`: 5 minutes
        - `1h`: 1 hour

        Defaults to `5m`.

        - `TTL_5M("5m")`

        - `TTL_1H("1h")`

  - `class DocumentBlockParam:`

    - `Source source`

      - `class Base64PdfSource:`

        - `String data`

        - `JsonValue; mediaType "application/pdf"constant`

          - `APPLICATION_PDF("application/pdf")`

        - `JsonValue; type "base64"constant`

          - `BASE64("base64")`

      - `class PlainTextSource:`

        - `String data`

        - `JsonValue; mediaType "text/plain"constant`

          - `TEXT_PLAIN("text/plain")`

        - `JsonValue; type "text"constant`

          - `TEXT("text")`

      - `class ContentBlockSource:`

        - `Content content`

          - `String`

          - `List<ContentBlockSourceContent>`

            - `class TextBlockParam:`

              - `String text`

              - `JsonValue; type "text"constant`

                - `TEXT("text")`

              - `Optional<CacheControlEphemeral> cacheControl`

                Create a cache control breakpoint at this content block.

                - `JsonValue; type "ephemeral"constant`

                  - `EPHEMERAL("ephemeral")`

                - `Optional<Ttl> ttl`

                  The time-to-live for the cache control breakpoint.

                  This may be one the following values:

                  - `5m`: 5 minutes
                  - `1h`: 1 hour

                  Defaults to `5m`.

                  - `TTL_5M("5m")`

                  - `TTL_1H("1h")`

              - `Optional<List<TextCitationParam>> citations`

                - `class CitationCharLocationParam:`

                  - `String citedText`

                  - `long documentIndex`

                  - `Optional<String> documentTitle`

                  - `long endCharIndex`

                  - `long startCharIndex`

                  - `JsonValue; type "char_location"constant`

                    - `CHAR_LOCATION("char_location")`

                - `class CitationPageLocationParam:`

                  - `String citedText`

                  - `long documentIndex`

                  - `Optional<String> documentTitle`

                  - `long endPageNumber`

                  - `long startPageNumber`

                  - `JsonValue; type "page_location"constant`

                    - `PAGE_LOCATION("page_location")`

                - `class CitationContentBlockLocationParam:`

                  - `String citedText`

                  - `long documentIndex`

                  - `Optional<String> documentTitle`

                  - `long endBlockIndex`

                  - `long startBlockIndex`

                  - `JsonValue; type "content_block_location"constant`

                    - `CONTENT_BLOCK_LOCATION("content_block_location")`

                - `class CitationWebSearchResultLocationParam:`

                  - `String citedText`

                  - `String encryptedIndex`

                  - `Optional<String> title`

                  - `JsonValue; type "web_search_result_location"constant`

                    - `WEB_SEARCH_RESULT_LOCATION("web_search_result_location")`

                  - `String url`

                - `class CitationSearchResultLocationParam:`

                  - `String citedText`

                  - `long endBlockIndex`

                  - `long searchResultIndex`

                  - `String source`

                  - `long startBlockIndex`

                  - `Optional<String> title`

                  - `JsonValue; type "search_result_location"constant`

                    - `SEARCH_RESULT_LOCATION("search_result_location")`

            - `class ImageBlockParam:`

              - `Source source`

                - `class Base64ImageSource:`

                  - `String data`

                  - `MediaType mediaType`

                    - `IMAGE_JPEG("image/jpeg")`

                    - `IMAGE_PNG("image/png")`

                    - `IMAGE_GIF("image/gif")`

                    - `IMAGE_WEBP("image/webp")`

                  - `JsonValue; type "base64"constant`

                    - `BASE64("base64")`

                - `class UrlImageSource:`

                  - `JsonValue; type "url"constant`

                    - `URL("url")`

                  - `String url`

              - `JsonValue; type "image"constant`

                - `IMAGE("image")`

              - `Optional<CacheControlEphemeral> cacheControl`

                Create a cache control breakpoint at this content block.

                - `JsonValue; type "ephemeral"constant`

                  - `EPHEMERAL("ephemeral")`

                - `Optional<Ttl> ttl`

                  The time-to-live for the cache control breakpoint.

                  This may be one the following values:

                  - `5m`: 5 minutes
                  - `1h`: 1 hour

                  Defaults to `5m`.

                  - `TTL_5M("5m")`

                  - `TTL_1H("1h")`

        - `JsonValue; type "content"constant`

          - `CONTENT("content")`

      - `class UrlPdfSource:`

        - `JsonValue; type "url"constant`

          - `URL("url")`

        - `String url`

    - `JsonValue; type "document"constant`

      - `DOCUMENT("document")`

    - `Optional<CacheControlEphemeral> cacheControl`

      Create a cache control breakpoint at this content block.

      - `JsonValue; type "ephemeral"constant`

        - `EPHEMERAL("ephemeral")`

      - `Optional<Ttl> ttl`

        The time-to-live for the cache control breakpoint.

        This may be one the following values:

        - `5m`: 5 minutes
        - `1h`: 1 hour

        Defaults to `5m`.

        - `TTL_5M("5m")`

        - `TTL_1H("1h")`

    - `Optional<CitationsConfigParam> citations`

      - `Optional<Boolean> enabled`

    - `Optional<String> context`

    - `Optional<String> title`

  - `class SearchResultBlockParam:`

    - `List<TextBlockParam> content`

      - `String text`

      - `JsonValue; type "text"constant`

        - `TEXT("text")`

      - `Optional<CacheControlEphemeral> cacheControl`

        Create a cache control breakpoint at this content block.

        - `JsonValue; type "ephemeral"constant`

          - `EPHEMERAL("ephemeral")`

        - `Optional<Ttl> ttl`

          The time-to-live for the cache control breakpoint.

          This may be one the following values:

          - `5m`: 5 minutes
          - `1h`: 1 hour

          Defaults to `5m`.

          - `TTL_5M("5m")`

          - `TTL_1H("1h")`

      - `Optional<List<TextCitationParam>> citations`

        - `class CitationCharLocationParam:`

          - `String citedText`

          - `long documentIndex`

          - `Optional<String> documentTitle`

          - `long endCharIndex`

          - `long startCharIndex`

          - `JsonValue; type "char_location"constant`

            - `CHAR_LOCATION("char_location")`

        - `class CitationPageLocationParam:`

          - `String citedText`

          - `long documentIndex`

          - `Optional<String> documentTitle`

          - `long endPageNumber`

          - `long startPageNumber`

          - `JsonValue; type "page_location"constant`

            - `PAGE_LOCATION("page_location")`

        - `class CitationContentBlockLocationParam:`

          - `String citedText`

          - `long documentIndex`

          - `Optional<String> documentTitle`

          - `long endBlockIndex`

          - `long startBlockIndex`

          - `JsonValue; type "content_block_location"constant`

            - `CONTENT_BLOCK_LOCATION("content_block_location")`

        - `class CitationWebSearchResultLocationParam:`

          - `String citedText`

          - `String encryptedIndex`

          - `Optional<String> title`

          - `JsonValue; type "web_search_result_location"constant`

            - `WEB_SEARCH_RESULT_LOCATION("web_search_result_location")`

          - `String url`

        - `class CitationSearchResultLocationParam:`

          - `String citedText`

          - `long endBlockIndex`

          - `long searchResultIndex`

          - `String source`

          - `long startBlockIndex`

          - `Optional<String> title`

          - `JsonValue; type "search_result_location"constant`

            - `SEARCH_RESULT_LOCATION("search_result_location")`

    - `String source`

    - `String title`

    - `JsonValue; type "search_result"constant`

      - `SEARCH_RESULT("search_result")`

    - `Optional<CacheControlEphemeral> cacheControl`

      Create a cache control breakpoint at this content block.

      - `JsonValue; type "ephemeral"constant`

        - `EPHEMERAL("ephemeral")`

      - `Optional<Ttl> ttl`

        The time-to-live for the cache control breakpoint.

        This may be one the following values:

        - `5m`: 5 minutes
        - `1h`: 1 hour

        Defaults to `5m`.

        - `TTL_5M("5m")`

        - `TTL_1H("1h")`

    - `Optional<CitationsConfigParam> citations`

      - `Optional<Boolean> enabled`

  - `class ThinkingBlockParam:`

    - `String signature`

    - `String thinking`

    - `JsonValue; type "thinking"constant`

      - `THINKING("thinking")`

  - `class RedactedThinkingBlockParam:`

    - `String data`

    - `JsonValue; type "redacted_thinking"constant`

      - `REDACTED_THINKING("redacted_thinking")`

  - `class ToolUseBlockParam:`

    - `String id`

    - `Input input`

    - `String name`

    - `JsonValue; type "tool_use"constant`

      - `TOOL_USE("tool_use")`

    - `Optional<CacheControlEphemeral> cacheControl`

      Create a cache control breakpoint at this content block.

      - `JsonValue; type "ephemeral"constant`

        - `EPHEMERAL("ephemeral")`

      - `Optional<Ttl> ttl`

        The time-to-live for the cache control breakpoint.

        This may be one the following values:

        - `5m`: 5 minutes
        - `1h`: 1 hour

        Defaults to `5m`.

        - `TTL_5M("5m")`

        - `TTL_1H("1h")`

    - `Optional<Caller> caller`

      Tool invocation directly from the model.

      - `class DirectCaller:`

        Tool invocation directly from the model.

        - `JsonValue; type "direct"constant`

          - `DIRECT("direct")`

      - `class ServerToolCaller:`

        Tool invocation generated by a server-side tool.

        - `String toolId`

        - `JsonValue; type "code_execution_20250825"constant`

          - `CODE_EXECUTION_20250825("code_execution_20250825")`

      - `class ServerToolCaller20260120:`

        - `String toolId`

        - `JsonValue; type "code_execution_20260120"constant`

          - `CODE_EXECUTION_20260120("code_execution_20260120")`

  - `class ToolResultBlockParam:`

    - `String toolUseId`

    - `JsonValue; type "tool_result"constant`

      - `TOOL_RESULT("tool_result")`

    - `Optional<CacheControlEphemeral> cacheControl`

      Create a cache control breakpoint at this content block.

      - `JsonValue; type "ephemeral"constant`

        - `EPHEMERAL("ephemeral")`

      - `Optional<Ttl> ttl`

        The time-to-live for the cache control breakpoint.

        This may be one the following values:

        - `5m`: 5 minutes
        - `1h`: 1 hour

        Defaults to `5m`.

        - `TTL_5M("5m")`

        - `TTL_1H("1h")`

    - `Optional<Content> content`

      - `String`

      - `List<Block>`

        - `class TextBlockParam:`

          - `String text`

          - `JsonValue; type "text"constant`

            - `TEXT("text")`

          - `Optional<CacheControlEphemeral> cacheControl`

            Create a cache control breakpoint at this content block.

            - `JsonValue; type "ephemeral"constant`

              - `EPHEMERAL("ephemeral")`

            - `Optional<Ttl> ttl`

              The time-to-live for the cache control breakpoint.

              This may be one the following values:

              - `5m`: 5 minutes
              - `1h`: 1 hour

              Defaults to `5m`.

              - `TTL_5M("5m")`

              - `TTL_1H("1h")`

          - `Optional<List<TextCitationParam>> citations`

            - `class CitationCharLocationParam:`

              - `String citedText`

              - `long documentIndex`

              - `Optional<String> documentTitle`

              - `long endCharIndex`

              - `long startCharIndex`

              - `JsonValue; type "char_location"constant`

                - `CHAR_LOCATION("char_location")`

            - `class CitationPageLocationParam:`

              - `String citedText`

              - `long documentIndex`

              - `Optional<String> documentTitle`

              - `long endPageNumber`

              - `long startPageNumber`

              - `JsonValue; type "page_location"constant`

                - `PAGE_LOCATION("page_location")`

            - `class CitationContentBlockLocationParam:`

              - `String citedText`

              - `long documentIndex`

              - `Optional<String> documentTitle`

              - `long endBlockIndex`

              - `long startBlockIndex`

              - `JsonValue; type "content_block_location"constant`

                - `CONTENT_BLOCK_LOCATION("content_block_location")`

            - `class CitationWebSearchResultLocationParam:`

              - `String citedText`

              - `String encryptedIndex`

              - `Optional<String> title`

              - `JsonValue; type "web_search_result_location"constant`

                - `WEB_SEARCH_RESULT_LOCATION("web_search_result_location")`

              - `String url`

            - `class CitationSearchResultLocationParam:`

              - `String citedText`

              - `long endBlockIndex`

              - `long searchResultIndex`

              - `String source`

              - `long startBlockIndex`

              - `Optional<String> title`

              - `JsonValue; type "search_result_location"constant`

                - `SEARCH_RESULT_LOCATION("search_result_location")`

        - `class ImageBlockParam:`

          - `Source source`

            - `class Base64ImageSource:`

              - `String data`

              - `MediaType mediaType`

                - `IMAGE_JPEG("image/jpeg")`

                - `IMAGE_PNG("image/png")`

                - `IMAGE_GIF("image/gif")`

                - `IMAGE_WEBP("image/webp")`

              - `JsonValue; type "base64"constant`

                - `BASE64("base64")`

            - `class UrlImageSource:`

              - `JsonValue; type "url"constant`

                - `URL("url")`

              - `String url`

          - `JsonValue; type "image"constant`

            - `IMAGE("image")`

          - `Optional<CacheControlEphemeral> cacheControl`

            Create a cache control breakpoint at this content block.

            - `JsonValue; type "ephemeral"constant`

              - `EPHEMERAL("ephemeral")`

            - `Optional<Ttl> ttl`

              The time-to-live for the cache control breakpoint.

              This may be one the following values:

              - `5m`: 5 minutes
              - `1h`: 1 hour

              Defaults to `5m`.

              - `TTL_5M("5m")`

              - `TTL_1H("1h")`

        - `class SearchResultBlockParam:`

          - `List<TextBlockParam> content`

            - `String text`

            - `JsonValue; type "text"constant`

              - `TEXT("text")`

            - `Optional<CacheControlEphemeral> cacheControl`

              Create a cache control breakpoint at this content block.

              - `JsonValue; type "ephemeral"constant`

                - `EPHEMERAL("ephemeral")`

              - `Optional<Ttl> ttl`

                The time-to-live for the cache control breakpoint.

                This may be one the following values:

                - `5m`: 5 minutes
                - `1h`: 1 hour

                Defaults to `5m`.

                - `TTL_5M("5m")`

                - `TTL_1H("1h")`

            - `Optional<List<TextCitationParam>> citations`

              - `class CitationCharLocationParam:`

                - `String citedText`

                - `long documentIndex`

                - `Optional<String> documentTitle`

                - `long endCharIndex`

                - `long startCharIndex`

                - `JsonValue; type "char_location"constant`

                  - `CHAR_LOCATION("char_location")`

              - `class CitationPageLocationParam:`

                - `String citedText`

                - `long documentIndex`

                - `Optional<String> documentTitle`

                - `long endPageNumber`

                - `long startPageNumber`

                - `JsonValue; type "page_location"constant`

                  - `PAGE_LOCATION("page_location")`

              - `class CitationContentBlockLocationParam:`

                - `String citedText`

                - `long documentIndex`

                - `Optional<String> documentTitle`

                - `long endBlockIndex`

                - `long startBlockIndex`

                - `JsonValue; type "content_block_location"constant`

                  - `CONTENT_BLOCK_LOCATION("content_block_location")`

              - `class CitationWebSearchResultLocationParam:`

                - `String citedText`

                - `String encryptedIndex`

                - `Optional<String> title`

                - `JsonValue; type "web_search_result_location"constant`

                  - `WEB_SEARCH_RESULT_LOCATION("web_search_result_location")`

                - `String url`

              - `class CitationSearchResultLocationParam:`

                - `String citedText`

                - `long endBlockIndex`

                - `long searchResultIndex`

                - `String source`

                - `long startBlockIndex`

                - `Optional<String> title`

                - `JsonValue; type "search_result_location"constant`

                  - `SEARCH_RESULT_LOCATION("search_result_location")`

          - `String source`

          - `String title`

          - `JsonValue; type "search_result"constant`

            - `SEARCH_RESULT("search_result")`

          - `Optional<CacheControlEphemeral> cacheControl`

            Create a cache control breakpoint at this content block.

            - `JsonValue; type "ephemeral"constant`

              - `EPHEMERAL("ephemeral")`

            - `Optional<Ttl> ttl`

              The time-to-live for the cache control breakpoint.

              This may be one the following values:

              - `5m`: 5 minutes
              - `1h`: 1 hour

              Defaults to `5m`.

              - `TTL_5M("5m")`

              - `TTL_1H("1h")`

          - `Optional<CitationsConfigParam> citations`

            - `Optional<Boolean> enabled`

        - `class DocumentBlockParam:`

          - `Source source`

            - `class Base64PdfSource:`

              - `String data`

              - `JsonValue; mediaType "application/pdf"constant`

                - `APPLICATION_PDF("application/pdf")`

              - `JsonValue; type "base64"constant`

                - `BASE64("base64")`

            - `class PlainTextSource:`

              - `String data`

              - `JsonValue; mediaType "text/plain"constant`

                - `TEXT_PLAIN("text/plain")`

              - `JsonValue; type "text"constant`

                - `TEXT("text")`

            - `class ContentBlockSource:`

              - `Content content`

                - `String`

                - `List<ContentBlockSourceContent>`

                  - `class TextBlockParam:`

                    - `String text`

                    - `JsonValue; type "text"constant`

                      - `TEXT("text")`

                    - `Optional<CacheControlEphemeral> cacheControl`

                      Create a cache control breakpoint at this content block.

                      - `JsonValue; type "ephemeral"constant`

                        - `EPHEMERAL("ephemeral")`

                      - `Optional<Ttl> ttl`

                        The time-to-live for the cache control breakpoint.

                        This may be one the following values:

                        - `5m`: 5 minutes
                        - `1h`: 1 hour

                        Defaults to `5m`.

                        - `TTL_5M("5m")`

                        - `TTL_1H("1h")`

                    - `Optional<List<TextCitationParam>> citations`

                      - `class CitationCharLocationParam:`

                        - `String citedText`

                        - `long documentIndex`

                        - `Optional<String> documentTitle`

                        - `long endCharIndex`

                        - `long startCharIndex`

                        - `JsonValue; type "char_location"constant`

                          - `CHAR_LOCATION("char_location")`

                      - `class CitationPageLocationParam:`

                        - `String citedText`

                        - `long documentIndex`

                        - `Optional<String> documentTitle`

                        - `long endPageNumber`

                        - `long startPageNumber`

                        - `JsonValue; type "page_location"constant`

                          - `PAGE_LOCATION("page_location")`

                      - `class CitationContentBlockLocationParam:`

                        - `String citedText`

                        - `long documentIndex`

                        - `Optional<String> documentTitle`

                        - `long endBlockIndex`

                        - `long startBlockIndex`

                        - `JsonValue; type "content_block_location"constant`

                          - `CONTENT_BLOCK_LOCATION("content_block_location")`

                      - `class CitationWebSearchResultLocationParam:`

                        - `String citedText`

                        - `String encryptedIndex`

                        - `Optional<String> title`

                        - `JsonValue; type "web_search_result_location"constant`

                          - `WEB_SEARCH_RESULT_LOCATION("web_search_result_location")`

                        - `String url`

                      - `class CitationSearchResultLocationParam:`

                        - `String citedText`

                        - `long endBlockIndex`

                        - `long searchResultIndex`

                        - `String source`

                        - `long startBlockIndex`

                        - `Optional<String> title`

                        - `JsonValue; type "search_result_location"constant`

                          - `SEARCH_RESULT_LOCATION("search_result_location")`

                  - `class ImageBlockParam:`

                    - `Source source`

                      - `class Base64ImageSource:`

                        - `String data`

                        - `MediaType mediaType`

                          - `IMAGE_JPEG("image/jpeg")`

                          - `IMAGE_PNG("image/png")`

                          - `IMAGE_GIF("image/gif")`

                          - `IMAGE_WEBP("image/webp")`

                        - `JsonValue; type "base64"constant`

                          - `BASE64("base64")`

                      - `class UrlImageSource:`

                        - `JsonValue; type "url"constant`

                          - `URL("url")`

                        - `String url`

                    - `JsonValue; type "image"constant`

                      - `IMAGE("image")`

                    - `Optional<CacheControlEphemeral> cacheControl`

                      Create a cache control breakpoint at this content block.

                      - `JsonValue; type "ephemeral"constant`

                        - `EPHEMERAL("ephemeral")`

                      - `Optional<Ttl> ttl`

                        The time-to-live for the cache control breakpoint.

                        This may be one the following values:

                        - `5m`: 5 minutes
                        - `1h`: 1 hour

                        Defaults to `5m`.

                        - `TTL_5M("5m")`

                        - `TTL_1H("1h")`

              - `JsonValue; type "content"constant`

                - `CONTENT("content")`

            - `class UrlPdfSource:`

              - `JsonValue; type "url"constant`

                - `URL("url")`

              - `String url`

          - `JsonValue; type "document"constant`

            - `DOCUMENT("document")`

          - `Optional<CacheControlEphemeral> cacheControl`

            Create a cache control breakpoint at this content block.

            - `JsonValue; type "ephemeral"constant`

              - `EPHEMERAL("ephemeral")`

            - `Optional<Ttl> ttl`

              The time-to-live for the cache control breakpoint.

              This may be one the following values:

              - `5m`: 5 minutes
              - `1h`: 1 hour

              Defaults to `5m`.

              - `TTL_5M("5m")`

              - `TTL_1H("1h")`

          - `Optional<CitationsConfigParam> citations`

            - `Optional<Boolean> enabled`

          - `Optional<String> context`

          - `Optional<String> title`

        - `class ToolReferenceBlockParam:`

          Tool reference block that can be included in tool_result content.

          - `String toolName`

          - `JsonValue; type "tool_reference"constant`

            - `TOOL_REFERENCE("tool_reference")`

          - `Optional<CacheControlEphemeral> cacheControl`

            Create a cache control breakpoint at this content block.

            - `JsonValue; type "ephemeral"constant`

              - `EPHEMERAL("ephemeral")`

            - `Optional<Ttl> ttl`

              The time-to-live for the cache control breakpoint.

              This may be one the following values:

              - `5m`: 5 minutes
              - `1h`: 1 hour

              Defaults to `5m`.

              - `TTL_5M("5m")`

              - `TTL_1H("1h")`

    - `Optional<Boolean> isError`

  - `class ServerToolUseBlockParam:`

    - `String id`

    - `Input input`

    - `Name name`

      - `WEB_SEARCH("web_search")`

      - `WEB_FETCH("web_fetch")`

      - `CODE_EXECUTION("code_execution")`

      - `BASH_CODE_EXECUTION("bash_code_execution")`

      - `TEXT_EDITOR_CODE_EXECUTION("text_editor_code_execution")`

      - `TOOL_SEARCH_TOOL_REGEX("tool_search_tool_regex")`

      - `TOOL_SEARCH_TOOL_BM25("tool_search_tool_bm25")`

    - `JsonValue; type "server_tool_use"constant`

      - `SERVER_TOOL_USE("server_tool_use")`

    - `Optional<CacheControlEphemeral> cacheControl`

      Create a cache control breakpoint at this content block.

      - `JsonValue; type "ephemeral"constant`

        - `EPHEMERAL("ephemeral")`

      - `Optional<Ttl> ttl`

        The time-to-live for the cache control breakpoint.

        This may be one the following values:

        - `5m`: 5 minutes
        - `1h`: 1 hour

        Defaults to `5m`.

        - `TTL_5M("5m")`

        - `TTL_1H("1h")`

    - `Optional<Caller> caller`

      Tool invocation directly from the model.

      - `class DirectCaller:`

        Tool invocation directly from the model.

        - `JsonValue; type "direct"constant`

          - `DIRECT("direct")`

      - `class ServerToolCaller:`

        Tool invocation generated by a server-side tool.

        - `String toolId`

        - `JsonValue; type "code_execution_20250825"constant`

          - `CODE_EXECUTION_20250825("code_execution_20250825")`

      - `class ServerToolCaller20260120:`

        - `String toolId`

        - `JsonValue; type "code_execution_20260120"constant`

          - `CODE_EXECUTION_20260120("code_execution_20260120")`

  - `class WebSearchToolResultBlockParam:`

    - `WebSearchToolResultBlockParamContent content`

      - `List<WebSearchResultBlockParam>`

        - `String encryptedContent`

        - `String title`

        - `JsonValue; type "web_search_result"constant`

          - `WEB_SEARCH_RESULT("web_search_result")`

        - `String url`

        - `Optional<String> pageAge`

      - `class WebSearchToolRequestError:`

        - `WebSearchToolResultErrorCode errorCode`

          - `INVALID_TOOL_INPUT("invalid_tool_input")`

          - `UNAVAILABLE("unavailable")`

          - `MAX_USES_EXCEEDED("max_uses_exceeded")`

          - `TOO_MANY_REQUESTS("too_many_requests")`

          - `QUERY_TOO_LONG("query_too_long")`

          - `REQUEST_TOO_LARGE("request_too_large")`

        - `JsonValue; type "web_search_tool_result_error"constant`

          - `WEB_SEARCH_TOOL_RESULT_ERROR("web_search_tool_result_error")`

    - `String toolUseId`

    - `JsonValue; type "web_search_tool_result"constant`

      - `WEB_SEARCH_TOOL_RESULT("web_search_tool_result")`

    - `Optional<CacheControlEphemeral> cacheControl`

      Create a cache control breakpoint at this content block.

      - `JsonValue; type "ephemeral"constant`

        - `EPHEMERAL("ephemeral")`

      - `Optional<Ttl> ttl`

        The time-to-live for the cache control breakpoint.

        This may be one the following values:

        - `5m`: 5 minutes
        - `1h`: 1 hour

        Defaults to `5m`.

        - `TTL_5M("5m")`

        - `TTL_1H("1h")`

    - `Optional<Caller> caller`

      Tool invocation directly from the model.

      - `class DirectCaller:`

        Tool invocation directly from the model.

        - `JsonValue; type "direct"constant`

          - `DIRECT("direct")`

      - `class ServerToolCaller:`

        Tool invocation generated by a server-side tool.

        - `String toolId`

        - `JsonValue; type "code_execution_20250825"constant`

          - `CODE_EXECUTION_20250825("code_execution_20250825")`

      - `class ServerToolCaller20260120:`

        - `String toolId`

        - `JsonValue; type "code_execution_20260120"constant`

          - `CODE_EXECUTION_20260120("code_execution_20260120")`

  - `class WebFetchToolResultBlockParam:`

    - `Content content`

      - `class WebFetchToolResultErrorBlockParam:`

        - `WebFetchToolResultErrorCode errorCode`

          - `INVALID_TOOL_INPUT("invalid_tool_input")`

          - `URL_TOO_LONG("url_too_long")`

          - `URL_NOT_ALLOWED("url_not_allowed")`

          - `URL_NOT_ACCESSIBLE("url_not_accessible")`

          - `UNSUPPORTED_CONTENT_TYPE("unsupported_content_type")`

          - `TOO_MANY_REQUESTS("too_many_requests")`

          - `MAX_USES_EXCEEDED("max_uses_exceeded")`

          - `UNAVAILABLE("unavailable")`

        - `JsonValue; type "web_fetch_tool_result_error"constant`

          - `WEB_FETCH_TOOL_RESULT_ERROR("web_fetch_tool_result_error")`

      - `class WebFetchBlockParam:`

        - `DocumentBlockParam content`

          - `Source source`

            - `class Base64PdfSource:`

              - `String data`

              - `JsonValue; mediaType "application/pdf"constant`

                - `APPLICATION_PDF("application/pdf")`

              - `JsonValue; type "base64"constant`

                - `BASE64("base64")`

            - `class PlainTextSource:`

              - `String data`

              - `JsonValue; mediaType "text/plain"constant`

                - `TEXT_PLAIN("text/plain")`

              - `JsonValue; type "text"constant`

                - `TEXT("text")`

            - `class ContentBlockSource:`

              - `Content content`

                - `String`

                - `List<ContentBlockSourceContent>`

                  - `class TextBlockParam:`

                    - `String text`

                    - `JsonValue; type "text"constant`

                      - `TEXT("text")`

                    - `Optional<CacheControlEphemeral> cacheControl`

                      Create a cache control breakpoint at this content block.

                      - `JsonValue; type "ephemeral"constant`

                        - `EPHEMERAL("ephemeral")`

                      - `Optional<Ttl> ttl`

                        The time-to-live for the cache control breakpoint.

                        This may be one the following values:

                        - `5m`: 5 minutes
                        - `1h`: 1 hour

                        Defaults to `5m`.

                        - `TTL_5M("5m")`

                        - `TTL_1H("1h")`

                    - `Optional<List<TextCitationParam>> citations`

                      - `class CitationCharLocationParam:`

                        - `String citedText`

                        - `long documentIndex`

                        - `Optional<String> documentTitle`

                        - `long endCharIndex`

                        - `long startCharIndex`

                        - `JsonValue; type "char_location"constant`

                          - `CHAR_LOCATION("char_location")`

                      - `class CitationPageLocationParam:`

                        - `String citedText`

                        - `long documentIndex`

                        - `Optional<String> documentTitle`

                        - `long endPageNumber`

                        - `long startPageNumber`

                        - `JsonValue; type "page_location"constant`

                          - `PAGE_LOCATION("page_location")`

                      - `class CitationContentBlockLocationParam:`

                        - `String citedText`

                        - `long documentIndex`

                        - `Optional<String> documentTitle`

                        - `long endBlockIndex`

                        - `long startBlockIndex`

                        - `JsonValue; type "content_block_location"constant`

                          - `CONTENT_BLOCK_LOCATION("content_block_location")`

                      - `class CitationWebSearchResultLocationParam:`

                        - `String citedText`

                        - `String encryptedIndex`

                        - `Optional<String> title`

                        - `JsonValue; type "web_search_result_location"constant`

                          - `WEB_SEARCH_RESULT_LOCATION("web_search_result_location")`

                        - `String url`

                      - `class CitationSearchResultLocationParam:`

                        - `String citedText`

                        - `long endBlockIndex`

                        - `long searchResultIndex`

                        - `String source`

                        - `long startBlockIndex`

                        - `Optional<String> title`

                        - `JsonValue; type "search_result_location"constant`

                          - `SEARCH_RESULT_LOCATION("search_result_location")`

                  - `class ImageBlockParam:`

                    - `Source source`

                      - `class Base64ImageSource:`

                        - `String data`

                        - `MediaType mediaType`

                          - `IMAGE_JPEG("image/jpeg")`

                          - `IMAGE_PNG("image/png")`

                          - `IMAGE_GIF("image/gif")`

                          - `IMAGE_WEBP("image/webp")`

                        - `JsonValue; type "base64"constant`

                          - `BASE64("base64")`

                      - `class UrlImageSource:`

                        - `JsonValue; type "url"constant`

                          - `URL("url")`

                        - `String url`

                    - `JsonValue; type "image"constant`

                      - `IMAGE("image")`

                    - `Optional<CacheControlEphemeral> cacheControl`

                      Create a cache control breakpoint at this content block.

                      - `JsonValue; type "ephemeral"constant`

                        - `EPHEMERAL("ephemeral")`

                      - `Optional<Ttl> ttl`

                        The time-to-live for the cache control breakpoint.

                        This may be one the following values:

                        - `5m`: 5 minutes
                        - `1h`: 1 hour

                        Defaults to `5m`.

                        - `TTL_5M("5m")`

                        - `TTL_1H("1h")`

              - `JsonValue; type "content"constant`

                - `CONTENT("content")`

            - `class UrlPdfSource:`

              - `JsonValue; type "url"constant`

                - `URL("url")`

              - `String url`

          - `JsonValue; type "document"constant`

            - `DOCUMENT("document")`

          - `Optional<CacheControlEphemeral> cacheControl`

            Create a cache control breakpoint at this content block.

            - `JsonValue; type "ephemeral"constant`

              - `EPHEMERAL("ephemeral")`

            - `Optional<Ttl> ttl`

              The time-to-live for the cache control breakpoint.

              This may be one the following values:

              - `5m`: 5 minutes
              - `1h`: 1 hour

              Defaults to `5m`.

              - `TTL_5M("5m")`

              - `TTL_1H("1h")`

          - `Optional<CitationsConfigParam> citations`

            - `Optional<Boolean> enabled`

          - `Optional<String> context`

          - `Optional<String> title`

        - `JsonValue; type "web_fetch_result"constant`

          - `WEB_FETCH_RESULT("web_fetch_result")`

        - `String url`

          Fetched content URL

        - `Optional<String> retrievedAt`

          ISO 8601 timestamp when the content was retrieved

    - `String toolUseId`

    - `JsonValue; type "web_fetch_tool_result"constant`

      - `WEB_FETCH_TOOL_RESULT("web_fetch_tool_result")`

    - `Optional<CacheControlEphemeral> cacheControl`

      Create a cache control breakpoint at this content block.

      - `JsonValue; type "ephemeral"constant`

        - `EPHEMERAL("ephemeral")`

      - `Optional<Ttl> ttl`

        The time-to-live for the cache control breakpoint.

        This may be one the following values:

        - `5m`: 5 minutes
        - `1h`: 1 hour

        Defaults to `5m`.

        - `TTL_5M("5m")`

        - `TTL_1H("1h")`

    - `Optional<Caller> caller`

      Tool invocation directly from the model.

      - `class DirectCaller:`

        Tool invocation directly from the model.

        - `JsonValue; type "direct"constant`

          - `DIRECT("direct")`

      - `class ServerToolCaller:`

        Tool invocation generated by a server-side tool.

        - `String toolId`

        - `JsonValue; type "code_execution_20250825"constant`

          - `CODE_EXECUTION_20250825("code_execution_20250825")`

      - `class ServerToolCaller20260120:`

        - `String toolId`

        - `JsonValue; type "code_execution_20260120"constant`

          - `CODE_EXECUTION_20260120("code_execution_20260120")`

  - `class CodeExecutionToolResultBlockParam:`

    - `CodeExecutionToolResultBlockParamContent content`

      Code execution result with encrypted stdout for PFC + web_search results.

      - `class CodeExecutionToolResultErrorParam:`

        - `CodeExecutionToolResultErrorCode errorCode`

          - `INVALID_TOOL_INPUT("invalid_tool_input")`

          - `UNAVAILABLE("unavailable")`

          - `TOO_MANY_REQUESTS("too_many_requests")`

          - `EXECUTION_TIME_EXCEEDED("execution_time_exceeded")`

        - `JsonValue; type "code_execution_tool_result_error"constant`

          - `CODE_EXECUTION_TOOL_RESULT_ERROR("code_execution_tool_result_error")`

      - `class CodeExecutionResultBlockParam:`

        - `List<CodeExecutionOutputBlockParam> content`

          - `String fileId`

          - `JsonValue; type "code_execution_output"constant`

            - `CODE_EXECUTION_OUTPUT("code_execution_output")`

        - `long returnCode`

        - `String stderr`

        - `String stdout`

        - `JsonValue; type "code_execution_result"constant`

          - `CODE_EXECUTION_RESULT("code_execution_result")`

      - `class EncryptedCodeExecutionResultBlockParam:`

        Code execution result with encrypted stdout for PFC + web_search results.

        - `List<CodeExecutionOutputBlockParam> content`

          - `String fileId`

          - `JsonValue; type "code_execution_output"constant`

            - `CODE_EXECUTION_OUTPUT("code_execution_output")`

        - `String encryptedStdout`

        - `long returnCode`

        - `String stderr`

        - `JsonValue; type "encrypted_code_execution_result"constant`

          - `ENCRYPTED_CODE_EXECUTION_RESULT("encrypted_code_execution_result")`

    - `String toolUseId`

    - `JsonValue; type "code_execution_tool_result"constant`

      - `CODE_EXECUTION_TOOL_RESULT("code_execution_tool_result")`

    - `Optional<CacheControlEphemeral> cacheControl`

      Create a cache control breakpoint at this content block.

      - `JsonValue; type "ephemeral"constant`

        - `EPHEMERAL("ephemeral")`

      - `Optional<Ttl> ttl`

        The time-to-live for the cache control breakpoint.

        This may be one the following values:

        - `5m`: 5 minutes
        - `1h`: 1 hour

        Defaults to `5m`.

        - `TTL_5M("5m")`

        - `TTL_1H("1h")`

  - `class BashCodeExecutionToolResultBlockParam:`

    - `Content content`

      - `class BashCodeExecutionToolResultErrorParam:`

        - `BashCodeExecutionToolResultErrorCode errorCode`

          - `INVALID_TOOL_INPUT("invalid_tool_input")`

          - `UNAVAILABLE("unavailable")`

          - `TOO_MANY_REQUESTS("too_many_requests")`

          - `EXECUTION_TIME_EXCEEDED("execution_time_exceeded")`

          - `OUTPUT_FILE_TOO_LARGE("output_file_too_large")`

        - `JsonValue; type "bash_code_execution_tool_result_error"constant`

          - `BASH_CODE_EXECUTION_TOOL_RESULT_ERROR("bash_code_execution_tool_result_error")`

      - `class BashCodeExecutionResultBlockParam:`

        - `List<BashCodeExecutionOutputBlockParam> content`

          - `String fileId`

          - `JsonValue; type "bash_code_execution_output"constant`

            - `BASH_CODE_EXECUTION_OUTPUT("bash_code_execution_output")`

        - `long returnCode`

        - `String stderr`

        - `String stdout`

        - `JsonValue; type "bash_code_execution_result"constant`

          - `BASH_CODE_EXECUTION_RESULT("bash_code_execution_result")`

    - `String toolUseId`

    - `JsonValue; type "bash_code_execution_tool_result"constant`

      - `BASH_CODE_EXECUTION_TOOL_RESULT("bash_code_execution_tool_result")`

    - `Optional<CacheControlEphemeral> cacheControl`

      Create a cache control breakpoint at this content block.

      - `JsonValue; type "ephemeral"constant`

        - `EPHEMERAL("ephemeral")`

      - `Optional<Ttl> ttl`

        The time-to-live for the cache control breakpoint.

        This may be one the following values:

        - `5m`: 5 minutes
        - `1h`: 1 hour

        Defaults to `5m`.

        - `TTL_5M("5m")`

        - `TTL_1H("1h")`

  - `class TextEditorCodeExecutionToolResultBlockParam:`

    - `Content content`

      - `class TextEditorCodeExecutionToolResultErrorParam:`

        - `TextEditorCodeExecutionToolResultErrorCode errorCode`

          - `INVALID_TOOL_INPUT("invalid_tool_input")`

          - `UNAVAILABLE("unavailable")`

          - `TOO_MANY_REQUESTS("too_many_requests")`

          - `EXECUTION_TIME_EXCEEDED("execution_time_exceeded")`

          - `FILE_NOT_FOUND("file_not_found")`

        - `JsonValue; type "text_editor_code_execution_tool_result_error"constant`

          - `TEXT_EDITOR_CODE_EXECUTION_TOOL_RESULT_ERROR("text_editor_code_execution_tool_result_error")`

        - `Optional<String> errorMessage`

      - `class TextEditorCodeExecutionViewResultBlockParam:`

        - `String content`

        - `FileType fileType`

          - `TEXT("text")`

          - `IMAGE("image")`

          - `PDF("pdf")`

        - `JsonValue; type "text_editor_code_execution_view_result"constant`

          - `TEXT_EDITOR_CODE_EXECUTION_VIEW_RESULT("text_editor_code_execution_view_result")`

        - `Optional<Long> numLines`

        - `Optional<Long> startLine`

        - `Optional<Long> totalLines`

      - `class TextEditorCodeExecutionCreateResultBlockParam:`

        - `boolean isFileUpdate`

        - `JsonValue; type "text_editor_code_execution_create_result"constant`

          - `TEXT_EDITOR_CODE_EXECUTION_CREATE_RESULT("text_editor_code_execution_create_result")`

      - `class TextEditorCodeExecutionStrReplaceResultBlockParam:`

        - `JsonValue; type "text_editor_code_execution_str_replace_result"constant`

          - `TEXT_EDITOR_CODE_EXECUTION_STR_REPLACE_RESULT("text_editor_code_execution_str_replace_result")`

        - `Optional<List<String>> lines`

        - `Optional<Long> newLines`

        - `Optional<Long> newStart`

        - `Optional<Long> oldLines`

        - `Optional<Long> oldStart`

    - `String toolUseId`

    - `JsonValue; type "text_editor_code_execution_tool_result"constant`

      - `TEXT_EDITOR_CODE_EXECUTION_TOOL_RESULT("text_editor_code_execution_tool_result")`

    - `Optional<CacheControlEphemeral> cacheControl`

      Create a cache control breakpoint at this content block.

      - `JsonValue; type "ephemeral"constant`

        - `EPHEMERAL("ephemeral")`

      - `Optional<Ttl> ttl`

        The time-to-live for the cache control breakpoint.

        This may be one the following values:

        - `5m`: 5 minutes
        - `1h`: 1 hour

        Defaults to `5m`.

        - `TTL_5M("5m")`

        - `TTL_1H("1h")`

  - `class ToolSearchToolResultBlockParam:`

    - `Content content`

      - `class ToolSearchToolResultErrorParam:`

        - `ToolSearchToolResultErrorCode errorCode`

          - `INVALID_TOOL_INPUT("invalid_tool_input")`

          - `UNAVAILABLE("unavailable")`

          - `TOO_MANY_REQUESTS("too_many_requests")`

          - `EXECUTION_TIME_EXCEEDED("execution_time_exceeded")`

        - `JsonValue; type "tool_search_tool_result_error"constant`

          - `TOOL_SEARCH_TOOL_RESULT_ERROR("tool_search_tool_result_error")`

      - `class ToolSearchToolSearchResultBlockParam:`

        - `List<ToolReferenceBlockParam> toolReferences`

          - `String toolName`

          - `JsonValue; type "tool_reference"constant`

            - `TOOL_REFERENCE("tool_reference")`

          - `Optional<CacheControlEphemeral> cacheControl`

            Create a cache control breakpoint at this content block.

            - `JsonValue; type "ephemeral"constant`

              - `EPHEMERAL("ephemeral")`

            - `Optional<Ttl> ttl`

              The time-to-live for the cache control breakpoint.

              This may be one the following values:

              - `5m`: 5 minutes
              - `1h`: 1 hour

              Defaults to `5m`.

              - `TTL_5M("5m")`

              - `TTL_1H("1h")`

        - `JsonValue; type "tool_search_tool_search_result"constant`

          - `TOOL_SEARCH_TOOL_SEARCH_RESULT("tool_search_tool_search_result")`

    - `String toolUseId`

    - `JsonValue; type "tool_search_tool_result"constant`

      - `TOOL_SEARCH_TOOL_RESULT("tool_search_tool_result")`

    - `Optional<CacheControlEphemeral> cacheControl`

      Create a cache control breakpoint at this content block.

      - `JsonValue; type "ephemeral"constant`

        - `EPHEMERAL("ephemeral")`

      - `Optional<Ttl> ttl`

        The time-to-live for the cache control breakpoint.

        This may be one the following values:

        - `5m`: 5 minutes
        - `1h`: 1 hour

        Defaults to `5m`.

        - `TTL_5M("5m")`

        - `TTL_1H("1h")`

  - `class ContainerUploadBlockParam:`

    A content block that represents a file to be uploaded to the container
    Files uploaded via this block will be available in the container's input directory.

    - `String fileId`

    - `JsonValue; type "container_upload"constant`

      - `CONTAINER_UPLOAD("container_upload")`

    - `Optional<CacheControlEphemeral> cacheControl`

      Create a cache control breakpoint at this content block.

      - `JsonValue; type "ephemeral"constant`

        - `EPHEMERAL("ephemeral")`

      - `Optional<Ttl> ttl`

        The time-to-live for the cache control breakpoint.

        This may be one the following values:

        - `5m`: 5 minutes
        - `1h`: 1 hour

        Defaults to `5m`.

        - `TTL_5M("5m")`

        - `TTL_1H("1h")`

### Content Block Source

- `class ContentBlockSource:`

  - `Content content`

    - `String`

    - `List<ContentBlockSourceContent>`

      - `class TextBlockParam:`

        - `String text`

        - `JsonValue; type "text"constant`

          - `TEXT("text")`

        - `Optional<CacheControlEphemeral> cacheControl`

          Create a cache control breakpoint at this content block.

          - `JsonValue; type "ephemeral"constant`

            - `EPHEMERAL("ephemeral")`

          - `Optional<Ttl> ttl`

            The time-to-live for the cache control breakpoint.

            This may be one the following values:

            - `5m`: 5 minutes
            - `1h`: 1 hour

            Defaults to `5m`.

            - `TTL_5M("5m")`

            - `TTL_1H("1h")`

        - `Optional<List<TextCitationParam>> citations`

          - `class CitationCharLocationParam:`

            - `String citedText`

            - `long documentIndex`

            - `Optional<String> documentTitle`

            - `long endCharIndex`

            - `long startCharIndex`

            - `JsonValue; type "char_location"constant`

              - `CHAR_LOCATION("char_location")`

          - `class CitationPageLocationParam:`

            - `String citedText`

            - `long documentIndex`

            - `Optional<String> documentTitle`

            - `long endPageNumber`

            - `long startPageNumber`

            - `JsonValue; type "page_location"constant`

              - `PAGE_LOCATION("page_location")`

          - `class CitationContentBlockLocationParam:`

            - `String citedText`

            - `long documentIndex`

            - `Optional<String> documentTitle`

            - `long endBlockIndex`

            - `long startBlockIndex`

            - `JsonValue; type "content_block_location"constant`

              - `CONTENT_BLOCK_LOCATION("content_block_location")`

          - `class CitationWebSearchResultLocationParam:`

            - `String citedText`

            - `String encryptedIndex`

            - `Optional<String> title`

            - `JsonValue; type "web_search_result_location"constant`

              - `WEB_SEARCH_RESULT_LOCATION("web_search_result_location")`

            - `String url`

          - `class CitationSearchResultLocationParam:`

            - `String citedText`

            - `long endBlockIndex`

            - `long searchResultIndex`

            - `String source`

            - `long startBlockIndex`

            - `Optional<String> title`

            - `JsonValue; type "search_result_location"constant`

              - `SEARCH_RESULT_LOCATION("search_result_location")`

      - `class ImageBlockParam:`

        - `Source source`

          - `class Base64ImageSource:`

            - `String data`

            - `MediaType mediaType`

              - `IMAGE_JPEG("image/jpeg")`

              - `IMAGE_PNG("image/png")`

              - `IMAGE_GIF("image/gif")`

              - `IMAGE_WEBP("image/webp")`

            - `JsonValue; type "base64"constant`

              - `BASE64("base64")`

          - `class UrlImageSource:`

            - `JsonValue; type "url"constant`

              - `URL("url")`

            - `String url`

        - `JsonValue; type "image"constant`

          - `IMAGE("image")`

        - `Optional<CacheControlEphemeral> cacheControl`

          Create a cache control breakpoint at this content block.

          - `JsonValue; type "ephemeral"constant`

            - `EPHEMERAL("ephemeral")`

          - `Optional<Ttl> ttl`

            The time-to-live for the cache control breakpoint.

            This may be one the following values:

            - `5m`: 5 minutes
            - `1h`: 1 hour

            Defaults to `5m`.

            - `TTL_5M("5m")`

            - `TTL_1H("1h")`

  - `JsonValue; type "content"constant`

    - `CONTENT("content")`

### Content Block Source Content

- `class ContentBlockSourceContent: A class that can be one of several variants.union`

  - `class TextBlockParam:`

    - `String text`

    - `JsonValue; type "text"constant`

      - `TEXT("text")`

    - `Optional<CacheControlEphemeral> cacheControl`

      Create a cache control breakpoint at this content block.

      - `JsonValue; type "ephemeral"constant`

        - `EPHEMERAL("ephemeral")`

      - `Optional<Ttl> ttl`

        The time-to-live for the cache control breakpoint.

        This may be one the following values:

        - `5m`: 5 minutes
        - `1h`: 1 hour

        Defaults to `5m`.

        - `TTL_5M("5m")`

        - `TTL_1H("1h")`

    - `Optional<List<TextCitationParam>> citations`

      - `class CitationCharLocationParam:`

        - `String citedText`

        - `long documentIndex`

        - `Optional<String> documentTitle`

        - `long endCharIndex`

        - `long startCharIndex`

        - `JsonValue; type "char_location"constant`

          - `CHAR_LOCATION("char_location")`

      - `class CitationPageLocationParam:`

        - `String citedText`

        - `long documentIndex`

        - `Optional<String> documentTitle`

        - `long endPageNumber`

        - `long startPageNumber`

        - `JsonValue; type "page_location"constant`

          - `PAGE_LOCATION("page_location")`

      - `class CitationContentBlockLocationParam:`

        - `String citedText`

        - `long documentIndex`

        - `Optional<String> documentTitle`

        - `long endBlockIndex`

        - `long startBlockIndex`

        - `JsonValue; type "content_block_location"constant`

          - `CONTENT_BLOCK_LOCATION("content_block_location")`

      - `class CitationWebSearchResultLocationParam:`

        - `String citedText`

        - `String encryptedIndex`

        - `Optional<String> title`

        - `JsonValue; type "web_search_result_location"constant`

          - `WEB_SEARCH_RESULT_LOCATION("web_search_result_location")`

        - `String url`

      - `class CitationSearchResultLocationParam:`

        - `String citedText`

        - `long endBlockIndex`

        - `long searchResultIndex`

        - `String source`

        - `long startBlockIndex`

        - `Optional<String> title`

        - `JsonValue; type "search_result_location"constant`

          - `SEARCH_RESULT_LOCATION("search_result_location")`

  - `class ImageBlockParam:`

    - `Source source`

      - `class Base64ImageSource:`

        - `String data`

        - `MediaType mediaType`

          - `IMAGE_JPEG("image/jpeg")`

          - `IMAGE_PNG("image/png")`

          - `IMAGE_GIF("image/gif")`

          - `IMAGE_WEBP("image/webp")`

        - `JsonValue; type "base64"constant`

          - `BASE64("base64")`

      - `class UrlImageSource:`

        - `JsonValue; type "url"constant`

          - `URL("url")`

        - `String url`

    - `JsonValue; type "image"constant`

      - `IMAGE("image")`

    - `Optional<CacheControlEphemeral> cacheControl`

      Create a cache control breakpoint at this content block.

      - `JsonValue; type "ephemeral"constant`

        - `EPHEMERAL("ephemeral")`

      - `Optional<Ttl> ttl`

        The time-to-live for the cache control breakpoint.

        This may be one the following values:

        - `5m`: 5 minutes
        - `1h`: 1 hour

        Defaults to `5m`.

        - `TTL_5M("5m")`

        - `TTL_1H("1h")`

### Direct Caller

- `class DirectCaller:`

  Tool invocation directly from the model.

  - `JsonValue; type "direct"constant`

    - `DIRECT("direct")`

### Document Block

- `class DocumentBlock:`

  - `Optional<CitationsConfig> citations`

    Citation configuration for the document

    - `boolean enabled`

  - `Source source`

    - `class Base64PdfSource:`

      - `String data`

      - `JsonValue; mediaType "application/pdf"constant`

        - `APPLICATION_PDF("application/pdf")`

      - `JsonValue; type "base64"constant`

        - `BASE64("base64")`

    - `class PlainTextSource:`

      - `String data`

      - `JsonValue; mediaType "text/plain"constant`

        - `TEXT_PLAIN("text/plain")`

      - `JsonValue; type "text"constant`

        - `TEXT("text")`

  - `Optional<String> title`

    The title of the document

  - `JsonValue; type "document"constant`

    - `DOCUMENT("document")`

### Document Block Param

- `class DocumentBlockParam:`

  - `Source source`

    - `class Base64PdfSource:`

      - `String data`

      - `JsonValue; mediaType "application/pdf"constant`

        - `APPLICATION_PDF("application/pdf")`

      - `JsonValue; type "base64"constant`

        - `BASE64("base64")`

    - `class PlainTextSource:`

      - `String data`

      - `JsonValue; mediaType "text/plain"constant`

        - `TEXT_PLAIN("text/plain")`

      - `JsonValue; type "text"constant`

        - `TEXT("text")`

    - `class ContentBlockSource:`

      - `Content content`

        - `String`

        - `List<ContentBlockSourceContent>`

          - `class TextBlockParam:`

            - `String text`

            - `JsonValue; type "text"constant`

              - `TEXT("text")`

            - `Optional<CacheControlEphemeral> cacheControl`

              Create a cache control breakpoint at this content block.

              - `JsonValue; type "ephemeral"constant`

                - `EPHEMERAL("ephemeral")`

              - `Optional<Ttl> ttl`

                The time-to-live for the cache control breakpoint.

                This may be one the following values:

                - `5m`: 5 minutes
                - `1h`: 1 hour

                Defaults to `5m`.

                - `TTL_5M("5m")`

                - `TTL_1H("1h")`

            - `Optional<List<TextCitationParam>> citations`

              - `class CitationCharLocationParam:`

                - `String citedText`

                - `long documentIndex`

                - `Optional<String> documentTitle`

                - `long endCharIndex`

                - `long startCharIndex`

                - `JsonValue; type "char_location"constant`

                  - `CHAR_LOCATION("char_location")`

              - `class CitationPageLocationParam:`

                - `String citedText`

                - `long documentIndex`

                - `Optional<String> documentTitle`

                - `long endPageNumber`

                - `long startPageNumber`

                - `JsonValue; type "page_location"constant`

                  - `PAGE_LOCATION("page_location")`

              - `class CitationContentBlockLocationParam:`

                - `String citedText`

                - `long documentIndex`

                - `Optional<String> documentTitle`

                - `long endBlockIndex`

                - `long startBlockIndex`

                - `JsonValue; type "content_block_location"constant`

                  - `CONTENT_BLOCK_LOCATION("content_block_location")`

              - `class CitationWebSearchResultLocationParam:`

                - `String citedText`

                - `String encryptedIndex`

                - `Optional<String> title`

                - `JsonValue; type "web_search_result_location"constant`

                  - `WEB_SEARCH_RESULT_LOCATION("web_search_result_location")`

                - `String url`

              - `class CitationSearchResultLocationParam:`

                - `String citedText`

                - `long endBlockIndex`

                - `long searchResultIndex`

                - `String source`

                - `long startBlockIndex`

                - `Optional<String> title`

                - `JsonValue; type "search_result_location"constant`

                  - `SEARCH_RESULT_LOCATION("search_result_location")`

          - `class ImageBlockParam:`

            - `Source source`

              - `class Base64ImageSource:`

                - `String data`

                - `MediaType mediaType`

                  - `IMAGE_JPEG("image/jpeg")`

                  - `IMAGE_PNG("image/png")`

                  - `IMAGE_GIF("image/gif")`

                  - `IMAGE_WEBP("image/webp")`

                - `JsonValue; type "base64"constant`

                  - `BASE64("base64")`

              - `class UrlImageSource:`

                - `JsonValue; type "url"constant`

                  - `URL("url")`

                - `String url`

            - `JsonValue; type "image"constant`

              - `IMAGE("image")`

            - `Optional<CacheControlEphemeral> cacheControl`

              Create a cache control breakpoint at this content block.

              - `JsonValue; type "ephemeral"constant`

                - `EPHEMERAL("ephemeral")`

              - `Optional<Ttl> ttl`

                The time-to-live for the cache control breakpoint.

                This may be one the following values:

                - `5m`: 5 minutes
                - `1h`: 1 hour

                Defaults to `5m`.

                - `TTL_5M("5m")`

                - `TTL_1H("1h")`

      - `JsonValue; type "content"constant`

        - `CONTENT("content")`

    - `class UrlPdfSource:`

      - `JsonValue; type "url"constant`

        - `URL("url")`

      - `String url`

  - `JsonValue; type "document"constant`

    - `DOCUMENT("document")`

  - `Optional<CacheControlEphemeral> cacheControl`

    Create a cache control breakpoint at this content block.

    - `JsonValue; type "ephemeral"constant`

      - `EPHEMERAL("ephemeral")`

    - `Optional<Ttl> ttl`

      The time-to-live for the cache control breakpoint.

      This may be one the following values:

      - `5m`: 5 minutes
      - `1h`: 1 hour

      Defaults to `5m`.

      - `TTL_5M("5m")`

      - `TTL_1H("1h")`

  - `Optional<CitationsConfigParam> citations`

    - `Optional<Boolean> enabled`

  - `Optional<String> context`

  - `Optional<String> title`

### Encrypted Code Execution Result Block

- `class EncryptedCodeExecutionResultBlock:`

  Code execution result with encrypted stdout for PFC + web_search results.

  - `List<CodeExecutionOutputBlock> content`

    - `String fileId`

    - `JsonValue; type "code_execution_output"constant`

      - `CODE_EXECUTION_OUTPUT("code_execution_output")`

  - `String encryptedStdout`

  - `long returnCode`

  - `String stderr`

  - `JsonValue; type "encrypted_code_execution_result"constant`

    - `ENCRYPTED_CODE_EXECUTION_RESULT("encrypted_code_execution_result")`

### Encrypted Code Execution Result Block Param

- `class EncryptedCodeExecutionResultBlockParam:`

  Code execution result with encrypted stdout for PFC + web_search results.

  - `List<CodeExecutionOutputBlockParam> content`

    - `String fileId`

    - `JsonValue; type "code_execution_output"constant`

      - `CODE_EXECUTION_OUTPUT("code_execution_output")`

  - `String encryptedStdout`

  - `long returnCode`

  - `String stderr`

  - `JsonValue; type "encrypted_code_execution_result"constant`

    - `ENCRYPTED_CODE_EXECUTION_RESULT("encrypted_code_execution_result")`

### Image Block Param

- `class ImageBlockParam:`

  - `Source source`

    - `class Base64ImageSource:`

      - `String data`

      - `MediaType mediaType`

        - `IMAGE_JPEG("image/jpeg")`

        - `IMAGE_PNG("image/png")`

        - `IMAGE_GIF("image/gif")`

        - `IMAGE_WEBP("image/webp")`

      - `JsonValue; type "base64"constant`

        - `BASE64("base64")`

    - `class UrlImageSource:`

      - `JsonValue; type "url"constant`

        - `URL("url")`

      - `String url`

  - `JsonValue; type "image"constant`

    - `IMAGE("image")`

  - `Optional<CacheControlEphemeral> cacheControl`

    Create a cache control breakpoint at this content block.

    - `JsonValue; type "ephemeral"constant`

      - `EPHEMERAL("ephemeral")`

    - `Optional<Ttl> ttl`

      The time-to-live for the cache control breakpoint.

      This may be one the following values:

      - `5m`: 5 minutes
      - `1h`: 1 hour

      Defaults to `5m`.

      - `TTL_5M("5m")`

      - `TTL_1H("1h")`

### Input JSON Delta

- `class InputJsonDelta:`

  - `String partialJson`

  - `JsonValue; type "input_json_delta"constant`

    - `INPUT_JSON_DELTA("input_json_delta")`

### JSON Output Format

- `class JsonOutputFormat:`

  - `Schema schema`

    The JSON schema of the format

  - `JsonValue; type "json_schema"constant`

    - `JSON_SCHEMA("json_schema")`

### Memory Tool 20250818

- `class MemoryTool20250818:`

  - `JsonValue; name "memory"constant`

    Name of the tool.

    This is how the tool will be called by the model and in `tool_use` blocks.

    - `MEMORY("memory")`

  - `JsonValue; type "memory_20250818"constant`

    - `MEMORY_20250818("memory_20250818")`

  - `Optional<List<AllowedCaller>> allowedCallers`

    - `DIRECT("direct")`

    - `CODE_EXECUTION_20250825("code_execution_20250825")`

    - `CODE_EXECUTION_20260120("code_execution_20260120")`

  - `Optional<CacheControlEphemeral> cacheControl`

    Create a cache control breakpoint at this content block.

    - `JsonValue; type "ephemeral"constant`

      - `EPHEMERAL("ephemeral")`

    - `Optional<Ttl> ttl`

      The time-to-live for the cache control breakpoint.

      This may be one the following values:

      - `5m`: 5 minutes
      - `1h`: 1 hour

      Defaults to `5m`.

      - `TTL_5M("5m")`

      - `TTL_1H("1h")`

  - `Optional<Boolean> deferLoading`

    If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

  - `Optional<List<InputExample>> inputExamples`

  - `Optional<Boolean> strict`

    When true, guarantees schema validation on tool names and inputs

### Message

- `class Message:`

  - `String id`

    Unique object identifier.

    The format and length of IDs may change over time.

  - `Optional<Container> container`

    Information about the container used in the request (for the code execution tool)

    - `String id`

      Identifier for the container used in this request

    - `LocalDateTime expiresAt`

      The time at which the container will expire.

  - `List<ContentBlock> content`

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

    - `class TextBlock:`

      - `Optional<List<TextCitation>> citations`

        Citations supporting the text block.

        The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

        - `class CitationCharLocation:`

          - `String citedText`

          - `long documentIndex`

          - `Optional<String> documentTitle`

          - `long endCharIndex`

          - `Optional<String> fileId`

          - `long startCharIndex`

          - `JsonValue; type "char_location"constant`

            - `CHAR_LOCATION("char_location")`

        - `class CitationPageLocation:`

          - `String citedText`

          - `long documentIndex`

          - `Optional<String> documentTitle`

          - `long endPageNumber`

          - `Optional<String> fileId`

          - `long startPageNumber`

          - `JsonValue; type "page_location"constant`

            - `PAGE_LOCATION("page_location")`

        - `class CitationContentBlockLocation:`

          - `String citedText`

          - `long documentIndex`

          - `Optional<String> documentTitle`

          - `long endBlockIndex`

          - `Optional<String> fileId`

          - `long startBlockIndex`

          - `JsonValue; type "content_block_location"constant`

            - `CONTENT_BLOCK_LOCATION("content_block_location")`

        - `class CitationsWebSearchResultLocation:`

          - `String citedText`

          - `String encryptedIndex`

          - `Optional<String> title`

          - `JsonValue; type "web_search_result_location"constant`

            - `WEB_SEARCH_RESULT_LOCATION("web_search_result_location")`

          - `String url`

        - `class CitationsSearchResultLocation:`

          - `String citedText`

          - `long endBlockIndex`

          - `long searchResultIndex`

          - `String source`

          - `long startBlockIndex`

          - `Optional<String> title`

          - `JsonValue; type "search_result_location"constant`

            - `SEARCH_RESULT_LOCATION("search_result_location")`

      - `String text`

      - `JsonValue; type "text"constant`

        - `TEXT("text")`

    - `class ThinkingBlock:`

      - `String signature`

      - `String thinking`

      - `JsonValue; type "thinking"constant`

        - `THINKING("thinking")`

    - `class RedactedThinkingBlock:`

      - `String data`

      - `JsonValue; type "redacted_thinking"constant`

        - `REDACTED_THINKING("redacted_thinking")`

    - `class ToolUseBlock:`

      - `String id`

      - `Caller caller`

        Tool invocation directly from the model.

        - `class DirectCaller:`

          Tool invocation directly from the model.

          - `JsonValue; type "direct"constant`

            - `DIRECT("direct")`

        - `class ServerToolCaller:`

          Tool invocation generated by a server-side tool.

          - `String toolId`

          - `JsonValue; type "code_execution_20250825"constant`

            - `CODE_EXECUTION_20250825("code_execution_20250825")`

        - `class ServerToolCaller20260120:`

          - `String toolId`

          - `JsonValue; type "code_execution_20260120"constant`

            - `CODE_EXECUTION_20260120("code_execution_20260120")`

      - `Input input`

      - `String name`

      - `JsonValue; type "tool_use"constant`

        - `TOOL_USE("tool_use")`

    - `class ServerToolUseBlock:`

      - `String id`

      - `Caller caller`

        Tool invocation directly from the model.

        - `class DirectCaller:`

          Tool invocation directly from the model.

          - `JsonValue; type "direct"constant`

            - `DIRECT("direct")`

        - `class ServerToolCaller:`

          Tool invocation generated by a server-side tool.

          - `String toolId`

          - `JsonValue; type "code_execution_20250825"constant`

            - `CODE_EXECUTION_20250825("code_execution_20250825")`

        - `class ServerToolCaller20260120:`

          - `String toolId`

          - `JsonValue; type "code_execution_20260120"constant`

            - `CODE_EXECUTION_20260120("code_execution_20260120")`

      - `Input input`

      - `Name name`

        - `WEB_SEARCH("web_search")`

        - `WEB_FETCH("web_fetch")`

        - `CODE_EXECUTION("code_execution")`

        - `BASH_CODE_EXECUTION("bash_code_execution")`

        - `TEXT_EDITOR_CODE_EXECUTION("text_editor_code_execution")`

        - `TOOL_SEARCH_TOOL_REGEX("tool_search_tool_regex")`

        - `TOOL_SEARCH_TOOL_BM25("tool_search_tool_bm25")`

      - `JsonValue; type "server_tool_use"constant`

        - `SERVER_TOOL_USE("server_tool_use")`

    - `class WebSearchToolResultBlock:`

      - `Caller caller`

        Tool invocation directly from the model.

        - `class DirectCaller:`

          Tool invocation directly from the model.

          - `JsonValue; type "direct"constant`

            - `DIRECT("direct")`

        - `class ServerToolCaller:`

          Tool invocation generated by a server-side tool.

          - `String toolId`

          - `JsonValue; type "code_execution_20250825"constant`

            - `CODE_EXECUTION_20250825("code_execution_20250825")`

        - `class ServerToolCaller20260120:`

          - `String toolId`

          - `JsonValue; type "code_execution_20260120"constant`

            - `CODE_EXECUTION_20260120("code_execution_20260120")`

      - `WebSearchToolResultBlockContent content`

        - `class WebSearchToolResultError:`

          - `WebSearchToolResultErrorCode errorCode`

            - `INVALID_TOOL_INPUT("invalid_tool_input")`

            - `UNAVAILABLE("unavailable")`

            - `MAX_USES_EXCEEDED("max_uses_exceeded")`

            - `TOO_MANY_REQUESTS("too_many_requests")`

            - `QUERY_TOO_LONG("query_too_long")`

            - `REQUEST_TOO_LARGE("request_too_large")`

          - `JsonValue; type "web_search_tool_result_error"constant`

            - `WEB_SEARCH_TOOL_RESULT_ERROR("web_search_tool_result_error")`

        - `List<WebSearchResultBlock>`

          - `String encryptedContent`

          - `Optional<String> pageAge`

          - `String title`

          - `JsonValue; type "web_search_result"constant`

            - `WEB_SEARCH_RESULT("web_search_result")`

          - `String url`

      - `String toolUseId`

      - `JsonValue; type "web_search_tool_result"constant`

        - `WEB_SEARCH_TOOL_RESULT("web_search_tool_result")`

    - `class WebFetchToolResultBlock:`

      - `Caller caller`

        Tool invocation directly from the model.

        - `class DirectCaller:`

          Tool invocation directly from the model.

          - `JsonValue; type "direct"constant`

            - `DIRECT("direct")`

        - `class ServerToolCaller:`

          Tool invocation generated by a server-side tool.

          - `String toolId`

          - `JsonValue; type "code_execution_20250825"constant`

            - `CODE_EXECUTION_20250825("code_execution_20250825")`

        - `class ServerToolCaller20260120:`

          - `String toolId`

          - `JsonValue; type "code_execution_20260120"constant`

            - `CODE_EXECUTION_20260120("code_execution_20260120")`

      - `Content content`

        - `class WebFetchToolResultErrorBlock:`

          - `WebFetchToolResultErrorCode errorCode`

            - `INVALID_TOOL_INPUT("invalid_tool_input")`

            - `URL_TOO_LONG("url_too_long")`

            - `URL_NOT_ALLOWED("url_not_allowed")`

            - `URL_NOT_ACCESSIBLE("url_not_accessible")`

            - `UNSUPPORTED_CONTENT_TYPE("unsupported_content_type")`

            - `TOO_MANY_REQUESTS("too_many_requests")`

            - `MAX_USES_EXCEEDED("max_uses_exceeded")`

            - `UNAVAILABLE("unavailable")`

          - `JsonValue; type "web_fetch_tool_result_error"constant`

            - `WEB_FETCH_TOOL_RESULT_ERROR("web_fetch_tool_result_error")`

        - `class WebFetchBlock:`

          - `DocumentBlock content`

            - `Optional<CitationsConfig> citations`

              Citation configuration for the document

              - `boolean enabled`

            - `Source source`

              - `class Base64PdfSource:`

                - `String data`

                - `JsonValue; mediaType "application/pdf"constant`

                  - `APPLICATION_PDF("application/pdf")`

                - `JsonValue; type "base64"constant`

                  - `BASE64("base64")`

              - `class PlainTextSource:`

                - `String data`

                - `JsonValue; mediaType "text/plain"constant`

                  - `TEXT_PLAIN("text/plain")`

                - `JsonValue; type "text"constant`

                  - `TEXT("text")`

            - `Optional<String> title`

              The title of the document

            - `JsonValue; type "document"constant`

              - `DOCUMENT("document")`

          - `Optional<String> retrievedAt`

            ISO 8601 timestamp when the content was retrieved

          - `JsonValue; type "web_fetch_result"constant`

            - `WEB_FETCH_RESULT("web_fetch_result")`

          - `String url`

            Fetched content URL

      - `String toolUseId`

      - `JsonValue; type "web_fetch_tool_result"constant`

        - `WEB_FETCH_TOOL_RESULT("web_fetch_tool_result")`

    - `class CodeExecutionToolResultBlock:`

      - `CodeExecutionToolResultBlockContent content`

        Code execution result with encrypted stdout for PFC + web_search results.

        - `class CodeExecutionToolResultError:`

          - `CodeExecutionToolResultErrorCode errorCode`

            - `INVALID_TOOL_INPUT("invalid_tool_input")`

            - `UNAVAILABLE("unavailable")`

            - `TOO_MANY_REQUESTS("too_many_requests")`

            - `EXECUTION_TIME_EXCEEDED("execution_time_exceeded")`

          - `JsonValue; type "code_execution_tool_result_error"constant`

            - `CODE_EXECUTION_TOOL_RESULT_ERROR("code_execution_tool_result_error")`

        - `class CodeExecutionResultBlock:`

          - `List<CodeExecutionOutputBlock> content`

            - `String fileId`

            - `JsonValue; type "code_execution_output"constant`

              - `CODE_EXECUTION_OUTPUT("code_execution_output")`

          - `long returnCode`

          - `String stderr`

          - `String stdout`

          - `JsonValue; type "code_execution_result"constant`

            - `CODE_EXECUTION_RESULT("code_execution_result")`

        - `class EncryptedCodeExecutionResultBlock:`

          Code execution result with encrypted stdout for PFC + web_search results.

          - `List<CodeExecutionOutputBlock> content`

            - `String fileId`

            - `JsonValue; type "code_execution_output"constant`

              - `CODE_EXECUTION_OUTPUT("code_execution_output")`

          - `String encryptedStdout`

          - `long returnCode`

          - `String stderr`

          - `JsonValue; type "encrypted_code_execution_result"constant`

            - `ENCRYPTED_CODE_EXECUTION_RESULT("encrypted_code_execution_result")`

      - `String toolUseId`

      - `JsonValue; type "code_execution_tool_result"constant`

        - `CODE_EXECUTION_TOOL_RESULT("code_execution_tool_result")`

    - `class BashCodeExecutionToolResultBlock:`

      - `Content content`

        - `class BashCodeExecutionToolResultError:`

          - `BashCodeExecutionToolResultErrorCode errorCode`

            - `INVALID_TOOL_INPUT("invalid_tool_input")`

            - `UNAVAILABLE("unavailable")`

            - `TOO_MANY_REQUESTS("too_many_requests")`

            - `EXECUTION_TIME_EXCEEDED("execution_time_exceeded")`

            - `OUTPUT_FILE_TOO_LARGE("output_file_too_large")`

          - `JsonValue; type "bash_code_execution_tool_result_error"constant`

            - `BASH_CODE_EXECUTION_TOOL_RESULT_ERROR("bash_code_execution_tool_result_error")`

        - `class BashCodeExecutionResultBlock:`

          - `List<BashCodeExecutionOutputBlock> content`

            - `String fileId`

            - `JsonValue; type "bash_code_execution_output"constant`

              - `BASH_CODE_EXECUTION_OUTPUT("bash_code_execution_output")`

          - `long returnCode`

          - `String stderr`

          - `String stdout`

          - `JsonValue; type "bash_code_execution_result"constant`

            - `BASH_CODE_EXECUTION_RESULT("bash_code_execution_result")`

      - `String toolUseId`

      - `JsonValue; type "bash_code_execution_tool_result"constant`

        - `BASH_CODE_EXECUTION_TOOL_RESULT("bash_code_execution_tool_result")`

    - `class TextEditorCodeExecutionToolResultBlock:`

      - `Content content`

        - `class TextEditorCodeExecutionToolResultError:`

          - `TextEditorCodeExecutionToolResultErrorCode errorCode`

            - `INVALID_TOOL_INPUT("invalid_tool_input")`

            - `UNAVAILABLE("unavailable")`

            - `TOO_MANY_REQUESTS("too_many_requests")`

            - `EXECUTION_TIME_EXCEEDED("execution_time_exceeded")`

            - `FILE_NOT_FOUND("file_not_found")`

          - `Optional<String> errorMessage`

          - `JsonValue; type "text_editor_code_execution_tool_result_error"constant`

            - `TEXT_EDITOR_CODE_EXECUTION_TOOL_RESULT_ERROR("text_editor_code_execution_tool_result_error")`

        - `class TextEditorCodeExecutionViewResultBlock:`

          - `String content`

          - `FileType fileType`

            - `TEXT("text")`

            - `IMAGE("image")`

            - `PDF("pdf")`

          - `Optional<Long> numLines`

          - `Optional<Long> startLine`

          - `Optional<Long> totalLines`

          - `JsonValue; type "text_editor_code_execution_view_result"constant`

            - `TEXT_EDITOR_CODE_EXECUTION_VIEW_RESULT("text_editor_code_execution_view_result")`

        - `class TextEditorCodeExecutionCreateResultBlock:`

          - `boolean isFileUpdate`

          - `JsonValue; type "text_editor_code_execution_create_result"constant`

            - `TEXT_EDITOR_CODE_EXECUTION_CREATE_RESULT("text_editor_code_execution_create_result")`

        - `class TextEditorCodeExecutionStrReplaceResultBlock:`

          - `Optional<List<String>> lines`

          - `Optional<Long> newLines`

          - `Optional<Long> newStart`

          - `Optional<Long> oldLines`

          - `Optional<Long> oldStart`

          - `JsonValue; type "text_editor_code_execution_str_replace_result"constant`

            - `TEXT_EDITOR_CODE_EXECUTION_STR_REPLACE_RESULT("text_editor_code_execution_str_replace_result")`

      - `String toolUseId`

      - `JsonValue; type "text_editor_code_execution_tool_result"constant`

        - `TEXT_EDITOR_CODE_EXECUTION_TOOL_RESULT("text_editor_code_execution_tool_result")`

    - `class ToolSearchToolResultBlock:`

      - `Content content`

        - `class ToolSearchToolResultError:`

          - `ToolSearchToolResultErrorCode errorCode`

            - `INVALID_TOOL_INPUT("invalid_tool_input")`

            - `UNAVAILABLE("unavailable")`

            - `TOO_MANY_REQUESTS("too_many_requests")`

            - `EXECUTION_TIME_EXCEEDED("execution_time_exceeded")`

          - `Optional<String> errorMessage`

          - `JsonValue; type "tool_search_tool_result_error"constant`

            - `TOOL_SEARCH_TOOL_RESULT_ERROR("tool_search_tool_result_error")`

        - `class ToolSearchToolSearchResultBlock:`

          - `List<ToolReferenceBlock> toolReferences`

            - `String toolName`

            - `JsonValue; type "tool_reference"constant`

              - `TOOL_REFERENCE("tool_reference")`

          - `JsonValue; type "tool_search_tool_search_result"constant`

            - `TOOL_SEARCH_TOOL_SEARCH_RESULT("tool_search_tool_search_result")`

      - `String toolUseId`

      - `JsonValue; type "tool_search_tool_result"constant`

        - `TOOL_SEARCH_TOOL_RESULT("tool_search_tool_result")`

    - `class ContainerUploadBlock:`

      Response model for a file uploaded to the container.

      - `String fileId`

      - `JsonValue; type "container_upload"constant`

        - `CONTAINER_UPLOAD("container_upload")`

  - `Model model`

    The model that will complete your prompt.

    See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

    - `CLAUDE_OPUS_4_6("claude-opus-4-6")`

      Most intelligent model for building agents and coding

    - `CLAUDE_SONNET_4_6("claude-sonnet-4-6")`

      Frontier intelligence at scale — built for coding, agents, and enterprise workflows

    - `CLAUDE_OPUS_4_5_20251101("claude-opus-4-5-20251101")`

      Premium model combining maximum intelligence with practical performance

    - `CLAUDE_OPUS_4_5("claude-opus-4-5")`

      Premium model combining maximum intelligence with practical performance

    - `CLAUDE_3_7_SONNET_LATEST("claude-3-7-sonnet-latest")`

      High-performance model with early extended thinking

    - `CLAUDE_3_7_SONNET_20250219("claude-3-7-sonnet-20250219")`

      High-performance model with early extended thinking

    - `CLAUDE_3_5_HAIKU_LATEST("claude-3-5-haiku-latest")`

      Fastest and most compact model for near-instant responsiveness

    - `CLAUDE_3_5_HAIKU_20241022("claude-3-5-haiku-20241022")`

      Our fastest model

    - `CLAUDE_HAIKU_4_5("claude-haiku-4-5")`

      Hybrid model, capable of near-instant responses and extended thinking

    - `CLAUDE_HAIKU_4_5_20251001("claude-haiku-4-5-20251001")`

      Hybrid model, capable of near-instant responses and extended thinking

    - `CLAUDE_SONNET_4_20250514("claude-sonnet-4-20250514")`

      High-performance model with extended thinking

    - `CLAUDE_SONNET_4_0("claude-sonnet-4-0")`

      High-performance model with extended thinking

    - `CLAUDE_4_SONNET_20250514("claude-4-sonnet-20250514")`

      High-performance model with extended thinking

    - `CLAUDE_SONNET_4_5("claude-sonnet-4-5")`

      Our best model for real-world agents and coding

    - `CLAUDE_SONNET_4_5_20250929("claude-sonnet-4-5-20250929")`

      Our best model for real-world agents and coding

    - `CLAUDE_OPUS_4_0("claude-opus-4-0")`

      Our most capable model

    - `CLAUDE_OPUS_4_20250514("claude-opus-4-20250514")`

      Our most capable model

    - `CLAUDE_4_OPUS_20250514("claude-4-opus-20250514")`

      Our most capable model

    - `CLAUDE_OPUS_4_1_20250805("claude-opus-4-1-20250805")`

      Our most capable model

    - `CLAUDE_3_OPUS_LATEST("claude-3-opus-latest")`

      Excels at writing and complex tasks

    - `CLAUDE_3_OPUS_20240229("claude-3-opus-20240229")`

      Excels at writing and complex tasks

    - `CLAUDE_3_HAIKU_20240307("claude-3-haiku-20240307")`

      Our previous most fast and cost-effective

  - `JsonValue; role "assistant"constant`

    Conversational role of the generated message.

    This will always be `"assistant"`.

    - `ASSISTANT("assistant")`

  - `Optional<StopReason> stopReason`

    The reason that we stopped.

    This may be one the following values:

    * `"end_turn"`: the model reached a natural stopping point
    * `"max_tokens"`: we exceeded the requested `max_tokens` or the model's maximum
    * `"stop_sequence"`: one of your provided custom `stop_sequences` was generated
    * `"tool_use"`: the model invoked one or more tools
    * `"pause_turn"`: we paused a long-running turn. You may provide the response back as-is in a subsequent request to let the model continue.
    * `"refusal"`: when streaming classifiers intervene to handle potential policy violations

    In non-streaming mode this value is always non-null. In streaming mode, it is null in the `message_start` event and non-null otherwise.

    - `END_TURN("end_turn")`

    - `MAX_TOKENS("max_tokens")`

    - `STOP_SEQUENCE("stop_sequence")`

    - `TOOL_USE("tool_use")`

    - `PAUSE_TURN("pause_turn")`

    - `REFUSAL("refusal")`

  - `Optional<String> stopSequence`

    Which custom stop sequence was generated, if any.

    This value will be a non-null string if one of your custom stop sequences was generated.

  - `JsonValue; type "message"constant`

    Object type.

    For Messages, this is always `"message"`.

    - `MESSAGE("message")`

  - `Usage usage`

    Billing and rate-limit usage.

    Anthropic's API bills and rate-limits by token counts, as tokens represent the underlying cost to our systems.

    Under the hood, the API transforms requests into a format suitable for the model. The model's output then goes through a parsing stage before becoming an API response. As a result, the token counts in `usage` will not match one-to-one with the exact visible content of an API request or response.

    For example, `output_tokens` will be non-zero, even for an empty string response from Claude.

    Total input tokens in a request is the summation of `input_tokens`, `cache_creation_input_tokens`, and `cache_read_input_tokens`.

    - `Optional<CacheCreation> cacheCreation`

      Breakdown of cached tokens by TTL

      - `long ephemeral1hInputTokens`

        The number of input tokens used to create the 1 hour cache entry.

      - `long ephemeral5mInputTokens`

        The number of input tokens used to create the 5 minute cache entry.

    - `Optional<Long> cacheCreationInputTokens`

      The number of input tokens used to create the cache entry.

    - `Optional<Long> cacheReadInputTokens`

      The number of input tokens read from the cache.

    - `Optional<String> inferenceGeo`

      The geographic region where inference was performed for this request.

    - `long inputTokens`

      The number of input tokens which were used.

    - `long outputTokens`

      The number of output tokens which were used.

    - `Optional<ServerToolUsage> serverToolUse`

      The number of server tool requests.

      - `long webFetchRequests`

        The number of web fetch tool requests.

      - `long webSearchRequests`

        The number of web search tool requests.

    - `Optional<ServiceTier> serviceTier`

      If the request used the priority, standard, or batch tier.

      - `STANDARD("standard")`

      - `PRIORITY("priority")`

      - `BATCH("batch")`

### Message Count Tokens Tool

- `class MessageCountTokensTool: A class that can be one of several variants.union`

  Code execution tool with REPL state persistence (daemon mode + gVisor checkpoint).

  - `class Tool:`

    - `InputSchema inputSchema`

      [JSON schema](https://json-schema.org/draft/2020-12) for this tool's input.

      This defines the shape of the `input` that your tool accepts and that the model will produce.

      - `JsonValue; type "object"constant`

        - `OBJECT("object")`

      - `Optional<Properties> properties`

      - `Optional<List<String>> required`

    - `String name`

      Name of the tool.

      This is how the tool will be called by the model and in `tool_use` blocks.

    - `Optional<List<AllowedCaller>> allowedCallers`

      - `DIRECT("direct")`

      - `CODE_EXECUTION_20250825("code_execution_20250825")`

      - `CODE_EXECUTION_20260120("code_execution_20260120")`

    - `Optional<CacheControlEphemeral> cacheControl`

      Create a cache control breakpoint at this content block.

      - `JsonValue; type "ephemeral"constant`

        - `EPHEMERAL("ephemeral")`

      - `Optional<Ttl> ttl`

        The time-to-live for the cache control breakpoint.

        This may be one the following values:

        - `5m`: 5 minutes
        - `1h`: 1 hour

        Defaults to `5m`.

        - `TTL_5M("5m")`

        - `TTL_1H("1h")`

    - `Optional<Boolean> deferLoading`

      If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

    - `Optional<String> description`

      Description of what this tool does.

      Tool descriptions should be as detailed as possible. The more information that the model has about what the tool is and how to use it, the better it will perform. You can use natural language descriptions to reinforce important aspects of the tool input JSON schema.

    - `Optional<Boolean> eagerInputStreaming`

      Enable eager input streaming for this tool. When true, tool input parameters will be streamed incrementally as they are generated, and types will be inferred on-the-fly rather than buffering the full JSON output. When false, streaming is disabled for this tool even if the fine-grained-tool-streaming beta is active. When null (default), uses the default behavior based on beta headers.

    - `Optional<List<InputExample>> inputExamples`

    - `Optional<Boolean> strict`

      When true, guarantees schema validation on tool names and inputs

    - `Optional<Type> type`

      - `CUSTOM("custom")`

  - `class ToolBash20250124:`

    - `JsonValue; name "bash"constant`

      Name of the tool.

      This is how the tool will be called by the model and in `tool_use` blocks.

      - `BASH("bash")`

    - `JsonValue; type "bash_20250124"constant`

      - `BASH_20250124("bash_20250124")`

    - `Optional<List<AllowedCaller>> allowedCallers`

      - `DIRECT("direct")`

      - `CODE_EXECUTION_20250825("code_execution_20250825")`

      - `CODE_EXECUTION_20260120("code_execution_20260120")`

    - `Optional<CacheControlEphemeral> cacheControl`

      Create a cache control breakpoint at this content block.

      - `JsonValue; type "ephemeral"constant`

        - `EPHEMERAL("ephemeral")`

      - `Optional<Ttl> ttl`

        The time-to-live for the cache control breakpoint.

        This may be one the following values:

        - `5m`: 5 minutes
        - `1h`: 1 hour

        Defaults to `5m`.

        - `TTL_5M("5m")`

        - `TTL_1H("1h")`

    - `Optional<Boolean> deferLoading`

      If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

    - `Optional<List<InputExample>> inputExamples`

    - `Optional<Boolean> strict`

      When true, guarantees schema validation on tool names and inputs

  - `class CodeExecutionTool20250522:`

    - `JsonValue; name "code_execution"constant`

      Name of the tool.

      This is how the tool will be called by the model and in `tool_use` blocks.

      - `CODE_EXECUTION("code_execution")`

    - `JsonValue; type "code_execution_20250522"constant`

      - `CODE_EXECUTION_20250522("code_execution_20250522")`

    - `Optional<List<AllowedCaller>> allowedCallers`

      - `DIRECT("direct")`

      - `CODE_EXECUTION_20250825("code_execution_20250825")`

      - `CODE_EXECUTION_20260120("code_execution_20260120")`

    - `Optional<CacheControlEphemeral> cacheControl`

      Create a cache control breakpoint at this content block.

      - `JsonValue; type "ephemeral"constant`

        - `EPHEMERAL("ephemeral")`

      - `Optional<Ttl> ttl`

        The time-to-live for the cache control breakpoint.

        This may be one the following values:

        - `5m`: 5 minutes
        - `1h`: 1 hour

        Defaults to `5m`.

        - `TTL_5M("5m")`

        - `TTL_1H("1h")`

    - `Optional<Boolean> deferLoading`

      If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

    - `Optional<Boolean> strict`

      When true, guarantees schema validation on tool names and inputs

  - `class CodeExecutionTool20250825:`

    - `JsonValue; name "code_execution"constant`

      Name of the tool.

      This is how the tool will be called by the model and in `tool_use` blocks.

      - `CODE_EXECUTION("code_execution")`

    - `JsonValue; type "code_execution_20250825"constant`

      - `CODE_EXECUTION_20250825("code_execution_20250825")`

    - `Optional<List<AllowedCaller>> allowedCallers`

      - `DIRECT("direct")`

      - `CODE_EXECUTION_20250825("code_execution_20250825")`

      - `CODE_EXECUTION_20260120("code_execution_20260120")`

    - `Optional<CacheControlEphemeral> cacheControl`

      Create a cache control breakpoint at this content block.

      - `JsonValue; type "ephemeral"constant`

        - `EPHEMERAL("ephemeral")`

      - `Optional<Ttl> ttl`

        The time-to-live for the cache control breakpoint.

        This may be one the following values:

        - `5m`: 5 minutes
        - `1h`: 1 hour

        Defaults to `5m`.

        - `TTL_5M("5m")`

        - `TTL_1H("1h")`

    - `Optional<Boolean> deferLoading`

      If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

    - `Optional<Boolean> strict`

      When true, guarantees schema validation on tool names and inputs

  - `class CodeExecutionTool20260120:`

    Code execution tool with REPL state persistence (daemon mode + gVisor checkpoint).

    - `JsonValue; name "code_execution"constant`

      Name of the tool.

      This is how the tool will be called by the model and in `tool_use` blocks.

      - `CODE_EXECUTION("code_execution")`

    - `JsonValue; type "code_execution_20260120"constant`

      - `CODE_EXECUTION_20260120("code_execution_20260120")`

    - `Optional<List<AllowedCaller>> allowedCallers`

      - `DIRECT("direct")`

      - `CODE_EXECUTION_20250825("code_execution_20250825")`

      - `CODE_EXECUTION_20260120("code_execution_20260120")`

    - `Optional<CacheControlEphemeral> cacheControl`

      Create a cache control breakpoint at this content block.

      - `JsonValue; type "ephemeral"constant`

        - `EPHEMERAL("ephemeral")`

      - `Optional<Ttl> ttl`

        The time-to-live for the cache control breakpoint.

        This may be one the following values:

        - `5m`: 5 minutes
        - `1h`: 1 hour

        Defaults to `5m`.

        - `TTL_5M("5m")`

        - `TTL_1H("1h")`

    - `Optional<Boolean> deferLoading`

      If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

    - `Optional<Boolean> strict`

      When true, guarantees schema validation on tool names and inputs

  - `class MemoryTool20250818:`

    - `JsonValue; name "memory"constant`

      Name of the tool.

      This is how the tool will be called by the model and in `tool_use` blocks.

      - `MEMORY("memory")`

    - `JsonValue; type "memory_20250818"constant`

      - `MEMORY_20250818("memory_20250818")`

    - `Optional<List<AllowedCaller>> allowedCallers`

      - `DIRECT("direct")`

      - `CODE_EXECUTION_20250825("code_execution_20250825")`

      - `CODE_EXECUTION_20260120("code_execution_20260120")`

    - `Optional<CacheControlEphemeral> cacheControl`

      Create a cache control breakpoint at this content block.

      - `JsonValue; type "ephemeral"constant`

        - `EPHEMERAL("ephemeral")`

      - `Optional<Ttl> ttl`

        The time-to-live for the cache control breakpoint.

        This may be one the following values:

        - `5m`: 5 minutes
        - `1h`: 1 hour

        Defaults to `5m`.

        - `TTL_5M("5m")`

        - `TTL_1H("1h")`

    - `Optional<Boolean> deferLoading`

      If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

    - `Optional<List<InputExample>> inputExamples`

    - `Optional<Boolean> strict`

      When true, guarantees schema validation on tool names and inputs

  - `class ToolTextEditor20250124:`

    - `JsonValue; name "str_replace_editor"constant`

      Name of the tool.

      This is how the tool will be called by the model and in `tool_use` blocks.

      - `STR_REPLACE_EDITOR("str_replace_editor")`

    - `JsonValue; type "text_editor_20250124"constant`

      - `TEXT_EDITOR_20250124("text_editor_20250124")`

    - `Optional<List<AllowedCaller>> allowedCallers`

      - `DIRECT("direct")`

      - `CODE_EXECUTION_20250825("code_execution_20250825")`

      - `CODE_EXECUTION_20260120("code_execution_20260120")`

    - `Optional<CacheControlEphemeral> cacheControl`

      Create a cache control breakpoint at this content block.

      - `JsonValue; type "ephemeral"constant`

        - `EPHEMERAL("ephemeral")`

      - `Optional<Ttl> ttl`

        The time-to-live for the cache control breakpoint.

        This may be one the following values:

        - `5m`: 5 minutes
        - `1h`: 1 hour

        Defaults to `5m`.

        - `TTL_5M("5m")`

        - `TTL_1H("1h")`

    - `Optional<Boolean> deferLoading`

      If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

    - `Optional<List<InputExample>> inputExamples`

    - `Optional<Boolean> strict`

      When true, guarantees schema validation on tool names and inputs

  - `class ToolTextEditor20250429:`

    - `JsonValue; name "str_replace_based_edit_tool"constant`

      Name of the tool.

      This is how the tool will be called by the model and in `tool_use` blocks.

      - `STR_REPLACE_BASED_EDIT_TOOL("str_replace_based_edit_tool")`

    - `JsonValue; type "text_editor_20250429"constant`

      - `TEXT_EDITOR_20250429("text_editor_20250429")`

    - `Optional<List<AllowedCaller>> allowedCallers`

      - `DIRECT("direct")`

      - `CODE_EXECUTION_20250825("code_execution_20250825")`

      - `CODE_EXECUTION_20260120("code_execution_20260120")`

    - `Optional<CacheControlEphemeral> cacheControl`

      Create a cache control breakpoint at this content block.

      - `JsonValue; type "ephemeral"constant`

        - `EPHEMERAL("ephemeral")`

      - `Optional<Ttl> ttl`

        The time-to-live for the cache control breakpoint.

        This may be one the following values:

        - `5m`: 5 minutes
        - `1h`: 1 hour

        Defaults to `5m`.

        - `TTL_5M("5m")`

        - `TTL_1H("1h")`

    - `Optional<Boolean> deferLoading`

      If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

    - `Optional<List<InputExample>> inputExamples`

    - `Optional<Boolean> strict`

      When true, guarantees schema validation on tool names and inputs

  - `class ToolTextEditor20250728:`

    - `JsonValue; name "str_replace_based_edit_tool"constant`

      Name of the tool.

      This is how the tool will be called by the model and in `tool_use` blocks.

      - `STR_REPLACE_BASED_EDIT_TOOL("str_replace_based_edit_tool")`

    - `JsonValue; type "text_editor_20250728"constant`

      - `TEXT_EDITOR_20250728("text_editor_20250728")`

    - `Optional<List<AllowedCaller>> allowedCallers`

      - `DIRECT("direct")`

      - `CODE_EXECUTION_20250825("code_execution_20250825")`

      - `CODE_EXECUTION_20260120("code_execution_20260120")`

    - `Optional<CacheControlEphemeral> cacheControl`

      Create a cache control breakpoint at this content block.

      - `JsonValue; type "ephemeral"constant`

        - `EPHEMERAL("ephemeral")`

      - `Optional<Ttl> ttl`

        The time-to-live for the cache control breakpoint.

        This may be one the following values:

        - `5m`: 5 minutes
        - `1h`: 1 hour

        Defaults to `5m`.

        - `TTL_5M("5m")`

        - `TTL_1H("1h")`

    - `Optional<Boolean> deferLoading`

      If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

    - `Optional<List<InputExample>> inputExamples`

    - `Optional<Long> maxCharacters`

      Maximum number of characters to display when viewing a file. If not specified, defaults to displaying the full file.

    - `Optional<Boolean> strict`

      When true, guarantees schema validation on tool names and inputs

  - `class WebSearchTool20250305:`

    - `JsonValue; name "web_search"constant`

      Name of the tool.

      This is how the tool will be called by the model and in `tool_use` blocks.

      - `WEB_SEARCH("web_search")`

    - `JsonValue; type "web_search_20250305"constant`

      - `WEB_SEARCH_20250305("web_search_20250305")`

    - `Optional<List<AllowedCaller>> allowedCallers`

      - `DIRECT("direct")`

      - `CODE_EXECUTION_20250825("code_execution_20250825")`

      - `CODE_EXECUTION_20260120("code_execution_20260120")`

    - `Optional<List<String>> allowedDomains`

      If provided, only these domains will be included in results. Cannot be used alongside `blocked_domains`.

    - `Optional<List<String>> blockedDomains`

      If provided, these domains will never appear in results. Cannot be used alongside `allowed_domains`.

    - `Optional<CacheControlEphemeral> cacheControl`

      Create a cache control breakpoint at this content block.

      - `JsonValue; type "ephemeral"constant`

        - `EPHEMERAL("ephemeral")`

      - `Optional<Ttl> ttl`

        The time-to-live for the cache control breakpoint.

        This may be one the following values:

        - `5m`: 5 minutes
        - `1h`: 1 hour

        Defaults to `5m`.

        - `TTL_5M("5m")`

        - `TTL_1H("1h")`

    - `Optional<Boolean> deferLoading`

      If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

    - `Optional<Long> maxUses`

      Maximum number of times the tool can be used in the API request.

    - `Optional<Boolean> strict`

      When true, guarantees schema validation on tool names and inputs

    - `Optional<UserLocation> userLocation`

      Parameters for the user's location. Used to provide more relevant search results.

      - `JsonValue; type "approximate"constant`

        - `APPROXIMATE("approximate")`

      - `Optional<String> city`

        The city of the user.

      - `Optional<String> country`

        The two letter [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) of the user.

      - `Optional<String> region`

        The region of the user.

      - `Optional<String> timezone`

        The [IANA timezone](https://nodatime.org/TimeZones) of the user.

  - `class WebFetchTool20250910:`

    - `JsonValue; name "web_fetch"constant`

      Name of the tool.

      This is how the tool will be called by the model and in `tool_use` blocks.

      - `WEB_FETCH("web_fetch")`

    - `JsonValue; type "web_fetch_20250910"constant`

      - `WEB_FETCH_20250910("web_fetch_20250910")`

    - `Optional<List<AllowedCaller>> allowedCallers`

      - `DIRECT("direct")`

      - `CODE_EXECUTION_20250825("code_execution_20250825")`

      - `CODE_EXECUTION_20260120("code_execution_20260120")`

    - `Optional<List<String>> allowedDomains`

      List of domains to allow fetching from

    - `Optional<List<String>> blockedDomains`

      List of domains to block fetching from

    - `Optional<CacheControlEphemeral> cacheControl`

      Create a cache control breakpoint at this content block.

      - `JsonValue; type "ephemeral"constant`

        - `EPHEMERAL("ephemeral")`

      - `Optional<Ttl> ttl`

        The time-to-live for the cache control breakpoint.

        This may be one the following values:

        - `5m`: 5 minutes
        - `1h`: 1 hour

        Defaults to `5m`.

        - `TTL_5M("5m")`

        - `TTL_1H("1h")`

    - `Optional<CitationsConfigParam> citations`

      Citations configuration for fetched documents. Citations are disabled by default.

      - `Optional<Boolean> enabled`

    - `Optional<Boolean> deferLoading`

      If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

    - `Optional<Long> maxContentTokens`

      Maximum number of tokens used by including web page text content in the context. The limit is approximate and does not apply to binary content such as PDFs.

    - `Optional<Long> maxUses`

      Maximum number of times the tool can be used in the API request.

    - `Optional<Boolean> strict`

      When true, guarantees schema validation on tool names and inputs

  - `class WebSearchTool20260209:`

    - `JsonValue; name "web_search"constant`

      Name of the tool.

      This is how the tool will be called by the model and in `tool_use` blocks.

      - `WEB_SEARCH("web_search")`

    - `JsonValue; type "web_search_20260209"constant`

      - `WEB_SEARCH_20260209("web_search_20260209")`

    - `Optional<List<AllowedCaller>> allowedCallers`

      - `DIRECT("direct")`

      - `CODE_EXECUTION_20250825("code_execution_20250825")`

      - `CODE_EXECUTION_20260120("code_execution_20260120")`

    - `Optional<List<String>> allowedDomains`

      If provided, only these domains will be included in results. Cannot be used alongside `blocked_domains`.

    - `Optional<List<String>> blockedDomains`

      If provided, these domains will never appear in results. Cannot be used alongside `allowed_domains`.

    - `Optional<CacheControlEphemeral> cacheControl`

      Create a cache control breakpoint at this content block.

      - `JsonValue; type "ephemeral"constant`

        - `EPHEMERAL("ephemeral")`

      - `Optional<Ttl> ttl`

        The time-to-live for the cache control breakpoint.

        This may be one the following values:

        - `5m`: 5 minutes
        - `1h`: 1 hour

        Defaults to `5m`.

        - `TTL_5M("5m")`

        - `TTL_1H("1h")`

    - `Optional<Boolean> deferLoading`

      If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

    - `Optional<Long> maxUses`

      Maximum number of times the tool can be used in the API request.

    - `Optional<Boolean> strict`

      When true, guarantees schema validation on tool names and inputs

    - `Optional<UserLocation> userLocation`

      Parameters for the user's location. Used to provide more relevant search results.

      - `JsonValue; type "approximate"constant`

        - `APPROXIMATE("approximate")`

      - `Optional<String> city`

        The city of the user.

      - `Optional<String> country`

        The two letter [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) of the user.

      - `Optional<String> region`

        The region of the user.

      - `Optional<String> timezone`

        The [IANA timezone](https://nodatime.org/TimeZones) of the user.

  - `class WebFetchTool20260209:`

    - `JsonValue; name "web_fetch"constant`

      Name of the tool.

      This is how the tool will be called by the model and in `tool_use` blocks.

      - `WEB_FETCH("web_fetch")`

    - `JsonValue; type "web_fetch_20260209"constant`

      - `WEB_FETCH_20260209("web_fetch_20260209")`

    - `Optional<List<AllowedCaller>> allowedCallers`

      - `DIRECT("direct")`

      - `CODE_EXECUTION_20250825("code_execution_20250825")`

      - `CODE_EXECUTION_20260120("code_execution_20260120")`

    - `Optional<List<String>> allowedDomains`

      List of domains to allow fetching from

    - `Optional<List<String>> blockedDomains`

      List of domains to block fetching from

    - `Optional<CacheControlEphemeral> cacheControl`

      Create a cache control breakpoint at this content block.

      - `JsonValue; type "ephemeral"constant`

        - `EPHEMERAL("ephemeral")`

      - `Optional<Ttl> ttl`

        The time-to-live for the cache control breakpoint.

        This may be one the following values:

        - `5m`: 5 minutes
        - `1h`: 1 hour

        Defaults to `5m`.

        - `TTL_5M("5m")`

        - `TTL_1H("1h")`

    - `Optional<CitationsConfigParam> citations`

      Citations configuration for fetched documents. Citations are disabled by default.

      - `Optional<Boolean> enabled`

    - `Optional<Boolean> deferLoading`

      If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

    - `Optional<Long> maxContentTokens`

      Maximum number of tokens used by including web page text content in the context. The limit is approximate and does not apply to binary content such as PDFs.

    - `Optional<Long> maxUses`

      Maximum number of times the tool can be used in the API request.

    - `Optional<Boolean> strict`

      When true, guarantees schema validation on tool names and inputs

  - `class ToolSearchToolBm25_20251119:`

    - `JsonValue; name "tool_search_tool_bm25"constant`

      Name of the tool.

      This is how the tool will be called by the model and in `tool_use` blocks.

      - `TOOL_SEARCH_TOOL_BM25("tool_search_tool_bm25")`

    - `Type type`

      - `TOOL_SEARCH_TOOL_BM25_20251119("tool_search_tool_bm25_20251119")`

      - `TOOL_SEARCH_TOOL_BM25("tool_search_tool_bm25")`

    - `Optional<List<AllowedCaller>> allowedCallers`

      - `DIRECT("direct")`

      - `CODE_EXECUTION_20250825("code_execution_20250825")`

      - `CODE_EXECUTION_20260120("code_execution_20260120")`

    - `Optional<CacheControlEphemeral> cacheControl`

      Create a cache control breakpoint at this content block.

      - `JsonValue; type "ephemeral"constant`

        - `EPHEMERAL("ephemeral")`

      - `Optional<Ttl> ttl`

        The time-to-live for the cache control breakpoint.

        This may be one the following values:

        - `5m`: 5 minutes
        - `1h`: 1 hour

        Defaults to `5m`.

        - `TTL_5M("5m")`

        - `TTL_1H("1h")`

    - `Optional<Boolean> deferLoading`

      If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

    - `Optional<Boolean> strict`

      When true, guarantees schema validation on tool names and inputs

  - `class ToolSearchToolRegex20251119:`

    - `JsonValue; name "tool_search_tool_regex"constant`

      Name of the tool.

      This is how the tool will be called by the model and in `tool_use` blocks.

      - `TOOL_SEARCH_TOOL_REGEX("tool_search_tool_regex")`

    - `Type type`

      - `TOOL_SEARCH_TOOL_REGEX_20251119("tool_search_tool_regex_20251119")`

      - `TOOL_SEARCH_TOOL_REGEX("tool_search_tool_regex")`

    - `Optional<List<AllowedCaller>> allowedCallers`

      - `DIRECT("direct")`

      - `CODE_EXECUTION_20250825("code_execution_20250825")`

      - `CODE_EXECUTION_20260120("code_execution_20260120")`

    - `Optional<CacheControlEphemeral> cacheControl`

      Create a cache control breakpoint at this content block.

      - `JsonValue; type "ephemeral"constant`

        - `EPHEMERAL("ephemeral")`

      - `Optional<Ttl> ttl`

        The time-to-live for the cache control breakpoint.

        This may be one the following values:

        - `5m`: 5 minutes
        - `1h`: 1 hour

        Defaults to `5m`.

        - `TTL_5M("5m")`

        - `TTL_1H("1h")`

    - `Optional<Boolean> deferLoading`

      If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

    - `Optional<Boolean> strict`

      When true, guarantees schema validation on tool names and inputs

### Message Delta Usage

- `class MessageDeltaUsage:`

  - `Optional<Long> cacheCreationInputTokens`

    The cumulative number of input tokens used to create the cache entry.

  - `Optional<Long> cacheReadInputTokens`

    The cumulative number of input tokens read from the cache.

  - `Optional<Long> inputTokens`

    The cumulative number of input tokens which were used.

  - `long outputTokens`

    The cumulative number of output tokens which were used.

  - `Optional<ServerToolUsage> serverToolUse`

    The number of server tool requests.

    - `long webFetchRequests`

      The number of web fetch tool requests.

    - `long webSearchRequests`

      The number of web search tool requests.

### Message Param

- `class MessageParam:`

  - `Content content`

    - `String`

    - `List<ContentBlockParam>`

      - `class TextBlockParam:`

        - `String text`

        - `JsonValue; type "text"constant`

          - `TEXT("text")`

        - `Optional<CacheControlEphemeral> cacheControl`

          Create a cache control breakpoint at this content block.

          - `JsonValue; type "ephemeral"constant`

            - `EPHEMERAL("ephemeral")`

          - `Optional<Ttl> ttl`

            The time-to-live for the cache control breakpoint.

            This may be one the following values:

            - `5m`: 5 minutes
            - `1h`: 1 hour

            Defaults to `5m`.

            - `TTL_5M("5m")`

            - `TTL_1H("1h")`

        - `Optional<List<TextCitationParam>> citations`

          - `class CitationCharLocationParam:`

            - `String citedText`

            - `long documentIndex`

            - `Optional<String> documentTitle`

            - `long endCharIndex`

            - `long startCharIndex`

            - `JsonValue; type "char_location"constant`

              - `CHAR_LOCATION("char_location")`

          - `class CitationPageLocationParam:`

            - `String citedText`

            - `long documentIndex`

            - `Optional<String> documentTitle`

            - `long endPageNumber`

            - `long startPageNumber`

            - `JsonValue; type "page_location"constant`

              - `PAGE_LOCATION("page_location")`

          - `class CitationContentBlockLocationParam:`

            - `String citedText`

            - `long documentIndex`

            - `Optional<String> documentTitle`

            - `long endBlockIndex`

            - `long startBlockIndex`

            - `JsonValue; type "content_block_location"constant`

              - `CONTENT_BLOCK_LOCATION("content_block_location")`

          - `class CitationWebSearchResultLocationParam:`

            - `String citedText`

            - `String encryptedIndex`

            - `Optional<String> title`

            - `JsonValue; type "web_search_result_location"constant`

              - `WEB_SEARCH_RESULT_LOCATION("web_search_result_location")`

            - `String url`

          - `class CitationSearchResultLocationParam:`

            - `String citedText`

            - `long endBlockIndex`

            - `long searchResultIndex`

            - `String source`

            - `long startBlockIndex`

            - `Optional<String> title`

            - `JsonValue; type "search_result_location"constant`

              - `SEARCH_RESULT_LOCATION("search_result_location")`

      - `class ImageBlockParam:`

        - `Source source`

          - `class Base64ImageSource:`

            - `String data`

            - `MediaType mediaType`

              - `IMAGE_JPEG("image/jpeg")`

              - `IMAGE_PNG("image/png")`

              - `IMAGE_GIF("image/gif")`

              - `IMAGE_WEBP("image/webp")`

            - `JsonValue; type "base64"constant`

              - `BASE64("base64")`

          - `class UrlImageSource:`

            - `JsonValue; type "url"constant`

              - `URL("url")`

            - `String url`

        - `JsonValue; type "image"constant`

          - `IMAGE("image")`

        - `Optional<CacheControlEphemeral> cacheControl`

          Create a cache control breakpoint at this content block.

          - `JsonValue; type "ephemeral"constant`

            - `EPHEMERAL("ephemeral")`

          - `Optional<Ttl> ttl`

            The time-to-live for the cache control breakpoint.

            This may be one the following values:

            - `5m`: 5 minutes
            - `1h`: 1 hour

            Defaults to `5m`.

            - `TTL_5M("5m")`

            - `TTL_1H("1h")`

      - `class DocumentBlockParam:`

        - `Source source`

          - `class Base64PdfSource:`

            - `String data`

            - `JsonValue; mediaType "application/pdf"constant`

              - `APPLICATION_PDF("application/pdf")`

            - `JsonValue; type "base64"constant`

              - `BASE64("base64")`

          - `class PlainTextSource:`

            - `String data`

            - `JsonValue; mediaType "text/plain"constant`

              - `TEXT_PLAIN("text/plain")`

            - `JsonValue; type "text"constant`

              - `TEXT("text")`

          - `class ContentBlockSource:`

            - `Content content`

              - `String`

              - `List<ContentBlockSourceContent>`

                - `class TextBlockParam:`

                  - `String text`

                  - `JsonValue; type "text"constant`

                    - `TEXT("text")`

                  - `Optional<CacheControlEphemeral> cacheControl`

                    Create a cache control breakpoint at this content block.

                    - `JsonValue; type "ephemeral"constant`

                      - `EPHEMERAL("ephemeral")`

                    - `Optional<Ttl> ttl`

                      The time-to-live for the cache control breakpoint.

                      This may be one the following values:

                      - `5m`: 5 minutes
                      - `1h`: 1 hour

                      Defaults to `5m`.

                      - `TTL_5M("5m")`

                      - `TTL_1H("1h")`

                  - `Optional<List<TextCitationParam>> citations`

                    - `class CitationCharLocationParam:`

                      - `String citedText`

                      - `long documentIndex`

                      - `Optional<String> documentTitle`

                      - `long endCharIndex`

                      - `long startCharIndex`

                      - `JsonValue; type "char_location"constant`

                        - `CHAR_LOCATION("char_location")`

                    - `class CitationPageLocationParam:`

                      - `String citedText`

                      - `long documentIndex`

                      - `Optional<String> documentTitle`

                      - `long endPageNumber`

                      - `long startPageNumber`

                      - `JsonValue; type "page_location"constant`

                        - `PAGE_LOCATION("page_location")`

                    - `class CitationContentBlockLocationParam:`

                      - `String citedText`

                      - `long documentIndex`

                      - `Optional<String> documentTitle`

                      - `long endBlockIndex`

                      - `long startBlockIndex`

                      - `JsonValue; type "content_block_location"constant`

                        - `CONTENT_BLOCK_LOCATION("content_block_location")`

                    - `class CitationWebSearchResultLocationParam:`

                      - `String citedText`

                      - `String encryptedIndex`

                      - `Optional<String> title`

                      - `JsonValue; type "web_search_result_location"constant`

                        - `WEB_SEARCH_RESULT_LOCATION("web_search_result_location")`

                      - `String url`

                    - `class CitationSearchResultLocationParam:`

                      - `String citedText`

                      - `long endBlockIndex`

                      - `long searchResultIndex`

                      - `String source`

                      - `long startBlockIndex`

                      - `Optional<String> title`

                      - `JsonValue; type "search_result_location"constant`

                        - `SEARCH_RESULT_LOCATION("search_result_location")`

                - `class ImageBlockParam:`

                  - `Source source`

                    - `class Base64ImageSource:`

                      - `String data`

                      - `MediaType mediaType`

                        - `IMAGE_JPEG("image/jpeg")`

                        - `IMAGE_PNG("image/png")`

                        - `IMAGE_GIF("image/gif")`

                        - `IMAGE_WEBP("image/webp")`

                      - `JsonValue; type "base64"constant`

                        - `BASE64("base64")`

                    - `class UrlImageSource:`

                      - `JsonValue; type "url"constant`

                        - `URL("url")`

                      - `String url`

                  - `JsonValue; type "image"constant`

                    - `IMAGE("image")`

                  - `Optional<CacheControlEphemeral> cacheControl`

                    Create a cache control breakpoint at this content block.

                    - `JsonValue; type "ephemeral"constant`

                      - `EPHEMERAL("ephemeral")`

                    - `Optional<Ttl> ttl`

                      The time-to-live for the cache control breakpoint.

                      This may be one the following values:

                      - `5m`: 5 minutes
                      - `1h`: 1 hour

                      Defaults to `5m`.

                      - `TTL_5M("5m")`

                      - `TTL_1H("1h")`

            - `JsonValue; type "content"constant`

              - `CONTENT("content")`

          - `class UrlPdfSource:`

            - `JsonValue; type "url"constant`

              - `URL("url")`

            - `String url`

        - `JsonValue; type "document"constant`

          - `DOCUMENT("document")`

        - `Optional<CacheControlEphemeral> cacheControl`

          Create a cache control breakpoint at this content block.

          - `JsonValue; type "ephemeral"constant`

            - `EPHEMERAL("ephemeral")`

          - `Optional<Ttl> ttl`

            The time-to-live for the cache control breakpoint.

            This may be one the following values:

            - `5m`: 5 minutes
            - `1h`: 1 hour

            Defaults to `5m`.

            - `TTL_5M("5m")`

            - `TTL_1H("1h")`

        - `Optional<CitationsConfigParam> citations`

          - `Optional<Boolean> enabled`

        - `Optional<String> context`

        - `Optional<String> title`

      - `class SearchResultBlockParam:`

        - `List<TextBlockParam> content`

          - `String text`

          - `JsonValue; type "text"constant`

            - `TEXT("text")`

          - `Optional<CacheControlEphemeral> cacheControl`

            Create a cache control breakpoint at this content block.

            - `JsonValue; type "ephemeral"constant`

              - `EPHEMERAL("ephemeral")`

            - `Optional<Ttl> ttl`

              The time-to-live for the cache control breakpoint.

              This may be one the following values:

              - `5m`: 5 minutes
              - `1h`: 1 hour

              Defaults to `5m`.

              - `TTL_5M("5m")`

              - `TTL_1H("1h")`

          - `Optional<List<TextCitationParam>> citations`

            - `class CitationCharLocationParam:`

              - `String citedText`

              - `long documentIndex`

              - `Optional<String> documentTitle`

              - `long endCharIndex`

              - `long startCharIndex`

              - `JsonValue; type "char_location"constant`

                - `CHAR_LOCATION("char_location")`

            - `class CitationPageLocationParam:`

              - `String citedText`

              - `long documentIndex`

              - `Optional<String> documentTitle`

              - `long endPageNumber`

              - `long startPageNumber`

              - `JsonValue; type "page_location"constant`

                - `PAGE_LOCATION("page_location")`

            - `class CitationContentBlockLocationParam:`

              - `String citedText`

              - `long documentIndex`

              - `Optional<String> documentTitle`

              - `long endBlockIndex`

              - `long startBlockIndex`

              - `JsonValue; type "content_block_location"constant`

                - `CONTENT_BLOCK_LOCATION("content_block_location")`

            - `class CitationWebSearchResultLocationParam:`

              - `String citedText`

              - `String encryptedIndex`

              - `Optional<String> title`

              - `JsonValue; type "web_search_result_location"constant`

                - `WEB_SEARCH_RESULT_LOCATION("web_search_result_location")`

              - `String url`

            - `class CitationSearchResultLocationParam:`

              - `String citedText`

              - `long endBlockIndex`

              - `long searchResultIndex`

              - `String source`

              - `long startBlockIndex`

              - `Optional<String> title`

              - `JsonValue; type "search_result_location"constant`

                - `SEARCH_RESULT_LOCATION("search_result_location")`

        - `String source`

        - `String title`

        - `JsonValue; type "search_result"constant`

          - `SEARCH_RESULT("search_result")`

        - `Optional<CacheControlEphemeral> cacheControl`

          Create a cache control breakpoint at this content block.

          - `JsonValue; type "ephemeral"constant`

            - `EPHEMERAL("ephemeral")`

          - `Optional<Ttl> ttl`

            The time-to-live for the cache control breakpoint.

            This may be one the following values:

            - `5m`: 5 minutes
            - `1h`: 1 hour

            Defaults to `5m`.

            - `TTL_5M("5m")`

            - `TTL_1H("1h")`

        - `Optional<CitationsConfigParam> citations`

          - `Optional<Boolean> enabled`

      - `class ThinkingBlockParam:`

        - `String signature`

        - `String thinking`

        - `JsonValue; type "thinking"constant`

          - `THINKING("thinking")`

      - `class RedactedThinkingBlockParam:`

        - `String data`

        - `JsonValue; type "redacted_thinking"constant`

          - `REDACTED_THINKING("redacted_thinking")`

      - `class ToolUseBlockParam:`

        - `String id`

        - `Input input`

        - `String name`

        - `JsonValue; type "tool_use"constant`

          - `TOOL_USE("tool_use")`

        - `Optional<CacheControlEphemeral> cacheControl`

          Create a cache control breakpoint at this content block.

          - `JsonValue; type "ephemeral"constant`

            - `EPHEMERAL("ephemeral")`

          - `Optional<Ttl> ttl`

            The time-to-live for the cache control breakpoint.

            This may be one the following values:

            - `5m`: 5 minutes
            - `1h`: 1 hour

            Defaults to `5m`.

            - `TTL_5M("5m")`

            - `TTL_1H("1h")`

        - `Optional<Caller> caller`

          Tool invocation directly from the model.

          - `class DirectCaller:`

            Tool invocation directly from the model.

            - `JsonValue; type "direct"constant`

              - `DIRECT("direct")`

          - `class ServerToolCaller:`

            Tool invocation generated by a server-side tool.

            - `String toolId`

            - `JsonValue; type "code_execution_20250825"constant`

              - `CODE_EXECUTION_20250825("code_execution_20250825")`

          - `class ServerToolCaller20260120:`

            - `String toolId`

            - `JsonValue; type "code_execution_20260120"constant`

              - `CODE_EXECUTION_20260120("code_execution_20260120")`

      - `class ToolResultBlockParam:`

        - `String toolUseId`

        - `JsonValue; type "tool_result"constant`

          - `TOOL_RESULT("tool_result")`

        - `Optional<CacheControlEphemeral> cacheControl`

          Create a cache control breakpoint at this content block.

          - `JsonValue; type "ephemeral"constant`

            - `EPHEMERAL("ephemeral")`

          - `Optional<Ttl> ttl`

            The time-to-live for the cache control breakpoint.

            This may be one the following values:

            - `5m`: 5 minutes
            - `1h`: 1 hour

            Defaults to `5m`.

            - `TTL_5M("5m")`

            - `TTL_1H("1h")`

        - `Optional<Content> content`

          - `String`

          - `List<Block>`

            - `class TextBlockParam:`

              - `String text`

              - `JsonValue; type "text"constant`

                - `TEXT("text")`

              - `Optional<CacheControlEphemeral> cacheControl`

                Create a cache control breakpoint at this content block.

                - `JsonValue; type "ephemeral"constant`

                  - `EPHEMERAL("ephemeral")`

                - `Optional<Ttl> ttl`

                  The time-to-live for the cache control breakpoint.

                  This may be one the following values:

                  - `5m`: 5 minutes
                  - `1h`: 1 hour

                  Defaults to `5m`.

                  - `TTL_5M("5m")`

                  - `TTL_1H("1h")`

              - `Optional<List<TextCitationParam>> citations`

                - `class CitationCharLocationParam:`

                  - `String citedText`

                  - `long documentIndex`

                  - `Optional<String> documentTitle`

                  - `long endCharIndex`

                  - `long startCharIndex`

                  - `JsonValue; type "char_location"constant`

                    - `CHAR_LOCATION("char_location")`

                - `class CitationPageLocationParam:`

                  - `String citedText`

                  - `long documentIndex`

                  - `Optional<String> documentTitle`

                  - `long endPageNumber`

                  - `long startPageNumber`

                  - `JsonValue; type "page_location"constant`

                    - `PAGE_LOCATION("page_location")`

                - `class CitationContentBlockLocationParam:`

                  - `String citedText`

                  - `long documentIndex`

                  - `Optional<String> documentTitle`

                  - `long endBlockIndex`

                  - `long startBlockIndex`

                  - `JsonValue; type "content_block_location"constant`

                    - `CONTENT_BLOCK_LOCATION("content_block_location")`

                - `class CitationWebSearchResultLocationParam:`

                  - `String citedText`

                  - `String encryptedIndex`

                  - `Optional<String> title`

                  - `JsonValue; type "web_search_result_location"constant`

                    - `WEB_SEARCH_RESULT_LOCATION("web_search_result_location")`

                  - `String url`

                - `class CitationSearchResultLocationParam:`

                  - `String citedText`

                  - `long endBlockIndex`

                  - `long searchResultIndex`

                  - `String source`

                  - `long startBlockIndex`

                  - `Optional<String> title`

                  - `JsonValue; type "search_result_location"constant`

                    - `SEARCH_RESULT_LOCATION("search_result_location")`

            - `class ImageBlockParam:`

              - `Source source`

                - `class Base64ImageSource:`

                  - `String data`

                  - `MediaType mediaType`

                    - `IMAGE_JPEG("image/jpeg")`

                    - `IMAGE_PNG("image/png")`

                    - `IMAGE_GIF("image/gif")`

                    - `IMAGE_WEBP("image/webp")`

                  - `JsonValue; type "base64"constant`

                    - `BASE64("base64")`

                - `class UrlImageSource:`

                  - `JsonValue; type "url"constant`

                    - `URL("url")`

                  - `String url`

              - `JsonValue; type "image"constant`

                - `IMAGE("image")`

              - `Optional<CacheControlEphemeral> cacheControl`

                Create a cache control breakpoint at this content block.

                - `JsonValue; type "ephemeral"constant`

                  - `EPHEMERAL("ephemeral")`

                - `Optional<Ttl> ttl`

                  The time-to-live for the cache control breakpoint.

                  This may be one the following values:

                  - `5m`: 5 minutes
                  - `1h`: 1 hour

                  Defaults to `5m`.

                  - `TTL_5M("5m")`

                  - `TTL_1H("1h")`

            - `class SearchResultBlockParam:`

              - `List<TextBlockParam> content`

                - `String text`

                - `JsonValue; type "text"constant`

                  - `TEXT("text")`

                - `Optional<CacheControlEphemeral> cacheControl`

                  Create a cache control breakpoint at this content block.

                  - `JsonValue; type "ephemeral"constant`

                    - `EPHEMERAL("ephemeral")`

                  - `Optional<Ttl> ttl`

                    The time-to-live for the cache control breakpoint.

                    This may be one the following values:

                    - `5m`: 5 minutes
                    - `1h`: 1 hour

                    Defaults to `5m`.

                    - `TTL_5M("5m")`

                    - `TTL_1H("1h")`

                - `Optional<List<TextCitationParam>> citations`

                  - `class CitationCharLocationParam:`

                    - `String citedText`

                    - `long documentIndex`

                    - `Optional<String> documentTitle`

                    - `long endCharIndex`

                    - `long startCharIndex`

                    - `JsonValue; type "char_location"constant`

                      - `CHAR_LOCATION("char_location")`

                  - `class CitationPageLocationParam:`

                    - `String citedText`

                    - `long documentIndex`

                    - `Optional<String> documentTitle`

                    - `long endPageNumber`

                    - `long startPageNumber`

                    - `JsonValue; type "page_location"constant`

                      - `PAGE_LOCATION("page_location")`

                  - `class CitationContentBlockLocationParam:`

                    - `String citedText`

                    - `long documentIndex`

                    - `Optional<String> documentTitle`

                    - `long endBlockIndex`

                    - `long startBlockIndex`

                    - `JsonValue; type "content_block_location"constant`

                      - `CONTENT_BLOCK_LOCATION("content_block_location")`

                  - `class CitationWebSearchResultLocationParam:`

                    - `String citedText`

                    - `String encryptedIndex`

                    - `Optional<String> title`

                    - `JsonValue; type "web_search_result_location"constant`

                      - `WEB_SEARCH_RESULT_LOCATION("web_search_result_location")`

                    - `String url`

                  - `class CitationSearchResultLocationParam:`

                    - `String citedText`

                    - `long endBlockIndex`

                    - `long searchResultIndex`

                    - `String source`

                    - `long startBlockIndex`

                    - `Optional<String> title`

                    - `JsonValue; type "search_result_location"constant`

                      - `SEARCH_RESULT_LOCATION("search_result_location")`

              - `String source`

              - `String title`

              - `JsonValue; type "search_result"constant`

                - `SEARCH_RESULT("search_result")`

              - `Optional<CacheControlEphemeral> cacheControl`

                Create a cache control breakpoint at this content block.

                - `JsonValue; type "ephemeral"constant`

                  - `EPHEMERAL("ephemeral")`

                - `Optional<Ttl> ttl`

                  The time-to-live for the cache control breakpoint.

                  This may be one the following values:

                  - `5m`: 5 minutes
                  - `1h`: 1 hour

                  Defaults to `5m`.

                  - `TTL_5M("5m")`

                  - `TTL_1H("1h")`

              - `Optional<CitationsConfigParam> citations`

                - `Optional<Boolean> enabled`

            - `class DocumentBlockParam:`

              - `Source source`

                - `class Base64PdfSource:`

                  - `String data`

                  - `JsonValue; mediaType "application/pdf"constant`

                    - `APPLICATION_PDF("application/pdf")`

                  - `JsonValue; type "base64"constant`

                    - `BASE64("base64")`

                - `class PlainTextSource:`

                  - `String data`

                  - `JsonValue; mediaType "text/plain"constant`

                    - `TEXT_PLAIN("text/plain")`

                  - `JsonValue; type "text"constant`

                    - `TEXT("text")`

                - `class ContentBlockSource:`

                  - `Content content`

                    - `String`

                    - `List<ContentBlockSourceContent>`

                      - `class TextBlockParam:`

                        - `String text`

                        - `JsonValue; type "text"constant`

                          - `TEXT("text")`

                        - `Optional<CacheControlEphemeral> cacheControl`

                          Create a cache control breakpoint at this content block.

                          - `JsonValue; type "ephemeral"constant`

                            - `EPHEMERAL("ephemeral")`

                          - `Optional<Ttl> ttl`

                            The time-to-live for the cache control breakpoint.

                            This may be one the following values:

                            - `5m`: 5 minutes
                            - `1h`: 1 hour

                            Defaults to `5m`.

                            - `TTL_5M("5m")`

                            - `TTL_1H("1h")`

                        - `Optional<List<TextCitationParam>> citations`

                          - `class CitationCharLocationParam:`

                            - `String citedText`

                            - `long documentIndex`

                            - `Optional<String> documentTitle`

                            - `long endCharIndex`

                            - `long startCharIndex`

                            - `JsonValue; type "char_location"constant`

                              - `CHAR_LOCATION("char_location")`

                          - `class CitationPageLocationParam:`

                            - `String citedText`

                            - `long documentIndex`

                            - `Optional<String> documentTitle`

                            - `long endPageNumber`

                            - `long startPageNumber`

                            - `JsonValue; type "page_location"constant`

                              - `PAGE_LOCATION("page_location")`

                          - `class CitationContentBlockLocationParam:`

                            - `String citedText`

                            - `long documentIndex`

                            - `Optional<String> documentTitle`

                            - `long endBlockIndex`

                            - `long startBlockIndex`

                            - `JsonValue; type "content_block_location"constant`

                              - `CONTENT_BLOCK_LOCATION("content_block_location")`

                          - `class CitationWebSearchResultLocationParam:`

                            - `String citedText`

                            - `String encryptedIndex`

                            - `Optional<String> title`

                            - `JsonValue; type "web_search_result_location"constant`

                              - `WEB_SEARCH_RESULT_LOCATION("web_search_result_location")`

                            - `String url`

                          - `class CitationSearchResultLocationParam:`

                            - `String citedText`

                            - `long endBlockIndex`

                            - `long searchResultIndex`

                            - `String source`

                            - `long startBlockIndex`

                            - `Optional<String> title`

                            - `JsonValue; type "search_result_location"constant`

                              - `SEARCH_RESULT_LOCATION("search_result_location")`

                      - `class ImageBlockParam:`

                        - `Source source`

                          - `class Base64ImageSource:`

                            - `String data`

                            - `MediaType mediaType`

                              - `IMAGE_JPEG("image/jpeg")`

                              - `IMAGE_PNG("image/png")`

                              - `IMAGE_GIF("image/gif")`

                              - `IMAGE_WEBP("image/webp")`

                            - `JsonValue; type "base64"constant`

                              - `BASE64("base64")`

                          - `class UrlImageSource:`

                            - `JsonValue; type "url"constant`

                              - `URL("url")`

                            - `String url`

                        - `JsonValue; type "image"constant`

                          - `IMAGE("image")`

                        - `Optional<CacheControlEphemeral> cacheControl`

                          Create a cache control breakpoint at this content block.

                          - `JsonValue; type "ephemeral"constant`

                            - `EPHEMERAL("ephemeral")`

                          - `Optional<Ttl> ttl`

                            The time-to-live for the cache control breakpoint.

                            This may be one the following values:

                            - `5m`: 5 minutes
                            - `1h`: 1 hour

                            Defaults to `5m`.

                            - `TTL_5M("5m")`

                            - `TTL_1H("1h")`

                  - `JsonValue; type "content"constant`

                    - `CONTENT("content")`

                - `class UrlPdfSource:`

                  - `JsonValue; type "url"constant`

                    - `URL("url")`

                  - `String url`

              - `JsonValue; type "document"constant`

                - `DOCUMENT("document")`

              - `Optional<CacheControlEphemeral> cacheControl`

                Create a cache control breakpoint at this content block.

                - `JsonValue; type "ephemeral"constant`

                  - `EPHEMERAL("ephemeral")`

                - `Optional<Ttl> ttl`

                  The time-to-live for the cache control breakpoint.

                  This may be one the following values:

                  - `5m`: 5 minutes
                  - `1h`: 1 hour

                  Defaults to `5m`.

                  - `TTL_5M("5m")`

                  - `TTL_1H("1h")`

              - `Optional<CitationsConfigParam> citations`

                - `Optional<Boolean> enabled`

              - `Optional<String> context`

              - `Optional<String> title`

            - `class ToolReferenceBlockParam:`

              Tool reference block that can be included in tool_result content.

              - `String toolName`

              - `JsonValue; type "tool_reference"constant`

                - `TOOL_REFERENCE("tool_reference")`

              - `Optional<CacheControlEphemeral> cacheControl`

                Create a cache control breakpoint at this content block.

                - `JsonValue; type "ephemeral"constant`

                  - `EPHEMERAL("ephemeral")`

                - `Optional<Ttl> ttl`

                  The time-to-live for the cache control breakpoint.

                  This may be one the following values:

                  - `5m`: 5 minutes
                  - `1h`: 1 hour

                  Defaults to `5m`.

                  - `TTL_5M("5m")`

                  - `TTL_1H("1h")`

        - `Optional<Boolean> isError`

      - `class ServerToolUseBlockParam:`

        - `String id`

        - `Input input`

        - `Name name`

          - `WEB_SEARCH("web_search")`

          - `WEB_FETCH("web_fetch")`

          - `CODE_EXECUTION("code_execution")`

          - `BASH_CODE_EXECUTION("bash_code_execution")`

          - `TEXT_EDITOR_CODE_EXECUTION("text_editor_code_execution")`

          - `TOOL_SEARCH_TOOL_REGEX("tool_search_tool_regex")`

          - `TOOL_SEARCH_TOOL_BM25("tool_search_tool_bm25")`

        - `JsonValue; type "server_tool_use"constant`

          - `SERVER_TOOL_USE("server_tool_use")`

        - `Optional<CacheControlEphemeral> cacheControl`

          Create a cache control breakpoint at this content block.

          - `JsonValue; type "ephemeral"constant`

            - `EPHEMERAL("ephemeral")`

          - `Optional<Ttl> ttl`

            The time-to-live for the cache control breakpoint.

            This may be one the following values:

            - `5m`: 5 minutes
            - `1h`: 1 hour

            Defaults to `5m`.

            - `TTL_5M("5m")`

            - `TTL_1H("1h")`

        - `Optional<Caller> caller`

          Tool invocation directly from the model.

          - `class DirectCaller:`

            Tool invocation directly from the model.

            - `JsonValue; type "direct"constant`

              - `DIRECT("direct")`

          - `class ServerToolCaller:`

            Tool invocation generated by a server-side tool.

            - `String toolId`

            - `JsonValue; type "code_execution_20250825"constant`

              - `CODE_EXECUTION_20250825("code_execution_20250825")`

          - `class ServerToolCaller20260120:`

            - `String toolId`

            - `JsonValue; type "code_execution_20260120"constant`

              - `CODE_EXECUTION_20260120("code_execution_20260120")`

      - `class WebSearchToolResultBlockParam:`

        - `WebSearchToolResultBlockParamContent content`

          - `List<WebSearchResultBlockParam>`

            - `String encryptedContent`

            - `String title`

            - `JsonValue; type "web_search_result"constant`

              - `WEB_SEARCH_RESULT("web_search_result")`

            - `String url`

            - `Optional<String> pageAge`

          - `class WebSearchToolRequestError:`

            - `WebSearchToolResultErrorCode errorCode`

              - `INVALID_TOOL_INPUT("invalid_tool_input")`

              - `UNAVAILABLE("unavailable")`

              - `MAX_USES_EXCEEDED("max_uses_exceeded")`

              - `TOO_MANY_REQUESTS("too_many_requests")`

              - `QUERY_TOO_LONG("query_too_long")`

              - `REQUEST_TOO_LARGE("request_too_large")`

            - `JsonValue; type "web_search_tool_result_error"constant`

              - `WEB_SEARCH_TOOL_RESULT_ERROR("web_search_tool_result_error")`

        - `String toolUseId`

        - `JsonValue; type "web_search_tool_result"constant`

          - `WEB_SEARCH_TOOL_RESULT("web_search_tool_result")`

        - `Optional<CacheControlEphemeral> cacheControl`

          Create a cache control breakpoint at this content block.

          - `JsonValue; type "ephemeral"constant`

            - `EPHEMERAL("ephemeral")`

          - `Optional<Ttl> ttl`

            The time-to-live for the cache control breakpoint.

            This may be one the following values:

            - `5m`: 5 minutes
            - `1h`: 1 hour

            Defaults to `5m`.

            - `TTL_5M("5m")`

            - `TTL_1H("1h")`

        - `Optional<Caller> caller`

          Tool invocation directly from the model.

          - `class DirectCaller:`

            Tool invocation directly from the model.

            - `JsonValue; type "direct"constant`

              - `DIRECT("direct")`

          - `class ServerToolCaller:`

            Tool invocation generated by a server-side tool.

            - `String toolId`

            - `JsonValue; type "code_execution_20250825"constant`

              - `CODE_EXECUTION_20250825("code_execution_20250825")`

          - `class ServerToolCaller20260120:`

            - `String toolId`

            - `JsonValue; type "code_execution_20260120"constant`

              - `CODE_EXECUTION_20260120("code_execution_20260120")`

      - `class WebFetchToolResultBlockParam:`

        - `Content content`

          - `class WebFetchToolResultErrorBlockParam:`

            - `WebFetchToolResultErrorCode errorCode`

              - `INVALID_TOOL_INPUT("invalid_tool_input")`

              - `URL_TOO_LONG("url_too_long")`

              - `URL_NOT_ALLOWED("url_not_allowed")`

              - `URL_NOT_ACCESSIBLE("url_not_accessible")`

              - `UNSUPPORTED_CONTENT_TYPE("unsupported_content_type")`

              - `TOO_MANY_REQUESTS("too_many_requests")`

              - `MAX_USES_EXCEEDED("max_uses_exceeded")`

              - `UNAVAILABLE("unavailable")`

            - `JsonValue; type "web_fetch_tool_result_error"constant`

              - `WEB_FETCH_TOOL_RESULT_ERROR("web_fetch_tool_result_error")`

          - `class WebFetchBlockParam:`

            - `DocumentBlockParam content`

              - `Source source`

                - `class Base64PdfSource:`

                  - `String data`

                  - `JsonValue; mediaType "application/pdf"constant`

                    - `APPLICATION_PDF("application/pdf")`

                  - `JsonValue; type "base64"constant`

                    - `BASE64("base64")`

                - `class PlainTextSource:`

                  - `String data`

                  - `JsonValue; mediaType "text/plain"constant`

                    - `TEXT_PLAIN("text/plain")`

                  - `JsonValue; type "text"constant`

                    - `TEXT("text")`

                - `class ContentBlockSource:`

                  - `Content content`

                    - `String`

                    - `List<ContentBlockSourceContent>`

                      - `class TextBlockParam:`

                        - `String text`

                        - `JsonValue; type "text"constant`

                          - `TEXT("text")`

                        - `Optional<CacheControlEphemeral> cacheControl`

                          Create a cache control breakpoint at this content block.

                          - `JsonValue; type "ephemeral"constant`

                            - `EPHEMERAL("ephemeral")`

                          - `Optional<Ttl> ttl`

                            The time-to-live for the cache control breakpoint.

                            This may be one the following values:

                            - `5m`: 5 minutes
                            - `1h`: 1 hour

                            Defaults to `5m`.

                            - `TTL_5M("5m")`

                            - `TTL_1H("1h")`

                        - `Optional<List<TextCitationParam>> citations`

                          - `class CitationCharLocationParam:`

                            - `String citedText`

                            - `long documentIndex`

                            - `Optional<String> documentTitle`

                            - `long endCharIndex`

                            - `long startCharIndex`

                            - `JsonValue; type "char_location"constant`

                              - `CHAR_LOCATION("char_location")`

                          - `class CitationPageLocationParam:`

                            - `String citedText`

                            - `long documentIndex`

                            - `Optional<String> documentTitle`

                            - `long endPageNumber`

                            - `long startPageNumber`

                            - `JsonValue; type "page_location"constant`

                              - `PAGE_LOCATION("page_location")`

                          - `class CitationContentBlockLocationParam:`

                            - `String citedText`

                            - `long documentIndex`

                            - `Optional<String> documentTitle`

                            - `long endBlockIndex`

                            - `long startBlockIndex`

                            - `JsonValue; type "content_block_location"constant`

                              - `CONTENT_BLOCK_LOCATION("content_block_location")`

                          - `class CitationWebSearchResultLocationParam:`

                            - `String citedText`

                            - `String encryptedIndex`

                            - `Optional<String> title`

                            - `JsonValue; type "web_search_result_location"constant`

                              - `WEB_SEARCH_RESULT_LOCATION("web_search_result_location")`

                            - `String url`

                          - `class CitationSearchResultLocationParam:`

                            - `String citedText`

                            - `long endBlockIndex`

                            - `long searchResultIndex`

                            - `String source`

                            - `long startBlockIndex`

                            - `Optional<String> title`

                            - `JsonValue; type "search_result_location"constant`

                              - `SEARCH_RESULT_LOCATION("search_result_location")`

                      - `class ImageBlockParam:`

                        - `Source source`

                          - `class Base64ImageSource:`

                            - `String data`

                            - `MediaType mediaType`

                              - `IMAGE_JPEG("image/jpeg")`

                              - `IMAGE_PNG("image/png")`

                              - `IMAGE_GIF("image/gif")`

                              - `IMAGE_WEBP("image/webp")`

                            - `JsonValue; type "base64"constant`

                              - `BASE64("base64")`

                          - `class UrlImageSource:`

                            - `JsonValue; type "url"constant`

                              - `URL("url")`

                            - `String url`

                        - `JsonValue; type "image"constant`

                          - `IMAGE("image")`

                        - `Optional<CacheControlEphemeral> cacheControl`

                          Create a cache control breakpoint at this content block.

                          - `JsonValue; type "ephemeral"constant`

                            - `EPHEMERAL("ephemeral")`

                          - `Optional<Ttl> ttl`

                            The time-to-live for the cache control breakpoint.

                            This may be one the following values:

                            - `5m`: 5 minutes
                            - `1h`: 1 hour

                            Defaults to `5m`.

                            - `TTL_5M("5m")`

                            - `TTL_1H("1h")`

                  - `JsonValue; type "content"constant`

                    - `CONTENT("content")`

                - `class UrlPdfSource:`

                  - `JsonValue; type "url"constant`

                    - `URL("url")`

                  - `String url`

              - `JsonValue; type "document"constant`

                - `DOCUMENT("document")`

              - `Optional<CacheControlEphemeral> cacheControl`

                Create a cache control breakpoint at this content block.

                - `JsonValue; type "ephemeral"constant`

                  - `EPHEMERAL("ephemeral")`

                - `Optional<Ttl> ttl`

                  The time-to-live for the cache control breakpoint.

                  This may be one the following values:

                  - `5m`: 5 minutes
                  - `1h`: 1 hour

                  Defaults to `5m`.

                  - `TTL_5M("5m")`

                  - `TTL_1H("1h")`

              - `Optional<CitationsConfigParam> citations`

                - `Optional<Boolean> enabled`

              - `Optional<String> context`

              - `Optional<String> title`

            - `JsonValue; type "web_fetch_result"constant`

              - `WEB_FETCH_RESULT("web_fetch_result")`

            - `String url`

              Fetched content URL

            - `Optional<String> retrievedAt`

              ISO 8601 timestamp when the content was retrieved

        - `String toolUseId`

        - `JsonValue; type "web_fetch_tool_result"constant`

          - `WEB_FETCH_TOOL_RESULT("web_fetch_tool_result")`

        - `Optional<CacheControlEphemeral> cacheControl`

          Create a cache control breakpoint at this content block.

          - `JsonValue; type "ephemeral"constant`

            - `EPHEMERAL("ephemeral")`

          - `Optional<Ttl> ttl`

            The time-to-live for the cache control breakpoint.

            This may be one the following values:

            - `5m`: 5 minutes
            - `1h`: 1 hour

            Defaults to `5m`.

            - `TTL_5M("5m")`

            - `TTL_1H("1h")`

        - `Optional<Caller> caller`

          Tool invocation directly from the model.

          - `class DirectCaller:`

            Tool invocation directly from the model.

            - `JsonValue; type "direct"constant`

              - `DIRECT("direct")`

          - `class ServerToolCaller:`

            Tool invocation generated by a server-side tool.

            - `String toolId`

            - `JsonValue; type "code_execution_20250825"constant`

              - `CODE_EXECUTION_20250825("code_execution_20250825")`

          - `class ServerToolCaller20260120:`

            - `String toolId`

            - `JsonValue; type "code_execution_20260120"constant`

              - `CODE_EXECUTION_20260120("code_execution_20260120")`

      - `class CodeExecutionToolResultBlockParam:`

        - `CodeExecutionToolResultBlockParamContent content`

          Code execution result with encrypted stdout for PFC + web_search results.

          - `class CodeExecutionToolResultErrorParam:`

            - `CodeExecutionToolResultErrorCode errorCode`

              - `INVALID_TOOL_INPUT("invalid_tool_input")`

              - `UNAVAILABLE("unavailable")`

              - `TOO_MANY_REQUESTS("too_many_requests")`

              - `EXECUTION_TIME_EXCEEDED("execution_time_exceeded")`

            - `JsonValue; type "code_execution_tool_result_error"constant`

              - `CODE_EXECUTION_TOOL_RESULT_ERROR("code_execution_tool_result_error")`

          - `class CodeExecutionResultBlockParam:`

            - `List<CodeExecutionOutputBlockParam> content`

              - `String fileId`

              - `JsonValue; type "code_execution_output"constant`

                - `CODE_EXECUTION_OUTPUT("code_execution_output")`

            - `long returnCode`

            - `String stderr`

            - `String stdout`

            - `JsonValue; type "code_execution_result"constant`

              - `CODE_EXECUTION_RESULT("code_execution_result")`

          - `class EncryptedCodeExecutionResultBlockParam:`

            Code execution result with encrypted stdout for PFC + web_search results.

            - `List<CodeExecutionOutputBlockParam> content`

              - `String fileId`

              - `JsonValue; type "code_execution_output"constant`

                - `CODE_EXECUTION_OUTPUT("code_execution_output")`

            - `String encryptedStdout`

            - `long returnCode`

            - `String stderr`

            - `JsonValue; type "encrypted_code_execution_result"constant`

              - `ENCRYPTED_CODE_EXECUTION_RESULT("encrypted_code_execution_result")`

        - `String toolUseId`

        - `JsonValue; type "code_execution_tool_result"constant`

          - `CODE_EXECUTION_TOOL_RESULT("code_execution_tool_result")`

        - `Optional<CacheControlEphemeral> cacheControl`

          Create a cache control breakpoint at this content block.

          - `JsonValue; type "ephemeral"constant`

            - `EPHEMERAL("ephemeral")`

          - `Optional<Ttl> ttl`

            The time-to-live for the cache control breakpoint.

            This may be one the following values:

            - `5m`: 5 minutes
            - `1h`: 1 hour

            Defaults to `5m`.

            - `TTL_5M("5m")`

            - `TTL_1H("1h")`

      - `class BashCodeExecutionToolResultBlockParam:`

        - `Content content`

          - `class BashCodeExecutionToolResultErrorParam:`

            - `BashCodeExecutionToolResultErrorCode errorCode`

              - `INVALID_TOOL_INPUT("invalid_tool_input")`

              - `UNAVAILABLE("unavailable")`

              - `TOO_MANY_REQUESTS("too_many_requests")`

              - `EXECUTION_TIME_EXCEEDED("execution_time_exceeded")`

              - `OUTPUT_FILE_TOO_LARGE("output_file_too_large")`

            - `JsonValue; type "bash_code_execution_tool_result_error"constant`

              - `BASH_CODE_EXECUTION_TOOL_RESULT_ERROR("bash_code_execution_tool_result_error")`

          - `class BashCodeExecutionResultBlockParam:`

            - `List<BashCodeExecutionOutputBlockParam> content`

              - `String fileId`

              - `JsonValue; type "bash_code_execution_output"constant`

                - `BASH_CODE_EXECUTION_OUTPUT("bash_code_execution_output")`

            - `long returnCode`

            - `String stderr`

            - `String stdout`

            - `JsonValue; type "bash_code_execution_result"constant`

              - `BASH_CODE_EXECUTION_RESULT("bash_code_execution_result")`

        - `String toolUseId`

        - `JsonValue; type "bash_code_execution_tool_result"constant`

          - `BASH_CODE_EXECUTION_TOOL_RESULT("bash_code_execution_tool_result")`

        - `Optional<CacheControlEphemeral> cacheControl`

          Create a cache control breakpoint at this content block.

          - `JsonValue; type "ephemeral"constant`

            - `EPHEMERAL("ephemeral")`

          - `Optional<Ttl> ttl`

            The time-to-live for the cache control breakpoint.

            This may be one the following values:

            - `5m`: 5 minutes
            - `1h`: 1 hour

            Defaults to `5m`.

            - `TTL_5M("5m")`

            - `TTL_1H("1h")`

      - `class TextEditorCodeExecutionToolResultBlockParam:`

        - `Content content`

          - `class TextEditorCodeExecutionToolResultErrorParam:`

            - `TextEditorCodeExecutionToolResultErrorCode errorCode`

              - `INVALID_TOOL_INPUT("invalid_tool_input")`

              - `UNAVAILABLE("unavailable")`

              - `TOO_MANY_REQUESTS("too_many_requests")`

              - `EXECUTION_TIME_EXCEEDED("execution_time_exceeded")`

              - `FILE_NOT_FOUND("file_not_found")`

            - `JsonValue; type "text_editor_code_execution_tool_result_error"constant`

              - `TEXT_EDITOR_CODE_EXECUTION_TOOL_RESULT_ERROR("text_editor_code_execution_tool_result_error")`

            - `Optional<String> errorMessage`

          - `class TextEditorCodeExecutionViewResultBlockParam:`

            - `String content`

            - `FileType fileType`

              - `TEXT("text")`

              - `IMAGE("image")`

              - `PDF("pdf")`

            - `JsonValue; type "text_editor_code_execution_view_result"constant`

              - `TEXT_EDITOR_CODE_EXECUTION_VIEW_RESULT("text_editor_code_execution_view_result")`

            - `Optional<Long> numLines`

            - `Optional<Long> startLine`

            - `Optional<Long> totalLines`

          - `class TextEditorCodeExecutionCreateResultBlockParam:`

            - `boolean isFileUpdate`

            - `JsonValue; type "text_editor_code_execution_create_result"constant`

              - `TEXT_EDITOR_CODE_EXECUTION_CREATE_RESULT("text_editor_code_execution_create_result")`

          - `class TextEditorCodeExecutionStrReplaceResultBlockParam:`

            - `JsonValue; type "text_editor_code_execution_str_replace_result"constant`

              - `TEXT_EDITOR_CODE_EXECUTION_STR_REPLACE_RESULT("text_editor_code_execution_str_replace_result")`

            - `Optional<List<String>> lines`

            - `Optional<Long> newLines`

            - `Optional<Long> newStart`

            - `Optional<Long> oldLines`

            - `Optional<Long> oldStart`

        - `String toolUseId`

        - `JsonValue; type "text_editor_code_execution_tool_result"constant`

          - `TEXT_EDITOR_CODE_EXECUTION_TOOL_RESULT("text_editor_code_execution_tool_result")`

        - `Optional<CacheControlEphemeral> cacheControl`

          Create a cache control breakpoint at this content block.

          - `JsonValue; type "ephemeral"constant`

            - `EPHEMERAL("ephemeral")`

          - `Optional<Ttl> ttl`

            The time-to-live for the cache control breakpoint.

            This may be one the following values:

            - `5m`: 5 minutes
            - `1h`: 1 hour

            Defaults to `5m`.

            - `TTL_5M("5m")`

            - `TTL_1H("1h")`

      - `class ToolSearchToolResultBlockParam:`

        - `Content content`

          - `class ToolSearchToolResultErrorParam:`

            - `ToolSearchToolResultErrorCode errorCode`

              - `INVALID_TOOL_INPUT("invalid_tool_input")`

              - `UNAVAILABLE("unavailable")`

              - `TOO_MANY_REQUESTS("too_many_requests")`

              - `EXECUTION_TIME_EXCEEDED("execution_time_exceeded")`

            - `JsonValue; type "tool_search_tool_result_error"constant`

              - `TOOL_SEARCH_TOOL_RESULT_ERROR("tool_search_tool_result_error")`

          - `class ToolSearchToolSearchResultBlockParam:`

            - `List<ToolReferenceBlockParam> toolReferences`

              - `String toolName`

              - `JsonValue; type "tool_reference"constant`

                - `TOOL_REFERENCE("tool_reference")`

              - `Optional<CacheControlEphemeral> cacheControl`

                Create a cache control breakpoint at this content block.

                - `JsonValue; type "ephemeral"constant`

                  - `EPHEMERAL("ephemeral")`

                - `Optional<Ttl> ttl`

                  The time-to-live for the cache control breakpoint.

                  This may be one the following values:

                  - `5m`: 5 minutes
                  - `1h`: 1 hour

                  Defaults to `5m`.

                  - `TTL_5M("5m")`

                  - `TTL_1H("1h")`

            - `JsonValue; type "tool_search_tool_search_result"constant`

              - `TOOL_SEARCH_TOOL_SEARCH_RESULT("tool_search_tool_search_result")`

        - `String toolUseId`

        - `JsonValue; type "tool_search_tool_result"constant`

          - `TOOL_SEARCH_TOOL_RESULT("tool_search_tool_result")`

        - `Optional<CacheControlEphemeral> cacheControl`

          Create a cache control breakpoint at this content block.

          - `JsonValue; type "ephemeral"constant`

            - `EPHEMERAL("ephemeral")`

          - `Optional<Ttl> ttl`

            The time-to-live for the cache control breakpoint.

            This may be one the following values:

            - `5m`: 5 minutes
            - `1h`: 1 hour

            Defaults to `5m`.

            - `TTL_5M("5m")`

            - `TTL_1H("1h")`

      - `class ContainerUploadBlockParam:`

        A content block that represents a file to be uploaded to the container
        Files uploaded via this block will be available in the container's input directory.

        - `String fileId`

        - `JsonValue; type "container_upload"constant`

          - `CONTAINER_UPLOAD("container_upload")`

        - `Optional<CacheControlEphemeral> cacheControl`

          Create a cache control breakpoint at this content block.

          - `JsonValue; type "ephemeral"constant`

            - `EPHEMERAL("ephemeral")`

          - `Optional<Ttl> ttl`

            The time-to-live for the cache control breakpoint.

            This may be one the following values:

            - `5m`: 5 minutes
            - `1h`: 1 hour

            Defaults to `5m`.

            - `TTL_5M("5m")`

            - `TTL_1H("1h")`

  - `Role role`

    - `USER("user")`

    - `ASSISTANT("assistant")`

### Message Tokens Count

- `class MessageTokensCount:`

  - `long inputTokens`

    The total number of tokens across the provided list of messages, system prompt, and tools.

### Metadata

- `class Metadata:`

  - `Optional<String> userId`

    An external identifier for the user who is associated with the request.

    This should be a uuid, hash value, or other opaque identifier. Anthropic may use this id to help detect abuse. Do not include any identifying information such as name, email address, or phone number.

### Output Config

- `class OutputConfig:`

  - `Optional<Effort> effort`

    All possible effort levels.

    - `LOW("low")`

    - `MEDIUM("medium")`

    - `HIGH("high")`

    - `MAX("max")`

  - `Optional<JsonOutputFormat> format`

    A schema to specify Claude's output format in responses. See [structured outputs](https://platform.claude.com/docs/en/build-with-claude/structured-outputs)

    - `Schema schema`

      The JSON schema of the format

    - `JsonValue; type "json_schema"constant`

      - `JSON_SCHEMA("json_schema")`

### Plain Text Source

- `class PlainTextSource:`

  - `String data`

  - `JsonValue; mediaType "text/plain"constant`

    - `TEXT_PLAIN("text/plain")`

  - `JsonValue; type "text"constant`

    - `TEXT("text")`

### Raw Content Block Delta

- `class RawContentBlockDelta: A class that can be one of several variants.union`

  - `class TextDelta:`

    - `String text`

    - `JsonValue; type "text_delta"constant`

      - `TEXT_DELTA("text_delta")`

  - `class InputJsonDelta:`

    - `String partialJson`

    - `JsonValue; type "input_json_delta"constant`

      - `INPUT_JSON_DELTA("input_json_delta")`

  - `class CitationsDelta:`

    - `Citation citation`

      - `class CitationCharLocation:`

        - `String citedText`

        - `long documentIndex`

        - `Optional<String> documentTitle`

        - `long endCharIndex`

        - `Optional<String> fileId`

        - `long startCharIndex`

        - `JsonValue; type "char_location"constant`

          - `CHAR_LOCATION("char_location")`

      - `class CitationPageLocation:`

        - `String citedText`

        - `long documentIndex`

        - `Optional<String> documentTitle`

        - `long endPageNumber`

        - `Optional<String> fileId`

        - `long startPageNumber`

        - `JsonValue; type "page_location"constant`

          - `PAGE_LOCATION("page_location")`

      - `class CitationContentBlockLocation:`

        - `String citedText`

        - `long documentIndex`

        - `Optional<String> documentTitle`

        - `long endBlockIndex`

        - `Optional<String> fileId`

        - `long startBlockIndex`

        - `JsonValue; type "content_block_location"constant`

          - `CONTENT_BLOCK_LOCATION("content_block_location")`

      - `class CitationsWebSearchResultLocation:`

        - `String citedText`

        - `String encryptedIndex`

        - `Optional<String> title`

        - `JsonValue; type "web_search_result_location"constant`

          - `WEB_SEARCH_RESULT_LOCATION("web_search_result_location")`

        - `String url`

      - `class CitationsSearchResultLocation:`

        - `String citedText`

        - `long endBlockIndex`

        - `long searchResultIndex`

        - `String source`

        - `long startBlockIndex`

        - `Optional<String> title`

        - `JsonValue; type "search_result_location"constant`

          - `SEARCH_RESULT_LOCATION("search_result_location")`

    - `JsonValue; type "citations_delta"constant`

      - `CITATIONS_DELTA("citations_delta")`

  - `class ThinkingDelta:`

    - `String thinking`

    - `JsonValue; type "thinking_delta"constant`

      - `THINKING_DELTA("thinking_delta")`

  - `class SignatureDelta:`

    - `String signature`

    - `JsonValue; type "signature_delta"constant`

      - `SIGNATURE_DELTA("signature_delta")`

### Raw Content Block Delta Event

- `class RawContentBlockDeltaEvent:`

  - `RawContentBlockDelta delta`

    - `class TextDelta:`

      - `String text`

      - `JsonValue; type "text_delta"constant`

        - `TEXT_DELTA("text_delta")`

    - `class InputJsonDelta:`

      - `String partialJson`

      - `JsonValue; type "input_json_delta"constant`

        - `INPUT_JSON_DELTA("input_json_delta")`

    - `class CitationsDelta:`

      - `Citation citation`

        - `class CitationCharLocation:`

          - `String citedText`

          - `long documentIndex`

          - `Optional<String> documentTitle`

          - `long endCharIndex`

          - `Optional<String> fileId`

          - `long startCharIndex`

          - `JsonValue; type "char_location"constant`

            - `CHAR_LOCATION("char_location")`

        - `class CitationPageLocation:`

          - `String citedText`

          - `long documentIndex`

          - `Optional<String> documentTitle`

          - `long endPageNumber`

          - `Optional<String> fileId`

          - `long startPageNumber`

          - `JsonValue; type "page_location"constant`

            - `PAGE_LOCATION("page_location")`

        - `class CitationContentBlockLocation:`

          - `String citedText`

          - `long documentIndex`

          - `Optional<String> documentTitle`

          - `long endBlockIndex`

          - `Optional<String> fileId`

          - `long startBlockIndex`

          - `JsonValue; type "content_block_location"constant`

            - `CONTENT_BLOCK_LOCATION("content_block_location")`

        - `class CitationsWebSearchResultLocation:`

          - `String citedText`

          - `String encryptedIndex`

          - `Optional<String> title`

          - `JsonValue; type "web_search_result_location"constant`

            - `WEB_SEARCH_RESULT_LOCATION("web_search_result_location")`

          - `String url`

        - `class CitationsSearchResultLocation:`

          - `String citedText`

          - `long endBlockIndex`

          - `long searchResultIndex`

          - `String source`

          - `long startBlockIndex`

          - `Optional<String> title`

          - `JsonValue; type "search_result_location"constant`

            - `SEARCH_RESULT_LOCATION("search_result_location")`

      - `JsonValue; type "citations_delta"constant`

        - `CITATIONS_DELTA("citations_delta")`

    - `class ThinkingDelta:`

      - `String thinking`

      - `JsonValue; type "thinking_delta"constant`

        - `THINKING_DELTA("thinking_delta")`

    - `class SignatureDelta:`

      - `String signature`

      - `JsonValue; type "signature_delta"constant`

        - `SIGNATURE_DELTA("signature_delta")`

  - `long index`

  - `JsonValue; type "content_block_delta"constant`

    - `CONTENT_BLOCK_DELTA("content_block_delta")`

### Raw Content Block Start Event

- `class RawContentBlockStartEvent:`

  - `ContentBlock contentBlock`

    Response model for a file uploaded to the container.

    - `class TextBlock:`

      - `Optional<List<TextCitation>> citations`

        Citations supporting the text block.

        The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

        - `class CitationCharLocation:`

          - `String citedText`

          - `long documentIndex`

          - `Optional<String> documentTitle`

          - `long endCharIndex`

          - `Optional<String> fileId`

          - `long startCharIndex`

          - `JsonValue; type "char_location"constant`

            - `CHAR_LOCATION("char_location")`

        - `class CitationPageLocation:`

          - `String citedText`

          - `long documentIndex`

          - `Optional<String> documentTitle`

          - `long endPageNumber`

          - `Optional<String> fileId`

          - `long startPageNumber`

          - `JsonValue; type "page_location"constant`

            - `PAGE_LOCATION("page_location")`

        - `class CitationContentBlockLocation:`

          - `String citedText`

          - `long documentIndex`

          - `Optional<String> documentTitle`

          - `long endBlockIndex`

          - `Optional<String> fileId`

          - `long startBlockIndex`

          - `JsonValue; type "content_block_location"constant`

            - `CONTENT_BLOCK_LOCATION("content_block_location")`

        - `class CitationsWebSearchResultLocation:`

          - `String citedText`

          - `String encryptedIndex`

          - `Optional<String> title`

          - `JsonValue; type "web_search_result_location"constant`

            - `WEB_SEARCH_RESULT_LOCATION("web_search_result_location")`

          - `String url`

        - `class CitationsSearchResultLocation:`

          - `String citedText`

          - `long endBlockIndex`

          - `long searchResultIndex`

          - `String source`

          - `long startBlockIndex`

          - `Optional<String> title`

          - `JsonValue; type "search_result_location"constant`

            - `SEARCH_RESULT_LOCATION("search_result_location")`

      - `String text`

      - `JsonValue; type "text"constant`

        - `TEXT("text")`

    - `class ThinkingBlock:`

      - `String signature`

      - `String thinking`

      - `JsonValue; type "thinking"constant`

        - `THINKING("thinking")`

    - `class RedactedThinkingBlock:`

      - `String data`

      - `JsonValue; type "redacted_thinking"constant`

        - `REDACTED_THINKING("redacted_thinking")`

    - `class ToolUseBlock:`

      - `String id`

      - `Caller caller`

        Tool invocation directly from the model.

        - `class DirectCaller:`

          Tool invocation directly from the model.

          - `JsonValue; type "direct"constant`

            - `DIRECT("direct")`

        - `class ServerToolCaller:`

          Tool invocation generated by a server-side tool.

          - `String toolId`

          - `JsonValue; type "code_execution_20250825"constant`

            - `CODE_EXECUTION_20250825("code_execution_20250825")`

        - `class ServerToolCaller20260120:`

          - `String toolId`

          - `JsonValue; type "code_execution_20260120"constant`

            - `CODE_EXECUTION_20260120("code_execution_20260120")`

      - `Input input`

      - `String name`

      - `JsonValue; type "tool_use"constant`

        - `TOOL_USE("tool_use")`

    - `class ServerToolUseBlock:`

      - `String id`

      - `Caller caller`

        Tool invocation directly from the model.

        - `class DirectCaller:`

          Tool invocation directly from the model.

          - `JsonValue; type "direct"constant`

            - `DIRECT("direct")`

        - `class ServerToolCaller:`

          Tool invocation generated by a server-side tool.

          - `String toolId`

          - `JsonValue; type "code_execution_20250825"constant`

            - `CODE_EXECUTION_20250825("code_execution_20250825")`

        - `class ServerToolCaller20260120:`

          - `String toolId`

          - `JsonValue; type "code_execution_20260120"constant`

            - `CODE_EXECUTION_20260120("code_execution_20260120")`

      - `Input input`

      - `Name name`

        - `WEB_SEARCH("web_search")`

        - `WEB_FETCH("web_fetch")`

        - `CODE_EXECUTION("code_execution")`

        - `BASH_CODE_EXECUTION("bash_code_execution")`

        - `TEXT_EDITOR_CODE_EXECUTION("text_editor_code_execution")`

        - `TOOL_SEARCH_TOOL_REGEX("tool_search_tool_regex")`

        - `TOOL_SEARCH_TOOL_BM25("tool_search_tool_bm25")`

      - `JsonValue; type "server_tool_use"constant`

        - `SERVER_TOOL_USE("server_tool_use")`

    - `class WebSearchToolResultBlock:`

      - `Caller caller`

        Tool invocation directly from the model.

        - `class DirectCaller:`

          Tool invocation directly from the model.

          - `JsonValue; type "direct"constant`

            - `DIRECT("direct")`

        - `class ServerToolCaller:`

          Tool invocation generated by a server-side tool.

          - `String toolId`

          - `JsonValue; type "code_execution_20250825"constant`

            - `CODE_EXECUTION_20250825("code_execution_20250825")`

        - `class ServerToolCaller20260120:`

          - `String toolId`

          - `JsonValue; type "code_execution_20260120"constant`

            - `CODE_EXECUTION_20260120("code_execution_20260120")`

      - `WebSearchToolResultBlockContent content`

        - `class WebSearchToolResultError:`

          - `WebSearchToolResultErrorCode errorCode`

            - `INVALID_TOOL_INPUT("invalid_tool_input")`

            - `UNAVAILABLE("unavailable")`

            - `MAX_USES_EXCEEDED("max_uses_exceeded")`

            - `TOO_MANY_REQUESTS("too_many_requests")`

            - `QUERY_TOO_LONG("query_too_long")`

            - `REQUEST_TOO_LARGE("request_too_large")`

          - `JsonValue; type "web_search_tool_result_error"constant`

            - `WEB_SEARCH_TOOL_RESULT_ERROR("web_search_tool_result_error")`

        - `List<WebSearchResultBlock>`

          - `String encryptedContent`

          - `Optional<String> pageAge`

          - `String title`

          - `JsonValue; type "web_search_result"constant`

            - `WEB_SEARCH_RESULT("web_search_result")`

          - `String url`

      - `String toolUseId`

      - `JsonValue; type "web_search_tool_result"constant`

        - `WEB_SEARCH_TOOL_RESULT("web_search_tool_result")`

    - `class WebFetchToolResultBlock:`

      - `Caller caller`

        Tool invocation directly from the model.

        - `class DirectCaller:`

          Tool invocation directly from the model.

          - `JsonValue; type "direct"constant`

            - `DIRECT("direct")`

        - `class ServerToolCaller:`

          Tool invocation generated by a server-side tool.

          - `String toolId`

          - `JsonValue; type "code_execution_20250825"constant`

            - `CODE_EXECUTION_20250825("code_execution_20250825")`

        - `class ServerToolCaller20260120:`

          - `String toolId`

          - `JsonValue; type "code_execution_20260120"constant`

            - `CODE_EXECUTION_20260120("code_execution_20260120")`

      - `Content content`

        - `class WebFetchToolResultErrorBlock:`

          - `WebFetchToolResultErrorCode errorCode`

            - `INVALID_TOOL_INPUT("invalid_tool_input")`

            - `URL_TOO_LONG("url_too_long")`

            - `URL_NOT_ALLOWED("url_not_allowed")`

            - `URL_NOT_ACCESSIBLE("url_not_accessible")`

            - `UNSUPPORTED_CONTENT_TYPE("unsupported_content_type")`

            - `TOO_MANY_REQUESTS("too_many_requests")`

            - `MAX_USES_EXCEEDED("max_uses_exceeded")`

            - `UNAVAILABLE("unavailable")`

          - `JsonValue; type "web_fetch_tool_result_error"constant`

            - `WEB_FETCH_TOOL_RESULT_ERROR("web_fetch_tool_result_error")`

        - `class WebFetchBlock:`

          - `DocumentBlock content`

            - `Optional<CitationsConfig> citations`

              Citation configuration for the document

              - `boolean enabled`

            - `Source source`

              - `class Base64PdfSource:`

                - `String data`

                - `JsonValue; mediaType "application/pdf"constant`

                  - `APPLICATION_PDF("application/pdf")`

                - `JsonValue; type "base64"constant`

                  - `BASE64("base64")`

              - `class PlainTextSource:`

                - `String data`

                - `JsonValue; mediaType "text/plain"constant`

                  - `TEXT_PLAIN("text/plain")`

                - `JsonValue; type "text"constant`

                  - `TEXT("text")`

            - `Optional<String> title`

              The title of the document

            - `JsonValue; type "document"constant`

              - `DOCUMENT("document")`

          - `Optional<String> retrievedAt`

            ISO 8601 timestamp when the content was retrieved

          - `JsonValue; type "web_fetch_result"constant`

            - `WEB_FETCH_RESULT("web_fetch_result")`

          - `String url`

            Fetched content URL

      - `String toolUseId`

      - `JsonValue; type "web_fetch_tool_result"constant`

        - `WEB_FETCH_TOOL_RESULT("web_fetch_tool_result")`

    - `class CodeExecutionToolResultBlock:`

      - `CodeExecutionToolResultBlockContent content`

        Code execution result with encrypted stdout for PFC + web_search results.

        - `class CodeExecutionToolResultError:`

          - `CodeExecutionToolResultErrorCode errorCode`

            - `INVALID_TOOL_INPUT("invalid_tool_input")`

            - `UNAVAILABLE("unavailable")`

            - `TOO_MANY_REQUESTS("too_many_requests")`

            - `EXECUTION_TIME_EXCEEDED("execution_time_exceeded")`

          - `JsonValue; type "code_execution_tool_result_error"constant`

            - `CODE_EXECUTION_TOOL_RESULT_ERROR("code_execution_tool_result_error")`

        - `class CodeExecutionResultBlock:`

          - `List<CodeExecutionOutputBlock> content`

            - `String fileId`

            - `JsonValue; type "code_execution_output"constant`

              - `CODE_EXECUTION_OUTPUT("code_execution_output")`

          - `long returnCode`

          - `String stderr`

          - `String stdout`

          - `JsonValue; type "code_execution_result"constant`

            - `CODE_EXECUTION_RESULT("code_execution_result")`

        - `class EncryptedCodeExecutionResultBlock:`

          Code execution result with encrypted stdout for PFC + web_search results.

          - `List<CodeExecutionOutputBlock> content`

            - `String fileId`

            - `JsonValue; type "code_execution_output"constant`

              - `CODE_EXECUTION_OUTPUT("code_execution_output")`

          - `String encryptedStdout`

          - `long returnCode`

          - `String stderr`

          - `JsonValue; type "encrypted_code_execution_result"constant`

            - `ENCRYPTED_CODE_EXECUTION_RESULT("encrypted_code_execution_result")`

      - `String toolUseId`

      - `JsonValue; type "code_execution_tool_result"constant`

        - `CODE_EXECUTION_TOOL_RESULT("code_execution_tool_result")`

    - `class BashCodeExecutionToolResultBlock:`

      - `Content content`

        - `class BashCodeExecutionToolResultError:`

          - `BashCodeExecutionToolResultErrorCode errorCode`

            - `INVALID_TOOL_INPUT("invalid_tool_input")`

            - `UNAVAILABLE("unavailable")`

            - `TOO_MANY_REQUESTS("too_many_requests")`

            - `EXECUTION_TIME_EXCEEDED("execution_time_exceeded")`

            - `OUTPUT_FILE_TOO_LARGE("output_file_too_large")`

          - `JsonValue; type "bash_code_execution_tool_result_error"constant`

            - `BASH_CODE_EXECUTION_TOOL_RESULT_ERROR("bash_code_execution_tool_result_error")`

        - `class BashCodeExecutionResultBlock:`

          - `List<BashCodeExecutionOutputBlock> content`

            - `String fileId`

            - `JsonValue; type "bash_code_execution_output"constant`

              - `BASH_CODE_EXECUTION_OUTPUT("bash_code_execution_output")`

          - `long returnCode`

          - `String stderr`

          - `String stdout`

          - `JsonValue; type "bash_code_execution_result"constant`

            - `BASH_CODE_EXECUTION_RESULT("bash_code_execution_result")`

      - `String toolUseId`

      - `JsonValue; type "bash_code_execution_tool_result"constant`

        - `BASH_CODE_EXECUTION_TOOL_RESULT("bash_code_execution_tool_result")`

    - `class TextEditorCodeExecutionToolResultBlock:`

      - `Content content`

        - `class TextEditorCodeExecutionToolResultError:`

          - `TextEditorCodeExecutionToolResultErrorCode errorCode`

            - `INVALID_TOOL_INPUT("invalid_tool_input")`

            - `UNAVAILABLE("unavailable")`

            - `TOO_MANY_REQUESTS("too_many_requests")`

            - `EXECUTION_TIME_EXCEEDED("execution_time_exceeded")`

            - `FILE_NOT_FOUND("file_not_found")`

          - `Optional<String> errorMessage`

          - `JsonValue; type "text_editor_code_execution_tool_result_error"constant`

            - `TEXT_EDITOR_CODE_EXECUTION_TOOL_RESULT_ERROR("text_editor_code_execution_tool_result_error")`

        - `class TextEditorCodeExecutionViewResultBlock:`

          - `String content`

          - `FileType fileType`

            - `TEXT("text")`

            - `IMAGE("image")`

            - `PDF("pdf")`

          - `Optional<Long> numLines`

          - `Optional<Long> startLine`

          - `Optional<Long> totalLines`

          - `JsonValue; type "text_editor_code_execution_view_result"constant`

            - `TEXT_EDITOR_CODE_EXECUTION_VIEW_RESULT("text_editor_code_execution_view_result")`

        - `class TextEditorCodeExecutionCreateResultBlock:`

          - `boolean isFileUpdate`

          - `JsonValue; type "text_editor_code_execution_create_result"constant`

            - `TEXT_EDITOR_CODE_EXECUTION_CREATE_RESULT("text_editor_code_execution_create_result")`

        - `class TextEditorCodeExecutionStrReplaceResultBlock:`

          - `Optional<List<String>> lines`

          - `Optional<Long> newLines`

          - `Optional<Long> newStart`

          - `Optional<Long> oldLines`

          - `Optional<Long> oldStart`

          - `JsonValue; type "text_editor_code_execution_str_replace_result"constant`

            - `TEXT_EDITOR_CODE_EXECUTION_STR_REPLACE_RESULT("text_editor_code_execution_str_replace_result")`

      - `String toolUseId`

      - `JsonValue; type "text_editor_code_execution_tool_result"constant`

        - `TEXT_EDITOR_CODE_EXECUTION_TOOL_RESULT("text_editor_code_execution_tool_result")`

    - `class ToolSearchToolResultBlock:`

      - `Content content`

        - `class ToolSearchToolResultError:`

          - `ToolSearchToolResultErrorCode errorCode`

            - `INVALID_TOOL_INPUT("invalid_tool_input")`

            - `UNAVAILABLE("unavailable")`

            - `TOO_MANY_REQUESTS("too_many_requests")`

            - `EXECUTION_TIME_EXCEEDED("execution_time_exceeded")`

          - `Optional<String> errorMessage`

          - `JsonValue; type "tool_search_tool_result_error"constant`

            - `TOOL_SEARCH_TOOL_RESULT_ERROR("tool_search_tool_result_error")`

        - `class ToolSearchToolSearchResultBlock:`

          - `List<ToolReferenceBlock> toolReferences`

            - `String toolName`

            - `JsonValue; type "tool_reference"constant`

              - `TOOL_REFERENCE("tool_reference")`

          - `JsonValue; type "tool_search_tool_search_result"constant`

            - `TOOL_SEARCH_TOOL_SEARCH_RESULT("tool_search_tool_search_result")`

      - `String toolUseId`

      - `JsonValue; type "tool_search_tool_result"constant`

        - `TOOL_SEARCH_TOOL_RESULT("tool_search_tool_result")`

    - `class ContainerUploadBlock:`

      Response model for a file uploaded to the container.

      - `String fileId`

      - `JsonValue; type "container_upload"constant`

        - `CONTAINER_UPLOAD("container_upload")`

  - `long index`

  - `JsonValue; type "content_block_start"constant`

    - `CONTENT_BLOCK_START("content_block_start")`

### Raw Content Block Stop Event

- `class RawContentBlockStopEvent:`

  - `long index`

  - `JsonValue; type "content_block_stop"constant`

    - `CONTENT_BLOCK_STOP("content_block_stop")`

### Raw Message Delta Event

- `class RawMessageDeltaEvent:`

  - `Delta delta`

    - `Optional<Container> container`

      Information about the container used in the request (for the code execution tool)

      - `String id`

        Identifier for the container used in this request

      - `LocalDateTime expiresAt`

        The time at which the container will expire.

    - `Optional<StopReason> stopReason`

      - `END_TURN("end_turn")`

      - `MAX_TOKENS("max_tokens")`

      - `STOP_SEQUENCE("stop_sequence")`

      - `TOOL_USE("tool_use")`

      - `PAUSE_TURN("pause_turn")`

      - `REFUSAL("refusal")`

    - `Optional<String> stopSequence`

  - `JsonValue; type "message_delta"constant`

    - `MESSAGE_DELTA("message_delta")`

  - `MessageDeltaUsage usage`

    Billing and rate-limit usage.

    Anthropic's API bills and rate-limits by token counts, as tokens represent the underlying cost to our systems.

    Under the hood, the API transforms requests into a format suitable for the model. The model's output then goes through a parsing stage before becoming an API response. As a result, the token counts in `usage` will not match one-to-one with the exact visible content of an API request or response.

    For example, `output_tokens` will be non-zero, even for an empty string response from Claude.

    Total input tokens in a request is the summation of `input_tokens`, `cache_creation_input_tokens`, and `cache_read_input_tokens`.

    - `Optional<Long> cacheCreationInputTokens`

      The cumulative number of input tokens used to create the cache entry.

    - `Optional<Long> cacheReadInputTokens`

      The cumulative number of input tokens read from the cache.

    - `Optional<Long> inputTokens`

      The cumulative number of input tokens which were used.

    - `long outputTokens`

      The cumulative number of output tokens which were used.

    - `Optional<ServerToolUsage> serverToolUse`

      The number of server tool requests.

      - `long webFetchRequests`

        The number of web fetch tool requests.

      - `long webSearchRequests`

        The number of web search tool requests.

### Raw Message Start Event

- `class RawMessageStartEvent:`

  - `Message message`

    - `String id`

      Unique object identifier.

      The format and length of IDs may change over time.

    - `Optional<Container> container`

      Information about the container used in the request (for the code execution tool)

      - `String id`

        Identifier for the container used in this request

      - `LocalDateTime expiresAt`

        The time at which the container will expire.

    - `List<ContentBlock> content`

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

      - `class TextBlock:`

        - `Optional<List<TextCitation>> citations`

          Citations supporting the text block.

          The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

          - `class CitationCharLocation:`

            - `String citedText`

            - `long documentIndex`

            - `Optional<String> documentTitle`

            - `long endCharIndex`

            - `Optional<String> fileId`

            - `long startCharIndex`

            - `JsonValue; type "char_location"constant`

              - `CHAR_LOCATION("char_location")`

          - `class CitationPageLocation:`

            - `String citedText`

            - `long documentIndex`

            - `Optional<String> documentTitle`

            - `long endPageNumber`

            - `Optional<String> fileId`

            - `long startPageNumber`

            - `JsonValue; type "page_location"constant`

              - `PAGE_LOCATION("page_location")`

          - `class CitationContentBlockLocation:`

            - `String citedText`

            - `long documentIndex`

            - `Optional<String> documentTitle`

            - `long endBlockIndex`

            - `Optional<String> fileId`

            - `long startBlockIndex`

            - `JsonValue; type "content_block_location"constant`

              - `CONTENT_BLOCK_LOCATION("content_block_location")`

          - `class CitationsWebSearchResultLocation:`

            - `String citedText`

            - `String encryptedIndex`

            - `Optional<String> title`

            - `JsonValue; type "web_search_result_location"constant`

              - `WEB_SEARCH_RESULT_LOCATION("web_search_result_location")`

            - `String url`

          - `class CitationsSearchResultLocation:`

            - `String citedText`

            - `long endBlockIndex`

            - `long searchResultIndex`

            - `String source`

            - `long startBlockIndex`

            - `Optional<String> title`

            - `JsonValue; type "search_result_location"constant`

              - `SEARCH_RESULT_LOCATION("search_result_location")`

        - `String text`

        - `JsonValue; type "text"constant`

          - `TEXT("text")`

      - `class ThinkingBlock:`

        - `String signature`

        - `String thinking`

        - `JsonValue; type "thinking"constant`

          - `THINKING("thinking")`

      - `class RedactedThinkingBlock:`

        - `String data`

        - `JsonValue; type "redacted_thinking"constant`

          - `REDACTED_THINKING("redacted_thinking")`

      - `class ToolUseBlock:`

        - `String id`

        - `Caller caller`

          Tool invocation directly from the model.

          - `class DirectCaller:`

            Tool invocation directly from the model.

            - `JsonValue; type "direct"constant`

              - `DIRECT("direct")`

          - `class ServerToolCaller:`

            Tool invocation generated by a server-side tool.

            - `String toolId`

            - `JsonValue; type "code_execution_20250825"constant`

              - `CODE_EXECUTION_20250825("code_execution_20250825")`

          - `class ServerToolCaller20260120:`

            - `String toolId`

            - `JsonValue; type "code_execution_20260120"constant`

              - `CODE_EXECUTION_20260120("code_execution_20260120")`

        - `Input input`

        - `String name`

        - `JsonValue; type "tool_use"constant`

          - `TOOL_USE("tool_use")`

      - `class ServerToolUseBlock:`

        - `String id`

        - `Caller caller`

          Tool invocation directly from the model.

          - `class DirectCaller:`

            Tool invocation directly from the model.

            - `JsonValue; type "direct"constant`

              - `DIRECT("direct")`

          - `class ServerToolCaller:`

            Tool invocation generated by a server-side tool.

            - `String toolId`

            - `JsonValue; type "code_execution_20250825"constant`

              - `CODE_EXECUTION_20250825("code_execution_20250825")`

          - `class ServerToolCaller20260120:`

            - `String toolId`

            - `JsonValue; type "code_execution_20260120"constant`

              - `CODE_EXECUTION_20260120("code_execution_20260120")`

        - `Input input`

        - `Name name`

          - `WEB_SEARCH("web_search")`

          - `WEB_FETCH("web_fetch")`

          - `CODE_EXECUTION("code_execution")`

          - `BASH_CODE_EXECUTION("bash_code_execution")`

          - `TEXT_EDITOR_CODE_EXECUTION("text_editor_code_execution")`

          - `TOOL_SEARCH_TOOL_REGEX("tool_search_tool_regex")`

          - `TOOL_SEARCH_TOOL_BM25("tool_search_tool_bm25")`

        - `JsonValue; type "server_tool_use"constant`

          - `SERVER_TOOL_USE("server_tool_use")`

      - `class WebSearchToolResultBlock:`

        - `Caller caller`

          Tool invocation directly from the model.

          - `class DirectCaller:`

            Tool invocation directly from the model.

            - `JsonValue; type "direct"constant`

              - `DIRECT("direct")`

          - `class ServerToolCaller:`

            Tool invocation generated by a server-side tool.

            - `String toolId`

            - `JsonValue; type "code_execution_20250825"constant`

              - `CODE_EXECUTION_20250825("code_execution_20250825")`

          - `class ServerToolCaller20260120:`

            - `String toolId`

            - `JsonValue; type "code_execution_20260120"constant`

              - `CODE_EXECUTION_20260120("code_execution_20260120")`

        - `WebSearchToolResultBlockContent content`

          - `class WebSearchToolResultError:`

            - `WebSearchToolResultErrorCode errorCode`

              - `INVALID_TOOL_INPUT("invalid_tool_input")`

              - `UNAVAILABLE("unavailable")`

              - `MAX_USES_EXCEEDED("max_uses_exceeded")`

              - `TOO_MANY_REQUESTS("too_many_requests")`

              - `QUERY_TOO_LONG("query_too_long")`

              - `REQUEST_TOO_LARGE("request_too_large")`

            - `JsonValue; type "web_search_tool_result_error"constant`

              - `WEB_SEARCH_TOOL_RESULT_ERROR("web_search_tool_result_error")`

          - `List<WebSearchResultBlock>`

            - `String encryptedContent`

            - `Optional<String> pageAge`

            - `String title`

            - `JsonValue; type "web_search_result"constant`

              - `WEB_SEARCH_RESULT("web_search_result")`

            - `String url`

        - `String toolUseId`

        - `JsonValue; type "web_search_tool_result"constant`

          - `WEB_SEARCH_TOOL_RESULT("web_search_tool_result")`

      - `class WebFetchToolResultBlock:`

        - `Caller caller`

          Tool invocation directly from the model.

          - `class DirectCaller:`

            Tool invocation directly from the model.

            - `JsonValue; type "direct"constant`

              - `DIRECT("direct")`

          - `class ServerToolCaller:`

            Tool invocation generated by a server-side tool.

            - `String toolId`

            - `JsonValue; type "code_execution_20250825"constant`

              - `CODE_EXECUTION_20250825("code_execution_20250825")`

          - `class ServerToolCaller20260120:`

            - `String toolId`

            - `JsonValue; type "code_execution_20260120"constant`

              - `CODE_EXECUTION_20260120("code_execution_20260120")`

        - `Content content`

          - `class WebFetchToolResultErrorBlock:`

            - `WebFetchToolResultErrorCode errorCode`

              - `INVALID_TOOL_INPUT("invalid_tool_input")`

              - `URL_TOO_LONG("url_too_long")`

              - `URL_NOT_ALLOWED("url_not_allowed")`

              - `URL_NOT_ACCESSIBLE("url_not_accessible")`

              - `UNSUPPORTED_CONTENT_TYPE("unsupported_content_type")`

              - `TOO_MANY_REQUESTS("too_many_requests")`

              - `MAX_USES_EXCEEDED("max_uses_exceeded")`

              - `UNAVAILABLE("unavailable")`

            - `JsonValue; type "web_fetch_tool_result_error"constant`

              - `WEB_FETCH_TOOL_RESULT_ERROR("web_fetch_tool_result_error")`

          - `class WebFetchBlock:`

            - `DocumentBlock content`

              - `Optional<CitationsConfig> citations`

                Citation configuration for the document

                - `boolean enabled`

              - `Source source`

                - `class Base64PdfSource:`

                  - `String data`

                  - `JsonValue; mediaType "application/pdf"constant`

                    - `APPLICATION_PDF("application/pdf")`

                  - `JsonValue; type "base64"constant`

                    - `BASE64("base64")`

                - `class PlainTextSource:`

                  - `String data`

                  - `JsonValue; mediaType "text/plain"constant`

                    - `TEXT_PLAIN("text/plain")`

                  - `JsonValue; type "text"constant`

                    - `TEXT("text")`

              - `Optional<String> title`

                The title of the document

              - `JsonValue; type "document"constant`

                - `DOCUMENT("document")`

            - `Optional<String> retrievedAt`

              ISO 8601 timestamp when the content was retrieved

            - `JsonValue; type "web_fetch_result"constant`

              - `WEB_FETCH_RESULT("web_fetch_result")`

            - `String url`

              Fetched content URL

        - `String toolUseId`

        - `JsonValue; type "web_fetch_tool_result"constant`

          - `WEB_FETCH_TOOL_RESULT("web_fetch_tool_result")`

      - `class CodeExecutionToolResultBlock:`

        - `CodeExecutionToolResultBlockContent content`

          Code execution result with encrypted stdout for PFC + web_search results.

          - `class CodeExecutionToolResultError:`

            - `CodeExecutionToolResultErrorCode errorCode`

              - `INVALID_TOOL_INPUT("invalid_tool_input")`

              - `UNAVAILABLE("unavailable")`

              - `TOO_MANY_REQUESTS("too_many_requests")`

              - `EXECUTION_TIME_EXCEEDED("execution_time_exceeded")`

            - `JsonValue; type "code_execution_tool_result_error"constant`

              - `CODE_EXECUTION_TOOL_RESULT_ERROR("code_execution_tool_result_error")`

          - `class CodeExecutionResultBlock:`

            - `List<CodeExecutionOutputBlock> content`

              - `String fileId`

              - `JsonValue; type "code_execution_output"constant`

                - `CODE_EXECUTION_OUTPUT("code_execution_output")`

            - `long returnCode`

            - `String stderr`

            - `String stdout`

            - `JsonValue; type "code_execution_result"constant`

              - `CODE_EXECUTION_RESULT("code_execution_result")`

          - `class EncryptedCodeExecutionResultBlock:`

            Code execution result with encrypted stdout for PFC + web_search results.

            - `List<CodeExecutionOutputBlock> content`

              - `String fileId`

              - `JsonValue; type "code_execution_output"constant`

                - `CODE_EXECUTION_OUTPUT("code_execution_output")`

            - `String encryptedStdout`

            - `long returnCode`

            - `String stderr`

            - `JsonValue; type "encrypted_code_execution_result"constant`

              - `ENCRYPTED_CODE_EXECUTION_RESULT("encrypted_code_execution_result")`

        - `String toolUseId`

        - `JsonValue; type "code_execution_tool_result"constant`

          - `CODE_EXECUTION_TOOL_RESULT("code_execution_tool_result")`

      - `class BashCodeExecutionToolResultBlock:`

        - `Content content`

          - `class BashCodeExecutionToolResultError:`

            - `BashCodeExecutionToolResultErrorCode errorCode`

              - `INVALID_TOOL_INPUT("invalid_tool_input")`

              - `UNAVAILABLE("unavailable")`

              - `TOO_MANY_REQUESTS("too_many_requests")`

              - `EXECUTION_TIME_EXCEEDED("execution_time_exceeded")`

              - `OUTPUT_FILE_TOO_LARGE("output_file_too_large")`

            - `JsonValue; type "bash_code_execution_tool_result_error"constant`

              - `BASH_CODE_EXECUTION_TOOL_RESULT_ERROR("bash_code_execution_tool_result_error")`

          - `class BashCodeExecutionResultBlock:`

            - `List<BashCodeExecutionOutputBlock> content`

              - `String fileId`

              - `JsonValue; type "bash_code_execution_output"constant`

                - `BASH_CODE_EXECUTION_OUTPUT("bash_code_execution_output")`

            - `long returnCode`

            - `String stderr`

            - `String stdout`

            - `JsonValue; type "bash_code_execution_result"constant`

              - `BASH_CODE_EXECUTION_RESULT("bash_code_execution_result")`

        - `String toolUseId`

        - `JsonValue; type "bash_code_execution_tool_result"constant`

          - `BASH_CODE_EXECUTION_TOOL_RESULT("bash_code_execution_tool_result")`

      - `class TextEditorCodeExecutionToolResultBlock:`

        - `Content content`

          - `class TextEditorCodeExecutionToolResultError:`

            - `TextEditorCodeExecutionToolResultErrorCode errorCode`

              - `INVALID_TOOL_INPUT("invalid_tool_input")`

              - `UNAVAILABLE("unavailable")`

              - `TOO_MANY_REQUESTS("too_many_requests")`

              - `EXECUTION_TIME_EXCEEDED("execution_time_exceeded")`

              - `FILE_NOT_FOUND("file_not_found")`

            - `Optional<String> errorMessage`

            - `JsonValue; type "text_editor_code_execution_tool_result_error"constant`

              - `TEXT_EDITOR_CODE_EXECUTION_TOOL_RESULT_ERROR("text_editor_code_execution_tool_result_error")`

          - `class TextEditorCodeExecutionViewResultBlock:`

            - `String content`

            - `FileType fileType`

              - `TEXT("text")`

              - `IMAGE("image")`

              - `PDF("pdf")`

            - `Optional<Long> numLines`

            - `Optional<Long> startLine`

            - `Optional<Long> totalLines`

            - `JsonValue; type "text_editor_code_execution_view_result"constant`

              - `TEXT_EDITOR_CODE_EXECUTION_VIEW_RESULT("text_editor_code_execution_view_result")`

          - `class TextEditorCodeExecutionCreateResultBlock:`

            - `boolean isFileUpdate`

            - `JsonValue; type "text_editor_code_execution_create_result"constant`

              - `TEXT_EDITOR_CODE_EXECUTION_CREATE_RESULT("text_editor_code_execution_create_result")`

          - `class TextEditorCodeExecutionStrReplaceResultBlock:`

            - `Optional<List<String>> lines`

            - `Optional<Long> newLines`

            - `Optional<Long> newStart`

            - `Optional<Long> oldLines`

            - `Optional<Long> oldStart`

            - `JsonValue; type "text_editor_code_execution_str_replace_result"constant`

              - `TEXT_EDITOR_CODE_EXECUTION_STR_REPLACE_RESULT("text_editor_code_execution_str_replace_result")`

        - `String toolUseId`

        - `JsonValue; type "text_editor_code_execution_tool_result"constant`

          - `TEXT_EDITOR_CODE_EXECUTION_TOOL_RESULT("text_editor_code_execution_tool_result")`

      - `class ToolSearchToolResultBlock:`

        - `Content content`

          - `class ToolSearchToolResultError:`

            - `ToolSearchToolResultErrorCode errorCode`

              - `INVALID_TOOL_INPUT("invalid_tool_input")`

              - `UNAVAILABLE("unavailable")`

              - `TOO_MANY_REQUESTS("too_many_requests")`

              - `EXECUTION_TIME_EXCEEDED("execution_time_exceeded")`

            - `Optional<String> errorMessage`

            - `JsonValue; type "tool_search_tool_result_error"constant`

              - `TOOL_SEARCH_TOOL_RESULT_ERROR("tool_search_tool_result_error")`

          - `class ToolSearchToolSearchResultBlock:`

            - `List<ToolReferenceBlock> toolReferences`

              - `String toolName`

              - `JsonValue; type "tool_reference"constant`

                - `TOOL_REFERENCE("tool_reference")`

            - `JsonValue; type "tool_search_tool_search_result"constant`

              - `TOOL_SEARCH_TOOL_SEARCH_RESULT("tool_search_tool_search_result")`

        - `String toolUseId`

        - `JsonValue; type "tool_search_tool_result"constant`

          - `TOOL_SEARCH_TOOL_RESULT("tool_search_tool_result")`

      - `class ContainerUploadBlock:`

        Response model for a file uploaded to the container.

        - `String fileId`

        - `JsonValue; type "container_upload"constant`

          - `CONTAINER_UPLOAD("container_upload")`

    - `Model model`

      The model that will complete your prompt.

      See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

      - `CLAUDE_OPUS_4_6("claude-opus-4-6")`

        Most intelligent model for building agents and coding

      - `CLAUDE_SONNET_4_6("claude-sonnet-4-6")`

        Frontier intelligence at scale — built for coding, agents, and enterprise workflows

      - `CLAUDE_OPUS_4_5_20251101("claude-opus-4-5-20251101")`

        Premium model combining maximum intelligence with practical performance

      - `CLAUDE_OPUS_4_5("claude-opus-4-5")`

        Premium model combining maximum intelligence with practical performance

      - `CLAUDE_3_7_SONNET_LATEST("claude-3-7-sonnet-latest")`

        High-performance model with early extended thinking

      - `CLAUDE_3_7_SONNET_20250219("claude-3-7-sonnet-20250219")`

        High-performance model with early extended thinking

      - `CLAUDE_3_5_HAIKU_LATEST("claude-3-5-haiku-latest")`

        Fastest and most compact model for near-instant responsiveness

      - `CLAUDE_3_5_HAIKU_20241022("claude-3-5-haiku-20241022")`

        Our fastest model

      - `CLAUDE_HAIKU_4_5("claude-haiku-4-5")`

        Hybrid model, capable of near-instant responses and extended thinking

      - `CLAUDE_HAIKU_4_5_20251001("claude-haiku-4-5-20251001")`

        Hybrid model, capable of near-instant responses and extended thinking

      - `CLAUDE_SONNET_4_20250514("claude-sonnet-4-20250514")`

        High-performance model with extended thinking

      - `CLAUDE_SONNET_4_0("claude-sonnet-4-0")`

        High-performance model with extended thinking

      - `CLAUDE_4_SONNET_20250514("claude-4-sonnet-20250514")`

        High-performance model with extended thinking

      - `CLAUDE_SONNET_4_5("claude-sonnet-4-5")`

        Our best model for real-world agents and coding

      - `CLAUDE_SONNET_4_5_20250929("claude-sonnet-4-5-20250929")`

        Our best model for real-world agents and coding

      - `CLAUDE_OPUS_4_0("claude-opus-4-0")`

        Our most capable model

      - `CLAUDE_OPUS_4_20250514("claude-opus-4-20250514")`

        Our most capable model

      - `CLAUDE_4_OPUS_20250514("claude-4-opus-20250514")`

        Our most capable model

      - `CLAUDE_OPUS_4_1_20250805("claude-opus-4-1-20250805")`

        Our most capable model

      - `CLAUDE_3_OPUS_LATEST("claude-3-opus-latest")`

        Excels at writing and complex tasks

      - `CLAUDE_3_OPUS_20240229("claude-3-opus-20240229")`

        Excels at writing and complex tasks

      - `CLAUDE_3_HAIKU_20240307("claude-3-haiku-20240307")`

        Our previous most fast and cost-effective

    - `JsonValue; role "assistant"constant`

      Conversational role of the generated message.

      This will always be `"assistant"`.

      - `ASSISTANT("assistant")`

    - `Optional<StopReason> stopReason`

      The reason that we stopped.

      This may be one the following values:

      * `"end_turn"`: the model reached a natural stopping point
      * `"max_tokens"`: we exceeded the requested `max_tokens` or the model's maximum
      * `"stop_sequence"`: one of your provided custom `stop_sequences` was generated
      * `"tool_use"`: the model invoked one or more tools
      * `"pause_turn"`: we paused a long-running turn. You may provide the response back as-is in a subsequent request to let the model continue.
      * `"refusal"`: when streaming classifiers intervene to handle potential policy violations

      In non-streaming mode this value is always non-null. In streaming mode, it is null in the `message_start` event and non-null otherwise.

      - `END_TURN("end_turn")`

      - `MAX_TOKENS("max_tokens")`

      - `STOP_SEQUENCE("stop_sequence")`

      - `TOOL_USE("tool_use")`

      - `PAUSE_TURN("pause_turn")`

      - `REFUSAL("refusal")`

    - `Optional<String> stopSequence`

      Which custom stop sequence was generated, if any.

      This value will be a non-null string if one of your custom stop sequences was generated.

    - `JsonValue; type "message"constant`

      Object type.

      For Messages, this is always `"message"`.

      - `MESSAGE("message")`

    - `Usage usage`

      Billing and rate-limit usage.

      Anthropic's API bills and rate-limits by token counts, as tokens represent the underlying cost to our systems.

      Under the hood, the API transforms requests into a format suitable for the model. The model's output then goes through a parsing stage before becoming an API response. As a result, the token counts in `usage` will not match one-to-one with the exact visible content of an API request or response.

      For example, `output_tokens` will be non-zero, even for an empty string response from Claude.

      Total input tokens in a request is the summation of `input_tokens`, `cache_creation_input_tokens`, and `cache_read_input_tokens`.

      - `Optional<CacheCreation> cacheCreation`

        Breakdown of cached tokens by TTL

        - `long ephemeral1hInputTokens`

          The number of input tokens used to create the 1 hour cache entry.

        - `long ephemeral5mInputTokens`

          The number of input tokens used to create the 5 minute cache entry.

      - `Optional<Long> cacheCreationInputTokens`

        The number of input tokens used to create the cache entry.

      - `Optional<Long> cacheReadInputTokens`

        The number of input tokens read from the cache.

      - `Optional<String> inferenceGeo`

        The geographic region where inference was performed for this request.

      - `long inputTokens`

        The number of input tokens which were used.

      - `long outputTokens`

        The number of output tokens which were used.

      - `Optional<ServerToolUsage> serverToolUse`

        The number of server tool requests.

        - `long webFetchRequests`

          The number of web fetch tool requests.

        - `long webSearchRequests`

          The number of web search tool requests.

      - `Optional<ServiceTier> serviceTier`

        If the request used the priority, standard, or batch tier.

        - `STANDARD("standard")`

        - `PRIORITY("priority")`

        - `BATCH("batch")`

  - `JsonValue; type "message_start"constant`

    - `MESSAGE_START("message_start")`

### Raw Message Stop Event

- `class RawMessageStopEvent:`

  - `JsonValue; type "message_stop"constant`

    - `MESSAGE_STOP("message_stop")`

### Raw Message Stream Event

- `class RawMessageStreamEvent: A class that can be one of several variants.union`

  - `class RawMessageStartEvent:`

    - `Message message`

      - `String id`

        Unique object identifier.

        The format and length of IDs may change over time.

      - `Optional<Container> container`

        Information about the container used in the request (for the code execution tool)

        - `String id`

          Identifier for the container used in this request

        - `LocalDateTime expiresAt`

          The time at which the container will expire.

      - `List<ContentBlock> content`

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

        - `class TextBlock:`

          - `Optional<List<TextCitation>> citations`

            Citations supporting the text block.

            The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

            - `class CitationCharLocation:`

              - `String citedText`

              - `long documentIndex`

              - `Optional<String> documentTitle`

              - `long endCharIndex`

              - `Optional<String> fileId`

              - `long startCharIndex`

              - `JsonValue; type "char_location"constant`

                - `CHAR_LOCATION("char_location")`

            - `class CitationPageLocation:`

              - `String citedText`

              - `long documentIndex`

              - `Optional<String> documentTitle`

              - `long endPageNumber`

              - `Optional<String> fileId`

              - `long startPageNumber`

              - `JsonValue; type "page_location"constant`

                - `PAGE_LOCATION("page_location")`

            - `class CitationContentBlockLocation:`

              - `String citedText`

              - `long documentIndex`

              - `Optional<String> documentTitle`

              - `long endBlockIndex`

              - `Optional<String> fileId`

              - `long startBlockIndex`

              - `JsonValue; type "content_block_location"constant`

                - `CONTENT_BLOCK_LOCATION("content_block_location")`

            - `class CitationsWebSearchResultLocation:`

              - `String citedText`

              - `String encryptedIndex`

              - `Optional<String> title`

              - `JsonValue; type "web_search_result_location"constant`

                - `WEB_SEARCH_RESULT_LOCATION("web_search_result_location")`

              - `String url`

            - `class CitationsSearchResultLocation:`

              - `String citedText`

              - `long endBlockIndex`

              - `long searchResultIndex`

              - `String source`

              - `long startBlockIndex`

              - `Optional<String> title`

              - `JsonValue; type "search_result_location"constant`

                - `SEARCH_RESULT_LOCATION("search_result_location")`

          - `String text`

          - `JsonValue; type "text"constant`

            - `TEXT("text")`

        - `class ThinkingBlock:`

          - `String signature`

          - `String thinking`

          - `JsonValue; type "thinking"constant`

            - `THINKING("thinking")`

        - `class RedactedThinkingBlock:`

          - `String data`

          - `JsonValue; type "redacted_thinking"constant`

            - `REDACTED_THINKING("redacted_thinking")`

        - `class ToolUseBlock:`

          - `String id`

          - `Caller caller`

            Tool invocation directly from the model.

            - `class DirectCaller:`

              Tool invocation directly from the model.

              - `JsonValue; type "direct"constant`

                - `DIRECT("direct")`

            - `class ServerToolCaller:`

              Tool invocation generated by a server-side tool.

              - `String toolId`

              - `JsonValue; type "code_execution_20250825"constant`

                - `CODE_EXECUTION_20250825("code_execution_20250825")`

            - `class ServerToolCaller20260120:`

              - `String toolId`

              - `JsonValue; type "code_execution_20260120"constant`

                - `CODE_EXECUTION_20260120("code_execution_20260120")`

          - `Input input`

          - `String name`

          - `JsonValue; type "tool_use"constant`

            - `TOOL_USE("tool_use")`

        - `class ServerToolUseBlock:`

          - `String id`

          - `Caller caller`

            Tool invocation directly from the model.

            - `class DirectCaller:`

              Tool invocation directly from the model.

              - `JsonValue; type "direct"constant`

                - `DIRECT("direct")`

            - `class ServerToolCaller:`

              Tool invocation generated by a server-side tool.

              - `String toolId`

              - `JsonValue; type "code_execution_20250825"constant`

                - `CODE_EXECUTION_20250825("code_execution_20250825")`

            - `class ServerToolCaller20260120:`

              - `String toolId`

              - `JsonValue; type "code_execution_20260120"constant`

                - `CODE_EXECUTION_20260120("code_execution_20260120")`

          - `Input input`

          - `Name name`

            - `WEB_SEARCH("web_search")`

            - `WEB_FETCH("web_fetch")`

            - `CODE_EXECUTION("code_execution")`

            - `BASH_CODE_EXECUTION("bash_code_execution")`

            - `TEXT_EDITOR_CODE_EXECUTION("text_editor_code_execution")`

            - `TOOL_SEARCH_TOOL_REGEX("tool_search_tool_regex")`

            - `TOOL_SEARCH_TOOL_BM25("tool_search_tool_bm25")`

          - `JsonValue; type "server_tool_use"constant`

            - `SERVER_TOOL_USE("server_tool_use")`

        - `class WebSearchToolResultBlock:`

          - `Caller caller`

            Tool invocation directly from the model.

            - `class DirectCaller:`

              Tool invocation directly from the model.

              - `JsonValue; type "direct"constant`

                - `DIRECT("direct")`

            - `class ServerToolCaller:`

              Tool invocation generated by a server-side tool.

              - `String toolId`

              - `JsonValue; type "code_execution_20250825"constant`

                - `CODE_EXECUTION_20250825("code_execution_20250825")`

            - `class ServerToolCaller20260120:`

              - `String toolId`

              - `JsonValue; type "code_execution_20260120"constant`

                - `CODE_EXECUTION_20260120("code_execution_20260120")`

          - `WebSearchToolResultBlockContent content`

            - `class WebSearchToolResultError:`

              - `WebSearchToolResultErrorCode errorCode`

                - `INVALID_TOOL_INPUT("invalid_tool_input")`

                - `UNAVAILABLE("unavailable")`

                - `MAX_USES_EXCEEDED("max_uses_exceeded")`

                - `TOO_MANY_REQUESTS("too_many_requests")`

                - `QUERY_TOO_LONG("query_too_long")`

                - `REQUEST_TOO_LARGE("request_too_large")`

              - `JsonValue; type "web_search_tool_result_error"constant`

                - `WEB_SEARCH_TOOL_RESULT_ERROR("web_search_tool_result_error")`

            - `List<WebSearchResultBlock>`

              - `String encryptedContent`

              - `Optional<String> pageAge`

              - `String title`

              - `JsonValue; type "web_search_result"constant`

                - `WEB_SEARCH_RESULT("web_search_result")`

              - `String url`

          - `String toolUseId`

          - `JsonValue; type "web_search_tool_result"constant`

            - `WEB_SEARCH_TOOL_RESULT("web_search_tool_result")`

        - `class WebFetchToolResultBlock:`

          - `Caller caller`

            Tool invocation directly from the model.

            - `class DirectCaller:`

              Tool invocation directly from the model.

              - `JsonValue; type "direct"constant`

                - `DIRECT("direct")`

            - `class ServerToolCaller:`

              Tool invocation generated by a server-side tool.

              - `String toolId`

              - `JsonValue; type "code_execution_20250825"constant`

                - `CODE_EXECUTION_20250825("code_execution_20250825")`

            - `class ServerToolCaller20260120:`

              - `String toolId`

              - `JsonValue; type "code_execution_20260120"constant`

                - `CODE_EXECUTION_20260120("code_execution_20260120")`

          - `Content content`

            - `class WebFetchToolResultErrorBlock:`

              - `WebFetchToolResultErrorCode errorCode`

                - `INVALID_TOOL_INPUT("invalid_tool_input")`

                - `URL_TOO_LONG("url_too_long")`

                - `URL_NOT_ALLOWED("url_not_allowed")`

                - `URL_NOT_ACCESSIBLE("url_not_accessible")`

                - `UNSUPPORTED_CONTENT_TYPE("unsupported_content_type")`

                - `TOO_MANY_REQUESTS("too_many_requests")`

                - `MAX_USES_EXCEEDED("max_uses_exceeded")`

                - `UNAVAILABLE("unavailable")`

              - `JsonValue; type "web_fetch_tool_result_error"constant`

                - `WEB_FETCH_TOOL_RESULT_ERROR("web_fetch_tool_result_error")`

            - `class WebFetchBlock:`

              - `DocumentBlock content`

                - `Optional<CitationsConfig> citations`

                  Citation configuration for the document

                  - `boolean enabled`

                - `Source source`

                  - `class Base64PdfSource:`

                    - `String data`

                    - `JsonValue; mediaType "application/pdf"constant`

                      - `APPLICATION_PDF("application/pdf")`

                    - `JsonValue; type "base64"constant`

                      - `BASE64("base64")`

                  - `class PlainTextSource:`

                    - `String data`

                    - `JsonValue; mediaType "text/plain"constant`

                      - `TEXT_PLAIN("text/plain")`

                    - `JsonValue; type "text"constant`

                      - `TEXT("text")`

                - `Optional<String> title`

                  The title of the document

                - `JsonValue; type "document"constant`

                  - `DOCUMENT("document")`

              - `Optional<String> retrievedAt`

                ISO 8601 timestamp when the content was retrieved

              - `JsonValue; type "web_fetch_result"constant`

                - `WEB_FETCH_RESULT("web_fetch_result")`

              - `String url`

                Fetched content URL

          - `String toolUseId`

          - `JsonValue; type "web_fetch_tool_result"constant`

            - `WEB_FETCH_TOOL_RESULT("web_fetch_tool_result")`

        - `class CodeExecutionToolResultBlock:`

          - `CodeExecutionToolResultBlockContent content`

            Code execution result with encrypted stdout for PFC + web_search results.

            - `class CodeExecutionToolResultError:`

              - `CodeExecutionToolResultErrorCode errorCode`

                - `INVALID_TOOL_INPUT("invalid_tool_input")`

                - `UNAVAILABLE("unavailable")`

                - `TOO_MANY_REQUESTS("too_many_requests")`

                - `EXECUTION_TIME_EXCEEDED("execution_time_exceeded")`

              - `JsonValue; type "code_execution_tool_result_error"constant`

                - `CODE_EXECUTION_TOOL_RESULT_ERROR("code_execution_tool_result_error")`

            - `class CodeExecutionResultBlock:`

              - `List<CodeExecutionOutputBlock> content`

                - `String fileId`

                - `JsonValue; type "code_execution_output"constant`

                  - `CODE_EXECUTION_OUTPUT("code_execution_output")`

              - `long returnCode`

              - `String stderr`

              - `String stdout`

              - `JsonValue; type "code_execution_result"constant`

                - `CODE_EXECUTION_RESULT("code_execution_result")`

            - `class EncryptedCodeExecutionResultBlock:`

              Code execution result with encrypted stdout for PFC + web_search results.

              - `List<CodeExecutionOutputBlock> content`

                - `String fileId`

                - `JsonValue; type "code_execution_output"constant`

                  - `CODE_EXECUTION_OUTPUT("code_execution_output")`

              - `String encryptedStdout`

              - `long returnCode`

              - `String stderr`

              - `JsonValue; type "encrypted_code_execution_result"constant`

                - `ENCRYPTED_CODE_EXECUTION_RESULT("encrypted_code_execution_result")`

          - `String toolUseId`

          - `JsonValue; type "code_execution_tool_result"constant`

            - `CODE_EXECUTION_TOOL_RESULT("code_execution_tool_result")`

        - `class BashCodeExecutionToolResultBlock:`

          - `Content content`

            - `class BashCodeExecutionToolResultError:`

              - `BashCodeExecutionToolResultErrorCode errorCode`

                - `INVALID_TOOL_INPUT("invalid_tool_input")`

                - `UNAVAILABLE("unavailable")`

                - `TOO_MANY_REQUESTS("too_many_requests")`

                - `EXECUTION_TIME_EXCEEDED("execution_time_exceeded")`

                - `OUTPUT_FILE_TOO_LARGE("output_file_too_large")`

              - `JsonValue; type "bash_code_execution_tool_result_error"constant`

                - `BASH_CODE_EXECUTION_TOOL_RESULT_ERROR("bash_code_execution_tool_result_error")`

            - `class BashCodeExecutionResultBlock:`

              - `List<BashCodeExecutionOutputBlock> content`

                - `String fileId`

                - `JsonValue; type "bash_code_execution_output"constant`

                  - `BASH_CODE_EXECUTION_OUTPUT("bash_code_execution_output")`

              - `long returnCode`

              - `String stderr`

              - `String stdout`

              - `JsonValue; type "bash_code_execution_result"constant`

                - `BASH_CODE_EXECUTION_RESULT("bash_code_execution_result")`

          - `String toolUseId`

          - `JsonValue; type "bash_code_execution_tool_result"constant`

            - `BASH_CODE_EXECUTION_TOOL_RESULT("bash_code_execution_tool_result")`

        - `class TextEditorCodeExecutionToolResultBlock:`

          - `Content content`

            - `class TextEditorCodeExecutionToolResultError:`

              - `TextEditorCodeExecutionToolResultErrorCode errorCode`

                - `INVALID_TOOL_INPUT("invalid_tool_input")`

                - `UNAVAILABLE("unavailable")`

                - `TOO_MANY_REQUESTS("too_many_requests")`

                - `EXECUTION_TIME_EXCEEDED("execution_time_exceeded")`

                - `FILE_NOT_FOUND("file_not_found")`

              - `Optional<String> errorMessage`

              - `JsonValue; type "text_editor_code_execution_tool_result_error"constant`

                - `TEXT_EDITOR_CODE_EXECUTION_TOOL_RESULT_ERROR("text_editor_code_execution_tool_result_error")`

            - `class TextEditorCodeExecutionViewResultBlock:`

              - `String content`

              - `FileType fileType`

                - `TEXT("text")`

                - `IMAGE("image")`

                - `PDF("pdf")`

              - `Optional<Long> numLines`

              - `Optional<Long> startLine`

              - `Optional<Long> totalLines`

              - `JsonValue; type "text_editor_code_execution_view_result"constant`

                - `TEXT_EDITOR_CODE_EXECUTION_VIEW_RESULT("text_editor_code_execution_view_result")`

            - `class TextEditorCodeExecutionCreateResultBlock:`

              - `boolean isFileUpdate`

              - `JsonValue; type "text_editor_code_execution_create_result"constant`

                - `TEXT_EDITOR_CODE_EXECUTION_CREATE_RESULT("text_editor_code_execution_create_result")`

            - `class TextEditorCodeExecutionStrReplaceResultBlock:`

              - `Optional<List<String>> lines`

              - `Optional<Long> newLines`

              - `Optional<Long> newStart`

              - `Optional<Long> oldLines`

              - `Optional<Long> oldStart`

              - `JsonValue; type "text_editor_code_execution_str_replace_result"constant`

                - `TEXT_EDITOR_CODE_EXECUTION_STR_REPLACE_RESULT("text_editor_code_execution_str_replace_result")`

          - `String toolUseId`

          - `JsonValue; type "text_editor_code_execution_tool_result"constant`

            - `TEXT_EDITOR_CODE_EXECUTION_TOOL_RESULT("text_editor_code_execution_tool_result")`

        - `class ToolSearchToolResultBlock:`

          - `Content content`

            - `class ToolSearchToolResultError:`

              - `ToolSearchToolResultErrorCode errorCode`

                - `INVALID_TOOL_INPUT("invalid_tool_input")`

                - `UNAVAILABLE("unavailable")`

                - `TOO_MANY_REQUESTS("too_many_requests")`

                - `EXECUTION_TIME_EXCEEDED("execution_time_exceeded")`

              - `Optional<String> errorMessage`

              - `JsonValue; type "tool_search_tool_result_error"constant`

                - `TOOL_SEARCH_TOOL_RESULT_ERROR("tool_search_tool_result_error")`

            - `class ToolSearchToolSearchResultBlock:`

              - `List<ToolReferenceBlock> toolReferences`

                - `String toolName`

                - `JsonValue; type "tool_reference"constant`

                  - `TOOL_REFERENCE("tool_reference")`

              - `JsonValue; type "tool_search_tool_search_result"constant`

                - `TOOL_SEARCH_TOOL_SEARCH_RESULT("tool_search_tool_search_result")`

          - `String toolUseId`

          - `JsonValue; type "tool_search_tool_result"constant`

            - `TOOL_SEARCH_TOOL_RESULT("tool_search_tool_result")`

        - `class ContainerUploadBlock:`

          Response model for a file uploaded to the container.

          - `String fileId`

          - `JsonValue; type "container_upload"constant`

            - `CONTAINER_UPLOAD("container_upload")`

      - `Model model`

        The model that will complete your prompt.

        See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

        - `CLAUDE_OPUS_4_6("claude-opus-4-6")`

          Most intelligent model for building agents and coding

        - `CLAUDE_SONNET_4_6("claude-sonnet-4-6")`

          Frontier intelligence at scale — built for coding, agents, and enterprise workflows

        - `CLAUDE_OPUS_4_5_20251101("claude-opus-4-5-20251101")`

          Premium model combining maximum intelligence with practical performance

        - `CLAUDE_OPUS_4_5("claude-opus-4-5")`

          Premium model combining maximum intelligence with practical performance

        - `CLAUDE_3_7_SONNET_LATEST("claude-3-7-sonnet-latest")`

          High-performance model with early extended thinking

        - `CLAUDE_3_7_SONNET_20250219("claude-3-7-sonnet-20250219")`

          High-performance model with early extended thinking

        - `CLAUDE_3_5_HAIKU_LATEST("claude-3-5-haiku-latest")`

          Fastest and most compact model for near-instant responsiveness

        - `CLAUDE_3_5_HAIKU_20241022("claude-3-5-haiku-20241022")`

          Our fastest model

        - `CLAUDE_HAIKU_4_5("claude-haiku-4-5")`

          Hybrid model, capable of near-instant responses and extended thinking

        - `CLAUDE_HAIKU_4_5_20251001("claude-haiku-4-5-20251001")`

          Hybrid model, capable of near-instant responses and extended thinking

        - `CLAUDE_SONNET_4_20250514("claude-sonnet-4-20250514")`

          High-performance model with extended thinking

        - `CLAUDE_SONNET_4_0("claude-sonnet-4-0")`

          High-performance model with extended thinking

        - `CLAUDE_4_SONNET_20250514("claude-4-sonnet-20250514")`

          High-performance model with extended thinking

        - `CLAUDE_SONNET_4_5("claude-sonnet-4-5")`

          Our best model for real-world agents and coding

        - `CLAUDE_SONNET_4_5_20250929("claude-sonnet-4-5-20250929")`

          Our best model for real-world agents and coding

        - `CLAUDE_OPUS_4_0("claude-opus-4-0")`

          Our most capable model

        - `CLAUDE_OPUS_4_20250514("claude-opus-4-20250514")`

          Our most capable model

        - `CLAUDE_4_OPUS_20250514("claude-4-opus-20250514")`

          Our most capable model

        - `CLAUDE_OPUS_4_1_20250805("claude-opus-4-1-20250805")`

          Our most capable model

        - `CLAUDE_3_OPUS_LATEST("claude-3-opus-latest")`

          Excels at writing and complex tasks

        - `CLAUDE_3_OPUS_20240229("claude-3-opus-20240229")`

          Excels at writing and complex tasks

        - `CLAUDE_3_HAIKU_20240307("claude-3-haiku-20240307")`

          Our previous most fast and cost-effective

      - `JsonValue; role "assistant"constant`

        Conversational role of the generated message.

        This will always be `"assistant"`.

        - `ASSISTANT("assistant")`

      - `Optional<StopReason> stopReason`

        The reason that we stopped.

        This may be one the following values:

        * `"end_turn"`: the model reached a natural stopping point
        * `"max_tokens"`: we exceeded the requested `max_tokens` or the model's maximum
        * `"stop_sequence"`: one of your provided custom `stop_sequences` was generated
        * `"tool_use"`: the model invoked one or more tools
        * `"pause_turn"`: we paused a long-running turn. You may provide the response back as-is in a subsequent request to let the model continue.
        * `"refusal"`: when streaming classifiers intervene to handle potential policy violations

        In non-streaming mode this value is always non-null. In streaming mode, it is null in the `message_start` event and non-null otherwise.

        - `END_TURN("end_turn")`

        - `MAX_TOKENS("max_tokens")`

        - `STOP_SEQUENCE("stop_sequence")`

        - `TOOL_USE("tool_use")`

        - `PAUSE_TURN("pause_turn")`

        - `REFUSAL("refusal")`

      - `Optional<String> stopSequence`

        Which custom stop sequence was generated, if any.

        This value will be a non-null string if one of your custom stop sequences was generated.

      - `JsonValue; type "message"constant`

        Object type.

        For Messages, this is always `"message"`.

        - `MESSAGE("message")`

      - `Usage usage`

        Billing and rate-limit usage.

        Anthropic's API bills and rate-limits by token counts, as tokens represent the underlying cost to our systems.

        Under the hood, the API transforms requests into a format suitable for the model. The model's output then goes through a parsing stage before becoming an API response. As a result, the token counts in `usage` will not match one-to-one with the exact visible content of an API request or response.

        For example, `output_tokens` will be non-zero, even for an empty string response from Claude.

        Total input tokens in a request is the summation of `input_tokens`, `cache_creation_input_tokens`, and `cache_read_input_tokens`.

        - `Optional<CacheCreation> cacheCreation`

          Breakdown of cached tokens by TTL

          - `long ephemeral1hInputTokens`

            The number of input tokens used to create the 1 hour cache entry.

          - `long ephemeral5mInputTokens`

            The number of input tokens used to create the 5 minute cache entry.

        - `Optional<Long> cacheCreationInputTokens`

          The number of input tokens used to create the cache entry.

        - `Optional<Long> cacheReadInputTokens`

          The number of input tokens read from the cache.

        - `Optional<String> inferenceGeo`

          The geographic region where inference was performed for this request.

        - `long inputTokens`

          The number of input tokens which were used.

        - `long outputTokens`

          The number of output tokens which were used.

        - `Optional<ServerToolUsage> serverToolUse`

          The number of server tool requests.

          - `long webFetchRequests`

            The number of web fetch tool requests.

          - `long webSearchRequests`

            The number of web search tool requests.

        - `Optional<ServiceTier> serviceTier`

          If the request used the priority, standard, or batch tier.

          - `STANDARD("standard")`

          - `PRIORITY("priority")`

          - `BATCH("batch")`

    - `JsonValue; type "message_start"constant`

      - `MESSAGE_START("message_start")`

  - `class RawMessageDeltaEvent:`

    - `Delta delta`

      - `Optional<Container> container`

        Information about the container used in the request (for the code execution tool)

        - `String id`

          Identifier for the container used in this request

        - `LocalDateTime expiresAt`

          The time at which the container will expire.

      - `Optional<StopReason> stopReason`

        - `END_TURN("end_turn")`

        - `MAX_TOKENS("max_tokens")`

        - `STOP_SEQUENCE("stop_sequence")`

        - `TOOL_USE("tool_use")`

        - `PAUSE_TURN("pause_turn")`

        - `REFUSAL("refusal")`

      - `Optional<String> stopSequence`

    - `JsonValue; type "message_delta"constant`

      - `MESSAGE_DELTA("message_delta")`

    - `MessageDeltaUsage usage`

      Billing and rate-limit usage.

      Anthropic's API bills and rate-limits by token counts, as tokens represent the underlying cost to our systems.

      Under the hood, the API transforms requests into a format suitable for the model. The model's output then goes through a parsing stage before becoming an API response. As a result, the token counts in `usage` will not match one-to-one with the exact visible content of an API request or response.

      For example, `output_tokens` will be non-zero, even for an empty string response from Claude.

      Total input tokens in a request is the summation of `input_tokens`, `cache_creation_input_tokens`, and `cache_read_input_tokens`.

      - `Optional<Long> cacheCreationInputTokens`

        The cumulative number of input tokens used to create the cache entry.

      - `Optional<Long> cacheReadInputTokens`

        The cumulative number of input tokens read from the cache.

      - `Optional<Long> inputTokens`

        The cumulative number of input tokens which were used.

      - `long outputTokens`

        The cumulative number of output tokens which were used.

      - `Optional<ServerToolUsage> serverToolUse`

        The number of server tool requests.

        - `long webFetchRequests`

          The number of web fetch tool requests.

        - `long webSearchRequests`

          The number of web search tool requests.

  - `class RawMessageStopEvent:`

    - `JsonValue; type "message_stop"constant`

      - `MESSAGE_STOP("message_stop")`

  - `class RawContentBlockStartEvent:`

    - `ContentBlock contentBlock`

      Response model for a file uploaded to the container.

      - `class TextBlock:`

        - `Optional<List<TextCitation>> citations`

          Citations supporting the text block.

          The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

          - `class CitationCharLocation:`

            - `String citedText`

            - `long documentIndex`

            - `Optional<String> documentTitle`

            - `long endCharIndex`

            - `Optional<String> fileId`

            - `long startCharIndex`

            - `JsonValue; type "char_location"constant`

              - `CHAR_LOCATION("char_location")`

          - `class CitationPageLocation:`

            - `String citedText`

            - `long documentIndex`

            - `Optional<String> documentTitle`

            - `long endPageNumber`

            - `Optional<String> fileId`

            - `long startPageNumber`

            - `JsonValue; type "page_location"constant`

              - `PAGE_LOCATION("page_location")`

          - `class CitationContentBlockLocation:`

            - `String citedText`

            - `long documentIndex`

            - `Optional<String> documentTitle`

            - `long endBlockIndex`

            - `Optional<String> fileId`

            - `long startBlockIndex`

            - `JsonValue; type "content_block_location"constant`

              - `CONTENT_BLOCK_LOCATION("content_block_location")`

          - `class CitationsWebSearchResultLocation:`

            - `String citedText`

            - `String encryptedIndex`

            - `Optional<String> title`

            - `JsonValue; type "web_search_result_location"constant`

              - `WEB_SEARCH_RESULT_LOCATION("web_search_result_location")`

            - `String url`

          - `class CitationsSearchResultLocation:`

            - `String citedText`

            - `long endBlockIndex`

            - `long searchResultIndex`

            - `String source`

            - `long startBlockIndex`

            - `Optional<String> title`

            - `JsonValue; type "search_result_location"constant`

              - `SEARCH_RESULT_LOCATION("search_result_location")`

        - `String text`

        - `JsonValue; type "text"constant`

          - `TEXT("text")`

      - `class ThinkingBlock:`

        - `String signature`

        - `String thinking`

        - `JsonValue; type "thinking"constant`

          - `THINKING("thinking")`

      - `class RedactedThinkingBlock:`

        - `String data`

        - `JsonValue; type "redacted_thinking"constant`

          - `REDACTED_THINKING("redacted_thinking")`

      - `class ToolUseBlock:`

        - `String id`

        - `Caller caller`

          Tool invocation directly from the model.

          - `class DirectCaller:`

            Tool invocation directly from the model.

            - `JsonValue; type "direct"constant`

              - `DIRECT("direct")`

          - `class ServerToolCaller:`

            Tool invocation generated by a server-side tool.

            - `String toolId`

            - `JsonValue; type "code_execution_20250825"constant`

              - `CODE_EXECUTION_20250825("code_execution_20250825")`

          - `class ServerToolCaller20260120:`

            - `String toolId`

            - `JsonValue; type "code_execution_20260120"constant`

              - `CODE_EXECUTION_20260120("code_execution_20260120")`

        - `Input input`

        - `String name`

        - `JsonValue; type "tool_use"constant`

          - `TOOL_USE("tool_use")`

      - `class ServerToolUseBlock:`

        - `String id`

        - `Caller caller`

          Tool invocation directly from the model.

          - `class DirectCaller:`

            Tool invocation directly from the model.

            - `JsonValue; type "direct"constant`

              - `DIRECT("direct")`

          - `class ServerToolCaller:`

            Tool invocation generated by a server-side tool.

            - `String toolId`

            - `JsonValue; type "code_execution_20250825"constant`

              - `CODE_EXECUTION_20250825("code_execution_20250825")`

          - `class ServerToolCaller20260120:`

            - `String toolId`

            - `JsonValue; type "code_execution_20260120"constant`

              - `CODE_EXECUTION_20260120("code_execution_20260120")`

        - `Input input`

        - `Name name`

          - `WEB_SEARCH("web_search")`

          - `WEB_FETCH("web_fetch")`

          - `CODE_EXECUTION("code_execution")`

          - `BASH_CODE_EXECUTION("bash_code_execution")`

          - `TEXT_EDITOR_CODE_EXECUTION("text_editor_code_execution")`

          - `TOOL_SEARCH_TOOL_REGEX("tool_search_tool_regex")`

          - `TOOL_SEARCH_TOOL_BM25("tool_search_tool_bm25")`

        - `JsonValue; type "server_tool_use"constant`

          - `SERVER_TOOL_USE("server_tool_use")`

      - `class WebSearchToolResultBlock:`

        - `Caller caller`

          Tool invocation directly from the model.

          - `class DirectCaller:`

            Tool invocation directly from the model.

            - `JsonValue; type "direct"constant`

              - `DIRECT("direct")`

          - `class ServerToolCaller:`

            Tool invocation generated by a server-side tool.

            - `String toolId`

            - `JsonValue; type "code_execution_20250825"constant`

              - `CODE_EXECUTION_20250825("code_execution_20250825")`

          - `class ServerToolCaller20260120:`

            - `String toolId`

            - `JsonValue; type "code_execution_20260120"constant`

              - `CODE_EXECUTION_20260120("code_execution_20260120")`

        - `WebSearchToolResultBlockContent content`

          - `class WebSearchToolResultError:`

            - `WebSearchToolResultErrorCode errorCode`

              - `INVALID_TOOL_INPUT("invalid_tool_input")`

              - `UNAVAILABLE("unavailable")`

              - `MAX_USES_EXCEEDED("max_uses_exceeded")`

              - `TOO_MANY_REQUESTS("too_many_requests")`

              - `QUERY_TOO_LONG("query_too_long")`

              - `REQUEST_TOO_LARGE("request_too_large")`

            - `JsonValue; type "web_search_tool_result_error"constant`

              - `WEB_SEARCH_TOOL_RESULT_ERROR("web_search_tool_result_error")`

          - `List<WebSearchResultBlock>`

            - `String encryptedContent`

            - `Optional<String> pageAge`

            - `String title`

            - `JsonValue; type "web_search_result"constant`

              - `WEB_SEARCH_RESULT("web_search_result")`

            - `String url`

        - `String toolUseId`

        - `JsonValue; type "web_search_tool_result"constant`

          - `WEB_SEARCH_TOOL_RESULT("web_search_tool_result")`

      - `class WebFetchToolResultBlock:`

        - `Caller caller`

          Tool invocation directly from the model.

          - `class DirectCaller:`

            Tool invocation directly from the model.

            - `JsonValue; type "direct"constant`

              - `DIRECT("direct")`

          - `class ServerToolCaller:`

            Tool invocation generated by a server-side tool.

            - `String toolId`

            - `JsonValue; type "code_execution_20250825"constant`

              - `CODE_EXECUTION_20250825("code_execution_20250825")`

          - `class ServerToolCaller20260120:`

            - `String toolId`

            - `JsonValue; type "code_execution_20260120"constant`

              - `CODE_EXECUTION_20260120("code_execution_20260120")`

        - `Content content`

          - `class WebFetchToolResultErrorBlock:`

            - `WebFetchToolResultErrorCode errorCode`

              - `INVALID_TOOL_INPUT("invalid_tool_input")`

              - `URL_TOO_LONG("url_too_long")`

              - `URL_NOT_ALLOWED("url_not_allowed")`

              - `URL_NOT_ACCESSIBLE("url_not_accessible")`

              - `UNSUPPORTED_CONTENT_TYPE("unsupported_content_type")`

              - `TOO_MANY_REQUESTS("too_many_requests")`

              - `MAX_USES_EXCEEDED("max_uses_exceeded")`

              - `UNAVAILABLE("unavailable")`

            - `JsonValue; type "web_fetch_tool_result_error"constant`

              - `WEB_FETCH_TOOL_RESULT_ERROR("web_fetch_tool_result_error")`

          - `class WebFetchBlock:`

            - `DocumentBlock content`

              - `Optional<CitationsConfig> citations`

                Citation configuration for the document

                - `boolean enabled`

              - `Source source`

                - `class Base64PdfSource:`

                  - `String data`

                  - `JsonValue; mediaType "application/pdf"constant`

                    - `APPLICATION_PDF("application/pdf")`

                  - `JsonValue; type "base64"constant`

                    - `BASE64("base64")`

                - `class PlainTextSource:`

                  - `String data`

                  - `JsonValue; mediaType "text/plain"constant`

                    - `TEXT_PLAIN("text/plain")`

                  - `JsonValue; type "text"constant`

                    - `TEXT("text")`

              - `Optional<String> title`

                The title of the document

              - `JsonValue; type "document"constant`

                - `DOCUMENT("document")`

            - `Optional<String> retrievedAt`

              ISO 8601 timestamp when the content was retrieved

            - `JsonValue; type "web_fetch_result"constant`

              - `WEB_FETCH_RESULT("web_fetch_result")`

            - `String url`

              Fetched content URL

        - `String toolUseId`

        - `JsonValue; type "web_fetch_tool_result"constant`

          - `WEB_FETCH_TOOL_RESULT("web_fetch_tool_result")`

      - `class CodeExecutionToolResultBlock:`

        - `CodeExecutionToolResultBlockContent content`

          Code execution result with encrypted stdout for PFC + web_search results.

          - `class CodeExecutionToolResultError:`

            - `CodeExecutionToolResultErrorCode errorCode`

              - `INVALID_TOOL_INPUT("invalid_tool_input")`

              - `UNAVAILABLE("unavailable")`

              - `TOO_MANY_REQUESTS("too_many_requests")`

              - `EXECUTION_TIME_EXCEEDED("execution_time_exceeded")`

            - `JsonValue; type "code_execution_tool_result_error"constant`

              - `CODE_EXECUTION_TOOL_RESULT_ERROR("code_execution_tool_result_error")`

          - `class CodeExecutionResultBlock:`

            - `List<CodeExecutionOutputBlock> content`

              - `String fileId`

              - `JsonValue; type "code_execution_output"constant`

                - `CODE_EXECUTION_OUTPUT("code_execution_output")`

            - `long returnCode`

            - `String stderr`

            - `String stdout`

            - `JsonValue; type "code_execution_result"constant`

              - `CODE_EXECUTION_RESULT("code_execution_result")`

          - `class EncryptedCodeExecutionResultBlock:`

            Code execution result with encrypted stdout for PFC + web_search results.

            - `List<CodeExecutionOutputBlock> content`

              - `String fileId`

              - `JsonValue; type "code_execution_output"constant`

                - `CODE_EXECUTION_OUTPUT("code_execution_output")`

            - `String encryptedStdout`

            - `long returnCode`

            - `String stderr`

            - `JsonValue; type "encrypted_code_execution_result"constant`

              - `ENCRYPTED_CODE_EXECUTION_RESULT("encrypted_code_execution_result")`

        - `String toolUseId`

        - `JsonValue; type "code_execution_tool_result"constant`

          - `CODE_EXECUTION_TOOL_RESULT("code_execution_tool_result")`

      - `class BashCodeExecutionToolResultBlock:`

        - `Content content`

          - `class BashCodeExecutionToolResultError:`

            - `BashCodeExecutionToolResultErrorCode errorCode`

              - `INVALID_TOOL_INPUT("invalid_tool_input")`

              - `UNAVAILABLE("unavailable")`

              - `TOO_MANY_REQUESTS("too_many_requests")`

              - `EXECUTION_TIME_EXCEEDED("execution_time_exceeded")`

              - `OUTPUT_FILE_TOO_LARGE("output_file_too_large")`

            - `JsonValue; type "bash_code_execution_tool_result_error"constant`

              - `BASH_CODE_EXECUTION_TOOL_RESULT_ERROR("bash_code_execution_tool_result_error")`

          - `class BashCodeExecutionResultBlock:`

            - `List<BashCodeExecutionOutputBlock> content`

              - `String fileId`

              - `JsonValue; type "bash_code_execution_output"constant`

                - `BASH_CODE_EXECUTION_OUTPUT("bash_code_execution_output")`

            - `long returnCode`

            - `String stderr`

            - `String stdout`

            - `JsonValue; type "bash_code_execution_result"constant`

              - `BASH_CODE_EXECUTION_RESULT("bash_code_execution_result")`

        - `String toolUseId`

        - `JsonValue; type "bash_code_execution_tool_result"constant`

          - `BASH_CODE_EXECUTION_TOOL_RESULT("bash_code_execution_tool_result")`

      - `class TextEditorCodeExecutionToolResultBlock:`

        - `Content content`

          - `class TextEditorCodeExecutionToolResultError:`

            - `TextEditorCodeExecutionToolResultErrorCode errorCode`

              - `INVALID_TOOL_INPUT("invalid_tool_input")`

              - `UNAVAILABLE("unavailable")`

              - `TOO_MANY_REQUESTS("too_many_requests")`

              - `EXECUTION_TIME_EXCEEDED("execution_time_exceeded")`

              - `FILE_NOT_FOUND("file_not_found")`

            - `Optional<String> errorMessage`

            - `JsonValue; type "text_editor_code_execution_tool_result_error"constant`

              - `TEXT_EDITOR_CODE_EXECUTION_TOOL_RESULT_ERROR("text_editor_code_execution_tool_result_error")`

          - `class TextEditorCodeExecutionViewResultBlock:`

            - `String content`

            - `FileType fileType`

              - `TEXT("text")`

              - `IMAGE("image")`

              - `PDF("pdf")`

            - `Optional<Long> numLines`

            - `Optional<Long> startLine`

            - `Optional<Long> totalLines`

            - `JsonValue; type "text_editor_code_execution_view_result"constant`

              - `TEXT_EDITOR_CODE_EXECUTION_VIEW_RESULT("text_editor_code_execution_view_result")`

          - `class TextEditorCodeExecutionCreateResultBlock:`

            - `boolean isFileUpdate`

            - `JsonValue; type "text_editor_code_execution_create_result"constant`

              - `TEXT_EDITOR_CODE_EXECUTION_CREATE_RESULT("text_editor_code_execution_create_result")`

          - `class TextEditorCodeExecutionStrReplaceResultBlock:`

            - `Optional<List<String>> lines`

            - `Optional<Long> newLines`

            - `Optional<Long> newStart`

            - `Optional<Long> oldLines`

            - `Optional<Long> oldStart`

            - `JsonValue; type "text_editor_code_execution_str_replace_result"constant`

              - `TEXT_EDITOR_CODE_EXECUTION_STR_REPLACE_RESULT("text_editor_code_execution_str_replace_result")`

        - `String toolUseId`

        - `JsonValue; type "text_editor_code_execution_tool_result"constant`

          - `TEXT_EDITOR_CODE_EXECUTION_TOOL_RESULT("text_editor_code_execution_tool_result")`

      - `class ToolSearchToolResultBlock:`

        - `Content content`

          - `class ToolSearchToolResultError:`

            - `ToolSearchToolResultErrorCode errorCode`

              - `INVALID_TOOL_INPUT("invalid_tool_input")`

              - `UNAVAILABLE("unavailable")`

              - `TOO_MANY_REQUESTS("too_many_requests")`

              - `EXECUTION_TIME_EXCEEDED("execution_time_exceeded")`

            - `Optional<String> errorMessage`

            - `JsonValue; type "tool_search_tool_result_error"constant`

              - `TOOL_SEARCH_TOOL_RESULT_ERROR("tool_search_tool_result_error")`

          - `class ToolSearchToolSearchResultBlock:`

            - `List<ToolReferenceBlock> toolReferences`

              - `String toolName`

              - `JsonValue; type "tool_reference"constant`

                - `TOOL_REFERENCE("tool_reference")`

            - `JsonValue; type "tool_search_tool_search_result"constant`

              - `TOOL_SEARCH_TOOL_SEARCH_RESULT("tool_search_tool_search_result")`

        - `String toolUseId`

        - `JsonValue; type "tool_search_tool_result"constant`

          - `TOOL_SEARCH_TOOL_RESULT("tool_search_tool_result")`

      - `class ContainerUploadBlock:`

        Response model for a file uploaded to the container.

        - `String fileId`

        - `JsonValue; type "container_upload"constant`

          - `CONTAINER_UPLOAD("container_upload")`

    - `long index`

    - `JsonValue; type "content_block_start"constant`

      - `CONTENT_BLOCK_START("content_block_start")`

  - `class RawContentBlockDeltaEvent:`

    - `RawContentBlockDelta delta`

      - `class TextDelta:`

        - `String text`

        - `JsonValue; type "text_delta"constant`

          - `TEXT_DELTA("text_delta")`

      - `class InputJsonDelta:`

        - `String partialJson`

        - `JsonValue; type "input_json_delta"constant`

          - `INPUT_JSON_DELTA("input_json_delta")`

      - `class CitationsDelta:`

        - `Citation citation`

          - `class CitationCharLocation:`

            - `String citedText`

            - `long documentIndex`

            - `Optional<String> documentTitle`

            - `long endCharIndex`

            - `Optional<String> fileId`

            - `long startCharIndex`

            - `JsonValue; type "char_location"constant`

              - `CHAR_LOCATION("char_location")`

          - `class CitationPageLocation:`

            - `String citedText`

            - `long documentIndex`

            - `Optional<String> documentTitle`

            - `long endPageNumber`

            - `Optional<String> fileId`

            - `long startPageNumber`

            - `JsonValue; type "page_location"constant`

              - `PAGE_LOCATION("page_location")`

          - `class CitationContentBlockLocation:`

            - `String citedText`

            - `long documentIndex`

            - `Optional<String> documentTitle`

            - `long endBlockIndex`

            - `Optional<String> fileId`

            - `long startBlockIndex`

            - `JsonValue; type "content_block_location"constant`

              - `CONTENT_BLOCK_LOCATION("content_block_location")`

          - `class CitationsWebSearchResultLocation:`

            - `String citedText`

            - `String encryptedIndex`

            - `Optional<String> title`

            - `JsonValue; type "web_search_result_location"constant`

              - `WEB_SEARCH_RESULT_LOCATION("web_search_result_location")`

            - `String url`

          - `class CitationsSearchResultLocation:`

            - `String citedText`

            - `long endBlockIndex`

            - `long searchResultIndex`

            - `String source`

            - `long startBlockIndex`

            - `Optional<String> title`

            - `JsonValue; type "search_result_location"constant`

              - `SEARCH_RESULT_LOCATION("search_result_location")`

        - `JsonValue; type "citations_delta"constant`

          - `CITATIONS_DELTA("citations_delta")`

      - `class ThinkingDelta:`

        - `String thinking`

        - `JsonValue; type "thinking_delta"constant`

          - `THINKING_DELTA("thinking_delta")`

      - `class SignatureDelta:`

        - `String signature`

        - `JsonValue; type "signature_delta"constant`

          - `SIGNATURE_DELTA("signature_delta")`

    - `long index`

    - `JsonValue; type "content_block_delta"constant`

      - `CONTENT_BLOCK_DELTA("content_block_delta")`

  - `class RawContentBlockStopEvent:`

    - `long index`

    - `JsonValue; type "content_block_stop"constant`

      - `CONTENT_BLOCK_STOP("content_block_stop")`

### Redacted Thinking Block

- `class RedactedThinkingBlock:`

  - `String data`

  - `JsonValue; type "redacted_thinking"constant`

    - `REDACTED_THINKING("redacted_thinking")`

### Redacted Thinking Block Param

- `class RedactedThinkingBlockParam:`

  - `String data`

  - `JsonValue; type "redacted_thinking"constant`

    - `REDACTED_THINKING("redacted_thinking")`

### Search Result Block Param

- `class SearchResultBlockParam:`

  - `List<TextBlockParam> content`

    - `String text`

    - `JsonValue; type "text"constant`

      - `TEXT("text")`

    - `Optional<CacheControlEphemeral> cacheControl`

      Create a cache control breakpoint at this content block.

      - `JsonValue; type "ephemeral"constant`

        - `EPHEMERAL("ephemeral")`

      - `Optional<Ttl> ttl`

        The time-to-live for the cache control breakpoint.

        This may be one the following values:

        - `5m`: 5 minutes
        - `1h`: 1 hour

        Defaults to `5m`.

        - `TTL_5M("5m")`

        - `TTL_1H("1h")`

    - `Optional<List<TextCitationParam>> citations`

      - `class CitationCharLocationParam:`

        - `String citedText`

        - `long documentIndex`

        - `Optional<String> documentTitle`

        - `long endCharIndex`

        - `long startCharIndex`

        - `JsonValue; type "char_location"constant`

          - `CHAR_LOCATION("char_location")`

      - `class CitationPageLocationParam:`

        - `String citedText`

        - `long documentIndex`

        - `Optional<String> documentTitle`

        - `long endPageNumber`

        - `long startPageNumber`

        - `JsonValue; type "page_location"constant`

          - `PAGE_LOCATION("page_location")`

      - `class CitationContentBlockLocationParam:`

        - `String citedText`

        - `long documentIndex`

        - `Optional<String> documentTitle`

        - `long endBlockIndex`

        - `long startBlockIndex`

        - `JsonValue; type "content_block_location"constant`

          - `CONTENT_BLOCK_LOCATION("content_block_location")`

      - `class CitationWebSearchResultLocationParam:`

        - `String citedText`

        - `String encryptedIndex`

        - `Optional<String> title`

        - `JsonValue; type "web_search_result_location"constant`

          - `WEB_SEARCH_RESULT_LOCATION("web_search_result_location")`

        - `String url`

      - `class CitationSearchResultLocationParam:`

        - `String citedText`

        - `long endBlockIndex`

        - `long searchResultIndex`

        - `String source`

        - `long startBlockIndex`

        - `Optional<String> title`

        - `JsonValue; type "search_result_location"constant`

          - `SEARCH_RESULT_LOCATION("search_result_location")`

  - `String source`

  - `String title`

  - `JsonValue; type "search_result"constant`

    - `SEARCH_RESULT("search_result")`

  - `Optional<CacheControlEphemeral> cacheControl`

    Create a cache control breakpoint at this content block.

    - `JsonValue; type "ephemeral"constant`

      - `EPHEMERAL("ephemeral")`

    - `Optional<Ttl> ttl`

      The time-to-live for the cache control breakpoint.

      This may be one the following values:

      - `5m`: 5 minutes
      - `1h`: 1 hour

      Defaults to `5m`.

      - `TTL_5M("5m")`

      - `TTL_1H("1h")`

  - `Optional<CitationsConfigParam> citations`

    - `Optional<Boolean> enabled`

### Server Tool Caller

- `class ServerToolCaller:`

  Tool invocation generated by a server-side tool.

  - `String toolId`

  - `JsonValue; type "code_execution_20250825"constant`

    - `CODE_EXECUTION_20250825("code_execution_20250825")`

### Server Tool Caller 20260120

- `class ServerToolCaller20260120:`

  - `String toolId`

  - `JsonValue; type "code_execution_20260120"constant`

    - `CODE_EXECUTION_20260120("code_execution_20260120")`

### Server Tool Usage

- `class ServerToolUsage:`

  - `long webFetchRequests`

    The number of web fetch tool requests.

  - `long webSearchRequests`

    The number of web search tool requests.

### Server Tool Use Block

- `class ServerToolUseBlock:`

  - `String id`

  - `Caller caller`

    Tool invocation directly from the model.

    - `class DirectCaller:`

      Tool invocation directly from the model.

      - `JsonValue; type "direct"constant`

        - `DIRECT("direct")`

    - `class ServerToolCaller:`

      Tool invocation generated by a server-side tool.

      - `String toolId`

      - `JsonValue; type "code_execution_20250825"constant`

        - `CODE_EXECUTION_20250825("code_execution_20250825")`

    - `class ServerToolCaller20260120:`

      - `String toolId`

      - `JsonValue; type "code_execution_20260120"constant`

        - `CODE_EXECUTION_20260120("code_execution_20260120")`

  - `Input input`

  - `Name name`

    - `WEB_SEARCH("web_search")`

    - `WEB_FETCH("web_fetch")`

    - `CODE_EXECUTION("code_execution")`

    - `BASH_CODE_EXECUTION("bash_code_execution")`

    - `TEXT_EDITOR_CODE_EXECUTION("text_editor_code_execution")`

    - `TOOL_SEARCH_TOOL_REGEX("tool_search_tool_regex")`

    - `TOOL_SEARCH_TOOL_BM25("tool_search_tool_bm25")`

  - `JsonValue; type "server_tool_use"constant`

    - `SERVER_TOOL_USE("server_tool_use")`

### Server Tool Use Block Param

- `class ServerToolUseBlockParam:`

  - `String id`

  - `Input input`

  - `Name name`

    - `WEB_SEARCH("web_search")`

    - `WEB_FETCH("web_fetch")`

    - `CODE_EXECUTION("code_execution")`

    - `BASH_CODE_EXECUTION("bash_code_execution")`

    - `TEXT_EDITOR_CODE_EXECUTION("text_editor_code_execution")`

    - `TOOL_SEARCH_TOOL_REGEX("tool_search_tool_regex")`

    - `TOOL_SEARCH_TOOL_BM25("tool_search_tool_bm25")`

  - `JsonValue; type "server_tool_use"constant`

    - `SERVER_TOOL_USE("server_tool_use")`

  - `Optional<CacheControlEphemeral> cacheControl`

    Create a cache control breakpoint at this content block.

    - `JsonValue; type "ephemeral"constant`

      - `EPHEMERAL("ephemeral")`

    - `Optional<Ttl> ttl`

      The time-to-live for the cache control breakpoint.

      This may be one the following values:

      - `5m`: 5 minutes
      - `1h`: 1 hour

      Defaults to `5m`.

      - `TTL_5M("5m")`

      - `TTL_1H("1h")`

  - `Optional<Caller> caller`

    Tool invocation directly from the model.

    - `class DirectCaller:`

      Tool invocation directly from the model.

      - `JsonValue; type "direct"constant`

        - `DIRECT("direct")`

    - `class ServerToolCaller:`

      Tool invocation generated by a server-side tool.

      - `String toolId`

      - `JsonValue; type "code_execution_20250825"constant`

        - `CODE_EXECUTION_20250825("code_execution_20250825")`

    - `class ServerToolCaller20260120:`

      - `String toolId`

      - `JsonValue; type "code_execution_20260120"constant`

        - `CODE_EXECUTION_20260120("code_execution_20260120")`

### Signature Delta

- `class SignatureDelta:`

  - `String signature`

  - `JsonValue; type "signature_delta"constant`

    - `SIGNATURE_DELTA("signature_delta")`

### Stop Reason

- `enum StopReason:`

  - `END_TURN("end_turn")`

  - `MAX_TOKENS("max_tokens")`

  - `STOP_SEQUENCE("stop_sequence")`

  - `TOOL_USE("tool_use")`

  - `PAUSE_TURN("pause_turn")`

  - `REFUSAL("refusal")`

### Text Block

- `class TextBlock:`

  - `Optional<List<TextCitation>> citations`

    Citations supporting the text block.

    The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

    - `class CitationCharLocation:`

      - `String citedText`

      - `long documentIndex`

      - `Optional<String> documentTitle`

      - `long endCharIndex`

      - `Optional<String> fileId`

      - `long startCharIndex`

      - `JsonValue; type "char_location"constant`

        - `CHAR_LOCATION("char_location")`

    - `class CitationPageLocation:`

      - `String citedText`

      - `long documentIndex`

      - `Optional<String> documentTitle`

      - `long endPageNumber`

      - `Optional<String> fileId`

      - `long startPageNumber`

      - `JsonValue; type "page_location"constant`

        - `PAGE_LOCATION("page_location")`

    - `class CitationContentBlockLocation:`

      - `String citedText`

      - `long documentIndex`

      - `Optional<String> documentTitle`

      - `long endBlockIndex`

      - `Optional<String> fileId`

      - `long startBlockIndex`

      - `JsonValue; type "content_block_location"constant`

        - `CONTENT_BLOCK_LOCATION("content_block_location")`

    - `class CitationsWebSearchResultLocation:`

      - `String citedText`

      - `String encryptedIndex`

      - `Optional<String> title`

      - `JsonValue; type "web_search_result_location"constant`

        - `WEB_SEARCH_RESULT_LOCATION("web_search_result_location")`

      - `String url`

    - `class CitationsSearchResultLocation:`

      - `String citedText`

      - `long endBlockIndex`

      - `long searchResultIndex`

      - `String source`

      - `long startBlockIndex`

      - `Optional<String> title`

      - `JsonValue; type "search_result_location"constant`

        - `SEARCH_RESULT_LOCATION("search_result_location")`

  - `String text`

  - `JsonValue; type "text"constant`

    - `TEXT("text")`

### Text Block Param

- `class TextBlockParam:`

  - `String text`

  - `JsonValue; type "text"constant`

    - `TEXT("text")`

  - `Optional<CacheControlEphemeral> cacheControl`

    Create a cache control breakpoint at this content block.

    - `JsonValue; type "ephemeral"constant`

      - `EPHEMERAL("ephemeral")`

    - `Optional<Ttl> ttl`

      The time-to-live for the cache control breakpoint.

      This may be one the following values:

      - `5m`: 5 minutes
      - `1h`: 1 hour

      Defaults to `5m`.

      - `TTL_5M("5m")`

      - `TTL_1H("1h")`

  - `Optional<List<TextCitationParam>> citations`

    - `class CitationCharLocationParam:`

      - `String citedText`

      - `long documentIndex`

      - `Optional<String> documentTitle`

      - `long endCharIndex`

      - `long startCharIndex`

      - `JsonValue; type "char_location"constant`

        - `CHAR_LOCATION("char_location")`

    - `class CitationPageLocationParam:`

      - `String citedText`

      - `long documentIndex`

      - `Optional<String> documentTitle`

      - `long endPageNumber`

      - `long startPageNumber`

      - `JsonValue; type "page_location"constant`

        - `PAGE_LOCATION("page_location")`

    - `class CitationContentBlockLocationParam:`

      - `String citedText`

      - `long documentIndex`

      - `Optional<String> documentTitle`

      - `long endBlockIndex`

      - `long startBlockIndex`

      - `JsonValue; type "content_block_location"constant`

        - `CONTENT_BLOCK_LOCATION("content_block_location")`

    - `class CitationWebSearchResultLocationParam:`

      - `String citedText`

      - `String encryptedIndex`

      - `Optional<String> title`

      - `JsonValue; type "web_search_result_location"constant`

        - `WEB_SEARCH_RESULT_LOCATION("web_search_result_location")`

      - `String url`

    - `class CitationSearchResultLocationParam:`

      - `String citedText`

      - `long endBlockIndex`

      - `long searchResultIndex`

      - `String source`

      - `long startBlockIndex`

      - `Optional<String> title`

      - `JsonValue; type "search_result_location"constant`

        - `SEARCH_RESULT_LOCATION("search_result_location")`

### Text Citation

- `class TextCitation: A class that can be one of several variants.union`

  - `class CitationCharLocation:`

    - `String citedText`

    - `long documentIndex`

    - `Optional<String> documentTitle`

    - `long endCharIndex`

    - `Optional<String> fileId`

    - `long startCharIndex`

    - `JsonValue; type "char_location"constant`

      - `CHAR_LOCATION("char_location")`

  - `class CitationPageLocation:`

    - `String citedText`

    - `long documentIndex`

    - `Optional<String> documentTitle`

    - `long endPageNumber`

    - `Optional<String> fileId`

    - `long startPageNumber`

    - `JsonValue; type "page_location"constant`

      - `PAGE_LOCATION("page_location")`

  - `class CitationContentBlockLocation:`

    - `String citedText`

    - `long documentIndex`

    - `Optional<String> documentTitle`

    - `long endBlockIndex`

    - `Optional<String> fileId`

    - `long startBlockIndex`

    - `JsonValue; type "content_block_location"constant`

      - `CONTENT_BLOCK_LOCATION("content_block_location")`

  - `class CitationsWebSearchResultLocation:`

    - `String citedText`

    - `String encryptedIndex`

    - `Optional<String> title`

    - `JsonValue; type "web_search_result_location"constant`

      - `WEB_SEARCH_RESULT_LOCATION("web_search_result_location")`

    - `String url`

  - `class CitationsSearchResultLocation:`

    - `String citedText`

    - `long endBlockIndex`

    - `long searchResultIndex`

    - `String source`

    - `long startBlockIndex`

    - `Optional<String> title`

    - `JsonValue; type "search_result_location"constant`

      - `SEARCH_RESULT_LOCATION("search_result_location")`

### Text Citation Param

- `class TextCitationParam: A class that can be one of several variants.union`

  - `class CitationCharLocationParam:`

    - `String citedText`

    - `long documentIndex`

    - `Optional<String> documentTitle`

    - `long endCharIndex`

    - `long startCharIndex`

    - `JsonValue; type "char_location"constant`

      - `CHAR_LOCATION("char_location")`

  - `class CitationPageLocationParam:`

    - `String citedText`

    - `long documentIndex`

    - `Optional<String> documentTitle`

    - `long endPageNumber`

    - `long startPageNumber`

    - `JsonValue; type "page_location"constant`

      - `PAGE_LOCATION("page_location")`

  - `class CitationContentBlockLocationParam:`

    - `String citedText`

    - `long documentIndex`

    - `Optional<String> documentTitle`

    - `long endBlockIndex`

    - `long startBlockIndex`

    - `JsonValue; type "content_block_location"constant`

      - `CONTENT_BLOCK_LOCATION("content_block_location")`

  - `class CitationWebSearchResultLocationParam:`

    - `String citedText`

    - `String encryptedIndex`

    - `Optional<String> title`

    - `JsonValue; type "web_search_result_location"constant`

      - `WEB_SEARCH_RESULT_LOCATION("web_search_result_location")`

    - `String url`

  - `class CitationSearchResultLocationParam:`

    - `String citedText`

    - `long endBlockIndex`

    - `long searchResultIndex`

    - `String source`

    - `long startBlockIndex`

    - `Optional<String> title`

    - `JsonValue; type "search_result_location"constant`

      - `SEARCH_RESULT_LOCATION("search_result_location")`

### Text Delta

- `class TextDelta:`

  - `String text`

  - `JsonValue; type "text_delta"constant`

    - `TEXT_DELTA("text_delta")`

### Text Editor Code Execution Create Result Block

- `class TextEditorCodeExecutionCreateResultBlock:`

  - `boolean isFileUpdate`

  - `JsonValue; type "text_editor_code_execution_create_result"constant`

    - `TEXT_EDITOR_CODE_EXECUTION_CREATE_RESULT("text_editor_code_execution_create_result")`

### Text Editor Code Execution Create Result Block Param

- `class TextEditorCodeExecutionCreateResultBlockParam:`

  - `boolean isFileUpdate`

  - `JsonValue; type "text_editor_code_execution_create_result"constant`

    - `TEXT_EDITOR_CODE_EXECUTION_CREATE_RESULT("text_editor_code_execution_create_result")`

### Text Editor Code Execution Str Replace Result Block

- `class TextEditorCodeExecutionStrReplaceResultBlock:`

  - `Optional<List<String>> lines`

  - `Optional<Long> newLines`

  - `Optional<Long> newStart`

  - `Optional<Long> oldLines`

  - `Optional<Long> oldStart`

  - `JsonValue; type "text_editor_code_execution_str_replace_result"constant`

    - `TEXT_EDITOR_CODE_EXECUTION_STR_REPLACE_RESULT("text_editor_code_execution_str_replace_result")`

### Text Editor Code Execution Str Replace Result Block Param

- `class TextEditorCodeExecutionStrReplaceResultBlockParam:`

  - `JsonValue; type "text_editor_code_execution_str_replace_result"constant`

    - `TEXT_EDITOR_CODE_EXECUTION_STR_REPLACE_RESULT("text_editor_code_execution_str_replace_result")`

  - `Optional<List<String>> lines`

  - `Optional<Long> newLines`

  - `Optional<Long> newStart`

  - `Optional<Long> oldLines`

  - `Optional<Long> oldStart`

### Text Editor Code Execution Tool Result Block

- `class TextEditorCodeExecutionToolResultBlock:`

  - `Content content`

    - `class TextEditorCodeExecutionToolResultError:`

      - `TextEditorCodeExecutionToolResultErrorCode errorCode`

        - `INVALID_TOOL_INPUT("invalid_tool_input")`

        - `UNAVAILABLE("unavailable")`

        - `TOO_MANY_REQUESTS("too_many_requests")`

        - `EXECUTION_TIME_EXCEEDED("execution_time_exceeded")`

        - `FILE_NOT_FOUND("file_not_found")`

      - `Optional<String> errorMessage`

      - `JsonValue; type "text_editor_code_execution_tool_result_error"constant`

        - `TEXT_EDITOR_CODE_EXECUTION_TOOL_RESULT_ERROR("text_editor_code_execution_tool_result_error")`

    - `class TextEditorCodeExecutionViewResultBlock:`

      - `String content`

      - `FileType fileType`

        - `TEXT("text")`

        - `IMAGE("image")`

        - `PDF("pdf")`

      - `Optional<Long> numLines`

      - `Optional<Long> startLine`

      - `Optional<Long> totalLines`

      - `JsonValue; type "text_editor_code_execution_view_result"constant`

        - `TEXT_EDITOR_CODE_EXECUTION_VIEW_RESULT("text_editor_code_execution_view_result")`

    - `class TextEditorCodeExecutionCreateResultBlock:`

      - `boolean isFileUpdate`

      - `JsonValue; type "text_editor_code_execution_create_result"constant`

        - `TEXT_EDITOR_CODE_EXECUTION_CREATE_RESULT("text_editor_code_execution_create_result")`

    - `class TextEditorCodeExecutionStrReplaceResultBlock:`

      - `Optional<List<String>> lines`

      - `Optional<Long> newLines`

      - `Optional<Long> newStart`

      - `Optional<Long> oldLines`

      - `Optional<Long> oldStart`

      - `JsonValue; type "text_editor_code_execution_str_replace_result"constant`

        - `TEXT_EDITOR_CODE_EXECUTION_STR_REPLACE_RESULT("text_editor_code_execution_str_replace_result")`

  - `String toolUseId`

  - `JsonValue; type "text_editor_code_execution_tool_result"constant`

    - `TEXT_EDITOR_CODE_EXECUTION_TOOL_RESULT("text_editor_code_execution_tool_result")`

### Text Editor Code Execution Tool Result Block Param

- `class TextEditorCodeExecutionToolResultBlockParam:`

  - `Content content`

    - `class TextEditorCodeExecutionToolResultErrorParam:`

      - `TextEditorCodeExecutionToolResultErrorCode errorCode`

        - `INVALID_TOOL_INPUT("invalid_tool_input")`

        - `UNAVAILABLE("unavailable")`

        - `TOO_MANY_REQUESTS("too_many_requests")`

        - `EXECUTION_TIME_EXCEEDED("execution_time_exceeded")`

        - `FILE_NOT_FOUND("file_not_found")`

      - `JsonValue; type "text_editor_code_execution_tool_result_error"constant`

        - `TEXT_EDITOR_CODE_EXECUTION_TOOL_RESULT_ERROR("text_editor_code_execution_tool_result_error")`

      - `Optional<String> errorMessage`

    - `class TextEditorCodeExecutionViewResultBlockParam:`

      - `String content`

      - `FileType fileType`

        - `TEXT("text")`

        - `IMAGE("image")`

        - `PDF("pdf")`

      - `JsonValue; type "text_editor_code_execution_view_result"constant`

        - `TEXT_EDITOR_CODE_EXECUTION_VIEW_RESULT("text_editor_code_execution_view_result")`

      - `Optional<Long> numLines`

      - `Optional<Long> startLine`

      - `Optional<Long> totalLines`

    - `class TextEditorCodeExecutionCreateResultBlockParam:`

      - `boolean isFileUpdate`

      - `JsonValue; type "text_editor_code_execution_create_result"constant`

        - `TEXT_EDITOR_CODE_EXECUTION_CREATE_RESULT("text_editor_code_execution_create_result")`

    - `class TextEditorCodeExecutionStrReplaceResultBlockParam:`

      - `JsonValue; type "text_editor_code_execution_str_replace_result"constant`

        - `TEXT_EDITOR_CODE_EXECUTION_STR_REPLACE_RESULT("text_editor_code_execution_str_replace_result")`

      - `Optional<List<String>> lines`

      - `Optional<Long> newLines`

      - `Optional<Long> newStart`

      - `Optional<Long> oldLines`

      - `Optional<Long> oldStart`

  - `String toolUseId`

  - `JsonValue; type "text_editor_code_execution_tool_result"constant`

    - `TEXT_EDITOR_CODE_EXECUTION_TOOL_RESULT("text_editor_code_execution_tool_result")`

  - `Optional<CacheControlEphemeral> cacheControl`

    Create a cache control breakpoint at this content block.

    - `JsonValue; type "ephemeral"constant`

      - `EPHEMERAL("ephemeral")`

    - `Optional<Ttl> ttl`

      The time-to-live for the cache control breakpoint.

      This may be one the following values:

      - `5m`: 5 minutes
      - `1h`: 1 hour

      Defaults to `5m`.

      - `TTL_5M("5m")`

      - `TTL_1H("1h")`

### Text Editor Code Execution Tool Result Error

- `class TextEditorCodeExecutionToolResultError:`

  - `TextEditorCodeExecutionToolResultErrorCode errorCode`

    - `INVALID_TOOL_INPUT("invalid_tool_input")`

    - `UNAVAILABLE("unavailable")`

    - `TOO_MANY_REQUESTS("too_many_requests")`

    - `EXECUTION_TIME_EXCEEDED("execution_time_exceeded")`

    - `FILE_NOT_FOUND("file_not_found")`

  - `Optional<String> errorMessage`

  - `JsonValue; type "text_editor_code_execution_tool_result_error"constant`

    - `TEXT_EDITOR_CODE_EXECUTION_TOOL_RESULT_ERROR("text_editor_code_execution_tool_result_error")`

### Text Editor Code Execution Tool Result Error Code

- `enum TextEditorCodeExecutionToolResultErrorCode:`

  - `INVALID_TOOL_INPUT("invalid_tool_input")`

  - `UNAVAILABLE("unavailable")`

  - `TOO_MANY_REQUESTS("too_many_requests")`

  - `EXECUTION_TIME_EXCEEDED("execution_time_exceeded")`

  - `FILE_NOT_FOUND("file_not_found")`

### Text Editor Code Execution Tool Result Error Param

- `class TextEditorCodeExecutionToolResultErrorParam:`

  - `TextEditorCodeExecutionToolResultErrorCode errorCode`

    - `INVALID_TOOL_INPUT("invalid_tool_input")`

    - `UNAVAILABLE("unavailable")`

    - `TOO_MANY_REQUESTS("too_many_requests")`

    - `EXECUTION_TIME_EXCEEDED("execution_time_exceeded")`

    - `FILE_NOT_FOUND("file_not_found")`

  - `JsonValue; type "text_editor_code_execution_tool_result_error"constant`

    - `TEXT_EDITOR_CODE_EXECUTION_TOOL_RESULT_ERROR("text_editor_code_execution_tool_result_error")`

  - `Optional<String> errorMessage`

### Text Editor Code Execution View Result Block

- `class TextEditorCodeExecutionViewResultBlock:`

  - `String content`

  - `FileType fileType`

    - `TEXT("text")`

    - `IMAGE("image")`

    - `PDF("pdf")`

  - `Optional<Long> numLines`

  - `Optional<Long> startLine`

  - `Optional<Long> totalLines`

  - `JsonValue; type "text_editor_code_execution_view_result"constant`

    - `TEXT_EDITOR_CODE_EXECUTION_VIEW_RESULT("text_editor_code_execution_view_result")`

### Text Editor Code Execution View Result Block Param

- `class TextEditorCodeExecutionViewResultBlockParam:`

  - `String content`

  - `FileType fileType`

    - `TEXT("text")`

    - `IMAGE("image")`

    - `PDF("pdf")`

  - `JsonValue; type "text_editor_code_execution_view_result"constant`

    - `TEXT_EDITOR_CODE_EXECUTION_VIEW_RESULT("text_editor_code_execution_view_result")`

  - `Optional<Long> numLines`

  - `Optional<Long> startLine`

  - `Optional<Long> totalLines`

### Thinking Block

- `class ThinkingBlock:`

  - `String signature`

  - `String thinking`

  - `JsonValue; type "thinking"constant`

    - `THINKING("thinking")`

### Thinking Block Param

- `class ThinkingBlockParam:`

  - `String signature`

  - `String thinking`

  - `JsonValue; type "thinking"constant`

    - `THINKING("thinking")`

### Thinking Config Adaptive

- `class ThinkingConfigAdaptive:`

  - `JsonValue; type "adaptive"constant`

    - `ADAPTIVE("adaptive")`

### Thinking Config Disabled

- `class ThinkingConfigDisabled:`

  - `JsonValue; type "disabled"constant`

    - `DISABLED("disabled")`

### Thinking Config Enabled

- `class ThinkingConfigEnabled:`

  - `long budgetTokens`

    Determines how many tokens Claude can use for its internal reasoning process. Larger budgets can enable more thorough analysis for complex problems, improving response quality.

    Must be ≥1024 and less than `max_tokens`.

    See [extended thinking](https://docs.claude.com/en/docs/build-with-claude/extended-thinking) for details.

  - `JsonValue; type "enabled"constant`

    - `ENABLED("enabled")`

### Thinking Config Param

- `class ThinkingConfigParam: A class that can be one of several variants.union`

  Configuration for enabling Claude's extended thinking.

  When enabled, responses include `thinking` content blocks showing Claude's thinking process before the final answer. Requires a minimum budget of 1,024 tokens and counts towards your `max_tokens` limit.

  See [extended thinking](https://docs.claude.com/en/docs/build-with-claude/extended-thinking) for details.

  - `class ThinkingConfigEnabled:`

    - `long budgetTokens`

      Determines how many tokens Claude can use for its internal reasoning process. Larger budgets can enable more thorough analysis for complex problems, improving response quality.

      Must be ≥1024 and less than `max_tokens`.

      See [extended thinking](https://docs.claude.com/en/docs/build-with-claude/extended-thinking) for details.

    - `JsonValue; type "enabled"constant`

      - `ENABLED("enabled")`

  - `class ThinkingConfigDisabled:`

    - `JsonValue; type "disabled"constant`

      - `DISABLED("disabled")`

  - `class ThinkingConfigAdaptive:`

    - `JsonValue; type "adaptive"constant`

      - `ADAPTIVE("adaptive")`

### Thinking Delta

- `class ThinkingDelta:`

  - `String thinking`

  - `JsonValue; type "thinking_delta"constant`

    - `THINKING_DELTA("thinking_delta")`

### Tool

- `class Tool:`

  - `InputSchema inputSchema`

    [JSON schema](https://json-schema.org/draft/2020-12) for this tool's input.

    This defines the shape of the `input` that your tool accepts and that the model will produce.

    - `JsonValue; type "object"constant`

      - `OBJECT("object")`

    - `Optional<Properties> properties`

    - `Optional<List<String>> required`

  - `String name`

    Name of the tool.

    This is how the tool will be called by the model and in `tool_use` blocks.

  - `Optional<List<AllowedCaller>> allowedCallers`

    - `DIRECT("direct")`

    - `CODE_EXECUTION_20250825("code_execution_20250825")`

    - `CODE_EXECUTION_20260120("code_execution_20260120")`

  - `Optional<CacheControlEphemeral> cacheControl`

    Create a cache control breakpoint at this content block.

    - `JsonValue; type "ephemeral"constant`

      - `EPHEMERAL("ephemeral")`

    - `Optional<Ttl> ttl`

      The time-to-live for the cache control breakpoint.

      This may be one the following values:

      - `5m`: 5 minutes
      - `1h`: 1 hour

      Defaults to `5m`.

      - `TTL_5M("5m")`

      - `TTL_1H("1h")`

  - `Optional<Boolean> deferLoading`

    If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

  - `Optional<String> description`

    Description of what this tool does.

    Tool descriptions should be as detailed as possible. The more information that the model has about what the tool is and how to use it, the better it will perform. You can use natural language descriptions to reinforce important aspects of the tool input JSON schema.

  - `Optional<Boolean> eagerInputStreaming`

    Enable eager input streaming for this tool. When true, tool input parameters will be streamed incrementally as they are generated, and types will be inferred on-the-fly rather than buffering the full JSON output. When false, streaming is disabled for this tool even if the fine-grained-tool-streaming beta is active. When null (default), uses the default behavior based on beta headers.

  - `Optional<List<InputExample>> inputExamples`

  - `Optional<Boolean> strict`

    When true, guarantees schema validation on tool names and inputs

  - `Optional<Type> type`

    - `CUSTOM("custom")`

### Tool Bash 20250124

- `class ToolBash20250124:`

  - `JsonValue; name "bash"constant`

    Name of the tool.

    This is how the tool will be called by the model and in `tool_use` blocks.

    - `BASH("bash")`

  - `JsonValue; type "bash_20250124"constant`

    - `BASH_20250124("bash_20250124")`

  - `Optional<List<AllowedCaller>> allowedCallers`

    - `DIRECT("direct")`

    - `CODE_EXECUTION_20250825("code_execution_20250825")`

    - `CODE_EXECUTION_20260120("code_execution_20260120")`

  - `Optional<CacheControlEphemeral> cacheControl`

    Create a cache control breakpoint at this content block.

    - `JsonValue; type "ephemeral"constant`

      - `EPHEMERAL("ephemeral")`

    - `Optional<Ttl> ttl`

      The time-to-live for the cache control breakpoint.

      This may be one the following values:

      - `5m`: 5 minutes
      - `1h`: 1 hour

      Defaults to `5m`.

      - `TTL_5M("5m")`

      - `TTL_1H("1h")`

  - `Optional<Boolean> deferLoading`

    If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

  - `Optional<List<InputExample>> inputExamples`

  - `Optional<Boolean> strict`

    When true, guarantees schema validation on tool names and inputs

### Tool Choice

- `class ToolChoice: A class that can be one of several variants.union`

  How the model should use the provided tools. The model can use a specific tool, any available tool, decide by itself, or not use tools at all.

  - `class ToolChoiceAuto:`

    The model will automatically decide whether to use tools.

    - `JsonValue; type "auto"constant`

      - `AUTO("auto")`

    - `Optional<Boolean> disableParallelToolUse`

      Whether to disable parallel tool use.

      Defaults to `false`. If set to `true`, the model will output at most one tool use.

  - `class ToolChoiceAny:`

    The model will use any available tools.

    - `JsonValue; type "any"constant`

      - `ANY("any")`

    - `Optional<Boolean> disableParallelToolUse`

      Whether to disable parallel tool use.

      Defaults to `false`. If set to `true`, the model will output exactly one tool use.

  - `class ToolChoiceTool:`

    The model will use the specified tool with `tool_choice.name`.

    - `String name`

      The name of the tool to use.

    - `JsonValue; type "tool"constant`

      - `TOOL("tool")`

    - `Optional<Boolean> disableParallelToolUse`

      Whether to disable parallel tool use.

      Defaults to `false`. If set to `true`, the model will output exactly one tool use.

  - `class ToolChoiceNone:`

    The model will not be allowed to use tools.

    - `JsonValue; type "none"constant`

      - `NONE("none")`

### Tool Choice Any

- `class ToolChoiceAny:`

  The model will use any available tools.

  - `JsonValue; type "any"constant`

    - `ANY("any")`

  - `Optional<Boolean> disableParallelToolUse`

    Whether to disable parallel tool use.

    Defaults to `false`. If set to `true`, the model will output exactly one tool use.

### Tool Choice Auto

- `class ToolChoiceAuto:`

  The model will automatically decide whether to use tools.

  - `JsonValue; type "auto"constant`

    - `AUTO("auto")`

  - `Optional<Boolean> disableParallelToolUse`

    Whether to disable parallel tool use.

    Defaults to `false`. If set to `true`, the model will output at most one tool use.

### Tool Choice None

- `class ToolChoiceNone:`

  The model will not be allowed to use tools.

  - `JsonValue; type "none"constant`

    - `NONE("none")`

### Tool Choice Tool

- `class ToolChoiceTool:`

  The model will use the specified tool with `tool_choice.name`.

  - `String name`

    The name of the tool to use.

  - `JsonValue; type "tool"constant`

    - `TOOL("tool")`

  - `Optional<Boolean> disableParallelToolUse`

    Whether to disable parallel tool use.

    Defaults to `false`. If set to `true`, the model will output exactly one tool use.

### Tool Reference Block

- `class ToolReferenceBlock:`

  - `String toolName`

  - `JsonValue; type "tool_reference"constant`

    - `TOOL_REFERENCE("tool_reference")`

### Tool Reference Block Param

- `class ToolReferenceBlockParam:`

  Tool reference block that can be included in tool_result content.

  - `String toolName`

  - `JsonValue; type "tool_reference"constant`

    - `TOOL_REFERENCE("tool_reference")`

  - `Optional<CacheControlEphemeral> cacheControl`

    Create a cache control breakpoint at this content block.

    - `JsonValue; type "ephemeral"constant`

      - `EPHEMERAL("ephemeral")`

    - `Optional<Ttl> ttl`

      The time-to-live for the cache control breakpoint.

      This may be one the following values:

      - `5m`: 5 minutes
      - `1h`: 1 hour

      Defaults to `5m`.

      - `TTL_5M("5m")`

      - `TTL_1H("1h")`

### Tool Result Block Param

- `class ToolResultBlockParam:`

  - `String toolUseId`

  - `JsonValue; type "tool_result"constant`

    - `TOOL_RESULT("tool_result")`

  - `Optional<CacheControlEphemeral> cacheControl`

    Create a cache control breakpoint at this content block.

    - `JsonValue; type "ephemeral"constant`

      - `EPHEMERAL("ephemeral")`

    - `Optional<Ttl> ttl`

      The time-to-live for the cache control breakpoint.

      This may be one the following values:

      - `5m`: 5 minutes
      - `1h`: 1 hour

      Defaults to `5m`.

      - `TTL_5M("5m")`

      - `TTL_1H("1h")`

  - `Optional<Content> content`

    - `String`

    - `List<Block>`

      - `class TextBlockParam:`

        - `String text`

        - `JsonValue; type "text"constant`

          - `TEXT("text")`

        - `Optional<CacheControlEphemeral> cacheControl`

          Create a cache control breakpoint at this content block.

          - `JsonValue; type "ephemeral"constant`

            - `EPHEMERAL("ephemeral")`

          - `Optional<Ttl> ttl`

            The time-to-live for the cache control breakpoint.

            This may be one the following values:

            - `5m`: 5 minutes
            - `1h`: 1 hour

            Defaults to `5m`.

            - `TTL_5M("5m")`

            - `TTL_1H("1h")`

        - `Optional<List<TextCitationParam>> citations`

          - `class CitationCharLocationParam:`

            - `String citedText`

            - `long documentIndex`

            - `Optional<String> documentTitle`

            - `long endCharIndex`

            - `long startCharIndex`

            - `JsonValue; type "char_location"constant`

              - `CHAR_LOCATION("char_location")`

          - `class CitationPageLocationParam:`

            - `String citedText`

            - `long documentIndex`

            - `Optional<String> documentTitle`

            - `long endPageNumber`

            - `long startPageNumber`

            - `JsonValue; type "page_location"constant`

              - `PAGE_LOCATION("page_location")`

          - `class CitationContentBlockLocationParam:`

            - `String citedText`

            - `long documentIndex`

            - `Optional<String> documentTitle`

            - `long endBlockIndex`

            - `long startBlockIndex`

            - `JsonValue; type "content_block_location"constant`

              - `CONTENT_BLOCK_LOCATION("content_block_location")`

          - `class CitationWebSearchResultLocationParam:`

            - `String citedText`

            - `String encryptedIndex`

            - `Optional<String> title`

            - `JsonValue; type "web_search_result_location"constant`

              - `WEB_SEARCH_RESULT_LOCATION("web_search_result_location")`

            - `String url`

          - `class CitationSearchResultLocationParam:`

            - `String citedText`

            - `long endBlockIndex`

            - `long searchResultIndex`

            - `String source`

            - `long startBlockIndex`

            - `Optional<String> title`

            - `JsonValue; type "search_result_location"constant`

              - `SEARCH_RESULT_LOCATION("search_result_location")`

      - `class ImageBlockParam:`

        - `Source source`

          - `class Base64ImageSource:`

            - `String data`

            - `MediaType mediaType`

              - `IMAGE_JPEG("image/jpeg")`

              - `IMAGE_PNG("image/png")`

              - `IMAGE_GIF("image/gif")`

              - `IMAGE_WEBP("image/webp")`

            - `JsonValue; type "base64"constant`

              - `BASE64("base64")`

          - `class UrlImageSource:`

            - `JsonValue; type "url"constant`

              - `URL("url")`

            - `String url`

        - `JsonValue; type "image"constant`

          - `IMAGE("image")`

        - `Optional<CacheControlEphemeral> cacheControl`

          Create a cache control breakpoint at this content block.

          - `JsonValue; type "ephemeral"constant`

            - `EPHEMERAL("ephemeral")`

          - `Optional<Ttl> ttl`

            The time-to-live for the cache control breakpoint.

            This may be one the following values:

            - `5m`: 5 minutes
            - `1h`: 1 hour

            Defaults to `5m`.

            - `TTL_5M("5m")`

            - `TTL_1H("1h")`

      - `class SearchResultBlockParam:`

        - `List<TextBlockParam> content`

          - `String text`

          - `JsonValue; type "text"constant`

            - `TEXT("text")`

          - `Optional<CacheControlEphemeral> cacheControl`

            Create a cache control breakpoint at this content block.

            - `JsonValue; type "ephemeral"constant`

              - `EPHEMERAL("ephemeral")`

            - `Optional<Ttl> ttl`

              The time-to-live for the cache control breakpoint.

              This may be one the following values:

              - `5m`: 5 minutes
              - `1h`: 1 hour

              Defaults to `5m`.

              - `TTL_5M("5m")`

              - `TTL_1H("1h")`

          - `Optional<List<TextCitationParam>> citations`

            - `class CitationCharLocationParam:`

              - `String citedText`

              - `long documentIndex`

              - `Optional<String> documentTitle`

              - `long endCharIndex`

              - `long startCharIndex`

              - `JsonValue; type "char_location"constant`

                - `CHAR_LOCATION("char_location")`

            - `class CitationPageLocationParam:`

              - `String citedText`

              - `long documentIndex`

              - `Optional<String> documentTitle`

              - `long endPageNumber`

              - `long startPageNumber`

              - `JsonValue; type "page_location"constant`

                - `PAGE_LOCATION("page_location")`

            - `class CitationContentBlockLocationParam:`

              - `String citedText`

              - `long documentIndex`

              - `Optional<String> documentTitle`

              - `long endBlockIndex`

              - `long startBlockIndex`

              - `JsonValue; type "content_block_location"constant`

                - `CONTENT_BLOCK_LOCATION("content_block_location")`

            - `class CitationWebSearchResultLocationParam:`

              - `String citedText`

              - `String encryptedIndex`

              - `Optional<String> title`

              - `JsonValue; type "web_search_result_location"constant`

                - `WEB_SEARCH_RESULT_LOCATION("web_search_result_location")`

              - `String url`

            - `class CitationSearchResultLocationParam:`

              - `String citedText`

              - `long endBlockIndex`

              - `long searchResultIndex`

              - `String source`

              - `long startBlockIndex`

              - `Optional<String> title`

              - `JsonValue; type "search_result_location"constant`

                - `SEARCH_RESULT_LOCATION("search_result_location")`

        - `String source`

        - `String title`

        - `JsonValue; type "search_result"constant`

          - `SEARCH_RESULT("search_result")`

        - `Optional<CacheControlEphemeral> cacheControl`

          Create a cache control breakpoint at this content block.

          - `JsonValue; type "ephemeral"constant`

            - `EPHEMERAL("ephemeral")`

          - `Optional<Ttl> ttl`

            The time-to-live for the cache control breakpoint.

            This may be one the following values:

            - `5m`: 5 minutes
            - `1h`: 1 hour

            Defaults to `5m`.

            - `TTL_5M("5m")`

            - `TTL_1H("1h")`

        - `Optional<CitationsConfigParam> citations`

          - `Optional<Boolean> enabled`

      - `class DocumentBlockParam:`

        - `Source source`

          - `class Base64PdfSource:`

            - `String data`

            - `JsonValue; mediaType "application/pdf"constant`

              - `APPLICATION_PDF("application/pdf")`

            - `JsonValue; type "base64"constant`

              - `BASE64("base64")`

          - `class PlainTextSource:`

            - `String data`

            - `JsonValue; mediaType "text/plain"constant`

              - `TEXT_PLAIN("text/plain")`

            - `JsonValue; type "text"constant`

              - `TEXT("text")`

          - `class ContentBlockSource:`

            - `Content content`

              - `String`

              - `List<ContentBlockSourceContent>`

                - `class TextBlockParam:`

                  - `String text`

                  - `JsonValue; type "text"constant`

                    - `TEXT("text")`

                  - `Optional<CacheControlEphemeral> cacheControl`

                    Create a cache control breakpoint at this content block.

                    - `JsonValue; type "ephemeral"constant`

                      - `EPHEMERAL("ephemeral")`

                    - `Optional<Ttl> ttl`

                      The time-to-live for the cache control breakpoint.

                      This may be one the following values:

                      - `5m`: 5 minutes
                      - `1h`: 1 hour

                      Defaults to `5m`.

                      - `TTL_5M("5m")`

                      - `TTL_1H("1h")`

                  - `Optional<List<TextCitationParam>> citations`

                    - `class CitationCharLocationParam:`

                      - `String citedText`

                      - `long documentIndex`

                      - `Optional<String> documentTitle`

                      - `long endCharIndex`

                      - `long startCharIndex`

                      - `JsonValue; type "char_location"constant`

                        - `CHAR_LOCATION("char_location")`

                    - `class CitationPageLocationParam:`

                      - `String citedText`

                      - `long documentIndex`

                      - `Optional<String> documentTitle`

                      - `long endPageNumber`

                      - `long startPageNumber`

                      - `JsonValue; type "page_location"constant`

                        - `PAGE_LOCATION("page_location")`

                    - `class CitationContentBlockLocationParam:`

                      - `String citedText`

                      - `long documentIndex`

                      - `Optional<String> documentTitle`

                      - `long endBlockIndex`

                      - `long startBlockIndex`

                      - `JsonValue; type "content_block_location"constant`

                        - `CONTENT_BLOCK_LOCATION("content_block_location")`

                    - `class CitationWebSearchResultLocationParam:`

                      - `String citedText`

                      - `String encryptedIndex`

                      - `Optional<String> title`

                      - `JsonValue; type "web_search_result_location"constant`

                        - `WEB_SEARCH_RESULT_LOCATION("web_search_result_location")`

                      - `String url`

                    - `class CitationSearchResultLocationParam:`

                      - `String citedText`

                      - `long endBlockIndex`

                      - `long searchResultIndex`

                      - `String source`

                      - `long startBlockIndex`

                      - `Optional<String> title`

                      - `JsonValue; type "search_result_location"constant`

                        - `SEARCH_RESULT_LOCATION("search_result_location")`

                - `class ImageBlockParam:`

                  - `Source source`

                    - `class Base64ImageSource:`

                      - `String data`

                      - `MediaType mediaType`

                        - `IMAGE_JPEG("image/jpeg")`

                        - `IMAGE_PNG("image/png")`

                        - `IMAGE_GIF("image/gif")`

                        - `IMAGE_WEBP("image/webp")`

                      - `JsonValue; type "base64"constant`

                        - `BASE64("base64")`

                    - `class UrlImageSource:`

                      - `JsonValue; type "url"constant`

                        - `URL("url")`

                      - `String url`

                  - `JsonValue; type "image"constant`

                    - `IMAGE("image")`

                  - `Optional<CacheControlEphemeral> cacheControl`

                    Create a cache control breakpoint at this content block.

                    - `JsonValue; type "ephemeral"constant`

                      - `EPHEMERAL("ephemeral")`

                    - `Optional<Ttl> ttl`

                      The time-to-live for the cache control breakpoint.

                      This may be one the following values:

                      - `5m`: 5 minutes
                      - `1h`: 1 hour

                      Defaults to `5m`.

                      - `TTL_5M("5m")`

                      - `TTL_1H("1h")`

            - `JsonValue; type "content"constant`

              - `CONTENT("content")`

          - `class UrlPdfSource:`

            - `JsonValue; type "url"constant`

              - `URL("url")`

            - `String url`

        - `JsonValue; type "document"constant`

          - `DOCUMENT("document")`

        - `Optional<CacheControlEphemeral> cacheControl`

          Create a cache control breakpoint at this content block.

          - `JsonValue; type "ephemeral"constant`

            - `EPHEMERAL("ephemeral")`

          - `Optional<Ttl> ttl`

            The time-to-live for the cache control breakpoint.

            This may be one the following values:

            - `5m`: 5 minutes
            - `1h`: 1 hour

            Defaults to `5m`.

            - `TTL_5M("5m")`

            - `TTL_1H("1h")`

        - `Optional<CitationsConfigParam> citations`

          - `Optional<Boolean> enabled`

        - `Optional<String> context`

        - `Optional<String> title`

      - `class ToolReferenceBlockParam:`

        Tool reference block that can be included in tool_result content.

        - `String toolName`

        - `JsonValue; type "tool_reference"constant`

          - `TOOL_REFERENCE("tool_reference")`

        - `Optional<CacheControlEphemeral> cacheControl`

          Create a cache control breakpoint at this content block.

          - `JsonValue; type "ephemeral"constant`

            - `EPHEMERAL("ephemeral")`

          - `Optional<Ttl> ttl`

            The time-to-live for the cache control breakpoint.

            This may be one the following values:

            - `5m`: 5 minutes
            - `1h`: 1 hour

            Defaults to `5m`.

            - `TTL_5M("5m")`

            - `TTL_1H("1h")`

  - `Optional<Boolean> isError`

### Tool Search Tool Bm25 20251119

- `class ToolSearchToolBm25_20251119:`

  - `JsonValue; name "tool_search_tool_bm25"constant`

    Name of the tool.

    This is how the tool will be called by the model and in `tool_use` blocks.

    - `TOOL_SEARCH_TOOL_BM25("tool_search_tool_bm25")`

  - `Type type`

    - `TOOL_SEARCH_TOOL_BM25_20251119("tool_search_tool_bm25_20251119")`

    - `TOOL_SEARCH_TOOL_BM25("tool_search_tool_bm25")`

  - `Optional<List<AllowedCaller>> allowedCallers`

    - `DIRECT("direct")`

    - `CODE_EXECUTION_20250825("code_execution_20250825")`

    - `CODE_EXECUTION_20260120("code_execution_20260120")`

  - `Optional<CacheControlEphemeral> cacheControl`

    Create a cache control breakpoint at this content block.

    - `JsonValue; type "ephemeral"constant`

      - `EPHEMERAL("ephemeral")`

    - `Optional<Ttl> ttl`

      The time-to-live for the cache control breakpoint.

      This may be one the following values:

      - `5m`: 5 minutes
      - `1h`: 1 hour

      Defaults to `5m`.

      - `TTL_5M("5m")`

      - `TTL_1H("1h")`

  - `Optional<Boolean> deferLoading`

    If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

  - `Optional<Boolean> strict`

    When true, guarantees schema validation on tool names and inputs

### Tool Search Tool Regex 20251119

- `class ToolSearchToolRegex20251119:`

  - `JsonValue; name "tool_search_tool_regex"constant`

    Name of the tool.

    This is how the tool will be called by the model and in `tool_use` blocks.

    - `TOOL_SEARCH_TOOL_REGEX("tool_search_tool_regex")`

  - `Type type`

    - `TOOL_SEARCH_TOOL_REGEX_20251119("tool_search_tool_regex_20251119")`

    - `TOOL_SEARCH_TOOL_REGEX("tool_search_tool_regex")`

  - `Optional<List<AllowedCaller>> allowedCallers`

    - `DIRECT("direct")`

    - `CODE_EXECUTION_20250825("code_execution_20250825")`

    - `CODE_EXECUTION_20260120("code_execution_20260120")`

  - `Optional<CacheControlEphemeral> cacheControl`

    Create a cache control breakpoint at this content block.

    - `JsonValue; type "ephemeral"constant`

      - `EPHEMERAL("ephemeral")`

    - `Optional<Ttl> ttl`

      The time-to-live for the cache control breakpoint.

      This may be one the following values:

      - `5m`: 5 minutes
      - `1h`: 1 hour

      Defaults to `5m`.

      - `TTL_5M("5m")`

      - `TTL_1H("1h")`

  - `Optional<Boolean> deferLoading`

    If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

  - `Optional<Boolean> strict`

    When true, guarantees schema validation on tool names and inputs

### Tool Search Tool Result Block

- `class ToolSearchToolResultBlock:`

  - `Content content`

    - `class ToolSearchToolResultError:`

      - `ToolSearchToolResultErrorCode errorCode`

        - `INVALID_TOOL_INPUT("invalid_tool_input")`

        - `UNAVAILABLE("unavailable")`

        - `TOO_MANY_REQUESTS("too_many_requests")`

        - `EXECUTION_TIME_EXCEEDED("execution_time_exceeded")`

      - `Optional<String> errorMessage`

      - `JsonValue; type "tool_search_tool_result_error"constant`

        - `TOOL_SEARCH_TOOL_RESULT_ERROR("tool_search_tool_result_error")`

    - `class ToolSearchToolSearchResultBlock:`

      - `List<ToolReferenceBlock> toolReferences`

        - `String toolName`

        - `JsonValue; type "tool_reference"constant`

          - `TOOL_REFERENCE("tool_reference")`

      - `JsonValue; type "tool_search_tool_search_result"constant`

        - `TOOL_SEARCH_TOOL_SEARCH_RESULT("tool_search_tool_search_result")`

  - `String toolUseId`

  - `JsonValue; type "tool_search_tool_result"constant`

    - `TOOL_SEARCH_TOOL_RESULT("tool_search_tool_result")`

### Tool Search Tool Result Block Param

- `class ToolSearchToolResultBlockParam:`

  - `Content content`

    - `class ToolSearchToolResultErrorParam:`

      - `ToolSearchToolResultErrorCode errorCode`

        - `INVALID_TOOL_INPUT("invalid_tool_input")`

        - `UNAVAILABLE("unavailable")`

        - `TOO_MANY_REQUESTS("too_many_requests")`

        - `EXECUTION_TIME_EXCEEDED("execution_time_exceeded")`

      - `JsonValue; type "tool_search_tool_result_error"constant`

        - `TOOL_SEARCH_TOOL_RESULT_ERROR("tool_search_tool_result_error")`

    - `class ToolSearchToolSearchResultBlockParam:`

      - `List<ToolReferenceBlockParam> toolReferences`

        - `String toolName`

        - `JsonValue; type "tool_reference"constant`

          - `TOOL_REFERENCE("tool_reference")`

        - `Optional<CacheControlEphemeral> cacheControl`

          Create a cache control breakpoint at this content block.

          - `JsonValue; type "ephemeral"constant`

            - `EPHEMERAL("ephemeral")`

          - `Optional<Ttl> ttl`

            The time-to-live for the cache control breakpoint.

            This may be one the following values:

            - `5m`: 5 minutes
            - `1h`: 1 hour

            Defaults to `5m`.

            - `TTL_5M("5m")`

            - `TTL_1H("1h")`

      - `JsonValue; type "tool_search_tool_search_result"constant`

        - `TOOL_SEARCH_TOOL_SEARCH_RESULT("tool_search_tool_search_result")`

  - `String toolUseId`

  - `JsonValue; type "tool_search_tool_result"constant`

    - `TOOL_SEARCH_TOOL_RESULT("tool_search_tool_result")`

  - `Optional<CacheControlEphemeral> cacheControl`

    Create a cache control breakpoint at this content block.

    - `JsonValue; type "ephemeral"constant`

      - `EPHEMERAL("ephemeral")`

    - `Optional<Ttl> ttl`

      The time-to-live for the cache control breakpoint.

      This may be one the following values:

      - `5m`: 5 minutes
      - `1h`: 1 hour

      Defaults to `5m`.

      - `TTL_5M("5m")`

      - `TTL_1H("1h")`

### Tool Search Tool Result Error

- `class ToolSearchToolResultError:`

  - `ToolSearchToolResultErrorCode errorCode`

    - `INVALID_TOOL_INPUT("invalid_tool_input")`

    - `UNAVAILABLE("unavailable")`

    - `TOO_MANY_REQUESTS("too_many_requests")`

    - `EXECUTION_TIME_EXCEEDED("execution_time_exceeded")`

  - `Optional<String> errorMessage`

  - `JsonValue; type "tool_search_tool_result_error"constant`

    - `TOOL_SEARCH_TOOL_RESULT_ERROR("tool_search_tool_result_error")`

### Tool Search Tool Result Error Code

- `enum ToolSearchToolResultErrorCode:`

  - `INVALID_TOOL_INPUT("invalid_tool_input")`

  - `UNAVAILABLE("unavailable")`

  - `TOO_MANY_REQUESTS("too_many_requests")`

  - `EXECUTION_TIME_EXCEEDED("execution_time_exceeded")`

### Tool Search Tool Result Error Param

- `class ToolSearchToolResultErrorParam:`

  - `ToolSearchToolResultErrorCode errorCode`

    - `INVALID_TOOL_INPUT("invalid_tool_input")`

    - `UNAVAILABLE("unavailable")`

    - `TOO_MANY_REQUESTS("too_many_requests")`

    - `EXECUTION_TIME_EXCEEDED("execution_time_exceeded")`

  - `JsonValue; type "tool_search_tool_result_error"constant`

    - `TOOL_SEARCH_TOOL_RESULT_ERROR("tool_search_tool_result_error")`

### Tool Search Tool Search Result Block

- `class ToolSearchToolSearchResultBlock:`

  - `List<ToolReferenceBlock> toolReferences`

    - `String toolName`

    - `JsonValue; type "tool_reference"constant`

      - `TOOL_REFERENCE("tool_reference")`

  - `JsonValue; type "tool_search_tool_search_result"constant`

    - `TOOL_SEARCH_TOOL_SEARCH_RESULT("tool_search_tool_search_result")`

### Tool Search Tool Search Result Block Param

- `class ToolSearchToolSearchResultBlockParam:`

  - `List<ToolReferenceBlockParam> toolReferences`

    - `String toolName`

    - `JsonValue; type "tool_reference"constant`

      - `TOOL_REFERENCE("tool_reference")`

    - `Optional<CacheControlEphemeral> cacheControl`

      Create a cache control breakpoint at this content block.

      - `JsonValue; type "ephemeral"constant`

        - `EPHEMERAL("ephemeral")`

      - `Optional<Ttl> ttl`

        The time-to-live for the cache control breakpoint.

        This may be one the following values:

        - `5m`: 5 minutes
        - `1h`: 1 hour

        Defaults to `5m`.

        - `TTL_5M("5m")`

        - `TTL_1H("1h")`

  - `JsonValue; type "tool_search_tool_search_result"constant`

    - `TOOL_SEARCH_TOOL_SEARCH_RESULT("tool_search_tool_search_result")`

### Tool Text Editor 20250124

- `class ToolTextEditor20250124:`

  - `JsonValue; name "str_replace_editor"constant`

    Name of the tool.

    This is how the tool will be called by the model and in `tool_use` blocks.

    - `STR_REPLACE_EDITOR("str_replace_editor")`

  - `JsonValue; type "text_editor_20250124"constant`

    - `TEXT_EDITOR_20250124("text_editor_20250124")`

  - `Optional<List<AllowedCaller>> allowedCallers`

    - `DIRECT("direct")`

    - `CODE_EXECUTION_20250825("code_execution_20250825")`

    - `CODE_EXECUTION_20260120("code_execution_20260120")`

  - `Optional<CacheControlEphemeral> cacheControl`

    Create a cache control breakpoint at this content block.

    - `JsonValue; type "ephemeral"constant`

      - `EPHEMERAL("ephemeral")`

    - `Optional<Ttl> ttl`

      The time-to-live for the cache control breakpoint.

      This may be one the following values:

      - `5m`: 5 minutes
      - `1h`: 1 hour

      Defaults to `5m`.

      - `TTL_5M("5m")`

      - `TTL_1H("1h")`

  - `Optional<Boolean> deferLoading`

    If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

  - `Optional<List<InputExample>> inputExamples`

  - `Optional<Boolean> strict`

    When true, guarantees schema validation on tool names and inputs

### Tool Text Editor 20250429

- `class ToolTextEditor20250429:`

  - `JsonValue; name "str_replace_based_edit_tool"constant`

    Name of the tool.

    This is how the tool will be called by the model and in `tool_use` blocks.

    - `STR_REPLACE_BASED_EDIT_TOOL("str_replace_based_edit_tool")`

  - `JsonValue; type "text_editor_20250429"constant`

    - `TEXT_EDITOR_20250429("text_editor_20250429")`

  - `Optional<List<AllowedCaller>> allowedCallers`

    - `DIRECT("direct")`

    - `CODE_EXECUTION_20250825("code_execution_20250825")`

    - `CODE_EXECUTION_20260120("code_execution_20260120")`

  - `Optional<CacheControlEphemeral> cacheControl`

    Create a cache control breakpoint at this content block.

    - `JsonValue; type "ephemeral"constant`

      - `EPHEMERAL("ephemeral")`

    - `Optional<Ttl> ttl`

      The time-to-live for the cache control breakpoint.

      This may be one the following values:

      - `5m`: 5 minutes
      - `1h`: 1 hour

      Defaults to `5m`.

      - `TTL_5M("5m")`

      - `TTL_1H("1h")`

  - `Optional<Boolean> deferLoading`

    If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

  - `Optional<List<InputExample>> inputExamples`

  - `Optional<Boolean> strict`

    When true, guarantees schema validation on tool names and inputs

### Tool Text Editor 20250728

- `class ToolTextEditor20250728:`

  - `JsonValue; name "str_replace_based_edit_tool"constant`

    Name of the tool.

    This is how the tool will be called by the model and in `tool_use` blocks.

    - `STR_REPLACE_BASED_EDIT_TOOL("str_replace_based_edit_tool")`

  - `JsonValue; type "text_editor_20250728"constant`

    - `TEXT_EDITOR_20250728("text_editor_20250728")`

  - `Optional<List<AllowedCaller>> allowedCallers`

    - `DIRECT("direct")`

    - `CODE_EXECUTION_20250825("code_execution_20250825")`

    - `CODE_EXECUTION_20260120("code_execution_20260120")`

  - `Optional<CacheControlEphemeral> cacheControl`

    Create a cache control breakpoint at this content block.

    - `JsonValue; type "ephemeral"constant`

      - `EPHEMERAL("ephemeral")`

    - `Optional<Ttl> ttl`

      The time-to-live for the cache control breakpoint.

      This may be one the following values:

      - `5m`: 5 minutes
      - `1h`: 1 hour

      Defaults to `5m`.

      - `TTL_5M("5m")`

      - `TTL_1H("1h")`

  - `Optional<Boolean> deferLoading`

    If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

  - `Optional<List<InputExample>> inputExamples`

  - `Optional<Long> maxCharacters`

    Maximum number of characters to display when viewing a file. If not specified, defaults to displaying the full file.

  - `Optional<Boolean> strict`

    When true, guarantees schema validation on tool names and inputs

### Tool Union

- `class ToolUnion: A class that can be one of several variants.union`

  Code execution tool with REPL state persistence (daemon mode + gVisor checkpoint).

  - `class Tool:`

    - `InputSchema inputSchema`

      [JSON schema](https://json-schema.org/draft/2020-12) for this tool's input.

      This defines the shape of the `input` that your tool accepts and that the model will produce.

      - `JsonValue; type "object"constant`

        - `OBJECT("object")`

      - `Optional<Properties> properties`

      - `Optional<List<String>> required`

    - `String name`

      Name of the tool.

      This is how the tool will be called by the model and in `tool_use` blocks.

    - `Optional<List<AllowedCaller>> allowedCallers`

      - `DIRECT("direct")`

      - `CODE_EXECUTION_20250825("code_execution_20250825")`

      - `CODE_EXECUTION_20260120("code_execution_20260120")`

    - `Optional<CacheControlEphemeral> cacheControl`

      Create a cache control breakpoint at this content block.

      - `JsonValue; type "ephemeral"constant`

        - `EPHEMERAL("ephemeral")`

      - `Optional<Ttl> ttl`

        The time-to-live for the cache control breakpoint.

        This may be one the following values:

        - `5m`: 5 minutes
        - `1h`: 1 hour

        Defaults to `5m`.

        - `TTL_5M("5m")`

        - `TTL_1H("1h")`

    - `Optional<Boolean> deferLoading`

      If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

    - `Optional<String> description`

      Description of what this tool does.

      Tool descriptions should be as detailed as possible. The more information that the model has about what the tool is and how to use it, the better it will perform. You can use natural language descriptions to reinforce important aspects of the tool input JSON schema.

    - `Optional<Boolean> eagerInputStreaming`

      Enable eager input streaming for this tool. When true, tool input parameters will be streamed incrementally as they are generated, and types will be inferred on-the-fly rather than buffering the full JSON output. When false, streaming is disabled for this tool even if the fine-grained-tool-streaming beta is active. When null (default), uses the default behavior based on beta headers.

    - `Optional<List<InputExample>> inputExamples`

    - `Optional<Boolean> strict`

      When true, guarantees schema validation on tool names and inputs

    - `Optional<Type> type`

      - `CUSTOM("custom")`

  - `class ToolBash20250124:`

    - `JsonValue; name "bash"constant`

      Name of the tool.

      This is how the tool will be called by the model and in `tool_use` blocks.

      - `BASH("bash")`

    - `JsonValue; type "bash_20250124"constant`

      - `BASH_20250124("bash_20250124")`

    - `Optional<List<AllowedCaller>> allowedCallers`

      - `DIRECT("direct")`

      - `CODE_EXECUTION_20250825("code_execution_20250825")`

      - `CODE_EXECUTION_20260120("code_execution_20260120")`

    - `Optional<CacheControlEphemeral> cacheControl`

      Create a cache control breakpoint at this content block.

      - `JsonValue; type "ephemeral"constant`

        - `EPHEMERAL("ephemeral")`

      - `Optional<Ttl> ttl`

        The time-to-live for the cache control breakpoint.

        This may be one the following values:

        - `5m`: 5 minutes
        - `1h`: 1 hour

        Defaults to `5m`.

        - `TTL_5M("5m")`

        - `TTL_1H("1h")`

    - `Optional<Boolean> deferLoading`

      If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

    - `Optional<List<InputExample>> inputExamples`

    - `Optional<Boolean> strict`

      When true, guarantees schema validation on tool names and inputs

  - `class CodeExecutionTool20250522:`

    - `JsonValue; name "code_execution"constant`

      Name of the tool.

      This is how the tool will be called by the model and in `tool_use` blocks.

      - `CODE_EXECUTION("code_execution")`

    - `JsonValue; type "code_execution_20250522"constant`

      - `CODE_EXECUTION_20250522("code_execution_20250522")`

    - `Optional<List<AllowedCaller>> allowedCallers`

      - `DIRECT("direct")`

      - `CODE_EXECUTION_20250825("code_execution_20250825")`

      - `CODE_EXECUTION_20260120("code_execution_20260120")`

    - `Optional<CacheControlEphemeral> cacheControl`

      Create a cache control breakpoint at this content block.

      - `JsonValue; type "ephemeral"constant`

        - `EPHEMERAL("ephemeral")`

      - `Optional<Ttl> ttl`

        The time-to-live for the cache control breakpoint.

        This may be one the following values:

        - `5m`: 5 minutes
        - `1h`: 1 hour

        Defaults to `5m`.

        - `TTL_5M("5m")`

        - `TTL_1H("1h")`

    - `Optional<Boolean> deferLoading`

      If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

    - `Optional<Boolean> strict`

      When true, guarantees schema validation on tool names and inputs

  - `class CodeExecutionTool20250825:`

    - `JsonValue; name "code_execution"constant`

      Name of the tool.

      This is how the tool will be called by the model and in `tool_use` blocks.

      - `CODE_EXECUTION("code_execution")`

    - `JsonValue; type "code_execution_20250825"constant`

      - `CODE_EXECUTION_20250825("code_execution_20250825")`

    - `Optional<List<AllowedCaller>> allowedCallers`

      - `DIRECT("direct")`

      - `CODE_EXECUTION_20250825("code_execution_20250825")`

      - `CODE_EXECUTION_20260120("code_execution_20260120")`

    - `Optional<CacheControlEphemeral> cacheControl`

      Create a cache control breakpoint at this content block.

      - `JsonValue; type "ephemeral"constant`

        - `EPHEMERAL("ephemeral")`

      - `Optional<Ttl> ttl`

        The time-to-live for the cache control breakpoint.

        This may be one the following values:

        - `5m`: 5 minutes
        - `1h`: 1 hour

        Defaults to `5m`.

        - `TTL_5M("5m")`

        - `TTL_1H("1h")`

    - `Optional<Boolean> deferLoading`

      If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

    - `Optional<Boolean> strict`

      When true, guarantees schema validation on tool names and inputs

  - `class CodeExecutionTool20260120:`

    Code execution tool with REPL state persistence (daemon mode + gVisor checkpoint).

    - `JsonValue; name "code_execution"constant`

      Name of the tool.

      This is how the tool will be called by the model and in `tool_use` blocks.

      - `CODE_EXECUTION("code_execution")`

    - `JsonValue; type "code_execution_20260120"constant`

      - `CODE_EXECUTION_20260120("code_execution_20260120")`

    - `Optional<List<AllowedCaller>> allowedCallers`

      - `DIRECT("direct")`

      - `CODE_EXECUTION_20250825("code_execution_20250825")`

      - `CODE_EXECUTION_20260120("code_execution_20260120")`

    - `Optional<CacheControlEphemeral> cacheControl`

      Create a cache control breakpoint at this content block.

      - `JsonValue; type "ephemeral"constant`

        - `EPHEMERAL("ephemeral")`

      - `Optional<Ttl> ttl`

        The time-to-live for the cache control breakpoint.

        This may be one the following values:

        - `5m`: 5 minutes
        - `1h`: 1 hour

        Defaults to `5m`.

        - `TTL_5M("5m")`

        - `TTL_1H("1h")`

    - `Optional<Boolean> deferLoading`

      If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

    - `Optional<Boolean> strict`

      When true, guarantees schema validation on tool names and inputs

  - `class MemoryTool20250818:`

    - `JsonValue; name "memory"constant`

      Name of the tool.

      This is how the tool will be called by the model and in `tool_use` blocks.

      - `MEMORY("memory")`

    - `JsonValue; type "memory_20250818"constant`

      - `MEMORY_20250818("memory_20250818")`

    - `Optional<List<AllowedCaller>> allowedCallers`

      - `DIRECT("direct")`

      - `CODE_EXECUTION_20250825("code_execution_20250825")`

      - `CODE_EXECUTION_20260120("code_execution_20260120")`

    - `Optional<CacheControlEphemeral> cacheControl`

      Create a cache control breakpoint at this content block.

      - `JsonValue; type "ephemeral"constant`

        - `EPHEMERAL("ephemeral")`

      - `Optional<Ttl> ttl`

        The time-to-live for the cache control breakpoint.

        This may be one the following values:

        - `5m`: 5 minutes
        - `1h`: 1 hour

        Defaults to `5m`.

        - `TTL_5M("5m")`

        - `TTL_1H("1h")`

    - `Optional<Boolean> deferLoading`

      If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

    - `Optional<List<InputExample>> inputExamples`

    - `Optional<Boolean> strict`

      When true, guarantees schema validation on tool names and inputs

  - `class ToolTextEditor20250124:`

    - `JsonValue; name "str_replace_editor"constant`

      Name of the tool.

      This is how the tool will be called by the model and in `tool_use` blocks.

      - `STR_REPLACE_EDITOR("str_replace_editor")`

    - `JsonValue; type "text_editor_20250124"constant`

      - `TEXT_EDITOR_20250124("text_editor_20250124")`

    - `Optional<List<AllowedCaller>> allowedCallers`

      - `DIRECT("direct")`

      - `CODE_EXECUTION_20250825("code_execution_20250825")`

      - `CODE_EXECUTION_20260120("code_execution_20260120")`

    - `Optional<CacheControlEphemeral> cacheControl`

      Create a cache control breakpoint at this content block.

      - `JsonValue; type "ephemeral"constant`

        - `EPHEMERAL("ephemeral")`

      - `Optional<Ttl> ttl`

        The time-to-live for the cache control breakpoint.

        This may be one the following values:

        - `5m`: 5 minutes
        - `1h`: 1 hour

        Defaults to `5m`.

        - `TTL_5M("5m")`

        - `TTL_1H("1h")`

    - `Optional<Boolean> deferLoading`

      If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

    - `Optional<List<InputExample>> inputExamples`

    - `Optional<Boolean> strict`

      When true, guarantees schema validation on tool names and inputs

  - `class ToolTextEditor20250429:`

    - `JsonValue; name "str_replace_based_edit_tool"constant`

      Name of the tool.

      This is how the tool will be called by the model and in `tool_use` blocks.

      - `STR_REPLACE_BASED_EDIT_TOOL("str_replace_based_edit_tool")`

    - `JsonValue; type "text_editor_20250429"constant`

      - `TEXT_EDITOR_20250429("text_editor_20250429")`

    - `Optional<List<AllowedCaller>> allowedCallers`

      - `DIRECT("direct")`

      - `CODE_EXECUTION_20250825("code_execution_20250825")`

      - `CODE_EXECUTION_20260120("code_execution_20260120")`

    - `Optional<CacheControlEphemeral> cacheControl`

      Create a cache control breakpoint at this content block.

      - `JsonValue; type "ephemeral"constant`

        - `EPHEMERAL("ephemeral")`

      - `Optional<Ttl> ttl`

        The time-to-live for the cache control breakpoint.

        This may be one the following values:

        - `5m`: 5 minutes
        - `1h`: 1 hour

        Defaults to `5m`.

        - `TTL_5M("5m")`

        - `TTL_1H("1h")`

    - `Optional<Boolean> deferLoading`

      If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

    - `Optional<List<InputExample>> inputExamples`

    - `Optional<Boolean> strict`

      When true, guarantees schema validation on tool names and inputs

  - `class ToolTextEditor20250728:`

    - `JsonValue; name "str_replace_based_edit_tool"constant`

      Name of the tool.

      This is how the tool will be called by the model and in `tool_use` blocks.

      - `STR_REPLACE_BASED_EDIT_TOOL("str_replace_based_edit_tool")`

    - `JsonValue; type "text_editor_20250728"constant`

      - `TEXT_EDITOR_20250728("text_editor_20250728")`

    - `Optional<List<AllowedCaller>> allowedCallers`

      - `DIRECT("direct")`

      - `CODE_EXECUTION_20250825("code_execution_20250825")`

      - `CODE_EXECUTION_20260120("code_execution_20260120")`

    - `Optional<CacheControlEphemeral> cacheControl`

      Create a cache control breakpoint at this content block.

      - `JsonValue; type "ephemeral"constant`

        - `EPHEMERAL("ephemeral")`

      - `Optional<Ttl> ttl`

        The time-to-live for the cache control breakpoint.

        This may be one the following values:

        - `5m`: 5 minutes
        - `1h`: 1 hour

        Defaults to `5m`.

        - `TTL_5M("5m")`

        - `TTL_1H("1h")`

    - `Optional<Boolean> deferLoading`

      If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

    - `Optional<List<InputExample>> inputExamples`

    - `Optional<Long> maxCharacters`

      Maximum number of characters to display when viewing a file. If not specified, defaults to displaying the full file.

    - `Optional<Boolean> strict`

      When true, guarantees schema validation on tool names and inputs

  - `class WebSearchTool20250305:`

    - `JsonValue; name "web_search"constant`

      Name of the tool.

      This is how the tool will be called by the model and in `tool_use` blocks.

      - `WEB_SEARCH("web_search")`

    - `JsonValue; type "web_search_20250305"constant`

      - `WEB_SEARCH_20250305("web_search_20250305")`

    - `Optional<List<AllowedCaller>> allowedCallers`

      - `DIRECT("direct")`

      - `CODE_EXECUTION_20250825("code_execution_20250825")`

      - `CODE_EXECUTION_20260120("code_execution_20260120")`

    - `Optional<List<String>> allowedDomains`

      If provided, only these domains will be included in results. Cannot be used alongside `blocked_domains`.

    - `Optional<List<String>> blockedDomains`

      If provided, these domains will never appear in results. Cannot be used alongside `allowed_domains`.

    - `Optional<CacheControlEphemeral> cacheControl`

      Create a cache control breakpoint at this content block.

      - `JsonValue; type "ephemeral"constant`

        - `EPHEMERAL("ephemeral")`

      - `Optional<Ttl> ttl`

        The time-to-live for the cache control breakpoint.

        This may be one the following values:

        - `5m`: 5 minutes
        - `1h`: 1 hour

        Defaults to `5m`.

        - `TTL_5M("5m")`

        - `TTL_1H("1h")`

    - `Optional<Boolean> deferLoading`

      If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

    - `Optional<Long> maxUses`

      Maximum number of times the tool can be used in the API request.

    - `Optional<Boolean> strict`

      When true, guarantees schema validation on tool names and inputs

    - `Optional<UserLocation> userLocation`

      Parameters for the user's location. Used to provide more relevant search results.

      - `JsonValue; type "approximate"constant`

        - `APPROXIMATE("approximate")`

      - `Optional<String> city`

        The city of the user.

      - `Optional<String> country`

        The two letter [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) of the user.

      - `Optional<String> region`

        The region of the user.

      - `Optional<String> timezone`

        The [IANA timezone](https://nodatime.org/TimeZones) of the user.

  - `class WebFetchTool20250910:`

    - `JsonValue; name "web_fetch"constant`

      Name of the tool.

      This is how the tool will be called by the model and in `tool_use` blocks.

      - `WEB_FETCH("web_fetch")`

    - `JsonValue; type "web_fetch_20250910"constant`

      - `WEB_FETCH_20250910("web_fetch_20250910")`

    - `Optional<List<AllowedCaller>> allowedCallers`

      - `DIRECT("direct")`

      - `CODE_EXECUTION_20250825("code_execution_20250825")`

      - `CODE_EXECUTION_20260120("code_execution_20260120")`

    - `Optional<List<String>> allowedDomains`

      List of domains to allow fetching from

    - `Optional<List<String>> blockedDomains`

      List of domains to block fetching from

    - `Optional<CacheControlEphemeral> cacheControl`

      Create a cache control breakpoint at this content block.

      - `JsonValue; type "ephemeral"constant`

        - `EPHEMERAL("ephemeral")`

      - `Optional<Ttl> ttl`

        The time-to-live for the cache control breakpoint.

        This may be one the following values:

        - `5m`: 5 minutes
        - `1h`: 1 hour

        Defaults to `5m`.

        - `TTL_5M("5m")`

        - `TTL_1H("1h")`

    - `Optional<CitationsConfigParam> citations`

      Citations configuration for fetched documents. Citations are disabled by default.

      - `Optional<Boolean> enabled`

    - `Optional<Boolean> deferLoading`

      If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

    - `Optional<Long> maxContentTokens`

      Maximum number of tokens used by including web page text content in the context. The limit is approximate and does not apply to binary content such as PDFs.

    - `Optional<Long> maxUses`

      Maximum number of times the tool can be used in the API request.

    - `Optional<Boolean> strict`

      When true, guarantees schema validation on tool names and inputs

  - `class WebSearchTool20260209:`

    - `JsonValue; name "web_search"constant`

      Name of the tool.

      This is how the tool will be called by the model and in `tool_use` blocks.

      - `WEB_SEARCH("web_search")`

    - `JsonValue; type "web_search_20260209"constant`

      - `WEB_SEARCH_20260209("web_search_20260209")`

    - `Optional<List<AllowedCaller>> allowedCallers`

      - `DIRECT("direct")`

      - `CODE_EXECUTION_20250825("code_execution_20250825")`

      - `CODE_EXECUTION_20260120("code_execution_20260120")`

    - `Optional<List<String>> allowedDomains`

      If provided, only these domains will be included in results. Cannot be used alongside `blocked_domains`.

    - `Optional<List<String>> blockedDomains`

      If provided, these domains will never appear in results. Cannot be used alongside `allowed_domains`.

    - `Optional<CacheControlEphemeral> cacheControl`

      Create a cache control breakpoint at this content block.

      - `JsonValue; type "ephemeral"constant`

        - `EPHEMERAL("ephemeral")`

      - `Optional<Ttl> ttl`

        The time-to-live for the cache control breakpoint.

        This may be one the following values:

        - `5m`: 5 minutes
        - `1h`: 1 hour

        Defaults to `5m`.

        - `TTL_5M("5m")`

        - `TTL_1H("1h")`

    - `Optional<Boolean> deferLoading`

      If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

    - `Optional<Long> maxUses`

      Maximum number of times the tool can be used in the API request.

    - `Optional<Boolean> strict`

      When true, guarantees schema validation on tool names and inputs

    - `Optional<UserLocation> userLocation`

      Parameters for the user's location. Used to provide more relevant search results.

      - `JsonValue; type "approximate"constant`

        - `APPROXIMATE("approximate")`

      - `Optional<String> city`

        The city of the user.

      - `Optional<String> country`

        The two letter [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) of the user.

      - `Optional<String> region`

        The region of the user.

      - `Optional<String> timezone`

        The [IANA timezone](https://nodatime.org/TimeZones) of the user.

  - `class WebFetchTool20260209:`

    - `JsonValue; name "web_fetch"constant`

      Name of the tool.

      This is how the tool will be called by the model and in `tool_use` blocks.

      - `WEB_FETCH("web_fetch")`

    - `JsonValue; type "web_fetch_20260209"constant`

      - `WEB_FETCH_20260209("web_fetch_20260209")`

    - `Optional<List<AllowedCaller>> allowedCallers`

      - `DIRECT("direct")`

      - `CODE_EXECUTION_20250825("code_execution_20250825")`

      - `CODE_EXECUTION_20260120("code_execution_20260120")`

    - `Optional<List<String>> allowedDomains`

      List of domains to allow fetching from

    - `Optional<List<String>> blockedDomains`

      List of domains to block fetching from

    - `Optional<CacheControlEphemeral> cacheControl`

      Create a cache control breakpoint at this content block.

      - `JsonValue; type "ephemeral"constant`

        - `EPHEMERAL("ephemeral")`

      - `Optional<Ttl> ttl`

        The time-to-live for the cache control breakpoint.

        This may be one the following values:

        - `5m`: 5 minutes
        - `1h`: 1 hour

        Defaults to `5m`.

        - `TTL_5M("5m")`

        - `TTL_1H("1h")`

    - `Optional<CitationsConfigParam> citations`

      Citations configuration for fetched documents. Citations are disabled by default.

      - `Optional<Boolean> enabled`

    - `Optional<Boolean> deferLoading`

      If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

    - `Optional<Long> maxContentTokens`

      Maximum number of tokens used by including web page text content in the context. The limit is approximate and does not apply to binary content such as PDFs.

    - `Optional<Long> maxUses`

      Maximum number of times the tool can be used in the API request.

    - `Optional<Boolean> strict`

      When true, guarantees schema validation on tool names and inputs

  - `class ToolSearchToolBm25_20251119:`

    - `JsonValue; name "tool_search_tool_bm25"constant`

      Name of the tool.

      This is how the tool will be called by the model and in `tool_use` blocks.

      - `TOOL_SEARCH_TOOL_BM25("tool_search_tool_bm25")`

    - `Type type`

      - `TOOL_SEARCH_TOOL_BM25_20251119("tool_search_tool_bm25_20251119")`

      - `TOOL_SEARCH_TOOL_BM25("tool_search_tool_bm25")`

    - `Optional<List<AllowedCaller>> allowedCallers`

      - `DIRECT("direct")`

      - `CODE_EXECUTION_20250825("code_execution_20250825")`

      - `CODE_EXECUTION_20260120("code_execution_20260120")`

    - `Optional<CacheControlEphemeral> cacheControl`

      Create a cache control breakpoint at this content block.

      - `JsonValue; type "ephemeral"constant`

        - `EPHEMERAL("ephemeral")`

      - `Optional<Ttl> ttl`

        The time-to-live for the cache control breakpoint.

        This may be one the following values:

        - `5m`: 5 minutes
        - `1h`: 1 hour

        Defaults to `5m`.

        - `TTL_5M("5m")`

        - `TTL_1H("1h")`

    - `Optional<Boolean> deferLoading`

      If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

    - `Optional<Boolean> strict`

      When true, guarantees schema validation on tool names and inputs

  - `class ToolSearchToolRegex20251119:`

    - `JsonValue; name "tool_search_tool_regex"constant`

      Name of the tool.

      This is how the tool will be called by the model and in `tool_use` blocks.

      - `TOOL_SEARCH_TOOL_REGEX("tool_search_tool_regex")`

    - `Type type`

      - `TOOL_SEARCH_TOOL_REGEX_20251119("tool_search_tool_regex_20251119")`

      - `TOOL_SEARCH_TOOL_REGEX("tool_search_tool_regex")`

    - `Optional<List<AllowedCaller>> allowedCallers`

      - `DIRECT("direct")`

      - `CODE_EXECUTION_20250825("code_execution_20250825")`

      - `CODE_EXECUTION_20260120("code_execution_20260120")`

    - `Optional<CacheControlEphemeral> cacheControl`

      Create a cache control breakpoint at this content block.

      - `JsonValue; type "ephemeral"constant`

        - `EPHEMERAL("ephemeral")`

      - `Optional<Ttl> ttl`

        The time-to-live for the cache control breakpoint.

        This may be one the following values:

        - `5m`: 5 minutes
        - `1h`: 1 hour

        Defaults to `5m`.

        - `TTL_5M("5m")`

        - `TTL_1H("1h")`

    - `Optional<Boolean> deferLoading`

      If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

    - `Optional<Boolean> strict`

      When true, guarantees schema validation on tool names and inputs

### Tool Use Block

- `class ToolUseBlock:`

  - `String id`

  - `Caller caller`

    Tool invocation directly from the model.

    - `class DirectCaller:`

      Tool invocation directly from the model.

      - `JsonValue; type "direct"constant`

        - `DIRECT("direct")`

    - `class ServerToolCaller:`

      Tool invocation generated by a server-side tool.

      - `String toolId`

      - `JsonValue; type "code_execution_20250825"constant`

        - `CODE_EXECUTION_20250825("code_execution_20250825")`

    - `class ServerToolCaller20260120:`

      - `String toolId`

      - `JsonValue; type "code_execution_20260120"constant`

        - `CODE_EXECUTION_20260120("code_execution_20260120")`

  - `Input input`

  - `String name`

  - `JsonValue; type "tool_use"constant`

    - `TOOL_USE("tool_use")`

### Tool Use Block Param

- `class ToolUseBlockParam:`

  - `String id`

  - `Input input`

  - `String name`

  - `JsonValue; type "tool_use"constant`

    - `TOOL_USE("tool_use")`

  - `Optional<CacheControlEphemeral> cacheControl`

    Create a cache control breakpoint at this content block.

    - `JsonValue; type "ephemeral"constant`

      - `EPHEMERAL("ephemeral")`

    - `Optional<Ttl> ttl`

      The time-to-live for the cache control breakpoint.

      This may be one the following values:

      - `5m`: 5 minutes
      - `1h`: 1 hour

      Defaults to `5m`.

      - `TTL_5M("5m")`

      - `TTL_1H("1h")`

  - `Optional<Caller> caller`

    Tool invocation directly from the model.

    - `class DirectCaller:`

      Tool invocation directly from the model.

      - `JsonValue; type "direct"constant`

        - `DIRECT("direct")`

    - `class ServerToolCaller:`

      Tool invocation generated by a server-side tool.

      - `String toolId`

      - `JsonValue; type "code_execution_20250825"constant`

        - `CODE_EXECUTION_20250825("code_execution_20250825")`

    - `class ServerToolCaller20260120:`

      - `String toolId`

      - `JsonValue; type "code_execution_20260120"constant`

        - `CODE_EXECUTION_20260120("code_execution_20260120")`

### URL Image Source

- `class UrlImageSource:`

  - `JsonValue; type "url"constant`

    - `URL("url")`

  - `String url`

### URL PDF Source

- `class UrlPdfSource:`

  - `JsonValue; type "url"constant`

    - `URL("url")`

  - `String url`

### Usage

- `class Usage:`

  - `Optional<CacheCreation> cacheCreation`

    Breakdown of cached tokens by TTL

    - `long ephemeral1hInputTokens`

      The number of input tokens used to create the 1 hour cache entry.

    - `long ephemeral5mInputTokens`

      The number of input tokens used to create the 5 minute cache entry.

  - `Optional<Long> cacheCreationInputTokens`

    The number of input tokens used to create the cache entry.

  - `Optional<Long> cacheReadInputTokens`

    The number of input tokens read from the cache.

  - `Optional<String> inferenceGeo`

    The geographic region where inference was performed for this request.

  - `long inputTokens`

    The number of input tokens which were used.

  - `long outputTokens`

    The number of output tokens which were used.

  - `Optional<ServerToolUsage> serverToolUse`

    The number of server tool requests.

    - `long webFetchRequests`

      The number of web fetch tool requests.

    - `long webSearchRequests`

      The number of web search tool requests.

  - `Optional<ServiceTier> serviceTier`

    If the request used the priority, standard, or batch tier.

    - `STANDARD("standard")`

    - `PRIORITY("priority")`

    - `BATCH("batch")`

### User Location

- `class UserLocation:`

  - `JsonValue; type "approximate"constant`

    - `APPROXIMATE("approximate")`

  - `Optional<String> city`

    The city of the user.

  - `Optional<String> country`

    The two letter [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) of the user.

  - `Optional<String> region`

    The region of the user.

  - `Optional<String> timezone`

    The [IANA timezone](https://nodatime.org/TimeZones) of the user.

### Web Fetch Block

- `class WebFetchBlock:`

  - `DocumentBlock content`

    - `Optional<CitationsConfig> citations`

      Citation configuration for the document

      - `boolean enabled`

    - `Source source`

      - `class Base64PdfSource:`

        - `String data`

        - `JsonValue; mediaType "application/pdf"constant`

          - `APPLICATION_PDF("application/pdf")`

        - `JsonValue; type "base64"constant`

          - `BASE64("base64")`

      - `class PlainTextSource:`

        - `String data`

        - `JsonValue; mediaType "text/plain"constant`

          - `TEXT_PLAIN("text/plain")`

        - `JsonValue; type "text"constant`

          - `TEXT("text")`

    - `Optional<String> title`

      The title of the document

    - `JsonValue; type "document"constant`

      - `DOCUMENT("document")`

  - `Optional<String> retrievedAt`

    ISO 8601 timestamp when the content was retrieved

  - `JsonValue; type "web_fetch_result"constant`

    - `WEB_FETCH_RESULT("web_fetch_result")`

  - `String url`

    Fetched content URL

### Web Fetch Block Param

- `class WebFetchBlockParam:`

  - `DocumentBlockParam content`

    - `Source source`

      - `class Base64PdfSource:`

        - `String data`

        - `JsonValue; mediaType "application/pdf"constant`

          - `APPLICATION_PDF("application/pdf")`

        - `JsonValue; type "base64"constant`

          - `BASE64("base64")`

      - `class PlainTextSource:`

        - `String data`

        - `JsonValue; mediaType "text/plain"constant`

          - `TEXT_PLAIN("text/plain")`

        - `JsonValue; type "text"constant`

          - `TEXT("text")`

      - `class ContentBlockSource:`

        - `Content content`

          - `String`

          - `List<ContentBlockSourceContent>`

            - `class TextBlockParam:`

              - `String text`

              - `JsonValue; type "text"constant`

                - `TEXT("text")`

              - `Optional<CacheControlEphemeral> cacheControl`

                Create a cache control breakpoint at this content block.

                - `JsonValue; type "ephemeral"constant`

                  - `EPHEMERAL("ephemeral")`

                - `Optional<Ttl> ttl`

                  The time-to-live for the cache control breakpoint.

                  This may be one the following values:

                  - `5m`: 5 minutes
                  - `1h`: 1 hour

                  Defaults to `5m`.

                  - `TTL_5M("5m")`

                  - `TTL_1H("1h")`

              - `Optional<List<TextCitationParam>> citations`

                - `class CitationCharLocationParam:`

                  - `String citedText`

                  - `long documentIndex`

                  - `Optional<String> documentTitle`

                  - `long endCharIndex`

                  - `long startCharIndex`

                  - `JsonValue; type "char_location"constant`

                    - `CHAR_LOCATION("char_location")`

                - `class CitationPageLocationParam:`

                  - `String citedText`

                  - `long documentIndex`

                  - `Optional<String> documentTitle`

                  - `long endPageNumber`

                  - `long startPageNumber`

                  - `JsonValue; type "page_location"constant`

                    - `PAGE_LOCATION("page_location")`

                - `class CitationContentBlockLocationParam:`

                  - `String citedText`

                  - `long documentIndex`

                  - `Optional<String> documentTitle`

                  - `long endBlockIndex`

                  - `long startBlockIndex`

                  - `JsonValue; type "content_block_location"constant`

                    - `CONTENT_BLOCK_LOCATION("content_block_location")`

                - `class CitationWebSearchResultLocationParam:`

                  - `String citedText`

                  - `String encryptedIndex`

                  - `Optional<String> title`

                  - `JsonValue; type "web_search_result_location"constant`

                    - `WEB_SEARCH_RESULT_LOCATION("web_search_result_location")`

                  - `String url`

                - `class CitationSearchResultLocationParam:`

                  - `String citedText`

                  - `long endBlockIndex`

                  - `long searchResultIndex`

                  - `String source`

                  - `long startBlockIndex`

                  - `Optional<String> title`

                  - `JsonValue; type "search_result_location"constant`

                    - `SEARCH_RESULT_LOCATION("search_result_location")`

            - `class ImageBlockParam:`

              - `Source source`

                - `class Base64ImageSource:`

                  - `String data`

                  - `MediaType mediaType`

                    - `IMAGE_JPEG("image/jpeg")`

                    - `IMAGE_PNG("image/png")`

                    - `IMAGE_GIF("image/gif")`

                    - `IMAGE_WEBP("image/webp")`

                  - `JsonValue; type "base64"constant`

                    - `BASE64("base64")`

                - `class UrlImageSource:`

                  - `JsonValue; type "url"constant`

                    - `URL("url")`

                  - `String url`

              - `JsonValue; type "image"constant`

                - `IMAGE("image")`

              - `Optional<CacheControlEphemeral> cacheControl`

                Create a cache control breakpoint at this content block.

                - `JsonValue; type "ephemeral"constant`

                  - `EPHEMERAL("ephemeral")`

                - `Optional<Ttl> ttl`

                  The time-to-live for the cache control breakpoint.

                  This may be one the following values:

                  - `5m`: 5 minutes
                  - `1h`: 1 hour

                  Defaults to `5m`.

                  - `TTL_5M("5m")`

                  - `TTL_1H("1h")`

        - `JsonValue; type "content"constant`

          - `CONTENT("content")`

      - `class UrlPdfSource:`

        - `JsonValue; type "url"constant`

          - `URL("url")`

        - `String url`

    - `JsonValue; type "document"constant`

      - `DOCUMENT("document")`

    - `Optional<CacheControlEphemeral> cacheControl`

      Create a cache control breakpoint at this content block.

      - `JsonValue; type "ephemeral"constant`

        - `EPHEMERAL("ephemeral")`

      - `Optional<Ttl> ttl`

        The time-to-live for the cache control breakpoint.

        This may be one the following values:

        - `5m`: 5 minutes
        - `1h`: 1 hour

        Defaults to `5m`.

        - `TTL_5M("5m")`

        - `TTL_1H("1h")`

    - `Optional<CitationsConfigParam> citations`

      - `Optional<Boolean> enabled`

    - `Optional<String> context`

    - `Optional<String> title`

  - `JsonValue; type "web_fetch_result"constant`

    - `WEB_FETCH_RESULT("web_fetch_result")`

  - `String url`

    Fetched content URL

  - `Optional<String> retrievedAt`

    ISO 8601 timestamp when the content was retrieved

### Web Fetch Tool 20250910

- `class WebFetchTool20250910:`

  - `JsonValue; name "web_fetch"constant`

    Name of the tool.

    This is how the tool will be called by the model and in `tool_use` blocks.

    - `WEB_FETCH("web_fetch")`

  - `JsonValue; type "web_fetch_20250910"constant`

    - `WEB_FETCH_20250910("web_fetch_20250910")`

  - `Optional<List<AllowedCaller>> allowedCallers`

    - `DIRECT("direct")`

    - `CODE_EXECUTION_20250825("code_execution_20250825")`

    - `CODE_EXECUTION_20260120("code_execution_20260120")`

  - `Optional<List<String>> allowedDomains`

    List of domains to allow fetching from

  - `Optional<List<String>> blockedDomains`

    List of domains to block fetching from

  - `Optional<CacheControlEphemeral> cacheControl`

    Create a cache control breakpoint at this content block.

    - `JsonValue; type "ephemeral"constant`

      - `EPHEMERAL("ephemeral")`

    - `Optional<Ttl> ttl`

      The time-to-live for the cache control breakpoint.

      This may be one the following values:

      - `5m`: 5 minutes
      - `1h`: 1 hour

      Defaults to `5m`.

      - `TTL_5M("5m")`

      - `TTL_1H("1h")`

  - `Optional<CitationsConfigParam> citations`

    Citations configuration for fetched documents. Citations are disabled by default.

    - `Optional<Boolean> enabled`

  - `Optional<Boolean> deferLoading`

    If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

  - `Optional<Long> maxContentTokens`

    Maximum number of tokens used by including web page text content in the context. The limit is approximate and does not apply to binary content such as PDFs.

  - `Optional<Long> maxUses`

    Maximum number of times the tool can be used in the API request.

  - `Optional<Boolean> strict`

    When true, guarantees schema validation on tool names and inputs

### Web Fetch Tool 20260209

- `class WebFetchTool20260209:`

  - `JsonValue; name "web_fetch"constant`

    Name of the tool.

    This is how the tool will be called by the model and in `tool_use` blocks.

    - `WEB_FETCH("web_fetch")`

  - `JsonValue; type "web_fetch_20260209"constant`

    - `WEB_FETCH_20260209("web_fetch_20260209")`

  - `Optional<List<AllowedCaller>> allowedCallers`

    - `DIRECT("direct")`

    - `CODE_EXECUTION_20250825("code_execution_20250825")`

    - `CODE_EXECUTION_20260120("code_execution_20260120")`

  - `Optional<List<String>> allowedDomains`

    List of domains to allow fetching from

  - `Optional<List<String>> blockedDomains`

    List of domains to block fetching from

  - `Optional<CacheControlEphemeral> cacheControl`

    Create a cache control breakpoint at this content block.

    - `JsonValue; type "ephemeral"constant`

      - `EPHEMERAL("ephemeral")`

    - `Optional<Ttl> ttl`

      The time-to-live for the cache control breakpoint.

      This may be one the following values:

      - `5m`: 5 minutes
      - `1h`: 1 hour

      Defaults to `5m`.

      - `TTL_5M("5m")`

      - `TTL_1H("1h")`

  - `Optional<CitationsConfigParam> citations`

    Citations configuration for fetched documents. Citations are disabled by default.

    - `Optional<Boolean> enabled`

  - `Optional<Boolean> deferLoading`

    If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

  - `Optional<Long> maxContentTokens`

    Maximum number of tokens used by including web page text content in the context. The limit is approximate and does not apply to binary content such as PDFs.

  - `Optional<Long> maxUses`

    Maximum number of times the tool can be used in the API request.

  - `Optional<Boolean> strict`

    When true, guarantees schema validation on tool names and inputs

### Web Fetch Tool Result Block

- `class WebFetchToolResultBlock:`

  - `Caller caller`

    Tool invocation directly from the model.

    - `class DirectCaller:`

      Tool invocation directly from the model.

      - `JsonValue; type "direct"constant`

        - `DIRECT("direct")`

    - `class ServerToolCaller:`

      Tool invocation generated by a server-side tool.

      - `String toolId`

      - `JsonValue; type "code_execution_20250825"constant`

        - `CODE_EXECUTION_20250825("code_execution_20250825")`

    - `class ServerToolCaller20260120:`

      - `String toolId`

      - `JsonValue; type "code_execution_20260120"constant`

        - `CODE_EXECUTION_20260120("code_execution_20260120")`

  - `Content content`

    - `class WebFetchToolResultErrorBlock:`

      - `WebFetchToolResultErrorCode errorCode`

        - `INVALID_TOOL_INPUT("invalid_tool_input")`

        - `URL_TOO_LONG("url_too_long")`

        - `URL_NOT_ALLOWED("url_not_allowed")`

        - `URL_NOT_ACCESSIBLE("url_not_accessible")`

        - `UNSUPPORTED_CONTENT_TYPE("unsupported_content_type")`

        - `TOO_MANY_REQUESTS("too_many_requests")`

        - `MAX_USES_EXCEEDED("max_uses_exceeded")`

        - `UNAVAILABLE("unavailable")`

      - `JsonValue; type "web_fetch_tool_result_error"constant`

        - `WEB_FETCH_TOOL_RESULT_ERROR("web_fetch_tool_result_error")`

    - `class WebFetchBlock:`

      - `DocumentBlock content`

        - `Optional<CitationsConfig> citations`

          Citation configuration for the document

          - `boolean enabled`

        - `Source source`

          - `class Base64PdfSource:`

            - `String data`

            - `JsonValue; mediaType "application/pdf"constant`

              - `APPLICATION_PDF("application/pdf")`

            - `JsonValue; type "base64"constant`

              - `BASE64("base64")`

          - `class PlainTextSource:`

            - `String data`

            - `JsonValue; mediaType "text/plain"constant`

              - `TEXT_PLAIN("text/plain")`

            - `JsonValue; type "text"constant`

              - `TEXT("text")`

        - `Optional<String> title`

          The title of the document

        - `JsonValue; type "document"constant`

          - `DOCUMENT("document")`

      - `Optional<String> retrievedAt`

        ISO 8601 timestamp when the content was retrieved

      - `JsonValue; type "web_fetch_result"constant`

        - `WEB_FETCH_RESULT("web_fetch_result")`

      - `String url`

        Fetched content URL

  - `String toolUseId`

  - `JsonValue; type "web_fetch_tool_result"constant`

    - `WEB_FETCH_TOOL_RESULT("web_fetch_tool_result")`

### Web Fetch Tool Result Block Param

- `class WebFetchToolResultBlockParam:`

  - `Content content`

    - `class WebFetchToolResultErrorBlockParam:`

      - `WebFetchToolResultErrorCode errorCode`

        - `INVALID_TOOL_INPUT("invalid_tool_input")`

        - `URL_TOO_LONG("url_too_long")`

        - `URL_NOT_ALLOWED("url_not_allowed")`

        - `URL_NOT_ACCESSIBLE("url_not_accessible")`

        - `UNSUPPORTED_CONTENT_TYPE("unsupported_content_type")`

        - `TOO_MANY_REQUESTS("too_many_requests")`

        - `MAX_USES_EXCEEDED("max_uses_exceeded")`

        - `UNAVAILABLE("unavailable")`

      - `JsonValue; type "web_fetch_tool_result_error"constant`

        - `WEB_FETCH_TOOL_RESULT_ERROR("web_fetch_tool_result_error")`

    - `class WebFetchBlockParam:`

      - `DocumentBlockParam content`

        - `Source source`

          - `class Base64PdfSource:`

            - `String data`

            - `JsonValue; mediaType "application/pdf"constant`

              - `APPLICATION_PDF("application/pdf")`

            - `JsonValue; type "base64"constant`

              - `BASE64("base64")`

          - `class PlainTextSource:`

            - `String data`

            - `JsonValue; mediaType "text/plain"constant`

              - `TEXT_PLAIN("text/plain")`

            - `JsonValue; type "text"constant`

              - `TEXT("text")`

          - `class ContentBlockSource:`

            - `Content content`

              - `String`

              - `List<ContentBlockSourceContent>`

                - `class TextBlockParam:`

                  - `String text`

                  - `JsonValue; type "text"constant`

                    - `TEXT("text")`

                  - `Optional<CacheControlEphemeral> cacheControl`

                    Create a cache control breakpoint at this content block.

                    - `JsonValue; type "ephemeral"constant`

                      - `EPHEMERAL("ephemeral")`

                    - `Optional<Ttl> ttl`

                      The time-to-live for the cache control breakpoint.

                      This may be one the following values:

                      - `5m`: 5 minutes
                      - `1h`: 1 hour

                      Defaults to `5m`.

                      - `TTL_5M("5m")`

                      - `TTL_1H("1h")`

                  - `Optional<List<TextCitationParam>> citations`

                    - `class CitationCharLocationParam:`

                      - `String citedText`

                      - `long documentIndex`

                      - `Optional<String> documentTitle`

                      - `long endCharIndex`

                      - `long startCharIndex`

                      - `JsonValue; type "char_location"constant`

                        - `CHAR_LOCATION("char_location")`

                    - `class CitationPageLocationParam:`

                      - `String citedText`

                      - `long documentIndex`

                      - `Optional<String> documentTitle`

                      - `long endPageNumber`

                      - `long startPageNumber`

                      - `JsonValue; type "page_location"constant`

                        - `PAGE_LOCATION("page_location")`

                    - `class CitationContentBlockLocationParam:`

                      - `String citedText`

                      - `long documentIndex`

                      - `Optional<String> documentTitle`

                      - `long endBlockIndex`

                      - `long startBlockIndex`

                      - `JsonValue; type "content_block_location"constant`

                        - `CONTENT_BLOCK_LOCATION("content_block_location")`

                    - `class CitationWebSearchResultLocationParam:`

                      - `String citedText`

                      - `String encryptedIndex`

                      - `Optional<String> title`

                      - `JsonValue; type "web_search_result_location"constant`

                        - `WEB_SEARCH_RESULT_LOCATION("web_search_result_location")`

                      - `String url`

                    - `class CitationSearchResultLocationParam:`

                      - `String citedText`

                      - `long endBlockIndex`

                      - `long searchResultIndex`

                      - `String source`

                      - `long startBlockIndex`

                      - `Optional<String> title`

                      - `JsonValue; type "search_result_location"constant`

                        - `SEARCH_RESULT_LOCATION("search_result_location")`

                - `class ImageBlockParam:`

                  - `Source source`

                    - `class Base64ImageSource:`

                      - `String data`

                      - `MediaType mediaType`

                        - `IMAGE_JPEG("image/jpeg")`

                        - `IMAGE_PNG("image/png")`

                        - `IMAGE_GIF("image/gif")`

                        - `IMAGE_WEBP("image/webp")`

                      - `JsonValue; type "base64"constant`

                        - `BASE64("base64")`

                    - `class UrlImageSource:`

                      - `JsonValue; type "url"constant`

                        - `URL("url")`

                      - `String url`

                  - `JsonValue; type "image"constant`

                    - `IMAGE("image")`

                  - `Optional<CacheControlEphemeral> cacheControl`

                    Create a cache control breakpoint at this content block.

                    - `JsonValue; type "ephemeral"constant`

                      - `EPHEMERAL("ephemeral")`

                    - `Optional<Ttl> ttl`

                      The time-to-live for the cache control breakpoint.

                      This may be one the following values:

                      - `5m`: 5 minutes
                      - `1h`: 1 hour

                      Defaults to `5m`.

                      - `TTL_5M("5m")`

                      - `TTL_1H("1h")`

            - `JsonValue; type "content"constant`

              - `CONTENT("content")`

          - `class UrlPdfSource:`

            - `JsonValue; type "url"constant`

              - `URL("url")`

            - `String url`

        - `JsonValue; type "document"constant`

          - `DOCUMENT("document")`

        - `Optional<CacheControlEphemeral> cacheControl`

          Create a cache control breakpoint at this content block.

          - `JsonValue; type "ephemeral"constant`

            - `EPHEMERAL("ephemeral")`

          - `Optional<Ttl> ttl`

            The time-to-live for the cache control breakpoint.

            This may be one the following values:

            - `5m`: 5 minutes
            - `1h`: 1 hour

            Defaults to `5m`.

            - `TTL_5M("5m")`

            - `TTL_1H("1h")`

        - `Optional<CitationsConfigParam> citations`

          - `Optional<Boolean> enabled`

        - `Optional<String> context`

        - `Optional<String> title`

      - `JsonValue; type "web_fetch_result"constant`

        - `WEB_FETCH_RESULT("web_fetch_result")`

      - `String url`

        Fetched content URL

      - `Optional<String> retrievedAt`

        ISO 8601 timestamp when the content was retrieved

  - `String toolUseId`

  - `JsonValue; type "web_fetch_tool_result"constant`

    - `WEB_FETCH_TOOL_RESULT("web_fetch_tool_result")`

  - `Optional<CacheControlEphemeral> cacheControl`

    Create a cache control breakpoint at this content block.

    - `JsonValue; type "ephemeral"constant`

      - `EPHEMERAL("ephemeral")`

    - `Optional<Ttl> ttl`

      The time-to-live for the cache control breakpoint.

      This may be one the following values:

      - `5m`: 5 minutes
      - `1h`: 1 hour

      Defaults to `5m`.

      - `TTL_5M("5m")`

      - `TTL_1H("1h")`

  - `Optional<Caller> caller`

    Tool invocation directly from the model.

    - `class DirectCaller:`

      Tool invocation directly from the model.

      - `JsonValue; type "direct"constant`

        - `DIRECT("direct")`

    - `class ServerToolCaller:`

      Tool invocation generated by a server-side tool.

      - `String toolId`

      - `JsonValue; type "code_execution_20250825"constant`

        - `CODE_EXECUTION_20250825("code_execution_20250825")`

    - `class ServerToolCaller20260120:`

      - `String toolId`

      - `JsonValue; type "code_execution_20260120"constant`

        - `CODE_EXECUTION_20260120("code_execution_20260120")`

### Web Fetch Tool Result Error Block

- `class WebFetchToolResultErrorBlock:`

  - `WebFetchToolResultErrorCode errorCode`

    - `INVALID_TOOL_INPUT("invalid_tool_input")`

    - `URL_TOO_LONG("url_too_long")`

    - `URL_NOT_ALLOWED("url_not_allowed")`

    - `URL_NOT_ACCESSIBLE("url_not_accessible")`

    - `UNSUPPORTED_CONTENT_TYPE("unsupported_content_type")`

    - `TOO_MANY_REQUESTS("too_many_requests")`

    - `MAX_USES_EXCEEDED("max_uses_exceeded")`

    - `UNAVAILABLE("unavailable")`

  - `JsonValue; type "web_fetch_tool_result_error"constant`

    - `WEB_FETCH_TOOL_RESULT_ERROR("web_fetch_tool_result_error")`

### Web Fetch Tool Result Error Block Param

- `class WebFetchToolResultErrorBlockParam:`

  - `WebFetchToolResultErrorCode errorCode`

    - `INVALID_TOOL_INPUT("invalid_tool_input")`

    - `URL_TOO_LONG("url_too_long")`

    - `URL_NOT_ALLOWED("url_not_allowed")`

    - `URL_NOT_ACCESSIBLE("url_not_accessible")`

    - `UNSUPPORTED_CONTENT_TYPE("unsupported_content_type")`

    - `TOO_MANY_REQUESTS("too_many_requests")`

    - `MAX_USES_EXCEEDED("max_uses_exceeded")`

    - `UNAVAILABLE("unavailable")`

  - `JsonValue; type "web_fetch_tool_result_error"constant`

    - `WEB_FETCH_TOOL_RESULT_ERROR("web_fetch_tool_result_error")`

### Web Fetch Tool Result Error Code

- `enum WebFetchToolResultErrorCode:`

  - `INVALID_TOOL_INPUT("invalid_tool_input")`

  - `URL_TOO_LONG("url_too_long")`

  - `URL_NOT_ALLOWED("url_not_allowed")`

  - `URL_NOT_ACCESSIBLE("url_not_accessible")`

  - `UNSUPPORTED_CONTENT_TYPE("unsupported_content_type")`

  - `TOO_MANY_REQUESTS("too_many_requests")`

  - `MAX_USES_EXCEEDED("max_uses_exceeded")`

  - `UNAVAILABLE("unavailable")`

### Web Search Result Block

- `class WebSearchResultBlock:`

  - `String encryptedContent`

  - `Optional<String> pageAge`

  - `String title`

  - `JsonValue; type "web_search_result"constant`

    - `WEB_SEARCH_RESULT("web_search_result")`

  - `String url`

### Web Search Result Block Param

- `class WebSearchResultBlockParam:`

  - `String encryptedContent`

  - `String title`

  - `JsonValue; type "web_search_result"constant`

    - `WEB_SEARCH_RESULT("web_search_result")`

  - `String url`

  - `Optional<String> pageAge`

### Web Search Tool 20250305

- `class WebSearchTool20250305:`

  - `JsonValue; name "web_search"constant`

    Name of the tool.

    This is how the tool will be called by the model and in `tool_use` blocks.

    - `WEB_SEARCH("web_search")`

  - `JsonValue; type "web_search_20250305"constant`

    - `WEB_SEARCH_20250305("web_search_20250305")`

  - `Optional<List<AllowedCaller>> allowedCallers`

    - `DIRECT("direct")`

    - `CODE_EXECUTION_20250825("code_execution_20250825")`

    - `CODE_EXECUTION_20260120("code_execution_20260120")`

  - `Optional<List<String>> allowedDomains`

    If provided, only these domains will be included in results. Cannot be used alongside `blocked_domains`.

  - `Optional<List<String>> blockedDomains`

    If provided, these domains will never appear in results. Cannot be used alongside `allowed_domains`.

  - `Optional<CacheControlEphemeral> cacheControl`

    Create a cache control breakpoint at this content block.

    - `JsonValue; type "ephemeral"constant`

      - `EPHEMERAL("ephemeral")`

    - `Optional<Ttl> ttl`

      The time-to-live for the cache control breakpoint.

      This may be one the following values:

      - `5m`: 5 minutes
      - `1h`: 1 hour

      Defaults to `5m`.

      - `TTL_5M("5m")`

      - `TTL_1H("1h")`

  - `Optional<Boolean> deferLoading`

    If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

  - `Optional<Long> maxUses`

    Maximum number of times the tool can be used in the API request.

  - `Optional<Boolean> strict`

    When true, guarantees schema validation on tool names and inputs

  - `Optional<UserLocation> userLocation`

    Parameters for the user's location. Used to provide more relevant search results.

    - `JsonValue; type "approximate"constant`

      - `APPROXIMATE("approximate")`

    - `Optional<String> city`

      The city of the user.

    - `Optional<String> country`

      The two letter [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) of the user.

    - `Optional<String> region`

      The region of the user.

    - `Optional<String> timezone`

      The [IANA timezone](https://nodatime.org/TimeZones) of the user.

### Web Search Tool 20260209

- `class WebSearchTool20260209:`

  - `JsonValue; name "web_search"constant`

    Name of the tool.

    This is how the tool will be called by the model and in `tool_use` blocks.

    - `WEB_SEARCH("web_search")`

  - `JsonValue; type "web_search_20260209"constant`

    - `WEB_SEARCH_20260209("web_search_20260209")`

  - `Optional<List<AllowedCaller>> allowedCallers`

    - `DIRECT("direct")`

    - `CODE_EXECUTION_20250825("code_execution_20250825")`

    - `CODE_EXECUTION_20260120("code_execution_20260120")`

  - `Optional<List<String>> allowedDomains`

    If provided, only these domains will be included in results. Cannot be used alongside `blocked_domains`.

  - `Optional<List<String>> blockedDomains`

    If provided, these domains will never appear in results. Cannot be used alongside `allowed_domains`.

  - `Optional<CacheControlEphemeral> cacheControl`

    Create a cache control breakpoint at this content block.

    - `JsonValue; type "ephemeral"constant`

      - `EPHEMERAL("ephemeral")`

    - `Optional<Ttl> ttl`

      The time-to-live for the cache control breakpoint.

      This may be one the following values:

      - `5m`: 5 minutes
      - `1h`: 1 hour

      Defaults to `5m`.

      - `TTL_5M("5m")`

      - `TTL_1H("1h")`

  - `Optional<Boolean> deferLoading`

    If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

  - `Optional<Long> maxUses`

    Maximum number of times the tool can be used in the API request.

  - `Optional<Boolean> strict`

    When true, guarantees schema validation on tool names and inputs

  - `Optional<UserLocation> userLocation`

    Parameters for the user's location. Used to provide more relevant search results.

    - `JsonValue; type "approximate"constant`

      - `APPROXIMATE("approximate")`

    - `Optional<String> city`

      The city of the user.

    - `Optional<String> country`

      The two letter [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) of the user.

    - `Optional<String> region`

      The region of the user.

    - `Optional<String> timezone`

      The [IANA timezone](https://nodatime.org/TimeZones) of the user.

### Web Search Tool Request Error

- `class WebSearchToolRequestError:`

  - `WebSearchToolResultErrorCode errorCode`

    - `INVALID_TOOL_INPUT("invalid_tool_input")`

    - `UNAVAILABLE("unavailable")`

    - `MAX_USES_EXCEEDED("max_uses_exceeded")`

    - `TOO_MANY_REQUESTS("too_many_requests")`

    - `QUERY_TOO_LONG("query_too_long")`

    - `REQUEST_TOO_LARGE("request_too_large")`

  - `JsonValue; type "web_search_tool_result_error"constant`

    - `WEB_SEARCH_TOOL_RESULT_ERROR("web_search_tool_result_error")`

### Web Search Tool Result Block

- `class WebSearchToolResultBlock:`

  - `Caller caller`

    Tool invocation directly from the model.

    - `class DirectCaller:`

      Tool invocation directly from the model.

      - `JsonValue; type "direct"constant`

        - `DIRECT("direct")`

    - `class ServerToolCaller:`

      Tool invocation generated by a server-side tool.

      - `String toolId`

      - `JsonValue; type "code_execution_20250825"constant`

        - `CODE_EXECUTION_20250825("code_execution_20250825")`

    - `class ServerToolCaller20260120:`

      - `String toolId`

      - `JsonValue; type "code_execution_20260120"constant`

        - `CODE_EXECUTION_20260120("code_execution_20260120")`

  - `WebSearchToolResultBlockContent content`

    - `class WebSearchToolResultError:`

      - `WebSearchToolResultErrorCode errorCode`

        - `INVALID_TOOL_INPUT("invalid_tool_input")`

        - `UNAVAILABLE("unavailable")`

        - `MAX_USES_EXCEEDED("max_uses_exceeded")`

        - `TOO_MANY_REQUESTS("too_many_requests")`

        - `QUERY_TOO_LONG("query_too_long")`

        - `REQUEST_TOO_LARGE("request_too_large")`

      - `JsonValue; type "web_search_tool_result_error"constant`

        - `WEB_SEARCH_TOOL_RESULT_ERROR("web_search_tool_result_error")`

    - `List<WebSearchResultBlock>`

      - `String encryptedContent`

      - `Optional<String> pageAge`

      - `String title`

      - `JsonValue; type "web_search_result"constant`

        - `WEB_SEARCH_RESULT("web_search_result")`

      - `String url`

  - `String toolUseId`

  - `JsonValue; type "web_search_tool_result"constant`

    - `WEB_SEARCH_TOOL_RESULT("web_search_tool_result")`

### Web Search Tool Result Block Content

- `class WebSearchToolResultBlockContent: A class that can be one of several variants.union`

  - `class WebSearchToolResultError:`

    - `WebSearchToolResultErrorCode errorCode`

      - `INVALID_TOOL_INPUT("invalid_tool_input")`

      - `UNAVAILABLE("unavailable")`

      - `MAX_USES_EXCEEDED("max_uses_exceeded")`

      - `TOO_MANY_REQUESTS("too_many_requests")`

      - `QUERY_TOO_LONG("query_too_long")`

      - `REQUEST_TOO_LARGE("request_too_large")`

    - `JsonValue; type "web_search_tool_result_error"constant`

      - `WEB_SEARCH_TOOL_RESULT_ERROR("web_search_tool_result_error")`

  - `List<WebSearchResultBlock>`

    - `String encryptedContent`

    - `Optional<String> pageAge`

    - `String title`

    - `JsonValue; type "web_search_result"constant`

      - `WEB_SEARCH_RESULT("web_search_result")`

    - `String url`

### Web Search Tool Result Block Param

- `class WebSearchToolResultBlockParam:`

  - `WebSearchToolResultBlockParamContent content`

    - `List<WebSearchResultBlockParam>`

      - `String encryptedContent`

      - `String title`

      - `JsonValue; type "web_search_result"constant`

        - `WEB_SEARCH_RESULT("web_search_result")`

      - `String url`

      - `Optional<String> pageAge`

    - `class WebSearchToolRequestError:`

      - `WebSearchToolResultErrorCode errorCode`

        - `INVALID_TOOL_INPUT("invalid_tool_input")`

        - `UNAVAILABLE("unavailable")`

        - `MAX_USES_EXCEEDED("max_uses_exceeded")`

        - `TOO_MANY_REQUESTS("too_many_requests")`

        - `QUERY_TOO_LONG("query_too_long")`

        - `REQUEST_TOO_LARGE("request_too_large")`

      - `JsonValue; type "web_search_tool_result_error"constant`

        - `WEB_SEARCH_TOOL_RESULT_ERROR("web_search_tool_result_error")`

  - `String toolUseId`

  - `JsonValue; type "web_search_tool_result"constant`

    - `WEB_SEARCH_TOOL_RESULT("web_search_tool_result")`

  - `Optional<CacheControlEphemeral> cacheControl`

    Create a cache control breakpoint at this content block.

    - `JsonValue; type "ephemeral"constant`

      - `EPHEMERAL("ephemeral")`

    - `Optional<Ttl> ttl`

      The time-to-live for the cache control breakpoint.

      This may be one the following values:

      - `5m`: 5 minutes
      - `1h`: 1 hour

      Defaults to `5m`.

      - `TTL_5M("5m")`

      - `TTL_1H("1h")`

  - `Optional<Caller> caller`

    Tool invocation directly from the model.

    - `class DirectCaller:`

      Tool invocation directly from the model.

      - `JsonValue; type "direct"constant`

        - `DIRECT("direct")`

    - `class ServerToolCaller:`

      Tool invocation generated by a server-side tool.

      - `String toolId`

      - `JsonValue; type "code_execution_20250825"constant`

        - `CODE_EXECUTION_20250825("code_execution_20250825")`

    - `class ServerToolCaller20260120:`

      - `String toolId`

      - `JsonValue; type "code_execution_20260120"constant`

        - `CODE_EXECUTION_20260120("code_execution_20260120")`

### Web Search Tool Result Block Param Content

- `class WebSearchToolResultBlockParamContent: A class that can be one of several variants.union`

  - `List<WebSearchResultBlockParam>`

    - `String encryptedContent`

    - `String title`

    - `JsonValue; type "web_search_result"constant`

      - `WEB_SEARCH_RESULT("web_search_result")`

    - `String url`

    - `Optional<String> pageAge`

  - `class WebSearchToolRequestError:`

    - `WebSearchToolResultErrorCode errorCode`

      - `INVALID_TOOL_INPUT("invalid_tool_input")`

      - `UNAVAILABLE("unavailable")`

      - `MAX_USES_EXCEEDED("max_uses_exceeded")`

      - `TOO_MANY_REQUESTS("too_many_requests")`

      - `QUERY_TOO_LONG("query_too_long")`

      - `REQUEST_TOO_LARGE("request_too_large")`

    - `JsonValue; type "web_search_tool_result_error"constant`

      - `WEB_SEARCH_TOOL_RESULT_ERROR("web_search_tool_result_error")`

### Web Search Tool Result Error

- `class WebSearchToolResultError:`

  - `WebSearchToolResultErrorCode errorCode`

    - `INVALID_TOOL_INPUT("invalid_tool_input")`

    - `UNAVAILABLE("unavailable")`

    - `MAX_USES_EXCEEDED("max_uses_exceeded")`

    - `TOO_MANY_REQUESTS("too_many_requests")`

    - `QUERY_TOO_LONG("query_too_long")`

    - `REQUEST_TOO_LARGE("request_too_large")`

  - `JsonValue; type "web_search_tool_result_error"constant`

    - `WEB_SEARCH_TOOL_RESULT_ERROR("web_search_tool_result_error")`

### Web Search Tool Result Error Code

- `enum WebSearchToolResultErrorCode:`

  - `INVALID_TOOL_INPUT("invalid_tool_input")`

  - `UNAVAILABLE("unavailable")`

  - `MAX_USES_EXCEEDED("max_uses_exceeded")`

  - `TOO_MANY_REQUESTS("too_many_requests")`

  - `QUERY_TOO_LONG("query_too_long")`

  - `REQUEST_TOO_LARGE("request_too_large")`

# Batches

## Create

`MessageBatch messages().batches().create(BatchCreateParamsparams, RequestOptionsrequestOptions = RequestOptions.none())`

**post** `/v1/messages/batches`

Send a batch of Message creation requests.

The Message Batches API can be used to process multiple Messages API requests at once. Once a Message Batch is created, it begins processing immediately. Batches can take up to 24 hours to complete.

Learn more about the Message Batches API in our [user guide](https://docs.claude.com/en/docs/build-with-claude/batch-processing)

### Parameters

- `BatchCreateParams params`

  - `List<Request> requests`

    List of requests for prompt completion. Each is an individual request to create a Message.

    - `String customId`

      Developer-provided ID created for each request in a Message Batch. Useful for matching results to requests, as results may be given out of request order.

      Must be unique for each request within the Message Batch.

    - `Params params`

      Messages API creation parameters for the individual request.

      See the [Messages API reference](https://docs.claude.com/en/api/messages) for full documentation on available parameters.

      - `long maxTokens`

        The maximum number of tokens to generate before stopping.

        Note that our models may stop _before_ reaching this maximum. This parameter only specifies the absolute maximum number of tokens to generate.

        Different models have different maximum values for this parameter.  See [models](https://docs.claude.com/en/docs/models-overview) for details.

      - `List<MessageParam> messages`

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

        - `Content content`

          - `String`

          - `List<ContentBlockParam>`

            - `class TextBlockParam:`

              - `String text`

              - `JsonValue; type "text"constant`

                - `TEXT("text")`

              - `Optional<CacheControlEphemeral> cacheControl`

                Create a cache control breakpoint at this content block.

                - `JsonValue; type "ephemeral"constant`

                  - `EPHEMERAL("ephemeral")`

                - `Optional<Ttl> ttl`

                  The time-to-live for the cache control breakpoint.

                  This may be one the following values:

                  - `5m`: 5 minutes
                  - `1h`: 1 hour

                  Defaults to `5m`.

                  - `TTL_5M("5m")`

                  - `TTL_1H("1h")`

              - `Optional<List<TextCitationParam>> citations`

                - `class CitationCharLocationParam:`

                  - `String citedText`

                  - `long documentIndex`

                  - `Optional<String> documentTitle`

                  - `long endCharIndex`

                  - `long startCharIndex`

                  - `JsonValue; type "char_location"constant`

                    - `CHAR_LOCATION("char_location")`

                - `class CitationPageLocationParam:`

                  - `String citedText`

                  - `long documentIndex`

                  - `Optional<String> documentTitle`

                  - `long endPageNumber`

                  - `long startPageNumber`

                  - `JsonValue; type "page_location"constant`

                    - `PAGE_LOCATION("page_location")`

                - `class CitationContentBlockLocationParam:`

                  - `String citedText`

                  - `long documentIndex`

                  - `Optional<String> documentTitle`

                  - `long endBlockIndex`

                  - `long startBlockIndex`

                  - `JsonValue; type "content_block_location"constant`

                    - `CONTENT_BLOCK_LOCATION("content_block_location")`

                - `class CitationWebSearchResultLocationParam:`

                  - `String citedText`

                  - `String encryptedIndex`

                  - `Optional<String> title`

                  - `JsonValue; type "web_search_result_location"constant`

                    - `WEB_SEARCH_RESULT_LOCATION("web_search_result_location")`

                  - `String url`

                - `class CitationSearchResultLocationParam:`

                  - `String citedText`

                  - `long endBlockIndex`

                  - `long searchResultIndex`

                  - `String source`

                  - `long startBlockIndex`

                  - `Optional<String> title`

                  - `JsonValue; type "search_result_location"constant`

                    - `SEARCH_RESULT_LOCATION("search_result_location")`

            - `class ImageBlockParam:`

              - `Source source`

                - `class Base64ImageSource:`

                  - `String data`

                  - `MediaType mediaType`

                    - `IMAGE_JPEG("image/jpeg")`

                    - `IMAGE_PNG("image/png")`

                    - `IMAGE_GIF("image/gif")`

                    - `IMAGE_WEBP("image/webp")`

                  - `JsonValue; type "base64"constant`

                    - `BASE64("base64")`

                - `class UrlImageSource:`

                  - `JsonValue; type "url"constant`

                    - `URL("url")`

                  - `String url`

              - `JsonValue; type "image"constant`

                - `IMAGE("image")`

              - `Optional<CacheControlEphemeral> cacheControl`

                Create a cache control breakpoint at this content block.

                - `JsonValue; type "ephemeral"constant`

                  - `EPHEMERAL("ephemeral")`

                - `Optional<Ttl> ttl`

                  The time-to-live for the cache control breakpoint.

                  This may be one the following values:

                  - `5m`: 5 minutes
                  - `1h`: 1 hour

                  Defaults to `5m`.

                  - `TTL_5M("5m")`

                  - `TTL_1H("1h")`

            - `class DocumentBlockParam:`

              - `Source source`

                - `class Base64PdfSource:`

                  - `String data`

                  - `JsonValue; mediaType "application/pdf"constant`

                    - `APPLICATION_PDF("application/pdf")`

                  - `JsonValue; type "base64"constant`

                    - `BASE64("base64")`

                - `class PlainTextSource:`

                  - `String data`

                  - `JsonValue; mediaType "text/plain"constant`

                    - `TEXT_PLAIN("text/plain")`

                  - `JsonValue; type "text"constant`

                    - `TEXT("text")`

                - `class ContentBlockSource:`

                  - `Content content`

                    - `String`

                    - `List<ContentBlockSourceContent>`

                      - `class TextBlockParam:`

                        - `String text`

                        - `JsonValue; type "text"constant`

                          - `TEXT("text")`

                        - `Optional<CacheControlEphemeral> cacheControl`

                          Create a cache control breakpoint at this content block.

                          - `JsonValue; type "ephemeral"constant`

                            - `EPHEMERAL("ephemeral")`

                          - `Optional<Ttl> ttl`

                            The time-to-live for the cache control breakpoint.

                            This may be one the following values:

                            - `5m`: 5 minutes
                            - `1h`: 1 hour

                            Defaults to `5m`.

                            - `TTL_5M("5m")`

                            - `TTL_1H("1h")`

                        - `Optional<List<TextCitationParam>> citations`

                          - `class CitationCharLocationParam:`

                            - `String citedText`

                            - `long documentIndex`

                            - `Optional<String> documentTitle`

                            - `long endCharIndex`

                            - `long startCharIndex`

                            - `JsonValue; type "char_location"constant`

                              - `CHAR_LOCATION("char_location")`

                          - `class CitationPageLocationParam:`

                            - `String citedText`

                            - `long documentIndex`

                            - `Optional<String> documentTitle`

                            - `long endPageNumber`

                            - `long startPageNumber`

                            - `JsonValue; type "page_location"constant`

                              - `PAGE_LOCATION("page_location")`

                          - `class CitationContentBlockLocationParam:`

                            - `String citedText`

                            - `long documentIndex`

                            - `Optional<String> documentTitle`

                            - `long endBlockIndex`

                            - `long startBlockIndex`

                            - `JsonValue; type "content_block_location"constant`

                              - `CONTENT_BLOCK_LOCATION("content_block_location")`

                          - `class CitationWebSearchResultLocationParam:`

                            - `String citedText`

                            - `String encryptedIndex`

                            - `Optional<String> title`

                            - `JsonValue; type "web_search_result_location"constant`

                              - `WEB_SEARCH_RESULT_LOCATION("web_search_result_location")`

                            - `String url`

                          - `class CitationSearchResultLocationParam:`

                            - `String citedText`

                            - `long endBlockIndex`

                            - `long searchResultIndex`

                            - `String source`

                            - `long startBlockIndex`

                            - `Optional<String> title`

                            - `JsonValue; type "search_result_location"constant`

                              - `SEARCH_RESULT_LOCATION("search_result_location")`

                      - `class ImageBlockParam:`

                        - `Source source`

                          - `class Base64ImageSource:`

                            - `String data`

                            - `MediaType mediaType`

                              - `IMAGE_JPEG("image/jpeg")`

                              - `IMAGE_PNG("image/png")`

                              - `IMAGE_GIF("image/gif")`

                              - `IMAGE_WEBP("image/webp")`

                            - `JsonValue; type "base64"constant`

                              - `BASE64("base64")`

                          - `class UrlImageSource:`

                            - `JsonValue; type "url"constant`

                              - `URL("url")`

                            - `String url`

                        - `JsonValue; type "image"constant`

                          - `IMAGE("image")`

                        - `Optional<CacheControlEphemeral> cacheControl`

                          Create a cache control breakpoint at this content block.

                          - `JsonValue; type "ephemeral"constant`

                            - `EPHEMERAL("ephemeral")`

                          - `Optional<Ttl> ttl`

                            The time-to-live for the cache control breakpoint.

                            This may be one the following values:

                            - `5m`: 5 minutes
                            - `1h`: 1 hour

                            Defaults to `5m`.

                            - `TTL_5M("5m")`

                            - `TTL_1H("1h")`

                  - `JsonValue; type "content"constant`

                    - `CONTENT("content")`

                - `class UrlPdfSource:`

                  - `JsonValue; type "url"constant`

                    - `URL("url")`

                  - `String url`

              - `JsonValue; type "document"constant`

                - `DOCUMENT("document")`

              - `Optional<CacheControlEphemeral> cacheControl`

                Create a cache control breakpoint at this content block.

                - `JsonValue; type "ephemeral"constant`

                  - `EPHEMERAL("ephemeral")`

                - `Optional<Ttl> ttl`

                  The time-to-live for the cache control breakpoint.

                  This may be one the following values:

                  - `5m`: 5 minutes
                  - `1h`: 1 hour

                  Defaults to `5m`.

                  - `TTL_5M("5m")`

                  - `TTL_1H("1h")`

              - `Optional<CitationsConfigParam> citations`

                - `Optional<Boolean> enabled`

              - `Optional<String> context`

              - `Optional<String> title`

            - `class SearchResultBlockParam:`

              - `List<TextBlockParam> content`

                - `String text`

                - `JsonValue; type "text"constant`

                  - `TEXT("text")`

                - `Optional<CacheControlEphemeral> cacheControl`

                  Create a cache control breakpoint at this content block.

                  - `JsonValue; type "ephemeral"constant`

                    - `EPHEMERAL("ephemeral")`

                  - `Optional<Ttl> ttl`

                    The time-to-live for the cache control breakpoint.

                    This may be one the following values:

                    - `5m`: 5 minutes
                    - `1h`: 1 hour

                    Defaults to `5m`.

                    - `TTL_5M("5m")`

                    - `TTL_1H("1h")`

                - `Optional<List<TextCitationParam>> citations`

                  - `class CitationCharLocationParam:`

                    - `String citedText`

                    - `long documentIndex`

                    - `Optional<String> documentTitle`

                    - `long endCharIndex`

                    - `long startCharIndex`

                    - `JsonValue; type "char_location"constant`

                      - `CHAR_LOCATION("char_location")`

                  - `class CitationPageLocationParam:`

                    - `String citedText`

                    - `long documentIndex`

                    - `Optional<String> documentTitle`

                    - `long endPageNumber`

                    - `long startPageNumber`

                    - `JsonValue; type "page_location"constant`

                      - `PAGE_LOCATION("page_location")`

                  - `class CitationContentBlockLocationParam:`

                    - `String citedText`

                    - `long documentIndex`

                    - `Optional<String> documentTitle`

                    - `long endBlockIndex`

                    - `long startBlockIndex`

                    - `JsonValue; type "content_block_location"constant`

                      - `CONTENT_BLOCK_LOCATION("content_block_location")`

                  - `class CitationWebSearchResultLocationParam:`

                    - `String citedText`

                    - `String encryptedIndex`

                    - `Optional<String> title`

                    - `JsonValue; type "web_search_result_location"constant`

                      - `WEB_SEARCH_RESULT_LOCATION("web_search_result_location")`

                    - `String url`

                  - `class CitationSearchResultLocationParam:`

                    - `String citedText`

                    - `long endBlockIndex`

                    - `long searchResultIndex`

                    - `String source`

                    - `long startBlockIndex`

                    - `Optional<String> title`

                    - `JsonValue; type "search_result_location"constant`

                      - `SEARCH_RESULT_LOCATION("search_result_location")`

              - `String source`

              - `String title`

              - `JsonValue; type "search_result"constant`

                - `SEARCH_RESULT("search_result")`

              - `Optional<CacheControlEphemeral> cacheControl`

                Create a cache control breakpoint at this content block.

                - `JsonValue; type "ephemeral"constant`

                  - `EPHEMERAL("ephemeral")`

                - `Optional<Ttl> ttl`

                  The time-to-live for the cache control breakpoint.

                  This may be one the following values:

                  - `5m`: 5 minutes
                  - `1h`: 1 hour

                  Defaults to `5m`.

                  - `TTL_5M("5m")`

                  - `TTL_1H("1h")`

              - `Optional<CitationsConfigParam> citations`

                - `Optional<Boolean> enabled`

            - `class ThinkingBlockParam:`

              - `String signature`

              - `String thinking`

              - `JsonValue; type "thinking"constant`

                - `THINKING("thinking")`

            - `class RedactedThinkingBlockParam:`

              - `String data`

              - `JsonValue; type "redacted_thinking"constant`

                - `REDACTED_THINKING("redacted_thinking")`

            - `class ToolUseBlockParam:`

              - `String id`

              - `Input input`

              - `String name`

              - `JsonValue; type "tool_use"constant`

                - `TOOL_USE("tool_use")`

              - `Optional<CacheControlEphemeral> cacheControl`

                Create a cache control breakpoint at this content block.

                - `JsonValue; type "ephemeral"constant`

                  - `EPHEMERAL("ephemeral")`

                - `Optional<Ttl> ttl`

                  The time-to-live for the cache control breakpoint.

                  This may be one the following values:

                  - `5m`: 5 minutes
                  - `1h`: 1 hour

                  Defaults to `5m`.

                  - `TTL_5M("5m")`

                  - `TTL_1H("1h")`

              - `Optional<Caller> caller`

                Tool invocation directly from the model.

                - `class DirectCaller:`

                  Tool invocation directly from the model.

                  - `JsonValue; type "direct"constant`

                    - `DIRECT("direct")`

                - `class ServerToolCaller:`

                  Tool invocation generated by a server-side tool.

                  - `String toolId`

                  - `JsonValue; type "code_execution_20250825"constant`

                    - `CODE_EXECUTION_20250825("code_execution_20250825")`

                - `class ServerToolCaller20260120:`

                  - `String toolId`

                  - `JsonValue; type "code_execution_20260120"constant`

                    - `CODE_EXECUTION_20260120("code_execution_20260120")`

            - `class ToolResultBlockParam:`

              - `String toolUseId`

              - `JsonValue; type "tool_result"constant`

                - `TOOL_RESULT("tool_result")`

              - `Optional<CacheControlEphemeral> cacheControl`

                Create a cache control breakpoint at this content block.

                - `JsonValue; type "ephemeral"constant`

                  - `EPHEMERAL("ephemeral")`

                - `Optional<Ttl> ttl`

                  The time-to-live for the cache control breakpoint.

                  This may be one the following values:

                  - `5m`: 5 minutes
                  - `1h`: 1 hour

                  Defaults to `5m`.

                  - `TTL_5M("5m")`

                  - `TTL_1H("1h")`

              - `Optional<Content> content`

                - `String`

                - `List<Block>`

                  - `class TextBlockParam:`

                    - `String text`

                    - `JsonValue; type "text"constant`

                      - `TEXT("text")`

                    - `Optional<CacheControlEphemeral> cacheControl`

                      Create a cache control breakpoint at this content block.

                      - `JsonValue; type "ephemeral"constant`

                        - `EPHEMERAL("ephemeral")`

                      - `Optional<Ttl> ttl`

                        The time-to-live for the cache control breakpoint.

                        This may be one the following values:

                        - `5m`: 5 minutes
                        - `1h`: 1 hour

                        Defaults to `5m`.

                        - `TTL_5M("5m")`

                        - `TTL_1H("1h")`

                    - `Optional<List<TextCitationParam>> citations`

                      - `class CitationCharLocationParam:`

                        - `String citedText`

                        - `long documentIndex`

                        - `Optional<String> documentTitle`

                        - `long endCharIndex`

                        - `long startCharIndex`

                        - `JsonValue; type "char_location"constant`

                          - `CHAR_LOCATION("char_location")`

                      - `class CitationPageLocationParam:`

                        - `String citedText`

                        - `long documentIndex`

                        - `Optional<String> documentTitle`

                        - `long endPageNumber`

                        - `long startPageNumber`

                        - `JsonValue; type "page_location"constant`

                          - `PAGE_LOCATION("page_location")`

                      - `class CitationContentBlockLocationParam:`

                        - `String citedText`

                        - `long documentIndex`

                        - `Optional<String> documentTitle`

                        - `long endBlockIndex`

                        - `long startBlockIndex`

                        - `JsonValue; type "content_block_location"constant`

                          - `CONTENT_BLOCK_LOCATION("content_block_location")`

                      - `class CitationWebSearchResultLocationParam:`

                        - `String citedText`

                        - `String encryptedIndex`

                        - `Optional<String> title`

                        - `JsonValue; type "web_search_result_location"constant`

                          - `WEB_SEARCH_RESULT_LOCATION("web_search_result_location")`

                        - `String url`

                      - `class CitationSearchResultLocationParam:`

                        - `String citedText`

                        - `long endBlockIndex`

                        - `long searchResultIndex`

                        - `String source`

                        - `long startBlockIndex`

                        - `Optional<String> title`

                        - `JsonValue; type "search_result_location"constant`

                          - `SEARCH_RESULT_LOCATION("search_result_location")`

                  - `class ImageBlockParam:`

                    - `Source source`

                      - `class Base64ImageSource:`

                        - `String data`

                        - `MediaType mediaType`

                          - `IMAGE_JPEG("image/jpeg")`

                          - `IMAGE_PNG("image/png")`

                          - `IMAGE_GIF("image/gif")`

                          - `IMAGE_WEBP("image/webp")`

                        - `JsonValue; type "base64"constant`

                          - `BASE64("base64")`

                      - `class UrlImageSource:`

                        - `JsonValue; type "url"constant`

                          - `URL("url")`

                        - `String url`

                    - `JsonValue; type "image"constant`

                      - `IMAGE("image")`

                    - `Optional<CacheControlEphemeral> cacheControl`

                      Create a cache control breakpoint at this content block.

                      - `JsonValue; type "ephemeral"constant`

                        - `EPHEMERAL("ephemeral")`

                      - `Optional<Ttl> ttl`

                        The time-to-live for the cache control breakpoint.

                        This may be one the following values:

                        - `5m`: 5 minutes
                        - `1h`: 1 hour

                        Defaults to `5m`.

                        - `TTL_5M("5m")`

                        - `TTL_1H("1h")`

                  - `class SearchResultBlockParam:`

                    - `List<TextBlockParam> content`

                      - `String text`

                      - `JsonValue; type "text"constant`

                        - `TEXT("text")`

                      - `Optional<CacheControlEphemeral> cacheControl`

                        Create a cache control breakpoint at this content block.

                        - `JsonValue; type "ephemeral"constant`

                          - `EPHEMERAL("ephemeral")`

                        - `Optional<Ttl> ttl`

                          The time-to-live for the cache control breakpoint.

                          This may be one the following values:

                          - `5m`: 5 minutes
                          - `1h`: 1 hour

                          Defaults to `5m`.

                          - `TTL_5M("5m")`

                          - `TTL_1H("1h")`

                      - `Optional<List<TextCitationParam>> citations`

                        - `class CitationCharLocationParam:`

                          - `String citedText`

                          - `long documentIndex`

                          - `Optional<String> documentTitle`

                          - `long endCharIndex`

                          - `long startCharIndex`

                          - `JsonValue; type "char_location"constant`

                            - `CHAR_LOCATION("char_location")`

                        - `class CitationPageLocationParam:`

                          - `String citedText`

                          - `long documentIndex`

                          - `Optional<String> documentTitle`

                          - `long endPageNumber`

                          - `long startPageNumber`

                          - `JsonValue; type "page_location"constant`

                            - `PAGE_LOCATION("page_location")`

                        - `class CitationContentBlockLocationParam:`

                          - `String citedText`

                          - `long documentIndex`

                          - `Optional<String> documentTitle`

                          - `long endBlockIndex`

                          - `long startBlockIndex`

                          - `JsonValue; type "content_block_location"constant`

                            - `CONTENT_BLOCK_LOCATION("content_block_location")`

                        - `class CitationWebSearchResultLocationParam:`

                          - `String citedText`

                          - `String encryptedIndex`

                          - `Optional<String> title`

                          - `JsonValue; type "web_search_result_location"constant`

                            - `WEB_SEARCH_RESULT_LOCATION("web_search_result_location")`

                          - `String url`

                        - `class CitationSearchResultLocationParam:`

                          - `String citedText`

                          - `long endBlockIndex`

                          - `long searchResultIndex`

                          - `String source`

                          - `long startBlockIndex`

                          - `Optional<String> title`

                          - `JsonValue; type "search_result_location"constant`

                            - `SEARCH_RESULT_LOCATION("search_result_location")`

                    - `String source`

                    - `String title`

                    - `JsonValue; type "search_result"constant`

                      - `SEARCH_RESULT("search_result")`

                    - `Optional<CacheControlEphemeral> cacheControl`

                      Create a cache control breakpoint at this content block.

                      - `JsonValue; type "ephemeral"constant`

                        - `EPHEMERAL("ephemeral")`

                      - `Optional<Ttl> ttl`

                        The time-to-live for the cache control breakpoint.

                        This may be one the following values:

                        - `5m`: 5 minutes
                        - `1h`: 1 hour

                        Defaults to `5m`.

                        - `TTL_5M("5m")`

                        - `TTL_1H("1h")`

                    - `Optional<CitationsConfigParam> citations`

                      - `Optional<Boolean> enabled`

                  - `class DocumentBlockParam:`

                    - `Source source`

                      - `class Base64PdfSource:`

                        - `String data`

                        - `JsonValue; mediaType "application/pdf"constant`

                          - `APPLICATION_PDF("application/pdf")`

                        - `JsonValue; type "base64"constant`

                          - `BASE64("base64")`

                      - `class PlainTextSource:`

                        - `String data`

                        - `JsonValue; mediaType "text/plain"constant`

                          - `TEXT_PLAIN("text/plain")`

                        - `JsonValue; type "text"constant`

                          - `TEXT("text")`

                      - `class ContentBlockSource:`

                        - `Content content`

                          - `String`

                          - `List<ContentBlockSourceContent>`

                            - `class TextBlockParam:`

                              - `String text`

                              - `JsonValue; type "text"constant`

                                - `TEXT("text")`

                              - `Optional<CacheControlEphemeral> cacheControl`

                                Create a cache control breakpoint at this content block.

                                - `JsonValue; type "ephemeral"constant`

                                  - `EPHEMERAL("ephemeral")`

                                - `Optional<Ttl> ttl`

                                  The time-to-live for the cache control breakpoint.

                                  This may be one the following values:

                                  - `5m`: 5 minutes
                                  - `1h`: 1 hour

                                  Defaults to `5m`.

                                  - `TTL_5M("5m")`

                                  - `TTL_1H("1h")`

                              - `Optional<List<TextCitationParam>> citations`

                                - `class CitationCharLocationParam:`

                                  - `String citedText`

                                  - `long documentIndex`

                                  - `Optional<String> documentTitle`

                                  - `long endCharIndex`

                                  - `long startCharIndex`

                                  - `JsonValue; type "char_location"constant`

                                    - `CHAR_LOCATION("char_location")`

                                - `class CitationPageLocationParam:`

                                  - `String citedText`

                                  - `long documentIndex`

                                  - `Optional<String> documentTitle`

                                  - `long endPageNumber`

                                  - `long startPageNumber`

                                  - `JsonValue; type "page_location"constant`

                                    - `PAGE_LOCATION("page_location")`

                                - `class CitationContentBlockLocationParam:`

                                  - `String citedText`

                                  - `long documentIndex`

                                  - `Optional<String> documentTitle`

                                  - `long endBlockIndex`

                                  - `long startBlockIndex`

                                  - `JsonValue; type "content_block_location"constant`

                                    - `CONTENT_BLOCK_LOCATION("content_block_location")`

                                - `class CitationWebSearchResultLocationParam:`

                                  - `String citedText`

                                  - `String encryptedIndex`

                                  - `Optional<String> title`

                                  - `JsonValue; type "web_search_result_location"constant`

                                    - `WEB_SEARCH_RESULT_LOCATION("web_search_result_location")`

                                  - `String url`

                                - `class CitationSearchResultLocationParam:`

                                  - `String citedText`

                                  - `long endBlockIndex`

                                  - `long searchResultIndex`

                                  - `String source`

                                  - `long startBlockIndex`

                                  - `Optional<String> title`

                                  - `JsonValue; type "search_result_location"constant`

                                    - `SEARCH_RESULT_LOCATION("search_result_location")`

                            - `class ImageBlockParam:`

                              - `Source source`

                                - `class Base64ImageSource:`

                                  - `String data`

                                  - `MediaType mediaType`

                                    - `IMAGE_JPEG("image/jpeg")`

                                    - `IMAGE_PNG("image/png")`

                                    - `IMAGE_GIF("image/gif")`

                                    - `IMAGE_WEBP("image/webp")`

                                  - `JsonValue; type "base64"constant`

                                    - `BASE64("base64")`

                                - `class UrlImageSource:`

                                  - `JsonValue; type "url"constant`

                                    - `URL("url")`

                                  - `String url`

                              - `JsonValue; type "image"constant`

                                - `IMAGE("image")`

                              - `Optional<CacheControlEphemeral> cacheControl`

                                Create a cache control breakpoint at this content block.

                                - `JsonValue; type "ephemeral"constant`

                                  - `EPHEMERAL("ephemeral")`

                                - `Optional<Ttl> ttl`

                                  The time-to-live for the cache control breakpoint.

                                  This may be one the following values:

                                  - `5m`: 5 minutes
                                  - `1h`: 1 hour

                                  Defaults to `5m`.

                                  - `TTL_5M("5m")`

                                  - `TTL_1H("1h")`

                        - `JsonValue; type "content"constant`

                          - `CONTENT("content")`

                      - `class UrlPdfSource:`

                        - `JsonValue; type "url"constant`

                          - `URL("url")`

                        - `String url`

                    - `JsonValue; type "document"constant`

                      - `DOCUMENT("document")`

                    - `Optional<CacheControlEphemeral> cacheControl`

                      Create a cache control breakpoint at this content block.

                      - `JsonValue; type "ephemeral"constant`

                        - `EPHEMERAL("ephemeral")`

                      - `Optional<Ttl> ttl`

                        The time-to-live for the cache control breakpoint.

                        This may be one the following values:

                        - `5m`: 5 minutes
                        - `1h`: 1 hour

                        Defaults to `5m`.

                        - `TTL_5M("5m")`

                        - `TTL_1H("1h")`

                    - `Optional<CitationsConfigParam> citations`

                      - `Optional<Boolean> enabled`

                    - `Optional<String> context`

                    - `Optional<String> title`

                  - `class ToolReferenceBlockParam:`

                    Tool reference block that can be included in tool_result content.

                    - `String toolName`

                    - `JsonValue; type "tool_reference"constant`

                      - `TOOL_REFERENCE("tool_reference")`

                    - `Optional<CacheControlEphemeral> cacheControl`

                      Create a cache control breakpoint at this content block.

                      - `JsonValue; type "ephemeral"constant`

                        - `EPHEMERAL("ephemeral")`

                      - `Optional<Ttl> ttl`

                        The time-to-live for the cache control breakpoint.

                        This may be one the following values:

                        - `5m`: 5 minutes
                        - `1h`: 1 hour

                        Defaults to `5m`.

                        - `TTL_5M("5m")`

                        - `TTL_1H("1h")`

              - `Optional<Boolean> isError`

            - `class ServerToolUseBlockParam:`

              - `String id`

              - `Input input`

              - `Name name`

                - `WEB_SEARCH("web_search")`

                - `WEB_FETCH("web_fetch")`

                - `CODE_EXECUTION("code_execution")`

                - `BASH_CODE_EXECUTION("bash_code_execution")`

                - `TEXT_EDITOR_CODE_EXECUTION("text_editor_code_execution")`

                - `TOOL_SEARCH_TOOL_REGEX("tool_search_tool_regex")`

                - `TOOL_SEARCH_TOOL_BM25("tool_search_tool_bm25")`

              - `JsonValue; type "server_tool_use"constant`

                - `SERVER_TOOL_USE("server_tool_use")`

              - `Optional<CacheControlEphemeral> cacheControl`

                Create a cache control breakpoint at this content block.

                - `JsonValue; type "ephemeral"constant`

                  - `EPHEMERAL("ephemeral")`

                - `Optional<Ttl> ttl`

                  The time-to-live for the cache control breakpoint.

                  This may be one the following values:

                  - `5m`: 5 minutes
                  - `1h`: 1 hour

                  Defaults to `5m`.

                  - `TTL_5M("5m")`

                  - `TTL_1H("1h")`

              - `Optional<Caller> caller`

                Tool invocation directly from the model.

                - `class DirectCaller:`

                  Tool invocation directly from the model.

                  - `JsonValue; type "direct"constant`

                    - `DIRECT("direct")`

                - `class ServerToolCaller:`

                  Tool invocation generated by a server-side tool.

                  - `String toolId`

                  - `JsonValue; type "code_execution_20250825"constant`

                    - `CODE_EXECUTION_20250825("code_execution_20250825")`

                - `class ServerToolCaller20260120:`

                  - `String toolId`

                  - `JsonValue; type "code_execution_20260120"constant`

                    - `CODE_EXECUTION_20260120("code_execution_20260120")`

            - `class WebSearchToolResultBlockParam:`

              - `WebSearchToolResultBlockParamContent content`

                - `List<WebSearchResultBlockParam>`

                  - `String encryptedContent`

                  - `String title`

                  - `JsonValue; type "web_search_result"constant`

                    - `WEB_SEARCH_RESULT("web_search_result")`

                  - `String url`

                  - `Optional<String> pageAge`

                - `class WebSearchToolRequestError:`

                  - `WebSearchToolResultErrorCode errorCode`

                    - `INVALID_TOOL_INPUT("invalid_tool_input")`

                    - `UNAVAILABLE("unavailable")`

                    - `MAX_USES_EXCEEDED("max_uses_exceeded")`

                    - `TOO_MANY_REQUESTS("too_many_requests")`

                    - `QUERY_TOO_LONG("query_too_long")`

                    - `REQUEST_TOO_LARGE("request_too_large")`

                  - `JsonValue; type "web_search_tool_result_error"constant`

                    - `WEB_SEARCH_TOOL_RESULT_ERROR("web_search_tool_result_error")`

              - `String toolUseId`

              - `JsonValue; type "web_search_tool_result"constant`

                - `WEB_SEARCH_TOOL_RESULT("web_search_tool_result")`

              - `Optional<CacheControlEphemeral> cacheControl`

                Create a cache control breakpoint at this content block.

                - `JsonValue; type "ephemeral"constant`

                  - `EPHEMERAL("ephemeral")`

                - `Optional<Ttl> ttl`

                  The time-to-live for the cache control breakpoint.

                  This may be one the following values:

                  - `5m`: 5 minutes
                  - `1h`: 1 hour

                  Defaults to `5m`.

                  - `TTL_5M("5m")`

                  - `TTL_1H("1h")`

              - `Optional<Caller> caller`

                Tool invocation directly from the model.

                - `class DirectCaller:`

                  Tool invocation directly from the model.

                  - `JsonValue; type "direct"constant`

                    - `DIRECT("direct")`

                - `class ServerToolCaller:`

                  Tool invocation generated by a server-side tool.

                  - `String toolId`

                  - `JsonValue; type "code_execution_20250825"constant`

                    - `CODE_EXECUTION_20250825("code_execution_20250825")`

                - `class ServerToolCaller20260120:`

                  - `String toolId`

                  - `JsonValue; type "code_execution_20260120"constant`

                    - `CODE_EXECUTION_20260120("code_execution_20260120")`

            - `class WebFetchToolResultBlockParam:`

              - `Content content`

                - `class WebFetchToolResultErrorBlockParam:`

                  - `WebFetchToolResultErrorCode errorCode`

                    - `INVALID_TOOL_INPUT("invalid_tool_input")`

                    - `URL_TOO_LONG("url_too_long")`

                    - `URL_NOT_ALLOWED("url_not_allowed")`

                    - `URL_NOT_ACCESSIBLE("url_not_accessible")`

                    - `UNSUPPORTED_CONTENT_TYPE("unsupported_content_type")`

                    - `TOO_MANY_REQUESTS("too_many_requests")`

                    - `MAX_USES_EXCEEDED("max_uses_exceeded")`

                    - `UNAVAILABLE("unavailable")`

                  - `JsonValue; type "web_fetch_tool_result_error"constant`

                    - `WEB_FETCH_TOOL_RESULT_ERROR("web_fetch_tool_result_error")`

                - `class WebFetchBlockParam:`

                  - `DocumentBlockParam content`

                    - `Source source`

                      - `class Base64PdfSource:`

                        - `String data`

                        - `JsonValue; mediaType "application/pdf"constant`

                          - `APPLICATION_PDF("application/pdf")`

                        - `JsonValue; type "base64"constant`

                          - `BASE64("base64")`

                      - `class PlainTextSource:`

                        - `String data`

                        - `JsonValue; mediaType "text/plain"constant`

                          - `TEXT_PLAIN("text/plain")`

                        - `JsonValue; type "text"constant`

                          - `TEXT("text")`

                      - `class ContentBlockSource:`

                        - `Content content`

                          - `String`

                          - `List<ContentBlockSourceContent>`

                            - `class TextBlockParam:`

                              - `String text`

                              - `JsonValue; type "text"constant`

                                - `TEXT("text")`

                              - `Optional<CacheControlEphemeral> cacheControl`

                                Create a cache control breakpoint at this content block.

                                - `JsonValue; type "ephemeral"constant`

                                  - `EPHEMERAL("ephemeral")`

                                - `Optional<Ttl> ttl`

                                  The time-to-live for the cache control breakpoint.

                                  This may be one the following values:

                                  - `5m`: 5 minutes
                                  - `1h`: 1 hour

                                  Defaults to `5m`.

                                  - `TTL_5M("5m")`

                                  - `TTL_1H("1h")`

                              - `Optional<List<TextCitationParam>> citations`

                                - `class CitationCharLocationParam:`

                                  - `String citedText`

                                  - `long documentIndex`

                                  - `Optional<String> documentTitle`

                                  - `long endCharIndex`

                                  - `long startCharIndex`

                                  - `JsonValue; type "char_location"constant`

                                    - `CHAR_LOCATION("char_location")`

                                - `class CitationPageLocationParam:`

                                  - `String citedText`

                                  - `long documentIndex`

                                  - `Optional<String> documentTitle`

                                  - `long endPageNumber`

                                  - `long startPageNumber`

                                  - `JsonValue; type "page_location"constant`

                                    - `PAGE_LOCATION("page_location")`

                                - `class CitationContentBlockLocationParam:`

                                  - `String citedText`

                                  - `long documentIndex`

                                  - `Optional<String> documentTitle`

                                  - `long endBlockIndex`

                                  - `long startBlockIndex`

                                  - `JsonValue; type "content_block_location"constant`

                                    - `CONTENT_BLOCK_LOCATION("content_block_location")`

                                - `class CitationWebSearchResultLocationParam:`

                                  - `String citedText`

                                  - `String encryptedIndex`

                                  - `Optional<String> title`

                                  - `JsonValue; type "web_search_result_location"constant`

                                    - `WEB_SEARCH_RESULT_LOCATION("web_search_result_location")`

                                  - `String url`

                                - `class CitationSearchResultLocationParam:`

                                  - `String citedText`

                                  - `long endBlockIndex`

                                  - `long searchResultIndex`

                                  - `String source`

                                  - `long startBlockIndex`

                                  - `Optional<String> title`

                                  - `JsonValue; type "search_result_location"constant`

                                    - `SEARCH_RESULT_LOCATION("search_result_location")`

                            - `class ImageBlockParam:`

                              - `Source source`

                                - `class Base64ImageSource:`

                                  - `String data`

                                  - `MediaType mediaType`

                                    - `IMAGE_JPEG("image/jpeg")`

                                    - `IMAGE_PNG("image/png")`

                                    - `IMAGE_GIF("image/gif")`

                                    - `IMAGE_WEBP("image/webp")`

                                  - `JsonValue; type "base64"constant`

                                    - `BASE64("base64")`

                                - `class UrlImageSource:`

                                  - `JsonValue; type "url"constant`

                                    - `URL("url")`

                                  - `String url`

                              - `JsonValue; type "image"constant`

                                - `IMAGE("image")`

                              - `Optional<CacheControlEphemeral> cacheControl`

                                Create a cache control breakpoint at this content block.

                                - `JsonValue; type "ephemeral"constant`

                                  - `EPHEMERAL("ephemeral")`

                                - `Optional<Ttl> ttl`

                                  The time-to-live for the cache control breakpoint.

                                  This may be one the following values:

                                  - `5m`: 5 minutes
                                  - `1h`: 1 hour

                                  Defaults to `5m`.

                                  - `TTL_5M("5m")`

                                  - `TTL_1H("1h")`

                        - `JsonValue; type "content"constant`

                          - `CONTENT("content")`

                      - `class UrlPdfSource:`

                        - `JsonValue; type "url"constant`

                          - `URL("url")`

                        - `String url`

                    - `JsonValue; type "document"constant`

                      - `DOCUMENT("document")`

                    - `Optional<CacheControlEphemeral> cacheControl`

                      Create a cache control breakpoint at this content block.

                      - `JsonValue; type "ephemeral"constant`

                        - `EPHEMERAL("ephemeral")`

                      - `Optional<Ttl> ttl`

                        The time-to-live for the cache control breakpoint.

                        This may be one the following values:

                        - `5m`: 5 minutes
                        - `1h`: 1 hour

                        Defaults to `5m`.

                        - `TTL_5M("5m")`

                        - `TTL_1H("1h")`

                    - `Optional<CitationsConfigParam> citations`

                      - `Optional<Boolean> enabled`

                    - `Optional<String> context`

                    - `Optional<String> title`

                  - `JsonValue; type "web_fetch_result"constant`

                    - `WEB_FETCH_RESULT("web_fetch_result")`

                  - `String url`

                    Fetched content URL

                  - `Optional<String> retrievedAt`

                    ISO 8601 timestamp when the content was retrieved

              - `String toolUseId`

              - `JsonValue; type "web_fetch_tool_result"constant`

                - `WEB_FETCH_TOOL_RESULT("web_fetch_tool_result")`

              - `Optional<CacheControlEphemeral> cacheControl`

                Create a cache control breakpoint at this content block.

                - `JsonValue; type "ephemeral"constant`

                  - `EPHEMERAL("ephemeral")`

                - `Optional<Ttl> ttl`

                  The time-to-live for the cache control breakpoint.

                  This may be one the following values:

                  - `5m`: 5 minutes
                  - `1h`: 1 hour

                  Defaults to `5m`.

                  - `TTL_5M("5m")`

                  - `TTL_1H("1h")`

              - `Optional<Caller> caller`

                Tool invocation directly from the model.

                - `class DirectCaller:`

                  Tool invocation directly from the model.

                  - `JsonValue; type "direct"constant`

                    - `DIRECT("direct")`

                - `class ServerToolCaller:`

                  Tool invocation generated by a server-side tool.

                  - `String toolId`

                  - `JsonValue; type "code_execution_20250825"constant`

                    - `CODE_EXECUTION_20250825("code_execution_20250825")`

                - `class ServerToolCaller20260120:`

                  - `String toolId`

                  - `JsonValue; type "code_execution_20260120"constant`

                    - `CODE_EXECUTION_20260120("code_execution_20260120")`

            - `class CodeExecutionToolResultBlockParam:`

              - `CodeExecutionToolResultBlockParamContent content`

                Code execution result with encrypted stdout for PFC + web_search results.

                - `class CodeExecutionToolResultErrorParam:`

                  - `CodeExecutionToolResultErrorCode errorCode`

                    - `INVALID_TOOL_INPUT("invalid_tool_input")`

                    - `UNAVAILABLE("unavailable")`

                    - `TOO_MANY_REQUESTS("too_many_requests")`

                    - `EXECUTION_TIME_EXCEEDED("execution_time_exceeded")`

                  - `JsonValue; type "code_execution_tool_result_error"constant`

                    - `CODE_EXECUTION_TOOL_RESULT_ERROR("code_execution_tool_result_error")`

                - `class CodeExecutionResultBlockParam:`

                  - `List<CodeExecutionOutputBlockParam> content`

                    - `String fileId`

                    - `JsonValue; type "code_execution_output"constant`

                      - `CODE_EXECUTION_OUTPUT("code_execution_output")`

                  - `long returnCode`

                  - `String stderr`

                  - `String stdout`

                  - `JsonValue; type "code_execution_result"constant`

                    - `CODE_EXECUTION_RESULT("code_execution_result")`

                - `class EncryptedCodeExecutionResultBlockParam:`

                  Code execution result with encrypted stdout for PFC + web_search results.

                  - `List<CodeExecutionOutputBlockParam> content`

                    - `String fileId`

                    - `JsonValue; type "code_execution_output"constant`

                      - `CODE_EXECUTION_OUTPUT("code_execution_output")`

                  - `String encryptedStdout`

                  - `long returnCode`

                  - `String stderr`

                  - `JsonValue; type "encrypted_code_execution_result"constant`

                    - `ENCRYPTED_CODE_EXECUTION_RESULT("encrypted_code_execution_result")`

              - `String toolUseId`

              - `JsonValue; type "code_execution_tool_result"constant`

                - `CODE_EXECUTION_TOOL_RESULT("code_execution_tool_result")`

              - `Optional<CacheControlEphemeral> cacheControl`

                Create a cache control breakpoint at this content block.

                - `JsonValue; type "ephemeral"constant`

                  - `EPHEMERAL("ephemeral")`

                - `Optional<Ttl> ttl`

                  The time-to-live for the cache control breakpoint.

                  This may be one the following values:

                  - `5m`: 5 minutes
                  - `1h`: 1 hour

                  Defaults to `5m`.

                  - `TTL_5M("5m")`

                  - `TTL_1H("1h")`

            - `class BashCodeExecutionToolResultBlockParam:`

              - `Content content`

                - `class BashCodeExecutionToolResultErrorParam:`

                  - `BashCodeExecutionToolResultErrorCode errorCode`

                    - `INVALID_TOOL_INPUT("invalid_tool_input")`

                    - `UNAVAILABLE("unavailable")`

                    - `TOO_MANY_REQUESTS("too_many_requests")`

                    - `EXECUTION_TIME_EXCEEDED("execution_time_exceeded")`

                    - `OUTPUT_FILE_TOO_LARGE("output_file_too_large")`

                  - `JsonValue; type "bash_code_execution_tool_result_error"constant`

                    - `BASH_CODE_EXECUTION_TOOL_RESULT_ERROR("bash_code_execution_tool_result_error")`

                - `class BashCodeExecutionResultBlockParam:`

                  - `List<BashCodeExecutionOutputBlockParam> content`

                    - `String fileId`

                    - `JsonValue; type "bash_code_execution_output"constant`

                      - `BASH_CODE_EXECUTION_OUTPUT("bash_code_execution_output")`

                  - `long returnCode`

                  - `String stderr`

                  - `String stdout`

                  - `JsonValue; type "bash_code_execution_result"constant`

                    - `BASH_CODE_EXECUTION_RESULT("bash_code_execution_result")`

              - `String toolUseId`

              - `JsonValue; type "bash_code_execution_tool_result"constant`

                - `BASH_CODE_EXECUTION_TOOL_RESULT("bash_code_execution_tool_result")`

              - `Optional<CacheControlEphemeral> cacheControl`

                Create a cache control breakpoint at this content block.

                - `JsonValue; type "ephemeral"constant`

                  - `EPHEMERAL("ephemeral")`

                - `Optional<Ttl> ttl`

                  The time-to-live for the cache control breakpoint.

                  This may be one the following values:

                  - `5m`: 5 minutes
                  - `1h`: 1 hour

                  Defaults to `5m`.

                  - `TTL_5M("5m")`

                  - `TTL_1H("1h")`

            - `class TextEditorCodeExecutionToolResultBlockParam:`

              - `Content content`

                - `class TextEditorCodeExecutionToolResultErrorParam:`

                  - `TextEditorCodeExecutionToolResultErrorCode errorCode`

                    - `INVALID_TOOL_INPUT("invalid_tool_input")`

                    - `UNAVAILABLE("unavailable")`

                    - `TOO_MANY_REQUESTS("too_many_requests")`

                    - `EXECUTION_TIME_EXCEEDED("execution_time_exceeded")`

                    - `FILE_NOT_FOUND("file_not_found")`

                  - `JsonValue; type "text_editor_code_execution_tool_result_error"constant`

                    - `TEXT_EDITOR_CODE_EXECUTION_TOOL_RESULT_ERROR("text_editor_code_execution_tool_result_error")`

                  - `Optional<String> errorMessage`

                - `class TextEditorCodeExecutionViewResultBlockParam:`

                  - `String content`

                  - `FileType fileType`

                    - `TEXT("text")`

                    - `IMAGE("image")`

                    - `PDF("pdf")`

                  - `JsonValue; type "text_editor_code_execution_view_result"constant`

                    - `TEXT_EDITOR_CODE_EXECUTION_VIEW_RESULT("text_editor_code_execution_view_result")`

                  - `Optional<Long> numLines`

                  - `Optional<Long> startLine`

                  - `Optional<Long> totalLines`

                - `class TextEditorCodeExecutionCreateResultBlockParam:`

                  - `boolean isFileUpdate`

                  - `JsonValue; type "text_editor_code_execution_create_result"constant`

                    - `TEXT_EDITOR_CODE_EXECUTION_CREATE_RESULT("text_editor_code_execution_create_result")`

                - `class TextEditorCodeExecutionStrReplaceResultBlockParam:`

                  - `JsonValue; type "text_editor_code_execution_str_replace_result"constant`

                    - `TEXT_EDITOR_CODE_EXECUTION_STR_REPLACE_RESULT("text_editor_code_execution_str_replace_result")`

                  - `Optional<List<String>> lines`

                  - `Optional<Long> newLines`

                  - `Optional<Long> newStart`

                  - `Optional<Long> oldLines`

                  - `Optional<Long> oldStart`

              - `String toolUseId`

              - `JsonValue; type "text_editor_code_execution_tool_result"constant`

                - `TEXT_EDITOR_CODE_EXECUTION_TOOL_RESULT("text_editor_code_execution_tool_result")`

              - `Optional<CacheControlEphemeral> cacheControl`

                Create a cache control breakpoint at this content block.

                - `JsonValue; type "ephemeral"constant`

                  - `EPHEMERAL("ephemeral")`

                - `Optional<Ttl> ttl`

                  The time-to-live for the cache control breakpoint.

                  This may be one the following values:

                  - `5m`: 5 minutes
                  - `1h`: 1 hour

                  Defaults to `5m`.

                  - `TTL_5M("5m")`

                  - `TTL_1H("1h")`

            - `class ToolSearchToolResultBlockParam:`

              - `Content content`

                - `class ToolSearchToolResultErrorParam:`

                  - `ToolSearchToolResultErrorCode errorCode`

                    - `INVALID_TOOL_INPUT("invalid_tool_input")`

                    - `UNAVAILABLE("unavailable")`

                    - `TOO_MANY_REQUESTS("too_many_requests")`

                    - `EXECUTION_TIME_EXCEEDED("execution_time_exceeded")`

                  - `JsonValue; type "tool_search_tool_result_error"constant`

                    - `TOOL_SEARCH_TOOL_RESULT_ERROR("tool_search_tool_result_error")`

                - `class ToolSearchToolSearchResultBlockParam:`

                  - `List<ToolReferenceBlockParam> toolReferences`

                    - `String toolName`

                    - `JsonValue; type "tool_reference"constant`

                      - `TOOL_REFERENCE("tool_reference")`

                    - `Optional<CacheControlEphemeral> cacheControl`

                      Create a cache control breakpoint at this content block.

                      - `JsonValue; type "ephemeral"constant`

                        - `EPHEMERAL("ephemeral")`

                      - `Optional<Ttl> ttl`

                        The time-to-live for the cache control breakpoint.

                        This may be one the following values:

                        - `5m`: 5 minutes
                        - `1h`: 1 hour

                        Defaults to `5m`.

                        - `TTL_5M("5m")`

                        - `TTL_1H("1h")`

                  - `JsonValue; type "tool_search_tool_search_result"constant`

                    - `TOOL_SEARCH_TOOL_SEARCH_RESULT("tool_search_tool_search_result")`

              - `String toolUseId`

              - `JsonValue; type "tool_search_tool_result"constant`

                - `TOOL_SEARCH_TOOL_RESULT("tool_search_tool_result")`

              - `Optional<CacheControlEphemeral> cacheControl`

                Create a cache control breakpoint at this content block.

                - `JsonValue; type "ephemeral"constant`

                  - `EPHEMERAL("ephemeral")`

                - `Optional<Ttl> ttl`

                  The time-to-live for the cache control breakpoint.

                  This may be one the following values:

                  - `5m`: 5 minutes
                  - `1h`: 1 hour

                  Defaults to `5m`.

                  - `TTL_5M("5m")`

                  - `TTL_1H("1h")`

            - `class ContainerUploadBlockParam:`

              A content block that represents a file to be uploaded to the container
              Files uploaded via this block will be available in the container's input directory.

              - `String fileId`

              - `JsonValue; type "container_upload"constant`

                - `CONTAINER_UPLOAD("container_upload")`

              - `Optional<CacheControlEphemeral> cacheControl`

                Create a cache control breakpoint at this content block.

                - `JsonValue; type "ephemeral"constant`

                  - `EPHEMERAL("ephemeral")`

                - `Optional<Ttl> ttl`

                  The time-to-live for the cache control breakpoint.

                  This may be one the following values:

                  - `5m`: 5 minutes
                  - `1h`: 1 hour

                  Defaults to `5m`.

                  - `TTL_5M("5m")`

                  - `TTL_1H("1h")`

        - `Role role`

          - `USER("user")`

          - `ASSISTANT("assistant")`

      - `Model model`

        The model that will complete your prompt.

        See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

        - `CLAUDE_OPUS_4_6("claude-opus-4-6")`

          Most intelligent model for building agents and coding

        - `CLAUDE_SONNET_4_6("claude-sonnet-4-6")`

          Frontier intelligence at scale — built for coding, agents, and enterprise workflows

        - `CLAUDE_OPUS_4_5_20251101("claude-opus-4-5-20251101")`

          Premium model combining maximum intelligence with practical performance

        - `CLAUDE_OPUS_4_5("claude-opus-4-5")`

          Premium model combining maximum intelligence with practical performance

        - `CLAUDE_3_7_SONNET_LATEST("claude-3-7-sonnet-latest")`

          High-performance model with early extended thinking

        - `CLAUDE_3_7_SONNET_20250219("claude-3-7-sonnet-20250219")`

          High-performance model with early extended thinking

        - `CLAUDE_3_5_HAIKU_LATEST("claude-3-5-haiku-latest")`

          Fastest and most compact model for near-instant responsiveness

        - `CLAUDE_3_5_HAIKU_20241022("claude-3-5-haiku-20241022")`

          Our fastest model

        - `CLAUDE_HAIKU_4_5("claude-haiku-4-5")`

          Hybrid model, capable of near-instant responses and extended thinking

        - `CLAUDE_HAIKU_4_5_20251001("claude-haiku-4-5-20251001")`

          Hybrid model, capable of near-instant responses and extended thinking

        - `CLAUDE_SONNET_4_20250514("claude-sonnet-4-20250514")`

          High-performance model with extended thinking

        - `CLAUDE_SONNET_4_0("claude-sonnet-4-0")`

          High-performance model with extended thinking

        - `CLAUDE_4_SONNET_20250514("claude-4-sonnet-20250514")`

          High-performance model with extended thinking

        - `CLAUDE_SONNET_4_5("claude-sonnet-4-5")`

          Our best model for real-world agents and coding

        - `CLAUDE_SONNET_4_5_20250929("claude-sonnet-4-5-20250929")`

          Our best model for real-world agents and coding

        - `CLAUDE_OPUS_4_0("claude-opus-4-0")`

          Our most capable model

        - `CLAUDE_OPUS_4_20250514("claude-opus-4-20250514")`

          Our most capable model

        - `CLAUDE_4_OPUS_20250514("claude-4-opus-20250514")`

          Our most capable model

        - `CLAUDE_OPUS_4_1_20250805("claude-opus-4-1-20250805")`

          Our most capable model

        - `CLAUDE_3_OPUS_LATEST("claude-3-opus-latest")`

          Excels at writing and complex tasks

        - `CLAUDE_3_OPUS_20240229("claude-3-opus-20240229")`

          Excels at writing and complex tasks

        - `CLAUDE_3_HAIKU_20240307("claude-3-haiku-20240307")`

          Our previous most fast and cost-effective

      - `Optional<CacheControlEphemeral> cacheControl`

        Top-level cache control automatically applies a cache_control marker to the last cacheable block in the request.

        - `JsonValue; type "ephemeral"constant`

          - `EPHEMERAL("ephemeral")`

        - `Optional<Ttl> ttl`

          The time-to-live for the cache control breakpoint.

          This may be one the following values:

          - `5m`: 5 minutes
          - `1h`: 1 hour

          Defaults to `5m`.

          - `TTL_5M("5m")`

          - `TTL_1H("1h")`

      - `Optional<String> container`

        Container identifier for reuse across requests.

      - `Optional<String> inferenceGeo`

        Specifies the geographic region for inference processing. If not specified, the workspace's `default_inference_geo` is used.

      - `Optional<Metadata> metadata`

        An object describing metadata about the request.

        - `Optional<String> userId`

          An external identifier for the user who is associated with the request.

          This should be a uuid, hash value, or other opaque identifier. Anthropic may use this id to help detect abuse. Do not include any identifying information such as name, email address, or phone number.

      - `Optional<OutputConfig> outputConfig`

        Configuration options for the model's output, such as the output format.

        - `Optional<Effort> effort`

          All possible effort levels.

          - `LOW("low")`

          - `MEDIUM("medium")`

          - `HIGH("high")`

          - `MAX("max")`

        - `Optional<JsonOutputFormat> format`

          A schema to specify Claude's output format in responses. See [structured outputs](https://platform.claude.com/docs/en/build-with-claude/structured-outputs)

          - `Schema schema`

            The JSON schema of the format

          - `JsonValue; type "json_schema"constant`

            - `JSON_SCHEMA("json_schema")`

      - `Optional<ServiceTier> serviceTier`

        Determines whether to use priority capacity (if available) or standard capacity for this request.

        Anthropic offers different levels of service for your API requests. See [service-tiers](https://docs.claude.com/en/api/service-tiers) for details.

        - `AUTO("auto")`

        - `STANDARD_ONLY("standard_only")`

      - `Optional<List<String>> stopSequences`

        Custom text sequences that will cause the model to stop generating.

        Our models will normally stop when they have naturally completed their turn, which will result in a response `stop_reason` of `"end_turn"`.

        If you want the model to stop generating when it encounters custom strings of text, you can use the `stop_sequences` parameter. If the model encounters one of the custom sequences, the response `stop_reason` value will be `"stop_sequence"` and the response `stop_sequence` value will contain the matched stop sequence.

      - `Optional<Boolean> stream`

        Whether to incrementally stream the response using server-sent events.

        See [streaming](https://docs.claude.com/en/api/messages-streaming) for details.

      - `Optional<System> system`

        System prompt.

        A system prompt is a way of providing context and instructions to Claude, such as specifying a particular goal or role. See our [guide to system prompts](https://docs.claude.com/en/docs/system-prompts).

        - `String`

        - `List<TextBlockParam>`

          - `String text`

          - `JsonValue; type "text"constant`

            - `TEXT("text")`

          - `Optional<CacheControlEphemeral> cacheControl`

            Create a cache control breakpoint at this content block.

            - `JsonValue; type "ephemeral"constant`

              - `EPHEMERAL("ephemeral")`

            - `Optional<Ttl> ttl`

              The time-to-live for the cache control breakpoint.

              This may be one the following values:

              - `5m`: 5 minutes
              - `1h`: 1 hour

              Defaults to `5m`.

              - `TTL_5M("5m")`

              - `TTL_1H("1h")`

          - `Optional<List<TextCitationParam>> citations`

            - `class CitationCharLocationParam:`

              - `String citedText`

              - `long documentIndex`

              - `Optional<String> documentTitle`

              - `long endCharIndex`

              - `long startCharIndex`

              - `JsonValue; type "char_location"constant`

                - `CHAR_LOCATION("char_location")`

            - `class CitationPageLocationParam:`

              - `String citedText`

              - `long documentIndex`

              - `Optional<String> documentTitle`

              - `long endPageNumber`

              - `long startPageNumber`

              - `JsonValue; type "page_location"constant`

                - `PAGE_LOCATION("page_location")`

            - `class CitationContentBlockLocationParam:`

              - `String citedText`

              - `long documentIndex`

              - `Optional<String> documentTitle`

              - `long endBlockIndex`

              - `long startBlockIndex`

              - `JsonValue; type "content_block_location"constant`

                - `CONTENT_BLOCK_LOCATION("content_block_location")`

            - `class CitationWebSearchResultLocationParam:`

              - `String citedText`

              - `String encryptedIndex`

              - `Optional<String> title`

              - `JsonValue; type "web_search_result_location"constant`

                - `WEB_SEARCH_RESULT_LOCATION("web_search_result_location")`

              - `String url`

            - `class CitationSearchResultLocationParam:`

              - `String citedText`

              - `long endBlockIndex`

              - `long searchResultIndex`

              - `String source`

              - `long startBlockIndex`

              - `Optional<String> title`

              - `JsonValue; type "search_result_location"constant`

                - `SEARCH_RESULT_LOCATION("search_result_location")`

      - `Optional<Double> temperature`

        Amount of randomness injected into the response.

        Defaults to `1.0`. Ranges from `0.0` to `1.0`. Use `temperature` closer to `0.0` for analytical / multiple choice, and closer to `1.0` for creative and generative tasks.

        Note that even with `temperature` of `0.0`, the results will not be fully deterministic.

      - `Optional<ThinkingConfigParam> thinking`

        Configuration for enabling Claude's extended thinking.

        When enabled, responses include `thinking` content blocks showing Claude's thinking process before the final answer. Requires a minimum budget of 1,024 tokens and counts towards your `max_tokens` limit.

        See [extended thinking](https://docs.claude.com/en/docs/build-with-claude/extended-thinking) for details.

        - `class ThinkingConfigEnabled:`

          - `long budgetTokens`

            Determines how many tokens Claude can use for its internal reasoning process. Larger budgets can enable more thorough analysis for complex problems, improving response quality.

            Must be ≥1024 and less than `max_tokens`.

            See [extended thinking](https://docs.claude.com/en/docs/build-with-claude/extended-thinking) for details.

          - `JsonValue; type "enabled"constant`

            - `ENABLED("enabled")`

        - `class ThinkingConfigDisabled:`

          - `JsonValue; type "disabled"constant`

            - `DISABLED("disabled")`

        - `class ThinkingConfigAdaptive:`

          - `JsonValue; type "adaptive"constant`

            - `ADAPTIVE("adaptive")`

      - `Optional<ToolChoice> toolChoice`

        How the model should use the provided tools. The model can use a specific tool, any available tool, decide by itself, or not use tools at all.

        - `class ToolChoiceAuto:`

          The model will automatically decide whether to use tools.

          - `JsonValue; type "auto"constant`

            - `AUTO("auto")`

          - `Optional<Boolean> disableParallelToolUse`

            Whether to disable parallel tool use.

            Defaults to `false`. If set to `true`, the model will output at most one tool use.

        - `class ToolChoiceAny:`

          The model will use any available tools.

          - `JsonValue; type "any"constant`

            - `ANY("any")`

          - `Optional<Boolean> disableParallelToolUse`

            Whether to disable parallel tool use.

            Defaults to `false`. If set to `true`, the model will output exactly one tool use.

        - `class ToolChoiceTool:`

          The model will use the specified tool with `tool_choice.name`.

          - `String name`

            The name of the tool to use.

          - `JsonValue; type "tool"constant`

            - `TOOL("tool")`

          - `Optional<Boolean> disableParallelToolUse`

            Whether to disable parallel tool use.

            Defaults to `false`. If set to `true`, the model will output exactly one tool use.

        - `class ToolChoiceNone:`

          The model will not be allowed to use tools.

          - `JsonValue; type "none"constant`

            - `NONE("none")`

      - `Optional<List<ToolUnion>> tools`

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

        - `class Tool:`

          - `InputSchema inputSchema`

            [JSON schema](https://json-schema.org/draft/2020-12) for this tool's input.

            This defines the shape of the `input` that your tool accepts and that the model will produce.

            - `JsonValue; type "object"constant`

              - `OBJECT("object")`

            - `Optional<Properties> properties`

            - `Optional<List<String>> required`

          - `String name`

            Name of the tool.

            This is how the tool will be called by the model and in `tool_use` blocks.

          - `Optional<List<AllowedCaller>> allowedCallers`

            - `DIRECT("direct")`

            - `CODE_EXECUTION_20250825("code_execution_20250825")`

            - `CODE_EXECUTION_20260120("code_execution_20260120")`

          - `Optional<CacheControlEphemeral> cacheControl`

            Create a cache control breakpoint at this content block.

            - `JsonValue; type "ephemeral"constant`

              - `EPHEMERAL("ephemeral")`

            - `Optional<Ttl> ttl`

              The time-to-live for the cache control breakpoint.

              This may be one the following values:

              - `5m`: 5 minutes
              - `1h`: 1 hour

              Defaults to `5m`.

              - `TTL_5M("5m")`

              - `TTL_1H("1h")`

          - `Optional<Boolean> deferLoading`

            If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

          - `Optional<String> description`

            Description of what this tool does.

            Tool descriptions should be as detailed as possible. The more information that the model has about what the tool is and how to use it, the better it will perform. You can use natural language descriptions to reinforce important aspects of the tool input JSON schema.

          - `Optional<Boolean> eagerInputStreaming`

            Enable eager input streaming for this tool. When true, tool input parameters will be streamed incrementally as they are generated, and types will be inferred on-the-fly rather than buffering the full JSON output. When false, streaming is disabled for this tool even if the fine-grained-tool-streaming beta is active. When null (default), uses the default behavior based on beta headers.

          - `Optional<List<InputExample>> inputExamples`

          - `Optional<Boolean> strict`

            When true, guarantees schema validation on tool names and inputs

          - `Optional<Type> type`

            - `CUSTOM("custom")`

        - `class ToolBash20250124:`

          - `JsonValue; name "bash"constant`

            Name of the tool.

            This is how the tool will be called by the model and in `tool_use` blocks.

            - `BASH("bash")`

          - `JsonValue; type "bash_20250124"constant`

            - `BASH_20250124("bash_20250124")`

          - `Optional<List<AllowedCaller>> allowedCallers`

            - `DIRECT("direct")`

            - `CODE_EXECUTION_20250825("code_execution_20250825")`

            - `CODE_EXECUTION_20260120("code_execution_20260120")`

          - `Optional<CacheControlEphemeral> cacheControl`

            Create a cache control breakpoint at this content block.

            - `JsonValue; type "ephemeral"constant`

              - `EPHEMERAL("ephemeral")`

            - `Optional<Ttl> ttl`

              The time-to-live for the cache control breakpoint.

              This may be one the following values:

              - `5m`: 5 minutes
              - `1h`: 1 hour

              Defaults to `5m`.

              - `TTL_5M("5m")`

              - `TTL_1H("1h")`

          - `Optional<Boolean> deferLoading`

            If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

          - `Optional<List<InputExample>> inputExamples`

          - `Optional<Boolean> strict`

            When true, guarantees schema validation on tool names and inputs

        - `class CodeExecutionTool20250522:`

          - `JsonValue; name "code_execution"constant`

            Name of the tool.

            This is how the tool will be called by the model and in `tool_use` blocks.

            - `CODE_EXECUTION("code_execution")`

          - `JsonValue; type "code_execution_20250522"constant`

            - `CODE_EXECUTION_20250522("code_execution_20250522")`

          - `Optional<List<AllowedCaller>> allowedCallers`

            - `DIRECT("direct")`

            - `CODE_EXECUTION_20250825("code_execution_20250825")`

            - `CODE_EXECUTION_20260120("code_execution_20260120")`

          - `Optional<CacheControlEphemeral> cacheControl`

            Create a cache control breakpoint at this content block.

            - `JsonValue; type "ephemeral"constant`

              - `EPHEMERAL("ephemeral")`

            - `Optional<Ttl> ttl`

              The time-to-live for the cache control breakpoint.

              This may be one the following values:

              - `5m`: 5 minutes
              - `1h`: 1 hour

              Defaults to `5m`.

              - `TTL_5M("5m")`

              - `TTL_1H("1h")`

          - `Optional<Boolean> deferLoading`

            If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

          - `Optional<Boolean> strict`

            When true, guarantees schema validation on tool names and inputs

        - `class CodeExecutionTool20250825:`

          - `JsonValue; name "code_execution"constant`

            Name of the tool.

            This is how the tool will be called by the model and in `tool_use` blocks.

            - `CODE_EXECUTION("code_execution")`

          - `JsonValue; type "code_execution_20250825"constant`

            - `CODE_EXECUTION_20250825("code_execution_20250825")`

          - `Optional<List<AllowedCaller>> allowedCallers`

            - `DIRECT("direct")`

            - `CODE_EXECUTION_20250825("code_execution_20250825")`

            - `CODE_EXECUTION_20260120("code_execution_20260120")`

          - `Optional<CacheControlEphemeral> cacheControl`

            Create a cache control breakpoint at this content block.

            - `JsonValue; type "ephemeral"constant`

              - `EPHEMERAL("ephemeral")`

            - `Optional<Ttl> ttl`

              The time-to-live for the cache control breakpoint.

              This may be one the following values:

              - `5m`: 5 minutes
              - `1h`: 1 hour

              Defaults to `5m`.

              - `TTL_5M("5m")`

              - `TTL_1H("1h")`

          - `Optional<Boolean> deferLoading`

            If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

          - `Optional<Boolean> strict`

            When true, guarantees schema validation on tool names and inputs

        - `class CodeExecutionTool20260120:`

          Code execution tool with REPL state persistence (daemon mode + gVisor checkpoint).

          - `JsonValue; name "code_execution"constant`

            Name of the tool.

            This is how the tool will be called by the model and in `tool_use` blocks.

            - `CODE_EXECUTION("code_execution")`

          - `JsonValue; type "code_execution_20260120"constant`

            - `CODE_EXECUTION_20260120("code_execution_20260120")`

          - `Optional<List<AllowedCaller>> allowedCallers`

            - `DIRECT("direct")`

            - `CODE_EXECUTION_20250825("code_execution_20250825")`

            - `CODE_EXECUTION_20260120("code_execution_20260120")`

          - `Optional<CacheControlEphemeral> cacheControl`

            Create a cache control breakpoint at this content block.

            - `JsonValue; type "ephemeral"constant`

              - `EPHEMERAL("ephemeral")`

            - `Optional<Ttl> ttl`

              The time-to-live for the cache control breakpoint.

              This may be one the following values:

              - `5m`: 5 minutes
              - `1h`: 1 hour

              Defaults to `5m`.

              - `TTL_5M("5m")`

              - `TTL_1H("1h")`

          - `Optional<Boolean> deferLoading`

            If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

          - `Optional<Boolean> strict`

            When true, guarantees schema validation on tool names and inputs

        - `class MemoryTool20250818:`

          - `JsonValue; name "memory"constant`

            Name of the tool.

            This is how the tool will be called by the model and in `tool_use` blocks.

            - `MEMORY("memory")`

          - `JsonValue; type "memory_20250818"constant`

            - `MEMORY_20250818("memory_20250818")`

          - `Optional<List<AllowedCaller>> allowedCallers`

            - `DIRECT("direct")`

            - `CODE_EXECUTION_20250825("code_execution_20250825")`

            - `CODE_EXECUTION_20260120("code_execution_20260120")`

          - `Optional<CacheControlEphemeral> cacheControl`

            Create a cache control breakpoint at this content block.

            - `JsonValue; type "ephemeral"constant`

              - `EPHEMERAL("ephemeral")`

            - `Optional<Ttl> ttl`

              The time-to-live for the cache control breakpoint.

              This may be one the following values:

              - `5m`: 5 minutes
              - `1h`: 1 hour

              Defaults to `5m`.

              - `TTL_5M("5m")`

              - `TTL_1H("1h")`

          - `Optional<Boolean> deferLoading`

            If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

          - `Optional<List<InputExample>> inputExamples`

          - `Optional<Boolean> strict`

            When true, guarantees schema validation on tool names and inputs

        - `class ToolTextEditor20250124:`

          - `JsonValue; name "str_replace_editor"constant`

            Name of the tool.

            This is how the tool will be called by the model and in `tool_use` blocks.

            - `STR_REPLACE_EDITOR("str_replace_editor")`

          - `JsonValue; type "text_editor_20250124"constant`

            - `TEXT_EDITOR_20250124("text_editor_20250124")`

          - `Optional<List<AllowedCaller>> allowedCallers`

            - `DIRECT("direct")`

            - `CODE_EXECUTION_20250825("code_execution_20250825")`

            - `CODE_EXECUTION_20260120("code_execution_20260120")`

          - `Optional<CacheControlEphemeral> cacheControl`

            Create a cache control breakpoint at this content block.

            - `JsonValue; type "ephemeral"constant`

              - `EPHEMERAL("ephemeral")`

            - `Optional<Ttl> ttl`

              The time-to-live for the cache control breakpoint.

              This may be one the following values:

              - `5m`: 5 minutes
              - `1h`: 1 hour

              Defaults to `5m`.

              - `TTL_5M("5m")`

              - `TTL_1H("1h")`

          - `Optional<Boolean> deferLoading`

            If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

          - `Optional<List<InputExample>> inputExamples`

          - `Optional<Boolean> strict`

            When true, guarantees schema validation on tool names and inputs

        - `class ToolTextEditor20250429:`

          - `JsonValue; name "str_replace_based_edit_tool"constant`

            Name of the tool.

            This is how the tool will be called by the model and in `tool_use` blocks.

            - `STR_REPLACE_BASED_EDIT_TOOL("str_replace_based_edit_tool")`

          - `JsonValue; type "text_editor_20250429"constant`

            - `TEXT_EDITOR_20250429("text_editor_20250429")`

          - `Optional<List<AllowedCaller>> allowedCallers`

            - `DIRECT("direct")`

            - `CODE_EXECUTION_20250825("code_execution_20250825")`

            - `CODE_EXECUTION_20260120("code_execution_20260120")`

          - `Optional<CacheControlEphemeral> cacheControl`

            Create a cache control breakpoint at this content block.

            - `JsonValue; type "ephemeral"constant`

              - `EPHEMERAL("ephemeral")`

            - `Optional<Ttl> ttl`

              The time-to-live for the cache control breakpoint.

              This may be one the following values:

              - `5m`: 5 minutes
              - `1h`: 1 hour

              Defaults to `5m`.

              - `TTL_5M("5m")`

              - `TTL_1H("1h")`

          - `Optional<Boolean> deferLoading`

            If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

          - `Optional<List<InputExample>> inputExamples`

          - `Optional<Boolean> strict`

            When true, guarantees schema validation on tool names and inputs

        - `class ToolTextEditor20250728:`

          - `JsonValue; name "str_replace_based_edit_tool"constant`

            Name of the tool.

            This is how the tool will be called by the model and in `tool_use` blocks.

            - `STR_REPLACE_BASED_EDIT_TOOL("str_replace_based_edit_tool")`

          - `JsonValue; type "text_editor_20250728"constant`

            - `TEXT_EDITOR_20250728("text_editor_20250728")`

          - `Optional<List<AllowedCaller>> allowedCallers`

            - `DIRECT("direct")`

            - `CODE_EXECUTION_20250825("code_execution_20250825")`

            - `CODE_EXECUTION_20260120("code_execution_20260120")`

          - `Optional<CacheControlEphemeral> cacheControl`

            Create a cache control breakpoint at this content block.

            - `JsonValue; type "ephemeral"constant`

              - `EPHEMERAL("ephemeral")`

            - `Optional<Ttl> ttl`

              The time-to-live for the cache control breakpoint.

              This may be one the following values:

              - `5m`: 5 minutes
              - `1h`: 1 hour

              Defaults to `5m`.

              - `TTL_5M("5m")`

              - `TTL_1H("1h")`

          - `Optional<Boolean> deferLoading`

            If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

          - `Optional<List<InputExample>> inputExamples`

          - `Optional<Long> maxCharacters`

            Maximum number of characters to display when viewing a file. If not specified, defaults to displaying the full file.

          - `Optional<Boolean> strict`

            When true, guarantees schema validation on tool names and inputs

        - `class WebSearchTool20250305:`

          - `JsonValue; name "web_search"constant`

            Name of the tool.

            This is how the tool will be called by the model and in `tool_use` blocks.

            - `WEB_SEARCH("web_search")`

          - `JsonValue; type "web_search_20250305"constant`

            - `WEB_SEARCH_20250305("web_search_20250305")`

          - `Optional<List<AllowedCaller>> allowedCallers`

            - `DIRECT("direct")`

            - `CODE_EXECUTION_20250825("code_execution_20250825")`

            - `CODE_EXECUTION_20260120("code_execution_20260120")`

          - `Optional<List<String>> allowedDomains`

            If provided, only these domains will be included in results. Cannot be used alongside `blocked_domains`.

          - `Optional<List<String>> blockedDomains`

            If provided, these domains will never appear in results. Cannot be used alongside `allowed_domains`.

          - `Optional<CacheControlEphemeral> cacheControl`

            Create a cache control breakpoint at this content block.

            - `JsonValue; type "ephemeral"constant`

              - `EPHEMERAL("ephemeral")`

            - `Optional<Ttl> ttl`

              The time-to-live for the cache control breakpoint.

              This may be one the following values:

              - `5m`: 5 minutes
              - `1h`: 1 hour

              Defaults to `5m`.

              - `TTL_5M("5m")`

              - `TTL_1H("1h")`

          - `Optional<Boolean> deferLoading`

            If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

          - `Optional<Long> maxUses`

            Maximum number of times the tool can be used in the API request.

          - `Optional<Boolean> strict`

            When true, guarantees schema validation on tool names and inputs

          - `Optional<UserLocation> userLocation`

            Parameters for the user's location. Used to provide more relevant search results.

            - `JsonValue; type "approximate"constant`

              - `APPROXIMATE("approximate")`

            - `Optional<String> city`

              The city of the user.

            - `Optional<String> country`

              The two letter [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) of the user.

            - `Optional<String> region`

              The region of the user.

            - `Optional<String> timezone`

              The [IANA timezone](https://nodatime.org/TimeZones) of the user.

        - `class WebFetchTool20250910:`

          - `JsonValue; name "web_fetch"constant`

            Name of the tool.

            This is how the tool will be called by the model and in `tool_use` blocks.

            - `WEB_FETCH("web_fetch")`

          - `JsonValue; type "web_fetch_20250910"constant`

            - `WEB_FETCH_20250910("web_fetch_20250910")`

          - `Optional<List<AllowedCaller>> allowedCallers`

            - `DIRECT("direct")`

            - `CODE_EXECUTION_20250825("code_execution_20250825")`

            - `CODE_EXECUTION_20260120("code_execution_20260120")`

          - `Optional<List<String>> allowedDomains`

            List of domains to allow fetching from

          - `Optional<List<String>> blockedDomains`

            List of domains to block fetching from

          - `Optional<CacheControlEphemeral> cacheControl`

            Create a cache control breakpoint at this content block.

            - `JsonValue; type "ephemeral"constant`

              - `EPHEMERAL("ephemeral")`

            - `Optional<Ttl> ttl`

              The time-to-live for the cache control breakpoint.

              This may be one the following values:

              - `5m`: 5 minutes
              - `1h`: 1 hour

              Defaults to `5m`.

              - `TTL_5M("5m")`

              - `TTL_1H("1h")`

          - `Optional<CitationsConfigParam> citations`

            Citations configuration for fetched documents. Citations are disabled by default.

            - `Optional<Boolean> enabled`

          - `Optional<Boolean> deferLoading`

            If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

          - `Optional<Long> maxContentTokens`

            Maximum number of tokens used by including web page text content in the context. The limit is approximate and does not apply to binary content such as PDFs.

          - `Optional<Long> maxUses`

            Maximum number of times the tool can be used in the API request.

          - `Optional<Boolean> strict`

            When true, guarantees schema validation on tool names and inputs

        - `class WebSearchTool20260209:`

          - `JsonValue; name "web_search"constant`

            Name of the tool.

            This is how the tool will be called by the model and in `tool_use` blocks.

            - `WEB_SEARCH("web_search")`

          - `JsonValue; type "web_search_20260209"constant`

            - `WEB_SEARCH_20260209("web_search_20260209")`

          - `Optional<List<AllowedCaller>> allowedCallers`

            - `DIRECT("direct")`

            - `CODE_EXECUTION_20250825("code_execution_20250825")`

            - `CODE_EXECUTION_20260120("code_execution_20260120")`

          - `Optional<List<String>> allowedDomains`

            If provided, only these domains will be included in results. Cannot be used alongside `blocked_domains`.

          - `Optional<List<String>> blockedDomains`

            If provided, these domains will never appear in results. Cannot be used alongside `allowed_domains`.

          - `Optional<CacheControlEphemeral> cacheControl`

            Create a cache control breakpoint at this content block.

            - `JsonValue; type "ephemeral"constant`

              - `EPHEMERAL("ephemeral")`

            - `Optional<Ttl> ttl`

              The time-to-live for the cache control breakpoint.

              This may be one the following values:

              - `5m`: 5 minutes
              - `1h`: 1 hour

              Defaults to `5m`.

              - `TTL_5M("5m")`

              - `TTL_1H("1h")`

          - `Optional<Boolean> deferLoading`

            If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

          - `Optional<Long> maxUses`

            Maximum number of times the tool can be used in the API request.

          - `Optional<Boolean> strict`

            When true, guarantees schema validation on tool names and inputs

          - `Optional<UserLocation> userLocation`

            Parameters for the user's location. Used to provide more relevant search results.

            - `JsonValue; type "approximate"constant`

              - `APPROXIMATE("approximate")`

            - `Optional<String> city`

              The city of the user.

            - `Optional<String> country`

              The two letter [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) of the user.

            - `Optional<String> region`

              The region of the user.

            - `Optional<String> timezone`

              The [IANA timezone](https://nodatime.org/TimeZones) of the user.

        - `class WebFetchTool20260209:`

          - `JsonValue; name "web_fetch"constant`

            Name of the tool.

            This is how the tool will be called by the model and in `tool_use` blocks.

            - `WEB_FETCH("web_fetch")`

          - `JsonValue; type "web_fetch_20260209"constant`

            - `WEB_FETCH_20260209("web_fetch_20260209")`

          - `Optional<List<AllowedCaller>> allowedCallers`

            - `DIRECT("direct")`

            - `CODE_EXECUTION_20250825("code_execution_20250825")`

            - `CODE_EXECUTION_20260120("code_execution_20260120")`

          - `Optional<List<String>> allowedDomains`

            List of domains to allow fetching from

          - `Optional<List<String>> blockedDomains`

            List of domains to block fetching from

          - `Optional<CacheControlEphemeral> cacheControl`

            Create a cache control breakpoint at this content block.

            - `JsonValue; type "ephemeral"constant`

              - `EPHEMERAL("ephemeral")`

            - `Optional<Ttl> ttl`

              The time-to-live for the cache control breakpoint.

              This may be one the following values:

              - `5m`: 5 minutes
              - `1h`: 1 hour

              Defaults to `5m`.

              - `TTL_5M("5m")`

              - `TTL_1H("1h")`

          - `Optional<CitationsConfigParam> citations`

            Citations configuration for fetched documents. Citations are disabled by default.

            - `Optional<Boolean> enabled`

          - `Optional<Boolean> deferLoading`

            If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

          - `Optional<Long> maxContentTokens`

            Maximum number of tokens used by including web page text content in the context. The limit is approximate and does not apply to binary content such as PDFs.

          - `Optional<Long> maxUses`

            Maximum number of times the tool can be used in the API request.

          - `Optional<Boolean> strict`

            When true, guarantees schema validation on tool names and inputs

        - `class ToolSearchToolBm25_20251119:`

          - `JsonValue; name "tool_search_tool_bm25"constant`

            Name of the tool.

            This is how the tool will be called by the model and in `tool_use` blocks.

            - `TOOL_SEARCH_TOOL_BM25("tool_search_tool_bm25")`

          - `Type type`

            - `TOOL_SEARCH_TOOL_BM25_20251119("tool_search_tool_bm25_20251119")`

            - `TOOL_SEARCH_TOOL_BM25("tool_search_tool_bm25")`

          - `Optional<List<AllowedCaller>> allowedCallers`

            - `DIRECT("direct")`

            - `CODE_EXECUTION_20250825("code_execution_20250825")`

            - `CODE_EXECUTION_20260120("code_execution_20260120")`

          - `Optional<CacheControlEphemeral> cacheControl`

            Create a cache control breakpoint at this content block.

            - `JsonValue; type "ephemeral"constant`

              - `EPHEMERAL("ephemeral")`

            - `Optional<Ttl> ttl`

              The time-to-live for the cache control breakpoint.

              This may be one the following values:

              - `5m`: 5 minutes
              - `1h`: 1 hour

              Defaults to `5m`.

              - `TTL_5M("5m")`

              - `TTL_1H("1h")`

          - `Optional<Boolean> deferLoading`

            If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

          - `Optional<Boolean> strict`

            When true, guarantees schema validation on tool names and inputs

        - `class ToolSearchToolRegex20251119:`

          - `JsonValue; name "tool_search_tool_regex"constant`

            Name of the tool.

            This is how the tool will be called by the model and in `tool_use` blocks.

            - `TOOL_SEARCH_TOOL_REGEX("tool_search_tool_regex")`

          - `Type type`

            - `TOOL_SEARCH_TOOL_REGEX_20251119("tool_search_tool_regex_20251119")`

            - `TOOL_SEARCH_TOOL_REGEX("tool_search_tool_regex")`

          - `Optional<List<AllowedCaller>> allowedCallers`

            - `DIRECT("direct")`

            - `CODE_EXECUTION_20250825("code_execution_20250825")`

            - `CODE_EXECUTION_20260120("code_execution_20260120")`

          - `Optional<CacheControlEphemeral> cacheControl`

            Create a cache control breakpoint at this content block.

            - `JsonValue; type "ephemeral"constant`

              - `EPHEMERAL("ephemeral")`

            - `Optional<Ttl> ttl`

              The time-to-live for the cache control breakpoint.

              This may be one the following values:

              - `5m`: 5 minutes
              - `1h`: 1 hour

              Defaults to `5m`.

              - `TTL_5M("5m")`

              - `TTL_1H("1h")`

          - `Optional<Boolean> deferLoading`

            If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

          - `Optional<Boolean> strict`

            When true, guarantees schema validation on tool names and inputs

      - `Optional<Long> topK`

        Only sample from the top K options for each subsequent token.

        Used to remove "long tail" low probability responses. [Learn more technical details here](https://towardsdatascience.com/how-to-sample-from-language-models-682bceb97277).

        Recommended for advanced use cases only. You usually only need to use `temperature`.

      - `Optional<Double> topP`

        Use nucleus sampling.

        In nucleus sampling, we compute the cumulative distribution over all the options for each subsequent token in decreasing probability order and cut it off once it reaches a particular probability specified by `top_p`. You should either alter `temperature` or `top_p`, but not both.

        Recommended for advanced use cases only. You usually only need to use `temperature`.

### Returns

- `class MessageBatch:`

  - `String id`

    Unique object identifier.

    The format and length of IDs may change over time.

  - `Optional<LocalDateTime> archivedAt`

    RFC 3339 datetime string representing the time at which the Message Batch was archived and its results became unavailable.

  - `Optional<LocalDateTime> cancelInitiatedAt`

    RFC 3339 datetime string representing the time at which cancellation was initiated for the Message Batch. Specified only if cancellation was initiated.

  - `LocalDateTime createdAt`

    RFC 3339 datetime string representing the time at which the Message Batch was created.

  - `Optional<LocalDateTime> endedAt`

    RFC 3339 datetime string representing the time at which processing for the Message Batch ended. Specified only once processing ends.

    Processing ends when every request in a Message Batch has either succeeded, errored, canceled, or expired.

  - `LocalDateTime expiresAt`

    RFC 3339 datetime string representing the time at which the Message Batch will expire and end processing, which is 24 hours after creation.

  - `ProcessingStatus processingStatus`

    Processing status of the Message Batch.

    - `IN_PROGRESS("in_progress")`

    - `CANCELING("canceling")`

    - `ENDED("ended")`

  - `MessageBatchRequestCounts requestCounts`

    Tallies requests within the Message Batch, categorized by their status.

    Requests start as `processing` and move to one of the other statuses only once processing of the entire batch ends. The sum of all values always matches the total number of requests in the batch.

    - `long canceled`

      Number of requests in the Message Batch that have been canceled.

      This is zero until processing of the entire Message Batch has ended.

    - `long errored`

      Number of requests in the Message Batch that encountered an error.

      This is zero until processing of the entire Message Batch has ended.

    - `long expired`

      Number of requests in the Message Batch that have expired.

      This is zero until processing of the entire Message Batch has ended.

    - `long processing`

      Number of requests in the Message Batch that are processing.

    - `long succeeded`

      Number of requests in the Message Batch that have completed successfully.

      This is zero until processing of the entire Message Batch has ended.

  - `Optional<String> resultsUrl`

    URL to a `.jsonl` file containing the results of the Message Batch requests. Specified only once processing ends.

    Results in the file are not guaranteed to be in the same order as requests. Use the `custom_id` field to match results to requests.

  - `JsonValue; type "message_batch"constant`

    Object type.

    For Message Batches, this is always `"message_batch"`.

    - `MESSAGE_BATCH("message_batch")`

### Example

```java
package com.anthropic.example;

import com.anthropic.client.AnthropicClient;
import com.anthropic.client.okhttp.AnthropicOkHttpClient;
import com.anthropic.models.messages.Model;
import com.anthropic.models.messages.batches.BatchCreateParams;
import com.anthropic.models.messages.batches.MessageBatch;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        AnthropicClient client = AnthropicOkHttpClient.fromEnv();

        BatchCreateParams params = BatchCreateParams.builder()
            .addRequest(BatchCreateParams.Request.builder()
                .customId("my-custom-id-1")
                .params(BatchCreateParams.Request.Params.builder()
                    .maxTokens(1024L)
                    .addUserMessage("Hello, world")
                    .model(Model.CLAUDE_OPUS_4_6)
                    .build())
                .build())
            .build();
        MessageBatch messageBatch = client.messages().batches().create(params);
    }
}
```

## Retrieve

`MessageBatch messages().batches().retrieve(BatchRetrieveParamsparams = BatchRetrieveParams.none(), RequestOptionsrequestOptions = RequestOptions.none())`

**get** `/v1/messages/batches/{message_batch_id}`

This endpoint is idempotent and can be used to poll for Message Batch completion. To access the results of a Message Batch, make a request to the `results_url` field in the response.

Learn more about the Message Batches API in our [user guide](https://docs.claude.com/en/docs/build-with-claude/batch-processing)

### Parameters

- `BatchRetrieveParams params`

  - `Optional<String> messageBatchId`

    ID of the Message Batch.

### Returns

- `class MessageBatch:`

  - `String id`

    Unique object identifier.

    The format and length of IDs may change over time.

  - `Optional<LocalDateTime> archivedAt`

    RFC 3339 datetime string representing the time at which the Message Batch was archived and its results became unavailable.

  - `Optional<LocalDateTime> cancelInitiatedAt`

    RFC 3339 datetime string representing the time at which cancellation was initiated for the Message Batch. Specified only if cancellation was initiated.

  - `LocalDateTime createdAt`

    RFC 3339 datetime string representing the time at which the Message Batch was created.

  - `Optional<LocalDateTime> endedAt`

    RFC 3339 datetime string representing the time at which processing for the Message Batch ended. Specified only once processing ends.

    Processing ends when every request in a Message Batch has either succeeded, errored, canceled, or expired.

  - `LocalDateTime expiresAt`

    RFC 3339 datetime string representing the time at which the Message Batch will expire and end processing, which is 24 hours after creation.

  - `ProcessingStatus processingStatus`

    Processing status of the Message Batch.

    - `IN_PROGRESS("in_progress")`

    - `CANCELING("canceling")`

    - `ENDED("ended")`

  - `MessageBatchRequestCounts requestCounts`

    Tallies requests within the Message Batch, categorized by their status.

    Requests start as `processing` and move to one of the other statuses only once processing of the entire batch ends. The sum of all values always matches the total number of requests in the batch.

    - `long canceled`

      Number of requests in the Message Batch that have been canceled.

      This is zero until processing of the entire Message Batch has ended.

    - `long errored`

      Number of requests in the Message Batch that encountered an error.

      This is zero until processing of the entire Message Batch has ended.

    - `long expired`

      Number of requests in the Message Batch that have expired.

      This is zero until processing of the entire Message Batch has ended.

    - `long processing`

      Number of requests in the Message Batch that are processing.

    - `long succeeded`

      Number of requests in the Message Batch that have completed successfully.

      This is zero until processing of the entire Message Batch has ended.

  - `Optional<String> resultsUrl`

    URL to a `.jsonl` file containing the results of the Message Batch requests. Specified only once processing ends.

    Results in the file are not guaranteed to be in the same order as requests. Use the `custom_id` field to match results to requests.

  - `JsonValue; type "message_batch"constant`

    Object type.

    For Message Batches, this is always `"message_batch"`.

    - `MESSAGE_BATCH("message_batch")`

### Example

```java
package com.anthropic.example;

import com.anthropic.client.AnthropicClient;
import com.anthropic.client.okhttp.AnthropicOkHttpClient;
import com.anthropic.models.messages.batches.BatchRetrieveParams;
import com.anthropic.models.messages.batches.MessageBatch;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        AnthropicClient client = AnthropicOkHttpClient.fromEnv();

        MessageBatch messageBatch = client.messages().batches().retrieve("message_batch_id");
    }
}
```

## List

`BatchListPage messages().batches().list(BatchListParamsparams = BatchListParams.none(), RequestOptionsrequestOptions = RequestOptions.none())`

**get** `/v1/messages/batches`

List all Message Batches within a Workspace. Most recently created batches are returned first.

Learn more about the Message Batches API in our [user guide](https://docs.claude.com/en/docs/build-with-claude/batch-processing)

### Parameters

- `BatchListParams params`

  - `Optional<String> afterId`

    ID of the object to use as a cursor for pagination. When provided, returns the page of results immediately after this object.

  - `Optional<String> beforeId`

    ID of the object to use as a cursor for pagination. When provided, returns the page of results immediately before this object.

  - `Optional<Long> limit`

    Number of items to return per page.

    Defaults to `20`. Ranges from `1` to `1000`.

### Returns

- `class MessageBatch:`

  - `String id`

    Unique object identifier.

    The format and length of IDs may change over time.

  - `Optional<LocalDateTime> archivedAt`

    RFC 3339 datetime string representing the time at which the Message Batch was archived and its results became unavailable.

  - `Optional<LocalDateTime> cancelInitiatedAt`

    RFC 3339 datetime string representing the time at which cancellation was initiated for the Message Batch. Specified only if cancellation was initiated.

  - `LocalDateTime createdAt`

    RFC 3339 datetime string representing the time at which the Message Batch was created.

  - `Optional<LocalDateTime> endedAt`

    RFC 3339 datetime string representing the time at which processing for the Message Batch ended. Specified only once processing ends.

    Processing ends when every request in a Message Batch has either succeeded, errored, canceled, or expired.

  - `LocalDateTime expiresAt`

    RFC 3339 datetime string representing the time at which the Message Batch will expire and end processing, which is 24 hours after creation.

  - `ProcessingStatus processingStatus`

    Processing status of the Message Batch.

    - `IN_PROGRESS("in_progress")`

    - `CANCELING("canceling")`

    - `ENDED("ended")`

  - `MessageBatchRequestCounts requestCounts`

    Tallies requests within the Message Batch, categorized by their status.

    Requests start as `processing` and move to one of the other statuses only once processing of the entire batch ends. The sum of all values always matches the total number of requests in the batch.

    - `long canceled`

      Number of requests in the Message Batch that have been canceled.

      This is zero until processing of the entire Message Batch has ended.

    - `long errored`

      Number of requests in the Message Batch that encountered an error.

      This is zero until processing of the entire Message Batch has ended.

    - `long expired`

      Number of requests in the Message Batch that have expired.

      This is zero until processing of the entire Message Batch has ended.

    - `long processing`

      Number of requests in the Message Batch that are processing.

    - `long succeeded`

      Number of requests in the Message Batch that have completed successfully.

      This is zero until processing of the entire Message Batch has ended.

  - `Optional<String> resultsUrl`

    URL to a `.jsonl` file containing the results of the Message Batch requests. Specified only once processing ends.

    Results in the file are not guaranteed to be in the same order as requests. Use the `custom_id` field to match results to requests.

  - `JsonValue; type "message_batch"constant`

    Object type.

    For Message Batches, this is always `"message_batch"`.

    - `MESSAGE_BATCH("message_batch")`

### Example

```java
package com.anthropic.example;

import com.anthropic.client.AnthropicClient;
import com.anthropic.client.okhttp.AnthropicOkHttpClient;
import com.anthropic.models.messages.batches.BatchListPage;
import com.anthropic.models.messages.batches.BatchListParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        AnthropicClient client = AnthropicOkHttpClient.fromEnv();

        BatchListPage page = client.messages().batches().list();
    }
}
```

## Cancel

`MessageBatch messages().batches().cancel(BatchCancelParamsparams = BatchCancelParams.none(), RequestOptionsrequestOptions = RequestOptions.none())`

**post** `/v1/messages/batches/{message_batch_id}/cancel`

Batches may be canceled any time before processing ends. Once cancellation is initiated, the batch enters a `canceling` state, at which time the system may complete any in-progress, non-interruptible requests before finalizing cancellation.

The number of canceled requests is specified in `request_counts`. To determine which requests were canceled, check the individual results within the batch. Note that cancellation may not result in any canceled requests if they were non-interruptible.

Learn more about the Message Batches API in our [user guide](https://docs.claude.com/en/docs/build-with-claude/batch-processing)

### Parameters

- `BatchCancelParams params`

  - `Optional<String> messageBatchId`

    ID of the Message Batch.

### Returns

- `class MessageBatch:`

  - `String id`

    Unique object identifier.

    The format and length of IDs may change over time.

  - `Optional<LocalDateTime> archivedAt`

    RFC 3339 datetime string representing the time at which the Message Batch was archived and its results became unavailable.

  - `Optional<LocalDateTime> cancelInitiatedAt`

    RFC 3339 datetime string representing the time at which cancellation was initiated for the Message Batch. Specified only if cancellation was initiated.

  - `LocalDateTime createdAt`

    RFC 3339 datetime string representing the time at which the Message Batch was created.

  - `Optional<LocalDateTime> endedAt`

    RFC 3339 datetime string representing the time at which processing for the Message Batch ended. Specified only once processing ends.

    Processing ends when every request in a Message Batch has either succeeded, errored, canceled, or expired.

  - `LocalDateTime expiresAt`

    RFC 3339 datetime string representing the time at which the Message Batch will expire and end processing, which is 24 hours after creation.

  - `ProcessingStatus processingStatus`

    Processing status of the Message Batch.

    - `IN_PROGRESS("in_progress")`

    - `CANCELING("canceling")`

    - `ENDED("ended")`

  - `MessageBatchRequestCounts requestCounts`

    Tallies requests within the Message Batch, categorized by their status.

    Requests start as `processing` and move to one of the other statuses only once processing of the entire batch ends. The sum of all values always matches the total number of requests in the batch.

    - `long canceled`

      Number of requests in the Message Batch that have been canceled.

      This is zero until processing of the entire Message Batch has ended.

    - `long errored`

      Number of requests in the Message Batch that encountered an error.

      This is zero until processing of the entire Message Batch has ended.

    - `long expired`

      Number of requests in the Message Batch that have expired.

      This is zero until processing of the entire Message Batch has ended.

    - `long processing`

      Number of requests in the Message Batch that are processing.

    - `long succeeded`

      Number of requests in the Message Batch that have completed successfully.

      This is zero until processing of the entire Message Batch has ended.

  - `Optional<String> resultsUrl`

    URL to a `.jsonl` file containing the results of the Message Batch requests. Specified only once processing ends.

    Results in the file are not guaranteed to be in the same order as requests. Use the `custom_id` field to match results to requests.

  - `JsonValue; type "message_batch"constant`

    Object type.

    For Message Batches, this is always `"message_batch"`.

    - `MESSAGE_BATCH("message_batch")`

### Example

```java
package com.anthropic.example;

import com.anthropic.client.AnthropicClient;
import com.anthropic.client.okhttp.AnthropicOkHttpClient;
import com.anthropic.models.messages.batches.BatchCancelParams;
import com.anthropic.models.messages.batches.MessageBatch;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        AnthropicClient client = AnthropicOkHttpClient.fromEnv();

        MessageBatch messageBatch = client.messages().batches().cancel("message_batch_id");
    }
}
```

## Delete

`DeletedMessageBatch messages().batches().delete(BatchDeleteParamsparams = BatchDeleteParams.none(), RequestOptionsrequestOptions = RequestOptions.none())`

**delete** `/v1/messages/batches/{message_batch_id}`

Delete a Message Batch.

Message Batches can only be deleted once they've finished processing. If you'd like to delete an in-progress batch, you must first cancel it.

Learn more about the Message Batches API in our [user guide](https://docs.claude.com/en/docs/build-with-claude/batch-processing)

### Parameters

- `BatchDeleteParams params`

  - `Optional<String> messageBatchId`

    ID of the Message Batch.

### Returns

- `class DeletedMessageBatch:`

  - `String id`

    ID of the Message Batch.

  - `JsonValue; type "message_batch_deleted"constant`

    Deleted object type.

    For Message Batches, this is always `"message_batch_deleted"`.

    - `MESSAGE_BATCH_DELETED("message_batch_deleted")`

### Example

```java
package com.anthropic.example;

import com.anthropic.client.AnthropicClient;
import com.anthropic.client.okhttp.AnthropicOkHttpClient;
import com.anthropic.models.messages.batches.BatchDeleteParams;
import com.anthropic.models.messages.batches.DeletedMessageBatch;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        AnthropicClient client = AnthropicOkHttpClient.fromEnv();

        DeletedMessageBatch deletedMessageBatch = client.messages().batches().delete("message_batch_id");
    }
}
```

## Results

`MessageBatchIndividualResponse messages().batches().resultsStreaming(BatchResultsParamsparams = BatchResultsParams.none(), RequestOptionsrequestOptions = RequestOptions.none())`

**get** `/v1/messages/batches/{message_batch_id}/results`

Streams the results of a Message Batch as a `.jsonl` file.

Each line in the file is a JSON object containing the result of a single request in the Message Batch. Results are not guaranteed to be in the same order as requests. Use the `custom_id` field to match results to requests.

Learn more about the Message Batches API in our [user guide](https://docs.claude.com/en/docs/build-with-claude/batch-processing)

### Parameters

- `BatchResultsParams params`

  - `Optional<String> messageBatchId`

    ID of the Message Batch.

### Returns

- `class MessageBatchIndividualResponse:`

  This is a single line in the response `.jsonl` file and does not represent the response as a whole.

  - `String customId`

    Developer-provided ID created for each request in a Message Batch. Useful for matching results to requests, as results may be given out of request order.

    Must be unique for each request within the Message Batch.

  - `MessageBatchResult result`

    Processing result for this request.

    Contains a Message output if processing was successful, an error response if processing failed, or the reason why processing was not attempted, such as cancellation or expiration.

    - `class MessageBatchSucceededResult:`

      - `Message message`

        - `String id`

          Unique object identifier.

          The format and length of IDs may change over time.

        - `Optional<Container> container`

          Information about the container used in the request (for the code execution tool)

          - `String id`

            Identifier for the container used in this request

          - `LocalDateTime expiresAt`

            The time at which the container will expire.

        - `List<ContentBlock> content`

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

          - `class TextBlock:`

            - `Optional<List<TextCitation>> citations`

              Citations supporting the text block.

              The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

              - `class CitationCharLocation:`

                - `String citedText`

                - `long documentIndex`

                - `Optional<String> documentTitle`

                - `long endCharIndex`

                - `Optional<String> fileId`

                - `long startCharIndex`

                - `JsonValue; type "char_location"constant`

                  - `CHAR_LOCATION("char_location")`

              - `class CitationPageLocation:`

                - `String citedText`

                - `long documentIndex`

                - `Optional<String> documentTitle`

                - `long endPageNumber`

                - `Optional<String> fileId`

                - `long startPageNumber`

                - `JsonValue; type "page_location"constant`

                  - `PAGE_LOCATION("page_location")`

              - `class CitationContentBlockLocation:`

                - `String citedText`

                - `long documentIndex`

                - `Optional<String> documentTitle`

                - `long endBlockIndex`

                - `Optional<String> fileId`

                - `long startBlockIndex`

                - `JsonValue; type "content_block_location"constant`

                  - `CONTENT_BLOCK_LOCATION("content_block_location")`

              - `class CitationsWebSearchResultLocation:`

                - `String citedText`

                - `String encryptedIndex`

                - `Optional<String> title`

                - `JsonValue; type "web_search_result_location"constant`

                  - `WEB_SEARCH_RESULT_LOCATION("web_search_result_location")`

                - `String url`

              - `class CitationsSearchResultLocation:`

                - `String citedText`

                - `long endBlockIndex`

                - `long searchResultIndex`

                - `String source`

                - `long startBlockIndex`

                - `Optional<String> title`

                - `JsonValue; type "search_result_location"constant`

                  - `SEARCH_RESULT_LOCATION("search_result_location")`

            - `String text`

            - `JsonValue; type "text"constant`

              - `TEXT("text")`

          - `class ThinkingBlock:`

            - `String signature`

            - `String thinking`

            - `JsonValue; type "thinking"constant`

              - `THINKING("thinking")`

          - `class RedactedThinkingBlock:`

            - `String data`

            - `JsonValue; type "redacted_thinking"constant`

              - `REDACTED_THINKING("redacted_thinking")`

          - `class ToolUseBlock:`

            - `String id`

            - `Caller caller`

              Tool invocation directly from the model.

              - `class DirectCaller:`

                Tool invocation directly from the model.

                - `JsonValue; type "direct"constant`

                  - `DIRECT("direct")`

              - `class ServerToolCaller:`

                Tool invocation generated by a server-side tool.

                - `String toolId`

                - `JsonValue; type "code_execution_20250825"constant`

                  - `CODE_EXECUTION_20250825("code_execution_20250825")`

              - `class ServerToolCaller20260120:`

                - `String toolId`

                - `JsonValue; type "code_execution_20260120"constant`

                  - `CODE_EXECUTION_20260120("code_execution_20260120")`

            - `Input input`

            - `String name`

            - `JsonValue; type "tool_use"constant`

              - `TOOL_USE("tool_use")`

          - `class ServerToolUseBlock:`

            - `String id`

            - `Caller caller`

              Tool invocation directly from the model.

              - `class DirectCaller:`

                Tool invocation directly from the model.

                - `JsonValue; type "direct"constant`

                  - `DIRECT("direct")`

              - `class ServerToolCaller:`

                Tool invocation generated by a server-side tool.

                - `String toolId`

                - `JsonValue; type "code_execution_20250825"constant`

                  - `CODE_EXECUTION_20250825("code_execution_20250825")`

              - `class ServerToolCaller20260120:`

                - `String toolId`

                - `JsonValue; type "code_execution_20260120"constant`

                  - `CODE_EXECUTION_20260120("code_execution_20260120")`

            - `Input input`

            - `Name name`

              - `WEB_SEARCH("web_search")`

              - `WEB_FETCH("web_fetch")`

              - `CODE_EXECUTION("code_execution")`

              - `BASH_CODE_EXECUTION("bash_code_execution")`

              - `TEXT_EDITOR_CODE_EXECUTION("text_editor_code_execution")`

              - `TOOL_SEARCH_TOOL_REGEX("tool_search_tool_regex")`

              - `TOOL_SEARCH_TOOL_BM25("tool_search_tool_bm25")`

            - `JsonValue; type "server_tool_use"constant`

              - `SERVER_TOOL_USE("server_tool_use")`

          - `class WebSearchToolResultBlock:`

            - `Caller caller`

              Tool invocation directly from the model.

              - `class DirectCaller:`

                Tool invocation directly from the model.

                - `JsonValue; type "direct"constant`

                  - `DIRECT("direct")`

              - `class ServerToolCaller:`

                Tool invocation generated by a server-side tool.

                - `String toolId`

                - `JsonValue; type "code_execution_20250825"constant`

                  - `CODE_EXECUTION_20250825("code_execution_20250825")`

              - `class ServerToolCaller20260120:`

                - `String toolId`

                - `JsonValue; type "code_execution_20260120"constant`

                  - `CODE_EXECUTION_20260120("code_execution_20260120")`

            - `WebSearchToolResultBlockContent content`

              - `class WebSearchToolResultError:`

                - `WebSearchToolResultErrorCode errorCode`

                  - `INVALID_TOOL_INPUT("invalid_tool_input")`

                  - `UNAVAILABLE("unavailable")`

                  - `MAX_USES_EXCEEDED("max_uses_exceeded")`

                  - `TOO_MANY_REQUESTS("too_many_requests")`

                  - `QUERY_TOO_LONG("query_too_long")`

                  - `REQUEST_TOO_LARGE("request_too_large")`

                - `JsonValue; type "web_search_tool_result_error"constant`

                  - `WEB_SEARCH_TOOL_RESULT_ERROR("web_search_tool_result_error")`

              - `List<WebSearchResultBlock>`

                - `String encryptedContent`

                - `Optional<String> pageAge`

                - `String title`

                - `JsonValue; type "web_search_result"constant`

                  - `WEB_SEARCH_RESULT("web_search_result")`

                - `String url`

            - `String toolUseId`

            - `JsonValue; type "web_search_tool_result"constant`

              - `WEB_SEARCH_TOOL_RESULT("web_search_tool_result")`

          - `class WebFetchToolResultBlock:`

            - `Caller caller`

              Tool invocation directly from the model.

              - `class DirectCaller:`

                Tool invocation directly from the model.

                - `JsonValue; type "direct"constant`

                  - `DIRECT("direct")`

              - `class ServerToolCaller:`

                Tool invocation generated by a server-side tool.

                - `String toolId`

                - `JsonValue; type "code_execution_20250825"constant`

                  - `CODE_EXECUTION_20250825("code_execution_20250825")`

              - `class ServerToolCaller20260120:`

                - `String toolId`

                - `JsonValue; type "code_execution_20260120"constant`

                  - `CODE_EXECUTION_20260120("code_execution_20260120")`

            - `Content content`

              - `class WebFetchToolResultErrorBlock:`

                - `WebFetchToolResultErrorCode errorCode`

                  - `INVALID_TOOL_INPUT("invalid_tool_input")`

                  - `URL_TOO_LONG("url_too_long")`

                  - `URL_NOT_ALLOWED("url_not_allowed")`

                  - `URL_NOT_ACCESSIBLE("url_not_accessible")`

                  - `UNSUPPORTED_CONTENT_TYPE("unsupported_content_type")`

                  - `TOO_MANY_REQUESTS("too_many_requests")`

                  - `MAX_USES_EXCEEDED("max_uses_exceeded")`

                  - `UNAVAILABLE("unavailable")`

                - `JsonValue; type "web_fetch_tool_result_error"constant`

                  - `WEB_FETCH_TOOL_RESULT_ERROR("web_fetch_tool_result_error")`

              - `class WebFetchBlock:`

                - `DocumentBlock content`

                  - `Optional<CitationsConfig> citations`

                    Citation configuration for the document

                    - `boolean enabled`

                  - `Source source`

                    - `class Base64PdfSource:`

                      - `String data`

                      - `JsonValue; mediaType "application/pdf"constant`

                        - `APPLICATION_PDF("application/pdf")`

                      - `JsonValue; type "base64"constant`

                        - `BASE64("base64")`

                    - `class PlainTextSource:`

                      - `String data`

                      - `JsonValue; mediaType "text/plain"constant`

                        - `TEXT_PLAIN("text/plain")`

                      - `JsonValue; type "text"constant`

                        - `TEXT("text")`

                  - `Optional<String> title`

                    The title of the document

                  - `JsonValue; type "document"constant`

                    - `DOCUMENT("document")`

                - `Optional<String> retrievedAt`

                  ISO 8601 timestamp when the content was retrieved

                - `JsonValue; type "web_fetch_result"constant`

                  - `WEB_FETCH_RESULT("web_fetch_result")`

                - `String url`

                  Fetched content URL

            - `String toolUseId`

            - `JsonValue; type "web_fetch_tool_result"constant`

              - `WEB_FETCH_TOOL_RESULT("web_fetch_tool_result")`

          - `class CodeExecutionToolResultBlock:`

            - `CodeExecutionToolResultBlockContent content`

              Code execution result with encrypted stdout for PFC + web_search results.

              - `class CodeExecutionToolResultError:`

                - `CodeExecutionToolResultErrorCode errorCode`

                  - `INVALID_TOOL_INPUT("invalid_tool_input")`

                  - `UNAVAILABLE("unavailable")`

                  - `TOO_MANY_REQUESTS("too_many_requests")`

                  - `EXECUTION_TIME_EXCEEDED("execution_time_exceeded")`

                - `JsonValue; type "code_execution_tool_result_error"constant`

                  - `CODE_EXECUTION_TOOL_RESULT_ERROR("code_execution_tool_result_error")`

              - `class CodeExecutionResultBlock:`

                - `List<CodeExecutionOutputBlock> content`

                  - `String fileId`

                  - `JsonValue; type "code_execution_output"constant`

                    - `CODE_EXECUTION_OUTPUT("code_execution_output")`

                - `long returnCode`

                - `String stderr`

                - `String stdout`

                - `JsonValue; type "code_execution_result"constant`

                  - `CODE_EXECUTION_RESULT("code_execution_result")`

              - `class EncryptedCodeExecutionResultBlock:`

                Code execution result with encrypted stdout for PFC + web_search results.

                - `List<CodeExecutionOutputBlock> content`

                  - `String fileId`

                  - `JsonValue; type "code_execution_output"constant`

                    - `CODE_EXECUTION_OUTPUT("code_execution_output")`

                - `String encryptedStdout`

                - `long returnCode`

                - `String stderr`

                - `JsonValue; type "encrypted_code_execution_result"constant`

                  - `ENCRYPTED_CODE_EXECUTION_RESULT("encrypted_code_execution_result")`

            - `String toolUseId`

            - `JsonValue; type "code_execution_tool_result"constant`

              - `CODE_EXECUTION_TOOL_RESULT("code_execution_tool_result")`

          - `class BashCodeExecutionToolResultBlock:`

            - `Content content`

              - `class BashCodeExecutionToolResultError:`

                - `BashCodeExecutionToolResultErrorCode errorCode`

                  - `INVALID_TOOL_INPUT("invalid_tool_input")`

                  - `UNAVAILABLE("unavailable")`

                  - `TOO_MANY_REQUESTS("too_many_requests")`

                  - `EXECUTION_TIME_EXCEEDED("execution_time_exceeded")`

                  - `OUTPUT_FILE_TOO_LARGE("output_file_too_large")`

                - `JsonValue; type "bash_code_execution_tool_result_error"constant`

                  - `BASH_CODE_EXECUTION_TOOL_RESULT_ERROR("bash_code_execution_tool_result_error")`

              - `class BashCodeExecutionResultBlock:`

                - `List<BashCodeExecutionOutputBlock> content`

                  - `String fileId`

                  - `JsonValue; type "bash_code_execution_output"constant`

                    - `BASH_CODE_EXECUTION_OUTPUT("bash_code_execution_output")`

                - `long returnCode`

                - `String stderr`

                - `String stdout`

                - `JsonValue; type "bash_code_execution_result"constant`

                  - `BASH_CODE_EXECUTION_RESULT("bash_code_execution_result")`

            - `String toolUseId`

            - `JsonValue; type "bash_code_execution_tool_result"constant`

              - `BASH_CODE_EXECUTION_TOOL_RESULT("bash_code_execution_tool_result")`

          - `class TextEditorCodeExecutionToolResultBlock:`

            - `Content content`

              - `class TextEditorCodeExecutionToolResultError:`

                - `TextEditorCodeExecutionToolResultErrorCode errorCode`

                  - `INVALID_TOOL_INPUT("invalid_tool_input")`

                  - `UNAVAILABLE("unavailable")`

                  - `TOO_MANY_REQUESTS("too_many_requests")`

                  - `EXECUTION_TIME_EXCEEDED("execution_time_exceeded")`

                  - `FILE_NOT_FOUND("file_not_found")`

                - `Optional<String> errorMessage`

                - `JsonValue; type "text_editor_code_execution_tool_result_error"constant`

                  - `TEXT_EDITOR_CODE_EXECUTION_TOOL_RESULT_ERROR("text_editor_code_execution_tool_result_error")`

              - `class TextEditorCodeExecutionViewResultBlock:`

                - `String content`

                - `FileType fileType`

                  - `TEXT("text")`

                  - `IMAGE("image")`

                  - `PDF("pdf")`

                - `Optional<Long> numLines`

                - `Optional<Long> startLine`

                - `Optional<Long> totalLines`

                - `JsonValue; type "text_editor_code_execution_view_result"constant`

                  - `TEXT_EDITOR_CODE_EXECUTION_VIEW_RESULT("text_editor_code_execution_view_result")`

              - `class TextEditorCodeExecutionCreateResultBlock:`

                - `boolean isFileUpdate`

                - `JsonValue; type "text_editor_code_execution_create_result"constant`

                  - `TEXT_EDITOR_CODE_EXECUTION_CREATE_RESULT("text_editor_code_execution_create_result")`

              - `class TextEditorCodeExecutionStrReplaceResultBlock:`

                - `Optional<List<String>> lines`

                - `Optional<Long> newLines`

                - `Optional<Long> newStart`

                - `Optional<Long> oldLines`

                - `Optional<Long> oldStart`

                - `JsonValue; type "text_editor_code_execution_str_replace_result"constant`

                  - `TEXT_EDITOR_CODE_EXECUTION_STR_REPLACE_RESULT("text_editor_code_execution_str_replace_result")`

            - `String toolUseId`

            - `JsonValue; type "text_editor_code_execution_tool_result"constant`

              - `TEXT_EDITOR_CODE_EXECUTION_TOOL_RESULT("text_editor_code_execution_tool_result")`

          - `class ToolSearchToolResultBlock:`

            - `Content content`

              - `class ToolSearchToolResultError:`

                - `ToolSearchToolResultErrorCode errorCode`

                  - `INVALID_TOOL_INPUT("invalid_tool_input")`

                  - `UNAVAILABLE("unavailable")`

                  - `TOO_MANY_REQUESTS("too_many_requests")`

                  - `EXECUTION_TIME_EXCEEDED("execution_time_exceeded")`

                - `Optional<String> errorMessage`

                - `JsonValue; type "tool_search_tool_result_error"constant`

                  - `TOOL_SEARCH_TOOL_RESULT_ERROR("tool_search_tool_result_error")`

              - `class ToolSearchToolSearchResultBlock:`

                - `List<ToolReferenceBlock> toolReferences`

                  - `String toolName`

                  - `JsonValue; type "tool_reference"constant`

                    - `TOOL_REFERENCE("tool_reference")`

                - `JsonValue; type "tool_search_tool_search_result"constant`

                  - `TOOL_SEARCH_TOOL_SEARCH_RESULT("tool_search_tool_search_result")`

            - `String toolUseId`

            - `JsonValue; type "tool_search_tool_result"constant`

              - `TOOL_SEARCH_TOOL_RESULT("tool_search_tool_result")`

          - `class ContainerUploadBlock:`

            Response model for a file uploaded to the container.

            - `String fileId`

            - `JsonValue; type "container_upload"constant`

              - `CONTAINER_UPLOAD("container_upload")`

        - `Model model`

          The model that will complete your prompt.

          See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

          - `CLAUDE_OPUS_4_6("claude-opus-4-6")`

            Most intelligent model for building agents and coding

          - `CLAUDE_SONNET_4_6("claude-sonnet-4-6")`

            Frontier intelligence at scale — built for coding, agents, and enterprise workflows

          - `CLAUDE_OPUS_4_5_20251101("claude-opus-4-5-20251101")`

            Premium model combining maximum intelligence with practical performance

          - `CLAUDE_OPUS_4_5("claude-opus-4-5")`

            Premium model combining maximum intelligence with practical performance

          - `CLAUDE_3_7_SONNET_LATEST("claude-3-7-sonnet-latest")`

            High-performance model with early extended thinking

          - `CLAUDE_3_7_SONNET_20250219("claude-3-7-sonnet-20250219")`

            High-performance model with early extended thinking

          - `CLAUDE_3_5_HAIKU_LATEST("claude-3-5-haiku-latest")`

            Fastest and most compact model for near-instant responsiveness

          - `CLAUDE_3_5_HAIKU_20241022("claude-3-5-haiku-20241022")`

            Our fastest model

          - `CLAUDE_HAIKU_4_5("claude-haiku-4-5")`

            Hybrid model, capable of near-instant responses and extended thinking

          - `CLAUDE_HAIKU_4_5_20251001("claude-haiku-4-5-20251001")`

            Hybrid model, capable of near-instant responses and extended thinking

          - `CLAUDE_SONNET_4_20250514("claude-sonnet-4-20250514")`

            High-performance model with extended thinking

          - `CLAUDE_SONNET_4_0("claude-sonnet-4-0")`

            High-performance model with extended thinking

          - `CLAUDE_4_SONNET_20250514("claude-4-sonnet-20250514")`

            High-performance model with extended thinking

          - `CLAUDE_SONNET_4_5("claude-sonnet-4-5")`

            Our best model for real-world agents and coding

          - `CLAUDE_SONNET_4_5_20250929("claude-sonnet-4-5-20250929")`

            Our best model for real-world agents and coding

          - `CLAUDE_OPUS_4_0("claude-opus-4-0")`

            Our most capable model

          - `CLAUDE_OPUS_4_20250514("claude-opus-4-20250514")`

            Our most capable model

          - `CLAUDE_4_OPUS_20250514("claude-4-opus-20250514")`

            Our most capable model

          - `CLAUDE_OPUS_4_1_20250805("claude-opus-4-1-20250805")`

            Our most capable model

          - `CLAUDE_3_OPUS_LATEST("claude-3-opus-latest")`

            Excels at writing and complex tasks

          - `CLAUDE_3_OPUS_20240229("claude-3-opus-20240229")`

            Excels at writing and complex tasks

          - `CLAUDE_3_HAIKU_20240307("claude-3-haiku-20240307")`

            Our previous most fast and cost-effective

        - `JsonValue; role "assistant"constant`

          Conversational role of the generated message.

          This will always be `"assistant"`.

          - `ASSISTANT("assistant")`

        - `Optional<StopReason> stopReason`

          The reason that we stopped.

          This may be one the following values:

          * `"end_turn"`: the model reached a natural stopping point
          * `"max_tokens"`: we exceeded the requested `max_tokens` or the model's maximum
          * `"stop_sequence"`: one of your provided custom `stop_sequences` was generated
          * `"tool_use"`: the model invoked one or more tools
          * `"pause_turn"`: we paused a long-running turn. You may provide the response back as-is in a subsequent request to let the model continue.
          * `"refusal"`: when streaming classifiers intervene to handle potential policy violations

          In non-streaming mode this value is always non-null. In streaming mode, it is null in the `message_start` event and non-null otherwise.

          - `END_TURN("end_turn")`

          - `MAX_TOKENS("max_tokens")`

          - `STOP_SEQUENCE("stop_sequence")`

          - `TOOL_USE("tool_use")`

          - `PAUSE_TURN("pause_turn")`

          - `REFUSAL("refusal")`

        - `Optional<String> stopSequence`

          Which custom stop sequence was generated, if any.

          This value will be a non-null string if one of your custom stop sequences was generated.

        - `JsonValue; type "message"constant`

          Object type.

          For Messages, this is always `"message"`.

          - `MESSAGE("message")`

        - `Usage usage`

          Billing and rate-limit usage.

          Anthropic's API bills and rate-limits by token counts, as tokens represent the underlying cost to our systems.

          Under the hood, the API transforms requests into a format suitable for the model. The model's output then goes through a parsing stage before becoming an API response. As a result, the token counts in `usage` will not match one-to-one with the exact visible content of an API request or response.

          For example, `output_tokens` will be non-zero, even for an empty string response from Claude.

          Total input tokens in a request is the summation of `input_tokens`, `cache_creation_input_tokens`, and `cache_read_input_tokens`.

          - `Optional<CacheCreation> cacheCreation`

            Breakdown of cached tokens by TTL

            - `long ephemeral1hInputTokens`

              The number of input tokens used to create the 1 hour cache entry.

            - `long ephemeral5mInputTokens`

              The number of input tokens used to create the 5 minute cache entry.

          - `Optional<Long> cacheCreationInputTokens`

            The number of input tokens used to create the cache entry.

          - `Optional<Long> cacheReadInputTokens`

            The number of input tokens read from the cache.

          - `Optional<String> inferenceGeo`

            The geographic region where inference was performed for this request.

          - `long inputTokens`

            The number of input tokens which were used.

          - `long outputTokens`

            The number of output tokens which were used.

          - `Optional<ServerToolUsage> serverToolUse`

            The number of server tool requests.

            - `long webFetchRequests`

              The number of web fetch tool requests.

            - `long webSearchRequests`

              The number of web search tool requests.

          - `Optional<ServiceTier> serviceTier`

            If the request used the priority, standard, or batch tier.

            - `STANDARD("standard")`

            - `PRIORITY("priority")`

            - `BATCH("batch")`

      - `JsonValue; type "succeeded"constant`

        - `SUCCEEDED("succeeded")`

    - `class MessageBatchErroredResult:`

      - `ErrorResponse error`

        - `ErrorObject error`

          - `class InvalidRequestError:`

            - `String message`

            - `JsonValue; type "invalid_request_error"constant`

              - `INVALID_REQUEST_ERROR("invalid_request_error")`

          - `class AuthenticationError:`

            - `String message`

            - `JsonValue; type "authentication_error"constant`

              - `AUTHENTICATION_ERROR("authentication_error")`

          - `class BillingError:`

            - `String message`

            - `JsonValue; type "billing_error"constant`

              - `BILLING_ERROR("billing_error")`

          - `class PermissionError:`

            - `String message`

            - `JsonValue; type "permission_error"constant`

              - `PERMISSION_ERROR("permission_error")`

          - `class NotFoundError:`

            - `String message`

            - `JsonValue; type "not_found_error"constant`

              - `NOT_FOUND_ERROR("not_found_error")`

          - `class RateLimitError:`

            - `String message`

            - `JsonValue; type "rate_limit_error"constant`

              - `RATE_LIMIT_ERROR("rate_limit_error")`

          - `class GatewayTimeoutError:`

            - `String message`

            - `JsonValue; type "timeout_error"constant`

              - `TIMEOUT_ERROR("timeout_error")`

          - `class ApiErrorObject:`

            - `String message`

            - `JsonValue; type "api_error"constant`

              - `API_ERROR("api_error")`

          - `class OverloadedError:`

            - `String message`

            - `JsonValue; type "overloaded_error"constant`

              - `OVERLOADED_ERROR("overloaded_error")`

        - `Optional<String> requestId`

        - `JsonValue; type "error"constant`

          - `ERROR("error")`

      - `JsonValue; type "errored"constant`

        - `ERRORED("errored")`

    - `class MessageBatchCanceledResult:`

      - `JsonValue; type "canceled"constant`

        - `CANCELED("canceled")`

    - `class MessageBatchExpiredResult:`

      - `JsonValue; type "expired"constant`

        - `EXPIRED("expired")`

### Example

```java
package com.anthropic.example;

import com.anthropic.client.AnthropicClient;
import com.anthropic.client.okhttp.AnthropicOkHttpClient;
import com.anthropic.core.http.StreamResponse;
import com.anthropic.models.messages.batches.BatchResultsParams;
import com.anthropic.models.messages.batches.MessageBatchIndividualResponse;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        AnthropicClient client = AnthropicOkHttpClient.fromEnv();

        StreamResponse<MessageBatchIndividualResponse> messageBatchIndividualResponse = client.messages().batches().resultsStreaming("message_batch_id");
    }
}
```

## Domain Types

### Deleted Message Batch

- `class DeletedMessageBatch:`

  - `String id`

    ID of the Message Batch.

  - `JsonValue; type "message_batch_deleted"constant`

    Deleted object type.

    For Message Batches, this is always `"message_batch_deleted"`.

    - `MESSAGE_BATCH_DELETED("message_batch_deleted")`

### Message Batch

- `class MessageBatch:`

  - `String id`

    Unique object identifier.

    The format and length of IDs may change over time.

  - `Optional<LocalDateTime> archivedAt`

    RFC 3339 datetime string representing the time at which the Message Batch was archived and its results became unavailable.

  - `Optional<LocalDateTime> cancelInitiatedAt`

    RFC 3339 datetime string representing the time at which cancellation was initiated for the Message Batch. Specified only if cancellation was initiated.

  - `LocalDateTime createdAt`

    RFC 3339 datetime string representing the time at which the Message Batch was created.

  - `Optional<LocalDateTime> endedAt`

    RFC 3339 datetime string representing the time at which processing for the Message Batch ended. Specified only once processing ends.

    Processing ends when every request in a Message Batch has either succeeded, errored, canceled, or expired.

  - `LocalDateTime expiresAt`

    RFC 3339 datetime string representing the time at which the Message Batch will expire and end processing, which is 24 hours after creation.

  - `ProcessingStatus processingStatus`

    Processing status of the Message Batch.

    - `IN_PROGRESS("in_progress")`

    - `CANCELING("canceling")`

    - `ENDED("ended")`

  - `MessageBatchRequestCounts requestCounts`

    Tallies requests within the Message Batch, categorized by their status.

    Requests start as `processing` and move to one of the other statuses only once processing of the entire batch ends. The sum of all values always matches the total number of requests in the batch.

    - `long canceled`

      Number of requests in the Message Batch that have been canceled.

      This is zero until processing of the entire Message Batch has ended.

    - `long errored`

      Number of requests in the Message Batch that encountered an error.

      This is zero until processing of the entire Message Batch has ended.

    - `long expired`

      Number of requests in the Message Batch that have expired.

      This is zero until processing of the entire Message Batch has ended.

    - `long processing`

      Number of requests in the Message Batch that are processing.

    - `long succeeded`

      Number of requests in the Message Batch that have completed successfully.

      This is zero until processing of the entire Message Batch has ended.

  - `Optional<String> resultsUrl`

    URL to a `.jsonl` file containing the results of the Message Batch requests. Specified only once processing ends.

    Results in the file are not guaranteed to be in the same order as requests. Use the `custom_id` field to match results to requests.

  - `JsonValue; type "message_batch"constant`

    Object type.

    For Message Batches, this is always `"message_batch"`.

    - `MESSAGE_BATCH("message_batch")`

### Message Batch Canceled Result

- `class MessageBatchCanceledResult:`

  - `JsonValue; type "canceled"constant`

    - `CANCELED("canceled")`

### Message Batch Errored Result

- `class MessageBatchErroredResult:`

  - `ErrorResponse error`

    - `ErrorObject error`

      - `class InvalidRequestError:`

        - `String message`

        - `JsonValue; type "invalid_request_error"constant`

          - `INVALID_REQUEST_ERROR("invalid_request_error")`

      - `class AuthenticationError:`

        - `String message`

        - `JsonValue; type "authentication_error"constant`

          - `AUTHENTICATION_ERROR("authentication_error")`

      - `class BillingError:`

        - `String message`

        - `JsonValue; type "billing_error"constant`

          - `BILLING_ERROR("billing_error")`

      - `class PermissionError:`

        - `String message`

        - `JsonValue; type "permission_error"constant`

          - `PERMISSION_ERROR("permission_error")`

      - `class NotFoundError:`

        - `String message`

        - `JsonValue; type "not_found_error"constant`

          - `NOT_FOUND_ERROR("not_found_error")`

      - `class RateLimitError:`

        - `String message`

        - `JsonValue; type "rate_limit_error"constant`

          - `RATE_LIMIT_ERROR("rate_limit_error")`

      - `class GatewayTimeoutError:`

        - `String message`

        - `JsonValue; type "timeout_error"constant`

          - `TIMEOUT_ERROR("timeout_error")`

      - `class ApiErrorObject:`

        - `String message`

        - `JsonValue; type "api_error"constant`

          - `API_ERROR("api_error")`

      - `class OverloadedError:`

        - `String message`

        - `JsonValue; type "overloaded_error"constant`

          - `OVERLOADED_ERROR("overloaded_error")`

    - `Optional<String> requestId`

    - `JsonValue; type "error"constant`

      - `ERROR("error")`

  - `JsonValue; type "errored"constant`

    - `ERRORED("errored")`

### Message Batch Expired Result

- `class MessageBatchExpiredResult:`

  - `JsonValue; type "expired"constant`

    - `EXPIRED("expired")`

### Message Batch Individual Response

- `class MessageBatchIndividualResponse:`

  This is a single line in the response `.jsonl` file and does not represent the response as a whole.

  - `String customId`

    Developer-provided ID created for each request in a Message Batch. Useful for matching results to requests, as results may be given out of request order.

    Must be unique for each request within the Message Batch.

  - `MessageBatchResult result`

    Processing result for this request.

    Contains a Message output if processing was successful, an error response if processing failed, or the reason why processing was not attempted, such as cancellation or expiration.

    - `class MessageBatchSucceededResult:`

      - `Message message`

        - `String id`

          Unique object identifier.

          The format and length of IDs may change over time.

        - `Optional<Container> container`

          Information about the container used in the request (for the code execution tool)

          - `String id`

            Identifier for the container used in this request

          - `LocalDateTime expiresAt`

            The time at which the container will expire.

        - `List<ContentBlock> content`

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

          - `class TextBlock:`

            - `Optional<List<TextCitation>> citations`

              Citations supporting the text block.

              The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

              - `class CitationCharLocation:`

                - `String citedText`

                - `long documentIndex`

                - `Optional<String> documentTitle`

                - `long endCharIndex`

                - `Optional<String> fileId`

                - `long startCharIndex`

                - `JsonValue; type "char_location"constant`

                  - `CHAR_LOCATION("char_location")`

              - `class CitationPageLocation:`

                - `String citedText`

                - `long documentIndex`

                - `Optional<String> documentTitle`

                - `long endPageNumber`

                - `Optional<String> fileId`

                - `long startPageNumber`

                - `JsonValue; type "page_location"constant`

                  - `PAGE_LOCATION("page_location")`

              - `class CitationContentBlockLocation:`

                - `String citedText`

                - `long documentIndex`

                - `Optional<String> documentTitle`

                - `long endBlockIndex`

                - `Optional<String> fileId`

                - `long startBlockIndex`

                - `JsonValue; type "content_block_location"constant`

                  - `CONTENT_BLOCK_LOCATION("content_block_location")`

              - `class CitationsWebSearchResultLocation:`

                - `String citedText`

                - `String encryptedIndex`

                - `Optional<String> title`

                - `JsonValue; type "web_search_result_location"constant`

                  - `WEB_SEARCH_RESULT_LOCATION("web_search_result_location")`

                - `String url`

              - `class CitationsSearchResultLocation:`

                - `String citedText`

                - `long endBlockIndex`

                - `long searchResultIndex`

                - `String source`

                - `long startBlockIndex`

                - `Optional<String> title`

                - `JsonValue; type "search_result_location"constant`

                  - `SEARCH_RESULT_LOCATION("search_result_location")`

            - `String text`

            - `JsonValue; type "text"constant`

              - `TEXT("text")`

          - `class ThinkingBlock:`

            - `String signature`

            - `String thinking`

            - `JsonValue; type "thinking"constant`

              - `THINKING("thinking")`

          - `class RedactedThinkingBlock:`

            - `String data`

            - `JsonValue; type "redacted_thinking"constant`

              - `REDACTED_THINKING("redacted_thinking")`

          - `class ToolUseBlock:`

            - `String id`

            - `Caller caller`

              Tool invocation directly from the model.

              - `class DirectCaller:`

                Tool invocation directly from the model.

                - `JsonValue; type "direct"constant`

                  - `DIRECT("direct")`

              - `class ServerToolCaller:`

                Tool invocation generated by a server-side tool.

                - `String toolId`

                - `JsonValue; type "code_execution_20250825"constant`

                  - `CODE_EXECUTION_20250825("code_execution_20250825")`

              - `class ServerToolCaller20260120:`

                - `String toolId`

                - `JsonValue; type "code_execution_20260120"constant`

                  - `CODE_EXECUTION_20260120("code_execution_20260120")`

            - `Input input`

            - `String name`

            - `JsonValue; type "tool_use"constant`

              - `TOOL_USE("tool_use")`

          - `class ServerToolUseBlock:`

            - `String id`

            - `Caller caller`

              Tool invocation directly from the model.

              - `class DirectCaller:`

                Tool invocation directly from the model.

                - `JsonValue; type "direct"constant`

                  - `DIRECT("direct")`

              - `class ServerToolCaller:`

                Tool invocation generated by a server-side tool.

                - `String toolId`

                - `JsonValue; type "code_execution_20250825"constant`

                  - `CODE_EXECUTION_20250825("code_execution_20250825")`

              - `class ServerToolCaller20260120:`

                - `String toolId`

                - `JsonValue; type "code_execution_20260120"constant`

                  - `CODE_EXECUTION_20260120("code_execution_20260120")`

            - `Input input`

            - `Name name`

              - `WEB_SEARCH("web_search")`

              - `WEB_FETCH("web_fetch")`

              - `CODE_EXECUTION("code_execution")`

              - `BASH_CODE_EXECUTION("bash_code_execution")`

              - `TEXT_EDITOR_CODE_EXECUTION("text_editor_code_execution")`

              - `TOOL_SEARCH_TOOL_REGEX("tool_search_tool_regex")`

              - `TOOL_SEARCH_TOOL_BM25("tool_search_tool_bm25")`

            - `JsonValue; type "server_tool_use"constant`

              - `SERVER_TOOL_USE("server_tool_use")`

          - `class WebSearchToolResultBlock:`

            - `Caller caller`

              Tool invocation directly from the model.

              - `class DirectCaller:`

                Tool invocation directly from the model.

                - `JsonValue; type "direct"constant`

                  - `DIRECT("direct")`

              - `class ServerToolCaller:`

                Tool invocation generated by a server-side tool.

                - `String toolId`

                - `JsonValue; type "code_execution_20250825"constant`

                  - `CODE_EXECUTION_20250825("code_execution_20250825")`

              - `class ServerToolCaller20260120:`

                - `String toolId`

                - `JsonValue; type "code_execution_20260120"constant`

                  - `CODE_EXECUTION_20260120("code_execution_20260120")`

            - `WebSearchToolResultBlockContent content`

              - `class WebSearchToolResultError:`

                - `WebSearchToolResultErrorCode errorCode`

                  - `INVALID_TOOL_INPUT("invalid_tool_input")`

                  - `UNAVAILABLE("unavailable")`

                  - `MAX_USES_EXCEEDED("max_uses_exceeded")`

                  - `TOO_MANY_REQUESTS("too_many_requests")`

                  - `QUERY_TOO_LONG("query_too_long")`

                  - `REQUEST_TOO_LARGE("request_too_large")`

                - `JsonValue; type "web_search_tool_result_error"constant`

                  - `WEB_SEARCH_TOOL_RESULT_ERROR("web_search_tool_result_error")`

              - `List<WebSearchResultBlock>`

                - `String encryptedContent`

                - `Optional<String> pageAge`

                - `String title`

                - `JsonValue; type "web_search_result"constant`

                  - `WEB_SEARCH_RESULT("web_search_result")`

                - `String url`

            - `String toolUseId`

            - `JsonValue; type "web_search_tool_result"constant`

              - `WEB_SEARCH_TOOL_RESULT("web_search_tool_result")`

          - `class WebFetchToolResultBlock:`

            - `Caller caller`

              Tool invocation directly from the model.

              - `class DirectCaller:`

                Tool invocation directly from the model.

                - `JsonValue; type "direct"constant`

                  - `DIRECT("direct")`

              - `class ServerToolCaller:`

                Tool invocation generated by a server-side tool.

                - `String toolId`

                - `JsonValue; type "code_execution_20250825"constant`

                  - `CODE_EXECUTION_20250825("code_execution_20250825")`

              - `class ServerToolCaller20260120:`

                - `String toolId`

                - `JsonValue; type "code_execution_20260120"constant`

                  - `CODE_EXECUTION_20260120("code_execution_20260120")`

            - `Content content`

              - `class WebFetchToolResultErrorBlock:`

                - `WebFetchToolResultErrorCode errorCode`

                  - `INVALID_TOOL_INPUT("invalid_tool_input")`

                  - `URL_TOO_LONG("url_too_long")`

                  - `URL_NOT_ALLOWED("url_not_allowed")`

                  - `URL_NOT_ACCESSIBLE("url_not_accessible")`

                  - `UNSUPPORTED_CONTENT_TYPE("unsupported_content_type")`

                  - `TOO_MANY_REQUESTS("too_many_requests")`

                  - `MAX_USES_EXCEEDED("max_uses_exceeded")`

                  - `UNAVAILABLE("unavailable")`

                - `JsonValue; type "web_fetch_tool_result_error"constant`

                  - `WEB_FETCH_TOOL_RESULT_ERROR("web_fetch_tool_result_error")`

              - `class WebFetchBlock:`

                - `DocumentBlock content`

                  - `Optional<CitationsConfig> citations`

                    Citation configuration for the document

                    - `boolean enabled`

                  - `Source source`

                    - `class Base64PdfSource:`

                      - `String data`

                      - `JsonValue; mediaType "application/pdf"constant`

                        - `APPLICATION_PDF("application/pdf")`

                      - `JsonValue; type "base64"constant`

                        - `BASE64("base64")`

                    - `class PlainTextSource:`

                      - `String data`

                      - `JsonValue; mediaType "text/plain"constant`

                        - `TEXT_PLAIN("text/plain")`

                      - `JsonValue; type "text"constant`

                        - `TEXT("text")`

                  - `Optional<String> title`

                    The title of the document

                  - `JsonValue; type "document"constant`

                    - `DOCUMENT("document")`

                - `Optional<String> retrievedAt`

                  ISO 8601 timestamp when the content was retrieved

                - `JsonValue; type "web_fetch_result"constant`

                  - `WEB_FETCH_RESULT("web_fetch_result")`

                - `String url`

                  Fetched content URL

            - `String toolUseId`

            - `JsonValue; type "web_fetch_tool_result"constant`

              - `WEB_FETCH_TOOL_RESULT("web_fetch_tool_result")`

          - `class CodeExecutionToolResultBlock:`

            - `CodeExecutionToolResultBlockContent content`

              Code execution result with encrypted stdout for PFC + web_search results.

              - `class CodeExecutionToolResultError:`

                - `CodeExecutionToolResultErrorCode errorCode`

                  - `INVALID_TOOL_INPUT("invalid_tool_input")`

                  - `UNAVAILABLE("unavailable")`

                  - `TOO_MANY_REQUESTS("too_many_requests")`

                  - `EXECUTION_TIME_EXCEEDED("execution_time_exceeded")`

                - `JsonValue; type "code_execution_tool_result_error"constant`

                  - `CODE_EXECUTION_TOOL_RESULT_ERROR("code_execution_tool_result_error")`

              - `class CodeExecutionResultBlock:`

                - `List<CodeExecutionOutputBlock> content`

                  - `String fileId`

                  - `JsonValue; type "code_execution_output"constant`

                    - `CODE_EXECUTION_OUTPUT("code_execution_output")`

                - `long returnCode`

                - `String stderr`

                - `String stdout`

                - `JsonValue; type "code_execution_result"constant`

                  - `CODE_EXECUTION_RESULT("code_execution_result")`

              - `class EncryptedCodeExecutionResultBlock:`

                Code execution result with encrypted stdout for PFC + web_search results.

                - `List<CodeExecutionOutputBlock> content`

                  - `String fileId`

                  - `JsonValue; type "code_execution_output"constant`

                    - `CODE_EXECUTION_OUTPUT("code_execution_output")`

                - `String encryptedStdout`

                - `long returnCode`

                - `String stderr`

                - `JsonValue; type "encrypted_code_execution_result"constant`

                  - `ENCRYPTED_CODE_EXECUTION_RESULT("encrypted_code_execution_result")`

            - `String toolUseId`

            - `JsonValue; type "code_execution_tool_result"constant`

              - `CODE_EXECUTION_TOOL_RESULT("code_execution_tool_result")`

          - `class BashCodeExecutionToolResultBlock:`

            - `Content content`

              - `class BashCodeExecutionToolResultError:`

                - `BashCodeExecutionToolResultErrorCode errorCode`

                  - `INVALID_TOOL_INPUT("invalid_tool_input")`

                  - `UNAVAILABLE("unavailable")`

                  - `TOO_MANY_REQUESTS("too_many_requests")`

                  - `EXECUTION_TIME_EXCEEDED("execution_time_exceeded")`

                  - `OUTPUT_FILE_TOO_LARGE("output_file_too_large")`

                - `JsonValue; type "bash_code_execution_tool_result_error"constant`

                  - `BASH_CODE_EXECUTION_TOOL_RESULT_ERROR("bash_code_execution_tool_result_error")`

              - `class BashCodeExecutionResultBlock:`

                - `List<BashCodeExecutionOutputBlock> content`

                  - `String fileId`

                  - `JsonValue; type "bash_code_execution_output"constant`

                    - `BASH_CODE_EXECUTION_OUTPUT("bash_code_execution_output")`

                - `long returnCode`

                - `String stderr`

                - `String stdout`

                - `JsonValue; type "bash_code_execution_result"constant`

                  - `BASH_CODE_EXECUTION_RESULT("bash_code_execution_result")`

            - `String toolUseId`

            - `JsonValue; type "bash_code_execution_tool_result"constant`

              - `BASH_CODE_EXECUTION_TOOL_RESULT("bash_code_execution_tool_result")`

          - `class TextEditorCodeExecutionToolResultBlock:`

            - `Content content`

              - `class TextEditorCodeExecutionToolResultError:`

                - `TextEditorCodeExecutionToolResultErrorCode errorCode`

                  - `INVALID_TOOL_INPUT("invalid_tool_input")`

                  - `UNAVAILABLE("unavailable")`

                  - `TOO_MANY_REQUESTS("too_many_requests")`

                  - `EXECUTION_TIME_EXCEEDED("execution_time_exceeded")`

                  - `FILE_NOT_FOUND("file_not_found")`

                - `Optional<String> errorMessage`

                - `JsonValue; type "text_editor_code_execution_tool_result_error"constant`

                  - `TEXT_EDITOR_CODE_EXECUTION_TOOL_RESULT_ERROR("text_editor_code_execution_tool_result_error")`

              - `class TextEditorCodeExecutionViewResultBlock:`

                - `String content`

                - `FileType fileType`

                  - `TEXT("text")`

                  - `IMAGE("image")`

                  - `PDF("pdf")`

                - `Optional<Long> numLines`

                - `Optional<Long> startLine`

                - `Optional<Long> totalLines`

                - `JsonValue; type "text_editor_code_execution_view_result"constant`

                  - `TEXT_EDITOR_CODE_EXECUTION_VIEW_RESULT("text_editor_code_execution_view_result")`

              - `class TextEditorCodeExecutionCreateResultBlock:`

                - `boolean isFileUpdate`

                - `JsonValue; type "text_editor_code_execution_create_result"constant`

                  - `TEXT_EDITOR_CODE_EXECUTION_CREATE_RESULT("text_editor_code_execution_create_result")`

              - `class TextEditorCodeExecutionStrReplaceResultBlock:`

                - `Optional<List<String>> lines`

                - `Optional<Long> newLines`

                - `Optional<Long> newStart`

                - `Optional<Long> oldLines`

                - `Optional<Long> oldStart`

                - `JsonValue; type "text_editor_code_execution_str_replace_result"constant`

                  - `TEXT_EDITOR_CODE_EXECUTION_STR_REPLACE_RESULT("text_editor_code_execution_str_replace_result")`

            - `String toolUseId`

            - `JsonValue; type "text_editor_code_execution_tool_result"constant`

              - `TEXT_EDITOR_CODE_EXECUTION_TOOL_RESULT("text_editor_code_execution_tool_result")`

          - `class ToolSearchToolResultBlock:`

            - `Content content`

              - `class ToolSearchToolResultError:`

                - `ToolSearchToolResultErrorCode errorCode`

                  - `INVALID_TOOL_INPUT("invalid_tool_input")`

                  - `UNAVAILABLE("unavailable")`

                  - `TOO_MANY_REQUESTS("too_many_requests")`

                  - `EXECUTION_TIME_EXCEEDED("execution_time_exceeded")`

                - `Optional<String> errorMessage`

                - `JsonValue; type "tool_search_tool_result_error"constant`

                  - `TOOL_SEARCH_TOOL_RESULT_ERROR("tool_search_tool_result_error")`

              - `class ToolSearchToolSearchResultBlock:`

                - `List<ToolReferenceBlock> toolReferences`

                  - `String toolName`

                  - `JsonValue; type "tool_reference"constant`

                    - `TOOL_REFERENCE("tool_reference")`

                - `JsonValue; type "tool_search_tool_search_result"constant`

                  - `TOOL_SEARCH_TOOL_SEARCH_RESULT("tool_search_tool_search_result")`

            - `String toolUseId`

            - `JsonValue; type "tool_search_tool_result"constant`

              - `TOOL_SEARCH_TOOL_RESULT("tool_search_tool_result")`

          - `class ContainerUploadBlock:`

            Response model for a file uploaded to the container.

            - `String fileId`

            - `JsonValue; type "container_upload"constant`

              - `CONTAINER_UPLOAD("container_upload")`

        - `Model model`

          The model that will complete your prompt.

          See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

          - `CLAUDE_OPUS_4_6("claude-opus-4-6")`

            Most intelligent model for building agents and coding

          - `CLAUDE_SONNET_4_6("claude-sonnet-4-6")`

            Frontier intelligence at scale — built for coding, agents, and enterprise workflows

          - `CLAUDE_OPUS_4_5_20251101("claude-opus-4-5-20251101")`

            Premium model combining maximum intelligence with practical performance

          - `CLAUDE_OPUS_4_5("claude-opus-4-5")`

            Premium model combining maximum intelligence with practical performance

          - `CLAUDE_3_7_SONNET_LATEST("claude-3-7-sonnet-latest")`

            High-performance model with early extended thinking

          - `CLAUDE_3_7_SONNET_20250219("claude-3-7-sonnet-20250219")`

            High-performance model with early extended thinking

          - `CLAUDE_3_5_HAIKU_LATEST("claude-3-5-haiku-latest")`

            Fastest and most compact model for near-instant responsiveness

          - `CLAUDE_3_5_HAIKU_20241022("claude-3-5-haiku-20241022")`

            Our fastest model

          - `CLAUDE_HAIKU_4_5("claude-haiku-4-5")`

            Hybrid model, capable of near-instant responses and extended thinking

          - `CLAUDE_HAIKU_4_5_20251001("claude-haiku-4-5-20251001")`

            Hybrid model, capable of near-instant responses and extended thinking

          - `CLAUDE_SONNET_4_20250514("claude-sonnet-4-20250514")`

            High-performance model with extended thinking

          - `CLAUDE_SONNET_4_0("claude-sonnet-4-0")`

            High-performance model with extended thinking

          - `CLAUDE_4_SONNET_20250514("claude-4-sonnet-20250514")`

            High-performance model with extended thinking

          - `CLAUDE_SONNET_4_5("claude-sonnet-4-5")`

            Our best model for real-world agents and coding

          - `CLAUDE_SONNET_4_5_20250929("claude-sonnet-4-5-20250929")`

            Our best model for real-world agents and coding

          - `CLAUDE_OPUS_4_0("claude-opus-4-0")`

            Our most capable model

          - `CLAUDE_OPUS_4_20250514("claude-opus-4-20250514")`

            Our most capable model

          - `CLAUDE_4_OPUS_20250514("claude-4-opus-20250514")`

            Our most capable model

          - `CLAUDE_OPUS_4_1_20250805("claude-opus-4-1-20250805")`

            Our most capable model

          - `CLAUDE_3_OPUS_LATEST("claude-3-opus-latest")`

            Excels at writing and complex tasks

          - `CLAUDE_3_OPUS_20240229("claude-3-opus-20240229")`

            Excels at writing and complex tasks

          - `CLAUDE_3_HAIKU_20240307("claude-3-haiku-20240307")`

            Our previous most fast and cost-effective

        - `JsonValue; role "assistant"constant`

          Conversational role of the generated message.

          This will always be `"assistant"`.

          - `ASSISTANT("assistant")`

        - `Optional<StopReason> stopReason`

          The reason that we stopped.

          This may be one the following values:

          * `"end_turn"`: the model reached a natural stopping point
          * `"max_tokens"`: we exceeded the requested `max_tokens` or the model's maximum
          * `"stop_sequence"`: one of your provided custom `stop_sequences` was generated
          * `"tool_use"`: the model invoked one or more tools
          * `"pause_turn"`: we paused a long-running turn. You may provide the response back as-is in a subsequent request to let the model continue.
          * `"refusal"`: when streaming classifiers intervene to handle potential policy violations

          In non-streaming mode this value is always non-null. In streaming mode, it is null in the `message_start` event and non-null otherwise.

          - `END_TURN("end_turn")`

          - `MAX_TOKENS("max_tokens")`

          - `STOP_SEQUENCE("stop_sequence")`

          - `TOOL_USE("tool_use")`

          - `PAUSE_TURN("pause_turn")`

          - `REFUSAL("refusal")`

        - `Optional<String> stopSequence`

          Which custom stop sequence was generated, if any.

          This value will be a non-null string if one of your custom stop sequences was generated.

        - `JsonValue; type "message"constant`

          Object type.

          For Messages, this is always `"message"`.

          - `MESSAGE("message")`

        - `Usage usage`

          Billing and rate-limit usage.

          Anthropic's API bills and rate-limits by token counts, as tokens represent the underlying cost to our systems.

          Under the hood, the API transforms requests into a format suitable for the model. The model's output then goes through a parsing stage before becoming an API response. As a result, the token counts in `usage` will not match one-to-one with the exact visible content of an API request or response.

          For example, `output_tokens` will be non-zero, even for an empty string response from Claude.

          Total input tokens in a request is the summation of `input_tokens`, `cache_creation_input_tokens`, and `cache_read_input_tokens`.

          - `Optional<CacheCreation> cacheCreation`

            Breakdown of cached tokens by TTL

            - `long ephemeral1hInputTokens`

              The number of input tokens used to create the 1 hour cache entry.

            - `long ephemeral5mInputTokens`

              The number of input tokens used to create the 5 minute cache entry.

          - `Optional<Long> cacheCreationInputTokens`

            The number of input tokens used to create the cache entry.

          - `Optional<Long> cacheReadInputTokens`

            The number of input tokens read from the cache.

          - `Optional<String> inferenceGeo`

            The geographic region where inference was performed for this request.

          - `long inputTokens`

            The number of input tokens which were used.

          - `long outputTokens`

            The number of output tokens which were used.

          - `Optional<ServerToolUsage> serverToolUse`

            The number of server tool requests.

            - `long webFetchRequests`

              The number of web fetch tool requests.

            - `long webSearchRequests`

              The number of web search tool requests.

          - `Optional<ServiceTier> serviceTier`

            If the request used the priority, standard, or batch tier.

            - `STANDARD("standard")`

            - `PRIORITY("priority")`

            - `BATCH("batch")`

      - `JsonValue; type "succeeded"constant`

        - `SUCCEEDED("succeeded")`

    - `class MessageBatchErroredResult:`

      - `ErrorResponse error`

        - `ErrorObject error`

          - `class InvalidRequestError:`

            - `String message`

            - `JsonValue; type "invalid_request_error"constant`

              - `INVALID_REQUEST_ERROR("invalid_request_error")`

          - `class AuthenticationError:`

            - `String message`

            - `JsonValue; type "authentication_error"constant`

              - `AUTHENTICATION_ERROR("authentication_error")`

          - `class BillingError:`

            - `String message`

            - `JsonValue; type "billing_error"constant`

              - `BILLING_ERROR("billing_error")`

          - `class PermissionError:`

            - `String message`

            - `JsonValue; type "permission_error"constant`

              - `PERMISSION_ERROR("permission_error")`

          - `class NotFoundError:`

            - `String message`

            - `JsonValue; type "not_found_error"constant`

              - `NOT_FOUND_ERROR("not_found_error")`

          - `class RateLimitError:`

            - `String message`

            - `JsonValue; type "rate_limit_error"constant`

              - `RATE_LIMIT_ERROR("rate_limit_error")`

          - `class GatewayTimeoutError:`

            - `String message`

            - `JsonValue; type "timeout_error"constant`

              - `TIMEOUT_ERROR("timeout_error")`

          - `class ApiErrorObject:`

            - `String message`

            - `JsonValue; type "api_error"constant`

              - `API_ERROR("api_error")`

          - `class OverloadedError:`

            - `String message`

            - `JsonValue; type "overloaded_error"constant`

              - `OVERLOADED_ERROR("overloaded_error")`

        - `Optional<String> requestId`

        - `JsonValue; type "error"constant`

          - `ERROR("error")`

      - `JsonValue; type "errored"constant`

        - `ERRORED("errored")`

    - `class MessageBatchCanceledResult:`

      - `JsonValue; type "canceled"constant`

        - `CANCELED("canceled")`

    - `class MessageBatchExpiredResult:`

      - `JsonValue; type "expired"constant`

        - `EXPIRED("expired")`

### Message Batch Request Counts

- `class MessageBatchRequestCounts:`

  - `long canceled`

    Number of requests in the Message Batch that have been canceled.

    This is zero until processing of the entire Message Batch has ended.

  - `long errored`

    Number of requests in the Message Batch that encountered an error.

    This is zero until processing of the entire Message Batch has ended.

  - `long expired`

    Number of requests in the Message Batch that have expired.

    This is zero until processing of the entire Message Batch has ended.

  - `long processing`

    Number of requests in the Message Batch that are processing.

  - `long succeeded`

    Number of requests in the Message Batch that have completed successfully.

    This is zero until processing of the entire Message Batch has ended.

### Message Batch Result

- `class MessageBatchResult: A class that can be one of several variants.union`

  Processing result for this request.

  Contains a Message output if processing was successful, an error response if processing failed, or the reason why processing was not attempted, such as cancellation or expiration.

  - `class MessageBatchSucceededResult:`

    - `Message message`

      - `String id`

        Unique object identifier.

        The format and length of IDs may change over time.

      - `Optional<Container> container`

        Information about the container used in the request (for the code execution tool)

        - `String id`

          Identifier for the container used in this request

        - `LocalDateTime expiresAt`

          The time at which the container will expire.

      - `List<ContentBlock> content`

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

        - `class TextBlock:`

          - `Optional<List<TextCitation>> citations`

            Citations supporting the text block.

            The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

            - `class CitationCharLocation:`

              - `String citedText`

              - `long documentIndex`

              - `Optional<String> documentTitle`

              - `long endCharIndex`

              - `Optional<String> fileId`

              - `long startCharIndex`

              - `JsonValue; type "char_location"constant`

                - `CHAR_LOCATION("char_location")`

            - `class CitationPageLocation:`

              - `String citedText`

              - `long documentIndex`

              - `Optional<String> documentTitle`

              - `long endPageNumber`

              - `Optional<String> fileId`

              - `long startPageNumber`

              - `JsonValue; type "page_location"constant`

                - `PAGE_LOCATION("page_location")`

            - `class CitationContentBlockLocation:`

              - `String citedText`

              - `long documentIndex`

              - `Optional<String> documentTitle`

              - `long endBlockIndex`

              - `Optional<String> fileId`

              - `long startBlockIndex`

              - `JsonValue; type "content_block_location"constant`

                - `CONTENT_BLOCK_LOCATION("content_block_location")`

            - `class CitationsWebSearchResultLocation:`

              - `String citedText`

              - `String encryptedIndex`

              - `Optional<String> title`

              - `JsonValue; type "web_search_result_location"constant`

                - `WEB_SEARCH_RESULT_LOCATION("web_search_result_location")`

              - `String url`

            - `class CitationsSearchResultLocation:`

              - `String citedText`

              - `long endBlockIndex`

              - `long searchResultIndex`

              - `String source`

              - `long startBlockIndex`

              - `Optional<String> title`

              - `JsonValue; type "search_result_location"constant`

                - `SEARCH_RESULT_LOCATION("search_result_location")`

          - `String text`

          - `JsonValue; type "text"constant`

            - `TEXT("text")`

        - `class ThinkingBlock:`

          - `String signature`

          - `String thinking`

          - `JsonValue; type "thinking"constant`

            - `THINKING("thinking")`

        - `class RedactedThinkingBlock:`

          - `String data`

          - `JsonValue; type "redacted_thinking"constant`

            - `REDACTED_THINKING("redacted_thinking")`

        - `class ToolUseBlock:`

          - `String id`

          - `Caller caller`

            Tool invocation directly from the model.

            - `class DirectCaller:`

              Tool invocation directly from the model.

              - `JsonValue; type "direct"constant`

                - `DIRECT("direct")`

            - `class ServerToolCaller:`

              Tool invocation generated by a server-side tool.

              - `String toolId`

              - `JsonValue; type "code_execution_20250825"constant`

                - `CODE_EXECUTION_20250825("code_execution_20250825")`

            - `class ServerToolCaller20260120:`

              - `String toolId`

              - `JsonValue; type "code_execution_20260120"constant`

                - `CODE_EXECUTION_20260120("code_execution_20260120")`

          - `Input input`

          - `String name`

          - `JsonValue; type "tool_use"constant`

            - `TOOL_USE("tool_use")`

        - `class ServerToolUseBlock:`

          - `String id`

          - `Caller caller`

            Tool invocation directly from the model.

            - `class DirectCaller:`

              Tool invocation directly from the model.

              - `JsonValue; type "direct"constant`

                - `DIRECT("direct")`

            - `class ServerToolCaller:`

              Tool invocation generated by a server-side tool.

              - `String toolId`

              - `JsonValue; type "code_execution_20250825"constant`

                - `CODE_EXECUTION_20250825("code_execution_20250825")`

            - `class ServerToolCaller20260120:`

              - `String toolId`

              - `JsonValue; type "code_execution_20260120"constant`

                - `CODE_EXECUTION_20260120("code_execution_20260120")`

          - `Input input`

          - `Name name`

            - `WEB_SEARCH("web_search")`

            - `WEB_FETCH("web_fetch")`

            - `CODE_EXECUTION("code_execution")`

            - `BASH_CODE_EXECUTION("bash_code_execution")`

            - `TEXT_EDITOR_CODE_EXECUTION("text_editor_code_execution")`

            - `TOOL_SEARCH_TOOL_REGEX("tool_search_tool_regex")`

            - `TOOL_SEARCH_TOOL_BM25("tool_search_tool_bm25")`

          - `JsonValue; type "server_tool_use"constant`

            - `SERVER_TOOL_USE("server_tool_use")`

        - `class WebSearchToolResultBlock:`

          - `Caller caller`

            Tool invocation directly from the model.

            - `class DirectCaller:`

              Tool invocation directly from the model.

              - `JsonValue; type "direct"constant`

                - `DIRECT("direct")`

            - `class ServerToolCaller:`

              Tool invocation generated by a server-side tool.

              - `String toolId`

              - `JsonValue; type "code_execution_20250825"constant`

                - `CODE_EXECUTION_20250825("code_execution_20250825")`

            - `class ServerToolCaller20260120:`

              - `String toolId`

              - `JsonValue; type "code_execution_20260120"constant`

                - `CODE_EXECUTION_20260120("code_execution_20260120")`

          - `WebSearchToolResultBlockContent content`

            - `class WebSearchToolResultError:`

              - `WebSearchToolResultErrorCode errorCode`

                - `INVALID_TOOL_INPUT("invalid_tool_input")`

                - `UNAVAILABLE("unavailable")`

                - `MAX_USES_EXCEEDED("max_uses_exceeded")`

                - `TOO_MANY_REQUESTS("too_many_requests")`

                - `QUERY_TOO_LONG("query_too_long")`

                - `REQUEST_TOO_LARGE("request_too_large")`

              - `JsonValue; type "web_search_tool_result_error"constant`

                - `WEB_SEARCH_TOOL_RESULT_ERROR("web_search_tool_result_error")`

            - `List<WebSearchResultBlock>`

              - `String encryptedContent`

              - `Optional<String> pageAge`

              - `String title`

              - `JsonValue; type "web_search_result"constant`

                - `WEB_SEARCH_RESULT("web_search_result")`

              - `String url`

          - `String toolUseId`

          - `JsonValue; type "web_search_tool_result"constant`

            - `WEB_SEARCH_TOOL_RESULT("web_search_tool_result")`

        - `class WebFetchToolResultBlock:`

          - `Caller caller`

            Tool invocation directly from the model.

            - `class DirectCaller:`

              Tool invocation directly from the model.

              - `JsonValue; type "direct"constant`

                - `DIRECT("direct")`

            - `class ServerToolCaller:`

              Tool invocation generated by a server-side tool.

              - `String toolId`

              - `JsonValue; type "code_execution_20250825"constant`

                - `CODE_EXECUTION_20250825("code_execution_20250825")`

            - `class ServerToolCaller20260120:`

              - `String toolId`

              - `JsonValue; type "code_execution_20260120"constant`

                - `CODE_EXECUTION_20260120("code_execution_20260120")`

          - `Content content`

            - `class WebFetchToolResultErrorBlock:`

              - `WebFetchToolResultErrorCode errorCode`

                - `INVALID_TOOL_INPUT("invalid_tool_input")`

                - `URL_TOO_LONG("url_too_long")`

                - `URL_NOT_ALLOWED("url_not_allowed")`

                - `URL_NOT_ACCESSIBLE("url_not_accessible")`

                - `UNSUPPORTED_CONTENT_TYPE("unsupported_content_type")`

                - `TOO_MANY_REQUESTS("too_many_requests")`

                - `MAX_USES_EXCEEDED("max_uses_exceeded")`

                - `UNAVAILABLE("unavailable")`

              - `JsonValue; type "web_fetch_tool_result_error"constant`

                - `WEB_FETCH_TOOL_RESULT_ERROR("web_fetch_tool_result_error")`

            - `class WebFetchBlock:`

              - `DocumentBlock content`

                - `Optional<CitationsConfig> citations`

                  Citation configuration for the document

                  - `boolean enabled`

                - `Source source`

                  - `class Base64PdfSource:`

                    - `String data`

                    - `JsonValue; mediaType "application/pdf"constant`

                      - `APPLICATION_PDF("application/pdf")`

                    - `JsonValue; type "base64"constant`

                      - `BASE64("base64")`

                  - `class PlainTextSource:`

                    - `String data`

                    - `JsonValue; mediaType "text/plain"constant`

                      - `TEXT_PLAIN("text/plain")`

                    - `JsonValue; type "text"constant`

                      - `TEXT("text")`

                - `Optional<String> title`

                  The title of the document

                - `JsonValue; type "document"constant`

                  - `DOCUMENT("document")`

              - `Optional<String> retrievedAt`

                ISO 8601 timestamp when the content was retrieved

              - `JsonValue; type "web_fetch_result"constant`

                - `WEB_FETCH_RESULT("web_fetch_result")`

              - `String url`

                Fetched content URL

          - `String toolUseId`

          - `JsonValue; type "web_fetch_tool_result"constant`

            - `WEB_FETCH_TOOL_RESULT("web_fetch_tool_result")`

        - `class CodeExecutionToolResultBlock:`

          - `CodeExecutionToolResultBlockContent content`

            Code execution result with encrypted stdout for PFC + web_search results.

            - `class CodeExecutionToolResultError:`

              - `CodeExecutionToolResultErrorCode errorCode`

                - `INVALID_TOOL_INPUT("invalid_tool_input")`

                - `UNAVAILABLE("unavailable")`

                - `TOO_MANY_REQUESTS("too_many_requests")`

                - `EXECUTION_TIME_EXCEEDED("execution_time_exceeded")`

              - `JsonValue; type "code_execution_tool_result_error"constant`

                - `CODE_EXECUTION_TOOL_RESULT_ERROR("code_execution_tool_result_error")`

            - `class CodeExecutionResultBlock:`

              - `List<CodeExecutionOutputBlock> content`

                - `String fileId`

                - `JsonValue; type "code_execution_output"constant`

                  - `CODE_EXECUTION_OUTPUT("code_execution_output")`

              - `long returnCode`

              - `String stderr`

              - `String stdout`

              - `JsonValue; type "code_execution_result"constant`

                - `CODE_EXECUTION_RESULT("code_execution_result")`

            - `class EncryptedCodeExecutionResultBlock:`

              Code execution result with encrypted stdout for PFC + web_search results.

              - `List<CodeExecutionOutputBlock> content`

                - `String fileId`

                - `JsonValue; type "code_execution_output"constant`

                  - `CODE_EXECUTION_OUTPUT("code_execution_output")`

              - `String encryptedStdout`

              - `long returnCode`

              - `String stderr`

              - `JsonValue; type "encrypted_code_execution_result"constant`

                - `ENCRYPTED_CODE_EXECUTION_RESULT("encrypted_code_execution_result")`

          - `String toolUseId`

          - `JsonValue; type "code_execution_tool_result"constant`

            - `CODE_EXECUTION_TOOL_RESULT("code_execution_tool_result")`

        - `class BashCodeExecutionToolResultBlock:`

          - `Content content`

            - `class BashCodeExecutionToolResultError:`

              - `BashCodeExecutionToolResultErrorCode errorCode`

                - `INVALID_TOOL_INPUT("invalid_tool_input")`

                - `UNAVAILABLE("unavailable")`

                - `TOO_MANY_REQUESTS("too_many_requests")`

                - `EXECUTION_TIME_EXCEEDED("execution_time_exceeded")`

                - `OUTPUT_FILE_TOO_LARGE("output_file_too_large")`

              - `JsonValue; type "bash_code_execution_tool_result_error"constant`

                - `BASH_CODE_EXECUTION_TOOL_RESULT_ERROR("bash_code_execution_tool_result_error")`

            - `class BashCodeExecutionResultBlock:`

              - `List<BashCodeExecutionOutputBlock> content`

                - `String fileId`

                - `JsonValue; type "bash_code_execution_output"constant`

                  - `BASH_CODE_EXECUTION_OUTPUT("bash_code_execution_output")`

              - `long returnCode`

              - `String stderr`

              - `String stdout`

              - `JsonValue; type "bash_code_execution_result"constant`

                - `BASH_CODE_EXECUTION_RESULT("bash_code_execution_result")`

          - `String toolUseId`

          - `JsonValue; type "bash_code_execution_tool_result"constant`

            - `BASH_CODE_EXECUTION_TOOL_RESULT("bash_code_execution_tool_result")`

        - `class TextEditorCodeExecutionToolResultBlock:`

          - `Content content`

            - `class TextEditorCodeExecutionToolResultError:`

              - `TextEditorCodeExecutionToolResultErrorCode errorCode`

                - `INVALID_TOOL_INPUT("invalid_tool_input")`

                - `UNAVAILABLE("unavailable")`

                - `TOO_MANY_REQUESTS("too_many_requests")`

                - `EXECUTION_TIME_EXCEEDED("execution_time_exceeded")`

                - `FILE_NOT_FOUND("file_not_found")`

              - `Optional<String> errorMessage`

              - `JsonValue; type "text_editor_code_execution_tool_result_error"constant`

                - `TEXT_EDITOR_CODE_EXECUTION_TOOL_RESULT_ERROR("text_editor_code_execution_tool_result_error")`

            - `class TextEditorCodeExecutionViewResultBlock:`

              - `String content`

              - `FileType fileType`

                - `TEXT("text")`

                - `IMAGE("image")`

                - `PDF("pdf")`

              - `Optional<Long> numLines`

              - `Optional<Long> startLine`

              - `Optional<Long> totalLines`

              - `JsonValue; type "text_editor_code_execution_view_result"constant`

                - `TEXT_EDITOR_CODE_EXECUTION_VIEW_RESULT("text_editor_code_execution_view_result")`

            - `class TextEditorCodeExecutionCreateResultBlock:`

              - `boolean isFileUpdate`

              - `JsonValue; type "text_editor_code_execution_create_result"constant`

                - `TEXT_EDITOR_CODE_EXECUTION_CREATE_RESULT("text_editor_code_execution_create_result")`

            - `class TextEditorCodeExecutionStrReplaceResultBlock:`

              - `Optional<List<String>> lines`

              - `Optional<Long> newLines`

              - `Optional<Long> newStart`

              - `Optional<Long> oldLines`

              - `Optional<Long> oldStart`

              - `JsonValue; type "text_editor_code_execution_str_replace_result"constant`

                - `TEXT_EDITOR_CODE_EXECUTION_STR_REPLACE_RESULT("text_editor_code_execution_str_replace_result")`

          - `String toolUseId`

          - `JsonValue; type "text_editor_code_execution_tool_result"constant`

            - `TEXT_EDITOR_CODE_EXECUTION_TOOL_RESULT("text_editor_code_execution_tool_result")`

        - `class ToolSearchToolResultBlock:`

          - `Content content`

            - `class ToolSearchToolResultError:`

              - `ToolSearchToolResultErrorCode errorCode`

                - `INVALID_TOOL_INPUT("invalid_tool_input")`

                - `UNAVAILABLE("unavailable")`

                - `TOO_MANY_REQUESTS("too_many_requests")`

                - `EXECUTION_TIME_EXCEEDED("execution_time_exceeded")`

              - `Optional<String> errorMessage`

              - `JsonValue; type "tool_search_tool_result_error"constant`

                - `TOOL_SEARCH_TOOL_RESULT_ERROR("tool_search_tool_result_error")`

            - `class ToolSearchToolSearchResultBlock:`

              - `List<ToolReferenceBlock> toolReferences`

                - `String toolName`

                - `JsonValue; type "tool_reference"constant`

                  - `TOOL_REFERENCE("tool_reference")`

              - `JsonValue; type "tool_search_tool_search_result"constant`

                - `TOOL_SEARCH_TOOL_SEARCH_RESULT("tool_search_tool_search_result")`

          - `String toolUseId`

          - `JsonValue; type "tool_search_tool_result"constant`

            - `TOOL_SEARCH_TOOL_RESULT("tool_search_tool_result")`

        - `class ContainerUploadBlock:`

          Response model for a file uploaded to the container.

          - `String fileId`

          - `JsonValue; type "container_upload"constant`

            - `CONTAINER_UPLOAD("container_upload")`

      - `Model model`

        The model that will complete your prompt.

        See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

        - `CLAUDE_OPUS_4_6("claude-opus-4-6")`

          Most intelligent model for building agents and coding

        - `CLAUDE_SONNET_4_6("claude-sonnet-4-6")`

          Frontier intelligence at scale — built for coding, agents, and enterprise workflows

        - `CLAUDE_OPUS_4_5_20251101("claude-opus-4-5-20251101")`

          Premium model combining maximum intelligence with practical performance

        - `CLAUDE_OPUS_4_5("claude-opus-4-5")`

          Premium model combining maximum intelligence with practical performance

        - `CLAUDE_3_7_SONNET_LATEST("claude-3-7-sonnet-latest")`

          High-performance model with early extended thinking

        - `CLAUDE_3_7_SONNET_20250219("claude-3-7-sonnet-20250219")`

          High-performance model with early extended thinking

        - `CLAUDE_3_5_HAIKU_LATEST("claude-3-5-haiku-latest")`

          Fastest and most compact model for near-instant responsiveness

        - `CLAUDE_3_5_HAIKU_20241022("claude-3-5-haiku-20241022")`

          Our fastest model

        - `CLAUDE_HAIKU_4_5("claude-haiku-4-5")`

          Hybrid model, capable of near-instant responses and extended thinking

        - `CLAUDE_HAIKU_4_5_20251001("claude-haiku-4-5-20251001")`

          Hybrid model, capable of near-instant responses and extended thinking

        - `CLAUDE_SONNET_4_20250514("claude-sonnet-4-20250514")`

          High-performance model with extended thinking

        - `CLAUDE_SONNET_4_0("claude-sonnet-4-0")`

          High-performance model with extended thinking

        - `CLAUDE_4_SONNET_20250514("claude-4-sonnet-20250514")`

          High-performance model with extended thinking

        - `CLAUDE_SONNET_4_5("claude-sonnet-4-5")`

          Our best model for real-world agents and coding

        - `CLAUDE_SONNET_4_5_20250929("claude-sonnet-4-5-20250929")`

          Our best model for real-world agents and coding

        - `CLAUDE_OPUS_4_0("claude-opus-4-0")`

          Our most capable model

        - `CLAUDE_OPUS_4_20250514("claude-opus-4-20250514")`

          Our most capable model

        - `CLAUDE_4_OPUS_20250514("claude-4-opus-20250514")`

          Our most capable model

        - `CLAUDE_OPUS_4_1_20250805("claude-opus-4-1-20250805")`

          Our most capable model

        - `CLAUDE_3_OPUS_LATEST("claude-3-opus-latest")`

          Excels at writing and complex tasks

        - `CLAUDE_3_OPUS_20240229("claude-3-opus-20240229")`

          Excels at writing and complex tasks

        - `CLAUDE_3_HAIKU_20240307("claude-3-haiku-20240307")`

          Our previous most fast and cost-effective

      - `JsonValue; role "assistant"constant`

        Conversational role of the generated message.

        This will always be `"assistant"`.

        - `ASSISTANT("assistant")`

      - `Optional<StopReason> stopReason`

        The reason that we stopped.

        This may be one the following values:

        * `"end_turn"`: the model reached a natural stopping point
        * `"max_tokens"`: we exceeded the requested `max_tokens` or the model's maximum
        * `"stop_sequence"`: one of your provided custom `stop_sequences` was generated
        * `"tool_use"`: the model invoked one or more tools
        * `"pause_turn"`: we paused a long-running turn. You may provide the response back as-is in a subsequent request to let the model continue.
        * `"refusal"`: when streaming classifiers intervene to handle potential policy violations

        In non-streaming mode this value is always non-null. In streaming mode, it is null in the `message_start` event and non-null otherwise.

        - `END_TURN("end_turn")`

        - `MAX_TOKENS("max_tokens")`

        - `STOP_SEQUENCE("stop_sequence")`

        - `TOOL_USE("tool_use")`

        - `PAUSE_TURN("pause_turn")`

        - `REFUSAL("refusal")`

      - `Optional<String> stopSequence`

        Which custom stop sequence was generated, if any.

        This value will be a non-null string if one of your custom stop sequences was generated.

      - `JsonValue; type "message"constant`

        Object type.

        For Messages, this is always `"message"`.

        - `MESSAGE("message")`

      - `Usage usage`

        Billing and rate-limit usage.

        Anthropic's API bills and rate-limits by token counts, as tokens represent the underlying cost to our systems.

        Under the hood, the API transforms requests into a format suitable for the model. The model's output then goes through a parsing stage before becoming an API response. As a result, the token counts in `usage` will not match one-to-one with the exact visible content of an API request or response.

        For example, `output_tokens` will be non-zero, even for an empty string response from Claude.

        Total input tokens in a request is the summation of `input_tokens`, `cache_creation_input_tokens`, and `cache_read_input_tokens`.

        - `Optional<CacheCreation> cacheCreation`

          Breakdown of cached tokens by TTL

          - `long ephemeral1hInputTokens`

            The number of input tokens used to create the 1 hour cache entry.

          - `long ephemeral5mInputTokens`

            The number of input tokens used to create the 5 minute cache entry.

        - `Optional<Long> cacheCreationInputTokens`

          The number of input tokens used to create the cache entry.

        - `Optional<Long> cacheReadInputTokens`

          The number of input tokens read from the cache.

        - `Optional<String> inferenceGeo`

          The geographic region where inference was performed for this request.

        - `long inputTokens`

          The number of input tokens which were used.

        - `long outputTokens`

          The number of output tokens which were used.

        - `Optional<ServerToolUsage> serverToolUse`

          The number of server tool requests.

          - `long webFetchRequests`

            The number of web fetch tool requests.

          - `long webSearchRequests`

            The number of web search tool requests.

        - `Optional<ServiceTier> serviceTier`

          If the request used the priority, standard, or batch tier.

          - `STANDARD("standard")`

          - `PRIORITY("priority")`

          - `BATCH("batch")`

    - `JsonValue; type "succeeded"constant`

      - `SUCCEEDED("succeeded")`

  - `class MessageBatchErroredResult:`

    - `ErrorResponse error`

      - `ErrorObject error`

        - `class InvalidRequestError:`

          - `String message`

          - `JsonValue; type "invalid_request_error"constant`

            - `INVALID_REQUEST_ERROR("invalid_request_error")`

        - `class AuthenticationError:`

          - `String message`

          - `JsonValue; type "authentication_error"constant`

            - `AUTHENTICATION_ERROR("authentication_error")`

        - `class BillingError:`

          - `String message`

          - `JsonValue; type "billing_error"constant`

            - `BILLING_ERROR("billing_error")`

        - `class PermissionError:`

          - `String message`

          - `JsonValue; type "permission_error"constant`

            - `PERMISSION_ERROR("permission_error")`

        - `class NotFoundError:`

          - `String message`

          - `JsonValue; type "not_found_error"constant`

            - `NOT_FOUND_ERROR("not_found_error")`

        - `class RateLimitError:`

          - `String message`

          - `JsonValue; type "rate_limit_error"constant`

            - `RATE_LIMIT_ERROR("rate_limit_error")`

        - `class GatewayTimeoutError:`

          - `String message`

          - `JsonValue; type "timeout_error"constant`

            - `TIMEOUT_ERROR("timeout_error")`

        - `class ApiErrorObject:`

          - `String message`

          - `JsonValue; type "api_error"constant`

            - `API_ERROR("api_error")`

        - `class OverloadedError:`

          - `String message`

          - `JsonValue; type "overloaded_error"constant`

            - `OVERLOADED_ERROR("overloaded_error")`

      - `Optional<String> requestId`

      - `JsonValue; type "error"constant`

        - `ERROR("error")`

    - `JsonValue; type "errored"constant`

      - `ERRORED("errored")`

  - `class MessageBatchCanceledResult:`

    - `JsonValue; type "canceled"constant`

      - `CANCELED("canceled")`

  - `class MessageBatchExpiredResult:`

    - `JsonValue; type "expired"constant`

      - `EXPIRED("expired")`

### Message Batch Succeeded Result

- `class MessageBatchSucceededResult:`

  - `Message message`

    - `String id`

      Unique object identifier.

      The format and length of IDs may change over time.

    - `Optional<Container> container`

      Information about the container used in the request (for the code execution tool)

      - `String id`

        Identifier for the container used in this request

      - `LocalDateTime expiresAt`

        The time at which the container will expire.

    - `List<ContentBlock> content`

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

      - `class TextBlock:`

        - `Optional<List<TextCitation>> citations`

          Citations supporting the text block.

          The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

          - `class CitationCharLocation:`

            - `String citedText`

            - `long documentIndex`

            - `Optional<String> documentTitle`

            - `long endCharIndex`

            - `Optional<String> fileId`

            - `long startCharIndex`

            - `JsonValue; type "char_location"constant`

              - `CHAR_LOCATION("char_location")`

          - `class CitationPageLocation:`

            - `String citedText`

            - `long documentIndex`

            - `Optional<String> documentTitle`

            - `long endPageNumber`

            - `Optional<String> fileId`

            - `long startPageNumber`

            - `JsonValue; type "page_location"constant`

              - `PAGE_LOCATION("page_location")`

          - `class CitationContentBlockLocation:`

            - `String citedText`

            - `long documentIndex`

            - `Optional<String> documentTitle`

            - `long endBlockIndex`

            - `Optional<String> fileId`

            - `long startBlockIndex`

            - `JsonValue; type "content_block_location"constant`

              - `CONTENT_BLOCK_LOCATION("content_block_location")`

          - `class CitationsWebSearchResultLocation:`

            - `String citedText`

            - `String encryptedIndex`

            - `Optional<String> title`

            - `JsonValue; type "web_search_result_location"constant`

              - `WEB_SEARCH_RESULT_LOCATION("web_search_result_location")`

            - `String url`

          - `class CitationsSearchResultLocation:`

            - `String citedText`

            - `long endBlockIndex`

            - `long searchResultIndex`

            - `String source`

            - `long startBlockIndex`

            - `Optional<String> title`

            - `JsonValue; type "search_result_location"constant`

              - `SEARCH_RESULT_LOCATION("search_result_location")`

        - `String text`

        - `JsonValue; type "text"constant`

          - `TEXT("text")`

      - `class ThinkingBlock:`

        - `String signature`

        - `String thinking`

        - `JsonValue; type "thinking"constant`

          - `THINKING("thinking")`

      - `class RedactedThinkingBlock:`

        - `String data`

        - `JsonValue; type "redacted_thinking"constant`

          - `REDACTED_THINKING("redacted_thinking")`

      - `class ToolUseBlock:`

        - `String id`

        - `Caller caller`

          Tool invocation directly from the model.

          - `class DirectCaller:`

            Tool invocation directly from the model.

            - `JsonValue; type "direct"constant`

              - `DIRECT("direct")`

          - `class ServerToolCaller:`

            Tool invocation generated by a server-side tool.

            - `String toolId`

            - `JsonValue; type "code_execution_20250825"constant`

              - `CODE_EXECUTION_20250825("code_execution_20250825")`

          - `class ServerToolCaller20260120:`

            - `String toolId`

            - `JsonValue; type "code_execution_20260120"constant`

              - `CODE_EXECUTION_20260120("code_execution_20260120")`

        - `Input input`

        - `String name`

        - `JsonValue; type "tool_use"constant`

          - `TOOL_USE("tool_use")`

      - `class ServerToolUseBlock:`

        - `String id`

        - `Caller caller`

          Tool invocation directly from the model.

          - `class DirectCaller:`

            Tool invocation directly from the model.

            - `JsonValue; type "direct"constant`

              - `DIRECT("direct")`

          - `class ServerToolCaller:`

            Tool invocation generated by a server-side tool.

            - `String toolId`

            - `JsonValue; type "code_execution_20250825"constant`

              - `CODE_EXECUTION_20250825("code_execution_20250825")`

          - `class ServerToolCaller20260120:`

            - `String toolId`

            - `JsonValue; type "code_execution_20260120"constant`

              - `CODE_EXECUTION_20260120("code_execution_20260120")`

        - `Input input`

        - `Name name`

          - `WEB_SEARCH("web_search")`

          - `WEB_FETCH("web_fetch")`

          - `CODE_EXECUTION("code_execution")`

          - `BASH_CODE_EXECUTION("bash_code_execution")`

          - `TEXT_EDITOR_CODE_EXECUTION("text_editor_code_execution")`

          - `TOOL_SEARCH_TOOL_REGEX("tool_search_tool_regex")`

          - `TOOL_SEARCH_TOOL_BM25("tool_search_tool_bm25")`

        - `JsonValue; type "server_tool_use"constant`

          - `SERVER_TOOL_USE("server_tool_use")`

      - `class WebSearchToolResultBlock:`

        - `Caller caller`

          Tool invocation directly from the model.

          - `class DirectCaller:`

            Tool invocation directly from the model.

            - `JsonValue; type "direct"constant`

              - `DIRECT("direct")`

          - `class ServerToolCaller:`

            Tool invocation generated by a server-side tool.

            - `String toolId`

            - `JsonValue; type "code_execution_20250825"constant`

              - `CODE_EXECUTION_20250825("code_execution_20250825")`

          - `class ServerToolCaller20260120:`

            - `String toolId`

            - `JsonValue; type "code_execution_20260120"constant`

              - `CODE_EXECUTION_20260120("code_execution_20260120")`

        - `WebSearchToolResultBlockContent content`

          - `class WebSearchToolResultError:`

            - `WebSearchToolResultErrorCode errorCode`

              - `INVALID_TOOL_INPUT("invalid_tool_input")`

              - `UNAVAILABLE("unavailable")`

              - `MAX_USES_EXCEEDED("max_uses_exceeded")`

              - `TOO_MANY_REQUESTS("too_many_requests")`

              - `QUERY_TOO_LONG("query_too_long")`

              - `REQUEST_TOO_LARGE("request_too_large")`

            - `JsonValue; type "web_search_tool_result_error"constant`

              - `WEB_SEARCH_TOOL_RESULT_ERROR("web_search_tool_result_error")`

          - `List<WebSearchResultBlock>`

            - `String encryptedContent`

            - `Optional<String> pageAge`

            - `String title`

            - `JsonValue; type "web_search_result"constant`

              - `WEB_SEARCH_RESULT("web_search_result")`

            - `String url`

        - `String toolUseId`

        - `JsonValue; type "web_search_tool_result"constant`

          - `WEB_SEARCH_TOOL_RESULT("web_search_tool_result")`

      - `class WebFetchToolResultBlock:`

        - `Caller caller`

          Tool invocation directly from the model.

          - `class DirectCaller:`

            Tool invocation directly from the model.

            - `JsonValue; type "direct"constant`

              - `DIRECT("direct")`

          - `class ServerToolCaller:`

            Tool invocation generated by a server-side tool.

            - `String toolId`

            - `JsonValue; type "code_execution_20250825"constant`

              - `CODE_EXECUTION_20250825("code_execution_20250825")`

          - `class ServerToolCaller20260120:`

            - `String toolId`

            - `JsonValue; type "code_execution_20260120"constant`

              - `CODE_EXECUTION_20260120("code_execution_20260120")`

        - `Content content`

          - `class WebFetchToolResultErrorBlock:`

            - `WebFetchToolResultErrorCode errorCode`

              - `INVALID_TOOL_INPUT("invalid_tool_input")`

              - `URL_TOO_LONG("url_too_long")`

              - `URL_NOT_ALLOWED("url_not_allowed")`

              - `URL_NOT_ACCESSIBLE("url_not_accessible")`

              - `UNSUPPORTED_CONTENT_TYPE("unsupported_content_type")`

              - `TOO_MANY_REQUESTS("too_many_requests")`

              - `MAX_USES_EXCEEDED("max_uses_exceeded")`

              - `UNAVAILABLE("unavailable")`

            - `JsonValue; type "web_fetch_tool_result_error"constant`

              - `WEB_FETCH_TOOL_RESULT_ERROR("web_fetch_tool_result_error")`

          - `class WebFetchBlock:`

            - `DocumentBlock content`

              - `Optional<CitationsConfig> citations`

                Citation configuration for the document

                - `boolean enabled`

              - `Source source`

                - `class Base64PdfSource:`

                  - `String data`

                  - `JsonValue; mediaType "application/pdf"constant`

                    - `APPLICATION_PDF("application/pdf")`

                  - `JsonValue; type "base64"constant`

                    - `BASE64("base64")`

                - `class PlainTextSource:`

                  - `String data`

                  - `JsonValue; mediaType "text/plain"constant`

                    - `TEXT_PLAIN("text/plain")`

                  - `JsonValue; type "text"constant`

                    - `TEXT("text")`

              - `Optional<String> title`

                The title of the document

              - `JsonValue; type "document"constant`

                - `DOCUMENT("document")`

            - `Optional<String> retrievedAt`

              ISO 8601 timestamp when the content was retrieved

            - `JsonValue; type "web_fetch_result"constant`

              - `WEB_FETCH_RESULT("web_fetch_result")`

            - `String url`

              Fetched content URL

        - `String toolUseId`

        - `JsonValue; type "web_fetch_tool_result"constant`

          - `WEB_FETCH_TOOL_RESULT("web_fetch_tool_result")`

      - `class CodeExecutionToolResultBlock:`

        - `CodeExecutionToolResultBlockContent content`

          Code execution result with encrypted stdout for PFC + web_search results.

          - `class CodeExecutionToolResultError:`

            - `CodeExecutionToolResultErrorCode errorCode`

              - `INVALID_TOOL_INPUT("invalid_tool_input")`

              - `UNAVAILABLE("unavailable")`

              - `TOO_MANY_REQUESTS("too_many_requests")`

              - `EXECUTION_TIME_EXCEEDED("execution_time_exceeded")`

            - `JsonValue; type "code_execution_tool_result_error"constant`

              - `CODE_EXECUTION_TOOL_RESULT_ERROR("code_execution_tool_result_error")`

          - `class CodeExecutionResultBlock:`

            - `List<CodeExecutionOutputBlock> content`

              - `String fileId`

              - `JsonValue; type "code_execution_output"constant`

                - `CODE_EXECUTION_OUTPUT("code_execution_output")`

            - `long returnCode`

            - `String stderr`

            - `String stdout`

            - `JsonValue; type "code_execution_result"constant`

              - `CODE_EXECUTION_RESULT("code_execution_result")`

          - `class EncryptedCodeExecutionResultBlock:`

            Code execution result with encrypted stdout for PFC + web_search results.

            - `List<CodeExecutionOutputBlock> content`

              - `String fileId`

              - `JsonValue; type "code_execution_output"constant`

                - `CODE_EXECUTION_OUTPUT("code_execution_output")`

            - `String encryptedStdout`

            - `long returnCode`

            - `String stderr`

            - `JsonValue; type "encrypted_code_execution_result"constant`

              - `ENCRYPTED_CODE_EXECUTION_RESULT("encrypted_code_execution_result")`

        - `String toolUseId`

        - `JsonValue; type "code_execution_tool_result"constant`

          - `CODE_EXECUTION_TOOL_RESULT("code_execution_tool_result")`

      - `class BashCodeExecutionToolResultBlock:`

        - `Content content`

          - `class BashCodeExecutionToolResultError:`

            - `BashCodeExecutionToolResultErrorCode errorCode`

              - `INVALID_TOOL_INPUT("invalid_tool_input")`

              - `UNAVAILABLE("unavailable")`

              - `TOO_MANY_REQUESTS("too_many_requests")`

              - `EXECUTION_TIME_EXCEEDED("execution_time_exceeded")`

              - `OUTPUT_FILE_TOO_LARGE("output_file_too_large")`

            - `JsonValue; type "bash_code_execution_tool_result_error"constant`

              - `BASH_CODE_EXECUTION_TOOL_RESULT_ERROR("bash_code_execution_tool_result_error")`

          - `class BashCodeExecutionResultBlock:`

            - `List<BashCodeExecutionOutputBlock> content`

              - `String fileId`

              - `JsonValue; type "bash_code_execution_output"constant`

                - `BASH_CODE_EXECUTION_OUTPUT("bash_code_execution_output")`

            - `long returnCode`

            - `String stderr`

            - `String stdout`

            - `JsonValue; type "bash_code_execution_result"constant`

              - `BASH_CODE_EXECUTION_RESULT("bash_code_execution_result")`

        - `String toolUseId`

        - `JsonValue; type "bash_code_execution_tool_result"constant`

          - `BASH_CODE_EXECUTION_TOOL_RESULT("bash_code_execution_tool_result")`

      - `class TextEditorCodeExecutionToolResultBlock:`

        - `Content content`

          - `class TextEditorCodeExecutionToolResultError:`

            - `TextEditorCodeExecutionToolResultErrorCode errorCode`

              - `INVALID_TOOL_INPUT("invalid_tool_input")`

              - `UNAVAILABLE("unavailable")`

              - `TOO_MANY_REQUESTS("too_many_requests")`

              - `EXECUTION_TIME_EXCEEDED("execution_time_exceeded")`

              - `FILE_NOT_FOUND("file_not_found")`

            - `Optional<String> errorMessage`

            - `JsonValue; type "text_editor_code_execution_tool_result_error"constant`

              - `TEXT_EDITOR_CODE_EXECUTION_TOOL_RESULT_ERROR("text_editor_code_execution_tool_result_error")`

          - `class TextEditorCodeExecutionViewResultBlock:`

            - `String content`

            - `FileType fileType`

              - `TEXT("text")`

              - `IMAGE("image")`

              - `PDF("pdf")`

            - `Optional<Long> numLines`

            - `Optional<Long> startLine`

            - `Optional<Long> totalLines`

            - `JsonValue; type "text_editor_code_execution_view_result"constant`

              - `TEXT_EDITOR_CODE_EXECUTION_VIEW_RESULT("text_editor_code_execution_view_result")`

          - `class TextEditorCodeExecutionCreateResultBlock:`

            - `boolean isFileUpdate`

            - `JsonValue; type "text_editor_code_execution_create_result"constant`

              - `TEXT_EDITOR_CODE_EXECUTION_CREATE_RESULT("text_editor_code_execution_create_result")`

          - `class TextEditorCodeExecutionStrReplaceResultBlock:`

            - `Optional<List<String>> lines`

            - `Optional<Long> newLines`

            - `Optional<Long> newStart`

            - `Optional<Long> oldLines`

            - `Optional<Long> oldStart`

            - `JsonValue; type "text_editor_code_execution_str_replace_result"constant`

              - `TEXT_EDITOR_CODE_EXECUTION_STR_REPLACE_RESULT("text_editor_code_execution_str_replace_result")`

        - `String toolUseId`

        - `JsonValue; type "text_editor_code_execution_tool_result"constant`

          - `TEXT_EDITOR_CODE_EXECUTION_TOOL_RESULT("text_editor_code_execution_tool_result")`

      - `class ToolSearchToolResultBlock:`

        - `Content content`

          - `class ToolSearchToolResultError:`

            - `ToolSearchToolResultErrorCode errorCode`

              - `INVALID_TOOL_INPUT("invalid_tool_input")`

              - `UNAVAILABLE("unavailable")`

              - `TOO_MANY_REQUESTS("too_many_requests")`

              - `EXECUTION_TIME_EXCEEDED("execution_time_exceeded")`

            - `Optional<String> errorMessage`

            - `JsonValue; type "tool_search_tool_result_error"constant`

              - `TOOL_SEARCH_TOOL_RESULT_ERROR("tool_search_tool_result_error")`

          - `class ToolSearchToolSearchResultBlock:`

            - `List<ToolReferenceBlock> toolReferences`

              - `String toolName`

              - `JsonValue; type "tool_reference"constant`

                - `TOOL_REFERENCE("tool_reference")`

            - `JsonValue; type "tool_search_tool_search_result"constant`

              - `TOOL_SEARCH_TOOL_SEARCH_RESULT("tool_search_tool_search_result")`

        - `String toolUseId`

        - `JsonValue; type "tool_search_tool_result"constant`

          - `TOOL_SEARCH_TOOL_RESULT("tool_search_tool_result")`

      - `class ContainerUploadBlock:`

        Response model for a file uploaded to the container.

        - `String fileId`

        - `JsonValue; type "container_upload"constant`

          - `CONTAINER_UPLOAD("container_upload")`

    - `Model model`

      The model that will complete your prompt.

      See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

      - `CLAUDE_OPUS_4_6("claude-opus-4-6")`

        Most intelligent model for building agents and coding

      - `CLAUDE_SONNET_4_6("claude-sonnet-4-6")`

        Frontier intelligence at scale — built for coding, agents, and enterprise workflows

      - `CLAUDE_OPUS_4_5_20251101("claude-opus-4-5-20251101")`

        Premium model combining maximum intelligence with practical performance

      - `CLAUDE_OPUS_4_5("claude-opus-4-5")`

        Premium model combining maximum intelligence with practical performance

      - `CLAUDE_3_7_SONNET_LATEST("claude-3-7-sonnet-latest")`

        High-performance model with early extended thinking

      - `CLAUDE_3_7_SONNET_20250219("claude-3-7-sonnet-20250219")`

        High-performance model with early extended thinking

      - `CLAUDE_3_5_HAIKU_LATEST("claude-3-5-haiku-latest")`

        Fastest and most compact model for near-instant responsiveness

      - `CLAUDE_3_5_HAIKU_20241022("claude-3-5-haiku-20241022")`

        Our fastest model

      - `CLAUDE_HAIKU_4_5("claude-haiku-4-5")`

        Hybrid model, capable of near-instant responses and extended thinking

      - `CLAUDE_HAIKU_4_5_20251001("claude-haiku-4-5-20251001")`

        Hybrid model, capable of near-instant responses and extended thinking

      - `CLAUDE_SONNET_4_20250514("claude-sonnet-4-20250514")`

        High-performance model with extended thinking

      - `CLAUDE_SONNET_4_0("claude-sonnet-4-0")`

        High-performance model with extended thinking

      - `CLAUDE_4_SONNET_20250514("claude-4-sonnet-20250514")`

        High-performance model with extended thinking

      - `CLAUDE_SONNET_4_5("claude-sonnet-4-5")`

        Our best model for real-world agents and coding

      - `CLAUDE_SONNET_4_5_20250929("claude-sonnet-4-5-20250929")`

        Our best model for real-world agents and coding

      - `CLAUDE_OPUS_4_0("claude-opus-4-0")`

        Our most capable model

      - `CLAUDE_OPUS_4_20250514("claude-opus-4-20250514")`

        Our most capable model

      - `CLAUDE_4_OPUS_20250514("claude-4-opus-20250514")`

        Our most capable model

      - `CLAUDE_OPUS_4_1_20250805("claude-opus-4-1-20250805")`

        Our most capable model

      - `CLAUDE_3_OPUS_LATEST("claude-3-opus-latest")`

        Excels at writing and complex tasks

      - `CLAUDE_3_OPUS_20240229("claude-3-opus-20240229")`

        Excels at writing and complex tasks

      - `CLAUDE_3_HAIKU_20240307("claude-3-haiku-20240307")`

        Our previous most fast and cost-effective

    - `JsonValue; role "assistant"constant`

      Conversational role of the generated message.

      This will always be `"assistant"`.

      - `ASSISTANT("assistant")`

    - `Optional<StopReason> stopReason`

      The reason that we stopped.

      This may be one the following values:

      * `"end_turn"`: the model reached a natural stopping point
      * `"max_tokens"`: we exceeded the requested `max_tokens` or the model's maximum
      * `"stop_sequence"`: one of your provided custom `stop_sequences` was generated
      * `"tool_use"`: the model invoked one or more tools
      * `"pause_turn"`: we paused a long-running turn. You may provide the response back as-is in a subsequent request to let the model continue.
      * `"refusal"`: when streaming classifiers intervene to handle potential policy violations

      In non-streaming mode this value is always non-null. In streaming mode, it is null in the `message_start` event and non-null otherwise.

      - `END_TURN("end_turn")`

      - `MAX_TOKENS("max_tokens")`

      - `STOP_SEQUENCE("stop_sequence")`

      - `TOOL_USE("tool_use")`

      - `PAUSE_TURN("pause_turn")`

      - `REFUSAL("refusal")`

    - `Optional<String> stopSequence`

      Which custom stop sequence was generated, if any.

      This value will be a non-null string if one of your custom stop sequences was generated.

    - `JsonValue; type "message"constant`

      Object type.

      For Messages, this is always `"message"`.

      - `MESSAGE("message")`

    - `Usage usage`

      Billing and rate-limit usage.

      Anthropic's API bills and rate-limits by token counts, as tokens represent the underlying cost to our systems.

      Under the hood, the API transforms requests into a format suitable for the model. The model's output then goes through a parsing stage before becoming an API response. As a result, the token counts in `usage` will not match one-to-one with the exact visible content of an API request or response.

      For example, `output_tokens` will be non-zero, even for an empty string response from Claude.

      Total input tokens in a request is the summation of `input_tokens`, `cache_creation_input_tokens`, and `cache_read_input_tokens`.

      - `Optional<CacheCreation> cacheCreation`

        Breakdown of cached tokens by TTL

        - `long ephemeral1hInputTokens`

          The number of input tokens used to create the 1 hour cache entry.

        - `long ephemeral5mInputTokens`

          The number of input tokens used to create the 5 minute cache entry.

      - `Optional<Long> cacheCreationInputTokens`

        The number of input tokens used to create the cache entry.

      - `Optional<Long> cacheReadInputTokens`

        The number of input tokens read from the cache.

      - `Optional<String> inferenceGeo`

        The geographic region where inference was performed for this request.

      - `long inputTokens`

        The number of input tokens which were used.

      - `long outputTokens`

        The number of output tokens which were used.

      - `Optional<ServerToolUsage> serverToolUse`

        The number of server tool requests.

        - `long webFetchRequests`

          The number of web fetch tool requests.

        - `long webSearchRequests`

          The number of web search tool requests.

      - `Optional<ServiceTier> serviceTier`

        If the request used the priority, standard, or batch tier.

        - `STANDARD("standard")`

        - `PRIORITY("priority")`

        - `BATCH("batch")`

  - `JsonValue; type "succeeded"constant`

    - `SUCCEEDED("succeeded")`
