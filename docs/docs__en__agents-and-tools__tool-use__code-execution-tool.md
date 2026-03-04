# Code execution tool

---

Claude can analyze data, create visualizations, perform complex calculations, run system commands, create and edit files, and process uploaded files directly within the API conversation. The code execution tool allows Claude to run Bash commands and manipulate files, including writing code, in a secure, sandboxed environment.

**Code execution is free when used with web search or web fetch.** When `web_search_20260209` or `web_fetch_20260209` is included in your request, there are no additional charges for code execution tool calls beyond the standard input and output token costs. Standard code execution charges apply when these tools are not included.

Code execution is a core primitive for building high-performance agents. It enables dynamic filtering in web search and web fetch tools, allowing Claude to process results before they reach the context window—improving accuracy while reducing token consumption.

<Note>
Reach out through the [feedback form](https://forms.gle/LTAU6Xn2puCJMi1n6) to share your feedback on this feature.
</Note>

<Note>
This feature is **not** covered by [Zero Data Retention (ZDR)](/docs/en/build-with-claude/zero-data-retention) arrangements. Data is retained according to the feature's standard retention policy.
</Note>

## Model compatibility

The code execution tool is available on the following models:

| Model | Tool Version |
|-------|--------------|
| Claude Opus 4.6 (`claude-opus-4-6`) | `code_execution_20250825` |
| Claude Sonnet 4.6 (`claude-sonnet-4-6`) | `code_execution_20250825` |
| Claude Sonnet 4.5 (`claude-sonnet-4-5-20250929`) | `code_execution_20250825` |
| Claude Opus 4.5 (`claude-opus-4-5-20251101`) | `code_execution_20250825` |
| Claude Opus 4.1 (`claude-opus-4-1-20250805`) | `code_execution_20250825` |
| Claude Opus 4 (`claude-opus-4-20250514`) | `code_execution_20250825` |
| Claude Sonnet 4 (`claude-sonnet-4-20250514`) | `code_execution_20250825` |
| Claude Sonnet 3.7 (`claude-3-7-sonnet-20250219`) ([deprecated](/docs/en/about-claude/model-deprecations)) | `code_execution_20250825` |
| Claude Haiku 4.5 (`claude-haiku-4-5-20251001`) | `code_execution_20250825` |
| Claude Haiku 3.5 (`claude-3-5-haiku-latest`) ([deprecated](/docs/en/about-claude/model-deprecations)) | `code_execution_20250825` |

<Note>
The current version `code_execution_20250825` supports Bash commands and file operations. A legacy version `code_execution_20250522` (Python only) is also available. See [Upgrade to latest tool version](#upgrade-to-latest-tool-version) for migration details.
</Note>

<Warning>
Older tool versions are not guaranteed to be backwards-compatible with newer models. Always use the tool version that corresponds to your model version.
</Warning>

## Platform availability

Code execution is available on:
- **Claude API** (Anthropic)
- **Microsoft Azure AI Foundry**

Code execution is not currently available on Amazon Bedrock or Google Vertex AI.

## Quick start

Here's a simple example that asks Claude to perform a calculation:

<CodeGroup>
```bash Shell
curl https://api.anthropic.com/v1/messages \
    --header "x-api-key: $ANTHROPIC_API_KEY" \
    --header "anthropic-version: 2023-06-01" \
    --header "content-type: application/json" \
    --data '{
        "model": "claude-opus-4-6",
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

```python Python
import anthropic

client = anthropic.Anthropic()

response = client.messages.create(
    model="claude-opus-4-6",
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

```typescript TypeScript hidelines={1..4}
import Anthropic from "@anthropic-ai/sdk";

const client = new Anthropic();

async function main() {
  const response = await client.messages.create({
    model: "claude-opus-4-6",
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

```csharp C# hidelines={1..10,-1}
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
            Model = Model.ClaudeOpus4_6,
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

### Execute Bash commands

Ask Claude to check system information and install packages:

<CodeGroup>
```bash Shell
curl https://api.anthropic.com/v1/messages \
    --header "x-api-key: $ANTHROPIC_API_KEY" \
    --header "anthropic-version: 2023-06-01" \
    --header "content-type: application/json" \
    --data '{
        "model": "claude-opus-4-6",
        "max_tokens": 4096,
        "messages": [{
            "role": "user",
            "content": "Check the Python version and list installed packages"
        }],
        "tools": [{
            "type": "code_execution_20250825",
            "name": "code_execution"
        }]
    }'
```

```python Python
response = client.messages.create(
    model="claude-opus-4-6",
    max_tokens=4096,
    messages=[
        {
            "role": "user",
            "content": "Check the Python version and list installed packages",
        }
    ],
    tools=[{"type": "code_execution_20250825", "name": "code_execution"}],
)
```

```typescript TypeScript
const response = await client.messages.create({
  model: "claude-opus-4-6",
  max_tokens: 4096,
  messages: [
    {
      role: "user",
      content: "Check the Python version and list installed packages"
    }
  ],
  tools: [
    {
      type: "code_execution_20250825",
      name: "code_execution"
    }
  ]
});
```

```csharp C# hidelines={1..10,-1}
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
            Model = Model.ClaudeOpus4_6,
            MaxTokens = 4096,
            Messages = [new() { Role = Role.User, Content = "Check the Python version and list installed packages" }],
            Tools = [new ToolUnion(new CodeExecutionTool20250825())]
        };

        var message = await client.Messages.Create(parameters);
        Console.WriteLine(message);
    }
}
```
</CodeGroup>

### Create and edit files directly

Claude can create, view, and edit files directly in the sandbox using the file manipulation capabilities:

<CodeGroup>
```bash Shell
curl https://api.anthropic.com/v1/messages \
    --header "x-api-key: $ANTHROPIC_API_KEY" \
    --header "anthropic-version: 2023-06-01" \
    --header "content-type: application/json" \
    --data '{
        "model": "claude-opus-4-6",
        "max_tokens": 4096,
        "messages": [{
            "role": "user",
            "content": "Create a config.yaml file with database settings, then update the port from 5432 to 3306"
        }],
        "tools": [{
            "type": "code_execution_20250825",
            "name": "code_execution"
        }]
    }'
```

```python Python
response = client.messages.create(
    model="claude-opus-4-6",
    max_tokens=4096,
    messages=[
        {
            "role": "user",
            "content": "Create a config.yaml file with database settings, then update the port from 5432 to 3306",
        }
    ],
    tools=[{"type": "code_execution_20250825", "name": "code_execution"}],
)
```

```typescript TypeScript
const response = await client.messages.create({
  model: "claude-opus-4-6",
  max_tokens: 4096,
  messages: [
    {
      role: "user",
      content:
        "Create a config.yaml file with database settings, then update the port from 5432 to 3306"
    }
  ],
  tools: [
    {
      type: "code_execution_20250825",
      name: "code_execution"
    }
  ]
});
```

```csharp C# hidelines={1..10,-1}
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
            Model = Model.ClaudeOpus4_6,
            MaxTokens = 4096,
            Messages = [new() { Role = Role.User, Content = "Create a config.yaml file with database settings, then update the port from 5432 to 3306" }],
            Tools = [new ToolUnion(new CodeExecutionTool20250825())]
        };

        var message = await client.Messages.Create(parameters);
        Console.WriteLine(message);
    }
}
```
</CodeGroup>

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
```bash Shell
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
        "model": "claude-opus-4-6",
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

```python Python nocheck hidelines={1..4}
import anthropic

client = anthropic.Anthropic()

# Upload a file
file_object = client.beta.files.upload(
    file=open("data.csv", "rb"),
)

# Use the file_id with code execution
response = client.beta.messages.create(
    model="claude-opus-4-6",
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
```

```typescript TypeScript nocheck
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
    model: "claude-opus-4-6",
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

```csharp C# nocheck hidelines={1..9,-1}
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
            Model = Model.ClaudeOpus4_6,
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
</CodeGroup>

#### Retrieve generated files

When Claude creates files during code execution, you can retrieve these files using the Files API:

<CodeGroup>

```python Python nocheck hidelines={1..5}
from anthropic import Anthropic

# Initialize the client
client = Anthropic()

# Request code execution that creates files
response = client.beta.messages.create(
    model="claude-opus-4-6",
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
                for file in content_item.content:
                    if hasattr(file, "file_id"):
                        file_ids.append(file.file_id)
    return file_ids


# Download the created files
for file_id in extract_file_ids(response):
    file_metadata = client.beta.files.retrieve_metadata(file_id)
    file_content = client.beta.files.download(file_id)
    file_content.write_to_file(file_metadata.filename)
    print(f"Downloaded: {file_metadata.filename}")
```

```typescript TypeScript hidelines={1}
import Anthropic from "@anthropic-ai/sdk";
import { writeFile } from "fs/promises";

const client = new Anthropic();

async function main() {
  // Request code execution that creates files
  const response = await client.beta.messages.create({
    model: "claude-opus-4-6",
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

```csharp C# nocheck hidelines={1..13,-1}
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
            Model = Model.ClaudeOpus4_6,
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
</CodeGroup>

### Combine operations

A complex workflow using all capabilities:

<CodeGroup>
```bash Shell
# First, upload a file
curl https://api.anthropic.com/v1/files \
    --header "x-api-key: $ANTHROPIC_API_KEY" \
    --header "anthropic-version: 2023-06-01" \
    --header "anthropic-beta: files-api-2025-04-14" \
    --form 'file=@"data.csv"' \
    > file_response.json

# Extract file_id (using jq)
FILE_ID=$(jq -r '.id' file_response.json)

# Then use it with code execution
curl https://api.anthropic.com/v1/messages \
    --header "x-api-key: $ANTHROPIC_API_KEY" \
    --header "anthropic-version: 2023-06-01" \
    --header "anthropic-beta: files-api-2025-04-14" \
    --header "content-type: application/json" \
    --data '{
        "model": "claude-opus-4-6",
        "max_tokens": 4096,
        "messages": [{
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": "Analyze this CSV data: create a summary report, save visualizations, and create a README with the findings"
                },
                {
                    "type": "container_upload",
                    "file_id": "'$FILE_ID'"
                }
            ]
        }],
        "tools": [{
            "type": "code_execution_20250825",
            "name": "code_execution"
        }]
    }'
```

```python Python nocheck
# Upload a file
file_object = client.beta.files.upload(
    file=open("data.csv", "rb"),
)

# Use it with code execution
response = client.beta.messages.create(
    model="claude-opus-4-6",
    betas=["files-api-2025-04-14"],
    max_tokens=4096,
    messages=[
        {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": "Analyze this CSV data: create a summary report, save visualizations, and create a README with the findings",
                },
                {"type": "container_upload", "file_id": file_object.id},
            ],
        }
    ],
    tools=[{"type": "code_execution_20250825", "name": "code_execution"}],
)

# Claude might:
# 1. Use bash to check file size and preview data
# 2. Use text_editor to write Python code to analyze the CSV and create visualizations
# 3. Use bash to run the Python code
# 4. Use text_editor to create a README.md with findings
# 5. Use bash to organize files into a report directory
```

```typescript TypeScript nocheck
import Anthropic, { toFile } from "@anthropic-ai/sdk";
import { createReadStream } from "fs";

const client = new Anthropic();

async function main() {
  // Upload a file
  const fileObject = await client.beta.files.upload({
    file: await toFile(createReadStream("data.csv"), undefined, { type: "text/csv" }),
    betas: ["files-api-2025-04-14"]
  });

  const response = await client.beta.messages.create({
    model: "claude-opus-4-6",
    betas: ["code-execution-2025-08-25", "files-api-2025-04-14"],
    max_tokens: 4096,
    messages: [
      {
        role: "user",
        content: [
          {
            type: "text",
            text: "Analyze this CSV data: create a summary report, save visualizations, and create a README with the findings"
          },
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

```csharp C# nocheck
using System;
using System.IO;
using System.Threading.Tasks;
using Anthropic;
using Anthropic.Models.Beta.Files;
using Anthropic.Models.Beta.Messages;

class Program
{
    static async Task Main(string[] args)
    {
        AnthropicClient client = new();

        var fileObject = await client.Beta.Files.Upload(new FileUploadParams
        {
            File = File.OpenRead("data.csv")
        });

        var parameters = new MessageCreateParams
        {
            Model = "claude-opus-4-6",
            Betas = ["files-api-2025-04-14"],
            MaxTokens = 4096,
            Messages = [
                new() {
                    Role = Role.User,
                    Content = [
                        new BetaTextBlockParam {
                            Text = "Analyze this CSV data: create a summary report, save visualizations, and create a README with the findings"
                        },
                        new BetaContainerUploadBlockParam {
                            FileID = fileObject.Id
                        }
                    ]
                }
            ],
            Tools = [
                new BetaTool {
                    Type = "code_execution_20250825",
                    Name = "code_execution"
                }
            ]
        };

        var message = await client.Beta.Messages.Create(parameters);
        Console.WriteLine(message);
    }
}
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

```json hidelines={1,-1}
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
```json hidelines={1,-1}
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
```json hidelines={1,-1}
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
```json hidelines={1,-1}
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
```json
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
```bash Shell
# First request: Create a file with a random number
curl https://api.anthropic.com/v1/messages \
    --header "x-api-key: $ANTHROPIC_API_KEY" \
    --header "anthropic-version: 2023-06-01" \
    --header "content-type: application/json" \
    --data '{
        "model": "claude-opus-4-6",
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
        "model": "claude-opus-4-6",
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

```python Python hidelines={1..5}
import os
from anthropic import Anthropic

# Initialize the client
client = Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))

# First request: Create a file with a random number
response1 = client.messages.create(
    model="claude-opus-4-6",
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
    model="claude-opus-4-6",
    max_tokens=4096,
    messages=[
        {
            "role": "user",
            "content": "Read the number from '/tmp/number.txt' and calculate its square",
        }
    ],
    tools=[{"type": "code_execution_20250825", "name": "code_execution"}],
)
```

```typescript TypeScript hidelines={1..4}
import Anthropic from "@anthropic-ai/sdk";

const client = new Anthropic();

async function main() {
  // First request: Create a file with a random number
  const response1 = await client.beta.messages.create({
    model: "claude-opus-4-6",
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
    model: "claude-opus-4-6",
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

```csharp C# nocheck hidelines={1..10,-1}
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
            Model = Model.ClaudeOpus4_6,
            MaxTokens = 4096,
            Messages = [new() { Role = Role.User, Content = "Write a file with a random number and save it to '/tmp/number.txt'" }],
            Tools = [new ToolUnion(new CodeExecutionTool20250825())]
        };

        var response1 = await client.Messages.Create(parameters1);
        var containerId = response1.Container.Id;

        var parameters2 = new MessageCreateParams
        {
            Container = containerId,
            Model = Model.ClaudeOpus4_6,
            MaxTokens = 4096,
            Messages = [new() { Role = Role.User, Content = "Read the number from '/tmp/number.txt' and calculate its square" }],
            Tools = [new ToolUnion(new CodeExecutionTool20250825())]
        };

        var response2 = await client.Messages.Create(parameters2);
        Console.WriteLine(response2);
    }
}
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

The code execution tool powers [programmatic tool calling](/docs/en/agents-and-tools/tool-use/programmatic-tool-calling), which allows Claude to write code that calls your custom tools programmatically within the execution container. This enables efficient multi-tool workflows, data filtering before reaching Claude's context, and complex conditional logic.

<CodeGroup>

```python Python nocheck
# Enable programmatic calling for your tools
response = client.messages.create(
    model="claude-opus-4-6",
    max_tokens=4096,
    messages=[
        {"role": "user", "content": "Get weather for 5 cities and find the warmest"}
    ],
    tools=[
        {"type": "code_execution_20250825", "name": "code_execution"},
        {
            "name": "get_weather",
            "description": "Get weather for a city",
            "input_schema": {...},
            "allowed_callers": [
                "code_execution_20250825"
            ],  # Enable programmatic calling
        },
    ],
)
```

```typescript TypeScript hidelines={1..4}
import Anthropic from "@anthropic-ai/sdk";

const client = new Anthropic();

async function main() {
  const response = await client.beta.messages.create({
    model: "claude-opus-4-6",
    betas: ["code-execution-2025-08-25"],
    max_tokens: 4096,
    messages: [{ role: "user", content: "Get weather for 5 cities and find the warmest" }],
    tools: [
      { type: "code_execution_20250825", name: "code_execution" },
      {
        name: "get_weather",
        description: "Get weather for a city",
        input_schema: {
          type: "object" as const,
          properties: {
            city: { type: "string" }
          },
          required: ["city"]
        },
        allowed_callers: ["code_execution_20250825"]
      }
    ]
  });

  console.log(response);
}

main().catch(console.error);
```

```csharp C# nocheck
using Anthropic;
using Anthropic.Models.Messages;
using System;
using System.Collections.Generic;
using System.Threading.Tasks;

class Program
{
    static async Task Main(string[] args)
    {
        AnthropicClient client = new();

        var parameters = new MessageCreateParams
        {
            Model = Model.ClaudeOpus4_6,
            MaxTokens = 4096,
            Messages = [new() { Role = Role.User, Content = "Get weather for 5 cities and find the warmest" }],
            Tools = new List<Tool>
            {
                new() { Type = "code_execution_20250825", Name = "code_execution" },
                new()
                {
                    Name = "get_weather",
                    Description = "Get weather for a city",
                    InputSchema = new
                    {
                        type = "object",
                        properties = new
                        {
                            city = new { type = "string" }
                        },
                        required = new[] { "city" }
                    },
                    AllowedCallers = new[] { "code_execution_20250825" }
                }
            }
        };

        var message = await client.Messages.Create(parameters);
        Console.WriteLine(message);
    }
}
```
</CodeGroup>

Learn more in the [Programmatic tool calling documentation](/docs/en/agents-and-tools/tool-use/programmatic-tool-calling).

## Using code execution with Agent Skills

The code execution tool enables Claude to use [Agent Skills](/docs/en/agents-and-tools/agent-skills/overview). Skills are modular capabilities consisting of instructions, scripts, and resources that extend Claude's functionality.

Learn more in the [Agent Skills documentation](/docs/en/agents-and-tools/agent-skills/overview) and [Agent Skills API guide](/docs/en/build-with-claude/skills-guide).