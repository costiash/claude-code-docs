# Files API

---

The Files API lets you upload and manage files to use with the Claude API without re-uploading content with each request. This is particularly useful when using the [code execution tool](/docs/en/agents-and-tools/tool-use/code-execution-tool) to provide inputs (e.g. datasets and documents) and then download outputs (e.g. charts). You can also use the Files API to prevent having to continually re-upload frequently used documents and images across multiple API calls. You can [explore the API reference directly](/docs/en/api/files-create), in addition to this guide.

<Note>
The Files API is in beta. Reach out through the [feedback form](https://forms.gle/tisHyierGwgN4DUE9) to share your experience with the Files API.
</Note>

<Note>
This feature is in beta and is **not** covered by [Zero Data Retention (ZDR)](/docs/en/build-with-claude/zero-data-retention) arrangements. Beta features are excluded from ZDR.
</Note>

## Supported models

Referencing a `file_id` in a Messages request is supported in all models that support the given file type. For example, [images](/docs/en/build-with-claude/vision) are supported in all Claude 3+ models, [PDFs](/docs/en/build-with-claude/pdf-support) in all Claude 3.5+ models, and [various other file types](/docs/en/agents-and-tools/tool-use/code-execution-tool#supported-file-types) for the code execution tool in Claude Haiku 4.5 plus all Claude 3.7+ models.

The Files API is currently not supported on Amazon Bedrock or Google Vertex AI.

## How the Files API works

The Files API provides a simple create-once, use-many-times approach for working with files:

- **Upload files** to our secure storage and receive a unique `file_id`
- **Download files** that are created from skills or the code execution tool
- **Reference files** in [Messages](/docs/en/api/messages) requests using the `file_id` instead of re-uploading content
- **Manage your files** with list, retrieve, and delete operations

## How to use the Files API

<Note>
To use the Files API, you'll need to include the beta feature header: `anthropic-beta: files-api-2025-04-14`.
</Note>

### Uploading a file

Upload a file to be referenced in future API calls:

<CodeGroup>
```bash Shell
curl -X POST https://api.anthropic.com/v1/files \
  -H "x-api-key: $ANTHROPIC_API_KEY" \
  -H "anthropic-version: 2023-06-01" \
  -H "anthropic-beta: files-api-2025-04-14" \
  -F "file=@/path/to/document.pdf"
```

```python Python nocheck
import anthropic

client = anthropic.Anthropic()
client.beta.files.upload(
    file=("document.pdf", open("/path/to/document.pdf", "rb"), "application/pdf"),
)
```

```typescript TypeScript nocheck
import Anthropic, { toFile } from "@anthropic-ai/sdk";
import fs from "fs";

const anthropic = new Anthropic();

await anthropic.beta.files.upload({
  file: await toFile(fs.createReadStream("/path/to/document.pdf"), undefined, {
    type: "application/pdf"
  }),
  betas: ["files-api-2025-04-14"]
});
```

```csharp C# nocheck
using Anthropic;

var client = new AnthropicClient();

var file = await client.Beta.Files.Upload(
    new FileUploadParams
    {
        File = File.OpenRead("/path/to/document.pdf")
    });

Console.WriteLine(file.Id);
```

```go Go hidelines={12..16}
package main

import (
	"context"
	"fmt"
	"log"
	"os"

	"github.com/anthropics/anthropic-sdk-go"
)

func init() {
	os.MkdirAll("/path/to", 0755)
	os.WriteFile("/path/to/document.pdf", []byte("%PDF-1.4 test"), 0644)
}

func main() {
	client := anthropic.NewClient()

	file, err := os.Open("/path/to/document.pdf")
	if err != nil {
		log.Fatal(err)
	}
	defer file.Close()

	response, err := client.Beta.Files.Upload(context.Background(),
		anthropic.BetaFileUploadParams{
			File:  file,
			Betas: []anthropic.AnthropicBeta{anthropic.AnthropicBetaFilesAPI2025_04_14},
		})
	if err != nil {
		log.Fatal(err)
	}

	fmt.Println(response.ID)
}
```

```java Java nocheck hidelines={1..8,-1}
import com.anthropic.client.AnthropicClient;
import com.anthropic.client.okhttp.AnthropicOkHttpClient;
import com.anthropic.models.beta.files.FileUploadParams;
import com.anthropic.models.beta.files.FileMetadata;
import java.nio.file.Path;

public class UploadFile {
    public static void main(String[] args) {
        AnthropicClient client = AnthropicOkHttpClient.fromEnv();

        FileMetadata file = client.beta().files().upload(
            FileUploadParams.builder()
                .file(Path.of("/path/to/document.pdf"))
                .build()
        );

        System.out.println(file.id());
    }
}
```

```php PHP nocheck
<?php

use Anthropic\Client;

$client = new Client(
    apiKey: getenv("ANTHROPIC_API_KEY")
);

$file = $client->beta->files->upload(
    file: fopen('/path/to/document.pdf', 'r'),
    betas: ['files-api-2025-04-14'],
);

echo $file->id;
```

```ruby Ruby nocheck
require "anthropic"

client = Anthropic::Client.new

file = client.beta.files.upload(
  file: File.open("/path/to/document.pdf", "rb")
)

puts file.id
```
</CodeGroup>

The response from uploading a file will include:

```json
{
  "id": "file_011CNha8iCJcU1wXNR6q4V8w",
  "type": "file",
  "filename": "document.pdf",
  "mime_type": "application/pdf",
  "size_bytes": 1024000,
  "created_at": "2025-01-01T00:00:00Z",
  "downloadable": false
}
```

### Using a file in messages

Once uploaded, reference the file using its `file_id`:

<CodeGroup>
```bash Shell
curl -X POST https://api.anthropic.com/v1/messages \
  -H "x-api-key: $ANTHROPIC_API_KEY" \
  -H "anthropic-version: 2023-06-01" \
  -H "anthropic-beta: files-api-2025-04-14" \
  -H "content-type: application/json" \
  -d '{
    "model": "claude-opus-4-6",
    "max_tokens": 1024,
    "messages": [
      {
        "role": "user",
        "content": [
          {
            "type": "text",
            "text": "Please summarize this document for me."
          },
          {
            "type": "document",
            "source": {
              "type": "file",
              "file_id": "file_011CNha8iCJcU1wXNR6q4V8w"
            }
          }
        ]
      }
    ]
  }'
```

```python Python nocheck hidelines={1..4,-1}
import anthropic

client = anthropic.Anthropic()

response = client.beta.messages.create(
    model="claude-opus-4-6",
    max_tokens=1024,
    messages=[
        {
            "role": "user",
            "content": [
                {"type": "text", "text": "Please summarize this document for me."},
                {
                    "type": "document",
                    "source": {
                        "type": "file",
                        "file_id": "file_011CNha8iCJcU1wXNR6q4V8w",
                    },
                },
            ],
        }
    ],
    betas=["files-api-2025-04-14"],
)
print(response)
```

```typescript TypeScript nocheck hidelines={1..4}
import Anthropic from "@anthropic-ai/sdk";

const anthropic = new Anthropic();

const response = await anthropic.beta.messages.create({
  model: "claude-opus-4-6",
  max_tokens: 1024,
  messages: [
    {
      role: "user",
      content: [
        {
          type: "text",
          text: "Please summarize this document for me."
        },
        {
          type: "document",
          source: {
            type: "file",
            file_id: "file_011CNha8iCJcU1wXNR6q4V8w"
          }
        }
      ]
    }
  ],
  betas: ["files-api-2025-04-14"]
});

console.log(response);
```

```csharp C# nocheck
using Anthropic;

var client = new AnthropicClient();

var response = await client.Beta.Messages.Create(
    new MessageCreateParams
    {
        Model = "claude-opus-4-6",
        MaxTokens = 1024,
        Betas = new[] { "files-api-2025-04-14" },
        Messages = new[]
        {
            new BetaMessageParam
            {
                Role = "user",
                Content = new object[]
                {
                    new { type = "text", text = "Please summarize this document for me." },
                    new
                    {
                        type = "document",
                        source = new
                        {
                            type = "file",
                            file_id = "file_011CNha8iCJcU1wXNR6q4V8w"
                        }
                    }
                }
            }
        }
    });

Console.WriteLine(response);
```

```go Go nocheck hidelines={1..13,-6..-1}
package main

import (
	"context"
	"fmt"
	"log"

	"github.com/anthropics/anthropic-sdk-go"
)

func main() {
	client := anthropic.NewClient()

	response, err := client.Beta.Messages.New(context.Background(),
		anthropic.BetaMessageNewParams{
			Model:     anthropic.ModelClaudeOpus4_6,
			MaxTokens: 1024,
			Betas:     []anthropic.AnthropicBeta{anthropic.AnthropicBetaFilesAPI2025_04_14},
			Messages: []anthropic.BetaMessageParam{
				anthropic.NewBetaUserMessage(
					anthropic.NewBetaTextBlock("Please summarize this document for me."),
					anthropic.NewBetaDocumentBlock(anthropic.BetaFileDocumentSourceParam{
						FileID: "file_011CNha8iCJcU1wXNR6q4V8w",
					}),
				),
			},
		})
	if err != nil {
		log.Fatal(err)
	}

	fmt.Println(response)
}
```

```java Java nocheck hidelines={1..13,-1}
import com.anthropic.client.AnthropicClient;
import com.anthropic.client.okhttp.AnthropicOkHttpClient;
import com.anthropic.models.messages.Model;
import com.anthropic.models.beta.messages.BetaContentBlockParam;
import com.anthropic.models.beta.messages.BetaMessage;
import com.anthropic.models.beta.messages.BetaRequestDocumentBlock;
import com.anthropic.models.beta.messages.BetaFileDocumentSource;
import com.anthropic.models.beta.messages.BetaTextBlockParam;
import com.anthropic.models.beta.messages.MessageCreateParams;
import java.util.List;

public class UseFileInMessages {
    public static void main(String[] args) {
        AnthropicClient client = AnthropicOkHttpClient.fromEnv();

        MessageCreateParams params = MessageCreateParams.builder()
            .model(Model.CLAUDE_OPUS_4_6)
            .addBeta("files-api-2025-04-14")
            .maxTokens(1024)
            .addUserMessageOfBetaContentBlockParams(List.of(
                BetaContentBlockParam.ofText(BetaTextBlockParam.builder()
                    .text("Please summarize this document for me.")
                    .build()),
                BetaContentBlockParam.ofDocument(BetaRequestDocumentBlock.builder()
                    .source(BetaFileDocumentSource.builder()
                        .fileId("file_011CNha8iCJcU1wXNR6q4V8w")
                        .build())
                    .build())
            ))
            .build();

        BetaMessage message = client.beta().messages().create(params);
        System.out.println(message);
    }
}
```

```php PHP hidelines={1..6} nocheck
<?php

use Anthropic\Client;

$client = new Client(apiKey: getenv("ANTHROPIC_API_KEY"));

$response = $client->beta->messages->create(
    maxTokens: 1024,
    messages: [
        [
            'role' => 'user',
            'content' => [
                ['type' => 'text', 'text' => 'Please summarize this document for me.'],
                [
                    'type' => 'document',
                    'source' => [
                        'type' => 'file',
                        'file_id' => 'file_011CNha8iCJcU1wXNR6q4V8w'
                    ]
                ]
            ]
        ]
    ],
    model: 'claude-opus-4-6',
    betas: ['files-api-2025-04-14'],
);

print_r($response);
```

```ruby Ruby nocheck
require "anthropic"

client = Anthropic::Client.new

response = client.beta.messages.create(
  model: "claude-opus-4-6",
  max_tokens: 1024,
  betas: ["files-api-2025-04-14"],
  messages: [
    {
      role: "user",
      content: [
        { type: "text", text: "Please summarize this document for me." },
        {
          type: "document",
          source: {
            type: "file",
            file_id: "file_011CNha8iCJcU1wXNR6q4V8w"
          }
        }
      ]
    }
  ]
)

puts response
```
</CodeGroup>

### File types and content blocks

The Files API supports different file types that correspond to different content block types:

| File Type | MIME Type | Content Block Type | Use Case |
| :--- | :--- | :--- | :--- |
| PDF | `application/pdf` | `document` | Text analysis, document processing |
| Plain text | `text/plain` | `document` | Text analysis, processing |
| Images | `image/jpeg`, `image/png`, `image/gif`, `image/webp` | `image` | Image analysis, visual tasks |
| [Datasets, others](/docs/en/agents-and-tools/tool-use/code-execution-tool#supported-file-types) | Varies | `container_upload` | Analyze data, create visualizations  |

### Working with other file formats

For file types that are not supported as `document` blocks (.csv, .txt, .md, .docx, .xlsx), convert the files to plain text, and include the content directly in your message:

<CodeGroup>
```bash Shell
# Example: Reading a text file and sending it as plain text
# Note: For files with special characters, consider base64 encoding
TEXT_CONTENT=$(cat document.txt | jq -Rs .)

curl https://api.anthropic.com/v1/messages \
  -H "content-type: application/json" \
  -H "x-api-key: $ANTHROPIC_API_KEY" \
  -H "anthropic-version: 2023-06-01" \
  -d @- <<EOF
{
  "model": "claude-opus-4-6",
  "max_tokens": 1024,
  "messages": [
    {
      "role": "user",
      "content": [
        {
          "type": "text",
          "text": "Here's the document content:\n\n${TEXT_CONTENT}\n\nPlease summarize this document."
        }
      ]
    }
  ]
}
EOF
```

```python Python nocheck hidelines={2..4,-1}
import pandas as pd
import anthropic

client = anthropic.Anthropic()

# Example: Reading a CSV file
df = pd.read_csv("data.csv")
csv_content = df.to_string()

# Send as plain text in the message
response = client.messages.create(
    model="claude-opus-4-6",
    max_tokens=1024,
    messages=[
        {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": f"Here's the CSV data:\n\n{csv_content}\n\nPlease analyze this data.",
                }
            ],
        }
    ],
)

print(response.content[0].text)
```

```typescript TypeScript nocheck hidelines={1}
import Anthropic from "@anthropic-ai/sdk";
import fs from "fs/promises";

const anthropic = new Anthropic();

async function analyzeDocument() {
  // Example: Reading a text file
  const textContent = await fs.readFile("document.txt", "utf-8");

  // Send as plain text in the message
  const response = await anthropic.messages.create({
    model: "claude-opus-4-6",
    max_tokens: 1024,
    messages: [
      {
        role: "user",
        content: [
          {
            type: "text",
            text: `Here's the document content:\n\n${textContent}\n\nPlease summarize this document.`
          }
        ]
      }
    ]
  });

  const block = response.content[0];
  if (block.type === "text") {
    console.log(block.text);
  }
}

analyzeDocument();
```

```csharp C# nocheck
using System;
using System.IO;
using System.Threading.Tasks;
using Anthropic;
using Anthropic.Models.Messages;

class Program
{
    static async Task Main(string[] args)
    {
        AnthropicClient client = new();

        // Example: Reading a text file
        string textContent = await File.ReadAllTextAsync("document.txt");

        var parameters = new MessageCreateParams
        {
            Model = Model.ClaudeOpus4_6,
            MaxTokens = 1024,
            Messages = [new()
            {
                Role = Role.User,
                Content = $"Here's the document content:\n\n{textContent}\n\nPlease summarize this document."
            }]
        };

        var message = await client.Messages.Create(parameters);
        Console.WriteLine(message);
    }
}
```

```go Go hidelines={12..15}
package main

import (
	"context"
	"fmt"
	"log"
	"os"

	"github.com/anthropics/anthropic-sdk-go"
)

func init() {
	os.WriteFile("document.txt", []byte("This is a test document for upload."), 0644)
}

func main() {
	client := anthropic.NewClient()

	// Example: Reading a text file
	textContent, err := os.ReadFile("document.txt")
	if err != nil {
		log.Fatal(err)
	}

	response, err := client.Messages.New(context.TODO(), anthropic.MessageNewParams{
		Model:     anthropic.ModelClaudeOpus4_6,
		MaxTokens: 1024,
		Messages: []anthropic.MessageParam{
			anthropic.NewUserMessage(anthropic.NewTextBlock(
				fmt.Sprintf("Here's the document content:\n\n%s\n\nPlease summarize this document.", string(textContent)),
			)),
		},
	})
	if err != nil {
		log.Fatal(err)
	}

	fmt.Println(response.Content[0].Text)
}
```

```java Java nocheck hidelines={1..11,-1}
import com.anthropic.client.AnthropicClient;
import com.anthropic.client.okhttp.AnthropicOkHttpClient;
import com.anthropic.models.messages.MessageCreateParams;
import com.anthropic.models.messages.Message;
import com.anthropic.models.messages.Model;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.io.IOException;

public class FileUploadExample {
    public static void main(String[] args) throws IOException {
        AnthropicClient client = AnthropicOkHttpClient.fromEnv();

        // Example: Reading a text file
        String textContent = Files.readString(Paths.get("document.txt"));

        MessageCreateParams params = MessageCreateParams.builder()
            .model(Model.CLAUDE_OPUS_4_6)
            .maxTokens(1024L)
            .addUserMessage("Here's the document content:\n\n" + textContent + "\n\nPlease summarize this document.")
            .build();

        Message response = client.messages().create(params);
        response.content().stream()
            .flatMap(block -> block.text().stream())
            .forEach(textBlock -> System.out.println(textBlock.text()));
    }
}
```

```php PHP hidelines={1..6} nocheck
<?php

use Anthropic\Client;

$client = new Client(apiKey: getenv("ANTHROPIC_API_KEY"));

// Example: Reading a text file
$textContent = file_get_contents("document.txt");

$message = $client->messages->create(
    maxTokens: 1024,
    messages: [
        [
            'role' => 'user',
            'content' => [
                [
                    'type' => 'text',
                    'text' => "Here's the document content:\n\n{$textContent}\n\nPlease summarize this document."
                ]
            ]
        ]
    ],
    model: 'claude-opus-4-6',
);

echo $message->content[0]->text;
```

```ruby Ruby nocheck
require "anthropic"

client = Anthropic::Client.new

# Example: Reading a text file
text_content = File.read("document.txt")

message = client.messages.create(
  model: "claude-opus-4-6",
  max_tokens: 1024,
  messages: [
    {
      role: "user",
      content: [
        {
          type: "text",
          text: "Here's the document content:\n\n#{text_content}\n\nPlease summarize this document."
        }
      ]
    }
  ]
)

puts message.content.first.text
```
</CodeGroup>

<Note>
For .docx files containing images, convert them to PDF format first, then use [PDF support](/docs/en/build-with-claude/pdf-support) to take advantage of the built-in image parsing. This allows using citations from the PDF document.
</Note>

#### Document blocks

For PDFs and text files, use the `document` content block:

```json
{
  "type": "document",
  "source": {
    "type": "file",
    "file_id": "file_011CNha8iCJcU1wXNR6q4V8w"
  },
  "title": "Document Title", // Optional
  "context": "Context about the document", // Optional
  "citations": { "enabled": true } // Optional, enables citations
}
```

#### Image blocks

For images, use the `image` content block:

```json
{
  "type": "image",
  "source": {
    "type": "file",
    "file_id": "file_011CPMxVD3fHLUhvTqtsQA5w"
  }
}
```

### Managing files

#### List files

Retrieve a list of your uploaded files:

<CodeGroup>
```bash Shell
curl https://api.anthropic.com/v1/files \
  -H "x-api-key: $ANTHROPIC_API_KEY" \
  -H "anthropic-version: 2023-06-01" \
  -H "anthropic-beta: files-api-2025-04-14"
```

```python Python hidelines={1..3}
import anthropic

client = anthropic.Anthropic()
files = client.beta.files.list()
```

```typescript TypeScript
import Anthropic from "@anthropic-ai/sdk";

const anthropic = new Anthropic();
const files = await anthropic.beta.files.list({
  betas: ["files-api-2025-04-14"]
});
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

        var files = await client.Beta.Files.List(new FileListParams
        {
            Betas = ["files-api-2025-04-14"]
        });
        Console.WriteLine(files);
    }
}
```

```go Go hidelines={1..13,-1}
package main

import (
	"context"
	"fmt"
	"log"

	"github.com/anthropics/anthropic-sdk-go"
)

func main() {
	client := anthropic.NewClient()

	files, err := client.Beta.Files.List(context.TODO(), anthropic.BetaFileListParams{
		Betas: []anthropic.AnthropicBeta{anthropic.AnthropicBetaFilesAPI2025_04_14},
	})
	if err != nil {
		log.Fatal(err)
	}
	fmt.Println(files)
}
```

```java Java hidelines={1..6,-1}
import com.anthropic.client.AnthropicClient;
import com.anthropic.client.okhttp.AnthropicOkHttpClient;
import com.anthropic.models.beta.files.FileListPage;

public class ListFiles {
    public static void main(String[] args) {
        AnthropicClient client = AnthropicOkHttpClient.fromEnv();

        FileListPage files = client.beta().files().list();
        System.out.println(files);
    }
}
```

```php PHP hidelines={1..6}
<?php

use Anthropic\Client;

$client = new Client(apiKey: getenv("ANTHROPIC_API_KEY"));

$files = $client->beta->files->list(
    betas: ['files-api-2025-04-14'],
);
print_r($files);
```

```ruby Ruby
require "anthropic"

client = Anthropic::Client.new

files = client.beta.files.list(
  betas: ["files-api-2025-04-14"]
)
puts files
```
</CodeGroup>

#### Get file metadata

Retrieve information about a specific file:

<CodeGroup>
```bash Shell
curl https://api.anthropic.com/v1/files/file_011CNha8iCJcU1wXNR6q4V8w \
  -H "x-api-key: $ANTHROPIC_API_KEY" \
  -H "anthropic-version: 2023-06-01" \
  -H "anthropic-beta: files-api-2025-04-14"
```

```python Python nocheck hidelines={1..3}
import anthropic

client = anthropic.Anthropic()
file = client.beta.files.retrieve_metadata("file_011CNha8iCJcU1wXNR6q4V8w")
```

```typescript TypeScript nocheck
import Anthropic from "@anthropic-ai/sdk";

const anthropic = new Anthropic();
const file = await anthropic.beta.files.retrieveMetadata("file_011CNha8iCJcU1wXNR6q4V8w", {
  betas: ["files-api-2025-04-14"]
});
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

        var file = await client.Beta.Files.RetrieveMetadata("file_011CNha8iCJcU1wXNR6q4V8w");
        Console.WriteLine(file);
    }
}
```

```go Go nocheck hidelines={1..13,-6..-1}
package main

import (
	"context"
	"fmt"
	"log"

	"github.com/anthropics/anthropic-sdk-go"
)

func main() {
	client := anthropic.NewClient()

	file, err := client.Beta.Files.GetMetadata(
		context.TODO(),
		"file_011CNha8iCJcU1wXNR6q4V8w",
		anthropic.BetaFileGetMetadataParams{
			Betas: []anthropic.AnthropicBeta{anthropic.AnthropicBetaFilesAPI2025_04_14},
		},
	)
	if err != nil {
		log.Fatal(err)
	}

	fmt.Println(file)
}
```

```java Java nocheck hidelines={1..6,-1}
import com.anthropic.client.AnthropicClient;
import com.anthropic.client.okhttp.AnthropicOkHttpClient;
import com.anthropic.models.beta.files.FileMetadata;

public class RetrieveFileMetadata {
    public static void main(String[] args) {
        AnthropicClient client = AnthropicOkHttpClient.fromEnv();

        FileMetadata file = client.beta().files().retrieveMetadata(
            "file_011CNha8iCJcU1wXNR6q4V8w"
        );

        System.out.println(file);
    }
}
```

```php PHP hidelines={1..6} nocheck
<?php

use Anthropic\Client;

$client = new Client(apiKey: getenv("ANTHROPIC_API_KEY"));

$file = $client->beta->files->retrieveMetadata(
    fileID: 'file_011CNha8iCJcU1wXNR6q4V8w',
    betas: ['files-api-2025-04-14'],
);
echo $file;
```

```ruby Ruby nocheck
require "anthropic"

client = Anthropic::Client.new

file = client.beta.files.retrieve_metadata("file_011CNha8iCJcU1wXNR6q4V8w")
puts file
```
</CodeGroup>

#### Delete a file

Remove a file from your workspace:

<CodeGroup>
```bash Shell
curl -X DELETE https://api.anthropic.com/v1/files/file_011CNha8iCJcU1wXNR6q4V8w \
  -H "x-api-key: $ANTHROPIC_API_KEY" \
  -H "anthropic-version: 2023-06-01" \
  -H "anthropic-beta: files-api-2025-04-14"
```

```python Python nocheck hidelines={1..3}
import anthropic

client = anthropic.Anthropic()
result = client.beta.files.delete("file_011CNha8iCJcU1wXNR6q4V8w")
```

```typescript TypeScript nocheck
import Anthropic from "@anthropic-ai/sdk";

const anthropic = new Anthropic();
await anthropic.beta.files.delete("file_011CNha8iCJcU1wXNR6q4V8w", {
  betas: ["files-api-2025-04-14"]
});
```

```csharp C# nocheck
using System;
using System.Threading.Tasks;
using Anthropic;

class Program
{
    static async Task Main()
    {
        AnthropicClient client = new();

        await client.Beta.Files.Delete("file_011CNha8iCJcU1wXNR6q4V8w");
    }
}
```

```go Go nocheck hidelines={1..12,-4..-1}
package main

import (
	"context"
	"log"

	"github.com/anthropics/anthropic-sdk-go"
)

func main() {
	client := anthropic.NewClient()

	_, err := client.Beta.Files.Delete(
		context.TODO(),
		"file_011CNha8iCJcU1wXNR6q4V8w",
		anthropic.BetaFileDeleteParams{
			Betas: []anthropic.AnthropicBeta{anthropic.AnthropicBetaFilesAPI2025_04_14},
		},
	)
	if err != nil {
		log.Fatal(err)
	}
}
```

```java Java nocheck hidelines={1..5,-1}
import com.anthropic.client.AnthropicClient;
import com.anthropic.client.okhttp.AnthropicOkHttpClient;

public class DeleteFile {
    public static void main(String[] args) {
        AnthropicClient client = AnthropicOkHttpClient.fromEnv();

        client.beta().files().delete("file_011CNha8iCJcU1wXNR6q4V8w");
    }
}
```

```php PHP hidelines={1..6} nocheck
<?php

use Anthropic\Client;

$client = new Client(apiKey: getenv("ANTHROPIC_API_KEY"));

$result = $client->beta->files->delete(
    fileID: 'file_011CNha8iCJcU1wXNR6q4V8w',
    betas: ['files-api-2025-04-14'],
);
```

```ruby Ruby nocheck
require "anthropic"

client = Anthropic::Client.new

result = client.beta.files.delete("file_011CNha8iCJcU1wXNR6q4V8w")
```
</CodeGroup>

### Downloading a file

Download files that have been created by skills or the code execution tool:

<CodeGroup>
```bash Shell
curl -X GET "https://api.anthropic.com/v1/files/file_011CNha8iCJcU1wXNR6q4V8w/content" \
  -H "x-api-key: $ANTHROPIC_API_KEY" \
  -H "anthropic-version: 2023-06-01" \
  -H "anthropic-beta: files-api-2025-04-14" \
  --output downloaded_file.txt
```

```python Python nocheck hidelines={1..3}
import anthropic

client = anthropic.Anthropic()
file_content = client.beta.files.download("file_011CNha8iCJcU1wXNR6q4V8w")

# Save to file
with open("downloaded_file.txt", "w") as f:
    f.write(file_content.decode("utf-8"))
```

```typescript TypeScript nocheck hidelines={1}
import Anthropic from "@anthropic-ai/sdk";
import fs from "fs/promises";

const anthropic = new Anthropic();

const response = await anthropic.beta.files.download("file_011CNha8iCJcU1wXNR6q4V8w", {
  betas: ["files-api-2025-04-14"]
});

// Save to file
const content = Buffer.from(await response.arrayBuffer());
await fs.writeFile("downloaded_file.txt", content);
```

```csharp C# nocheck
using System;
using System.IO;
using System.Threading.Tasks;
using Anthropic;

class Program
{
    static async Task Main(string[] args)
    {
        AnthropicClient client = new();

        byte[] fileContent = await client.Beta.Files.Download("file_011CNha8iCJcU1wXNR6q4V8w");

        await File.WriteAllBytesAsync("downloaded_file.txt", fileContent);
    }
}
```

```go Go nocheck hidelines={1..14,-4..-1}
package main

import (
	"context"
	"io"
	"log"
	"os"

	"github.com/anthropics/anthropic-sdk-go"
)

func main() {
	client := anthropic.NewClient()

	resp, err := client.Beta.Files.Download(
		context.TODO(),
		"file_011CNha8iCJcU1wXNR6q4V8w",
		anthropic.BetaFileDownloadParams{
			Betas: []anthropic.AnthropicBeta{anthropic.AnthropicBetaFilesAPI2025_04_14},
		},
	)
	if err != nil {
		log.Fatal(err)
	}
	defer resp.Body.Close()

	fileContent, err := io.ReadAll(resp.Body)
	if err != nil {
		log.Fatal(err)
	}

	err = os.WriteFile("downloaded_file.txt", fileContent, 0644)
	if err != nil {
		log.Fatal(err)
	}
}
```

```java Java nocheck hidelines={1..11,-1}
import com.anthropic.client.AnthropicClient;
import com.anthropic.client.okhttp.AnthropicOkHttpClient;
import com.anthropic.core.http.HttpResponse;
import java.io.IOException;
import java.io.InputStream;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.StandardCopyOption;

public class DownloadFile {
    public static void main(String[] args) throws IOException {
        AnthropicClient client = AnthropicOkHttpClient.fromEnv();

        try (HttpResponse response = client.beta().files().download(
                "file_011CNha8iCJcU1wXNR6q4V8w")) {
            try (InputStream body = response.body()) {
                Files.copy(body, Path.of("downloaded_file.txt"),
                    StandardCopyOption.REPLACE_EXISTING);
            }
        }
    }
}
```

```php PHP hidelines={1..6} nocheck
<?php

use Anthropic\Client;

$client = new Client(apiKey: getenv("ANTHROPIC_API_KEY"));

$fileContent = $client->beta->files->download(
    fileID: 'file_011CNha8iCJcU1wXNR6q4V8w',
    betas: ['files-api-2025-04-14'],
);

file_put_contents("downloaded_file.txt", $fileContent);
```

```ruby Ruby nocheck
require "anthropic"

client = Anthropic::Client.new

file_content = client.beta.files.download("file_011CNha8iCJcU1wXNR6q4V8w")

File.binwrite("downloaded_file.txt", file_content.read)
```
</CodeGroup>

<Note>
You can only download files that were created by [skills](/docs/en/build-with-claude/skills-guide) or the [code execution tool](/docs/en/agents-and-tools/tool-use/code-execution-tool). Files that you uploaded cannot be downloaded.
</Note>

---

## File storage and limits

### Storage limits

- **Maximum file size:** 500 MB per file
- **Total storage:** 100 GB per organization

### File lifecycle

- Files are scoped to the workspace of the API key. Other API keys can use files created by any other API key associated with the same workspace
- Files persist until you delete them
- Deleted files cannot be recovered
- Files are inaccessible via the API shortly after deletion, but they may persist in active `Messages` API calls and associated tool uses
- Files that users delete will be deleted in accordance with our [data retention policy](https://privacy.claude.com/en/articles/7996866-how-long-do-you-store-my-organization-s-data).

---

## Error handling

Common errors when using the Files API include:

- **File not found (404):** The specified `file_id` doesn't exist or you don't have access to it
- **Invalid file type (400):** The file type doesn't match the content block type (e.g., using an image file in a document block)
- **Exceeds context window size (400):** The file is larger than the context window size (e.g. using a 500 MB plaintext file in a `/v1/messages` request)
- **Invalid filename (400):** Filename doesn't meet the length requirements (1-255 characters) or contains forbidden characters (`<`, `>`, `:`, `"`, `|`, `?`, `*`, `\`, `/`, or unicode characters 0-31)
- **File too large (413):** File exceeds the 500 MB limit
- **Storage limit exceeded (403):** Your organization has reached the 100 GB storage limit

```json
{
  "type": "error",
  "error": {
    "type": "invalid_request_error",
    "message": "File not found: file_011CNha8iCJcU1wXNR6q4V8w"
  }
}
```

## Usage and billing

File API operations are **free**:
- Uploading files
- Downloading files
- Listing files
- Getting file metadata
- Deleting files

File content used in `Messages` requests are priced as input tokens. You can only download files created by [skills](/docs/en/build-with-claude/skills-guide) or the [code execution tool](/docs/en/agents-and-tools/tool-use/code-execution-tool).

### Rate limits

During the beta period:
- File-related API calls are limited to approximately 100 requests per minute
- [Contact us](mailto:sales@anthropic.com) if you need higher limits for your use case