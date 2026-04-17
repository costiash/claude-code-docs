# Memory tool

---

The memory tool enables Claude to store and retrieve information across conversations through a memory file directory. Claude can create, read, update, and delete files that persist between sessions, allowing it to build knowledge over time without keeping everything in the context window.

This is the key primitive for just-in-time context retrieval: rather than loading all relevant information upfront, agents store what they learn in memory and pull it back on demand. This keeps the active context focused on what's currently relevant, critical for long-running workflows where loading everything at once would overwhelm the context window. See [Effective context engineering](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents) for the broader pattern.

The memory tool operates client-side: you control where and how the data is stored through your own infrastructure.

<Note>
Reach out through the [feedback form](https://forms.gle/YXC2EKGMhjN1c4L88) to share your feedback on this feature.
</Note>

<Note>
This feature is eligible for [Zero Data Retention (ZDR)](/docs/en/build-with-claude/api-and-data-retention). When your organization has a ZDR arrangement, data sent through this feature is not stored after the API response is returned.
</Note>

## Use cases

- Maintain project context across multiple agent executions
- Learn from past interactions, decisions, and feedback
- Build knowledge bases over time
- Enable cross-conversation learning where Claude improves at recurring workflows

## How it works

When enabled, Claude automatically checks its memory directory before starting tasks. Claude can create, read, update, and delete files in the `/memories` directory to store what it learns while working, then reference those memories in future conversations to handle similar tasks more effectively or pick up where it left off.

Since this is a client-side tool, Claude makes tool calls to perform memory operations, and your application executes those operations locally. This gives you complete control over where and how the memory is stored. For security, you should restrict all memory operations to the `/memories` directory.

### Example: How memory tool calls work

When you ask Claude to help with a task, Claude automatically checks its memory directory first. Here's what a typical interaction looks like:

**1. User request:**
```text
"Help me respond to this customer service ticket."
```

**2. Claude checks the memory directory:**
```text
"I'll help you respond to the customer service ticket. Let me check my memory for any previous context."
```

Claude calls the memory tool:
```json
{
  "type": "tool_use",
  "id": "toolu_01C4D5E6F7G8H9I0J1K2L3M4",
  "name": "memory",
  "input": {
    "command": "view",
    "path": "/memories"
  }
}
```

**3. Your application returns the directory contents:**
```json
{
  "type": "tool_result",
  "tool_use_id": "toolu_01C4D5E6F7G8H9I0J1K2L3M4",
  "content": "Here're the files and directories up to 2 levels deep in /memories, excluding hidden items and node_modules:\n4.0K\t/memories\n1.5K\t/memories/customer_service_guidelines.xml\n2.0K\t/memories/refund_policies.xml"
}
```

**4. Claude reads relevant files:**
```json
{
  "type": "tool_use",
  "id": "toolu_01D5E6F7G8H9I0J1K2L3M4N5",
  "name": "memory",
  "input": {
    "command": "view",
    "path": "/memories/customer_service_guidelines.xml"
  }
}
```

**5. Your application returns the file contents:**
```json
{
  "type": "tool_result",
  "tool_use_id": "toolu_01D5E6F7G8H9I0J1K2L3M4N5",
  "content": "Here's the content of /memories/customer_service_guidelines.xml with line numbers:\n     1\t<guidelines>\n     2\t<addressing_customers>\n     3\t- Always address customers by their first name\n     4\t- Use empathetic language\n..."
}
```

**6. Claude uses the memory to help:**
```text
"Based on your customer service guidelines, I can help you craft a response. Please share the ticket details..."
```

For model support, see the [Tool reference](/docs/en/agents-and-tools/tool-use/tool-reference).

## Getting started

To use the memory tool:

1. Add the memory tool to your request
2. Implement client-side handlers for memory operations

<Note>
To handle memory tool operations in your application, you need to implement handlers for each memory command. The SDKs provide memory tool helpers that handle the tool interface. You can subclass `BetaAbstractMemoryTool` (Python) or use `betaMemoryTool` (TypeScript) to implement your own memory backend (file-based, database, cloud storage, encrypted files, etc.).

For working examples, see:
- Python: [examples/memory/basic.py](https://github.com/anthropics/anthropic-sdk-python/blob/main/examples/memory/basic.py)
- TypeScript: [examples/tools-helpers-memory.ts](https://github.com/anthropics/anthropic-sdk-typescript/blob/main/examples/tools-helpers-memory.ts)
</Note>

## Basic usage

<CodeGroup>

```bash cURL
curl https://api.anthropic.com/v1/messages \
    --header "x-api-key: $ANTHROPIC_API_KEY" \
    --header "anthropic-version: 2023-06-01" \
    --header "content-type: application/json" \
    --data '{
        "model": "claude-opus-4-7",
        "max_tokens": 2048,
        "messages": [
            {
                "role": "user",
                "content": "I'\''m working on a Python web scraper that keeps crashing with a timeout error. Here'\''s the problematic function:\n\n```python\ndef fetch_page(url, retries=3):\n    for i in range(retries):\n        try:\n            response = requests.get(url, timeout=5)\n            return response.text\n        except requests.exceptions.Timeout:\n            if i == retries - 1:\n                raise\n            time.sleep(1)\n```\n\nPlease help me debug this."
            }
        ],
        "tools": [{
            "type": "memory_20250818",
            "name": "memory"
        }]
    }'
```

````bash CLI
ant messages create <<'YAML'
model: claude-opus-4-7
max_tokens: 2048
tools:
  - type: memory_20250818
    name: memory
messages:
  - role: user
    content: |
      I'm working on a Python web scraper that keeps crashing with a
      timeout error. Here's the problematic function:

      ```python
      def fetch_page(url, retries=3):
          for i in range(retries):
              try:
                  response = requests.get(url, timeout=5)
                  return response.text
              except requests.exceptions.Timeout:
                  if i == retries - 1:
                      raise
                  time.sleep(1)
      ```

      Please help me debug this.
YAML
````

```python Python hidelines={1..2}
import anthropic

client = anthropic.Anthropic()

message = client.messages.create(
    model="claude-opus-4-7",
    max_tokens=2048,
    messages=[
        {
            "role": "user",
            "content": "I'm working on a Python web scraper that keeps crashing with a timeout error. Here's the problematic function:\n\n```python\ndef fetch_page(url, retries=3):\n    for i in range(retries):\n        try:\n            response = requests.get(url, timeout=5)\n            return response.text\n        except requests.exceptions.Timeout:\n            if i == retries - 1:\n                raise\n            time.sleep(1)\n```\n\nPlease help me debug this.",
        }
    ],
    tools=[{"type": "memory_20250818", "name": "memory"}],
)

print(message)
```

```typescript TypeScript hidelines={1..2}
import Anthropic from "@anthropic-ai/sdk";

const anthropic = new Anthropic({
  apiKey: process.env.ANTHROPIC_API_KEY
});

const message = await anthropic.messages.create({
  model: "claude-opus-4-7",
  max_tokens: 2048,
  messages: [
    {
      role: "user",
      content:
        "I'm working on a Python web scraper that keeps crashing with a timeout error. Here's the problematic function:\n\n```python\ndef fetch_page(url, retries=3):\n    for i in range(retries):\n        try:\n            response = requests.get(url, timeout=5)\n            return response.text\n        except requests.exceptions.Timeout:\n            if i == retries - 1:\n                raise\n            time.sleep(1)\n```\n\nPlease help me debug this."
    }
  ],
  tools: [{ type: "memory_20250818", name: "memory" }]
});

console.log(message);
```

```csharp C#
using System;
using System.Threading.Tasks;
using Anthropic;
using Anthropic.Models.Messages;

public class Program
{
    public static async Task Main(string[] args)
    {
        AnthropicClient client = new()
        {
            ApiKey = Environment.GetEnvironmentVariable("ANTHROPIC_API_KEY")
        };

        var parameters = new MessageCreateParams
        {
            Model = Model.ClaudeOpus4_7,
            MaxTokens = 2048,
            Messages = [
                new()
                {
                    Role = Role.User,
                    Content = "I'm working on a Python web scraper that keeps crashing with a timeout error. Here's the problematic function:\n\n```python\ndef fetch_page(url, retries=3):\n    for i in range(retries):\n        try:\n            response = requests.get(url, timeout=5)\n            return response.text\n        except requests.exceptions.Timeout:\n            if i == retries - 1:\n                raise\n            time.sleep(1)\n```\n\nPlease help me debug this."
                }
            ],
            Tools = [new ToolUnion(new MemoryTool20250818())]
        };

        var message = await client.Messages.Create(parameters);
        Console.WriteLine(message);
    }
}
```

```go Go hidelines={1..11,-1}
package main

import (
	"context"
	"fmt"
	"log"

	"github.com/anthropics/anthropic-sdk-go"
)

func main() {
	client := anthropic.NewClient()

	response, err := client.Beta.Messages.New(context.TODO(), anthropic.BetaMessageNewParams{
		Model:     anthropic.ModelClaudeOpus4_7,
		MaxTokens: 2048,
		Messages: []anthropic.BetaMessageParam{
			anthropic.NewBetaUserMessage(anthropic.NewBetaTextBlock("I'm working on a Python web scraper that keeps crashing with a timeout error. Here's the problematic function:\n\n```python\ndef fetch_page(url, retries=3):\n    for i in range(retries):\n        try:\n            response = requests.get(url, timeout=5)\n            return response.text\n        except requests.exceptions.Timeout:\n            if i == retries - 1:\n                raise\n            time.sleep(1)\n```\n\nPlease help me debug this.")),
		},
		Tools: []anthropic.BetaToolUnionParam{
			{OfMemoryTool20250818: &anthropic.BetaMemoryTool20250818Param{}},
		},
	})
	if err != nil {
		log.Fatal(err)
	}
	fmt.Println(response)
}
```

```java Java hidelines={1..2,4..9,-2..}
import com.anthropic.client.AnthropicClient;
import com.anthropic.client.okhttp.AnthropicOkHttpClient;
import com.anthropic.models.messages.MemoryTool20250818;
import com.anthropic.models.messages.Message;
import com.anthropic.models.messages.MessageCreateParams;
import com.anthropic.models.messages.Model;

public class MemoryToolExample {
    public static void main(String[] args) {
        AnthropicClient client = AnthropicOkHttpClient.fromEnv();

        MessageCreateParams params = MessageCreateParams.builder()
            .model(Model.CLAUDE_OPUS_4_7)
            .maxTokens(2048L)
            .addUserMessage("I'm working on a Python web scraper that keeps crashing with a timeout error. Here's the problematic function:\n\n```python\ndef fetch_page(url, retries=3):\n    for i in range(retries):\n        try:\n            response = requests.get(url, timeout=5)\n            return response.text\n        except requests.exceptions.Timeout:\n            if i == retries - 1:\n                raise\n            time.sleep(1)\n```\n\nPlease help me debug this.")
            .addTool(MemoryTool20250818.builder().build())
            .build();

        Message response = client.messages().create(params);
        System.out.println(response);
    }
}
```

```php PHP hidelines={1..4}
<?php

use Anthropic\Client;

$client = new Client(apiKey: getenv("ANTHROPIC_API_KEY"));

$message = $client->messages->create(
    maxTokens: 2048,
    messages: [
        [
            'role' => 'user',
            'content' => "I'm working on a Python web scraper that keeps crashing with a timeout error. Here's the problematic function:\n\n```python\ndef fetch_page(url, retries=3):\n    for i in range(retries):\n        try:\n            response = requests.get(url, timeout=5)\n            return response.text\n        except requests.exceptions.Timeout:\n            if i == retries - 1:\n                raise\n            time.sleep(1)\n```\n\nPlease help me debug this.",
        ],
    ],
    model: 'claude-opus-4-7',
    tools: [
        [
            'type' => 'memory_20250818',
            'name' => 'memory',
        ],
    ],
);
```

```ruby Ruby hidelines={1..2}
require "anthropic"

client = Anthropic::Client.new

message = client.messages.create(
  model: "claude-opus-4-7",
  max_tokens: 2048,
  messages: [
    {
      role: "user",
      content: "I'm working on a Python web scraper that keeps crashing with a timeout error. Here's the problematic function:\n\n```python\ndef fetch_page(url, retries=3):\n    for i in range(retries):\n        try:\n            response = requests.get(url, timeout=5)\n            return response.text\n        except requests.exceptions.Timeout:\n            if i == retries - 1:\n                raise\n            time.sleep(1)\n```\n\nPlease help me debug this."
    }
  ],
  tools: [
    {
      type: "memory_20250818",
      name: "memory"
    }
  ]
)
puts message
```

</CodeGroup>

## Tool commands

Your client-side implementation needs to handle these memory tool commands. While these specifications describe the recommended behaviors that Claude is most familiar with, you can modify your implementation and return strings as needed for your use case.

### view
Shows directory contents or file contents with optional line ranges:

```json
{
  "command": "view",
  "path": "/memories",
  "view_range": [1, 10] // Optional: view specific lines
}
```

#### Return values

**For directories:** Return a listing that shows files and directories with their sizes:
```text
Here're the files and directories up to 2 levels deep in {path}, excluding hidden items and node_modules:
{size}    {path}
{size}    {path}/{filename1}
{size}    {path}/{filename2}
```

- Lists files up to 2 levels deep
- Shows human-readable sizes (for example, `5.5K`, `1.2M`)
- Excludes hidden items (files starting with `.`) and `node_modules`
- Uses tab character between size and path

**For files:** Return file contents with a header and line numbers:
```text
Here's the content of {path} with line numbers:
{line_numbers}{tab}{content}
```

Line number formatting:
- **Width**: 6 characters, right-aligned with space padding
- **Separator**: Tab character between line number and content
- **Indexing**: 1-indexed (first line is line 1)
- **Line limit**: Files with more than 999,999 lines should return an error: `"File {path} exceeds maximum line limit of 999,999 lines."`

**Example output:**
```text
Here's the content of /memories/notes.txt with line numbers:
     1	Hello World
     2	This is line two
    10	Line ten
   100	Line one hundred
```

#### Error handling

- **File/directory does not exist**: `"The path {path} does not exist. Please provide a valid path."`

### create
Create a new file:

```json
{
  "command": "create",
  "path": "/memories/notes.txt",
  "file_text": "Meeting notes:\n- Discussed project timeline\n- Next steps defined\n"
}
```

#### Return values

- **Success**: `"File created successfully at: {path}"`

#### Error handling

- **File already exists**: `"Error: File {path} already exists"`

### str_replace
Replace text in a file:

```json
{
  "command": "str_replace",
  "path": "/memories/preferences.txt",
  "old_str": "Favorite color: blue",
  "new_str": "Favorite color: green"
}
```

#### Return values

- **Success**: `"The memory file has been edited."` followed by a snippet of the edited file with line numbers

#### Error handling

- **File does not exist**: `"Error: The path {path} does not exist. Please provide a valid path."`
- **Text not found**: ``"No replacement was performed, old_str `{old_str}` did not appear verbatim in {path}."``
- **Duplicate text**: When `old_str` appears multiple times, return: ``"No replacement was performed. Multiple occurrences of old_str `{old_str}` in lines: {line_numbers}. Please ensure it is unique"``

#### Directory handling

If the path is a directory, return a "file does not exist" error.

### insert
Insert text at a specific line:

```json
{
  "command": "insert",
  "path": "/memories/todo.txt",
  "insert_line": 2,
  "insert_text": "- Review memory tool documentation\n"
}
```

#### Return values

- **Success**: `"The file {path} has been edited."`

#### Error handling

- **File does not exist**: `"Error: The path {path} does not exist"`
- **Invalid line number**: ``"Error: Invalid `insert_line` parameter: {insert_line}. It should be within the range of lines of the file: [0, {n_lines}]"``

#### Directory handling

If the path is a directory, return a "file does not exist" error.

### delete
Delete a file or directory:

```json
{
  "command": "delete",
  "path": "/memories/old_file.txt"
}
```

#### Return values

- **Success**: `"Successfully deleted {path}"`

#### Error handling

- **File/directory does not exist**: `"Error: The path {path} does not exist"`

#### Directory handling

Deletes the directory and all its contents recursively.

### rename
Rename or move a file/directory:

```json
{
  "command": "rename",
  "old_path": "/memories/draft.txt",
  "new_path": "/memories/final.txt"
}
```

#### Return values

- **Success**: `"Successfully renamed {old_path} to {new_path}"`

#### Error handling

- **Source does not exist**: `"Error: The path {old_path} does not exist"`
- **Destination already exists**: Return an error (do not overwrite): `"Error: The destination {new_path} already exists"`

#### Directory handling

Renames the directory.

## Prompting guidance

This instruction is automatically included in the system prompt when the memory tool is enabled:

```text
IMPORTANT: ALWAYS VIEW YOUR MEMORY DIRECTORY BEFORE DOING ANYTHING ELSE.
MEMORY PROTOCOL:
1. Use the `view` command of your `memory` tool to check for earlier progress.
2. ... (work on the task) ...
     - As you make progress, record status / progress / thoughts etc in your memory.
ASSUME INTERRUPTION: Your context window might be reset at any moment, so you risk losing any progress that is not recorded in your memory directory.
```

If you observe Claude creating cluttered memory files, you can include this instruction:

> Note: when editing your memory folder, always try to keep its content up-to-date, coherent and organized. You can rename or delete files that are no longer relevant. Do not create new files unless necessary.

You can also guide what Claude writes to memory. For example: "Only write down information relevant to \<topic\> in your memory system."

## Security considerations

Here are important security concerns when implementing your memory store:

### Sensitive information
Claude will usually refuse to write down sensitive information in memory files. However, you may want to implement stricter validation that strips out potentially sensitive information.

### File storage size
Consider tracking memory file sizes and preventing files from growing too large. Consider adding a maximum number of characters the memory read command can return, and let Claude paginate through contents.

### Memory expiration
Consider clearing out memory files periodically that haven't been accessed in an extended time.

### Path traversal protection

<Warning>
Malicious path inputs could attempt to access files outside the `/memories` directory. Your implementation **MUST** validate all paths to prevent directory traversal attacks.
</Warning>

Consider these safeguards:

- Validate that all paths start with `/memories`
- Resolve paths to their canonical form and verify they remain within the memory directory
- Reject paths containing sequences like `../`, `..\\`, or other traversal patterns
- Watch for URL-encoded traversal sequences (`%2e%2e%2f`)
- Use your language's built-in path security utilities (for example, Python's `pathlib.Path.resolve()` and `relative_to()`)

## Error handling

The memory tool uses similar error handling patterns to the [text editor tool](/docs/en/agents-and-tools/tool-use/text-editor-tool#handle-errors). See the individual tool command sections above for detailed error messages and behaviors. Common errors include file not found, permission errors, invalid paths, and duplicate text matches.

## Context editing integration

The memory tool pairs with context editing to manage long-running conversations. For details, see [Context editing](/docs/en/build-with-claude/context-editing).

## Using with Compaction

The memory tool can also be paired with [compaction](/docs/en/build-with-claude/compaction), which provides server-side summarization of older conversation context. While context editing clears specific tool results on the client side, compaction automatically summarizes the entire conversation on the server side when it approaches the context window limit.

For long-running agentic workflows, consider using both: compaction keeps the active context manageable without client-side bookkeeping, and memory persists important information across compaction boundaries so that nothing critical is lost in the summary.

## Multi-session software development pattern

For long-running software projects that span multiple agent sessions, memory files need to be bootstrapped deliberately, not just written ad hoc as work progresses. The pattern below turns memory into a structured recovery mechanism, so each new session can pick up exactly where the last one left off.

### How it works

1. **Initializer session:** The first session sets up the memory artifacts before any substantive work begins. This includes a progress log (tracking what has been done and what comes next), a feature checklist (defining the scope of work), and a reference to any startup or initialization script the project needs.

2. **Subsequent sessions:** Each new session opens by reading those memory artifacts. This recovers the full state of the project in seconds, without needing to re-explore the codebase or retrace earlier decisions.

3. **End-of-session update:** Before a session ends, it updates the progress log with what was completed and what remains. This ensures the next session has an accurate starting point.

### Key principle

Work on one feature at a time. Only mark a feature complete after end-to-end verification confirms it works, not just after the code is written. This keeps the progress log trustworthy and prevents scope creep from compounding across sessions.

<Tip>
For a detailed case study of this pattern in practice, including the initializer script, progress file structure, and git-based recovery, see [Effective harnesses for long-running agents](https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents).
</Tip>

## Next steps

<CardGroup>
  <Card href="/docs/en/agents-and-tools/tool-use/tool-reference" title="See all tools">
    Directory of Anthropic-provided tools and their properties.
  </Card>
  <Card href="/docs/en/build-with-claude/context-editing" title="Context editing">
    Manage conversation length alongside memory.
  </Card>
</CardGroup>