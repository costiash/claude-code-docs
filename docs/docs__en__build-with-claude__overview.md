# Features overview

Explore Claude's advanced features and capabilities.

---

Claude's API surface is organized into five areas:

- **Model capabilities:** Control how Claude reasons and formats responses.
- **Tools:** Let Claude take actions on the web or in your environment.
- **Tool infrastructure:** Handles discovery and orchestration at scale.
- **Context management:** Keeps long-running sessions efficient.
- **Files and assets:** Manage the documents and data you provide to Claude.

If you're new, start with [model capabilities](#model-capabilities) and [tools](#tools). Return to the other sections when you're ready to optimize cost, latency, or scale.

## Model capabilities

Ways to steer Claude and Claude's direct outputs, including response format, reasoning depth, and input modalities.

| Feature | Description | Availability |
|---------|-------------|--------------|
| [1M token context window](/docs/en/build-with-claude/context-windows#1m-token-context-window) | An extended context window that allows you to process much larger documents, maintain longer conversations, and work with more extensive codebases. | <PlatformAvailability claudeApiBeta bedrockBeta vertexAiBeta azureAiBeta /> |
| [Adaptive thinking](/docs/en/build-with-claude/adaptive-thinking) | Let Claude dynamically decide when and how much to think. The recommended thinking mode for Opus 4.6. Use the effort parameter to control thinking depth. | <PlatformAvailability claudeApi bedrock vertexAi azureAiBeta /> |
| [Batch processing](/docs/en/build-with-claude/batch-processing) | Process large volumes of requests asynchronously for cost savings. Send batches with a large number of queries per batch. Batch API calls cost 50% less than standard API calls. | <PlatformAvailability claudeApi bedrock vertexAi /> |
| [Citations](/docs/en/build-with-claude/citations) | Ground Claude's responses in source documents. With Citations, Claude can provide detailed references to the exact sentences and passages it uses to generate responses, leading to more verifiable, trustworthy outputs. | <PlatformAvailability claudeApi bedrock vertexAi azureAiBeta /> |
| [Data residency](/docs/en/build-with-claude/data-residency) | Control where model inference runs using geographic controls. Specify `"global"` or `"us"` routing per request via the `inference_geo` parameter. | <PlatformAvailability claudeApi /> |
| [Effort](/docs/en/build-with-claude/effort) | Control how many tokens Claude uses when responding with the effort parameter, trading off between response thoroughness and token efficiency. Supported on Opus 4.6 and Opus 4.5. | <PlatformAvailability claudeApi bedrock vertexAi azureAiBeta /> |
| [Extended thinking](/docs/en/build-with-claude/extended-thinking) | Enhanced reasoning capabilities for complex tasks, providing transparency into Claude's step-by-step thought process before delivering its final answer. | <PlatformAvailability claudeApi bedrock vertexAi azureAiBeta /> |
| [PDF support](/docs/en/build-with-claude/pdf-support) | Process and analyze text and visual content from PDF documents. | <PlatformAvailability claudeApi bedrock vertexAi azureAiBeta /> |
| [Search results](/docs/en/build-with-claude/search-results) | Enable natural citations for RAG applications by providing search results with proper source attribution. Achieve web search-quality citations for custom knowledge bases and tools. | <PlatformAvailability claudeApi bedrock vertexAi azureAiBeta /> |
| [Structured outputs](/docs/en/build-with-claude/structured-outputs) | Guarantee schema conformance with two approaches: JSON outputs for structured data responses, and strict tool use for validated tool inputs. | <PlatformAvailability claudeApi bedrock azureAiBeta /> |

## Tools

Built-in tools that Claude invokes via `tool_use`. Server-side tools are run by the platform; client-side tools are implemented and executed by you.

### Server-side tools

| Feature | Description | Availability |
|---------|-------------|--------------|
| [Code execution](/docs/en/agents-and-tools/tool-use/code-execution-tool) | Run code in a sandboxed environment for advanced data analysis, calculations, and file processing. Free when used with web search or web fetch. | <PlatformAvailability claudeApi azureAiBeta /> |
| [Memory](/docs/en/agents-and-tools/tool-use/memory-tool) | Enable Claude to store and retrieve information across conversations. Build knowledge bases over time, maintain project context, and learn from past interactions. | <PlatformAvailability claudeApi bedrock vertexAi azureAiBeta /> |
| [Web fetch](/docs/en/agents-and-tools/tool-use/web-fetch-tool) | Retrieve full content from specified web pages and PDF documents for in-depth analysis. | <PlatformAvailability claudeApi azureAiBeta /> |
| [Web search](/docs/en/agents-and-tools/tool-use/web-search-tool) | Augment Claude's comprehensive knowledge with current, real-world data from across the web. | <PlatformAvailability claudeApi vertexAi azureAiBeta /> |

### Client-side tools

| Feature | Description | Availability |
|---------|-------------|--------------|
| [Bash](/docs/en/agents-and-tools/tool-use/bash-tool) | Execute bash commands and scripts to interact with the system shell and perform command-line operations. | <PlatformAvailability claudeApi bedrock vertexAi azureAiBeta /> |
| [Computer use](/docs/en/agents-and-tools/tool-use/computer-use-tool) | Control computer interfaces by taking screenshots and issuing mouse and keyboard commands. | <PlatformAvailability claudeApiBeta bedrockBeta vertexAiBeta azureAiBeta /> |
| [Text editor](/docs/en/agents-and-tools/tool-use/text-editor-tool) | Create and edit text files with a built-in text editor interface for file manipulation tasks. | <PlatformAvailability claudeApi bedrock vertexAi azureAiBeta /> |

## Tool infrastructure

Infrastructure that supports discovering, orchestrating, and scaling tool use.

| Feature | Description | Availability |
|---------|-------------|--------------|
| [Agent Skills](/docs/en/agents-and-tools/agent-skills/overview) | Extend Claude's capabilities with Skills. Use pre-built Skills (PowerPoint, Excel, Word, PDF) or create custom Skills with instructions and scripts. Skills use progressive disclosure to efficiently manage context. | <PlatformAvailability claudeApiBeta azureAiBeta /> |
| [Fine-grained tool streaming](/docs/en/agents-and-tools/tool-use/fine-grained-tool-streaming) | Stream tool use parameters without buffering/JSON validation, reducing latency for receiving large parameters. | <PlatformAvailability claudeApi bedrock vertexAi azureAiBeta /> |
| [MCP connector](/docs/en/agents-and-tools/mcp-connector) | Connect to remote [MCP](/docs/en/mcp) servers directly from the Messages API without a separate MCP client. | <PlatformAvailability claudeApiBeta azureAiBeta /> |
| [Programmatic tool calling](/docs/en/agents-and-tools/tool-use/programmatic-tool-calling) | Enable Claude to call your tools programmatically from within code execution containers, reducing latency and token consumption for multi-tool workflows. | <PlatformAvailability claudeApi azureAiBeta /> |
| [Tool search](/docs/en/agents-and-tools/tool-use/tool-search-tool) | Scale to thousands of tools by dynamically discovering and loading tools on-demand using regex-based search, optimizing context usage and improving tool selection accuracy. | <PlatformAvailability claudeApi bedrock vertexAi azureAiBeta /> |

## Context management

Infrastructure for controlling and optimizing Claude's context window.

| Feature | Description | Availability |
|---------|-------------|--------------|
| [Compaction](/docs/en/build-with-claude/compaction) | Server-side context summarization for long-running conversations. When context approaches the window limit, the API automatically summarizes earlier parts of the conversation. Supported on Opus 4.6 and Haiku 4.5. | <PlatformAvailability claudeApiBeta /> |
| [Context editing](/docs/en/build-with-claude/context-editing) | Automatically manage conversation context with configurable strategies. Supports clearing tool results when approaching token limits and managing thinking blocks in extended thinking conversations. | <PlatformAvailability claudeApiBeta bedrockBeta vertexAiBeta azureAiBeta /> |
| [Automatic prompt caching](/docs/en/build-with-claude/prompt-caching#automatic-caching) | Simplify prompt caching to a single API parameter. The system automatically caches the last cacheable block in your request, moving the cache point forward as conversations grow. | <PlatformAvailability claudeApi azureAiBeta /> |
| [Prompt caching (5m)](/docs/en/build-with-claude/prompt-caching) | Provide Claude with more background knowledge and example outputs to reduce costs and latency. | <PlatformAvailability claudeApi bedrock vertexAi azureAiBeta /> |
| [Prompt caching (1hr)](/docs/en/build-with-claude/prompt-caching#1-hour-cache-duration) | Extended 1-hour cache duration for less frequently accessed but important context, complementing the standard 5-minute cache. | <PlatformAvailability claudeApi azureAiBeta /> |
| [Token counting](/docs/en/api/messages-count-tokens) | Token counting enables you to determine the number of tokens in a message before sending it to Claude, helping you make informed decisions about your prompts and usage. | <PlatformAvailability claudeApi bedrock vertexAi azureAiBeta /> |

## Files and assets

Manage files and assets for use with Claude.

| Feature | Description | Availability |
|---------|-------------|--------------|
| [Files API](/docs/en/build-with-claude/files) | Upload and manage files to use with Claude without re-uploading content with each request. Supports PDFs, images, and text files. | <PlatformAvailability claudeApiBeta azureAiBeta /> |