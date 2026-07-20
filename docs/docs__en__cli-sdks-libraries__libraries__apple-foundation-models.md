# Apple Foundation Models

Use Claude on Apple platforms through the Foundation Models framework with the Claude for Foundation Models Swift package.

---

[Claude for Foundation Models](https://github.com/anthropics/ClaudeForFoundationModels) is a Swift package that makes Claude available as a server-side language model in Apple's [Foundation Models](https://developer.apple.com/documentation/foundationmodels) framework. The package conforms Claude to the framework's `LanguageModel` protocol, so you drive it with the same `LanguageModelSession` API you use for Apple's on-device model: `respond(to:)`, streaming, guided generation, and tool calling all work the same way.

Requests go directly from your app to the Claude API; Apple is not in the request path and does not see prompts or responses. Usage is billed to your Anthropic account at [standard API pricing](/docs/en/about-claude/pricing). Your app decides when to use Claude and when to use Apple's on-device model: pass whichever model you want to each session.

<Note>
  **Beta.** This package targets the Foundation Models server-side language model API introduced in the OS 27 betas. APIs might change before general availability.
</Note>

<Info>
  Claude for Foundation Models is **not** a general-purpose Messages API client. Its public surface is the Foundation Models provider conformance plus the configuration types that reach it (`ClaudeLanguageModel`, `ClaudeModel`, `AuthMode`, `ClaudeServerTool`). For direct access to the Messages API in another language, see the [Client SDKs](/docs/en/cli-sdks-libraries/overview#client-sdks).
</Info>

## Requirements

* iOS 27, macOS 27, visionOS 27, or watchOS 27 (all in beta): the OS releases whose Foundation Models framework supports server-side language models
* Xcode 27 (beta)
* A Claude API key from the [Claude Console](https://platform.claude.com/) for development. See [Authentication](#authentication) for production options.

## Install the package

Add the package to your `Package.swift`:

```swift
dependencies: [
  .package(url: "https://github.com/anthropics/ClaudeForFoundationModels.git", from: "0.1.0")
]
```

Or in Xcode: **File** > **Add Package Dependencies…** and enter the repository URL.

Then add `ClaudeForFoundationModels` to your target's dependencies and import it alongside `FoundationModels`:

```swift
import FoundationModels
import ClaudeForFoundationModels
```

## Quick start

`ClaudeLanguageModel` is the entry point. Pass it to `LanguageModelSession` and use the session exactly as you would with any Foundation Models provider:

```swift
import FoundationModels
import ClaudeForFoundationModels

let model = ClaudeLanguageModel(
  name: .sonnet4_6,
  auth: .apiKey(ProcessInfo.processInfo.environment["ANTHROPIC_API_KEY"] ?? "")
)

let session = LanguageModelSession(model: model)
let response = try await session.respond(to: "Plan a 4-day trip to Buenos Aires.")
print(response.content)
```

The initializer also accepts `baseURL` (default `https://api.anthropic.com`), `timeout`, and `serverTools` (see [Server-side tools](#server-side-tools)).

For a complete working program, the repository includes [`Examples/ClaudeExample`](https://github.com/anthropics/ClaudeForFoundationModels/tree/main/Examples/ClaudeExample), a runnable command-line target that streams a chat turn to the terminal, with a `--search` flag that enables server-side web search for the turn. Running it requires a macOS 27 host.

## Choosing a model

Model identifiers are values of `ClaudeModel`. Use a compiled-in constant, or construct one with explicit capabilities for an ID that isn't compiled in yet (see [Capabilities](#capabilities)):

```swift
ClaudeLanguageModel(name: .opus4_8, auth: auth)
```

Constants mirror API model IDs (`.opus4_8` is `claude-opus-4-8`) and carry each model's capabilities. New models ship as new constants in package releases; check `ClaudeModel` in Xcode for the current list, and the [Models overview](/docs/en/about-claude/models/overview) to compare models.

### Capabilities

Each `ClaudeModel` declares what it accepts: sampling parameters, effort levels, adaptive thinking, structured output, and image input. The package uses this to determine which request fields to send, because sending a field a model rejects is a hard error. The constants carry the right capabilities. For an ID that isn't compiled in, declare what the model accepts (there is deliberately no shorthand that guesses):

```swift
let model = ClaudeModel(
  id: "claude-experimental-x",
  capabilities: .init(samplingParams: false, effortLevels: [.low, .high])
)
ClaudeLanguageModel(name: model, auth: auth)
```

### Effort

Pin a Claude [effort level](/docs/en/build-with-claude/effort) for every request with `fixedEffort:`. It takes precedence over the framework's per-request reasoning hints, and it's the only way to request `.xhigh` or `.max`, because the framework's reasoning levels stop at high. The API defaults to `high` when no effort is sent:

```swift
ClaudeLanguageModel(name: .opus4_8, auth: auth, fixedEffort: .xhigh)
```

The level must be one the model accepts. Each `ClaudeModel` declares which of the five levels (`low`, `medium`, `high`, `xhigh`, `max`) its model takes, if any: some models don't accept effort at all.

### When to use Claude versus the on-device model

Apple's on-device model is fast, private, and available offline, but it is sized for lightweight tasks. Escalate to Claude when you need larger context, frontier reasoning, or server-side tools such as web search and code execution. Because both use the same `LanguageModelSession` API, you can switch by swapping the `model:` argument.

## Authentication

Set the credential with the `auth:` parameter.

### API key (development)

Pass an API key directly while developing:

```swift
ClaudeLanguageModel(name: .sonnet4_6, auth: .apiKey("YOUR_API_KEY"))
```

<Warning>
  A key bundled into an app is extractable from the shipping binary, and anyone who extracts it can make requests billed to your account. Use `.apiKey` for development only, and switch to a proxy before release.
</Warning>

### Proxy (production)

For production, route requests through your own back end with `.proxied`. The relay at `baseURL` adds the Claude API credential server-side, so the app ships no key. The `headers` you provide are sent on every request so your proxy can authorize the caller. Pass `[:]` if it needs none:

```swift
ClaudeLanguageModel(
  name: .sonnet4_6,
  auth: .proxied(headers: ["X-App-Token": "..."]),
  baseURL: URL(string: "https://api.yourapp.com/claude")!
)
```

Your proxy receives standard [Messages API](/docs/en/api/messages/create) requests, attaches the `x-api-key` header, and forwards them to `https://api.anthropic.com`.

## Streaming

`streamResponse(to:)` returns the response incrementally. Each element is a cumulative snapshot of the response so far, not a delta:

```swift
let stream = session.streamResponse(to: "Summarize today's top science stories.")
for try await partial in stream {
  print(partial.content)
}
```

## Structured output

Annotate a type with `@Generable` and request it with `generating:`. The model returns a value of that type through [structured outputs](/docs/en/build-with-claude/structured-outputs):

```swift
@Generable
struct Trip {
  @Guide(description: "Destination city") var destination: String
  @Guide(description: "Length in days") var days: Int
}

let response = try await session.respond(to: "Plan a trip to Tokyo.", generating: Trip.self)
print(response.content.destination)
```

Structured output requires a model whose capabilities include it (all compiled-in constants do). If the chosen model does not, the package throws `LanguageModelError.unsupportedGenerationGuide` rather than silently degrading.

## Tool use

### Client-side tools

The framework's `tools:` array works unchanged. Conform your types to `Tool`, pass them to `LanguageModelSession`, and the framework invokes them on the device when Claude calls them. See [Tool use with Claude](/docs/en/agents-and-tools/tool-use/overview).

```swift
let session = LanguageModelSession(model: model, tools: [FindRestaurantsTool()])
```

### Server-side tools

[Server tools](/docs/en/agents-and-tools/tool-use/server-tools) (web search, web fetch, and code execution) run on Anthropic's infrastructure within a single round trip, with nothing for the framework to invoke on the device. Configure them for each model with `serverTools:`:

```swift
let model = ClaudeLanguageModel(
  name: .sonnet4_6,
  auth: auth,
  serverTools: [
    .webSearch(maxUses: 5),
    .codeExecution,
  ]
)
```

`.webSearch` and `.webFetch` accept optional `allowedDomains`, `blockedDomains`, and `maxUses`. Server tool activity surfaces in the transcript as `ClaudeServerToolSegment` custom segments.

<Note>
  `serverTools` is configured on `ClaudeLanguageModel` rather than on `LanguageModelSession` because the session type is Apple's. To use different server-tool sets for each conversation, construct multiple `ClaudeLanguageModel` instances.
</Note>

## Images

Models whose capabilities include image input declare the framework's vision capability. Pass image content through the framework's standard session API; the package converts it to the Claude API's image format. See [Vision](/docs/en/build-with-claude/vision) for image requirements.

## Error handling

The package maps Claude API errors onto Apple's `LanguageModelError` cases where one fits: context-window overflow surfaces as `.contextSizeExceeded`, HTTP 429 as `.rateLimited`, a request past the configured timeout as `.timeout`. Provider errors with no framework equivalent surface as `ClaudeError`. Pattern-match to drive product flows:

```swift
do {
  let response = try await session.respond(to: prompt)
  print(response.content)
} catch ClaudeError.missingCredential {
  // Prompt for an API key.
} catch let error as LanguageModelError {
  // Framework-shaped errors (rate limits, guardrails, context length, decoding).
} catch {
  // Transport errors.
}
```

A common pattern is to catch `.rateLimited` and fall back to `SystemLanguageModel` for that turn, queue the request, or surface a retry affordance.

## Feature support

The package surfaces the Messages API capabilities that the Foundation Models provider protocol can express. Features with no representation in Apple's protocol are not available through it, including:

* Prompt caching controls (the package applies prompt caching automatically; cache TTL and breakpoint placement are not configurable)
* Stop sequences
* Batch processing
* Files API
* Token counting
* Beta headers

## Additional resources

| Reference                                                                                           | Covers                                                                                            |
| --------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------- |
| [Apple Foundation Models documentation](https://developer.apple.com/documentation/foundationmodels) | `LanguageModelSession`, `@Generable`, `Transcript`, `Tool`, and the rest of the framework surface |
| [`ClaudeForFoundationModels` on GitHub](https://github.com/anthropics/ClaudeForFoundationModels)    | Source, the runnable example, and the issue tracker                                               |
| [Claude API reference](/docs/en/api/overview)                                                       | The underlying Messages API                                                                       |

The package is licensed under Apache 2.0. Bug reports are welcome through GitHub issues. External pull requests are not being accepted during the beta period.
