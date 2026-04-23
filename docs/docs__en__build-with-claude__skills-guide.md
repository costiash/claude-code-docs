# Using Agent Skills with the API

Learn how to use Agent Skills to extend Claude's capabilities through the API.

---

Agent Skills extend Claude's capabilities through organized folders of instructions, scripts, and resources. This guide shows you how to use both pre-built and custom Skills with the Claude API.

<Note>
For complete API reference including request/response schemas and all parameters, see:
- [Skill Management API Reference](/docs/en/api/skills/list-skills) - CRUD operations for Skills
- [Skill Versions API Reference](/docs/en/api/skills/list-skill-versions) - Version management
</Note>

<Note>
This feature is **not** eligible for [Zero Data Retention (ZDR)](/docs/en/build-with-claude/api-and-data-retention). Data is retained according to the feature's standard retention policy.
</Note>

## Quick Links

<CardGroup cols={2}>
  <Card
    title="Get started with Agent Skills"
    icon="rocket"
    href="/docs/en/agents-and-tools/agent-skills/quickstart"
  >
    Create your first Skill
  </Card>
  <Card
    title="Create Custom Skills"
    icon="hammer"
    href="/docs/en/agents-and-tools/agent-skills/best-practices"
  >
    Best practices for authoring Skills
  </Card>
</CardGroup>

## Overview

<Note>
For a deep dive into the architecture and real-world applications of Agent Skills, read the engineering blog post: [Equipping agents for the real world with Agent Skills](https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills).
</Note>

Skills integrate with the Messages API through the code execution tool. Whether using pre-built Skills managed by Anthropic or custom Skills you've uploaded, the integration shape is identical: both require code execution and use the same `container` structure.

### Using Skills

Skills integrate identically in the Messages API regardless of source. You specify Skills in the `container` parameter with a `skill_id`, `type`, and optional `version`, and they execute in the code execution environment.

**You can use Skills from two sources:**

| Aspect | Anthropic Skills | Custom Skills |
|--------|------------------|---------------|
| **Type value** | `anthropic` | `custom` |
| **Skill IDs** | Short names: `pptx`, `xlsx`, `docx`, `pdf` | Generated: `skill_01AbCdEfGhIjKlMnOpQrStUv` |
| **Version format** | Date-based: `20251013` or `latest` | Epoch timestamp: `1759178010641129` or `latest` |
| **Management** | Pre-built and maintained by Anthropic | Upload and manage via [Skills API](/docs/en/api/skills/create-skill) |
| **Availability** | Available to all users | Private to your workspace |

Both skill sources are returned by the [List Skills endpoint](/docs/en/api/skills/list-skills) (use the `source` parameter to filter). The integration shape and execution environment are identical. The only difference is where the Skills come from and how they're managed.

### Prerequisites

To use Skills, you need:

1. **Claude API key** from the [Console](/settings/keys)
2. **Beta headers:**
   - `code-execution-2025-08-25` - Enables code execution (required for Skills)
   - `skills-2025-10-02` - Enables Skills API
   - `files-api-2025-04-14` - For uploading/downloading files to/from container
3. **Code execution tool** enabled in your requests

---

## Using Skills in Messages

### Container Parameter

Skills are specified using the `container` parameter in the Messages API. You can include up to 8 Skills per request.

The structure is identical for both Anthropic and custom Skills. Specify the required `type` and `skill_id`, and optionally include `version` to pin to a specific version:

<CodeGroup>
```bash cURL
curl https://api.anthropic.com/v1/messages \
  -H "x-api-key: $ANTHROPIC_API_KEY" \
  -H "anthropic-version: 2023-06-01" \
  -H "anthropic-beta: code-execution-2025-08-25,skills-2025-10-02" \
  -H "content-type: application/json" \
  -d '{
    "model": "claude-opus-4-7",
    "max_tokens": 4096,
    "container": {
      "skills": [
        {
          "type": "anthropic",
          "skill_id": "pptx",
          "version": "latest"
        }
      ]
    },
    "messages": [{
      "role": "user",
      "content": "Create a presentation about renewable energy"
    }],
    "tools": [{
      "type": "code_execution_20250825",
      "name": "code_execution"
    }]
  }'
```

```bash CLI
ant beta:messages create \
  --beta code-execution-2025-08-25 \
  --beta skills-2025-10-02 <<'YAML'
model: claude-opus-4-7
max_tokens: 4096
container:
  skills:
    - type: anthropic
      skill_id: pptx
      version: latest
messages:
  - role: user
    content: Create a presentation about renewable energy
tools:
  - type: code_execution_20250825
    name: code_execution
YAML
```

```python Python nocheck hidelines={1..2}
import anthropic

client = anthropic.Anthropic()

response = client.beta.messages.create(
    model="claude-opus-4-7",
    max_tokens=4096,
    betas=["code-execution-2025-08-25", "skills-2025-10-02"],
    container={
        "skills": [{"type": "anthropic", "skill_id": "pptx", "version": "latest"}]
    },
    messages=[
        {"role": "user", "content": "Create a presentation about renewable energy"}
    ],
    tools=[{"type": "code_execution_20250825", "name": "code_execution"}],
)
```

```typescript TypeScript hidelines={1..2}
import Anthropic from "@anthropic-ai/sdk";

const client = new Anthropic();

const response = await client.beta.messages.create({
  model: "claude-opus-4-7",
  max_tokens: 4096,
  betas: ["code-execution-2025-08-25", "skills-2025-10-02"],
  container: {
    skills: [
      {
        type: "anthropic",
        skill_id: "pptx",
        version: "latest"
      }
    ]
  },
  messages: [
    {
      role: "user",
      content: "Create a presentation about renewable energy"
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

```csharp C# nocheck
using System;
using System.Threading.Tasks;
using Anthropic;
using Anthropic.Models.Beta.Messages;

public class Program
{
    public static async Task Main(string[] args)
    {
        AnthropicClient client = new();

        var parameters = new MessageCreateParams
        {
            Model = "claude-opus-4-7",
            MaxTokens = 4096,
            Betas = new[] { "code-execution-2025-08-25", "skills-2025-10-02" },
            Container = new BetaContainerParams
            {
                Skills = new[]
                {
                    new BetaAnthropicSkillParams
                    {
                        Type = "anthropic",
                        SkillId = "pptx",
                        Version = "latest"
                    }
                }
            },
            Messages = new[]
            {
                new BetaMessageParam
                {
                    Role = Role.User,
                    Content = "Create a presentation about renewable energy"
                }
            },
            Tools = new[]
            {
                new BetaCodeExecutionToolParams
                {
                    Type = "code_execution_20250825",
                    Name = "code_execution"
                }
            }
        };

        var message = await client.Beta.Messages.Create(parameters);
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
		Model:     "claude-opus-4-7",
		MaxTokens: 4096,
		Betas: []anthropic.AnthropicBeta{
			"code-execution-2025-08-25",
			anthropic.AnthropicBetaSkills2025_10_02,
		},
		Container: anthropic.BetaMessageNewParamsContainerUnion{
			OfContainers: &anthropic.BetaContainerParams{
				Skills: []anthropic.BetaSkillParams{
					{
						Type:    anthropic.BetaSkillParamsTypeAnthropic,
						SkillID: "pptx",
						Version: anthropic.String("latest"),
					},
				},
			},
		},
		Messages: []anthropic.BetaMessageParam{
			anthropic.NewBetaUserMessage(anthropic.NewBetaTextBlock("Create a presentation about renewable energy")),
		},
		Tools: []anthropic.BetaToolUnionParam{
			{OfCodeExecutionTool20250825: &anthropic.BetaCodeExecutionTool20250825Param{}},
		},
	})
	if err != nil {
		log.Fatal(err)
	}
	fmt.Println(response)
}
```

```java Java hidelines={1..4,8..10,-2..}
import com.anthropic.client.AnthropicClient;
import com.anthropic.client.okhttp.AnthropicOkHttpClient;
import com.anthropic.models.beta.messages.MessageCreateParams;
import com.anthropic.models.beta.messages.BetaMessage;
import com.anthropic.models.beta.messages.BetaContainerParams;
import com.anthropic.models.beta.messages.BetaSkillParams;
import com.anthropic.models.beta.messages.BetaCodeExecutionTool20250825;

public class Main {
    public static void main(String[] args) {
        AnthropicClient client = AnthropicOkHttpClient.fromEnv();

        MessageCreateParams params = MessageCreateParams.builder()
            .model("claude-opus-4-7")
            .maxTokens(4096L)
            .addBeta("code-execution-2025-08-25")
            .addBeta("skills-2025-10-02")
            .container(BetaContainerParams.builder()
                .addSkill(BetaSkillParams.builder()
                    .type(BetaSkillParams.Type.ANTHROPIC)
                    .skillId("pptx")
                    .version("latest")
                    .build())
                .build())
            .addUserMessage("Create a presentation about renewable energy")
            .addTool(BetaCodeExecutionTool20250825.builder().build())
            .build();

        BetaMessage response = client.beta().messages().create(params);
        System.out.println(response);
    }
}
```

```php PHP hidelines={1..4}
<?php

use Anthropic\Client;

$client = new Client(apiKey: getenv("ANTHROPIC_API_KEY"));

$message = $client->beta->messages->create(
    maxTokens: 4096,
    messages: [
        ['role' => 'user', 'content' => 'Create a presentation about renewable energy']
    ],
    model: 'claude-opus-4-7',
    betas: ['code-execution-2025-08-25', 'skills-2025-10-02'],
    container: [
        'skills' => [
            [
                'type' => 'anthropic',
                'skill_id' => 'pptx',
                'version' => 'latest'
            ]
        ]
    ],
    tools: [
        ['type' => 'code_execution_20250825', 'name' => 'code_execution']
    ]
);

echo $message;
```

```ruby Ruby hidelines={1..2}
require "anthropic"

client = Anthropic::Client.new

message = client.beta.messages.create(
  model: "claude-opus-4-7",
  max_tokens: 4096,
  betas: ["code-execution-2025-08-25", "skills-2025-10-02"],
  container: {
    skills: [
      {
        type: "anthropic",
        skill_id: "pptx",
        version: "latest"
      }
    ]
  },
  messages: [
    { role: "user", content: "Create a presentation about renewable energy" }
  ],
  tools: [
    { type: "code_execution_20250825", name: "code_execution" }
  ]
)
puts message
```
</CodeGroup>

### Downloading Generated Files

When Skills create documents (Excel, PowerPoint, PDF, Word), they return `file_id` attributes in the response. You must use the Files API to download these files.

**How it works:**
1. Skills create files during code execution
2. Response includes `file_id` for each created file
3. Use Files API to download the actual file content
4. Save locally or process as needed

**Example: Creating and downloading an Excel file**

<Tabs>
<Tab title="cURL">

```bash cURL hidelines={1}
cd "$(mktemp -d)"
# Step 1: Use a Skill to create a file
RESPONSE=$(curl https://api.anthropic.com/v1/messages \
  -H "x-api-key: $ANTHROPIC_API_KEY" \
  -H "anthropic-version: 2023-06-01" \
  -H "anthropic-beta: code-execution-2025-08-25,skills-2025-10-02" \
  -H "content-type: application/json" \
  -d '{
    "model": "claude-opus-4-7",
    "max_tokens": 4096,
    "container": {
      "skills": [
        {"type": "anthropic", "skill_id": "xlsx", "version": "latest"}
      ]
    },
    "messages": [{
      "role": "user",
      "content": "Create an Excel file with a simple budget spreadsheet"
    }],
    "tools": [{
      "type": "code_execution_20250825",
      "name": "code_execution"
    }]
  }')

# Step 2: Extract file_id from response (using jq)
FILE_ID=$(echo "$RESPONSE" | jq -r '.content[] | select(.type=="bash_code_execution_tool_result") | .content | select(.type=="bash_code_execution_result") | .content[] | select(.file_id) | .file_id')

# Step 3: Get filename from metadata
FILENAME=$(curl "https://api.anthropic.com/v1/files/$FILE_ID" \
  -H "x-api-key: $ANTHROPIC_API_KEY" \
  -H "anthropic-version: 2023-06-01" \
  -H "anthropic-beta: files-api-2025-04-14" | jq -r '.filename')

# Step 4: Download the file using Files API
curl "https://api.anthropic.com/v1/files/$FILE_ID/content" \
  -H "x-api-key: $ANTHROPIC_API_KEY" \
  -H "anthropic-version: 2023-06-01" \
  -H "anthropic-beta: files-api-2025-04-14" \
  --output "$FILENAME"

echo "Downloaded: $FILENAME"
```

</Tab>
<Tab title="CLI">

```bash CLI nocheck hidelines={1}
cd "$(mktemp -d)"
# Step 1: Use the xlsx Skill to create a file
# Step 2: Extract file_id from the response via --transform (GJSON path)
FILE_ID=$(ant beta:messages create \
  --beta code-execution-2025-08-25 \
  --beta skills-2025-10-02 \
  --transform 'content.#.content.content.#.file_id|@flatten|0' \
  --format yaml <<'YAML'
model: claude-opus-4-7
max_tokens: 4096
container:
  skills:
    - type: anthropic
      skill_id: xlsx
      version: latest
messages:
  - role: user
    content: Create an Excel file with a simple budget spreadsheet
tools:
  - type: code_execution_20250825
    name: code_execution
YAML
)

# Step 3: Get the filename from file metadata
FILENAME=$(ant beta:files retrieve-metadata \
  --file-id "$FILE_ID" \
  --transform filename --format yaml)

# Step 4: Download the file using Files API
ant beta:files download \
  --file-id "$FILE_ID" \
  --output "$FILENAME" > /dev/null

printf 'Downloaded: %s\n' "$FILENAME"
```

</Tab>
<Tab title="Python">

```python Python nocheck hidelines={1..2}
import anthropic

client = anthropic.Anthropic()

# Step 1: Use a Skill to create a file
response = client.beta.messages.create(
    model="claude-opus-4-7",
    max_tokens=4096,
    betas=["code-execution-2025-08-25", "skills-2025-10-02"],
    container={
        "skills": [{"type": "anthropic", "skill_id": "xlsx", "version": "latest"}]
    },
    messages=[
        {
            "role": "user",
            "content": "Create an Excel file with a simple budget spreadsheet",
        }
    ],
    tools=[{"type": "code_execution_20250825", "name": "code_execution"}],
)


# Step 2: Extract file IDs from the response
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


# Step 3: Download the file using Files API
for file_id in extract_file_ids(response):
    file_metadata = client.beta.files.retrieve_metadata(file_id=file_id)
    file_content = client.beta.files.download(file_id=file_id)

    # Step 4: Save to disk
    file_content.write_to_file(file_metadata.filename)
    print(f"Downloaded: {file_metadata.filename}")
```

</Tab>
<Tab title="TypeScript">

```typescript TypeScript hidelines={1..3}
import Anthropic from "@anthropic-ai/sdk";
import fs from "node:fs/promises";

const client = new Anthropic();

// Step 1: Use a Skill to create a file
const response = await client.beta.messages.create({
  model: "claude-opus-4-7",
  max_tokens: 4096,
  betas: ["code-execution-2025-08-25", "skills-2025-10-02"],
  container: {
    skills: [{ type: "anthropic", skill_id: "xlsx", version: "latest" }]
  },
  messages: [
    {
      role: "user",
      content: "Create an Excel file with a simple budget spreadsheet"
    }
  ],
  tools: [{ type: "code_execution_20250825", name: "code_execution" }]
});

// Step 2: Extract file IDs from the response
function extractFileIds(response: any): string[] {
  const fileIds: string[] = [];
  for (const item of response.content) {
    if (item.type === "bash_code_execution_tool_result") {
      const contentItem = item.content;
      if (contentItem.type === "bash_code_execution_result") {
        for (const file of contentItem.content) {
          if ("file_id" in file) {
            fileIds.push(file.file_id);
          }
        }
      }
    }
  }
  return fileIds;
}

// Step 3: Download the file using Files API
for (const fileId of extractFileIds(response)) {
  const fileMetadata = await client.beta.files.retrieveMetadata(fileId);
  const fileContent = await client.beta.files.download(fileId);

  // Step 4: Save to disk
  await fs.writeFile(fileMetadata.filename, Buffer.from(await fileContent.arrayBuffer()));
  console.log(`Downloaded: ${fileMetadata.filename}`);
}
```

</Tab>
<Tab title="C#">

```csharp C# nocheck
using System;
using System.IO;
using System.Linq;
using System.Threading.Tasks;
using System.Collections.Generic;
using Anthropic;
using Anthropic.Models.Beta.Messages;
using Anthropic.Models.Beta.Files;

class Program
{
    static async Task Main(string[] args)
    {
        AnthropicClient client = new();

        // Step 1: Use a Skill to create a file
        var parameters = new MessageCreateParams
        {
            Model = "claude-opus-4-7",
            MaxTokens = 4096,
            Betas = new[] { "code-execution-2025-08-25", "skills-2025-10-02" },
            Container = new BetaContainer
            {
                Skills = new[]
                {
                    new BetaSkill
                    {
                        Type = "anthropic",
                        SkillId = "xlsx",
                        Version = "latest"
                    }
                }
            },
            Messages = new[]
            {
                new BetaMessage
                {
                    Role = Role.User,
                    Content = "Create an Excel file with a simple budget spreadsheet"
                }
            },
            Tools = new[]
            {
                new BetaTool
                {
                    Type = "code_execution_20250825",
                    Name = "code_execution"
                }
            }
        };

        var response = await client.Beta.Messages.Create(parameters);

        // Step 2: Extract file IDs from the response
        var fileIds = ExtractFileIds(response);

        // Step 3: Download the file using Files API
        foreach (var fileId in fileIds)
        {
            var fileMetadata = await client.Beta.Files.RetrieveMetadata(fileId);

            var fileContent = await client.Beta.Files.Download(fileId);

            // Step 4: Save to disk
            await File.WriteAllBytesAsync(fileMetadata.Filename, fileContent);
            Console.WriteLine($"Downloaded: {fileMetadata.Filename}");
        }
    }

    static List<string> ExtractFileIds(BetaMessage response)
    {
        var fileIds = new List<string>();
        foreach (var item in response.Content)
        {
            if (item is BetaBashCodeExecutionToolResult toolResult)
            {
                if (toolResult.Content is BetaBashCodeExecutionResult result)
                {
                    foreach (var content in result.Content)
                    {
                        if (content is BetaBashCodeExecutionResultFile file)
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

</Tab>
<Tab title="Go">

```go Go hidelines={1..15,68..69}
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

	// Step 1: Use a Skill to create a file
	response, err := client.Beta.Messages.New(context.TODO(), anthropic.BetaMessageNewParams{
		Model:     "claude-opus-4-7",
		MaxTokens: 4096,
		Betas:     []anthropic.AnthropicBeta{"code-execution-2025-08-25", anthropic.AnthropicBetaSkills2025_10_02},
		Container: anthropic.BetaMessageNewParamsContainerUnion{
			OfContainers: &anthropic.BetaContainerParams{
				Skills: []anthropic.BetaSkillParams{
					{
						Type:    anthropic.BetaSkillParamsTypeAnthropic,
						SkillID: "xlsx",
						Version: anthropic.String("latest"),
					},
				},
			},
		},
		Messages: []anthropic.BetaMessageParam{
			anthropic.NewBetaUserMessage(anthropic.NewBetaTextBlock("Create an Excel file with a simple budget spreadsheet")),
		},
		Tools: []anthropic.BetaToolUnionParam{
			{OfCodeExecutionTool20250825: &anthropic.BetaCodeExecutionTool20250825Param{}},
		},
	})
	if err != nil {
		log.Fatal(err)
	}

	// Step 2: Extract file IDs from the response
	fileIDs := extractFileIDs(response)

	// Step 3: Download the file using Files API
	for _, fileID := range fileIDs {
		fileMetadata, err := client.Beta.Files.GetMetadata(context.TODO(), fileID, anthropic.BetaFileGetMetadataParams{})
		if err != nil {
			log.Fatal(err)
		}

		fileContent, err := client.Beta.Files.Download(context.TODO(), fileID, anthropic.BetaFileDownloadParams{})
		if err != nil {
			log.Fatal(err)
		}

		// Step 4: Save to disk
		out, err := os.Create(fileMetadata.Filename)
		if err != nil {
			log.Fatal(err)
		}
		io.Copy(out, fileContent.Body)
		out.Close()
		fileContent.Body.Close()
		fmt.Printf("Downloaded: %s\n", fileMetadata.Filename)
	}
}

func extractFileIDs(response *anthropic.BetaMessage) []string {
	var fileIDs []string
	for _, item := range response.Content {
		switch v := item.AsAny().(type) {
		case anthropic.BetaBashCodeExecutionToolResultBlock:
			for _, output := range v.Content.Content {
				if output.FileID != "" {
					fileIDs = append(fileIDs, output.FileID)
				}
			}
		}
	}
	return fileIDs
}
```

</Tab>
<Tab title="Java">

```java Java nocheck hidelines={1..4,8,10..17,-2..}
import com.anthropic.client.AnthropicClient;
import com.anthropic.client.okhttp.AnthropicOkHttpClient;
import com.anthropic.models.beta.messages.MessageCreateParams;
import com.anthropic.models.beta.messages.BetaMessage;
import com.anthropic.models.beta.messages.BetaContainerParams;
import com.anthropic.models.beta.messages.BetaSkillParams;
import com.anthropic.models.beta.messages.BetaCodeExecutionTool20250825;
import com.anthropic.models.beta.messages.BetaContentBlock;
import com.anthropic.models.beta.files.FileMetadata;
import com.anthropic.core.http.HttpResponse;
import java.io.FileOutputStream;
import java.io.InputStream;
import java.util.ArrayList;
import java.util.List;

public class SkillsFileDownload {
    public static void main(String[] args) throws Exception {
        AnthropicClient client = AnthropicOkHttpClient.fromEnv();

        // Step 1: Use a Skill to create a file
        MessageCreateParams params = MessageCreateParams.builder()
            .model("claude-opus-4-7")
            .maxTokens(4096L)
            .addBeta("code-execution-2025-08-25")
            .addBeta("skills-2025-10-02")
            .container(BetaContainerParams.builder()
                .addSkill(BetaSkillParams.builder()
                    .type(BetaSkillParams.Type.ANTHROPIC)
                    .skillId("xlsx")
                    .version("latest")
                    .build())
                .build())
            .addUserMessage("Create an Excel file with a simple budget spreadsheet")
            .addTool(BetaCodeExecutionTool20250825.builder().build())
            .build();

        BetaMessage response = client.beta().messages().create(params);

        // Step 2: Extract file IDs from the response
        List<String> fileIds = new ArrayList<>();
        for (BetaContentBlock block : response.content()) {
            if (block.isCodeExecutionToolResult()) {
                var toolResult = block.asCodeExecutionToolResult();
                for (var content : toolResult.content()) {
                    content.file().ifPresent(file -> fileIds.add(file.fileId()));
                }
            }
        }

        // Step 3: Download the file using Files API
        for (String fileId : fileIds) {
            FileMetadata fileMetadata = client.beta().files().retrieveMetadata(fileId);
            HttpResponse fileContent = client.beta().files().download(fileId);

            // Step 4: Save to disk
            try (InputStream is = fileContent.body();
                 FileOutputStream fos = new FileOutputStream(fileMetadata.filename())) {
                is.transferTo(fos);
            }
            System.out.println("Downloaded: " + fileMetadata.filename());
        }
    }
}
```

</Tab>
<Tab title="PHP">

<Note>
The PHP SDK doesn't include a file download method. Use `retrieveMetadata()` for file info, then download the file content via the REST API.
</Note>

```php PHP nocheck hidelines={1..4}
<?php

use Anthropic\Client;

$client = new Client(apiKey: getenv("ANTHROPIC_API_KEY"));

// Step 1: Use a Skill to create a file
$response = $client->beta->messages->create(
    maxTokens: 4096,
    messages: [
        ['role' => 'user', 'content' => 'Create an Excel file with a simple budget spreadsheet']
    ],
    model: 'claude-opus-4-7',
    betas: ['code-execution-2025-08-25', 'skills-2025-10-02'],
    container: [
        'skills' => [
            ['type' => 'anthropic', 'skill_id' => 'xlsx', 'version' => 'latest']
        ]
    ],
    tools: [
        ['type' => 'code_execution_20250825', 'name' => 'code_execution']
    ]
);

// Step 2: Extract file IDs from the response
function extractFileIds($response) {
    $fileIds = [];
    foreach ($response->content as $item) {
        if ($item->type === 'bash_code_execution_tool_result') {
            $contentItem = $item->content;
            if ($contentItem->type === 'bash_code_execution_result') {
                foreach ($contentItem->content as $file) {
                    if (isset($file->fileID)) {
                        $fileIds[] = $file->fileID;
                    }
                }
            }
        }
    }
    return $fileIds;
}

// Step 3: Get metadata and download via REST API
$apiKey = getenv("ANTHROPIC_API_KEY");
foreach (extractFileIds($response) as $fileId) {
    $fileMetadata = $client->beta->files->retrieveMetadata(
        fileID: $fileId,
    );

    // Download file content via REST API
    $context = stream_context_create([
        'http' => [
            'header' => implode("\r\n", [
                "x-api-key: $apiKey",
                "anthropic-version: 2023-06-01",
                "anthropic-beta: files-api-2025-04-14",
            ]),
        ],
    ]);
    $fileContent = file_get_contents(
        "https://api.anthropic.com/v1/files/$fileId/content",
        false,
        $context
    );

    // Step 4: Save to disk
    file_put_contents($fileMetadata->filename, $fileContent);
    echo "Downloaded: {$fileMetadata->filename}\n";
}
```

</Tab>
<Tab title="Ruby">

```ruby Ruby nocheck hidelines={1..2}
require "anthropic"

client = Anthropic::Client.new

# Step 1: Use a Skill to create a file
response = client.beta.messages.create(
  model: "claude-opus-4-7",
  max_tokens: 4096,
  betas: ["code-execution-2025-08-25", "skills-2025-10-02"],
  container: {
    skills: [{ type: "anthropic", skill_id: "xlsx", version: "latest" }]
  },
  messages: [
    {
      role: "user",
      content: "Create an Excel file with a simple budget spreadsheet"
    }
  ],
  tools: [{ type: "code_execution_20250825", name: "code_execution" }]
)

# Step 2: Extract file IDs from the response
def extract_file_ids(response)
  file_ids = []
  response.content.each do |item|
    if item.type == :bash_code_execution_tool_result
      content_item = item.content
      if content_item.type == :bash_code_execution_result
        content_item.content.each do |file|
          file_ids << file.file_id if file.respond_to?(:file_id)
        end
      end
    end
  end
  file_ids
end

# Step 3: Download the file using Files API
extract_file_ids(response).each do |file_id|
  file_metadata = client.beta.files.retrieve_metadata(file_id)

  file_content = client.beta.files.download(file_id)

  # Step 4: Save to disk
  File.binwrite(file_metadata.filename, file_content.read)
  puts "Downloaded: #{file_metadata.filename}"
end
```

</Tab>
</Tabs>

**Additional Files API operations:**

<CodeGroup>
```bash cURL
# Get file metadata
curl "https://api.anthropic.com/v1/files/$FILE_ID" \
  -H "x-api-key: $ANTHROPIC_API_KEY" \
  -H "anthropic-version: 2023-06-01" \
  -H "anthropic-beta: files-api-2025-04-14"

# List all files
curl "https://api.anthropic.com/v1/files" \
  -H "x-api-key: $ANTHROPIC_API_KEY" \
  -H "anthropic-version: 2023-06-01" \
  -H "anthropic-beta: files-api-2025-04-14"

# Delete a file
curl -X DELETE "https://api.anthropic.com/v1/files/$FILE_ID" \
  -H "x-api-key: $ANTHROPIC_API_KEY" \
  -H "anthropic-version: 2023-06-01" \
  -H "anthropic-beta: files-api-2025-04-14"
```

```bash CLI nocheck
# Get file metadata
ant beta:files retrieve-metadata --file-id "$FILE_ID" \
  --transform '{filename,size_bytes}' --format yaml \
  | { read -r _ name; read -r _ size
      printf 'Filename: %s, Size: %s bytes\n' "$name" "$size"; }

# List all files
ant beta:files list \
  --transform '{filename,created_at}' --format yaml \
  | while read -r _ name && read -r _ date; do
      printf '%s - %s\n' "$name" "${date//\"/}"
    done

# Delete a file
ant beta:files delete --file-id "$FILE_ID" >/dev/null
```

```python Python nocheck hidelines={1..2}
import anthropic

client = anthropic.Anthropic()
file_id = "file_abc123"
# Get file metadata
file_info = client.beta.files.retrieve_metadata(file_id=file_id)
print(f"Filename: {file_info.filename}, Size: {file_info.size_bytes} bytes")

# List all files
files = client.beta.files.list()
for file in files.data:
    print(f"{file.filename} - {file.created_at}")

# Delete a file
client.beta.files.delete(file_id=file_id)
```

```typescript TypeScript nocheck hidelines={1..2}
import Anthropic from "@anthropic-ai/sdk";

const client = new Anthropic();
const fileId = "file_011CNha8iCJcU1wXNR6q4V8w";

// Get file metadata
const fileInfo = await client.beta.files.retrieveMetadata(fileId);
console.log(`Filename: ${fileInfo.filename}, Size: ${fileInfo.size_bytes} bytes`);

// List all files
const files = await client.beta.files.list();
for (const file of files.data) {
  console.log(`${file.filename} - ${file.created_at}`);
}

// Delete a file
await client.beta.files.delete(fileId);
```

```csharp C# nocheck
using System;
using System.Threading.Tasks;
using Anthropic;
using Anthropic.Models.Beta.Files;

class Program
{
    static async Task Main(string[] args)
    {
        AnthropicClient client = new();
        string fileId = "file_abc123";

        // Get file metadata
        var fileInfo = await client.Beta.Files.RetrieveMetadata(fileId);
        Console.WriteLine($"Filename: {fileInfo.Filename}, Size: {fileInfo.SizeBytes} bytes");

        // List all files
        var files = await client.Beta.Files.List();
        foreach (var file in files.Data)
        {
            Console.WriteLine($"{file.Filename} - {file.CreatedAt}");
        }

        // Delete a file
        await client.Beta.Files.Delete(fileId);
    }
}
```

```go Go nocheck hidelines={1..11,-1}
package main

import (
	"context"
	"fmt"
	"log"

	"github.com/anthropics/anthropic-sdk-go"
)

func main() {
	client := anthropic.NewClient()
	fileID := "file_abc123"

	// Get file metadata
	fileInfo, err := client.Beta.Files.GetMetadata(context.TODO(), fileID, anthropic.BetaFileGetMetadataParams{})
	if err != nil {
		log.Fatal(err)
	}
	fmt.Printf("Filename: %s, Size: %d bytes\n", fileInfo.Filename, fileInfo.SizeBytes)

	// List all files
	files := client.Beta.Files.ListAutoPaging(context.TODO(), anthropic.BetaFileListParams{})
	for files.Next() {
		file := files.Current()
		fmt.Printf("%s - %s\n", file.Filename, file.CreatedAt)
	}

	// Delete a file
	_, err = client.Beta.Files.Delete(context.TODO(), fileID, anthropic.BetaFileDeleteParams{})
	if err != nil {
		log.Fatal(err)
	}
}
```

```java Java nocheck hidelines={1..2,5..7,-2..}
import com.anthropic.client.AnthropicClient;
import com.anthropic.client.okhttp.AnthropicOkHttpClient;
import com.anthropic.models.beta.files.FileMetadata;
import com.anthropic.models.beta.files.FileListPage;

public class FileManagement {
    public static void main(String[] args) {
        AnthropicClient client = AnthropicOkHttpClient.fromEnv();
        String fileId = "file_abc123";

        // Get file metadata
        FileMetadata fileInfo = client.beta().files().retrieveMetadata(fileId);
        System.out.println("Filename: " + fileInfo.filename() + ", Size: " + fileInfo.sizeBytes() + " bytes");

        // List all files
        FileListPage files = client.beta().files().list();
        for (var file : files.data()) {
            System.out.println(file.filename() + " - " + file.createdAt());
        }

        // Delete a file
        client.beta().files().delete(fileId);
    }
}
```

```php PHP hidelines={1..4} nocheck
<?php

use Anthropic\Client;

$client = new Client(apiKey: getenv("ANTHROPIC_API_KEY"));
$fileId = "file_abc123";

// Get file metadata
$fileInfo = $client->beta->files->retrieveMetadata(
    fileID: $fileId,
);
echo "Filename: {$fileInfo->filename}, Size: {$fileInfo->sizeBytes} bytes\n";

// List all files
$files = $client->beta->files->list();
foreach ($files->data as $file) {
    echo "{$file->filename} - {$file->createdAt}\n";
}

// Delete a file
$client->beta->files->delete(
    fileID: $fileId,
);
```

```ruby Ruby nocheck hidelines={1..2}
require "anthropic"

client = Anthropic::Client.new
file_id = "file_abc123"

# Get file metadata
file_info = client.beta.files.retrieve_metadata(file_id)
puts "Filename: #{file_info.filename}, Size: #{file_info.size_bytes} bytes"

# List all files
files = client.beta.files.list
files.data.each do |file|
  puts "#{file.filename} - #{file.created_at}"
end

# Delete a file
client.beta.files.delete(file_id)
```
</CodeGroup>

<Note>
For complete details on the Files API, see the [Files API documentation](/docs/en/api/files-content).
</Note>

### Multi-Turn Conversations

Reuse the same container across multiple messages by specifying the container ID:

<CodeGroup>
```bash CLI
# First request creates container
CONTAINER_ID=$(ant beta:messages create \
  --beta code-execution-2025-08-25 --beta skills-2025-10-02 \
  --transform container.id --format yaml <<'YAML'
model: claude-opus-4-7
max_tokens: 4096
container:
  skills:
    - {type: anthropic, skill_id: xlsx, version: latest}
messages:
  - role: user
    content: Analyze this sales data
tools:
  - {type: code_execution_20250825, name: code_execution}
YAML
)

# Continue conversation with same container
ant beta:messages create \
  --beta code-execution-2025-08-25 --beta skills-2025-10-02 <<YAML
model: claude-opus-4-7
max_tokens: 4096
container:
  id: $CONTAINER_ID  # Reuse container
  skills:
    - {type: anthropic, skill_id: xlsx, version: latest}
messages:
  - role: user
    content: Analyze this sales data
  - role: assistant
    content: []  # content blocks from the first response
  - role: user
    content: What was the total revenue?
tools:
  - {type: code_execution_20250825, name: code_execution}
YAML
```

```python Python
# First request creates container
response1 = client.beta.messages.create(
    model="claude-opus-4-7",
    max_tokens=4096,
    betas=["code-execution-2025-08-25", "skills-2025-10-02"],
    container={
        "skills": [{"type": "anthropic", "skill_id": "xlsx", "version": "latest"}]
    },
    messages=[{"role": "user", "content": "Analyze this sales data"}],
    tools=[{"type": "code_execution_20250825", "name": "code_execution"}],
)

# Continue conversation with same container
messages = [
    {"role": "user", "content": "Analyze this sales data"},
    {"role": "assistant", "content": response1.content},
    {"role": "user", "content": "What was the total revenue?"},
]

response2 = client.beta.messages.create(
    model="claude-opus-4-7",
    max_tokens=4096,
    betas=["code-execution-2025-08-25", "skills-2025-10-02"],
    container={
        "id": response1.container.id,  # Reuse container
        "skills": [{"type": "anthropic", "skill_id": "xlsx", "version": "latest"}],
    },
    messages=messages,
    tools=[{"type": "code_execution_20250825", "name": "code_execution"}],
)
```

```typescript TypeScript
// First request creates container
const response1 = await client.beta.messages.create({
  model: "claude-opus-4-7",
  max_tokens: 4096,
  betas: ["code-execution-2025-08-25", "skills-2025-10-02"],
  container: {
    skills: [{ type: "anthropic", skill_id: "xlsx", version: "latest" }]
  },
  messages: [{ role: "user", content: "Analyze this sales data" }],
  tools: [{ type: "code_execution_20250825", name: "code_execution" }]
});

// Continue conversation with same container
const messages: Anthropic.Beta.Messages.BetaMessageParam[] = [
  { role: "user", content: "Analyze this sales data" },
  {
    role: "assistant",
    content: response1.content as Anthropic.Beta.Messages.BetaContentBlockParam[]
  },
  { role: "user", content: "What was the total revenue?" }
];

const response2 = await client.beta.messages.create({
  model: "claude-opus-4-7",
  max_tokens: 4096,
  betas: ["code-execution-2025-08-25", "skills-2025-10-02"],
  container: {
    id: response1.container!.id, // Reuse container
    skills: [{ type: "anthropic", skill_id: "xlsx", version: "latest" }]
  },
  messages,
  tools: [{ type: "code_execution_20250825", name: "code_execution" }]
});
```

```csharp C# nocheck
using System;
using System.Threading.Tasks;
using Anthropic;
using Anthropic.Models.Beta.Messages;

public class Program
{
    public static async Task Main()
    {
        var client = new AnthropicClient();

        var parameters1 = new MessageCreateParams
        {
            Model = "claude-opus-4-7",
            MaxTokens = 4096,
            Betas = new[] { "code-execution-2025-08-25", "skills-2025-10-02" },
            Container = new BetaContainerParams
            {
                Skills = new[]
                {
                    new BetaSkillParam
                    {
                        Type = "anthropic",
                        SkillId = "xlsx",
                        Version = "latest"
                    }
                }
            },
            Messages = new[]
            {
                new BetaMessageParam
                {
                    Role = Role.User,
                    Content = "Analyze this sales data"
                }
            },
            Tools = new[]
            {
                new BetaToolParam
                {
                    Type = "code_execution_20250825",
                    Name = "code_execution"
                }
            }
        };

        var response1 = await client.Beta.Messages.Create(parameters1);

        var parameters2 = new MessageCreateParams
        {
            Model = "claude-opus-4-7",
            MaxTokens = 4096,
            Betas = new[] { "code-execution-2025-08-25", "skills-2025-10-02" },
            Container = new BetaContainerParams
            {
                Id = response1.Container.Id,
                Skills = new[]
                {
                    new BetaSkillParam
                    {
                        Type = "anthropic",
                        SkillId = "xlsx",
                        Version = "latest"
                    }
                }
            },
            Messages = new[]
            {
                new BetaMessageParam { Role = Role.User, Content = "Analyze this sales data" },
                new BetaMessageParam { Role = Role.Assistant, Content = response1.Content },
                new BetaMessageParam { Role = Role.User, Content = "What was the total revenue?" }
            },
            Tools = new[]
            {
                new BetaToolParam
                {
                    Type = "code_execution_20250825",
                    Name = "code_execution"
                }
            }
        };

        var response2 = await client.Beta.Messages.Create(parameters2);
        Console.WriteLine(response2);
    }
}
```

```go Go nocheck hidelines={1..11,-1}
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
		Model:     "claude-opus-4-7",
		MaxTokens: 4096,
		Betas:     []anthropic.AnthropicBeta{"code-execution-2025-08-25", anthropic.AnthropicBetaSkills2025_10_02},
		Container: anthropic.BetaMessageNewParamsContainerUnion{
			OfContainers: &anthropic.BetaContainerParams{
				Skills: []anthropic.BetaSkillParams{
					{
						Type:    anthropic.BetaSkillParamsTypeAnthropic,
						SkillID: "xlsx",
						Version: anthropic.String("latest"),
					},
				},
			},
		},
		Messages: []anthropic.BetaMessageParam{
			anthropic.NewBetaUserMessage(anthropic.NewBetaTextBlock("Analyze this sales data")),
		},
		Tools: []anthropic.BetaToolUnionParam{
			{OfCodeExecutionTool20250825: &anthropic.BetaCodeExecutionTool20250825Param{}},
		},
	})
	if err != nil {
		log.Fatal(err)
	}

	response2, err := client.Beta.Messages.New(context.TODO(), anthropic.BetaMessageNewParams{
		Model:     "claude-opus-4-7",
		MaxTokens: 4096,
		Betas:     []anthropic.AnthropicBeta{"code-execution-2025-08-25", anthropic.AnthropicBetaSkills2025_10_02},
		Container: anthropic.BetaMessageNewParamsContainerUnion{
			OfString: anthropic.String(response1.Container.ID),
		},
		Messages: []anthropic.BetaMessageParam{
			anthropic.NewBetaUserMessage(anthropic.NewBetaTextBlock("Analyze this sales data")),
			response1.ToParam(),
			anthropic.NewBetaUserMessage(anthropic.NewBetaTextBlock("What was the total revenue?")),
		},
		Tools: []anthropic.BetaToolUnionParam{
			{OfCodeExecutionTool20250825: &anthropic.BetaCodeExecutionTool20250825Param{}},
		},
	})
	if err != nil {
		log.Fatal(err)
	}

	fmt.Println(response2)
}
```

```java Java hidelines={1..4,8..10,-2..}
import com.anthropic.client.AnthropicClient;
import com.anthropic.client.okhttp.AnthropicOkHttpClient;
import com.anthropic.models.beta.messages.MessageCreateParams;
import com.anthropic.models.beta.messages.BetaMessage;
import com.anthropic.models.beta.messages.BetaContainerParams;
import com.anthropic.models.beta.messages.BetaSkillParams;
import com.anthropic.models.beta.messages.BetaCodeExecutionTool20250825;

public class ContainerReuse {
    public static void main(String[] args) {
        AnthropicClient client = AnthropicOkHttpClient.fromEnv();

        MessageCreateParams params1 = MessageCreateParams.builder()
            .model("claude-opus-4-7")
            .maxTokens(4096L)
            .addBeta("code-execution-2025-08-25")
            .addBeta("skills-2025-10-02")
            .container(BetaContainerParams.builder()
                .addSkill(BetaSkillParams.builder()
                    .type(BetaSkillParams.Type.ANTHROPIC)
                    .skillId("xlsx")
                    .version("latest")
                    .build())
                .build())
            .addUserMessage("Analyze this sales data")
            .addTool(BetaCodeExecutionTool20250825.builder().build())
            .build();

        BetaMessage response1 = client.beta().messages().create(params1);

        MessageCreateParams params2 = MessageCreateParams.builder()
            .model("claude-opus-4-7")
            .maxTokens(4096L)
            .addBeta("code-execution-2025-08-25")
            .addBeta("skills-2025-10-02")
            .container(BetaContainerParams.builder()
                .id(response1.container().get().id())
                .addSkill(BetaSkillParams.builder()
                    .type(BetaSkillParams.Type.ANTHROPIC)
                    .skillId("xlsx")
                    .version("latest")
                    .build())
                .build())
            .addUserMessage("Analyze this sales data")
            .addMessage(response1)
            .addUserMessage("What was the total revenue?")
            .addTool(BetaCodeExecutionTool20250825.builder().build())
            .build();

        BetaMessage response2 = client.beta().messages().create(params2);
        System.out.println(response2);
    }
}
```

```php PHP hidelines={1..4}
<?php

use Anthropic\Client;

$client = new Client(apiKey: getenv("ANTHROPIC_API_KEY"));

$response1 = $client->beta->messages->create(
    maxTokens: 4096,
    messages: [
        ['role' => 'user', 'content' => 'Analyze this sales data']
    ],
    model: 'claude-opus-4-7',
    betas: ['code-execution-2025-08-25', 'skills-2025-10-02'],
    container: [
        'skills' => [
            ['type' => 'anthropic', 'skill_id' => 'xlsx', 'version' => 'latest']
        ]
    ],
    tools: [
        ['type' => 'code_execution_20250825', 'name' => 'code_execution']
    ]
);

$messages = [
    ['role' => 'user', 'content' => 'Analyze this sales data'],
    ['role' => 'assistant', 'content' => $response1->content],
    ['role' => 'user', 'content' => 'What was the total revenue?']
];

$response2 = $client->beta->messages->create(
    maxTokens: 4096,
    messages: $messages,
    model: 'claude-opus-4-7',
    betas: ['code-execution-2025-08-25', 'skills-2025-10-02'],
    container: [
        'id' => $response1->container->id,
        'skills' => [
            ['type' => 'anthropic', 'skill_id' => 'xlsx', 'version' => 'latest']
        ]
    ],
    tools: [
        ['type' => 'code_execution_20250825', 'name' => 'code_execution']
    ]
);

echo $response2;
```

```ruby Ruby hidelines={1..2}
require "anthropic"

client = Anthropic::Client.new

response1 = client.beta.messages.create(
  model: "claude-opus-4-7",
  max_tokens: 4096,
  betas: ["code-execution-2025-08-25", "skills-2025-10-02"],
  container: {
    skills: [{ type: "anthropic", skill_id: "xlsx", version: "latest" }]
  },
  messages: [
    { role: "user", content: "Analyze this sales data" }
  ],
  tools: [
    { type: "code_execution_20250825", name: "code_execution" }
  ]
)

messages = [
  { role: "user", content: "Analyze this sales data" },
  { role: "assistant", content: response1.content },
  { role: "user", content: "What was the total revenue?" }
]

response2 = client.beta.messages.create(
  model: "claude-opus-4-7",
  max_tokens: 4096,
  betas: ["code-execution-2025-08-25", "skills-2025-10-02"],
  container: {
    id: response1.container.id,
    skills: [
      { type: "anthropic", skill_id: "xlsx", version: "latest" }
    ]
  },
  messages: messages,
  tools: [
    { type: "code_execution_20250825", name: "code_execution" }
  ]
)

puts response2
```
</CodeGroup>

### Long-Running Operations

Skills may perform operations that require multiple turns. Handle `pause_turn` stop reasons:

<CodeGroup>

```bash cURL nocheck
# Initial request
RESPONSE=$(curl https://api.anthropic.com/v1/messages \
  -H "x-api-key: $ANTHROPIC_API_KEY" \
  -H "anthropic-version: 2023-06-01" \
  -H "anthropic-beta: code-execution-2025-08-25,skills-2025-10-02" \
  -H "content-type: application/json" \
  -d '{
    "model": "claude-opus-4-7",
    "max_tokens": 4096,
    "container": {
      "skills": [
        {
          "type": "custom",
          "skill_id": "skill_01AbCdEfGhIjKlMnOpQrStUv",
          "version": "latest"
        }
      ]
    },
    "messages": [{
      "role": "user",
      "content": "Process this large dataset"
    }],
    "tools": [{
      "type": "code_execution_20250825",
      "name": "code_execution"
    }]
  }')

# Check stop_reason and handle pause_turn in a loop
STOP_REASON=$(echo "$RESPONSE" | jq -r '.stop_reason')
CONTAINER_ID=$(echo "$RESPONSE" | jq -r '.container.id')

while [ "$STOP_REASON" = "pause_turn" ]; do
  # Continue with same container
  RESPONSE=$(curl https://api.anthropic.com/v1/messages \
    -H "x-api-key: $ANTHROPIC_API_KEY" \
    -H "anthropic-version: 2023-06-01" \
    -H "anthropic-beta: code-execution-2025-08-25,skills-2025-10-02" \
    -H "content-type: application/json" \
    -d "{
      \"model\": \"claude-opus-4-7\",
      \"max_tokens\": 4096,
      \"container\": {
        \"id\": \"$CONTAINER_ID\",
        \"skills\": [{
          \"type\": \"custom\",
          \"skill_id\": \"skill_01AbCdEfGhIjKlMnOpQrStUv\",
          \"version\": \"latest\"
        }]
      },
      \"messages\": [/* include conversation history */],
      \"tools\": [{
        \"type\": \"code_execution_20250825\",
        \"name\": \"code_execution\"
      }]
    }")

  STOP_REASON=$(echo "$RESPONSE" | jq -r '.stop_reason')
done
```

```bash CLI nocheck
RESP=$(mktemp)

# Initial request: capture the full JSON response to a temp file
ant beta:messages create \
  --beta code-execution-2025-08-25 \
  --beta skills-2025-10-02 \
 > "$RESP" <<'YAML'
model: claude-opus-4-7
max_tokens: 4096
container:
  skills:
    - type: custom
      skill_id: skill_01AbCdEfGhIjKlMnOpQrStUv
      version: latest
messages:
  - role: user
    content: Process this large dataset
tools:
  - type: code_execution_20250825
    name: code_execution
YAML

# Handle pause_turn for long operations (up to 10 iterations)
for _ in {1..10}; do
  [[ $(jq -r '.stop_reason' "$RESP") == pause_turn ]] || break

  CONTAINER_ID=$(jq -r '.container.id' "$RESP")

  # Continue in the same container, appending the prior response's
  # content array to messages as the assistant turn.
  ant beta:messages create \
    --beta code-execution-2025-08-25 \
    --beta skills-2025-10-02 \
 > "$RESP" <<YAML
model: claude-opus-4-7
max_tokens: 4096
container:
  id: $CONTAINER_ID
  skills:
    - type: custom
      skill_id: skill_01AbCdEfGhIjKlMnOpQrStUv
      version: latest
messages:
  # ... conversation history with prior assistant content appended
tools:
  - type: code_execution_20250825
    name: code_execution
YAML
done
```

```python Python nocheck
messages = [{"role": "user", "content": "Process this large dataset"}]
max_retries = 10

response = client.beta.messages.create(
    model="claude-opus-4-7",
    max_tokens=4096,
    betas=["code-execution-2025-08-25", "skills-2025-10-02"],
    container={
        "skills": [
            {
                "type": "custom",
                "skill_id": "skill_01AbCdEfGhIjKlMnOpQrStUv",
                "version": "latest",
            }
        ]
    },
    messages=messages,
    tools=[{"type": "code_execution_20250825", "name": "code_execution"}],
)

# Handle pause_turn for long operations
for i in range(max_retries):
    if response.stop_reason != "pause_turn":
        break

    messages.append({"role": "assistant", "content": response.content})
    response = client.beta.messages.create(
        model="claude-opus-4-7",
        max_tokens=4096,
        betas=["code-execution-2025-08-25", "skills-2025-10-02"],
        container={
            "id": response.container.id,
            "skills": [
                {
                    "type": "custom",
                    "skill_id": "skill_01AbCdEfGhIjKlMnOpQrStUv",
                    "version": "latest",
                }
            ],
        },
        messages=messages,
        tools=[{"type": "code_execution_20250825", "name": "code_execution"}],
    )
```

```typescript TypeScript nocheck hidelines={1..2}
import Anthropic from "@anthropic-ai/sdk";

const client = new Anthropic();
const messages: Anthropic.Beta.Messages.BetaMessageParam[] = [
  { role: "user", content: "Process this large dataset" }
];
const maxRetries = 10;

let response = await client.beta.messages.create({
  model: "claude-opus-4-7",
  max_tokens: 4096,
  betas: ["code-execution-2025-08-25", "skills-2025-10-02"],
  container: {
    skills: [{ type: "custom", skill_id: "skill_01AbCdEfGhIjKlMnOpQrStUv", version: "latest" }]
  },
  messages,
  tools: [{ type: "code_execution_20250825", name: "code_execution" }]
});

// Handle pause_turn for long operations
for (let i = 0; i < maxRetries; i++) {
  if (response.stop_reason !== "pause_turn") {
    break;
  }

  messages.push({
    role: "assistant" as const,
    content: response.content as Anthropic.Beta.Messages.BetaContentBlockParam[]
  });
  response = await client.beta.messages.create({
    model: "claude-opus-4-7",
    max_tokens: 4096,
    betas: ["code-execution-2025-08-25", "skills-2025-10-02"],
    container: {
      id: response.container!.id,
      skills: [
        { type: "custom", skill_id: "skill_01AbCdEfGhIjKlMnOpQrStUv", version: "latest" }
      ]
    },
    messages,
    tools: [{ type: "code_execution_20250825", name: "code_execution" }]
  });
}
```

```csharp C# nocheck
using Anthropic;
using Anthropic.Models.Beta.Messages;

AnthropicClient client = new();

var messages = new List<BetaMessageParam>
{
    new() { Role = Role.User, Content = "Process this large dataset" }
};
int maxRetries = 10;

var response = await client.Beta.Messages.Create(new MessageCreateParams
{
    Model = "claude-opus-4-7",
    MaxTokens = 4096,
    Betas = ["code-execution-2025-08-25", "skills-2025-10-02"],
    Container = new BetaContainerParams
    {
        Skills = [
            new BetaSkillParam
            {
                Type = "custom",
                SkillId = "skill_01AbCdEfGhIjKlMnOpQrStUv",
                Version = "latest"
            }
        ]
    },
    Messages = messages,
    Tools = [new BetaToolParam { Type = "code_execution_20250825", Name = "code_execution" }]
});

for (int i = 0; i < maxRetries; i++)
{
    if (response.StopReason != "pause_turn")
    {
        break;
    }

    messages.Add(new BetaMessageParam { Role = Role.Assistant, Content = response.Content });

    response = await client.Beta.Messages.Create(new MessageCreateParams
    {
        Model = "claude-opus-4-7",
        MaxTokens = 4096,
        Betas = ["code-execution-2025-08-25", "skills-2025-10-02"],
        Container = new BetaContainerParams
        {
            Id = response.Container.Id,
            Skills = [
                new BetaSkillParam
                {
                    Type = "custom",
                    SkillId = "skill_01AbCdEfGhIjKlMnOpQrStUv",
                    Version = "latest"
                }
            ]
        },
        Messages = messages,
        Tools = [new BetaToolParam { Type = "code_execution_20250825", Name = "code_execution" }]
    });
}
```

```go Go nocheck hidelines={1..11,-1}
package main

import (
	"context"
	"fmt"
	"log"

	"github.com/anthropics/anthropic-sdk-go"
)

func main() {
	client := anthropic.NewClient()

	messages := []anthropic.BetaMessageParam{
		anthropic.NewBetaUserMessage(anthropic.NewBetaTextBlock("Process this large dataset")),
	}
	maxRetries := 10

	response, err := client.Beta.Messages.New(context.TODO(), anthropic.BetaMessageNewParams{
		Model:     "claude-opus-4-7",
		MaxTokens: 4096,
		Betas:     []anthropic.AnthropicBeta{"code-execution-2025-08-25", anthropic.AnthropicBetaSkills2025_10_02},
		Container: anthropic.BetaMessageNewParamsContainerUnion{
			OfContainers: &anthropic.BetaContainerParams{
				Skills: []anthropic.BetaSkillParams{
					{
						Type:    anthropic.BetaSkillParamsTypeCustom,
						SkillID: "skill_01AbCdEfGhIjKlMnOpQrStUv",
						Version: anthropic.String("latest"),
					},
				},
			},
		},
		Messages: messages,
		Tools: []anthropic.BetaToolUnionParam{
			{OfCodeExecutionTool20250825: &anthropic.BetaCodeExecutionTool20250825Param{}},
		},
	})
	if err != nil {
		log.Fatal(err)
	}

	for i := 0; i < maxRetries; i++ {
		if response.StopReason != "pause_turn" {
			break
		}

		messages = append(messages, response.ToParam())

		response, err = client.Beta.Messages.New(context.TODO(), anthropic.BetaMessageNewParams{
			Model:     "claude-opus-4-7",
			MaxTokens: 4096,
			Betas:     []anthropic.AnthropicBeta{"code-execution-2025-08-25", anthropic.AnthropicBetaSkills2025_10_02},
			Container: anthropic.BetaMessageNewParamsContainerUnion{
				OfString: anthropic.String(response.Container.ID),
			},
			Messages: messages,
			Tools: []anthropic.BetaToolUnionParam{
				{OfCodeExecutionTool20250825: &anthropic.BetaCodeExecutionTool20250825Param{}},
			},
		})
		if err != nil {
			log.Fatal(err)
		}
	}

	fmt.Println(response)
}
```

```java Java nocheck hidelines={1..5,9..10,12..14,-2..}
import com.anthropic.client.AnthropicClient;
import com.anthropic.client.okhttp.AnthropicOkHttpClient;
import com.anthropic.models.beta.messages.MessageCreateParams;
import com.anthropic.models.beta.messages.BetaMessage;
import com.anthropic.models.beta.messages.BetaMessageParam;
import com.anthropic.models.beta.messages.BetaContainerParams;
import com.anthropic.models.beta.messages.BetaSkillParams;
import com.anthropic.models.beta.messages.BetaCodeExecutionTool20250825;
import java.util.ArrayList;
import java.util.List;
import com.anthropic.models.beta.messages.BetaStopReason;

public class Main {
    public static void main(String[] args) {
        AnthropicClient client = AnthropicOkHttpClient.fromEnv();

        List<BetaMessageParam> messages = new ArrayList<>();
        messages.add(
            BetaMessageParam.builder()
                .role(BetaMessageParam.Role.USER)
                .content("Process this large dataset")
                .build()
        );
        int maxRetries = 10;

        BetaMessage response = client.beta().messages().create(
            MessageCreateParams.builder()
                .model("claude-opus-4-7")
                .maxTokens(4096L)
                .addBeta("code-execution-2025-08-25")
                .addBeta("skills-2025-10-02")
                .container(BetaContainerParams.builder()
                    .addSkill(BetaSkillParams.builder()
                        .type(BetaSkillParams.Type.CUSTOM)
                        .skillId("skill_01AbCdEfGhIjKlMnOpQrStUv")
                        .version("latest")
                        .build())
                    .build())
                .messages(messages)
                .addTool(BetaCodeExecutionTool20250825.builder().build())
                .build());

        for (int i = 0; i < maxRetries; i++) {
            if (!response.stopReason().isPresent()
                    || !response.stopReason().get().equals(BetaStopReason.PAUSE_TURN)) {
                break;
            }

            messages.add(response.toParam());

            response = client.beta().messages().create(
                MessageCreateParams.builder()
                    .model("claude-opus-4-7")
                    .maxTokens(4096L)
                    .addBeta("code-execution-2025-08-25")
                    .addBeta("skills-2025-10-02")
                    .container(BetaContainerParams.builder()
                        .id(response.container().get().id())
                        .addSkill(BetaSkillParams.builder()
                            .type(BetaSkillParams.Type.CUSTOM)
                            .skillId("skill_01AbCdEfGhIjKlMnOpQrStUv")
                            .version("latest")
                            .build())
                        .build())
                    .messages(messages)
                    .addTool(BetaCodeExecutionTool20250825.builder().build())
                    .build());
        }
    }
}
```

```php PHP hidelines={1..4} nocheck
<?php

use Anthropic\Client;

$client = new Client(apiKey: getenv("ANTHROPIC_API_KEY"));

$messages = [
    ['role' => 'user', 'content' => 'Process this large dataset']
];
$maxRetries = 10;

$response = $client->beta->messages->create(
    maxTokens: 4096,
    messages: $messages,
    model: 'claude-opus-4-7',
    betas: ['code-execution-2025-08-25', 'skills-2025-10-02'],
    container: [
        'skills' => [
            [
                'type' => 'custom',
                'skill_id' => 'skill_01AbCdEfGhIjKlMnOpQrStUv',
                'version' => 'latest'
            ]
        ]
    ],
    tools: [['type' => 'code_execution_20250825', 'name' => 'code_execution']]
);

for ($i = 0; $i < $maxRetries; $i++) {
    if ($response->stopReason !== 'pause_turn') {
        break;
    }

    $messages[] = ['role' => 'assistant', 'content' => $response->content];

    $response = $client->beta->messages->create(
        maxTokens: 4096,
        messages: $messages,
        model: 'claude-opus-4-7',
        betas: ['code-execution-2025-08-25', 'skills-2025-10-02'],
        container: [
            'id' => $response->container->id,
            'skills' => [
                [
                    'type' => 'custom',
                    'skill_id' => 'skill_01AbCdEfGhIjKlMnOpQrStUv',
                    'version' => 'latest'
                ]
            ]
        ],
        tools: [['type' => 'code_execution_20250825', 'name' => 'code_execution']]
    );
}
```

```ruby Ruby nocheck hidelines={1..2}
require "anthropic"

client = Anthropic::Client.new

messages = [
  { role: "user", content: "Process this large dataset" }
]
max_retries = 10

response = client.beta.messages.create(
  model: "claude-opus-4-7",
  max_tokens: 4096,
  betas: ["code-execution-2025-08-25", "skills-2025-10-02"],
  container: {
    skills: [
      {
        type: "custom",
        skill_id: "skill_01AbCdEfGhIjKlMnOpQrStUv",
        version: "latest"
      }
    ]
  },
  messages: messages,
  tools: [{ type: "code_execution_20250825", name: "code_execution" }]
)

max_retries.times do
  break if response.stop_reason != :pause_turn

  messages << { role: "assistant", content: response.content }

  response = client.beta.messages.create(
    model: "claude-opus-4-7",
    max_tokens: 4096,
    betas: ["code-execution-2025-08-25", "skills-2025-10-02"],
    container: {
      id: response.container.id,
      skills: [
        {
          type: "custom",
          skill_id: "skill_01AbCdEfGhIjKlMnOpQrStUv",
          version: "latest"
        }
      ]
    },
    messages: messages,
    tools: [{ type: "code_execution_20250825", name: "code_execution" }]
  )
end
```
</CodeGroup>

<Note>
The response may include a `pause_turn` stop reason, which indicates that the API paused a long-running Skill operation. You can provide the response back as-is in a subsequent request to let Claude continue its turn, or modify the content if you wish to interrupt the conversation and provide additional guidance.
</Note>

### Using Multiple Skills

Combine multiple Skills in a single request to handle complex workflows:

<CodeGroup>

```bash cURL nocheck
curl https://api.anthropic.com/v1/messages \
  -H "x-api-key: $ANTHROPIC_API_KEY" \
  -H "anthropic-version: 2023-06-01" \
  -H "anthropic-beta: code-execution-2025-08-25,skills-2025-10-02" \
  -H "content-type: application/json" \
  -d '{
    "model": "claude-opus-4-7",
    "max_tokens": 4096,
    "container": {
      "skills": [
        {
          "type": "anthropic",
          "skill_id": "xlsx",
          "version": "latest"
        },
        {
          "type": "anthropic",
          "skill_id": "pptx",
          "version": "latest"
        },
        {
          "type": "custom",
          "skill_id": "skill_01AbCdEfGhIjKlMnOpQrStUv",
          "version": "latest"
        }
      ]
    },
    "messages": [{
      "role": "user",
      "content": "Analyze sales data and create a presentation"
    }],
    "tools": [{
      "type": "code_execution_20250825",
      "name": "code_execution"
    }]
  }'
```

```bash CLI nocheck
ant beta:messages create \
  --beta code-execution-2025-08-25 \
  --beta skills-2025-10-02 <<'YAML'
model: claude-opus-4-7
max_tokens: 4096
container:
  skills:
    - type: anthropic
      skill_id: xlsx
      version: latest
    - type: anthropic
      skill_id: pptx
      version: latest
    - type: custom
      skill_id: skill_01AbCdEfGhIjKlMnOpQrStUv
      version: latest
messages:
  - role: user
    content: Analyze sales data and create a presentation
tools:
  - type: code_execution_20250825
    name: code_execution
YAML
```

```python Python nocheck
response = client.beta.messages.create(
    model="claude-opus-4-7",
    max_tokens=4096,
    betas=["code-execution-2025-08-25", "skills-2025-10-02"],
    container={
        "skills": [
            {"type": "anthropic", "skill_id": "xlsx", "version": "latest"},
            {"type": "anthropic", "skill_id": "pptx", "version": "latest"},
            {
                "type": "custom",
                "skill_id": "skill_01AbCdEfGhIjKlMnOpQrStUv",
                "version": "latest",
            },
        ]
    },
    messages=[
        {"role": "user", "content": "Analyze sales data and create a presentation"}
    ],
    tools=[{"type": "code_execution_20250825", "name": "code_execution"}],
)
```

```typescript TypeScript nocheck
const response = await client.beta.messages.create({
  model: "claude-opus-4-7",
  max_tokens: 4096,
  betas: ["code-execution-2025-08-25", "skills-2025-10-02"],
  container: {
    skills: [
      {
        type: "anthropic",
        skill_id: "xlsx",
        version: "latest"
      },
      {
        type: "anthropic",
        skill_id: "pptx",
        version: "latest"
      },
      {
        type: "custom",
        skill_id: "skill_01AbCdEfGhIjKlMnOpQrStUv",
        version: "latest"
      }
    ]
  },
  messages: [
    {
      role: "user",
      content: "Analyze sales data and create a presentation"
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

```csharp C# nocheck
using System;
using System.Threading.Tasks;
using Anthropic;
using Anthropic.Models.Beta.Messages;

public class Program
{
    public static async Task Main(string[] args)
    {
        AnthropicClient client = new();

        var parameters = new MessageCreateParams
        {
            Model = "claude-opus-4-7",
            MaxTokens = 4096,
            Betas = new[] { "code-execution-2025-08-25", "skills-2025-10-02" },
            Container = new BetaContainerParams
            {
                Skills = new object[]
                {
                    new
                    {
                        type = "anthropic",
                        skill_id = "xlsx",
                        version = "latest"
                    },
                    new
                    {
                        type = "anthropic",
                        skill_id = "pptx",
                        version = "latest"
                    },
                    new
                    {
                        type = "custom",
                        skill_id = "skill_01AbCdEfGhIjKlMnOpQrStUv",
                        version = "latest"
                    }
                }
            },
            Messages = new[]
            {
                new BetaMessageParam
                {
                    Role = Role.User,
                    Content = "Analyze sales data and create a presentation"
                }
            },
            Tools = new object[]
            {
                new
                {
                    type = "code_execution_20250825",
                    name = "code_execution"
                }
            }
        };

        var message = await client.Beta.Messages.Create(parameters);
        Console.WriteLine(message);
    }
}
```

```go Go nocheck hidelines={1..11,-1}
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
		Model:     "claude-opus-4-7",
		MaxTokens: 4096,
		Betas: []anthropic.AnthropicBeta{
			"code-execution-2025-08-25",
			anthropic.AnthropicBetaSkills2025_10_02,
		},
		Container: anthropic.BetaMessageNewParamsContainerUnion{
			OfContainers: &anthropic.BetaContainerParams{
				Skills: []anthropic.BetaSkillParams{
					{
						Type:    anthropic.BetaSkillParamsTypeAnthropic,
						SkillID: "xlsx",
						Version: anthropic.String("latest"),
					},
					{
						Type:    anthropic.BetaSkillParamsTypeAnthropic,
						SkillID: "pptx",
						Version: anthropic.String("latest"),
					},
					{
						Type:    anthropic.BetaSkillParamsTypeCustom,
						SkillID: "skill_01AbCdEfGhIjKlMnOpQrStUv",
						Version: anthropic.String("latest"),
					},
				},
			},
		},
		Messages: []anthropic.BetaMessageParam{
			anthropic.NewBetaUserMessage(anthropic.NewBetaTextBlock("Analyze sales data and create a presentation")),
		},
		Tools: []anthropic.BetaToolUnionParam{
			{OfCodeExecutionTool20250825: &anthropic.BetaCodeExecutionTool20250825Param{}},
		},
	})
	if err != nil {
		log.Fatal(err)
	}
	fmt.Println(response)
}
```

```java Java nocheck hidelines={1..4,8..11,-2..}
import com.anthropic.client.AnthropicClient;
import com.anthropic.client.okhttp.AnthropicOkHttpClient;
import com.anthropic.models.beta.messages.MessageCreateParams;
import com.anthropic.models.beta.messages.BetaMessage;
import com.anthropic.models.beta.messages.BetaContainerParams;
import com.anthropic.models.beta.messages.BetaSkillParams;
import com.anthropic.models.beta.messages.BetaCodeExecutionTool20250825;
import java.util.List;

public class SkillsExample {
    public static void main(String[] args) {
        AnthropicClient client = AnthropicOkHttpClient.fromEnv();

        MessageCreateParams params = MessageCreateParams.builder()
            .model("claude-opus-4-7")
            .maxTokens(4096L)
            .addBeta("code-execution-2025-08-25")
            .addBeta("skills-2025-10-02")
            .container(BetaContainerParams.builder()
                .skills(List.of(
                    BetaSkillParams.builder()
                        .type(BetaSkillParams.Type.ANTHROPIC)
                        .skillId("xlsx")
                        .version("latest")
                        .build(),
                    BetaSkillParams.builder()
                        .type(BetaSkillParams.Type.ANTHROPIC)
                        .skillId("pptx")
                        .version("latest")
                        .build(),
                    BetaSkillParams.builder()
                        .type(BetaSkillParams.Type.CUSTOM)
                        .skillId("skill_01AbCdEfGhIjKlMnOpQrStUv")
                        .version("latest")
                        .build()
                ))
                .build())
            .addUserMessage("Analyze sales data and create a presentation")
            .addTool(BetaCodeExecutionTool20250825.builder().build())
            .build();

        BetaMessage response = client.beta().messages().create(params);
        System.out.println(response);
    }
}
```

```php PHP hidelines={1..4} nocheck
<?php

use Anthropic\Client;

$client = new Client(apiKey: getenv("ANTHROPIC_API_KEY"));

$message = $client->beta->messages->create(
    maxTokens: 4096,
    messages: [
        ['role' => 'user', 'content' => 'Analyze sales data and create a presentation']
    ],
    model: 'claude-opus-4-7',
    betas: ['code-execution-2025-08-25', 'skills-2025-10-02'],
    container: [
        'skills' => [
            [
                'type' => 'anthropic',
                'skill_id' => 'xlsx',
                'version' => 'latest'
            ],
            [
                'type' => 'anthropic',
                'skill_id' => 'pptx',
                'version' => 'latest'
            ],
            [
                'type' => 'custom',
                'skill_id' => 'skill_01AbCdEfGhIjKlMnOpQrStUv',
                'version' => 'latest'
            ]
        ]
    ],
    tools: [
        ['type' => 'code_execution_20250825', 'name' => 'code_execution']
    ]
);

echo $message;
```

```ruby Ruby nocheck hidelines={1..2}
require "anthropic"

client = Anthropic::Client.new

message = client.beta.messages.create(
  model: "claude-opus-4-7",
  max_tokens: 4096,
  betas: ["code-execution-2025-08-25", "skills-2025-10-02"],
  container: {
    skills: [
      {
        type: "anthropic",
        skill_id: "xlsx",
        version: "latest"
      },
      {
        type: "anthropic",
        skill_id: "pptx",
        version: "latest"
      },
      {
        type: "custom",
        skill_id: "skill_01AbCdEfGhIjKlMnOpQrStUv",
        version: "latest"
      }
    ]
  },
  messages: [
    { role: "user", content: "Analyze sales data and create a presentation" }
  ],
  tools: [
    { type: "code_execution_20250825", name: "code_execution" }
  ]
)
puts message
```
</CodeGroup>

---

## Managing Custom Skills

### Creating a Skill

Upload your custom Skill to make it available in your workspace. You can upload using either a directory path or individual file objects.

<CodeGroup defaultLanguage="CLI">

```bash cURL nocheck
curl -X POST "https://api.anthropic.com/v1/skills" \
  -H "x-api-key: $ANTHROPIC_API_KEY" \
  -H "anthropic-version: 2023-06-01" \
  -H "anthropic-beta: skills-2025-10-02" \
  -F "display_title=Financial Analysis" \
  -F "files[]=@financial_skill/SKILL.md;filename=financial_skill/SKILL.md" \
  -F "files[]=@financial_skill/analyze.py;filename=financial_skill/analyze.py"
```

```bash CLI nocheck
# Option 1: Upload individual files (one --file flag per file)
ant beta:skills create \
  --display-title "Financial Analysis" \
  --file financial_skill/SKILL.md \
  --file financial_skill/analyze.py \
  --beta skills-2025-10-02

# Option 2: Upload a zip archive
ant beta:skills create \
  --display-title "Financial Analysis" \
  --file financial_analysis_skill.zip \
  --beta skills-2025-10-02
```

```python Python nocheck hidelines={1..2}
import anthropic

client = anthropic.Anthropic()

# Option 1: Using files_from_dir helper (Python only, recommended)
from anthropic.lib import files_from_dir

skill = client.beta.skills.create(
    display_title="Financial Analysis",
    files=files_from_dir("/path/to/financial_analysis_skill"),
)

# Option 2: Using a zip file
skill = client.beta.skills.create(
    display_title="Financial Analysis",
    files=[("skill.zip", open("financial_analysis_skill.zip", "rb"))],
)

# Option 3: Using file tuples (filename, file_content, mime_type)
skill = client.beta.skills.create(
    display_title="Financial Analysis",
    files=[
        (
            "financial_skill/SKILL.md",
            open("financial_skill/SKILL.md", "rb"),
            "text/markdown",
        ),
        (
            "financial_skill/analyze.py",
            open("financial_skill/analyze.py", "rb"),
            "text/x-python",
        ),
    ],
)

print(f"Created skill: {skill.id}")
print(f"Latest version: {skill.latest_version}")
```

```typescript TypeScript nocheck
import Anthropic, { toFile } from "@anthropic-ai/sdk";
import fs from "fs";

const client = new Anthropic();

// Option 1: Using a zip file
const skillFromZip = await client.beta.skills.create({
  display_title: "Financial Analysis",
  files: [await toFile(fs.createReadStream("financial_analysis_skill.zip"), "skill.zip")]
});

// Option 2: Using individual file objects
const skill = await client.beta.skills.create({
  display_title: "Financial Analysis",
  files: [
    await toFile(fs.createReadStream("financial_skill/SKILL.md"), "financial_skill/SKILL.md", {
      type: "text/markdown"
    }),
    await toFile(
      fs.createReadStream("financial_skill/analyze.py"),
      "financial_skill/analyze.py",
      { type: "text/x-python" }
    )
  ]
});

console.log(`Created skill: ${skill.id}`);
console.log(`Latest version: ${skill.latest_version}`);
```

```csharp C# nocheck
using System;
using System.IO;
using System.Threading.Tasks;
using Anthropic;
using Anthropic.Models.Beta.Skills;

class Program
{
    static async Task Main(string[] args)
    {
        AnthropicClient client = new();

        // Option 1: Using a zip file
        var parameters = new SkillCreateParams
        {
            DisplayTitle = "Financial Analysis",
            Files = [
                new FileStream("financial_analysis_skill.zip", FileMode.Open, FileAccess.Read)
            ],
        };

        var skill = await client.Beta.Skills.Create(parameters);

        // Option 2: Using individual files
        var parameters2 = new SkillCreateParams
        {
            DisplayTitle = "Financial Analysis",
            Files = [
                new FileStream("financial_skill/SKILL.md", FileMode.Open, FileAccess.Read),
                new FileStream("financial_skill/analyze.py", FileMode.Open, FileAccess.Read)
            ],
        };

        var skill2 = await client.Beta.Skills.Create(parameters2);

        Console.WriteLine($"Created skill: {skill.Id}");
        Console.WriteLine($"Latest version: {skill.LatestVersion}");
    }
}
```

```go Go nocheck hidelines={1..15,-1}
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

	// Option 1: Using a zip file
	zipFile, err := os.Open("financial_analysis_skill.zip")
	if err != nil {
		log.Fatal(err)
	}
	defer zipFile.Close()

	skill, err := client.Beta.Skills.New(context.TODO(), anthropic.BetaSkillNewParams{
		DisplayTitle: anthropic.String("Financial Analysis"),
		Files:        []io.Reader{zipFile},
	})
	if err != nil {
		log.Fatal(err)
	}

	// Option 2: Using individual files
	skillMd, err := os.Open("financial_skill/SKILL.md")
	if err != nil {
		log.Fatal(err)
	}
	defer skillMd.Close()

	analyzePy, err := os.Open("financial_skill/analyze.py")
	if err != nil {
		log.Fatal(err)
	}
	defer analyzePy.Close()

	skill2, err := client.Beta.Skills.New(context.TODO(), anthropic.BetaSkillNewParams{
		DisplayTitle: anthropic.String("Financial Analysis"),
		Files:        []io.Reader{skillMd, analyzePy},
	})
	if err != nil {
		log.Fatal(err)
	}

	fmt.Printf("Created skill: %s\n", skill.ID)
	fmt.Printf("Latest version: %s\n", skill.LatestVersion)
	fmt.Printf("Created skill 2: %s\n", skill2.ID)
}
```

```java Java nocheck hidelines={1..2,5..10,-2..}
import com.anthropic.client.AnthropicClient;
import com.anthropic.client.okhttp.AnthropicOkHttpClient;
import com.anthropic.models.beta.skills.SkillCreateParams;
import com.anthropic.models.beta.skills.SkillCreateResponse;
import java.io.FileInputStream;
import java.io.IOException;
import java.nio.file.Path;

public class SkillCreate {
    public static void main(String[] args) throws IOException {
        AnthropicClient client = AnthropicOkHttpClient.fromEnv();

        // Option 1: Using a zip file
        SkillCreateParams params = SkillCreateParams.builder()
            .displayTitle("Financial Analysis")
            .addFile(new FileInputStream("financial_analysis_skill.zip"))
            .build();

        SkillCreateResponse skill = client.beta().skills().create(params);

        // Option 2: Using individual files
        SkillCreateParams params2 = SkillCreateParams.builder()
            .displayTitle("Financial Analysis")
            .addFile(Path.of("financial_skill/SKILL.md"))
            .addFile(Path.of("financial_skill/analyze.py"))
            .build();

        SkillCreateResponse skill2 = client.beta().skills().create(params2);

        System.out.println("Created skill: " + skill.id());
        System.out.println("Latest version: " + skill.latestVersion());
    }
}
```

```php PHP hidelines={1..4} nocheck
<?php

use Anthropic\Client;

$client = new Client(apiKey: getenv("ANTHROPIC_API_KEY"));

// Option 1: Using a zip file
$skill = $client->beta->skills->create(
    displayTitle: 'Financial Analysis',
    files: [
        fopen('financial_analysis_skill.zip', 'r')
    ],
);

// Option 2: Using individual files
$skill = $client->beta->skills->create(
    displayTitle: 'Financial Analysis',
    files: [
        fopen('financial_skill/SKILL.md', 'r'),
        fopen('financial_skill/analyze.py', 'r')
    ],
);

echo "Created skill: {$skill->id}\n";
echo "Latest version: {$skill->latestVersion}\n";
```

```ruby Ruby nocheck hidelines={1..2}
require "anthropic"

client = Anthropic::Client.new

# Option 1: Using a zip file
skill = client.beta.skills.create(
  display_title: "Financial Analysis",
  files: [
    File.open("financial_analysis_skill.zip", "rb")
  ]
)

# Option 2: Using individual files
skill = client.beta.skills.create(
  display_title: "Financial Analysis",
  files: [
    File.open("financial_skill/SKILL.md", "rb"),
    File.open("financial_skill/analyze.py", "rb")
  ]
)

puts "Created skill: #{skill.id}"
puts "Latest version: #{skill.latest_version}"
```
</CodeGroup>

**Requirements:**
- Must include a SKILL.md file at the top level
- All files must specify a common root directory in their paths
- Total upload size must be under 30&nbsp;MB
- YAML frontmatter requirements:
  - `name`: Maximum 64 characters, lowercase letters/numbers/hyphens only, no XML tags, no reserved words ("anthropic", "claude")
  - `description`: Maximum 1024 characters, non-empty, no XML tags

For complete request/response schemas, see the [Create Skill API reference](/docs/en/api/skills/create-skill).

### Listing Skills

Retrieve all Skills available to your workspace, including both Anthropic pre-built Skills and your custom Skills. Use the `source` parameter to filter by skill type:

<CodeGroup defaultLanguage="CLI">
```bash cURL
# List all Skills
curl "https://api.anthropic.com/v1/skills" \
  -H "x-api-key: $ANTHROPIC_API_KEY" \
  -H "anthropic-version: 2023-06-01" \
  -H "anthropic-beta: skills-2025-10-02"

# List only custom Skills
curl "https://api.anthropic.com/v1/skills?source=custom" \
  -H "x-api-key: $ANTHROPIC_API_KEY" \
  -H "anthropic-version: 2023-06-01" \
  -H "anthropic-beta: skills-2025-10-02"
```

```bash CLI
# List all Skills
ant beta:skills list

# List only custom Skills
ant beta:skills list --source custom
```

```python Python
# List all Skills
skills = client.beta.skills.list()

for skill in skills.data:
    print(f"{skill.id}: {skill.display_title} (source: {skill.source})")

# List only custom Skills
custom_skills = client.beta.skills.list(source="custom")
```

```typescript TypeScript
// List all Skills
const skills = await client.beta.skills.list();

for (const skill of skills.data) {
  console.log(`${skill.id}: ${skill.display_title} (source: ${skill.source})`);
}

// List only custom Skills
const customSkills = await client.beta.skills.list({
  source: "custom"
});
```

```csharp C# nocheck
using System;
using System.Threading.Tasks;
using Anthropic;
using Anthropic.Models.Beta.Skills;

class Program
{
    static async Task Main(string[] args)
    {
        AnthropicClient client = new();

        // List all Skills
        var skills = await client.Beta.Skills.List();

        foreach (var skill in skills.Data)
        {
            Console.WriteLine($"{skill.Id}: {skill.DisplayTitle} (source: {skill.Source})");
        }

        // List only custom Skills
        var customSkills = await client.Beta.Skills.List(new SkillListParams
        {
            Source = "custom",
        });
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

	// List all Skills
	skills := client.Beta.Skills.ListAutoPaging(context.TODO(), anthropic.BetaSkillListParams{})

	for skills.Next() {
		skill := skills.Current()
		fmt.Printf("%s: %s (source: %s)\n", skill.ID, skill.DisplayTitle, skill.Source)
	}
	if skills.Err() != nil {
		log.Fatal(skills.Err())
	}

	// List only custom Skills
	customSkills := client.Beta.Skills.ListAutoPaging(context.TODO(), anthropic.BetaSkillListParams{
		Source: anthropic.String("custom"),
	})

	for customSkills.Next() {
		skill := customSkills.Current()
		fmt.Printf("%s: %s (source: %s)\n", skill.ID, skill.DisplayTitle, skill.Source)
	}
}
```

```java Java hidelines={1..2,6..8,-2..}
import com.anthropic.client.AnthropicClient;
import com.anthropic.client.okhttp.AnthropicOkHttpClient;
import com.anthropic.models.beta.skills.SkillListParams;
import com.anthropic.models.beta.skills.SkillListPage;
import com.anthropic.models.beta.skills.SkillListResponse;

public class ListSkills {
    public static void main(String[] args) {
        AnthropicClient client = AnthropicOkHttpClient.fromEnv();

        // List all Skills
        SkillListPage skills = client.beta().skills().list();

        for (SkillListResponse skill : skills.data()) {
            System.out.println(skill.id() + ": " + skill.displayTitle() + " (source: " + skill.source() + ")");
        }

        // List only custom Skills
        SkillListParams customParams = SkillListParams.builder()
            .source("custom")
            .build();

        SkillListPage customSkills = client.beta().skills().list(customParams);
    }
}
```

```php PHP hidelines={1..4}
<?php

use Anthropic\Client;

$client = new Client(apiKey: getenv("ANTHROPIC_API_KEY"));

// List all Skills
$skills = $client->beta->skills->list();

foreach ($skills->data as $skill) {
    echo "{$skill->id}: {$skill->displayTitle} (source: {$skill->source})\n";
}

// List only custom Skills
$customSkills = $client->beta->skills->list(
    source: 'custom',
);
```

```ruby Ruby hidelines={1..2}
require "anthropic"

client = Anthropic::Client.new

# List all Skills
skills = client.beta.skills.list

skills.data.each do |skill|
  puts "#{skill.id}: #{skill.display_title} (source: #{skill.source})"
end

# List only custom Skills
custom_skills = client.beta.skills.list(
  source: "custom"
)
```
</CodeGroup>

See the [List Skills API reference](/docs/en/api/skills/list-skills) for pagination and filtering options.

### Retrieving a Skill

Get details about a specific Skill:

<CodeGroup defaultLanguage="CLI">

```bash cURL nocheck
curl "https://api.anthropic.com/v1/skills/skill_01AbCdEfGhIjKlMnOpQrStUv" \
  -H "x-api-key: $ANTHROPIC_API_KEY" \
  -H "anthropic-version: 2023-06-01" \
  -H "anthropic-beta: skills-2025-10-02"
```

```bash CLI nocheck
ant beta:skills retrieve \
  --skill-id skill_01AbCdEfGhIjKlMnOpQrStUv
```

```python Python nocheck
skill = client.beta.skills.retrieve(skill_id="skill_01AbCdEfGhIjKlMnOpQrStUv")

print(f"Skill: {skill.display_title}")
print(f"Latest version: {skill.latest_version}")
print(f"Created: {skill.created_at}")
```

```typescript TypeScript nocheck
const skill = await client.beta.skills.retrieve("skill_01AbCdEfGhIjKlMnOpQrStUv");

console.log(`Skill: ${skill.display_title}`);
console.log(`Latest version: ${skill.latest_version}`);
console.log(`Created: ${skill.created_at}`);
```

```csharp C# nocheck
using System;
using System.Threading.Tasks;
using Anthropic;
using Anthropic.Models.Beta.Skills;

class Program
{
    static async Task Main(string[] args)
    {
        AnthropicClient client = new();

        var skill = await client.Beta.Skills.Retrieve("skill_01AbCdEfGhIjKlMnOpQrStUv");

        Console.WriteLine($"Skill: {skill.DisplayTitle}");
        Console.WriteLine($"Latest version: {skill.LatestVersion}");
        Console.WriteLine($"Created: {skill.CreatedAt}");
    }
}
```

```go Go nocheck hidelines={1..13,-1}
package main

import (
	"context"
	"fmt"
	"log"

	"github.com/anthropics/anthropic-sdk-go"
)

func main() {
	client := anthropic.NewClient()

	skill, err := client.Beta.Skills.Get(
		context.TODO(),
		"skill_01AbCdEfGhIjKlMnOpQrStUv",
		anthropic.BetaSkillGetParams{},
	)
	if err != nil {
		log.Fatal(err)
	}

	fmt.Printf("Skill: %s\n", skill.DisplayTitle)
	fmt.Printf("Latest version: %s\n", skill.LatestVersion)
	fmt.Printf("Created: %s\n", skill.CreatedAt)
}
```

```java Java nocheck hidelines={1..2,4..6,-2..}
import com.anthropic.client.AnthropicClient;
import com.anthropic.client.okhttp.AnthropicOkHttpClient;
import com.anthropic.models.beta.skills.SkillRetrieveResponse;

public class RetrieveSkill {
    public static void main(String[] args) {
        AnthropicClient client = AnthropicOkHttpClient.fromEnv();

        SkillRetrieveResponse skill = client.beta().skills().retrieve("skill_01AbCdEfGhIjKlMnOpQrStUv");

        System.out.println("Skill: " + skill.displayTitle());
        System.out.println("Latest version: " + skill.latestVersion());
        System.out.println("Created: " + skill.createdAt());
    }
}
```

```php PHP hidelines={1..4} nocheck
<?php

use Anthropic\Client;

$client = new Client(apiKey: getenv("ANTHROPIC_API_KEY"));

$skill = $client->beta->skills->retrieve(
    skillID: "skill_01AbCdEfGhIjKlMnOpQrStUv",
);

echo "Skill: " . $skill->displayTitle . "\n";
echo "Latest version: " . $skill->latestVersion . "\n";
echo "Created: " . $skill->createdAt . "\n";
```

```ruby Ruby nocheck hidelines={1..2}
require "anthropic"

client = Anthropic::Client.new

skill = client.beta.skills.retrieve("skill_01AbCdEfGhIjKlMnOpQrStUv")

puts "Skill: #{skill.display_title}"
puts "Latest version: #{skill.latest_version}"
puts "Created: #{skill.created_at}"
```
</CodeGroup>

### Deleting a Skill

To delete a Skill, you must first delete all its versions:

<CodeGroup defaultLanguage="CLI">

```bash cURL nocheck
# Delete all versions first, then delete the Skill
curl -X DELETE "https://api.anthropic.com/v1/skills/skill_01AbCdEfGhIjKlMnOpQrStUv" \
  -H "x-api-key: $ANTHROPIC_API_KEY" \
  -H "anthropic-version: 2023-06-01" \
  -H "anthropic-beta: skills-2025-10-02"
```

```bash CLI nocheck
# Step 1: Delete all versions
ant beta:skills:versions list \
  --skill-id skill_01AbCdEfGhIjKlMnOpQrStUv \
  --transform version --format yaml \
  | tr -d '"' \
  | while read -r VERSION; do
      ant beta:skills:versions delete \
        --skill-id skill_01AbCdEfGhIjKlMnOpQrStUv \
        --version "$VERSION" >/dev/null
    done

# Step 2: Delete the Skill
ant beta:skills delete \
  --skill-id skill_01AbCdEfGhIjKlMnOpQrStUv >/dev/null
```

```python Python nocheck
# Step 1: Delete all versions
versions = client.beta.skills.versions.list(skill_id="skill_01AbCdEfGhIjKlMnOpQrStUv")

for version in versions.data:
    client.beta.skills.versions.delete(
        skill_id="skill_01AbCdEfGhIjKlMnOpQrStUv",
        version=version.version,
    )

# Step 2: Delete the Skill
client.beta.skills.delete(skill_id="skill_01AbCdEfGhIjKlMnOpQrStUv")
```

```typescript TypeScript nocheck hidelines={1..2}
import Anthropic from "@anthropic-ai/sdk";

const client = new Anthropic();

// Step 1: Delete all versions
const versions = await client.beta.skills.versions.list("skill_01AbCdEfGhIjKlMnOpQrStUv");

for (const version of versions.data) {
  await client.beta.skills.versions.delete("skill_01AbCdEfGhIjKlMnOpQrStUv", version.version);
}

// Step 2: Delete the Skill
await client.beta.skills.delete("skill_01AbCdEfGhIjKlMnOpQrStUv");
```

```csharp C# nocheck
using System;
using System.Threading.Tasks;
using Anthropic;

class Program
{
    static async Task Main(string[] args)
    {
        AnthropicClient client = new();

        // Step 1: Delete all versions
        var versions = await client.Beta.Skills.Versions.List("skill_01AbCdEfGhIjKlMnOpQrStUv");

        foreach (var version in versions.Data)
        {
            await client.Beta.Skills.Versions.Delete(
                "skill_01AbCdEfGhIjKlMnOpQrStUv",
                version.Version
            );
        }

        // Step 2: Delete the Skill
        await client.Beta.Skills.Delete("skill_01AbCdEfGhIjKlMnOpQrStUv");
    }
}
```

```go Go nocheck hidelines={1..12,-1}
package main

import (
	"context"
	"log"

	"github.com/anthropics/anthropic-sdk-go"
)

func main() {
	client := anthropic.NewClient()

	// Step 1: Delete all versions
	versions := client.Beta.Skills.Versions.ListAutoPaging(
		context.TODO(),
		"skill_01AbCdEfGhIjKlMnOpQrStUv",
		anthropic.BetaSkillVersionListParams{},
	)

	for versions.Next() {
		version := versions.Current()
		_, err := client.Beta.Skills.Versions.Delete(
			context.TODO(),
			version.Version,
			anthropic.BetaSkillVersionDeleteParams{
				SkillID: "skill_01AbCdEfGhIjKlMnOpQrStUv",
			},
		)
		if err != nil {
			log.Fatal(err)
		}
	}

	// Step 2: Delete the Skill
	_, err := client.Beta.Skills.Delete(
		context.TODO(),
		"skill_01AbCdEfGhIjKlMnOpQrStUv",
		anthropic.BetaSkillDeleteParams{},
	)
	if err != nil {
		log.Fatal(err)
	}
}
```

```java Java nocheck hidelines={1..2,5..7,-2..}
import com.anthropic.client.AnthropicClient;
import com.anthropic.client.okhttp.AnthropicOkHttpClient;
import com.anthropic.models.beta.skills.versions.VersionListPage;
import com.anthropic.models.beta.skills.versions.VersionDeleteParams;

public class DeleteSkill {
    public static void main(String[] args) {
        AnthropicClient client = AnthropicOkHttpClient.fromEnv();

        // Step 1: Delete all versions
        VersionListPage versions = client.beta().skills().versions().list("skill_01AbCdEfGhIjKlMnOpQrStUv");

        for (var version : versions.data()) {
            client.beta().skills().versions().delete(
                version.version(),
                VersionDeleteParams.builder()
                    .skillId("skill_01AbCdEfGhIjKlMnOpQrStUv")
                    .build()
            );
        }

        // Step 2: Delete the Skill
        client.beta().skills().delete("skill_01AbCdEfGhIjKlMnOpQrStUv");
    }
}
```

```php PHP hidelines={1..4} nocheck
<?php

use Anthropic\Client;

$client = new Client(apiKey: getenv("ANTHROPIC_API_KEY"));

// Step 1: Delete all versions
$versions = $client->beta->skills->versions->list(
    skillID: "skill_01AbCdEfGhIjKlMnOpQrStUv",
);

foreach ($versions->data as $version) {
    $client->beta->skills->versions->delete(
        skillID: "skill_01AbCdEfGhIjKlMnOpQrStUv",
        version: $version->version,
    );
}

// Step 2: Delete the Skill
$client->beta->skills->delete(
    skillID: "skill_01AbCdEfGhIjKlMnOpQrStUv",
);
```

```ruby Ruby nocheck hidelines={1..2}
require "anthropic"

client = Anthropic::Client.new

# Step 1: Delete all versions
versions = client.beta.skills.versions.list("skill_01AbCdEfGhIjKlMnOpQrStUv")

versions.data.each do |version|
  client.beta.skills.versions.delete(
    version.version,
    skill_id: "skill_01AbCdEfGhIjKlMnOpQrStUv"
  )
end

# Step 2: Delete the Skill
client.beta.skills.delete("skill_01AbCdEfGhIjKlMnOpQrStUv")
```
</CodeGroup>

Attempting to delete a Skill with existing versions returns a 400 error.

### Versioning

Skills support versioning to manage updates safely:

**Anthropic-Managed Skills:**
- Versions use date format: `20251013`
- New versions released as updates are made
- Specify exact versions for stability

**Custom Skills:**
- Auto-generated epoch timestamps: `1759178010641129`
- Use `"latest"` to always get the most recent version
- Create new versions when updating Skill files

<CodeGroup defaultLanguage="CLI">

```bash cURL nocheck
# Create a new version
NEW_VERSION=$(curl -X POST "https://api.anthropic.com/v1/skills/skill_01AbCdEfGhIjKlMnOpQrStUv/versions" \
  -H "x-api-key: $ANTHROPIC_API_KEY" \
  -H "anthropic-version: 2023-06-01" \
  -H "anthropic-beta: skills-2025-10-02" \
  -F "files[]=@updated_skill/SKILL.md;filename=updated_skill/SKILL.md")

VERSION_NUMBER=$(echo "$NEW_VERSION" | jq -r '.version')

# Use specific version
curl https://api.anthropic.com/v1/messages \
  -H "x-api-key: $ANTHROPIC_API_KEY" \
  -H "anthropic-version: 2023-06-01" \
  -H "anthropic-beta: code-execution-2025-08-25,skills-2025-10-02" \
  -H "content-type: application/json" \
  -d "{
    \"model\": \"claude-opus-4-7\",
    \"max_tokens\": 4096,
    \"container\": {
      \"skills\": [{
        \"type\": \"custom\",
        \"skill_id\": \"skill_01AbCdEfGhIjKlMnOpQrStUv\",
        \"version\": \"$VERSION_NUMBER\"
      }]
    },
    \"messages\": [{\"role\": \"user\", \"content\": \"Use updated Skill\"}],
    \"tools\": [{\"type\": \"code_execution_20250825\", \"name\": \"code_execution\"}]
  }"

# Use latest version
curl https://api.anthropic.com/v1/messages \
  -H "x-api-key: $ANTHROPIC_API_KEY" \
  -H "anthropic-version: 2023-06-01" \
  -H "anthropic-beta: code-execution-2025-08-25,skills-2025-10-02" \
  -H "content-type: application/json" \
  -d '{
    "model": "claude-opus-4-7",
    "max_tokens": 4096,
    "container": {
      "skills": [{
        "type": "custom",
        "skill_id": "skill_01AbCdEfGhIjKlMnOpQrStUv",
        "version": "latest"
      }]
    },
    "messages": [{"role": "user", "content": "Use latest Skill version"}],
    "tools": [{"type": "code_execution_20250825", "name": "code_execution"}]
  }'
```

```bash CLI nocheck
# Create a new version
VERSION_NUMBER=$(ant beta:skills:versions create \
  --skill-id skill_01AbCdEfGhIjKlMnOpQrStUv \
  --file updated_skill/SKILL.md \
  --transform version --format yaml)

# Use specific version
ant beta:messages create \
  --beta code-execution-2025-08-25 \
  --beta skills-2025-10-02 <<YAML
model: claude-opus-4-7
max_tokens: 4096
container:
  skills:
    - type: custom
      skill_id: skill_01AbCdEfGhIjKlMnOpQrStUv
      version: $VERSION_NUMBER
messages:
  - role: user
    content: Use updated Skill
tools:
  - type: code_execution_20250825
    name: code_execution
YAML

# Use latest version
ant beta:messages create \
  --beta code-execution-2025-08-25 \
  --beta skills-2025-10-02 <<'YAML'
model: claude-opus-4-7
max_tokens: 4096
container:
  skills:
    - type: custom
      skill_id: skill_01AbCdEfGhIjKlMnOpQrStUv
      version: latest
messages:
  - role: user
    content: Use latest Skill version
tools:
  - type: code_execution_20250825
    name: code_execution
YAML
```

```python Python nocheck
# Create a new version
from anthropic.lib import files_from_dir

new_version = client.beta.skills.versions.create(
    skill_id="skill_01AbCdEfGhIjKlMnOpQrStUv",
    files=files_from_dir("/path/to/updated_skill"),
)

# Use specific version
response = client.beta.messages.create(
    model="claude-opus-4-7",
    max_tokens=4096,
    betas=["code-execution-2025-08-25", "skills-2025-10-02"],
    container={
        "skills": [
            {
                "type": "custom",
                "skill_id": "skill_01AbCdEfGhIjKlMnOpQrStUv",
                "version": new_version.version,
            }
        ]
    },
    messages=[{"role": "user", "content": "Use updated Skill"}],
    tools=[{"type": "code_execution_20250825", "name": "code_execution"}],
)

# Use latest version
response = client.beta.messages.create(
    model="claude-opus-4-7",
    max_tokens=4096,
    betas=["code-execution-2025-08-25", "skills-2025-10-02"],
    container={
        "skills": [
            {
                "type": "custom",
                "skill_id": "skill_01AbCdEfGhIjKlMnOpQrStUv",
                "version": "latest",
            }
        ]
    },
    messages=[{"role": "user", "content": "Use latest Skill version"}],
    tools=[{"type": "code_execution_20250825", "name": "code_execution"}],
)
```

```typescript TypeScript nocheck hidelines={1}
import Anthropic from "@anthropic-ai/sdk";
import fs from "fs";

const client = new Anthropic();

// Create a new version using a zip file
const newVersion = await client.beta.skills.versions.create("skill_01AbCdEfGhIjKlMnOpQrStUv", {
  files: [fs.createReadStream("updated_skill.zip")]
});

// Use specific version
const specificVersionResponse = await client.beta.messages.create({
  model: "claude-opus-4-7",
  max_tokens: 4096,
  betas: ["code-execution-2025-08-25", "skills-2025-10-02"],
  container: {
    skills: [
      {
        type: "custom",
        skill_id: "skill_01AbCdEfGhIjKlMnOpQrStUv",
        version: newVersion.version
      }
    ]
  },
  messages: [{ role: "user", content: "Use updated Skill" }],
  tools: [{ type: "code_execution_20250825", name: "code_execution" }]
});

// Use latest version
const latestVersionResponse = await client.beta.messages.create({
  model: "claude-opus-4-7",
  max_tokens: 4096,
  betas: ["code-execution-2025-08-25", "skills-2025-10-02"],
  container: {
    skills: [
      {
        type: "custom",
        skill_id: "skill_01AbCdEfGhIjKlMnOpQrStUv",
        version: "latest"
      }
    ]
  },
  messages: [{ role: "user", content: "Use latest Skill version" }],
  tools: [{ type: "code_execution_20250825", name: "code_execution" }]
});
```

```csharp C# nocheck
using System;
using System.IO;
using System.Threading.Tasks;
using Anthropic;
using Anthropic.Models.Beta.Messages;
using Anthropic.Models.Beta.Skills;

class Program
{
    static async Task Main()
    {
        var client = new AnthropicClient
        {
            ApiKey = Environment.GetEnvironmentVariable("ANTHROPIC_API_KEY")
        };

        // Create a new version
        var versionParams = new SkillVersionCreateParams
        {
            Files = [File.OpenRead("/path/to/updated_skill/SKILL.md")],
        };

        var newVersion = await client.Beta.Skills.Versions.Create(
            "skill_01AbCdEfGhIjKlMnOpQrStUv",
            versionParams
        );

        // Use specific version
        var specificVersionParams = new MessageCreateParams
        {
            Model = "claude-opus-4-7",
            MaxTokens = 4096,
            Betas = ["code-execution-2025-08-25", "skills-2025-10-02"],
            Container = new()
            {
                Skills =
                [
                    new()
                    {
                        Type = "custom",
                        SkillId = "skill_01AbCdEfGhIjKlMnOpQrStUv",
                        Version = newVersion.Version
                    }
                ]
            },
            Messages = [new() { Role = Role.User, Content = "Use updated Skill" }],
            Tools =
            [
                new() { Type = "code_execution_20250825", Name = "code_execution" }
            ]
        };

        var response = await client.Beta.Messages.Create(specificVersionParams);
        Console.WriteLine(response);

        // Use latest version
        var latestVersionParams = new MessageCreateParams
        {
            Model = "claude-opus-4-7",
            MaxTokens = 4096,
            Betas = ["code-execution-2025-08-25", "skills-2025-10-02"],
            Container = new()
            {
                Skills =
                [
                    new()
                    {
                        Type = "custom",
                        SkillId = "skill_01AbCdEfGhIjKlMnOpQrStUv",
                        Version = "latest"
                    }
                ]
            },
            Messages = [new() { Role = Role.User, Content = "Use latest Skill version" }],
            Tools =
            [
                new() { Type = "code_execution_20250825", Name = "code_execution" }
            ]
        };

        var latestResponse = await client.Beta.Messages.Create(latestVersionParams);
        Console.WriteLine(latestResponse);
    }
}
```

```go Go nocheck hidelines={1..13,87..88}
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

	// Create a new version
	skillFile := mustOpen("/path/to/updated_skill/SKILL.md")
	defer skillFile.Close()

	newVersion, err := client.Beta.Skills.Versions.New(
		context.TODO(),
		"skill_01AbCdEfGhIjKlMnOpQrStUv",
		anthropic.BetaSkillVersionNewParams{
			Files: []io.Reader{skillFile},
		},
	)
	if err != nil {
		log.Fatal(err)
	}

	// Use specific version
	response, err := client.Beta.Messages.New(context.TODO(), anthropic.BetaMessageNewParams{
		Model:     "claude-opus-4-7",
		MaxTokens: 4096,
		Betas:     []anthropic.AnthropicBeta{"code-execution-2025-08-25", anthropic.AnthropicBetaSkills2025_10_02},
		Container: anthropic.BetaMessageNewParamsContainerUnion{
			OfContainers: &anthropic.BetaContainerParams{
				Skills: []anthropic.BetaSkillParams{
					{
						Type:    anthropic.BetaSkillParamsTypeCustom,
						SkillID: "skill_01AbCdEfGhIjKlMnOpQrStUv",
						Version: anthropic.String(newVersion.Version),
					},
				},
			},
		},
		Messages: []anthropic.BetaMessageParam{
			anthropic.NewBetaUserMessage(anthropic.NewBetaTextBlock("Use updated Skill")),
		},
		Tools: []anthropic.BetaToolUnionParam{
			{OfCodeExecutionTool20250825: &anthropic.BetaCodeExecutionTool20250825Param{}},
		},
	})
	if err != nil {
		log.Fatal(err)
	}
	fmt.Println(response)

	// Use latest version
	latestResponse, err := client.Beta.Messages.New(context.TODO(), anthropic.BetaMessageNewParams{
		Model:     "claude-opus-4-7",
		MaxTokens: 4096,
		Betas:     []anthropic.AnthropicBeta{"code-execution-2025-08-25", anthropic.AnthropicBetaSkills2025_10_02},
		Container: anthropic.BetaMessageNewParamsContainerUnion{
			OfContainers: &anthropic.BetaContainerParams{
				Skills: []anthropic.BetaSkillParams{
					{
						Type:    anthropic.BetaSkillParamsTypeCustom,
						SkillID: "skill_01AbCdEfGhIjKlMnOpQrStUv",
						Version: anthropic.String("latest"),
					},
				},
			},
		},
		Messages: []anthropic.BetaMessageParam{
			anthropic.NewBetaUserMessage(anthropic.NewBetaTextBlock("Use latest Skill version")),
		},
		Tools: []anthropic.BetaToolUnionParam{
			{OfCodeExecutionTool20250825: &anthropic.BetaCodeExecutionTool20250825Param{}},
		},
	})
	if err != nil {
		log.Fatal(err)
	}
	fmt.Println(latestResponse)
}

func mustOpen(path string) *os.File {
	f, err := os.Open(path)
	if err != nil {
		log.Fatal(err)
	}
	return f
}
```

```java Java nocheck hidelines={1..4,10..13,-2..}
import com.anthropic.client.AnthropicClient;
import com.anthropic.client.okhttp.AnthropicOkHttpClient;
import com.anthropic.models.beta.messages.MessageCreateParams;
import com.anthropic.models.beta.messages.BetaMessage;
import com.anthropic.models.beta.messages.BetaContainerParams;
import com.anthropic.models.beta.messages.BetaSkillParams;
import com.anthropic.models.beta.messages.BetaCodeExecutionTool20250825;
import com.anthropic.models.beta.skills.versions.VersionCreateParams;
import com.anthropic.models.beta.skills.versions.VersionCreateResponse;
import java.nio.file.Path;

public class SkillVersioning {
    public static void main(String[] args) {
        AnthropicClient client = AnthropicOkHttpClient.fromEnv();

        // Create a new version
        VersionCreateParams versionParams = VersionCreateParams.builder()
            .addFile(Path.of("/path/to/updated_skill/SKILL.md"))
            .build();

        VersionCreateResponse newVersion = client.beta().skills().versions()
            .create("skill_01AbCdEfGhIjKlMnOpQrStUv", versionParams);

        // Use specific version
        MessageCreateParams specificVersionParams = MessageCreateParams.builder()
            .model("claude-opus-4-7")
            .maxTokens(4096L)
            .addBeta("code-execution-2025-08-25")
            .addBeta("skills-2025-10-02")
            .container(BetaContainerParams.builder()
                .addSkill(BetaSkillParams.builder()
                    .type(BetaSkillParams.Type.CUSTOM)
                    .skillId("skill_01AbCdEfGhIjKlMnOpQrStUv")
                    .version(newVersion.version())
                    .build())
                .build())
            .addUserMessage("Use updated Skill")
            .addTool(BetaCodeExecutionTool20250825.builder().build())
            .build();

        BetaMessage response = client.beta().messages().create(specificVersionParams);
        System.out.println(response);

        // Use latest version
        MessageCreateParams latestVersionParams = MessageCreateParams.builder()
            .model("claude-opus-4-7")
            .maxTokens(4096L)
            .addBeta("code-execution-2025-08-25")
            .addBeta("skills-2025-10-02")
            .container(BetaContainerParams.builder()
                .addSkill(BetaSkillParams.builder()
                    .type(BetaSkillParams.Type.CUSTOM)
                    .skillId("skill_01AbCdEfGhIjKlMnOpQrStUv")
                    .version("latest")
                    .build())
                .build())
            .addUserMessage("Use latest Skill version")
            .addTool(BetaCodeExecutionTool20250825.builder().build())
            .build();

        BetaMessage latestResponse = client.beta().messages().create(latestVersionParams);
        System.out.println(latestResponse);
    }
}
```

```php PHP hidelines={1..4} nocheck
<?php

use Anthropic\Client;

$client = new Client(apiKey: getenv("ANTHROPIC_API_KEY"));

// Create a new version
$newVersion = $client->beta->skills->versions->create(
    skillID: "skill_01AbCdEfGhIjKlMnOpQrStUv",
    files: [fopen("/path/to/updated_skill/SKILL.md", "r")],
);

// Use specific version
$response = $client->beta->messages->create(
    maxTokens: 4096,
    messages: [['role' => 'user', 'content' => 'Use updated Skill']],
    model: 'claude-opus-4-7',
    betas: ['code-execution-2025-08-25', 'skills-2025-10-02'],
    container: [
        'skills' => [[
            'type' => 'custom',
            'skill_id' => 'skill_01AbCdEfGhIjKlMnOpQrStUv',
            'version' => $newVersion->version
        ]]
    ],
    tools: [['type' => 'code_execution_20250825', 'name' => 'code_execution']]
);
echo $response;

// Use latest version
$latestResponse = $client->beta->messages->create(
    maxTokens: 4096,
    messages: [['role' => 'user', 'content' => 'Use latest Skill version']],
    model: 'claude-opus-4-7',
    betas: ['code-execution-2025-08-25', 'skills-2025-10-02'],
    container: [
        'skills' => [[
            'type' => 'custom',
            'skill_id' => 'skill_01AbCdEfGhIjKlMnOpQrStUv',
            'version' => 'latest'
        ]]
    ],
    tools: [['type' => 'code_execution_20250825', 'name' => 'code_execution']]
);
echo $latestResponse;
```

```ruby Ruby nocheck hidelines={1..2}
require "anthropic"

client = Anthropic::Client.new

# Create a new version
new_version = client.beta.skills.versions.create(
  "skill_01AbCdEfGhIjKlMnOpQrStUv",
  files: [File.open("/path/to/updated_skill/SKILL.md")]
)

# Use specific version
response = client.beta.messages.create(
  model: "claude-opus-4-7",
  max_tokens: 4096,
  betas: ["code-execution-2025-08-25", "skills-2025-10-02"],
  container: {
    skills: [{
      type: "custom",
      skill_id: "skill_01AbCdEfGhIjKlMnOpQrStUv",
      version: new_version.version
    }]
  },
  messages: [{ role: "user", content: "Use updated Skill" }],
  tools: [{ type: "code_execution_20250825", name: "code_execution" }]
)
puts response

# Use latest version
latest_response = client.beta.messages.create(
  model: "claude-opus-4-7",
  max_tokens: 4096,
  betas: ["code-execution-2025-08-25", "skills-2025-10-02"],
  container: {
    skills: [{
      type: "custom",
      skill_id: "skill_01AbCdEfGhIjKlMnOpQrStUv",
      version: "latest"
    }]
  },
  messages: [{ role: "user", content: "Use latest Skill version" }],
  tools: [{ type: "code_execution_20250825", name: "code_execution" }]
)
puts latest_response
```
</CodeGroup>

See the [Create Skill Version API reference](/docs/en/api/skills/create-skill-version) for complete details.

---

## How Skills Are Loaded

When you specify Skills in a container:

1. **Metadata Discovery:** Claude sees metadata for each Skill (name, description) in the system prompt
2. **File Loading:** Skill files are copied into the container at `/skills/{directory}/`
3. **Automatic Use:** Claude automatically loads and uses Skills when relevant to your request
4. **Composition:** Multiple Skills compose together for complex workflows

The progressive disclosure architecture ensures efficient context usage: Claude only loads full Skill instructions when needed.

---

## Use Cases

### Organizational Skills

**Brand & Communications**
- Apply company-specific formatting (colors, fonts, layouts) to documents
- Generate communications following organizational templates
- Ensure consistent brand guidelines across all outputs

**Project Management**
- Structure notes with company-specific formats (OKRs, decision logs)
- Generate tasks following team conventions
- Create standardized meeting recaps and status updates

**Business Operations**
- Create company-standard reports, proposals, and analyses
- Execute company-specific analytical procedures
- Generate financial models following organizational templates

### Personal Skills

**Content Creation**
- Custom document templates
- Specialized formatting and styling
- Domain-specific content generation

**Data Analysis**
- Custom data processing pipelines
- Specialized visualization templates
- Industry-specific analytical methods

**Development & Automation**
- Code generation templates
- Testing frameworks
- Deployment workflows

### Example: Financial Modeling

Combine Excel and custom DCF analysis Skills:

<CodeGroup>

```bash cURL nocheck
# Create custom DCF analysis Skill
DCF_SKILL=$(curl -X POST "https://api.anthropic.com/v1/skills" \
  -H "x-api-key: $ANTHROPIC_API_KEY" \
  -H "anthropic-version: 2023-06-01" \
  -H "anthropic-beta: skills-2025-10-02" \
  -F "display_title=DCF Analysis" \
  -F "files[]=@dcf_skill/SKILL.md;filename=dcf_skill/SKILL.md")

DCF_SKILL_ID=$(echo "$DCF_SKILL" | jq -r '.id')

# Use with Excel to create financial model
curl https://api.anthropic.com/v1/messages \
  -H "x-api-key: $ANTHROPIC_API_KEY" \
  -H "anthropic-version: 2023-06-01" \
  -H "anthropic-beta: code-execution-2025-08-25,skills-2025-10-02" \
  -H "content-type: application/json" \
  -d "{
    \"model\": \"claude-opus-4-7\",
    \"max_tokens\": 4096,
    \"container\": {
      \"skills\": [
        {
          \"type\": \"anthropic\",
          \"skill_id\": \"xlsx\",
          \"version\": \"latest\"
        },
        {
          \"type\": \"custom\",
          \"skill_id\": \"$DCF_SKILL_ID\",
          \"version\": \"latest\"
        }
      ]
    },
    \"messages\": [{
      \"role\": \"user\",
      \"content\": \"Build a DCF valuation model for a SaaS company with the attached financials\"
    }],
    \"tools\": [{
      \"type\": \"code_execution_20250825\",
      \"name\": \"code_execution\"
    }]
  }"
```

```bash CLI nocheck
# Create custom DCF analysis Skill
DCF_SKILL_ID=$(ant beta:skills create \
  --display-title "DCF Analysis" \
  --file dcf_skill/SKILL.md \
  --transform id --format yaml)

# Use with Excel to create financial model
ant beta:messages create \
  --beta code-execution-2025-08-25 \
  --beta skills-2025-10-02 <<YAML
model: claude-opus-4-7
max_tokens: 4096
container:
  skills:
    - type: anthropic
      skill_id: xlsx
      version: latest
    - type: custom
      skill_id: $DCF_SKILL_ID
      version: latest
messages:
  - role: user
    content: Build a DCF valuation model for a SaaS company with the attached financials
tools:
  - type: code_execution_20250825
    name: code_execution
YAML
```

```python Python nocheck
# Create custom DCF analysis Skill
from anthropic.lib import files_from_dir

dcf_skill = client.beta.skills.create(
    display_title="DCF Analysis",
    files=files_from_dir("/path/to/dcf_skill"),
)

# Use with Excel to create financial model
response = client.beta.messages.create(
    model="claude-opus-4-7",
    max_tokens=4096,
    betas=["code-execution-2025-08-25", "skills-2025-10-02"],
    container={
        "skills": [
            {"type": "anthropic", "skill_id": "xlsx", "version": "latest"},
            {"type": "custom", "skill_id": dcf_skill.id, "version": "latest"},
        ]
    },
    messages=[
        {
            "role": "user",
            "content": "Build a DCF valuation model for a SaaS company with the attached financials",
        }
    ],
    tools=[{"type": "code_execution_20250825", "name": "code_execution"}],
)
```

```typescript TypeScript nocheck
// Create custom DCF analysis Skill
import Anthropic, { toFile } from "@anthropic-ai/sdk";
import fs from "fs";

const client = new Anthropic();

const dcfSkill = await client.beta.skills.create({
  display_title: "DCF Analysis",
  files: [await toFile(fs.createReadStream("dcf_skill.zip"), "skill.zip")]
});

// Use with Excel to create financial model
const response = await client.beta.messages.create({
  model: "claude-opus-4-7",
  max_tokens: 4096,
  betas: ["code-execution-2025-08-25", "skills-2025-10-02"],
  container: {
    skills: [
      { type: "anthropic", skill_id: "xlsx", version: "latest" },
      { type: "custom", skill_id: dcfSkill.id, version: "latest" }
    ]
  },
  messages: [
    {
      role: "user",
      content: "Build a DCF valuation model for a SaaS company with the attached financials"
    }
  ],
  tools: [{ type: "code_execution_20250825", name: "code_execution" }]
});
```

```csharp C# nocheck hidelines={1..7}
using System;
using System.Threading.Tasks;
using Anthropic;
using Anthropic.Models.Beta.Messages;

var client = new AnthropicClient();

// Create custom DCF analysis Skill
var dcfSkill = await client.Beta.Skills.Create(new SkillCreateParams
{
    DisplayTitle = "DCF Analysis",
    Files = new[] { new SkillFileParam { Path = "dcf_skill/SKILL.md", Content = skillContent } },
});

// Use with Excel to create financial model
var parameters = new MessageCreateParams
{
    Model = "claude-opus-4-7",
    MaxTokens = 4096,
    Betas = new[] { "code-execution-2025-08-25", "skills-2025-10-02" },
    Container = new BetaContainerParams
    {
        Skills = new[]
        {
            new BetaSkillParam
            {
                Type = "anthropic",
                SkillId = "xlsx",
                Version = "latest"
            },
            new BetaSkillParam
            {
                Type = "custom",
                SkillId = dcfSkill.Id,
                Version = "latest"
            }
        }
    },
    Messages = new[]
    {
        new BetaMessageParam
        {
            Role = Role.User,
            Content = "Build a DCF valuation model for a SaaS company with the attached financials"
        }
    },
    Tools = new[]
    {
        new BetaToolParam
        {
            Type = "code_execution_20250825",
            Name = "code_execution"
        }
    }
};

var message = await client.Beta.Messages.Create(parameters);
Console.WriteLine(message);
```

```go Go nocheck hidelines={1..11,-1}
package main

import (
	"context"
	"fmt"
	"log"

	"github.com/anthropics/anthropic-sdk-go"
)

func main() {
	client := anthropic.NewClient()

	// Create custom DCF analysis Skill (ID obtained from Skills API)
	dcfSkillID := "skill_01AbCdEfGhIjKlMnOpQrStUv"

	// Use with Excel to create financial model
	response, err := client.Beta.Messages.New(context.TODO(), anthropic.BetaMessageNewParams{
		Model:     "claude-opus-4-7",
		MaxTokens: 4096,
		Betas: []anthropic.AnthropicBeta{
			"code-execution-2025-08-25",
			anthropic.AnthropicBetaSkills2025_10_02,
		},
		Container: anthropic.BetaMessageNewParamsContainerUnion{
			OfContainers: &anthropic.BetaContainerParams{
				Skills: []anthropic.BetaSkillParams{
					{
						Type:    anthropic.BetaSkillParamsTypeAnthropic,
						SkillID: "xlsx",
						Version: anthropic.String("latest"),
					},
					{
						Type:    anthropic.BetaSkillParamsTypeCustom,
						SkillID: dcfSkillID,
						Version: anthropic.String("latest"),
					},
				},
			},
		},
		Messages: []anthropic.BetaMessageParam{
			anthropic.NewBetaUserMessage(anthropic.NewBetaTextBlock("Build a DCF valuation model for a SaaS company with the attached financials")),
		},
		Tools: []anthropic.BetaToolUnionParam{
			{OfCodeExecutionTool20250825: &anthropic.BetaCodeExecutionTool20250825Param{}},
		},
	})
	if err != nil {
		log.Fatal(err)
	}
	fmt.Println(response)
}
```

```java Java nocheck hidelines={1..4,8..11,-2..}
import com.anthropic.client.AnthropicClient;
import com.anthropic.client.okhttp.AnthropicOkHttpClient;
import com.anthropic.models.beta.messages.MessageCreateParams;
import com.anthropic.models.beta.messages.BetaMessage;
import com.anthropic.models.beta.messages.BetaContainerParams;
import com.anthropic.models.beta.messages.BetaSkillParams;
import com.anthropic.models.beta.messages.BetaCodeExecutionTool20250825;
import java.util.List;

public class CustomSkillExample {
    public static void main(String[] args) {
        AnthropicClient client = AnthropicOkHttpClient.fromEnv();

        // Create custom DCF analysis Skill (via Skills API)
        String dcfSkillId = "skill_01AbCdEfGhIjKlMnOpQrStUv"; // From Skills API create response

        // Use with Excel Skill to create financial model
        MessageCreateParams params = MessageCreateParams.builder()
            .model("claude-opus-4-7")
            .maxTokens(4096L)
            .addBeta("code-execution-2025-08-25")
            .addBeta("skills-2025-10-02")
            .container(BetaContainerParams.builder()
                .skills(List.of(
                    BetaSkillParams.builder()
                        .type(BetaSkillParams.Type.ANTHROPIC)
                        .skillId("xlsx")
                        .version("latest")
                        .build(),
                    BetaSkillParams.builder()
                        .type(BetaSkillParams.Type.CUSTOM)
                        .skillId(dcfSkillId)
                        .version("latest")
                        .build()
                ))
                .build())
            .addUserMessage("Build a DCF valuation model for a SaaS company with the attached financials")
            .addTool(BetaCodeExecutionTool20250825.builder().build())
            .build();

        BetaMessage response = client.beta().messages().create(params);
        System.out.println(response);
    }
}
```

```php PHP hidelines={1..4} nocheck
<?php

use Anthropic\Client;

$client = new Client(apiKey: getenv("ANTHROPIC_API_KEY"));

// Create custom DCF analysis Skill
$dcfSkillId = "skill_01AbCdEfGhIjKlMnOpQrStUv"; // From API response

// Use with Excel to create financial model
$message = $client->beta->messages->create(
    maxTokens: 4096,
    messages: [
        ['role' => 'user', 'content' => 'Build a DCF valuation model for a SaaS company with the attached financials']
    ],
    model: 'claude-opus-4-7',
    betas: ['code-execution-2025-08-25', 'skills-2025-10-02'],
    container: [
        'skills' => [
            ['type' => 'anthropic', 'skill_id' => 'xlsx', 'version' => 'latest'],
            ['type' => 'custom', 'skill_id' => $dcfSkillId, 'version' => 'latest']
        ]
    ],
    tools: [
        ['type' => 'code_execution_20250825', 'name' => 'code_execution']
    ]
);
echo $message->content[0]->text;
```

```ruby Ruby nocheck hidelines={1..2}
require "anthropic"

client = Anthropic::Client.new

# Create custom DCF analysis Skill
dcf_skill = client.beta.skills.create(
  display_title: "DCF Analysis",
  files: [
    File.open("dcf_skill/SKILL.md", "rb")
  ]
)

# Use with Excel to create financial model
response = client.beta.messages.create(
  model: "claude-opus-4-7",
  max_tokens: 4096,
  betas: ["code-execution-2025-08-25", "skills-2025-10-02"],
  container: {
    skills: [
      { type: "anthropic", skill_id: "xlsx", version: "latest" },
      { type: "custom", skill_id: dcf_skill.id, version: "latest" }
    ]
  },
  messages: [
    { role: "user", content: "Build a DCF valuation model for a SaaS company with the attached financials" }
  ],
  tools: [{ type: "code_execution_20250825", name: "code_execution" }]
)
```
</CodeGroup>

---

## Limits and Constraints

### Request Limits
- **Maximum Skills per request:** 8
- **Maximum Skill upload size:** 30&nbsp;MB (all files combined)
- **YAML frontmatter requirements:**
  - `name`: Maximum 64 characters, lowercase letters/numbers/hyphens only, no XML tags, no reserved words
  - `description`: Maximum 1024 characters, non-empty, no XML tags

### Environment Constraints
Skills run in the code execution container with these limitations:
- **No network access** - Cannot make external API calls
- **No runtime package installation** - Only pre-installed packages available
- **Isolated environment** - Each request gets a fresh container

See the [code execution tool documentation](/docs/en/agents-and-tools/tool-use/code-execution-tool) for available packages.

---

## Best Practices

### When to Use Multiple Skills

Combine Skills when tasks involve multiple document types or domains:

**Good use cases:**
- Data analysis (Excel) + presentation creation (PowerPoint)
- Report generation (Word) + export to PDF
- Custom domain logic + document generation

**Avoid:**
- Including unused Skills (impacts performance)

### Version Management Strategy

**For production:**

```python nocheck
# Pin to specific versions for stability
container = {
    "skills": [
        {
            "type": "custom",
            "skill_id": "skill_01AbCdEfGhIjKlMnOpQrStUv",
            "version": "1759178010641129",  # Specific version
        }
    ]
}
```

**For development:**

```python nocheck
# Use latest for active development
container = {
    "skills": [
        {
            "type": "custom",
            "skill_id": "skill_01AbCdEfGhIjKlMnOpQrStUv",
            "version": "latest",  # Always get newest
        }
    ]
}
```

### Prompt Caching Considerations

When using prompt caching, note that changing the Skills list in your container breaks the cache:

<CodeGroup>
```bash cURL
# First request creates cache
curl https://api.anthropic.com/v1/messages \
  -H "x-api-key: $ANTHROPIC_API_KEY" \
  -H "anthropic-version: 2023-06-01" \
  -H "anthropic-beta: code-execution-2025-08-25,skills-2025-10-02,prompt-caching-2024-07-31" \
  -H "content-type: application/json" \
  -d '{
    "model": "claude-opus-4-7",
    "max_tokens": 4096,
    "container": {
      "skills": [
        {"type": "anthropic", "skill_id": "xlsx", "version": "latest"}
      ]
    },
    "messages": [{"role": "user", "content": "Analyze sales data"}],
    "tools": [{"type": "code_execution_20250825", "name": "code_execution"}]
  }'

# Adding/removing Skills breaks cache
curl https://api.anthropic.com/v1/messages \
  -H "x-api-key: $ANTHROPIC_API_KEY" \
  -H "anthropic-version: 2023-06-01" \
  -H "anthropic-beta: code-execution-2025-08-25,skills-2025-10-02,prompt-caching-2024-07-31" \
  -H "content-type: application/json" \
  -d '{
    "model": "claude-opus-4-7",
    "max_tokens": 4096,
    "container": {
      "skills": [
        {"type": "anthropic", "skill_id": "xlsx", "version": "latest"},
        {"type": "anthropic", "skill_id": "pptx", "version": "latest"}
      ]
    },
    "messages": [{"role": "user", "content": "Create a presentation"}],
    "tools": [{"type": "code_execution_20250825", "name": "code_execution"}]
  }'
```

```bash CLI
# First request creates cache
ant beta:messages create \
  --beta code-execution-2025-08-25 \
  --beta skills-2025-10-02 \
  --beta prompt-caching-2024-07-31 <<'YAML'
model: claude-opus-4-7
max_tokens: 4096
container:
  skills:
    - type: anthropic
      skill_id: xlsx
      version: latest
messages:
  - role: user
    content: Analyze sales data
tools:
  - type: code_execution_20250825
    name: code_execution
YAML

# Adding/removing Skills breaks cache
ant beta:messages create \
  --beta code-execution-2025-08-25 \
  --beta skills-2025-10-02 \
  --beta prompt-caching-2024-07-31 <<'YAML'
model: claude-opus-4-7
max_tokens: 4096
container:
  skills:
    - type: anthropic
      skill_id: xlsx
      version: latest
    - type: anthropic
      skill_id: pptx
      version: latest
messages:
  - role: user
    content: Create a presentation
tools:
  - type: code_execution_20250825
    name: code_execution
YAML
```

```python Python
# First request creates cache
response1 = client.beta.messages.create(
    model="claude-opus-4-7",
    max_tokens=4096,
    betas=[
        "code-execution-2025-08-25",
        "skills-2025-10-02",
        "prompt-caching-2024-07-31",
    ],
    container={
        "skills": [{"type": "anthropic", "skill_id": "xlsx", "version": "latest"}]
    },
    messages=[{"role": "user", "content": "Analyze sales data"}],
    tools=[{"type": "code_execution_20250825", "name": "code_execution"}],
)

# Adding/removing Skills breaks cache
response2 = client.beta.messages.create(
    model="claude-opus-4-7",
    max_tokens=4096,
    betas=[
        "code-execution-2025-08-25",
        "skills-2025-10-02",
        "prompt-caching-2024-07-31",
    ],
    container={
        "skills": [
            {"type": "anthropic", "skill_id": "xlsx", "version": "latest"},
            {
                "type": "anthropic",
                "skill_id": "pptx",
                "version": "latest",
            },  # Cache miss
        ]
    },
    messages=[{"role": "user", "content": "Create a presentation"}],
    tools=[{"type": "code_execution_20250825", "name": "code_execution"}],
)
```

```typescript TypeScript
// First request creates cache
const response1 = await client.beta.messages.create({
  model: "claude-opus-4-7",
  max_tokens: 4096,
  betas: ["code-execution-2025-08-25", "skills-2025-10-02", "prompt-caching-2024-07-31"],
  container: {
    skills: [{ type: "anthropic", skill_id: "xlsx", version: "latest" }]
  },
  messages: [{ role: "user", content: "Analyze sales data" }],
  tools: [{ type: "code_execution_20250825", name: "code_execution" }]
});

// Adding/removing Skills breaks cache
const response2 = await client.beta.messages.create({
  model: "claude-opus-4-7",
  max_tokens: 4096,
  betas: ["code-execution-2025-08-25", "skills-2025-10-02", "prompt-caching-2024-07-31"],
  container: {
    skills: [
      { type: "anthropic", skill_id: "xlsx", version: "latest" },
      { type: "anthropic", skill_id: "pptx", version: "latest" } // Cache miss
    ]
  },
  messages: [{ role: "user", content: "Create a presentation" }],
  tools: [{ type: "code_execution_20250825", name: "code_execution" }]
});
```

```csharp C# nocheck
using System;
using System.Threading.Tasks;
using Anthropic;
using Anthropic.Models.Messages;

public class Program
{
    public static async Task Main(string[] args)
    {
        AnthropicClient client = new();

        // First request creates cache
        var parameters1 = new MessageCreateParams
        {
            Model = "claude-opus-4-7",
            MaxTokens = 4096,
            Betas = new[] { "code-execution-2025-08-25", "skills-2025-10-02", "prompt-caching-2024-07-31" },
            Container = new BetaContainer
            {
                Skills = new[]
                {
                    new BetaSkill { Type = "anthropic", SkillId = "xlsx", Version = "latest" }
                }
            },
            Messages = new[] { new BetaMessageParam { Role = Role.User, Content = "Analyze sales data" } },
            Tools = new[] { new BetaTool { Type = "code_execution_20250825", Name = "code_execution" } }
        };
        var response1 = await client.Beta.Messages.Create(parameters1);
        Console.WriteLine(response1);

        // Adding/removing Skills breaks cache
        var parameters2 = new MessageCreateParams
        {
            Model = "claude-opus-4-7",
            MaxTokens = 4096,
            Betas = new[] { "code-execution-2025-08-25", "skills-2025-10-02", "prompt-caching-2024-07-31" },
            Container = new BetaContainer
            {
                Skills = new[]
                {
                    new BetaSkill { Type = "anthropic", SkillId = "xlsx", Version = "latest" },
                    new BetaSkill { Type = "anthropic", SkillId = "pptx", Version = "latest" }
                }
            },
            Messages = new[] { new BetaMessageParam { Role = Role.User, Content = "Create a presentation" } },
            Tools = new[] { new BetaTool { Type = "code_execution_20250825", Name = "code_execution" } }
        };
        var response2 = await client.Beta.Messages.Create(parameters2);
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

	// First request creates cache
	response1, err := client.Beta.Messages.New(context.TODO(), anthropic.BetaMessageNewParams{
		Model:     "claude-opus-4-7",
		MaxTokens: 4096,
		Betas: []anthropic.AnthropicBeta{
			"code-execution-2025-08-25",
			anthropic.AnthropicBetaSkills2025_10_02,
			anthropic.AnthropicBetaPromptCaching2024_07_31,
		},
		Container: anthropic.BetaMessageNewParamsContainerUnion{
			OfContainers: &anthropic.BetaContainerParams{
				Skills: []anthropic.BetaSkillParams{
					{
						Type:    anthropic.BetaSkillParamsTypeAnthropic,
						SkillID: "xlsx",
						Version: anthropic.String("latest"),
					},
				},
			},
		},
		Messages: []anthropic.BetaMessageParam{
			anthropic.NewBetaUserMessage(anthropic.NewBetaTextBlock("Analyze sales data")),
		},
		Tools: []anthropic.BetaToolUnionParam{
			{OfCodeExecutionTool20250825: &anthropic.BetaCodeExecutionTool20250825Param{}},
		},
	})
	if err != nil {
		log.Fatal(err)
	}
	fmt.Println(response1)

	// Adding/removing Skills breaks cache
	response2, err := client.Beta.Messages.New(context.TODO(), anthropic.BetaMessageNewParams{
		Model:     "claude-opus-4-7",
		MaxTokens: 4096,
		Betas: []anthropic.AnthropicBeta{
			"code-execution-2025-08-25",
			anthropic.AnthropicBetaSkills2025_10_02,
			anthropic.AnthropicBetaPromptCaching2024_07_31,
		},
		Container: anthropic.BetaMessageNewParamsContainerUnion{
			OfContainers: &anthropic.BetaContainerParams{
				Skills: []anthropic.BetaSkillParams{
					{
						Type:    anthropic.BetaSkillParamsTypeAnthropic,
						SkillID: "xlsx",
						Version: anthropic.String("latest"),
					},
					{
						Type:    anthropic.BetaSkillParamsTypeAnthropic,
						SkillID: "pptx",
						Version: anthropic.String("latest"),
					},
				},
			},
		},
		Messages: []anthropic.BetaMessageParam{
			anthropic.NewBetaUserMessage(anthropic.NewBetaTextBlock("Create a presentation")),
		},
		Tools: []anthropic.BetaToolUnionParam{
			{OfCodeExecutionTool20250825: &anthropic.BetaCodeExecutionTool20250825Param{}},
		},
	})
	if err != nil {
		log.Fatal(err)
	}
	fmt.Println(response2)
}
```

```java Java hidelines={1..4,8..11,-2..}
import com.anthropic.client.AnthropicClient;
import com.anthropic.client.okhttp.AnthropicOkHttpClient;
import com.anthropic.models.beta.messages.MessageCreateParams;
import com.anthropic.models.beta.messages.BetaMessage;
import com.anthropic.models.beta.messages.BetaContainerParams;
import com.anthropic.models.beta.messages.BetaSkillParams;
import com.anthropic.models.beta.messages.BetaCodeExecutionTool20250825;
import java.util.List;

public class SkillsCaching {
    public static void main(String[] args) {
        AnthropicClient client = AnthropicOkHttpClient.fromEnv();

        // First request creates cache
        MessageCreateParams params1 = MessageCreateParams.builder()
            .model("claude-opus-4-7")
            .maxTokens(4096L)
            .addBeta("code-execution-2025-08-25")
            .addBeta("skills-2025-10-02")
            .addBeta("prompt-caching-2024-07-31")
            .container(BetaContainerParams.builder()
                .skills(List.of(
                    BetaSkillParams.builder()
                        .type(BetaSkillParams.Type.ANTHROPIC)
                        .skillId("xlsx")
                        .version("latest")
                        .build()
                ))
                .build())
            .addUserMessage("Analyze sales data")
            .addTool(BetaCodeExecutionTool20250825.builder().build())
            .build();

        BetaMessage response1 = client.beta().messages().create(params1);
        System.out.println(response1);

        // Adding/removing Skills breaks cache
        MessageCreateParams params2 = MessageCreateParams.builder()
            .model("claude-opus-4-7")
            .maxTokens(4096L)
            .addBeta("code-execution-2025-08-25")
            .addBeta("skills-2025-10-02")
            .addBeta("prompt-caching-2024-07-31")
            .container(BetaContainerParams.builder()
                .skills(List.of(
                    BetaSkillParams.builder()
                        .type(BetaSkillParams.Type.ANTHROPIC)
                        .skillId("xlsx")
                        .version("latest")
                        .build(),
                    BetaSkillParams.builder()
                        .type(BetaSkillParams.Type.ANTHROPIC)
                        .skillId("pptx")
                        .version("latest")
                        .build()
                ))
                .build())
            .addUserMessage("Create a presentation")
            .addTool(BetaCodeExecutionTool20250825.builder().build())
            .build();

        BetaMessage response2 = client.beta().messages().create(params2);
        System.out.println(response2);
    }
}
```

```php PHP hidelines={1..4}
<?php

use Anthropic\Client;

$client = new Client(apiKey: getenv("ANTHROPIC_API_KEY"));

// First request creates cache
$response1 = $client->beta->messages->create(
    maxTokens: 4096,
    messages: [
        ['role' => 'user', 'content' => 'Analyze sales data']
    ],
    model: 'claude-opus-4-7',
    betas: [
        'code-execution-2025-08-25',
        'skills-2025-10-02',
        'prompt-caching-2024-07-31'
    ],
    container: [
        'skills' => [
            ['type' => 'anthropic', 'skill_id' => 'xlsx', 'version' => 'latest']
        ]
    ],
    tools: [
        ['type' => 'code_execution_20250825', 'name' => 'code_execution']
    ]
);
echo $response1;

// Adding/removing Skills breaks cache
$response2 = $client->beta->messages->create(
    maxTokens: 4096,
    messages: [
        ['role' => 'user', 'content' => 'Create a presentation']
    ],
    model: 'claude-opus-4-7',
    betas: [
        'code-execution-2025-08-25',
        'skills-2025-10-02',
        'prompt-caching-2024-07-31'
    ],
    container: [
        'skills' => [
            ['type' => 'anthropic', 'skill_id' => 'xlsx', 'version' => 'latest'],
            ['type' => 'anthropic', 'skill_id' => 'pptx', 'version' => 'latest']
        ]
    ],
    tools: [
        ['type' => 'code_execution_20250825', 'name' => 'code_execution']
    ]
);
echo $response2;
```

```ruby Ruby hidelines={1..2}
require "anthropic"

client = Anthropic::Client.new

# First request creates cache
response1 = client.beta.messages.create(
  model: "claude-opus-4-7",
  max_tokens: 4096,
  betas: [
    "code-execution-2025-08-25",
    "skills-2025-10-02",
    "prompt-caching-2024-07-31"
  ],
  container: {
    skills: [{ type: "anthropic", skill_id: "xlsx", version: "latest" }]
  },
  messages: [{ role: "user", content: "Analyze sales data" }],
  tools: [{ type: "code_execution_20250825", name: "code_execution" }]
)
puts response1

# Adding/removing Skills breaks cache
response2 = client.beta.messages.create(
  model: "claude-opus-4-7",
  max_tokens: 4096,
  betas: [
    "code-execution-2025-08-25",
    "skills-2025-10-02",
    "prompt-caching-2024-07-31"
  ],
  container: {
    skills: [
      { type: "anthropic", skill_id: "xlsx", version: "latest" },
      { type: "anthropic", skill_id: "pptx", version: "latest" }
    ]
  },
  messages: [{ role: "user", content: "Create a presentation" }],
  tools: [{ type: "code_execution_20250825", name: "code_execution" }]
)
puts response2
```
</CodeGroup>

For best caching performance, keep your Skills list consistent across requests.

### Error Handling

Handle Skill-related errors gracefully:

<CodeGroup>

```bash CLI nocheck
if ! RESULT=$(ant beta:messages create \
  --beta code-execution-2025-08-25 \
  --beta skills-2025-10-02 \
  --transform-error error.message --format-error yaml 2>&1 <<'YAML'
model: claude-opus-4-7
max_tokens: 4096
container:
  skills:
    - type: custom
      skill_id: skill_01AbCdEfGhIjKlMnOpQrStUv
      version: latest
messages:
  - role: user
    content: Process data
tools:
  - type: code_execution_20250825
    name: code_execution
YAML
); then
  case "$RESULT" in
    *skill*)
      printf 'Skill error: %s\n' "$RESULT"
      # Handle skill-specific errors
      ;;
    *)
      printf '%s\n' "$RESULT" >&2
      exit 1
      ;;
  esac
fi
```

```python Python nocheck hidelines={1..2}
import anthropic

client = anthropic.Anthropic()

try:
    response = client.beta.messages.create(
        model="claude-opus-4-7",
        max_tokens=4096,
        betas=["code-execution-2025-08-25", "skills-2025-10-02"],
        container={
            "skills": [
                {
                    "type": "custom",
                    "skill_id": "skill_01AbCdEfGhIjKlMnOpQrStUv",
                    "version": "latest",
                }
            ]
        },
        messages=[{"role": "user", "content": "Process data"}],
        tools=[{"type": "code_execution_20250825", "name": "code_execution"}],
    )
except anthropic.BadRequestError as e:
    if "skill" in str(e):
        print(f"Skill error: {e}")
        # Handle skill-specific errors
    else:
        raise
```

```typescript TypeScript nocheck
try {
  const response = await client.beta.messages.create({
    model: "claude-opus-4-7",
    max_tokens: 4096,
    betas: ["code-execution-2025-08-25", "skills-2025-10-02"],
    container: {
      skills: [
        { type: "custom", skill_id: "skill_01AbCdEfGhIjKlMnOpQrStUv", version: "latest" }
      ]
    },
    messages: [{ role: "user", content: "Process data" }],
    tools: [{ type: "code_execution_20250825", name: "code_execution" }]
  });
} catch (error) {
  if (error instanceof Anthropic.BadRequestError && error.message.includes("skill")) {
    console.error(`Skill error: ${error.message}`);
    // Handle skill-specific errors
  } else {
    throw error;
  }
}
```

```csharp C# nocheck
using System;
using System.Threading.Tasks;
using Anthropic;
using Anthropic.Models.Beta.Messages;

class Program
{
    static async Task Main(string[] args)
    {
        var client = new AnthropicClient();

        try
        {
            var parameters = new MessageCreateParams
            {
                Model = "claude-opus-4-7",
                MaxTokens = 4096,
                Betas = ["code-execution-2025-08-25", "skills-2025-10-02"],
                Container = new BetaContainerParams
                {
                    Skills = [
                        new BetaSkillParam
                        {
                            Type = "custom",
                            SkillId = "skill_01AbCdEfGhIjKlMnOpQrStUv",
                            Version = "latest"
                        }
                    ]
                },
                Messages = [new() { Role = Role.User, Content = "Process data" }],
                Tools = [new BetaToolParam { Type = "code_execution_20250825", Name = "code_execution" }]
            };

            var message = await client.Beta.Messages.Create(parameters);
            Console.WriteLine(message);
        }
        catch (Exception e) when (e.Message.Contains("skill"))
        {
            Console.WriteLine($"Skill error: {e.Message}");
        }
    }
}
```

```go Go nocheck hidelines={1..14,-1}
package main

import (
	"context"
	"fmt"
	"log"
	"strings"

	"github.com/anthropics/anthropic-sdk-go"
)

func main() {
	client := anthropic.NewClient()

	_, err := client.Beta.Messages.New(context.TODO(), anthropic.BetaMessageNewParams{
		Model:     "claude-opus-4-7",
		MaxTokens: 4096,
		Betas:     []anthropic.AnthropicBeta{"code-execution-2025-08-25", anthropic.AnthropicBetaSkills2025_10_02},
		Container: anthropic.BetaMessageNewParamsContainerUnion{
			OfContainers: &anthropic.BetaContainerParams{
				Skills: []anthropic.BetaSkillParams{
					{
						Type:    anthropic.BetaSkillParamsTypeCustom,
						SkillID: "skill_01AbCdEfGhIjKlMnOpQrStUv",
						Version: anthropic.String("latest"),
					},
				},
			},
		},
		Messages: []anthropic.BetaMessageParam{
			anthropic.NewBetaUserMessage(anthropic.NewBetaTextBlock("Process data")),
		},
		Tools: []anthropic.BetaToolUnionParam{
			{OfCodeExecutionTool20250825: &anthropic.BetaCodeExecutionTool20250825Param{}},
		},
	})

	if err != nil {
		if strings.Contains(err.Error(), "skill") {
			fmt.Printf("Skill error: %v\n", err)
		} else {
			log.Fatal(err)
		}
	}
}
```

```java Java nocheck hidelines={1..4,8..10,-2..}
import com.anthropic.client.AnthropicClient;
import com.anthropic.client.okhttp.AnthropicOkHttpClient;
import com.anthropic.models.beta.messages.MessageCreateParams;
import com.anthropic.models.beta.messages.BetaMessage;
import com.anthropic.models.beta.messages.BetaContainerParams;
import com.anthropic.models.beta.messages.BetaSkillParams;
import com.anthropic.models.beta.messages.BetaCodeExecutionTool20250825;

public class SkillErrorHandling {
    public static void main(String[] args) {
        AnthropicClient client = AnthropicOkHttpClient.fromEnv();

        try {
            MessageCreateParams params = MessageCreateParams.builder()
                .model("claude-opus-4-7")
                .maxTokens(4096L)
                .addBeta("code-execution-2025-08-25")
                .addBeta("skills-2025-10-02")
                .container(BetaContainerParams.builder()
                    .addSkill(BetaSkillParams.builder()
                        .type(BetaSkillParams.Type.CUSTOM)
                        .skillId("skill_01AbCdEfGhIjKlMnOpQrStUv")
                        .version("latest")
                        .build())
                    .build())
                .addUserMessage("Process data")
                .addTool(BetaCodeExecutionTool20250825.builder().build())
                .build();

            BetaMessage response = client.beta().messages().create(params);
            System.out.println(response);
        } catch (Exception e) {
            if (e.getMessage().contains("skill")) {
                System.err.println("Skill error: " + e.getMessage());
            } else {
                throw e;
            }
        }
    }
}
```

```php PHP hidelines={1..4} nocheck
<?php

use Anthropic\Client;

$client = new Client(apiKey: getenv("ANTHROPIC_API_KEY"));

try {
    $message = $client->beta->messages->create(
        maxTokens: 4096,
        messages: [
            ['role' => 'user', 'content' => 'Process data']
        ],
        model: 'claude-opus-4-7',
        betas: ['code-execution-2025-08-25', 'skills-2025-10-02'],
        container: [
            'skills' => [
                [
                    'type' => 'custom',
                    'skill_id' => 'skill_01AbCdEfGhIjKlMnOpQrStUv',
                    'version' => 'latest'
                ]
            ]
        ],
        tools: [
            ['type' => 'code_execution_20250825', 'name' => 'code_execution']
        ]
    );
    echo $message->content[0]->text;
} catch (Exception $e) {
    if (str_contains($e->getMessage(), 'skill')) {
        echo "Skill error: " . $e->getMessage();
    } else {
        throw $e;
    }
}
```

```ruby Ruby nocheck hidelines={1..2}
require "anthropic"

client = Anthropic::Client.new

begin
  response = client.beta.messages.create(
    model: "claude-opus-4-7",
    max_tokens: 4096,
    betas: ["code-execution-2025-08-25", "skills-2025-10-02"],
    container: {
      skills: [
        {
          type: "custom",
          skill_id: "skill_01AbCdEfGhIjKlMnOpQrStUv",
          version: "latest"
        }
      ]
    },
    messages: [{ role: "user", content: "Process data" }],
    tools: [{ type: "code_execution_20250825", name: "code_execution" }]
  )
rescue Anthropic::Errors::BadRequestError => e
  if e.message.include?("skill")
    puts "Skill error: #{e.message}"
  else
    raise
  end
end
```
</CodeGroup>

---

## Data retention

Agent Skills are not covered by ZDR arrangements. Skill definitions and execution data are retained according to Anthropic's standard data retention policy.

For ZDR eligibility across all features, see [API and data retention](/docs/en/build-with-claude/api-and-data-retention).

## Next Steps

<CardGroup cols={2}>
  <Card
    title="API Reference"
    icon="book"
    href="/docs/en/api/skills/create-skill"
  >
    Complete API reference with all endpoints
  </Card>
  <Card
    title="Authoring Guide"
    icon="edit"
    href="/docs/en/agents-and-tools/agent-skills/best-practices"
  >
    Best practices for writing effective Skills
  </Card>
  <Card
    title="Code Execution Tool"
    icon="terminal"
    href="/docs/en/agents-and-tools/tool-use/code-execution-tool"
  >
    Learn about the code execution environment
  </Card>
</CardGroup>