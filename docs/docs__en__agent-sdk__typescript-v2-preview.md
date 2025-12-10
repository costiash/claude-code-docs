# TypeScript SDK V2 interface (preview)

Preview of the simplified V2 TypeScript Agent SDK, with session-based send/receive patterns for multi-turn conversations.

---

<Warning>
The V2 interface is an **unstable preview**. APIs may change based on feedback before becoming stable. Some features like session forking are only available in the [V1 SDK](/docs/en/agent-sdk/typescript).
</Warning>

The V2 Claude Agent TypeScript SDK removes the need for async generators and yield coordination. This makes multi-turn conversations simpler—instead of managing generator state across turns, each turn is a separate `send()`/`receive()` cycle. The API surface reduces to three concepts:

- `createSession()` / `resumeSession()`: Start or continue a conversation
- `session.send()`: Send a message
- `session.receive()`: Get the response

## Installation

The V2 interface is included in the existing SDK package:

```bash
npm install @anthropic-ai/claude-agent-sdk
```

## Quick start

### One-shot prompt

For simple single-turn queries where you don't need to maintain a session, use `unstable_v2_prompt()`. This example sends a math question and logs the answer:

```typescript
import { unstable_v2_prompt } from '@anthropic-ai/claude-agent-sdk'

const result = await unstable_v2_prompt('What is 2 + 2?', {
  model: 'claude-sonnet-4-5-20250929'
})
console.log(result.result)
```

<details>
<summary>See the same operation in V1</summary>

```typescript
import { query } from '@anthropic-ai/claude-agent-sdk'

const q = query({
  prompt: 'What is 2 + 2?',
  options: { model: 'claude-sonnet-4-5-20250929' }
})

for await (const msg of q) {
  if (msg.type === 'result') {
    console.log(msg.result)
  }
}
```

</details>

### Basic session

For interactions beyond a single prompt, create a session. V2 separates sending and receiving into distinct steps:
- `send()` dispatches your message
- `receive()` streams back the response

This explicit separation makes it easier to add logic between turns (like processing responses before sending follow-ups).

The example below creates a session, sends "Hello!" to Claude, and prints the text response. It uses [`await using`](https://www.typescriptlang.org/docs/handbook/release-notes/typescript-5-2.html#using-declarations-and-explicit-resource-management) (TypeScript 5.2+) to automatically close the session when the block exits. You can also call `session.close()` manually.

```typescript
import { unstable_v2_createSession } from '@anthropic-ai/claude-agent-sdk'

await using session = unstable_v2_createSession({
  model: 'claude-sonnet-4-5-20250929'
})

await session.send('Hello!')
for await (const msg of session.receive()) {
  if (msg.type === 'assistant') {
    const text = msg.message.content
      .filter(block => block.type === 'text')
      .map(block => block.text)
      .join('')
    console.log(text)
  }
}
```

<details>
<summary>See the same operation in V1</summary>

In V1, both input and output flow through a single async generator. For a basic prompt this looks similar, but adding multi-turn logic requires restructuring to use an input generator.

```typescript
import { query } from '@anthropic-ai/claude-agent-sdk'

const q = query({
  prompt: 'Hello!',
  options: { model: 'claude-sonnet-4-5-20250929' }
})

for await (const msg of q) {
  if (msg.type === 'assistant') {
    const text = msg.message.content
      .filter(block => block.type === 'text')
      .map(block => block.text)
      .join('')
    console.log(text)
  }
}
```

</details>

### Multi-turn conversation

Sessions persist context across multiple exchanges. To continue a conversation, call `send()` again on the same session. Claude remembers the previous turns.

This example asks a math question, then asks a follow-up that references the previous answer:

```typescript
import { unstable_v2_createSession } from '@anthropic-ai/claude-agent-sdk'

await using session = unstable_v2_createSession({
  model: 'claude-sonnet-4-5-20250929'
})

// Turn 1
await session.send('What is 5 + 3?')
for await (const msg of session.receive()) {
  console.log(msg)
}

// Turn 2
await session.send('Multiply that by 2')
for await (const msg of session.receive()) {
  console.log(msg)
}
```

<details>
<summary>See the same operation in V1</summary>

```typescript
import { query } from '@anthropic-ai/claude-agent-sdk'

// Must create an async iterable to feed messages
async function* createInputStream() {
  yield {
    type: 'user',
    session_id: '',
    message: { role: 'user', content: [{ type: 'text', text: 'What is 5 + 3?' }] },
    parent_tool_use_id: null
  }
  // Must coordinate when to yield next message
  yield {
    type: 'user',
    session_id: '',
    message: { role: 'user', content: [{ type: 'text', text: 'Multiply by 2' }] },
    parent_tool_use_id: null
  }
}

const q = query({
  prompt: createInputStream(),
  options: { model: 'claude-sonnet-4-5-20250929' }
})

for await (const msg of q) {
  console.log(msg)
}
```

</details>

### Session resume

If you have a session ID from a previous interaction, you can resume it later. This is useful for long-running workflows or when you need to persist conversations across application restarts.

This example reconnects to an existing session and continues the conversation:

```typescript
import { unstable_v2_resumeSession } from '@anthropic-ai/claude-agent-sdk'

await using session = unstable_v2_resumeSession(sessionId, {
  model: 'claude-sonnet-4-5-20250929'
})

await session.send('Continue from where we left off')
for await (const msg of session.receive()) {
  // Process response
}
```

<details>
<summary>See the same operation in V1</summary>

```typescript
import { query } from '@anthropic-ai/claude-agent-sdk'

const q = query({
  prompt: 'Continue from where we left off',
  options: {
    model: 'claude-sonnet-4-5-20250929',
    resume: sessionId
  }
})

for await (const msg of q) {
  // Process response
}
```

</details>

### Cleanup

Sessions can be closed manually or automatically using [`await using`](https://www.typescriptlang.org/docs/handbook/release-notes/typescript-5-2.html#using-declarations-and-explicit-resource-management), a TypeScript 5.2+ feature for automatic resource cleanup. If you're using an older TypeScript version or encounter compatibility issues, use manual cleanup instead.

```typescript
// Automatic cleanup with await using (TypeScript 5.2+)
await using session = unstable_v2_createSession({
  model: 'claude-sonnet-4-5-20250929'
})
// Session closes automatically when the block exits

// Manual cleanup (works with any TypeScript version)
const session = unstable_v2_createSession({
  model: 'claude-sonnet-4-5-20250929'
})
// ...
session.close()
```

## API reference

### `unstable_v2_createSession()`

Creates a new session for multi-turn conversations.

```typescript
function unstable_v2_createSession(options: {
  model: string;
  // Additional options supported
}): Session
```

### `unstable_v2_resumeSession()`

Resumes an existing session by ID.

```typescript
function unstable_v2_resumeSession(
  sessionId: string,
  options: {
    model: string;
    // Additional options supported
  }
): Session
```

### `unstable_v2_prompt()`

One-shot convenience function for single-turn queries.

```typescript
function unstable_v2_prompt(
  prompt: string,
  options: {
    model: string;
    // Additional options supported
  }
): Promise<Result>
```

### Session interface

```typescript
interface Session {
  send(message: string): Promise<void>;
  receive(): AsyncGenerator<SDKMessage>;
  close(): void;
}
```

## Feature availability

Not all V1 features are available in V2 yet. The following require using the [V1 SDK](/docs/en/agent-sdk/typescript):

- Session forking (`forkSession` option)
- Some advanced streaming input patterns

## Feedback

Share your feedback on the V2 interface before it becomes stable. Report issues and suggestions through [GitHub Issues](https://github.com/anthropics/claude-code/issues).

## See also

- [TypeScript SDK reference (V1)](/docs/en/agent-sdk/typescript) - Full V1 SDK documentation
- [SDK overview](/docs/en/agent-sdk/overview) - General SDK concepts
- [V2 examples on GitHub](https://github.com/anthropics/claude-agent-sdk-demos/tree/main/hello-world-v2) - Working code examples