# Memory tool

Let Claude store and retrieve information across conversations by implementing the memory tool's file operations in your application.

---

The memory tool lets Claude store and retrieve information across conversations in a directory of memory files. Claude can create, read, update, and delete files that persist between sessions, building up knowledge over time without keeping everything in the context window.

Memory supports just-in-time context retrieval. Rather than loading all relevant information up front, an agent records what it learns in memory files and reads them back on demand. This keeps the active context focused on the current task, which matters for long-running sessions that would otherwise overwhelm the context window. See [Effective context engineering](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents) for the broader pattern.

The memory tool operates client-side: Claude requests file operations, and your application executes them. You control where and how the data is stored through your own infrastructure.

<Note>
  Reach out through the [feedback form](https://forms.gle/YXC2EKGMhjN1c4L88) to share your feedback on this feature.
</Note>

<Note>
  For how zero data retention (ZDR) applies to this feature, see [API and data retention](/docs/en/manage-claude/api-and-data-retention).
</Note>

## Use cases

* Maintain project context across multiple agent sessions
* Apply lessons from past interactions, decisions, and feedback to new tasks
* Build up a knowledge base over time

## How it works

When the memory tool is enabled, Claude automatically checks its memory directory before starting a task. As it works, Claude stores what it learns in files under `/memories` and reads them back in later conversations to continue earlier work.

Because the memory tool is client-side, Claude only requests memory operations. Your application executes each request against storage you control and returns the result in a `tool_result` block (see [Handle tool calls](/docs/en/agents-and-tools/tool-use/handle-tool-calls)). The `/memories` path is a prefix that your handler maps onto real storage, such as a per-user directory or keys in a database. Memory lives entirely in your application. A later conversation continues from the same memory when it sends the same `tools` entry and your handler serves the same store. For security, restrict all memory operations to the `/memories` directory (see [Path traversal protection](#path-traversal-protection)).

### Example: How memory tool calls work

A typical interaction looks like this:

**1. User request:**

```text wrap
"Help me respond to this customer service ticket."
```

**2. Claude checks the memory directory:**

```text wrap
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

```text wrap
"Based on your customer service guidelines, I can help you craft a response. Please share the ticket details..."
```

The memory tool is available on all Claude 4 and later models. For the full list of Anthropic-provided tools, see the [Tool reference](/docs/en/agents-and-tools/tool-use/tool-reference).

## Getting started

The memory tool is generally available on the Messages API: no beta header is required. Using it takes two steps:

1. Add the memory tool to your request. The `tools` entry `{"type": "memory_20250818", "name": "memory"}` is the entire configuration: the `name` must be `memory`, and you don't define an input schema for an Anthropic-provided tool.
2. Implement a client-side handler for each memory command. Your handler must reject paths outside `/memories`, so read [Path traversal protection](#path-traversal-protection) before you write it.

## Basic usage

<CodeGroup>
  ```bash cURL
  curl https://api.anthropic.com/v1/messages \
    -H "x-api-key: $ANTHROPIC_API_KEY" \
    -H "anthropic-version: 2023-06-01" \
    -H "content-type: application/json" \
    -d '{
      "model": "claude-opus-4-8",
      "max_tokens": 2048,
      "messages": [
        {
          "role": "user",
          "content": "Help me respond to this customer service ticket."
        }
      ],
      "tools": [{
        "type": "memory_20250818",
        "name": "memory"
      }]
    }'
  ```

  ```bash CLI
  ant messages create <<'YAML'
  model: claude-opus-4-8
  max_tokens: 2048
  tools:
    - type: memory_20250818
      name: memory
  messages:
    - role: user
      content: Help me respond to this customer service ticket.
  YAML
  ```

  ```python Python
  client = anthropic.Anthropic()

  message = client.messages.create(
      model="claude-opus-4-8",
      max_tokens=2048,
      messages=[
          {
              "role": "user",
              "content": "Help me respond to this customer service ticket.",
          }
      ],
      tools=[{"type": "memory_20250818", "name": "memory"}],
  )

  print(message)
  ```

  ```typescript TypeScript
  const anthropic = new Anthropic();

  const message = await anthropic.messages.create({
    model: "claude-opus-4-8",
    max_tokens: 2048,
    messages: [
      {
        role: "user",
        content: "Help me respond to this customer service ticket."
      }
    ],
    tools: [{ type: "memory_20250818", name: "memory" }]
  });

  console.log(message);
  ```

  ```csharp C#
  var client = new AnthropicClient();

  var message = await client.Messages.Create(
      new()
      {
          Model = Model.ClaudeOpus4_8,
          MaxTokens = 2048,
          Messages =
          [
              new()
              {
                  Role = Role.User,
                  Content = "Help me respond to this customer service ticket.",
              },
          ],
          Tools = [new MemoryTool20250818()],
      }
  );

  Console.WriteLine(message);
  ```

  ```go Go
  client := anthropic.NewClient()

  message, err := client.Messages.New(context.TODO(), anthropic.MessageNewParams{
  	Model:     anthropic.ModelClaudeOpus4_8,
  	MaxTokens: 2048,
  	Messages: []anthropic.MessageParam{
  		anthropic.NewUserMessage(anthropic.NewTextBlock("Help me respond to this customer service ticket.")),
  	},
  	Tools: []anthropic.ToolUnionParam{
  		{OfMemoryTool20250818: &anthropic.MemoryTool20250818Param{}},
  	},
  })
  if err != nil {
  	log.Fatal(err)
  }
  fmt.Println(message)
  ```

  ```java Java
  import com.anthropic.models.messages.MemoryTool20250818;
  // ...
    AnthropicClient client = AnthropicOkHttpClient.fromEnv();

    MessageCreateParams params = MessageCreateParams.builder()
      .model(Model.CLAUDE_OPUS_4_8)
      .maxTokens(2048L)
      .addTool(MemoryTool20250818.builder().build())
      .addUserMessage("Help me respond to this customer service ticket.")
      .build();

    Message message = client.messages().create(params);
    IO.println(message);
  ```

  ```php PHP
  $client = new Client();

  $message = $client->messages->create(
      model: Model::CLAUDE_OPUS_4_8,
      maxTokens: 2048,
      messages: [
          [
              'role' => 'user',
              'content' => 'Help me respond to this customer service ticket.',
          ],
      ],
      tools: [new MemoryTool20250818],
  );

  echo $message;
  ```

  ```ruby Ruby
  client = Anthropic::Client.new

  message = client.messages.create(
    model: Anthropic::Model::CLAUDE_OPUS_4_8,
    max_tokens: 2048,
    messages: [
      {
        role: "user",
        content: "Help me respond to this customer service ticket."
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

## Implement the memory handler

Claude's reply to a request like the previous one ends with a `tool_use` block that requests a memory operation, such as `view /memories`. Your application executes the operation and returns the result in a `tool_result` block, then sends the conversation back so Claude can continue: the standard [tool-use loop](/docs/en/agents-and-tools/tool-use/handle-tool-calls).

Four SDKs provide memory tool helpers that handle the tool interface and the loop. Subclass `BetaAbstractMemoryTool` (Python and C#), use `betaMemoryTool` (TypeScript), or implement `BetaMemoryToolHandler` (Java) to back memory with your own storage, such as files on disk, a database, cloud storage, or encrypted files. Python and TypeScript also ship a ready-made local-filesystem implementation, `BetaLocalFilesystemMemoryTool`. The helper and tool-runner surfaces live in each SDK's beta namespace even though the memory tool itself is generally available. The Go and Ruby SDKs have no memory helper, so those examples run the tool-use loop themselves, and PHP wraps your handler closure in its generic `BetaRunnableTool`. All three use an in-memory store that you replace with your own storage.

<CodeGroup exclude="shell">
  ```python Python
  import anthropic
  from anthropic.tools import BetaLocalFilesystemMemoryTool

  client = anthropic.Anthropic()
  memory = BetaLocalFilesystemMemoryTool(base_path="./memory")

  runner = client.beta.messages.tool_runner(
      model="claude-opus-4-8",
      max_tokens=1024,
      messages=[
          {
              "role": "user",
              "content": "Remember that customer Acme Corp prefers email follow-ups.",
          }
      ],
      tools=[memory],
  )

  final_message = runner.until_done()
  print(final_message.content)
  ```

  ```typescript TypeScript
  import Anthropic from "@anthropic-ai/sdk";
  import { betaMemoryTool } from "@anthropic-ai/sdk/helpers/beta/memory";
  import { BetaLocalFilesystemMemoryTool } from "@anthropic-ai/sdk/tools/memory/node";

  const client = new Anthropic();

  const backend = await BetaLocalFilesystemMemoryTool.init("./memory");
  const memory = betaMemoryTool(backend); // or pass your own handlers object

  const runner = client.beta.messages.toolRunner({
    model: "claude-opus-4-8",
    max_tokens: 1024,
    messages: [
      {
        role: "user",
        content: "Remember that customer Acme Corp prefers email follow-ups."
      }
    ],
    tools: [memory],
    max_iterations: 10
  });

  const finalMessage = await runner;
  console.log(finalMessage.content);
  ```

  ```csharp C#
  using Anthropic;
  using Anthropic.Helpers.Beta;
  using Anthropic.Models.Beta.Messages;

  var client = new AnthropicClient();

  // Your subclass of BetaAbstractMemoryTool
  var memory = new FilesystemMemoryTool("./memories");

  var runner = client.Beta.Messages.ToolRunner(
      new MessageCreateParams
      {
          Model = Anthropic.Models.Messages.Model.ClaudeOpus4_8,
          MaxTokens = 1024,
          Messages =
          [
              new()
              {
                  Role = Role.User,
                  Content = "Remember that customer Acme Corp prefers email follow-ups.",
              },
          ],
      },
      [memory],
      maxIterations: 10
  );

  var finalMessage = await runner.RunUntilDoneAsync();
  Console.WriteLine(finalMessage);
  ```

  ```go Go
  package main

  import (
  	"context"
  	"encoding/json"
  	"fmt"
  	"log"
  	"slices"
  	"sort"
  	"strings"

  	"github.com/anthropics/anthropic-sdk-go"
  )

  // An in-memory store that maps memory file paths to their contents.
  // Use your own storage in production.
  var store = map[string]string{}

  type memoryCommand struct {
  	Command    string `json:"command"`
  	Path       string `json:"path"`
  	FileText   string `json:"file_text"`
  	OldStr     string `json:"old_str"`
  	NewStr     string `json:"new_str"`
  	InsertLine int    `json:"insert_line"`
  	InsertText string `json:"insert_text"`
  	OldPath    string `json:"old_path"`
  	NewPath    string `json:"new_path"`
  }

  func executeMemory(raw json.RawMessage) string {
  	var cmd memoryCommand
  	if err := json.Unmarshal(raw, &cmd); err != nil {
  		return "Error: invalid memory command"
  	}
  	switch cmd.Command {
  	case "view":
  		if content, ok := store[cmd.Path]; ok {
  			lines := strings.Split(strings.TrimSuffix(content, "\n"), "\n")
  			for i, line := range lines {
  				lines[i] = fmt.Sprintf("%6d\t%s", i+1, line)
  			}
  			return fmt.Sprintf("Here's the content of %s with line numbers:\n%s", cmd.Path, strings.Join(lines, "\n"))
  		}
  		if cmd.Path == "/memories" {
  			listing := []string{"1.0K\t/memories"}
  			for path := range store {
  				listing = append(listing, "1.0K\t"+path)
  			}
  			sort.Strings(listing[1:])
  			return fmt.Sprintf("Here're the files and directories up to 2 levels deep in %s, excluding hidden items and node_modules:\n%s", cmd.Path, strings.Join(listing, "\n"))
  		}
  		return fmt.Sprintf("The path %s does not exist. Please provide a valid path.", cmd.Path)
  	case "create":
  		store[cmd.Path] = cmd.FileText
  		return "File created successfully at: " + cmd.Path
  	case "str_replace":
  		content, ok := store[cmd.Path]
  		if !ok || !strings.Contains(content, cmd.OldStr) {
  			return fmt.Sprintf("No replacement was performed, old_str `%s` did not appear verbatim in %s.", cmd.OldStr, cmd.Path)
  		}
  		store[cmd.Path] = strings.Replace(content, cmd.OldStr, cmd.NewStr, 1)
  		return "The memory file has been edited."
  	case "insert":
  		content, ok := store[cmd.Path]
  		if !ok {
  			return fmt.Sprintf("Error: The path %s does not exist", cmd.Path)
  		}
  		lines := strings.Split(content, "\n")
  		if cmd.InsertLine < 0 || cmd.InsertLine > len(lines) {
  			return fmt.Sprintf("Error: Invalid `insert_line` parameter: %d. It should be within the range of lines of the file: [0, %d]", cmd.InsertLine, len(lines))
  		}
  		lines = slices.Insert(lines, cmd.InsertLine, strings.TrimSuffix(cmd.InsertText, "\n"))
  		store[cmd.Path] = strings.Join(lines, "\n")
  		return fmt.Sprintf("The file %s has been edited.", cmd.Path)
  	case "delete":
  		if _, ok := store[cmd.Path]; !ok {
  			return fmt.Sprintf("Error: The path %s does not exist", cmd.Path)
  		}
  		delete(store, cmd.Path)
  		return "Successfully deleted " + cmd.Path
  	case "rename":
  		if _, ok := store[cmd.OldPath]; !ok {
  			return fmt.Sprintf("Error: The path %s does not exist", cmd.OldPath)
  		}
  		if _, ok := store[cmd.NewPath]; ok {
  			return fmt.Sprintf("Error: The destination %s already exists", cmd.NewPath)
  		}
  		store[cmd.NewPath] = store[cmd.OldPath]
  		delete(store, cmd.OldPath)
  		return fmt.Sprintf("Successfully renamed %s to %s", cmd.OldPath, cmd.NewPath)
  	default:
  		return "Error: unknown command " + cmd.Command
  	}
  }

  func main() {
  	client := anthropic.NewClient()
  	tools := []anthropic.ToolUnionParam{{OfMemoryTool20250818: &anthropic.MemoryTool20250818Param{}}}
  	messages := []anthropic.MessageParam{
  		anthropic.NewUserMessage(anthropic.NewTextBlock("Remember that customer Acme Corp prefers email follow-ups.")),
  	}

  	for {
  		message, err := client.Messages.New(context.TODO(), anthropic.MessageNewParams{
  			Model:     anthropic.ModelClaudeOpus4_8,
  			MaxTokens: 1024,
  			Messages:  messages,
  			Tools:     tools,
  		})
  		if err != nil {
  			log.Fatal(err)
  		}
  		if message.StopReason != anthropic.StopReasonToolUse {
  			for _, block := range message.Content {
  				if block.Type == "text" {
  					fmt.Println(block.Text)
  				}
  			}
  			break
  		}
  		results := []anthropic.ContentBlockParamUnion{}
  		for _, block := range message.Content {
  			if block.Type == "tool_use" {
  				results = append(results, anthropic.NewToolResultBlock(block.ID, executeMemory(block.Input), false))
  			}
  		}
  		messages = append(messages, message.ToParam(), anthropic.NewUserMessage(results...))
  	}
  }
  ```

  ```java Java
  import com.anthropic.client.AnthropicClient;
  import com.anthropic.client.okhttp.AnthropicOkHttpClient;
  import com.anthropic.helpers.BetaMemoryToolHandler;
  import com.anthropic.helpers.BetaToolRunner;
  import com.anthropic.models.beta.messages.BetaMemoryTool20250818;
  import com.anthropic.models.beta.messages.BetaMessage;
  import com.anthropic.models.beta.messages.MessageCreateParams; // beta package, not models.messages
  import com.anthropic.models.beta.messages.ToolRunnerCreateParams;
  import com.anthropic.models.messages.Model;
  import java.nio.file.Path;

  void main() {
    AnthropicClient client = AnthropicOkHttpClient.fromEnv();

    // Your BetaMemoryToolHandler implementation of the six memory commands
    BetaMemoryToolHandler handler = new FileSystemMemoryToolHandler(Path.of("memories"));

    MessageCreateParams createParams = MessageCreateParams.builder()
      .model(Model.CLAUDE_OPUS_4_8)
      .maxTokens(1024L)
      .addTool(BetaMemoryTool20250818.builder().build())
      .addUserMessage("Remember that customer Acme Corp prefers email follow-ups.")
      .build();

    ToolRunnerCreateParams runnerParams = ToolRunnerCreateParams.builder()
      .betaMemoryToolHandler(handler)
      .initialMessageParams(createParams)
      .maxIterations(10)
      .build();

    BetaToolRunner runner = client.beta().messages().toolRunner(runnerParams);
    for (BetaMessage message : runner) {
      IO.println(message);
    }
  }
  ```

  ```php PHP
  <?php

  use Anthropic\Beta\Messages\BetaMemoryTool20250818;
  use Anthropic\Client;
  use Anthropic\Lib\Tools\BetaRunnableTool;
  use Anthropic\Messages\Model;

  $client = new Client();

  // An in-memory store that maps memory file paths to their contents.
  // Use your own storage in production.
  $store = [];

  $memory = new BetaRunnableTool(
      definition: new BetaMemoryTool20250818,
      run: function (array $input) use (&$store): string {
          $path = $input['path'] ?? '';
          switch ($input['command']) {
              case 'view':
                  if (isset($store[$path])) {
                      $numbered = [];
                      foreach (explode("\n", preg_replace('/\n\z/', '', $store[$path])) as $i => $line) {
                          $numbered[] = sprintf("%6d\t%s", $i + 1, $line);
                      }
                      return "Here's the content of {$path} with line numbers:\n" . implode("\n", $numbered);
                  }
                  if ($path === '/memories') {
                      $listing = ["1.0K\t/memories"];
                      foreach (array_keys($store) as $stored) {
                          $listing[] = "1.0K\t{$stored}";
                      }
                      return "Here're the files and directories up to 2 levels deep in {$path}, excluding hidden items and node_modules:\n" . implode("\n", $listing);
                  }
                  return "The path {$path} does not exist. Please provide a valid path.";
              case 'create':
                  $store[$path] = $input['file_text'];
                  return "File created successfully at: {$path}";
              case 'str_replace':
                  $position = strpos($store[$path] ?? '', $input['old_str']);
                  if ($position === false) {
                      return "No replacement was performed, old_str `{$input['old_str']}` did not appear verbatim in {$path}.";
                  }
                  $store[$path] = substr_replace($store[$path], $input['new_str'] ?? '', $position, strlen($input['old_str']));
                  return 'The memory file has been edited.';
              case 'insert':
                  if (!isset($store[$path])) {
                      return "Error: The path {$path} does not exist";
                  }
                  $lines = explode("\n", $store[$path]);
                  if ($input['insert_line'] < 0 || $input['insert_line'] > count($lines)) {
                      return "Error: Invalid `insert_line` parameter: {$input['insert_line']}. It should be within the range of lines of the file: [0, " . count($lines) . "]";
                  }
                  array_splice($lines, $input['insert_line'], 0, [preg_replace('/\n\z/', '', $input['insert_text'])]);
                  $store[$path] = implode("\n", $lines);
                  return "The file {$path} has been edited.";
              case 'delete':
                  if (!isset($store[$path])) {
                      return "Error: The path {$path} does not exist";
                  }
                  unset($store[$path]);
                  return "Successfully deleted {$path}";
              case 'rename':
                  if (!isset($store[$input['old_path']])) {
                      return "Error: The path {$input['old_path']} does not exist";
                  }
                  if (isset($store[$input['new_path']])) {
                      return "Error: The destination {$input['new_path']} already exists";
                  }
                  $store[$input['new_path']] = $store[$input['old_path']];
                  unset($store[$input['old_path']]);
                  return "Successfully renamed {$input['old_path']} to {$input['new_path']}";
              default:
                  return "Error: unknown command {$input['command']}";
          }
      },
  );

  $runner = $client->beta->messages->toolRunner(
      maxTokens: 1024,
      messages: [['role' => 'user', 'content' => 'Remember that customer Acme Corp prefers email follow-ups.']],
      model: Model::CLAUDE_OPUS_4_8,
      tools: [$memory],
      maxIterations: 10,
  );

  $finalMessage = $runner->runUntilDone();
  print_r($finalMessage->content);
  ```

  ```ruby Ruby
  require "anthropic"

  client = Anthropic::Client.new
  TOOLS = [{type: "memory_20250818", name: "memory"}].freeze

  # An in-memory store that maps memory file paths to their contents.
  # Use your own storage in production.
  STORE = {}

  def execute_memory(input)
    path = input[:path]
    case input[:command]
    when "view"
      if STORE.key?(path)
        lines = STORE[path].chomp.split("\n", -1)
        lines = [""] if lines.empty?
        numbered = lines.each_with_index.map { |line, i| format("%6d\t%s", i + 1, line) }
        "Here's the content of #{path} with line numbers:\n#{numbered.join("\n")}"
      elsif path == "/memories"
        listing = ["1.0K\t/memories"] + STORE.keys.map { |stored| "1.0K\t#{stored}" }
        "Here're the files and directories up to 2 levels deep in #{path}, excluding hidden items and node_modules:\n#{listing.join("\n")}"
      else
        "The path #{path} does not exist. Please provide a valid path."
      end
    when "create"
      STORE[path] = input[:file_text]
      "File created successfully at: #{path}"
    when "str_replace"
      unless STORE.key?(path) && STORE[path].include?(input[:old_str])
        return "No replacement was performed, old_str `#{input[:old_str]}` did not appear verbatim in #{path}."
      end
      STORE[path] = STORE[path].sub(input[:old_str]) { input[:new_str].to_s }
      "The memory file has been edited."
    when "insert"
      return "Error: The path #{path} does not exist" unless STORE.key?(path)
      lines = STORE[path].split("\n", -1)
      lines = [""] if lines.empty?
      if input[:insert_line] < 0 || input[:insert_line] > lines.length
        return "Error: Invalid `insert_line` parameter: #{input[:insert_line]}. It should be within the range of lines of the file: [0, #{lines.length}]"
      end
      lines.insert(input[:insert_line], input[:insert_text].chomp)
      STORE[path] = lines.join("\n")
      "The file #{path} has been edited."
    when "delete"
      return "Error: The path #{path} does not exist" unless STORE.key?(path)
      STORE.delete(path)
      "Successfully deleted #{path}"
    when "rename"
      return "Error: The path #{input[:old_path]} does not exist" unless STORE.key?(input[:old_path])
      return "Error: The destination #{input[:new_path]} already exists" if STORE.key?(input[:new_path])
      STORE[input[:new_path]] = STORE.delete(input[:old_path])
      "Successfully renamed #{input[:old_path]} to #{input[:new_path]}"
    else
      "Error: unknown command #{input[:command]}"
    end
  end

  messages = [{role: "user", content: "Remember that customer Acme Corp prefers email follow-ups."}]
  loop do
    message = client.messages.create(
      model: Anthropic::Model::CLAUDE_OPUS_4_8,
      max_tokens: 1024,
      messages: messages,
      tools: TOOLS
    )
    unless message.stop_reason == :tool_use
      puts message.content
      break
    end
    tool_results = message.content.filter_map do |block|
      next unless block.type == :tool_use
      {type: "tool_result", tool_use_id: block.id, content: execute_memory(block.input)}
    end
    messages << {role: "assistant", content: message.content} << {role: "user", content: tool_results}
  end
  ```
</CodeGroup>

The in-memory stores in the Go, PHP, and Ruby examples keep them self-contained: each one dispatches on the `command` field in the `tool_use` block's `input` and returns the strings described under [Tool commands](#tool-commands). A production handler also needs the [path validation](#path-traversal-protection) these demonstration stores skip. For the SDKs' own complete examples, see:

* Python: [examples/memory/basic.py](https://github.com/anthropics/anthropic-sdk-python/blob/main/examples/memory/basic.py)
* TypeScript: [examples/tools-helpers-memory.ts](https://github.com/anthropics/anthropic-sdk-typescript/blob/main/examples/tools-helpers-memory.ts)
* C#: [MemoryToolExample](https://github.com/anthropics/anthropic-sdk-csharp/tree/main/examples/MemoryToolExample)
* Java: [BetaMemoryToolExample.java](https://github.com/anthropics/anthropic-sdk-java/blob/main/anthropic-java-example/src/main/java/com/anthropic/example/BetaMemoryToolExample.java)

## Tool commands

Your client-side implementation must handle the following commands. These specifications describe the recommended behaviors and return strings: Claude reads whatever text your tool result contains, so you can return different strings if your application needs to.

### view

Shows directory contents or file contents with optional line ranges:

```json
{
  "command": "view",
  "path": "/memories/notes.txt",
  "view_range": [1, 10]
}
```

`view_range` is optional and applies to text-file views: `[start_line, end_line]` returns those lines, and `[start_line, -1]` returns everything from `start_line` to the end of the file.

#### Return values

**For directories:** Return a listing that shows files and directories with their sizes:

```text
Here're the files and directories up to 2 levels deep in {path}, excluding hidden items and node_modules:
{size}\t{path}
{size}\t{path}/{filename1}
{size}\t{path}/{filename2}
```

* Lists files up to 2 levels deep
* Shows human-readable sizes (for example, `5.5K`, `1.2M`)
* Excludes hidden items (files starting with `.`) and `node_modules`
* Uses a tab character between the size and the path

The first `view` of `/memories` on an empty store is not an error. The SDKs' local-filesystem memory tools (`BetaLocalFilesystemMemoryTool`) create the memory root before Claude's first call and return the listing header followed by a single size-and-path line for the empty directory itself.

**For files:** Return file contents with a header and line numbers:

```text wrap
Here's the content of {path} with line numbers:
{line_numbers}{tab}{content}
```

Line number formatting:

* **Width:** 6 characters, right-aligned with space padding
* **Separator:** Tab character between line number and content
* **Indexing:** 1-indexed (first line is line 1)
* **Line limit:** Files with more than 999,999 lines should return an error: `"File {path} exceeds maximum line limit of 999,999 lines."`

**Example output:**

```text
Here's the content of /memories/notes.txt with line numbers:
     1	Hello World
     2	This is line two
    10	Line ten
   100	Line one hundred
```

Claude's tool description also says that `view` displays image files (`.jpg`, `.jpeg`, and `.png`) and truncates the text view of files longer than 16,000 characters. Expect `view` calls on image paths and follow-up ranged views of long files.

#### Error handling

* **File or directory does not exist:** `"The path {path} does not exist. Please provide a valid path."`

### create

Creates a new file:

```json
{
  "command": "create",
  "path": "/memories/notes.txt",
  "file_text": "Meeting notes:\n- Discussed project timeline\n- Next steps defined\n"
}
```

#### Return values

* **Success:** `"File created successfully at: {path}"`

#### Error handling

* **File already exists:** `"Error: File {path} already exists"`

Claude's tool description says `create` "creates or overwrites" a file, so expect `create` calls on paths that already exist. Returning the error is the reference behavior, and overwriting instead is a valid implementation choice.

### str\_replace

Replaces text in a file:

```json
{
  "command": "str_replace",
  "path": "/memories/preferences.txt",
  "old_str": "Favorite color: blue",
  "new_str": "Favorite color: green"
}
```

`new_str` is optional for `str_replace`: when it's omitted, `old_str` is deleted without a replacement.

#### Return values

* **Success:** `"The memory file has been edited."` followed by a snippet of the edited file with line numbers

#### Error handling

* **File does not exist:** `"Error: The path {path} does not exist. Please provide a valid path."`
* **Text not found:** ``"No replacement was performed, old_str `\{old_str}` did not appear verbatim in {path}."``
* **Duplicate text:** When `old_str` appears multiple times, return: ``"No replacement was performed. Multiple occurrences of old_str `\{old_str}` in lines: {line_numbers}. Please ensure it is unique"``

#### Directory handling

If the path is a directory, return a "file does not exist" error.

### insert

Inserts text at a specific line:

```json
{
  "command": "insert",
  "path": "/memories/todo.txt",
  "insert_line": 2,
  "insert_text": "- Review memory tool documentation\n"
}
```

`insert_text` is inserted after line `insert_line`, and `0` inserts at the beginning of the file.

#### Return values

* **Success:** `"The file {path} has been edited."`

#### Error handling

* **File does not exist:** `"Error: The path {path} does not exist"`
* **Invalid line number:** ``"Error: Invalid `insert_line` parameter: {insert_line}. It should be within the range of lines of the file: [0, {n_lines}]"``

#### Directory handling

If the path is a directory, return a "file does not exist" error.

### delete

Deletes a file or directory:

```json
{
  "command": "delete",
  "path": "/memories/old_file.txt"
}
```

#### Return values

* **Success:** `"Successfully deleted {path}"`

#### Error handling

* **File or directory does not exist:** `"Error: The path {path} does not exist"`

#### Directory handling

Deletes the directory and all its contents recursively. The tool description tells Claude it cannot delete the `/memories` directory itself, so reject a `delete` whose path is the memory root.

### rename

Renames or moves a file or directory:

```json
{
  "command": "rename",
  "old_path": "/memories/draft.txt",
  "new_path": "/memories/final.txt"
}
```

#### Return values

* **Success:** `"Successfully renamed {old_path} to {new_path}"`

#### Error handling

* **Source does not exist:** `"Error: The path {old_path} does not exist"`
* **Destination already exists:** Return an error (do not overwrite): `"Error: The destination {new_path} already exists"`

#### Directory handling

Renames the directory. The tool description tells Claude it cannot rename the `/memories` directory itself, so reject a `rename` whose `old_path` is the memory root.

## Prompting guidance

When the memory tool is present in your request's `tools`, the API automatically adds this instruction to the system prompt. You don't need to send it yourself:

```text wrap
IMPORTANT: ALWAYS VIEW YOUR MEMORY DIRECTORY BEFORE DOING ANYTHING ELSE.
MEMORY PROTOCOL:
1. Use the `view` command of your `memory` tool to check for earlier progress.
2. ... (work on the task) ...
   - As you make progress, record status / progress / thoughts etc in your memory.
ASSUME INTERRUPTION: Your context window might be reset at any moment, so you risk losing any progress that is not recorded in your memory directory.
```

Claude's tool description already tells it to keep the memory directory organized, so you don't need to repeat that instruction. If Claude still creates cluttered memory files, you can reinforce it in your prompt:

```text wrap
Note: when editing your memory folder, always try to keep its content up-to-date, coherent and organized. You can rename or delete files that are no longer relevant. Do not create new files unless necessary.
```

You can also guide what Claude writes to memory. For example: "Only write down information relevant to \<topic> in your memory system."

## Security considerations

Your application executes every file operation Claude requests, so these safeguards are your responsibility:

### Sensitive information

Claude usually refuses to write sensitive information to memory files. For stronger guarantees, add validation that strips sensitive data before your handler writes the file.

### File storage size

Track memory file sizes and cap how large a file can grow. Consider capping how many characters the `view` command returns, and let Claude page through the rest with `view_range`.

### Memory expiration

Periodically delete memory files that haven't been accessed in a long time.

### Path traversal protection

<Warning>
  A malicious path such as `/memories/../../secrets.env` can reach files outside the `/memories` directory. Your implementation must validate every path in every command to prevent directory traversal attacks.
</Warning>

Consider these safeguards:

* Validate that all paths start with `/memories`
* Resolve paths to their canonical form and verify they remain within the memory directory
* Reject paths containing sequences such as `../`, `..\\`, or other traversal patterns
* Watch for URL-encoded traversal sequences (`%2e%2e%2f`)
* Use your language's built-in path security utilities (for example, Python's `pathlib.Path.resolve()` and `relative_to()`)

## Error handling

The memory tool uses similar error-handling patterns to the [text editor tool](/docs/en/agents-and-tools/tool-use/text-editor-tool#handle-errors). Each command's error messages are listed under [Tool commands](#tool-commands). To return an error to Claude, set `is_error` to `true` on the tool result and put the message in `content`:

```json
{
  "type": "tool_result",
  "tool_use_id": "toolu_01C4D5E6F7G8H9I0J1K2L3M4",
  "content": "Error: The path /memories/notes.txt does not exist",
  "is_error": true
}
```

## Context editing integration

The memory tool pairs with context editing to manage long-running conversations. For details, see [Context editing](/docs/en/build-with-claude/context-editing).

## Using with compaction

The memory tool can also be paired with [compaction](/docs/en/build-with-claude/compaction), which summarizes older conversation context server-side. Context editing clears specific tool results on the client. Compaction automatically summarizes the whole conversation on the server when the conversation approaches the context window limit.

For long-running agents, consider using both: compaction keeps the active context small without client-side bookkeeping, and memory preserves the information that must survive summarization.

## Multisession software development pattern

For software projects that span multiple agent sessions, set up memory files deliberately instead of writing them ad hoc as work progresses. The following pattern turns memory into a recovery mechanism: each new session resumes from the state the last one recorded.

### How the pattern works

1. **Initializer session:** The first session sets up the memory files before any substantive work begins. This includes a progress log (tracking what has been done and what comes next), a feature checklist (defining the scope of work), and a reference to any startup or initialization script the project needs.

2. **Subsequent sessions:** Each new session opens by reading those memory files. This restores the project state without re-exploring the code base or retracing earlier decisions.

3. **End-of-session update:** Before a session ends, it updates the progress log with what was completed and what remains. This ensures the next session has an accurate starting point.

### Key principle

Work on one feature at a time. Mark a feature complete only after end-to-end verification confirms it works, not when the code is written. This keeps the progress log accurate from session to session.

<Tip>
  For a detailed case study of this pattern in practice, including the initializer script, progress file structure, and git-based recovery, see [Effective harnesses for long-running agents](https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents).
</Tip>

## Next steps

<CardGroup cols={2}>
  <Card title="Bash tool" icon="terminal" href="/docs/en/agents-and-tools/tool-use/bash-tool">
    Execute shell commands in a persistent bash session.
  </Card>

  <Card title="Context editing" icon="edit" href="/docs/en/build-with-claude/context-editing">
    Automatically manage conversation context as it grows with context editing.
  </Card>

  <Card title="Compaction" icon="stack" href="/docs/en/build-with-claude/compaction">
    Server-side context compaction for managing long conversations that approach context window limits.
  </Card>

  <Card title="Tool reference" icon="book" href="/docs/en/agents-and-tools/tool-use/tool-reference">
    Directory of Anthropic-provided tools and reference for optional tool definition properties.
  </Card>
</CardGroup>
