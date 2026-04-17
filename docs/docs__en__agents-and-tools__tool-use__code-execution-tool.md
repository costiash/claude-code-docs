# Code execution tool

Run Python and bash code in a sandboxed container to analyze data, generate files, and iterate on solutions.

---

Claude can analyze data, create visualizations, perform complex calculations, run system commands, create and edit files, and process uploaded files directly within the API conversation. The code execution tool allows Claude to run Bash commands and manipulate files, including writing code, in a secure, sandboxed environment.

**Code execution is free when used with web search or web fetch.** When `web_search_20260209` or `web_fetch_20260209` is included in your request, there are no additional charges for code execution tool calls beyond the standard input and output token costs. Standard code execution charges apply when these tools are not included.

Code execution is a core primitive for building high-performance agents. It enables dynamic filtering in web search and web fetch tools, allowing Claude to process results before they reach the context window, improving accuracy while reducing token consumption.

<Note>
Reach out through the [feedback form](https://forms.gle/LTAU6Xn2puCJMi1n6) to share your feedback on this feature.
</Note>

<Note>
This feature is **not** eligible for [Zero Data Retention (ZDR)](/docs/en/build-with-claude/api-and-data-retention). Data is retained according to the feature's standard retention policy.
</Note>

## Model compatibility

The code execution tool is available on the following models:

| Model | Tool versions |
|-------|--------------|
| Claude Opus 4.7 (`claude-opus-4-7`) | `code_execution_20250825`, `code_execution_20260120` |
| Claude Opus 4.6 (`claude-opus-4-6`) | `code_execution_20250825`, `code_execution_20260120` |
| Claude Sonnet 4.6 (`claude-sonnet-4-6`) | `code_execution_20250825`, `code_execution_20260120` |
| Claude Opus 4.5 (`claude-opus-4-5-20251101`) | `code_execution_20250825`, `code_execution_20260120` |
| Claude Sonnet 4.5 (`claude-sonnet-4-5-20250929`) | `code_execution_20250825`, `code_execution_20260120` |
| Claude Haiku 4.5 (`claude-haiku-4-5-20251001`) | `code_execution_20250825` |
| Claude Opus 4.1 (`claude-opus-4-1-20250805`) | `code_execution_20250825` |
| Claude Opus 4 (`claude-opus-4-20250514`) ([deprecated](/docs/en/about-claude/model-deprecations)) | `code_execution_20250825` |
| Claude Sonnet 4 (`claude-sonnet-4-20250514`) ([deprecated](/docs/en/about-claude/model-deprecations)) | `code_execution_20250825` |
| Claude Sonnet 3.7 (`claude-3-7-sonnet-20250219`) ([deprecated](/docs/en/about-claude/model-deprecations)) | `code_execution_20250825` |
| Claude Haiku 3.5 (`claude-3-5-haiku-latest`) ([deprecated](/docs/en/about-claude/model-deprecations)) | `code_execution_20250825` |

<Note>
`code_execution_20250825` supports Bash commands and file operations and is available on every model listed above. `code_execution_20260120` adds REPL state persistence and [programmatic tool calling](/docs/en/agents-and-tools/tool-use/programmatic-tool-calling) from within the sandbox, and is available on Opus 4.5+ and Sonnet 4.5+ only. A legacy version `code_execution_20250522` (Python only) is also available on the same models as `code_execution_20250825`; see [Upgrade to latest tool version](#upgrade-to-latest-tool-version) to migrate from it.
</Note>

<Warning>
Older tool versions are not guaranteed to be backwards-compatible with newer models. Always use the tool version that corresponds to your model version.
</Warning>

## Platform availability

Code execution is available on:
- **Claude API** (Anthropic)
- **Microsoft Azure AI Foundry**

Code execution is not currently available on Amazon Bedrock or Google Vertex AI.

<Note>
For [Claude Mythos Preview](https://anthropic.com/glasswing), code execution is supported on the Claude API and Microsoft Foundry only. It is not available for Mythos Preview on Amazon Bedrock or Google Vertex AI.
</Note>

## Quick start

Here's a simple example that asks Claude to perform a calculation:

<CodeGroup>
```bash cURL
curl https://api.anthropic.com/v1/messages \
    --header "x-api-key: $ANTHROPIC_API_KEY" \
    --header "anthropic-version: 2023-06-01" \
    --header "content-type: application/json" \
    --data '{
        "model": "claude-opus-4-7",
        "max_tokens": 4096,
        "messages": [
            {
                "role": "user",
                "content": "Calculate the mean and standard deviation of [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]"
            }
        ],
        "tools": [{
            "type": "code_execution_20250825",
            "name": "code_execution"
        }]
    }'
```

```bash CLI
ant messages create \
  --model claude-opus-4-7 \
  --max-tokens 4096 \
  --message '{role: user, content: "Calculate the mean and standard deviation of [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]"}' \
  --tool '{type: code_execution_20250825, name: code_execution}'
```

```python Python hidelines={1..2}
import anthropic

client = anthropic.Anthropic()

response = client.messages.create(
    model="claude-opus-4-7",
    max_tokens=4096,
    messages=[
        {
            "role": "user",
            "content": "Calculate the mean and standard deviation of [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]",
        }
    ],
    tools=[{"type": "code_execution_20250825", "name": "code_execution"}],
)

print(response)
```

```typescript TypeScript hidelines={1..5,-3..-1}
import Anthropic from "@anthropic-ai/sdk";

const client = new Anthropic();

async function main() {
  const response = await client.messages.create({
    model: "claude-opus-4-7",
    max_tokens: 4096,
    messages: [
      {
        role: "user",
        content: "Calculate the mean and standard deviation of [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]"
      }
    ],
    tools: [
      {
        type: "code_execution_20250825",
        name: "code_execution"
      }
    ]
  });

  console.log(response);
}

main().catch(console.error);
```

```csharp C# hidelines={1..11,-2..}
using System;
using System.Threading.Tasks;
using Anthropic;
using Anthropic.Models.Messages;

class Program
{
    static async Task Main(string[] args)
    {
        AnthropicClient client = new();

        var parameters = new MessageCreateParams
        {
            Model = Model.ClaudeOpus4_7,
            MaxTokens = 4096,
            Messages = [
                new() {
                    Role = Role.User,
                    Content = "Calculate the mean and standard deviation of [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]"
                }
            ],
            Tools = [new ToolUnion(new CodeExecutionTool20250825())]
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
		MaxTokens: 4096,
		Messages: []anthropic.BetaMessageParam{
			anthropic.NewBetaUserMessage(anthropic.NewBetaTextBlock("Calculate the mean and standard deviation of [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]")),
		},
		Tools: []anthropic.BetaToolUnionParam{
			{OfCodeExecutionTool20250825: &anthropic.BetaCodeExecutionTool20250825Param{}},
		},
		Betas: []anthropic.AnthropicBeta{"code-execution-2025-08-25"},
	})
	if err != nil {
		log.Fatal(err)
	}
	fmt.Println(response)
}
```

```java Java hidelines={1..5,7..9,-2..}
import com.anthropic.client.AnthropicClient;
import com.anthropic.client.okhttp.AnthropicOkHttpClient;
import com.anthropic.models.messages.MessageCreateParams;
import com.anthropic.models.messages.Message;
import com.anthropic.models.messages.Model;
import com.anthropic.models.messages.CodeExecutionTool20250825;

public class CodeExecution {
    public static void main(String[] args) {
        AnthropicClient client = AnthropicOkHttpClient.fromEnv();

        MessageCreateParams params = MessageCreateParams.builder()
            .model(Model.CLAUDE_OPUS_4_7)
            .maxTokens(4096L)
            .addUserMessage("Calculate the mean and standard deviation of [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]")
            .addTool(CodeExecutionTool20250825.builder().build())
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
    maxTokens: 4096,
    messages: [
        [
            'role' => 'user',
            'content' => 'Calculate the mean and standard deviation of [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]'
        ]
    ],
    model: 'claude-opus-4-7',
    tools: [
        [
            'type' => 'code_execution_20250825',
            'name' => 'code_execution'
        ]
    ],
);

echo $message;
```

```ruby Ruby hidelines={1..2}
require "anthropic"

client = Anthropic::Client.new

message = client.messages.create(
  model: "claude-opus-4-7",
  max_tokens: 4096,
  messages: [
    {
      role: "user",
      content: "Calculate the mean and standard deviation of [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]"
    }
  ],
  tools: [
    {
      type: "code_execution_20250825",
      name: "code_execution"
    }
  ]
)

puts message
```
</CodeGroup>

## How code execution works

When you add the code execution tool to your API request:

1. Claude evaluates whether code execution would help answer your question
2. The tool automatically provides Claude with the following capabilities:
   - **Bash commands**: Execute shell commands for system operations and package management
   - **File operations**: Create, view, and edit files directly, including writing code
3. Claude can use any combination of these capabilities in a single request
4. All operations run in a secure sandbox environment
5. Claude provides results with any generated charts, calculations, or analysis

## Using code execution with other execution tools

When you provide code execution alongside client-provided tools that also run code (such as a [bash tool](/docs/en/agents-and-tools/tool-use/bash-tool) or custom REPL), Claude is operating in a multi-computer environment. The code execution tool runs in Anthropic's sandboxed container, while your client-provided tools run in a separate environment that you control. Claude can sometimes confuse these environments, attempting to use the wrong tool or assuming state is shared between them.

To avoid this, add instructions to your system prompt that clarify the distinction:

```text
When multiple code execution environments are available, be aware that:
- Variables, files, and state do NOT persist between different execution environments
- Use the code_execution tool for general-purpose computation in Anthropic's sandboxed environment
- Use client-provided execution tools (e.g., bash) when you need access to the user's local system, files, or data
- If you need to pass results between environments, explicitly include outputs in subsequent tool calls rather than assuming shared state
```

This is especially important when combining code execution with [web search](/docs/en/agents-and-tools/tool-use/web-search-tool) or [web fetch](/docs/en/agents-and-tools/tool-use/web-fetch-tool), which enable code execution automatically. If your application already provides a client-side shell tool, the automatic code execution creates a second execution environment that Claude needs to distinguish between.

## How to use the tool

### Upload and analyze your own files

To analyze your own data files (CSV, Excel, images, etc.), upload them via the Files API and reference them in your request:

<Note>
Using the Files API with Code Execution requires the Files API beta header: `"anthropic-beta": "files-api-2025-04-14"`
</Note>

The Python environment can process various file types uploaded via the Files API, including:

- CSV
- Excel (.xlsx, .xls)
- JSON
- XML
- Images (JPEG, PNG, GIF, WebP)
- Text files (.txt, .md, .py, etc)

#### Upload and analyze files

1. **Upload your file** using the [Files API](/docs/en/build-with-claude/files)
2. **Reference the file** in your message using a `container_upload` content block
3. **Include the code execution tool** in your API request

<CodeGroup>
```bash cURL hidelines={1..2}
cd "$(mktemp -d)"
printf 'name,value\nfoo,1\nbar,2\n' > data.csv
# First, upload a file
curl https://api.anthropic.com/v1/files \
    --header "x-api-key: $ANTHROPIC_API_KEY" \
    --header "anthropic-version: 2023-06-01" \
    --header "anthropic-beta: files-api-2025-04-14" \
    --form 'file=@"data.csv"' \

# Then use the file_id with code execution
curl https://api.anthropic.com/v1/messages \
    --header "x-api-key: $ANTHROPIC_API_KEY" \
    --header "anthropic-version: 2023-06-01" \
    --header "anthropic-beta: files-api-2025-04-14" \
    --header "content-type: application/json" \
    --data '{
        "model": "claude-opus-4-7",
        "max_tokens": 4096,
        "messages": [{
            "role": "user",
            "content": [
                {"type": "text", "text": "Analyze this CSV data"},
                {"type": "container_upload", "file_id": "file_abc123"}
            ]
        }],
        "tools": [{
            "type": "code_execution_20250825",
            "name": "code_execution"
        }]
    }'
```

```bash CLI hidelines={1}
printf 'name,value\nfoo,1\nbar,2\n' > data.csv
# Upload a file
FILE_ID=$(ant beta:files upload \
  --file ./data.csv \
  --transform id --format yaml)

# Use the file_id with code execution
ant beta:messages create \
  --beta files-api-2025-04-14 <<YAML
model: claude-opus-4-7
max_tokens: 4096
messages:
  - role: user
    content:
      - type: text
        text: Analyze this CSV data
      - type: container_upload
        file_id: $FILE_ID
tools:
  - type: code_execution_20250825
    name: code_execution
YAML
```

```python Python nocheck hidelines={1..2}
import anthropic

client = anthropic.Anthropic()

# Upload a file
file_object = client.beta.files.upload(
    file=open("data.csv", "rb"),
)

# Use the file_id with code execution
response = client.beta.messages.create(
    model="claude-opus-4-7",
    betas=["files-api-2025-04-14"],
    max_tokens=4096,
    messages=[
        {
            "role": "user",
            "content": [
                {"type": "text", "text": "Analyze this CSV data"},
                {"type": "container_upload", "file_id": file_object.id},
            ],
        }
    ],
    tools=[{"type": "code_execution_20250825", "name": "code_execution"}],
)

print(response)
```

```typescript TypeScript nocheck hidelines={5..6,-3..-1}
import Anthropic, { toFile } from "@anthropic-ai/sdk";
import { createReadStream } from "fs";

const client = new Anthropic();

async function main() {
  // Upload a file
  const fileObject = await client.beta.files.upload({
    file: await toFile(createReadStream("data.csv"), undefined, { type: "text/csv" }),
    betas: ["files-api-2025-04-14"]
  });

  // Use the file_id with code execution
  const response = await client.beta.messages.create({
    model: "claude-opus-4-7",
    betas: ["files-api-2025-04-14"],
    max_tokens: 4096,
    messages: [
      {
        role: "user",
        content: [
          { type: "text", text: "Analyze this CSV data" },
          { type: "container_upload", file_id: fileObject.id }
        ]
      }
    ],
    tools: [
      {
        type: "code_execution_20250825",
        name: "code_execution"
      }
    ]
  });

  console.log(response);
}

main().catch(console.error);
```

```csharp C# nocheck hidelines={1..10,-2..}
using Anthropic;
using Anthropic.Models.Beta.Files;
using Anthropic.Models.Beta.Messages;

class Program
{
    static async Task Main(string[] args)
    {
        AnthropicClient client = new();

        // Upload a file
        var fileObject = await client.Beta.Files.Upload(new FileUploadParams
        {
            File = File.OpenRead("data.csv")
        });

        // Use the file_id with code execution
        var parameters = new MessageCreateParams
        {
            Model = Model.ClaudeOpus4_7,
            Betas = ["files-api-2025-04-14"],
            MaxTokens = 4096,
            Messages = [
                new()
                {
                    Role = Role.User,
                    Content = [
                        new() { Type = "text", Text = "Analyze this CSV data" },
                        new() { Type = "container_upload", FileId = fileObject.Id }
                    ]
                }
            ],
            Tools = [new ToolUnion(new CodeExecutionTool20250825())]
        };

        var response = await client.Beta.Messages.Create(parameters);
        Console.WriteLine(response);
    }
}
```

```go Go hidelines={11..15}
package main

import (
	"context"
	"fmt"
	"log"
	"os"

	"github.com/anthropics/anthropic-sdk-go"
)

func init() {
	os.WriteFile("data.csv", []byte("name,value\nalpha,1\nbeta,2\ngamma,3\n"), 0644)
}

func main() {
	client := anthropic.NewClient()

	// Upload a file
	file, err := os.Open("data.csv")
	if err != nil {
		log.Fatal(err)
	}
	defer file.Close()

	fileObject, err := client.Beta.Files.Upload(context.TODO(), anthropic.BetaFileUploadParams{
		File:  file,
		Betas: []anthropic.AnthropicBeta{anthropic.AnthropicBetaFilesAPI2025_04_14},
	})
	if err != nil {
		log.Fatal(err)
	}

	// Use the file_id with code execution
	response, err := client.Beta.Messages.New(context.TODO(), anthropic.BetaMessageNewParams{
		Model:     anthropic.ModelClaudeOpus4_7,
		MaxTokens: 4096,
		Messages: []anthropic.BetaMessageParam{
			anthropic.NewBetaUserMessage(
				anthropic.NewBetaTextBlock("Analyze this CSV data"),
				anthropic.NewBetaContainerUploadBlock(fileObject.ID),
			),
		},
		Tools: []anthropic.BetaToolUnionParam{
			{OfCodeExecutionTool20250825: &anthropic.BetaCodeExecutionTool20250825Param{}},
		},
		Betas: []anthropic.AnthropicBeta{
			"code-execution-2025-08-25",
			anthropic.AnthropicBetaFilesAPI2025_04_14,
		},
	})
	if err != nil {
		log.Fatal(err)
	}

	fmt.Println(response)
}
```

```java Java nocheck hidelines={1..2,5..6,8..9,11..15,-2..}
import com.anthropic.client.AnthropicClient;
import com.anthropic.client.okhttp.AnthropicOkHttpClient;
import com.anthropic.models.beta.files.FileMetadata;
import com.anthropic.models.beta.files.FileUploadParams;
import com.anthropic.models.beta.messages.BetaMessage;
import com.anthropic.models.beta.messages.MessageCreateParams;
import com.anthropic.models.beta.messages.BetaCodeExecutionTool20250825;
import com.anthropic.models.beta.messages.BetaContentBlockParam;
import com.anthropic.models.beta.messages.BetaTextBlockParam;
import com.anthropic.models.beta.messages.BetaContainerUploadBlockParam;
import java.nio.file.Paths;
import java.util.List;

public class CodeExecutionWithFiles {
    public static void main(String[] args) {
        AnthropicClient client = AnthropicOkHttpClient.fromEnv();

        // Upload a file
        FileMetadata fileMetadata = client.beta().files().upload(
            FileUploadParams.builder()
                .file(Paths.get("data.csv"))
                .build()
        );

        // Use the file_id with code execution
        BetaMessage response = client.beta().messages().create(
            MessageCreateParams.builder()
                .model("claude-opus-4-7")
                .addBeta("files-api-2025-04-14")
                .maxTokens(4096L)
                .addUserMessageOfBetaContentBlockParams(List.of(
                    BetaContentBlockParam.ofText(BetaTextBlockParam.builder()
                        .text("Analyze this CSV data")
                        .build()),
                    BetaContentBlockParam.ofContainerUpload(BetaContainerUploadBlockParam.builder()
                        .fileId(fileMetadata.id())
                        .build())
                ))
                .addTool(BetaCodeExecutionTool20250825.builder().build())
                .build()
        );

        System.out.println(response);
    }
}
```

```php PHP hidelines={1..4} nocheck
<?php

use Anthropic\Client;

$client = new Client(apiKey: getenv("ANTHROPIC_API_KEY"));

// Upload a file
$fileObject = $client->beta->files->upload(
    file: fopen('data.csv', 'r'),
);

// Use the file_id with code execution
$response = $client->beta->messages->create(
    maxTokens: 4096,
    messages: [
        [
            'role' => 'user',
            'content' => [
                ['type' => 'text', 'text' => 'Analyze this CSV data'],
                ['type' => 'container_upload', 'file_id' => $fileObject->id]
            ]
        ]
    ],
    model: 'claude-opus-4-7',
    betas: ['files-api-2025-04-14'],
    tools: [
        ['type' => 'code_execution_20250825', 'name' => 'code_execution']
    ],
);

echo $response;
```

```ruby Ruby nocheck hidelines={1..2}
require "anthropic"

client = Anthropic::Client.new

# Upload a file
file_object = client.beta.files.upload(
  file: File.open("data.csv", "rb")
)

# Use the file_id with code execution
response = client.beta.messages.create(
  model: "claude-opus-4-7",
  betas: ["files-api-2025-04-14"],
  max_tokens: 4096,
  messages: [
    {
      role: "user",
      content: [
        { type: "text", text: "Analyze this CSV data" },
        { type: "container_upload", file_id: file_object.id }
      ]
    }
  ],
  tools: [
    { type: "code_execution_20250825", name: "code_execution" }
  ]
)

puts response
```
</CodeGroup>

#### Retrieve generated files

When Claude creates files during code execution, you can retrieve these files using the Files API:

<CodeGroup>

```bash CLI nocheck
# Request code execution that creates files; extract file_ids from tool results
TOOL_RESULT='content.#(type=="bash_code_execution_tool_result")#'
FILE_IDS=$(ant beta:messages create \
  --beta files-api-2025-04-14 \
  --transform "${TOOL_RESULT}.content.content|@flatten|#.file_id" \
  --format yaml \
    --model claude-opus-4-7 \
    --max-tokens 4096 \
    --message '{role: user, content: Create a matplotlib visualization and save it as output.png}' \
    --tool '{type: code_execution_20250825, name: code_execution}'
)

# Download each created file
while IFS= read -r LINE; do
  [[ "$LINE" != "- "* ]] && continue
  FILE_ID="${LINE#- }"
  FILENAME=$(ant beta:files retrieve-metadata \
    --file-id "$FILE_ID" \
    --transform filename --format yaml)
  ant beta:files download \
    --file-id "$FILE_ID" \
    --output "$FILENAME" > /dev/null
  printf 'Downloaded: %s\n' "$FILENAME"
done <<< "$FILE_IDS"
```

```python Python nocheck hidelines={1..2}
from anthropic import Anthropic

# Initialize the client
client = Anthropic()

# Request code execution that creates files
response = client.beta.messages.create(
    model="claude-opus-4-7",
    betas=["files-api-2025-04-14"],
    max_tokens=4096,
    messages=[
        {
            "role": "user",
            "content": "Create a matplotlib visualization and save it as output.png",
        }
    ],
    tools=[{"type": "code_execution_20250825", "name": "code_execution"}],
)


# Extract file IDs from the response
def extract_file_ids(response):
    file_ids = []
    for item in response.content:
        if item.type == "bash_code_execution_tool_result":
            content_item = item.content
            if content_item.type == "bash_code_execution_result":
                # concrete-typed list: List[BashCodeExecutionOutputBlock]
                for file in content_item.content:
                    file_ids.append(file.file_id)
    return file_ids


# Download the created files
for file_id in extract_file_ids(response):
    file_metadata = client.beta.files.retrieve_metadata(file_id)
    file_content = client.beta.files.download(file_id)
    file_content.write_to_file(file_metadata.filename)
    print(f"Downloaded: {file_metadata.filename}")
```

```typescript TypeScript nocheck hidelines={5..6,-3..-1}
import Anthropic from "@anthropic-ai/sdk";
import { writeFile } from "fs/promises";

const client = new Anthropic();

async function main() {
  // Request code execution that creates files
  const response = await client.beta.messages.create({
    model: "claude-opus-4-7",
    betas: ["code-execution-2025-08-25", "files-api-2025-04-14"],
    max_tokens: 4096,
    messages: [
      {
        role: "user",
        content: "Create a matplotlib visualization and save it as output.png"
      }
    ],
    tools: [
      {
        type: "code_execution_20250825",
        name: "code_execution"
      }
    ]
  });

  // Extract file IDs from the response
  for (const item of response.content) {
    if (item.type === "bash_code_execution_tool_result") {
      const contentItem = item.content;
      if (contentItem.type === "bash_code_execution_result" && contentItem.content) {
        // concrete-typed list: BashCodeExecutionOutputBlock
        for (const file of contentItem.content) {
          const fileMetadata = await client.beta.files.retrieveMetadata(file.file_id);
          const fileResponse = await client.beta.files.download(file.file_id);
          const fileBytes = Buffer.from(await fileResponse.arrayBuffer());
          await writeFile(fileMetadata.filename, fileBytes);
          console.log(`Downloaded: ${fileMetadata.filename}`);
        }
      }
    }
  }
}

main().catch(console.error);
```

```csharp C# nocheck hidelines={1..14,-2..}
using System;
using System.IO;
using System.Linq;
using System.Threading.Tasks;
using System.Collections.Generic;
using Anthropic;
using Anthropic.Models.Messages;

public class Program
{
    static async Task Main(string[] args)
    {
        var client = new AnthropicClient();

        var parameters = new MessageCreateParams
        {
            Model = Model.ClaudeOpus4_7,
            MaxTokens = 4096,
            Messages = [
                new() {
                    Role = Role.User,
                    Content = "Create a matplotlib visualization and save it as output.png"
                }
            ],
            Tools = [new ToolUnion(new CodeExecutionTool20250825())]
        };

        var response = await client.Beta.Messages.Create(parameters, ["files-api-2025-04-14"]);

        var fileIds = ExtractFileIds(response);

        foreach (var fileId in fileIds)
        {
            var fileMetadata = await client.Beta.Files.RetrieveMetadata(fileId);
            var fileContent = await client.Beta.Files.Download(fileId);

            await File.WriteAllBytesAsync(fileMetadata.Filename, fileContent);
            Console.WriteLine($"Downloaded: {fileMetadata.Filename}");
        }
    }

    static List<string> ExtractFileIds(dynamic response)
    {
        var fileIds = new List<string>();
        foreach (var item in response.Content)
        {
            if (item.Type == "bash_code_execution_tool_result")
            {
                var contentItem = item.Content;
                if (contentItem.Type == "bash_code_execution_result")
                {
                    // concrete-typed list: BetaBashCodeExecutionOutputBlock
                    foreach (var file in contentItem.Content)
                    {
                        if (file.FileId != null)
                        {
                            fileIds.Add(file.FileId);
                        }
                    }
                }
            }
        }
        return fileIds;
    }
}
```

```go Go nocheck hidelines={1..13,65..66}
package main

import (
	"context"
	"fmt"
	"io"
	"log"
	"os"

	"github.com/anthropics/anthropic-sdk-go"
)

func main() {
	client := anthropic.NewClient()

	response, err := client.Beta.Messages.New(context.TODO(), anthropic.BetaMessageNewParams{
		Model:     anthropic.ModelClaudeOpus4_7,
		MaxTokens: 4096,
		Messages: []anthropic.BetaMessageParam{
			anthropic.NewBetaUserMessage(anthropic.NewBetaTextBlock("Create a matplotlib visualization and save it as output.png")),
		},
		Tools: []anthropic.BetaToolUnionParam{
			{OfCodeExecutionTool20250825: &anthropic.BetaCodeExecutionTool20250825Param{}},
		},
		Betas: []anthropic.AnthropicBeta{
			"code-execution-2025-08-25",
			anthropic.AnthropicBetaFilesAPI2025_04_14,
		},
	})
	if err != nil {
		log.Fatal(err)
	}

	fileIDs := extractFileIDs(response)

	for _, fileID := range fileIDs {
		fileMetadata, err := client.Beta.Files.GetMetadata(context.TODO(), fileID, anthropic.BetaFileGetMetadataParams{
			Betas: []anthropic.AnthropicBeta{anthropic.AnthropicBetaFilesAPI2025_04_14},
		})
		if err != nil {
			log.Fatal(err)
		}

		fileContent, err := client.Beta.Files.Download(context.TODO(), fileID, anthropic.BetaFileDownloadParams{
			Betas: []anthropic.AnthropicBeta{anthropic.AnthropicBetaFilesAPI2025_04_14},
		})
		if err != nil {
			log.Fatal(err)
		}

		outFile, err := os.Create(fileMetadata.Filename)
		if err != nil {
			log.Fatal(err)
		}

		_, err = io.Copy(outFile, fileContent.Body)
		if err != nil {
			log.Fatal(err)
		}
		outFile.Close()
		fileContent.Body.Close()

		fmt.Printf("Downloaded: %s\n", fileMetadata.Filename)
	}
}

func extractFileIDs(response *anthropic.BetaMessage) []string {
	var fileIDs []string
	for _, item := range response.Content {
		switch variant := item.AsAny().(type) {
		case anthropic.BetaBashCodeExecutionToolResultBlock:
			// concrete-typed list: BashCodeExecutionOutputBlock
			for _, file := range variant.Content.Content {
				if file.FileID != "" {
					fileIDs = append(fileIDs, file.FileID)
				}
			}
		}
	}
	return fileIDs
}
```

```java Java nocheck hidelines={1..6,11..15,39..40}
import com.anthropic.client.AnthropicClient;
import com.anthropic.client.okhttp.AnthropicOkHttpClient;
import com.anthropic.core.http.HttpResponse;
import com.anthropic.models.beta.messages.MessageCreateParams;
import com.anthropic.models.beta.messages.BetaMessage;
import com.anthropic.models.beta.messages.BetaContentBlock;
import com.anthropic.models.beta.messages.BetaCodeExecutionTool20250825;
import com.anthropic.models.beta.messages.BetaBashCodeExecutionResultBlock;
import com.anthropic.models.beta.messages.BetaBashCodeExecutionOutputBlock;
import com.anthropic.models.beta.files.FileMetadata;
import java.io.FileOutputStream;
import java.util.ArrayList;
import java.util.List;

void main() throws Exception {
    AnthropicClient client = AnthropicOkHttpClient.fromEnv();

    MessageCreateParams params = MessageCreateParams.builder()
        .model("claude-opus-4-7")
        .addBeta("files-api-2025-04-14")
        .maxTokens(4096L)
        .addUserMessage("Create a matplotlib visualization and save it as output.png")
        .addTool(BetaCodeExecutionTool20250825.builder().build())
        .build();

    BetaMessage response = client.beta().messages().create(params);

    List<String> fileIds = extractFileIds(response);

    for (String fileId : fileIds) {
        FileMetadata fileMetadata = client.beta().files().retrieveMetadata(fileId);
        try (HttpResponse fileContent = client.beta().files().download(fileId)) {
            try (FileOutputStream fos = new FileOutputStream(fileMetadata.filename())) {
                fileContent.body().transferTo(fos);
            }
        }
        IO.println("Downloaded: " + fileMetadata.filename());
    }
}

List<String> extractFileIds(BetaMessage response) {
    List<String> fileIds = new ArrayList<>();
    // .ifPresent() is the discriminator guard (not concrete-typed; scanner can't see lambda guards)
    for (BetaContentBlock item : response.content()) {
        item.bashCodeExecutionToolResult().ifPresent(toolResult -> {
            if (toolResult.content().isBetaBashCodeExecutionResultBlock()) {
                BetaBashCodeExecutionResultBlock result =
                    toolResult.content().asBetaBashCodeExecutionResultBlock();
                // concrete-typed list: BetaBashCodeExecutionOutputBlock
                for (BetaBashCodeExecutionOutputBlock output : result.content()) {
                    fileIds.add(output.fileId());
                }
            }
        });
    }
    return fileIds;
}
```

```php PHP hidelines={1..4} nocheck
<?php

use Anthropic\Client;

$client = new Client(apiKey: getenv("ANTHROPIC_API_KEY"));

$response = $client->beta->messages->create(
    maxTokens: 4096,
    messages: [
        [
            'role' => 'user',
            'content' => 'Create a matplotlib visualization and save it as output.png'
        ]
    ],
    model: 'claude-opus-4-7',
    betas: ['files-api-2025-04-14'],
    tools: [
        [
            'type' => 'code_execution_20250825',
            'name' => 'code_execution'
        ]
    ],
);

function extractFileIds($response) {
    $fileIds = [];
    foreach ($response->content as $item) {
        if ($item->type === 'bash_code_execution_tool_result') {
            $contentItem = $item->content;
            if ($contentItem->type === 'bash_code_execution_result') {
                // concrete-typed list: BashCodeExecutionOutputBlock
                foreach ($contentItem->content as $file) {
                    $fileIds[] = $file->fileID;
                }
            }
        }
    }
    return $fileIds;
}

foreach (extractFileIds($response) as $fileId) {
    $fileMetadata = $client->beta->files->retrieveMetadata(fileID: $fileId, betas: ['files-api-2025-04-14']);
    $fileContent = $client->beta->files->download(fileID: $fileId, betas: ['files-api-2025-04-14']);

    file_put_contents($fileMetadata->filename, $fileContent);
    echo "Downloaded: {$fileMetadata->filename}\n";
}
```

```ruby Ruby nocheck hidelines={1..2}
require "anthropic"

client = Anthropic::Client.new

response = client.beta.messages.create(
  model: "claude-opus-4-7",
  betas: ["files-api-2025-04-14"],
  max_tokens: 4096,
  messages: [
    {
      role: "user",
      content: "Create a matplotlib visualization and save it as output.png"
    }
  ],
  tools: [
    {
      type: "code_execution_20250825",
      name: "code_execution"
    }
  ]
)

def extract_file_ids(response)
  file_ids = []
  response.content.each do |item|
    if item.type == :bash_code_execution_tool_result
      content_item = item.content
      if content_item.type == :bash_code_execution_result
        # concrete-typed list: BashCodeExecutionOutputBlock
        content_item.content.each do |file|
          file_ids << file.file_id
        end
      end
    end
  end
  file_ids
end

extract_file_ids(response).each do |file_id|
  file_metadata = client.beta.files.retrieve_metadata(file_id)
  file_content = client.beta.files.download(file_id)

  File.open(file_metadata.filename, "wb") do |f|
    f.write(file_content.read)
  end

  puts "Downloaded: #{file_metadata.filename}"
end
```
</CodeGroup>

## Tool definition

The code execution tool requires no additional parameters:

```json JSON
{
  "type": "code_execution_20250825",
  "name": "code_execution"
}
```

When this tool is provided, Claude automatically gains access to two sub-tools:
- `bash_code_execution`: Run shell commands
- `text_editor_code_execution`: View, create, and edit files, including writing code

## Response format

The code execution tool can return two types of results depending on the operation:

### Bash command response

```json Output hidelines={1,-1}
[
  {
    "type": "server_tool_use",
    "id": "srvtoolu_01B3C4D5E6F7G8H9I0J1K2L3",
    "name": "bash_code_execution",
    "input": {
      "command": "ls -la | head -5"
    }
  },
  {
    "type": "bash_code_execution_tool_result",
    "tool_use_id": "srvtoolu_01B3C4D5E6F7G8H9I0J1K2L3",
    "content": {
      "type": "bash_code_execution_result",
      "stdout": "total 24\ndrwxr-xr-x 2 user user 4096 Jan 1 12:00 .\ndrwxr-xr-x 3 user user 4096 Jan 1 11:00 ..\n-rw-r--r-- 1 user user  220 Jan 1 12:00 data.csv\n-rw-r--r-- 1 user user  180 Jan 1 12:00 config.json",
      "stderr": "",
      "return_code": 0
    }
  }
]
```

### File operation responses

**View file:**
```json Output hidelines={1,-1}
[
  {
    "type": "server_tool_use",
    "id": "srvtoolu_01C4D5E6F7G8H9I0J1K2L3M4",
    "name": "text_editor_code_execution",
    "input": {
      "command": "view",
      "path": "config.json"
    }
  },
  {
    "type": "text_editor_code_execution_tool_result",
    "tool_use_id": "srvtoolu_01C4D5E6F7G8H9I0J1K2L3M4",
    "content": {
      "type": "text_editor_code_execution_result",
      "file_type": "text",
      "content": "{\n  \"setting\": \"value\",\n  \"debug\": true\n}",
      "numLines": 4,
      "startLine": 1,
      "totalLines": 4
    }
  }
]
```

**Create file:**
```json Output hidelines={1,-1}
[
  {
    "type": "server_tool_use",
    "id": "srvtoolu_01D5E6F7G8H9I0J1K2L3M4N5",
    "name": "text_editor_code_execution",
    "input": {
      "command": "create",
      "path": "new_file.txt",
      "file_text": "Hello, World!"
    }
  },
  {
    "type": "text_editor_code_execution_tool_result",
    "tool_use_id": "srvtoolu_01D5E6F7G8H9I0J1K2L3M4N5",
    "content": {
      "type": "text_editor_code_execution_result",
      "is_file_update": false
    }
  }
]
```

**Edit file (str_replace):**
```json Output hidelines={1,-1}
[
  {
    "type": "server_tool_use",
    "id": "srvtoolu_01E6F7G8H9I0J1K2L3M4N5O6",
    "name": "text_editor_code_execution",
    "input": {
      "command": "str_replace",
      "path": "config.json",
      "old_str": "\"debug\": true",
      "new_str": "\"debug\": false"
    }
  },
  {
    "type": "text_editor_code_execution_tool_result",
    "tool_use_id": "srvtoolu_01E6F7G8H9I0J1K2L3M4N5O6",
    "content": {
      "type": "text_editor_code_execution_result",
      "oldStart": 3,
      "oldLines": 1,
      "newStart": 3,
      "newLines": 1,
      "lines": ["-  \"debug\": true", "+  \"debug\": false"]
    }
  }
]
```

### Results

All execution results include:
- `stdout`: Output from successful execution
- `stderr`: Error messages if execution fails
- `return_code`: 0 for success, non-zero for failure

Additional fields for file operations:
- **View**: `file_type`, `content`, `numLines`, `startLine`, `totalLines`
- **Create**: `is_file_update` (whether file already existed)
- **Edit**: `oldStart`, `oldLines`, `newStart`, `newLines`, `lines` (diff format)

### Errors

Each tool type can return specific errors:

**Common errors (all tools):**
```json Output
{
  "type": "bash_code_execution_tool_result",
  "tool_use_id": "srvtoolu_01VfmxgZ46TiHbmXgy928hQR",
  "content": {
    "type": "bash_code_execution_tool_result_error",
    "error_code": "unavailable"
  }
}
```

**Error codes by tool type:**

| Tool | Error Code | Description |
|------|-----------|-------------|
| All tools | `unavailable` | The tool is temporarily unavailable |
| All tools | `execution_time_exceeded` | Execution exceeded maximum time limit |
| All tools | `container_expired` | Container expired and is no longer available |
| All tools | `invalid_tool_input` | Invalid parameters provided to the tool |
| All tools | `too_many_requests` | Rate limit exceeded for tool usage |
| bash | `output_file_too_large` | Command output exceeded the maximum size |
| text_editor | `file_not_found` | File doesn't exist (for view/edit operations) |
| text_editor | `string_not_found` | The `old_str` not found in file (for str_replace) |

#### `pause_turn` stop reason

The response may include a `pause_turn` stop reason, which indicates that the API paused a long-running turn. You may
provide the response back as-is in a subsequent request to let Claude continue its turn, or modify the content if you
wish to interrupt the conversation.

## Containers

The code execution tool runs in a secure, containerized environment designed specifically for code execution, with a higher focus on Python.

### Runtime environment
- **Python version**: 3.11.12
- **Operating system**: Linux-based container
- **Architecture**: x86_64 (AMD64)

### Resource limits
- **Memory**: 5GiB RAM
- **Disk space**: 5GiB workspace storage
- **CPU**: 1 CPU

### Networking and security
- **Internet access**: Completely disabled for security
- **External connections**: No outbound network requests permitted
- **Sandbox isolation**: Full isolation from host system and other containers
- **File access**: Limited to workspace directory only
- **Workspace scoping**: Like [Files](/docs/en/build-with-claude/files), containers are scoped to the workspace of the API key
- **Expiration**: Containers expire 30 days after creation

### Pre-installed libraries
The sandboxed Python environment includes these commonly used libraries:
- **Data Science**: pandas, numpy, scipy, scikit-learn, statsmodels
- **Visualization**: matplotlib, seaborn
- **File Processing**: pyarrow, openpyxl, xlsxwriter, xlrd, pillow, python-pptx, python-docx, pypdf, pdfplumber, pypdfium2, pdf2image, pdfkit, tabula-py, reportlab[pycairo], Img2pdf
- **Math & Computing**: sympy, mpmath
- **Utilities**: tqdm, python-dateutil, pytz, joblib, unzip, unrar, 7zip, bc, rg (ripgrep), fd, sqlite

## Container reuse

You can reuse an existing container across multiple API requests by providing the container ID from a previous response.
This allows you to maintain created files between requests.

### Example

<CodeGroup>
```bash cURL hidelines={1}
cd "$(mktemp -d)"
# First request: Create a file with a random number
curl https://api.anthropic.com/v1/messages \
    --header "x-api-key: $ANTHROPIC_API_KEY" \
    --header "anthropic-version: 2023-06-01" \
    --header "content-type: application/json" \
    --data '{
        "model": "claude-opus-4-7",
        "max_tokens": 4096,
        "messages": [{
            "role": "user",
            "content": "Write a file with a random number and save it to \"/tmp/number.txt\""
        }],
        "tools": [{
            "type": "code_execution_20250825",
            "name": "code_execution"
        }]
    }' > response1.json

# Extract container ID from the response (using jq)
CONTAINER_ID=$(jq -r '.container.id' response1.json)

# Second request: Reuse the container to read the file
curl https://api.anthropic.com/v1/messages \
    --header "x-api-key: $ANTHROPIC_API_KEY" \
    --header "anthropic-version: 2023-06-01" \
    --header "content-type: application/json" \
    --data '{
        "container": "'$CONTAINER_ID'",
        "model": "claude-opus-4-7",
        "max_tokens": 4096,
        "messages": [{
            "role": "user",
            "content": "Read the number from \"/tmp/number.txt\" and calculate its square"
        }],
        "tools": [{
            "type": "code_execution_20250825",
            "name": "code_execution"
        }]
    }'
```

```bash CLI
# First request: Create a file with a random number
CONTAINER_ID=$(ant messages create \
  --transform container.id --format yaml \
    --model claude-opus-4-7 \
    --max-tokens 4096 \
    --message '{role: user, content: Write a file with a random number and save it to "/tmp/number.txt"}' \
    --tool '{type: code_execution_20250825, name: code_execution}'
)

# Second request: Reuse the container to read the file
ant messages create --container "$CONTAINER_ID" \
  --model claude-opus-4-7 \
  --max-tokens 4096 \
  --message '{role: user, content: Read the number from "/tmp/number.txt" and calculate its square}' \
  --tool '{type: code_execution_20250825, name: code_execution}'
```

```python Python hidelines={1..6}
import os
from anthropic import Anthropic

# Initialize the client
client = Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))

# First request: Create a file with a random number
response1 = client.messages.create(
    model="claude-opus-4-7",
    max_tokens=4096,
    messages=[
        {
            "role": "user",
            "content": "Write a file with a random number and save it to '/tmp/number.txt'",
        }
    ],
    tools=[{"type": "code_execution_20250825", "name": "code_execution"}],
)

# Extract the container ID from the first response
container_id = response1.container.id

# Second request: Reuse the container to read the file
response2 = client.messages.create(
    container=container_id,  # Reuse the same container
    model="claude-opus-4-7",
    max_tokens=4096,
    messages=[
        {
            "role": "user",
            "content": "Read the number from '/tmp/number.txt' and calculate its square",
        }
    ],
    tools=[{"type": "code_execution_20250825", "name": "code_execution"}],
)

print(response2)
```

```typescript TypeScript hidelines={1..5,-3..-1}
import Anthropic from "@anthropic-ai/sdk";

const client = new Anthropic();

async function main() {
  // First request: Create a file with a random number
  const response1 = await client.beta.messages.create({
    model: "claude-opus-4-7",
    betas: ["code-execution-2025-08-25"],
    max_tokens: 4096,
    messages: [
      {
        role: "user",
        content: "Write a file with a random number and save it to '/tmp/number.txt'"
      }
    ],
    tools: [
      {
        type: "code_execution_20250825",
        name: "code_execution"
      }
    ]
  });

  // Extract the container ID from the first response
  const containerId = response1.container!.id;

  // Second request: Reuse the container to read the file
  const response2 = await client.beta.messages.create({
    container: containerId,
    model: "claude-opus-4-7",
    betas: ["code-execution-2025-08-25"],
    max_tokens: 4096,
    messages: [
      {
        role: "user",
        content: "Read the number from '/tmp/number.txt' and calculate its square"
      }
    ],
    tools: [
      {
        type: "code_execution_20250825",
        name: "code_execution"
      }
    ]
  });

  console.log(response2.content);
}

main().catch(console.error);
```

```csharp C# hidelines={1..11,-2..}
using Anthropic;
using Anthropic.Models.Messages;
using System;
using System.Threading.Tasks;

class Program
{
    static async Task Main()
    {
        AnthropicClient client = new();

        var parameters1 = new MessageCreateParams
        {
            Model = Model.ClaudeOpus4_7,
            MaxTokens = 4096,
            Messages = [new() { Role = Role.User, Content = "Write a file with a random number and save it to '/tmp/number.txt'" }],
            Tools = [new ToolUnion(new CodeExecutionTool20250825())]
        };

        var response1 = await client.Messages.Create(parameters1);
        var containerId = response1.Container!.ID;

        var parameters2 = new MessageCreateParams
        {
            Container = containerId,
            Model = Model.ClaudeOpus4_7,
            MaxTokens = 4096,
            Messages = [new() { Role = Role.User, Content = "Read the number from '/tmp/number.txt' and calculate its square" }],
            Tools = [new ToolUnion(new CodeExecutionTool20250825())]
        };

        var response2 = await client.Messages.Create(parameters2);
        Console.WriteLine(response2);
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

	response1, err := client.Beta.Messages.New(context.TODO(), anthropic.BetaMessageNewParams{
		Model:     anthropic.ModelClaudeOpus4_7,
		MaxTokens: 4096,
		Messages: []anthropic.BetaMessageParam{
			anthropic.NewBetaUserMessage(anthropic.NewBetaTextBlock("Write a file with a random number and save it to '/tmp/number.txt'")),
		},
		Tools: []anthropic.BetaToolUnionParam{
			{OfCodeExecutionTool20250825: &anthropic.BetaCodeExecutionTool20250825Param{}},
		},
		Betas: []anthropic.AnthropicBeta{"code-execution-2025-08-25"},
	})
	if err != nil {
		log.Fatal(err)
	}

	containerID := response1.Container.ID

	response2, err := client.Beta.Messages.New(context.TODO(), anthropic.BetaMessageNewParams{
		Container: anthropic.BetaMessageNewParamsContainerUnion{
			OfString: anthropic.String(containerID),
		},
		Model:     anthropic.ModelClaudeOpus4_7,
		MaxTokens: 4096,
		Messages: []anthropic.BetaMessageParam{
			anthropic.NewBetaUserMessage(anthropic.NewBetaTextBlock("Read the number from '/tmp/number.txt' and calculate its square")),
		},
		Tools: []anthropic.BetaToolUnionParam{
			{OfCodeExecutionTool20250825: &anthropic.BetaCodeExecutionTool20250825Param{}},
		},
		Betas: []anthropic.AnthropicBeta{"code-execution-2025-08-25"},
	})
	if err != nil {
		log.Fatal(err)
	}

	for _, block := range response2.Content {
		if block.Type == "text" {
			fmt.Println(block.Text)
		}
	}
}
```

```java Java hidelines={1..5,7..9,-2..}
import com.anthropic.client.AnthropicClient;
import com.anthropic.client.okhttp.AnthropicOkHttpClient;
import com.anthropic.models.messages.MessageCreateParams;
import com.anthropic.models.messages.Message;
import com.anthropic.models.messages.Model;
import com.anthropic.models.messages.CodeExecutionTool20250825;

public class ContainerReuse {
    public static void main(String[] args) {
        AnthropicClient client = AnthropicOkHttpClient.fromEnv();

        MessageCreateParams params1 = MessageCreateParams.builder()
            .model(Model.CLAUDE_OPUS_4_7)
            .maxTokens(4096L)
            .addUserMessage("Write a file with a random number and save it to '/tmp/number.txt'")
            .addTool(CodeExecutionTool20250825.builder().build())
            .build();

        Message response1 = client.messages().create(params1);
        String containerId = response1.container().get().id();

        MessageCreateParams params2 = MessageCreateParams.builder()
            .container(containerId)
            .model(Model.CLAUDE_OPUS_4_7)
            .maxTokens(4096L)
            .addUserMessage("Read the number from '/tmp/number.txt' and calculate its square")
            .addTool(CodeExecutionTool20250825.builder().build())
            .build();

        Message response2 = client.messages().create(params2);
        System.out.println(response2);
    }
}
```

```php PHP hidelines={1..4}
<?php

use Anthropic\Client;

$client = new Client(apiKey: getenv("ANTHROPIC_API_KEY"));

$response1 = $client->messages->create(
    maxTokens: 4096,
    messages: [
        ['role' => 'user', 'content' => "Write a file with a random number and save it to '/tmp/number.txt'"]
    ],
    model: 'claude-opus-4-7',
    tools: [
        ['type' => 'code_execution_20250825', 'name' => 'code_execution']
    ],
);

$containerId = $response1->container->id;

$response2 = $client->messages->create(
    container: $containerId,
    maxTokens: 4096,
    messages: [
        ['role' => 'user', 'content' => "Read the number from '/tmp/number.txt' and calculate its square"]
    ],
    model: 'claude-opus-4-7',
    tools: [
        ['type' => 'code_execution_20250825', 'name' => 'code_execution']
    ],
);
```

```ruby Ruby hidelines={1..2}
require "anthropic"

client = Anthropic::Client.new

response1 = client.messages.create(
  model: "claude-opus-4-7",
  max_tokens: 4096,
  messages: [
    { role: "user", content: "Write a file with a random number and save it to '/tmp/number.txt'" }
  ],
  tools: [
    { type: "code_execution_20250825", name: "code_execution" }
  ]
)

container_id = response1.container.id

response2 = client.messages.create(
  container: container_id,
  model: "claude-opus-4-7",
  max_tokens: 4096,
  messages: [
    { role: "user", content: "Read the number from '/tmp/number.txt' and calculate its square" }
  ],
  tools: [
    { type: "code_execution_20250825", name: "code_execution" }
  ]
)

puts response2.content
```
</CodeGroup>

## Streaming

With streaming enabled, you'll receive code execution events as they occur:

```sse
event: content_block_start
data: {"type": "content_block_start", "index": 1, "content_block": {"type": "server_tool_use", "id": "srvtoolu_xyz789", "name": "code_execution"}}

// Code execution streamed
event: content_block_delta
data: {"type": "content_block_delta", "index": 1, "delta": {"type": "input_json_delta", "partial_json": "{\"code\":\"import pandas as pd\\ndf = pd.read_csv('data.csv')\\nprint(df.head())\"}"}}

// Pause while code executes

// Execution results streamed
event: content_block_start
data: {"type": "content_block_start", "index": 2, "content_block": {"type": "code_execution_tool_result", "tool_use_id": "srvtoolu_xyz789", "content": {"stdout": "   A  B  C\n0  1  2  3\n1  4  5  6", "stderr": ""}}}
```

## Batch requests

You can include the code execution tool in the [Messages Batches API](/docs/en/build-with-claude/batch-processing). Code execution tool calls through the Messages Batches API are priced the same as those in regular Messages API requests.

## Usage and pricing

**Code execution is free when used with web search or web fetch.** When `web_search_20260209` or `web_fetch_20260209` is included in your API request, there are no additional charges for code execution tool calls beyond the standard input and output token costs.

When used without these tools, code execution is billed by execution time, tracked separately from token usage:

- Execution time has a minimum of 5 minutes
- Each organization receives **1,550 free hours** of usage per month
- Additional usage beyond 1,550 hours is billed at **$0.05 per hour, per container**
- If files are included in the request, execution time is billed even if the tool is not invoked, due to files being preloaded onto the container

Code execution usage is tracked in the response:

```json
"usage": {
  "input_tokens": 105,
  "output_tokens": 239,
  "server_tool_use": {
    "code_execution_requests": 1
  }
}
```

## Upgrade to latest tool version

By upgrading to `code-execution-2025-08-25`, you get access to file manipulation and Bash capabilities, including code in multiple languages. There is no price difference.

### What's changed

| Component | Legacy | Current |
|-----------|------------------|----------------------------|
| Beta header | `code-execution-2025-05-22` | `code-execution-2025-08-25` |
| Tool type | `code_execution_20250522` | `code_execution_20250825` |
| Capabilities | Python only | Bash commands, file operations |
| Response types | `code_execution_result` | `bash_code_execution_result`, `text_editor_code_execution_result` |

### Backward compatibility

- All existing Python code execution continues to work exactly as before
- No changes required to existing Python-only workflows

### Upgrade steps

To upgrade, update the tool type in your API requests:

```diff
- "type": "code_execution_20250522"
+ "type": "code_execution_20250825"
```

**Review response handling** (if parsing responses programmatically):
- The previous blocks for Python execution responses will no longer be sent
- Instead, new response types for Bash and file operations will be sent (see Response Format section)

## Programmatic tool calling

For running tools inside the code execution container, see [Programmatic tool calling](/docs/en/agents-and-tools/tool-use/programmatic-tool-calling).

## Data retention

Code execution runs in server-side sandbox containers. Container data, including execution artifacts, uploaded files, and outputs, is retained for up to 30 days. This retention applies to all data processed within the container environment. Files that code execution creates in the [Files API](/docs/en/build-with-claude/files) (retrievable via `client.beta.files.download()`) persist until explicitly deleted.

For ZDR eligibility across all features, see [API and data retention](/docs/en/build-with-claude/api-and-data-retention).

## Using code execution with Agent Skills

The code execution tool enables Claude to use [Agent Skills](/docs/en/agents-and-tools/agent-skills/overview). Skills are modular capabilities consisting of instructions, scripts, and resources that extend Claude's functionality.

Learn more in the [Agent Skills documentation](/docs/en/agents-and-tools/agent-skills/overview) and [Agent Skills API guide](/docs/en/build-with-claude/skills-guide).