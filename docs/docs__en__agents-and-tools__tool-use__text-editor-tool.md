# Text editor tool

---

<Note>
This feature is eligible for [Zero Data Retention (ZDR)](/docs/en/build-with-claude/api-and-data-retention). When your organization has a ZDR arrangement, data sent through this feature is not stored after the API response is returned.
</Note>

Claude can use an Anthropic-schema text editor tool to view and modify text files, helping you debug, fix, and improve your code or other text documents. This allows Claude to directly interact with your files, providing hands-on assistance rather than just suggesting changes.

For model support, see the [Tool reference](/docs/en/agents-and-tools/tool-use/tool-reference).

## When to use the text editor tool

Some examples of when to use the text editor tool are:
- **Code debugging:** Have Claude identify and fix bugs in your code, from syntax errors to logic issues.
- **Code refactoring:** Let Claude improve your code structure, readability, and performance through targeted edits.
- **Documentation generation:** Ask Claude to add docstrings, comments, or README files to your codebase.
- **Test creation:** Have Claude create unit tests for your code based on its understanding of the implementation.

## Use the text editor tool

Provide the text editor tool (named `str_replace_based_edit_tool`) to Claude using the Messages API.

You can optionally specify a `max_characters` parameter to control truncation when viewing large files.

<Note>
`max_characters` is only compatible with `text_editor_20250728` and later versions of the text editor tool.
</Note>

<CodeGroup>

```bash cURL
curl https://api.anthropic.com/v1/messages \
  -H "content-type: application/json" \
  -H "x-api-key: $ANTHROPIC_API_KEY" \
  -H "anthropic-version: 2023-06-01" \
  -d '{
    "model": "claude-opus-4-8",
    "max_tokens": 1024,
    "tools": [
      {
        "type": "text_editor_20250728",
        "name": "str_replace_based_edit_tool",
        "max_characters": 10000
      }
    ],
    "messages": [
      {
        "role": "user",
        "content": "There'\''s a syntax error in my primes.py file. Can you help me fix it?"
      }
    ]
  }'
```

```bash CLI
ant messages create \
  --model claude-opus-4-8 \
  --max-tokens 1024 \
  --tool '{type: text_editor_20250728, name: str_replace_based_edit_tool, max_characters: 10000}' \
  --message '{role: user, content: There is a syntax error in my primes.py file. Can you help me fix it?}'
```

```python Python hidelines={1..2}
import anthropic

client = anthropic.Anthropic()

response = client.messages.create(
    model="claude-opus-4-8",
    max_tokens=1024,
    tools=[
        {
            "type": "text_editor_20250728",
            "name": "str_replace_based_edit_tool",
            "max_characters": 10000,
        }
    ],
    messages=[
        {
            "role": "user",
            "content": "There's a syntax error in my primes.py file. Can you help me fix it?",
        }
    ],
)

print(response)
```

```typescript TypeScript hidelines={1..2}
import Anthropic from "@anthropic-ai/sdk";

const anthropic = new Anthropic();

const response = await anthropic.messages.create({
  model: "claude-opus-4-8",
  max_tokens: 1024,
  tools: [
    {
      type: "text_editor_20250728",
      name: "str_replace_based_edit_tool",
      max_characters: 10000
    }
  ],
  messages: [
    {
      role: "user",
      content: "There's a syntax error in my primes.py file. Can you help me fix it?"
    }
  ]
});

console.log(response);
```

```csharp C# hidelines={1..3}
using Anthropic;
using Anthropic.Models.Messages;

var client = new AnthropicClient();

var response = await client.Messages.Create(
    new()
    {
        Model = Model.ClaudeOpus4_8,
        MaxTokens = 1024,
        Tools = [new ToolTextEditor20250728 { MaxCharacters = 10000 }],
        Messages =
        [
            new()
            {
                Role = Role.User,
                Content = "There's a syntax error in my primes.py file. Can you help me fix it?",
            },
        ],
    }
);

Console.WriteLine(response);
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

	response, err := client.Messages.New(context.TODO(), anthropic.MessageNewParams{
		Model:     anthropic.ModelClaudeOpus4_8,
		MaxTokens: 1024,
		Tools: []anthropic.ToolUnionParam{
			{OfTextEditor20250728: &anthropic.ToolTextEditor20250728Param{
				MaxCharacters: anthropic.Int(10000),
			}},
		},
		Messages: []anthropic.MessageParam{
			anthropic.NewUserMessage(anthropic.NewTextBlock("There's a syntax error in my primes.py file. Can you help me fix it?")),
		},
	})
	if err != nil {
		log.Fatal(err)
	}
	fmt.Println(response)
}
```

```java Java hidelines={1..5,7..8,-1..}
import com.anthropic.client.AnthropicClient;
import com.anthropic.client.okhttp.AnthropicOkHttpClient;
import com.anthropic.models.messages.Message;
import com.anthropic.models.messages.MessageCreateParams;
import com.anthropic.models.messages.Model;
import com.anthropic.models.messages.ToolTextEditor20250728;

void main() {
  AnthropicClient client = AnthropicOkHttpClient.fromEnv();

  ToolTextEditor20250728 editorTool =
    ToolTextEditor20250728.builder()
      .maxCharacters(10000L)
      .build();

  MessageCreateParams params = MessageCreateParams.builder()
    .model(Model.CLAUDE_OPUS_4_8)
    .maxTokens(1024)
    .addTool(editorTool)
    .addUserMessage("There's a syntax error in my primes.py file. Can you help me fix it?")
    .build();

  Message message = client.messages().create(params);
  IO.println(message);
}
```

```php PHP hidelines={1..5}
<?php

use Anthropic\Client;
use Anthropic\Messages\ToolTextEditor20250728;

$client = new Client();

$response = $client->messages->create(
    model: 'claude-opus-4-8',
    maxTokens: 1024,
    tools: [ToolTextEditor20250728::with(maxCharacters: 10000)],
    messages: [
        [
            'role' => 'user',
            'content' => "There's a syntax error in my primes.py file. Can you help me fix it?",
        ],
    ],
);

echo $response;
```

```ruby Ruby hidelines={1..2}
require "anthropic"

client = Anthropic::Client.new

response = client.messages.create(
  model: "claude-opus-4-8",
  max_tokens: 1024,
  tools: [
    {
      type: "text_editor_20250728",
      name: "str_replace_based_edit_tool",
      max_characters: 10000
    }
  ],
  messages: [
    {
      role: "user",
      content: "There's a syntax error in my primes.py file. Can you help me fix it?"
    }
  ]
)

puts response
```
</CodeGroup>

The text editor tool can be used in the following way:

<Steps>
  <Step title="Provide Claude with the text editor tool and a user prompt">
    - Include the text editor tool in your API request
    - Provide a user prompt that may require examining or modifying files, such as "Can you fix the syntax error in my code?"
  </Step>
  <Step title="Claude uses the tool to examine files or directories">
    - Claude assesses what it needs to look at and uses the `view` command to examine file contents or list directory contents
    - The API response will contain a `tool_use` content block with the `view` command
  </Step>
  <Step title="Execute the view command and return results">
    - Extract the file or directory path from Claude's tool use request
    - Read the file's contents or list the directory contents
    - If a `max_characters` parameter was specified in the tool configuration, truncate the file contents to that length
    - Return the results to Claude by continuing the conversation with a new `user` message containing a `tool_result` content block
  </Step>
  <Step title="Claude uses the tool to modify files">
    - After examining the file or directory, Claude may use a command such as `str_replace` to make changes or `insert` to add text at a specific line number.
    - If Claude uses the `str_replace` command, Claude constructs a properly formatted tool use request with the old text and new text to replace it with
  </Step>
  <Step title="Execute the edit and return results">
    - Extract the file path, old text, and new text from Claude's tool use request
    - Perform the text replacement in the file
    - Return the results to Claude
  </Step>
  <Step title="Claude provides its analysis and explanation">
    - After examining and possibly editing the files, Claude provides a complete explanation of what it found and what changes it made
  </Step>
</Steps>

### Text editor tool commands

The text editor tool supports several commands for viewing and modifying files:

#### view

The `view` command allows Claude to examine the contents of a file or list the contents of a directory. It can read the entire file or a specific range of lines.

Parameters:
- `command`: Must be "view"
- `path`: The path to the file or directory to view
- `view_range` (optional): An array of two integers specifying the start and end line numbers to view. Line numbers are 1-indexed, and -1 for the end line means read to the end of the file. This parameter only applies when viewing files, not directories.

<section title="Example view commands">

Example for viewing a file:

```json
{
  "type": "tool_use",
  "id": "toolu_01A09q90qw90lq917835lq9",
  "name": "str_replace_based_edit_tool",
  "input": {
    "command": "view",
    "path": "primes.py"
  }
}
```

Example for viewing a directory:

```json
{
  "type": "tool_use",
  "id": "toolu_02B19r91rw91mr917835mr9",
  "name": "str_replace_based_edit_tool",
  "input": {
    "command": "view",
    "path": "src/"
  }
}
```

</section>

#### str_replace

The `str_replace` command allows Claude to replace a specific string in a file with a new string. This is used for making precise edits.

Parameters:
- `command`: Must be "str_replace"
- `path`: The path to the file to modify
- `old_str`: The text to replace (must match exactly, including whitespace and indentation)
- `new_str`: The new text to insert in place of the old text

<section title="Example str_replace command">

```json
{
  "type": "tool_use",
  "id": "toolu_01A09q90qw90lq917835lq9",
  "name": "str_replace_based_edit_tool",
  "input": {
    "command": "str_replace",
    "path": "primes.py",
    "old_str": "for num in range(2, limit + 1)",
    "new_str": "for num in range(2, limit + 1):"
  }
}
```

</section>

#### create

The `create` command allows Claude to create a new file with specified content.

Parameters:
- `command`: Must be "create"
- `path`: The path where the new file should be created
- `file_text`: The content to write to the new file

<section title="Example create command">

```json
{
  "type": "tool_use",
  "id": "toolu_01A09q90qw90lq917835lq9",
  "name": "str_replace_based_edit_tool",
  "input": {
    "command": "create",
    "path": "test_primes.py",
    "file_text": "import unittest\nimport primes\n\nclass TestPrimes(unittest.TestCase):\n    def test_is_prime(self):\n        self.assertTrue(primes.is_prime(2))\n        self.assertTrue(primes.is_prime(3))\n        self.assertFalse(primes.is_prime(4))\n\nif __name__ == '__main__':\n    unittest.main()"
  }
}
```

</section>

#### insert

The `insert` command allows Claude to insert text at a specific location in a file.

Parameters:
- `command`: Must be "insert"
- `path`: The path to the file to modify
- `insert_line`: The line number after which to insert the text (0 for beginning of file)
- `insert_text`: The text to insert

<section title="Example insert command">

```json
{
  "type": "tool_use",
  "id": "toolu_01A09q90qw90lq917835lq9",
  "name": "str_replace_based_edit_tool",
  "input": {
    "command": "insert",
    "path": "primes.py",
    "insert_line": 0,
    "insert_text": "\"\"\"Module for working with prime numbers.\n\nThis module provides functions to check if a number is prime\nand to generate a list of prime numbers up to a given limit.\n\"\"\"\n"
  }
}
```

</section>

### Example: Fixing a syntax error with the text editor tool

This example demonstrates how Claude uses the text editor tool to fix a syntax error in a Python file.

First, your application provides Claude with the text editor tool and a prompt to fix a syntax error:

<CodeGroup>
```bash cURL
curl https://api.anthropic.com/v1/messages \
  -H "content-type: application/json" \
  -H "x-api-key: $ANTHROPIC_API_KEY" \
  -H "anthropic-version: 2023-06-01" \
  -d '{
    "model": "claude-opus-4-8",
    "max_tokens": 1024,
    "tools": [
      {
        "type": "text_editor_20250728",
        "name": "str_replace_based_edit_tool"
      }
    ],
    "messages": [
      {
        "role": "user",
        "content": "There'\''s a syntax error in my primes.py file. Can you help me fix it?"
      }
    ]
  }'
```

```bash CLI
ant messages create \
  --model claude-opus-4-8 \
  --max-tokens 1024 \
  --tool '{type: text_editor_20250728, name: str_replace_based_edit_tool}' \
  --message '{role: user, content: There is a syntax error in my primes.py file. Can you help me fix it?}'
```

```python Python hidelines={1..2}
import anthropic

client = anthropic.Anthropic()

response = client.messages.create(
    model="claude-opus-4-8",
    max_tokens=1024,
    tools=[{"type": "text_editor_20250728", "name": "str_replace_based_edit_tool"}],
    messages=[
        {
            "role": "user",
            "content": "There's a syntax error in my primes.py file. Can you help me fix it?",
        }
    ],
)

print(response)
```

```typescript TypeScript hidelines={1..2}
import Anthropic from "@anthropic-ai/sdk";

const anthropic = new Anthropic();

const response = await anthropic.messages.create({
  model: "claude-opus-4-8",
  max_tokens: 1024,
  tools: [
    {
      type: "text_editor_20250728",
      name: "str_replace_based_edit_tool"
    }
  ],
  messages: [
    {
      role: "user",
      content: "There's a syntax error in my primes.py file. Can you help me fix it?"
    }
  ]
});

console.log(response);
```

```csharp C# hidelines={1..3}
using Anthropic;
using Anthropic.Models.Messages;

var client = new AnthropicClient();

var response = await client.Messages.Create(
    new()
    {
        Model = Model.ClaudeOpus4_8,
        MaxTokens = 1024,
        Tools = [new ToolTextEditor20250728()],
        Messages =
        [
            new()
            {
                Role = Role.User,
                Content = "There's a syntax error in my primes.py file. Can you help me fix it?",
            },
        ],
    }
);

Console.WriteLine(response);
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

	response, err := client.Messages.New(context.TODO(), anthropic.MessageNewParams{
		Model:     anthropic.ModelClaudeOpus4_8,
		MaxTokens: 1024,
		Tools: []anthropic.ToolUnionParam{
			{OfTextEditor20250728: &anthropic.ToolTextEditor20250728Param{}},
		},
		Messages: []anthropic.MessageParam{
			anthropic.NewUserMessage(anthropic.NewTextBlock("There's a syntax error in my primes.py file. Can you help me fix it?")),
		},
	})
	if err != nil {
		log.Fatal(err)
	}
	fmt.Println(response)
}
```

```java Java hidelines={1..5,7..8,-1..}
import com.anthropic.client.AnthropicClient;
import com.anthropic.client.okhttp.AnthropicOkHttpClient;
import com.anthropic.models.messages.Message;
import com.anthropic.models.messages.MessageCreateParams;
import com.anthropic.models.messages.Model;
import com.anthropic.models.messages.ToolTextEditor20250728;

void main() {
  AnthropicClient client = AnthropicOkHttpClient.fromEnv();

  ToolTextEditor20250728 editorTool =
    ToolTextEditor20250728.builder().build();

  MessageCreateParams params = MessageCreateParams.builder()
    .model(Model.CLAUDE_OPUS_4_8)
    .maxTokens(1024)
    .addTool(editorTool)
    .addUserMessage("There's a syntax error in my primes.py file. Can you help me fix it?")
    .build();

  Message message = client.messages().create(params);
  IO.println(message);
}
```

```php PHP hidelines={1..5}
<?php

use Anthropic\Client;
use Anthropic\Messages\ToolTextEditor20250728;

$client = new Client();

$response = $client->messages->create(
    model: 'claude-opus-4-8',
    maxTokens: 1024,
    tools: [new ToolTextEditor20250728()],
    messages: [
        [
            'role' => 'user',
            'content' => "There's a syntax error in my primes.py file. Can you help me fix it?",
        ],
    ],
);

echo $response;
```

```ruby Ruby hidelines={1..2}
require "anthropic"

client = Anthropic::Client.new

response = client.messages.create(
  model: "claude-opus-4-8",
  max_tokens: 1024,
  tools: [{type: "text_editor_20250728", name: "str_replace_based_edit_tool"}],
  messages: [
    {
      role: "user",
      content: "There's a syntax error in my primes.py file. Can you help me fix it?"
    }
  ]
)

puts response
```
</CodeGroup>

Claude uses the text editor tool first to view the file:

```json Output
{
  "id": "msg_01XAbCDeFgHiJkLmNoPQrStU",
  "model": "claude-opus-4-8",
  "stop_reason": "tool_use",
  "role": "assistant",
  "content": [
    {
      "type": "text",
      "text": "I'll help you fix the syntax error in your primes.py file. First, let me take a look at the file to identify the issue."
    },
    {
      "type": "tool_use",
      "id": "toolu_01AbCdEfGhIjKlMnOpQrStU",
      "name": "str_replace_based_edit_tool",
      "input": {
        "command": "view",
        "path": "primes.py"
      }
    }
  ]
}
```

Your application should then read the file and return its contents to Claude:

<CodeGroup>
```bash cURL
curl https://api.anthropic.com/v1/messages \
  -H "content-type: application/json" \
  -H "x-api-key: $ANTHROPIC_API_KEY" \
  -H "anthropic-version: 2023-06-01" \
  -d '{
    "model": "claude-opus-4-8",
    "max_tokens": 1024,
    "tools": [
      {
        "type": "text_editor_20250728",
        "name": "str_replace_based_edit_tool"
      }
    ],
    "messages": [
      {
        "role": "user",
        "content": "There'\''s a syntax error in my primes.py file. Can you help me fix it?"
      },
      {
        "role": "assistant",
        "content": [
          {
            "type": "text",
            "text": "I'\''ll help you fix the syntax error in your primes.py file. First, let me take a look at the file to identify the issue."
          },
          {
            "type": "tool_use",
            "id": "toolu_01AbCdEfGhIjKlMnOpQrStU",
            "name": "str_replace_based_edit_tool",
            "input": {
              "command": "view",
              "path": "primes.py"
            }
          }
        ]
      },
      {
        "role": "user",
        "content": [
          {
            "type": "tool_result",
            "tool_use_id": "toolu_01AbCdEfGhIjKlMnOpQrStU",
            "content": "1: def is_prime(n):\n2:     \"\"\"Check if a number is prime.\"\"\"\n3:     if n <= 1:\n4:         return False\n5:     if n <= 3:\n6:         return True\n7:     if n % 2 == 0 or n % 3 == 0:\n8:         return False\n9:     i = 5\n10:     while i * i <= n:\n11:         if n % i == 0 or n % (i + 2) == 0:\n12:             return False\n13:         i += 6\n14:     return True\n15: \n16: def get_primes(limit):\n17:     \"\"\"Generate a list of prime numbers up to the given limit.\"\"\"\n18:     primes = []\n19:     for num in range(2, limit + 1)\n20:         if is_prime(num):\n21:             primes.append(num)\n22:     return primes\n23: \n24: def main():\n25:     \"\"\"Main function to demonstrate prime number generation.\"\"\"\n26:     limit = 100\n27:     prime_list = get_primes(limit)\n28:     print(f\"Prime numbers up to {limit}:\")\n29:     print(prime_list)\n30:     print(f\"Found {len(prime_list)} prime numbers.\")\n31: \n32: if __name__ == \"__main__\":\n33:     main()"
          }
        ]
      }
    ]
  }'
```

```bash CLI
ant messages create <<'YAML'
model: claude-opus-4-8
max_tokens: 1024
tools:
  - type: text_editor_20250728
    name: str_replace_based_edit_tool
messages:
  - role: user
    content: There's a syntax error in my primes.py file. Can you help me fix it?
  - role: assistant
    content:
      - type: text
        text: >-
          I'll help you fix the syntax error in your primes.py file. First,
          let me take a look at the file to identify the issue.
      - type: tool_use
        id: toolu_01AbCdEfGhIjKlMnOpQrStU
        name: str_replace_based_edit_tool
        input:
          command: view
          path: primes.py
  - role: user
    content:
      - type: tool_result
        tool_use_id: toolu_01AbCdEfGhIjKlMnOpQrStU
        content: |-
          1: def is_prime(n):
          2:     """Check if a number is prime."""
          3:     if n <= 1:
          4:         return False
          5:     if n <= 3:
          6:         return True
          7:     if n % 2 == 0 or n % 3 == 0:
          8:         return False
          9:     i = 5
          10:     while i * i <= n:
          11:         if n % i == 0 or n % (i + 2) == 0:
          12:             return False
          13:         i += 6
          14:     return True
          15:
          16: def get_primes(limit):
          17:     """Generate a list of prime numbers up to the given limit."""
          18:     primes = []
          19:     for num in range(2, limit + 1)
          20:         if is_prime(num):
          21:             primes.append(num)
          22:     return primes
          23:
          24: def main():
          25:     """Main function to demonstrate prime number generation."""
          26:     limit = 100
          27:     prime_list = get_primes(limit)
          28:     print(f"Prime numbers up to {limit}:")
          29:     print(prime_list)
          30:     print(f"Found {len(prime_list)} prime numbers.")
          31:
          32: if __name__ == "__main__":
          33:     main()
YAML
```

```python Python
response = client.messages.create(
    model="claude-opus-4-8",
    max_tokens=1024,
    tools=[{"type": "text_editor_20250728", "name": "str_replace_based_edit_tool"}],
    messages=[
        {
            "role": "user",
            "content": "There's a syntax error in my primes.py file. Can you help me fix it?",
        },
        {
            "role": "assistant",
            "content": [
                {
                    "type": "text",
                    "text": "I'll help you fix the syntax error in your primes.py file. First, let me take a look at the file to identify the issue.",
                },
                {
                    "type": "tool_use",
                    "id": "toolu_01AbCdEfGhIjKlMnOpQrStU",
                    "name": "str_replace_based_edit_tool",
                    "input": {"command": "view", "path": "primes.py"},
                },
            ],
        },
        {
            "role": "user",
            "content": [
                {
                    "type": "tool_result",
                    "tool_use_id": "toolu_01AbCdEfGhIjKlMnOpQrStU",
                    "content": '1: def is_prime(n):\n2:     """Check if a number is prime."""\n3:     if n <= 1:\n4:         return False\n5:     if n <= 3:\n6:         return True\n7:     if n % 2 == 0 or n % 3 == 0:\n8:         return False\n9:     i = 5\n10:     while i * i <= n:\n11:         if n % i == 0 or n % (i + 2) == 0:\n12:             return False\n13:         i += 6\n14:     return True\n15: \n16: def get_primes(limit):\n17:     """Generate a list of prime numbers up to the given limit."""\n18:     primes = []\n19:     for num in range(2, limit + 1)\n20:         if is_prime(num):\n21:             primes.append(num)\n22:     return primes\n23: \n24: def main():\n25:     """Main function to demonstrate prime number generation."""\n26:     limit = 100\n27:     prime_list = get_primes(limit)\n28:     print(f"Prime numbers up to {limit}:")\n29:     print(prime_list)\n30:     print(f"Found {len(prime_list)} prime numbers.")\n31: \n32: if __name__ == "__main__":\n33:     main()',
                }
            ],
        },
    ],
)

print(response)
```

```typescript TypeScript hidelines={1..2}
import Anthropic from "@anthropic-ai/sdk";

const anthropic = new Anthropic();

const response = await anthropic.messages.create({
  model: "claude-opus-4-8",
  max_tokens: 1024,
  tools: [
    {
      type: "text_editor_20250728",
      name: "str_replace_based_edit_tool"
    }
  ],
  messages: [
    {
      role: "user",
      content: "There's a syntax error in my primes.py file. Can you help me fix it?"
    },
    {
      role: "assistant",
      content: [
        {
          type: "text",
          text: "I'll help you fix the syntax error in your primes.py file. First, let me take a look at the file to identify the issue."
        },
        {
          type: "tool_use",
          id: "toolu_01AbCdEfGhIjKlMnOpQrStU",
          name: "str_replace_based_edit_tool",
          input: {
            command: "view",
            path: "primes.py"
          }
        }
      ]
    },
    {
      role: "user",
      content: [
        {
          type: "tool_result",
          tool_use_id: "toolu_01AbCdEfGhIjKlMnOpQrStU",
          content:
            '1: def is_prime(n):\n2:     """Check if a number is prime."""\n3:     if n <= 1:\n4:         return False\n5:     if n <= 3:\n6:         return True\n7:     if n % 2 == 0 or n % 3 == 0:\n8:         return False\n9:     i = 5\n10:     while i * i <= n:\n11:         if n % i == 0 or n % (i + 2) == 0:\n12:             return False\n13:         i += 6\n14:     return True\n15: \n16: def get_primes(limit):\n17:     """Generate a list of prime numbers up to the given limit."""\n18:     primes = []\n19:     for num in range(2, limit + 1)\n20:         if is_prime(num):\n21:             primes.append(num)\n22:     return primes\n23: \n24: def main():\n25:     """Main function to demonstrate prime number generation."""\n26:     limit = 100\n27:     prime_list = get_primes(limit)\n28:     print(f"Prime numbers up to {limit}:")\n29:     print(prime_list)\n30:     print(f"Found {len(prime_list)} prime numbers.")\n31: \n32: if __name__ == "__main__":\n33:     main()'
        }
      ]
    }
  ]
});

console.log(response);
```

```csharp C# hidelines={1..4}
using System.Text.Json;
using Anthropic;
using Anthropic.Models.Messages;

var client = new AnthropicClient();

var response = await client.Messages.Create(
    new()
    {
        Model = Model.ClaudeOpus4_8,
        MaxTokens = 1024,
        Tools = [new ToolTextEditor20250728()],
        Messages =
        [
            new()
            {
                Role = Role.User,
                Content = "There's a syntax error in my primes.py file. Can you help me fix it?",
            },
            new()
            {
                Role = Role.Assistant,
                Content = new MessageParamContent(new List<ContentBlockParam>
                {
                    new ContentBlockParam(new TextBlockParam()
                    {
                        Text = "I'll help you fix the syntax error in your primes.py file. First, let me take a look at the file to identify the issue.",
                    }),
                    new ContentBlockParam(new ToolUseBlockParam()
                    {
                        ID = "toolu_01AbCdEfGhIjKlMnOpQrStU",
                        Name = "str_replace_based_edit_tool",
                        Input = new Dictionary<string, JsonElement>
                        {
                            ["command"] = JsonSerializer.SerializeToElement("view"),
                            ["path"] = JsonSerializer.SerializeToElement("primes.py"),
                        },
                    }),
                }),
            },
            new()
            {
                Role = Role.User,
                Content = new MessageParamContent(new List<ContentBlockParam>
                {
                    new ContentBlockParam(new ToolResultBlockParam()
                    {
                        ToolUseID = "toolu_01AbCdEfGhIjKlMnOpQrStU",
                        Content = "1: def is_prime(n):\n2:     \"\"\"Check if a number is prime.\"\"\"\n3:     if n <= 1:\n4:         return False\n5:     if n <= 3:\n6:         return True\n7:     if n % 2 == 0 or n % 3 == 0:\n8:         return False\n9:     i = 5\n10:     while i * i <= n:\n11:         if n % i == 0 or n % (i + 2) == 0:\n12:             return False\n13:         i += 6\n14:     return True\n15: \n16: def get_primes(limit):\n17:     \"\"\"Generate a list of prime numbers up to the given limit.\"\"\"\n18:     primes = []\n19:     for num in range(2, limit + 1)\n20:         if is_prime(num):\n21:             primes.append(num)\n22:     return primes\n23: \n24: def main():\n25:     \"\"\"Main function to demonstrate prime number generation.\"\"\"\n26:     limit = 100\n27:     prime_list = get_primes(limit)\n28:     print(f\"Prime numbers up to {limit}:\")\n29:     print(prime_list)\n30:     print(f\"Found {len(prime_list)} prime numbers.\")\n31: \n32: if __name__ == \"__main__\":\n33:     main()",
                    }),
                }),
            },
        ],
    }
);

Console.WriteLine(response);
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

	response, err := client.Messages.New(context.TODO(), anthropic.MessageNewParams{
		Model:     anthropic.ModelClaudeOpus4_8,
		MaxTokens: 1024,
		Tools: []anthropic.ToolUnionParam{
			{OfTextEditor20250728: &anthropic.ToolTextEditor20250728Param{}},
		},
		Messages: []anthropic.MessageParam{
			anthropic.NewUserMessage(anthropic.NewTextBlock("There's a syntax error in my primes.py file. Can you help me fix it?")),
			anthropic.NewAssistantMessage(
				anthropic.NewTextBlock("I'll help you fix the syntax error in your primes.py file. First, let me take a look at the file to identify the issue."),
				anthropic.NewToolUseBlock(
					"toolu_01AbCdEfGhIjKlMnOpQrStU",
					map[string]any{"command": "view", "path": "primes.py"},
					"str_replace_based_edit_tool",
				),
			),
			anthropic.NewUserMessage(
				anthropic.NewToolResultBlock(
					"toolu_01AbCdEfGhIjKlMnOpQrStU",
					"1: def is_prime(n):\n2:     \"\"\"Check if a number is prime.\"\"\"\n3:     if n <= 1:\n4:         return False\n5:     if n <= 3:\n6:         return True\n7:     if n % 2 == 0 or n % 3 == 0:\n8:         return False\n9:     i = 5\n10:     while i * i <= n:\n11:         if n % i == 0 or n % (i + 2) == 0:\n12:             return False\n13:         i += 6\n14:     return True\n15: \n16: def get_primes(limit):\n17:     \"\"\"Generate a list of prime numbers up to the given limit.\"\"\"\n18:     primes = []\n19:     for num in range(2, limit + 1)\n20:         if is_prime(num):\n21:             primes.append(num)\n22:     return primes\n23: \n24: def main():\n25:     \"\"\"Main function to demonstrate prime number generation.\"\"\"\n26:     limit = 100\n27:     prime_list = get_primes(limit)\n28:     print(f\"Prime numbers up to {limit}:\")\n29:     print(prime_list)\n30:     print(f\"Found {len(prime_list)} prime numbers.\")\n31: \n32: if __name__ == \"__main__\":\n33:     main()",
					false,
				),
			),
		},
	})
	if err != nil {
		log.Fatal(err)
	}
	fmt.Println(response)
}
```

```java Java hidelines={1..9,11..16,-2..}
import com.anthropic.client.AnthropicClient;
import com.anthropic.client.okhttp.AnthropicOkHttpClient;
import com.anthropic.core.JsonValue;
import com.anthropic.models.messages.ContentBlockParam;
import com.anthropic.models.messages.Message;
import com.anthropic.models.messages.MessageCreateParams;
import com.anthropic.models.messages.Model;
import com.anthropic.models.messages.TextBlockParam;
import com.anthropic.models.messages.ToolResultBlockParam;
import com.anthropic.models.messages.ToolTextEditor20250728;
import com.anthropic.models.messages.ToolUseBlockParam;
import java.util.List;

public class TextEditorToolResultExample {

  public static void main(String[] args) {
    AnthropicClient client = AnthropicOkHttpClient.fromEnv();

    MessageCreateParams params = MessageCreateParams.builder()
      .model(Model.CLAUDE_OPUS_4_8)
      .maxTokens(1024)
      .addTool(ToolTextEditor20250728.builder().build())
      .addUserMessage("There's a syntax error in my primes.py file. Can you help me fix it?")
      .addAssistantMessageOfBlockParams(
        List.of(
          ContentBlockParam.ofText(
            TextBlockParam.builder()
              .text("I'll help you fix the syntax error in your primes.py file. First, let me take a look at the file to identify the issue.")
              .build()
          ),
          ContentBlockParam.ofToolUse(
            ToolUseBlockParam.builder()
              .id("toolu_01AbCdEfGhIjKlMnOpQrStU")
              .name("str_replace_based_edit_tool")
              .input(
                ToolUseBlockParam.Input.builder()
                  .putAdditionalProperty("command", JsonValue.from("view"))
                  .putAdditionalProperty("path", JsonValue.from("primes.py"))
                  .build()
              )
              .build()
          )
        )
      )
      .addUserMessageOfBlockParams(
        List.of(
          ContentBlockParam.ofToolResult(
            ToolResultBlockParam.builder()
              .toolUseId("toolu_01AbCdEfGhIjKlMnOpQrStU")
              .content("1: def is_prime(n):\n2:     \"\"\"Check if a number is prime.\"\"\"\n3:     if n <= 1:\n4:         return False\n5:     if n <= 3:\n6:         return True\n7:     if n % 2 == 0 or n % 3 == 0:\n8:         return False\n9:     i = 5\n10:     while i * i <= n:\n11:         if n % i == 0 or n % (i + 2) == 0:\n12:             return False\n13:         i += 6\n14:     return True\n15: \n16: def get_primes(limit):\n17:     \"\"\"Generate a list of prime numbers up to the given limit.\"\"\"\n18:     primes = []\n19:     for num in range(2, limit + 1)\n20:         if is_prime(num):\n21:             primes.append(num)\n22:     return primes\n23: \n24: def main():\n25:     \"\"\"Main function to demonstrate prime number generation.\"\"\"\n26:     limit = 100\n27:     prime_list = get_primes(limit)\n28:     print(f\"Prime numbers up to {limit}:\")\n29:     print(prime_list)\n30:     print(f\"Found {len(prime_list)} prime numbers.\")\n31: \n32: if __name__ == \"__main__\":\n33:     main()")
              .build()
          )
        )
      )
      .build();

    Message message = client.messages().create(params);
    System.out.println(message);
  }
}
```

```php PHP hidelines={1..5}
<?php

use Anthropic\Client;
use Anthropic\Messages\ToolTextEditor20250728;

$client = new Client();

$response = $client->messages->create(
    model: 'claude-opus-4-8',
    maxTokens: 1024,
    tools: [new ToolTextEditor20250728()],
    messages: [
        [
            'role' => 'user',
            'content' => "There's a syntax error in my primes.py file. Can you help me fix it?",
        ],
        [
            'role' => 'assistant',
            'content' => [
                [
                    'type' => 'text',
                    'text' => "I'll help you fix the syntax error in your primes.py file. First, let me take a look at the file to identify the issue.",
                ],
                [
                    'type' => 'tool_use',
                    'id' => 'toolu_01AbCdEfGhIjKlMnOpQrStU',
                    'name' => 'str_replace_based_edit_tool',
                    'input' => ['command' => 'view', 'path' => 'primes.py'],
                ],
            ],
        ],
        [
            'role' => 'user',
            'content' => [
                [
                    'type' => 'tool_result',
                    'tool_use_id' => 'toolu_01AbCdEfGhIjKlMnOpQrStU',
                    'content' => "1: def is_prime(n):\n2:     \"\"\"Check if a number is prime.\"\"\"\n3:     if n <= 1:\n4:         return False\n5:     if n <= 3:\n6:         return True\n7:     if n % 2 == 0 or n % 3 == 0:\n8:         return False\n9:     i = 5\n10:     while i * i <= n:\n11:         if n % i == 0 or n % (i + 2) == 0:\n12:             return False\n13:         i += 6\n14:     return True\n15: \n16: def get_primes(limit):\n17:     \"\"\"Generate a list of prime numbers up to the given limit.\"\"\"\n18:     primes = []\n19:     for num in range(2, limit + 1)\n20:         if is_prime(num):\n21:             primes.append(num)\n22:     return primes\n23: \n24: def main():\n25:     \"\"\"Main function to demonstrate prime number generation.\"\"\"\n26:     limit = 100\n27:     prime_list = get_primes(limit)\n28:     print(f\"Prime numbers up to {limit}:\")\n29:     print(prime_list)\n30:     print(f\"Found {len(prime_list)} prime numbers.\")\n31: \n32: if __name__ == \"__main__\":\n33:     main()",
                ],
            ],
        ],
    ],
);

echo $response;
```

```ruby Ruby hidelines={1..2}
require "anthropic"

client = Anthropic::Client.new

response = client.messages.create(
  model: "claude-opus-4-8",
  max_tokens: 1024,
  tools: [{type: "text_editor_20250728", name: "str_replace_based_edit_tool"}],
  messages: [
    {
      role: "user",
      content: "There's a syntax error in my primes.py file. Can you help me fix it?"
    },
    {
      role: "assistant",
      content: [
        {
          type: "text",
          text: "I'll help you fix the syntax error in your primes.py file. First, let me take a look at the file to identify the issue."
        },
        {
          type: "tool_use",
          id: "toolu_01AbCdEfGhIjKlMnOpQrStU",
          name: "str_replace_based_edit_tool",
          input: {command: "view", path: "primes.py"}
        }
      ]
    },
    {
      role: "user",
      content: [
        {
          type: "tool_result",
          tool_use_id: "toolu_01AbCdEfGhIjKlMnOpQrStU",
          content: "1: def is_prime(n):\n2:     \"\"\"Check if a number is prime.\"\"\"\n3:     if n <= 1:\n4:         return False\n5:     if n <= 3:\n6:         return True\n7:     if n % 2 == 0 or n % 3 == 0:\n8:         return False\n9:     i = 5\n10:     while i * i <= n:\n11:         if n % i == 0 or n % (i + 2) == 0:\n12:             return False\n13:         i += 6\n14:     return True\n15: \n16: def get_primes(limit):\n17:     \"\"\"Generate a list of prime numbers up to the given limit.\"\"\"\n18:     primes = []\n19:     for num in range(2, limit + 1)\n20:         if is_prime(num):\n21:             primes.append(num)\n22:     return primes\n23: \n24: def main():\n25:     \"\"\"Main function to demonstrate prime number generation.\"\"\"\n26:     limit = 100\n27:     prime_list = get_primes(limit)\n28:     print(f\"Prime numbers up to {limit}:\")\n29:     print(prime_list)\n30:     print(f\"Found {len(prime_list)} prime numbers.\")\n31: \n32: if __name__ == \"__main__\":\n33:     main()"
        }
      ]
    }
  ]
)

puts response
```
</CodeGroup>

<Tip>
**Line numbers**

In the example above, the `view` tool result includes file contents with line numbers prepended to each line (e.g., "1: def is_prime(n):"). Line numbers are not required, but they are essential for successfully using the `view_range` parameter to examine specific sections of files and the `insert_line` parameter to add content at precise locations.
</Tip>

Claude identifies the syntax error and uses the `str_replace` command to fix it:

```json Output
{
  "id": "msg_01VwXyZAbCdEfGhIjKlMnO",
  "model": "claude-opus-4-8",
  "stop_reason": "tool_use",
  "role": "assistant",
  "content": [
    {
      "type": "text",
      "text": "I found the syntax error in your primes.py file. In the `get_primes` function, there is a missing colon (:) at the end of the for loop line. Let me fix that for you."
    },
    {
      "type": "tool_use",
      "id": "toolu_01PqRsTuVwXyZAbCdEfGh",
      "name": "str_replace_based_edit_tool",
      "input": {
        "command": "str_replace",
        "path": "primes.py",
        "old_str": "    for num in range(2, limit + 1)",
        "new_str": "    for num in range(2, limit + 1):"
      }
    }
  ]
}
```

Your application should then make the edit and return the result:

<CodeGroup>
```bash cURL
curl https://api.anthropic.com/v1/messages \
  -H "content-type: application/json" \
  -H "x-api-key: $ANTHROPIC_API_KEY" \
  -H "anthropic-version: 2023-06-01" \
  -d '{
    "model": "claude-opus-4-8",
    "max_tokens": 1024,
    "tools": [
      {
        "type": "text_editor_20250728",
        "name": "str_replace_based_edit_tool"
      }
    ],
    "messages": [
      {
        "role": "assistant",
        "content": [
          {
            "type": "text",
            "text": "I found the syntax error in your primes.py file. In the `get_primes` function, there is a missing colon (:) at the end of the for loop line. Let me fix that for you."
          },
          {
            "type": "tool_use",
            "id": "toolu_01PqRsTuVwXyZAbCdEfGh",
            "name": "str_replace_based_edit_tool",
            "input": {
              "command": "str_replace",
              "path": "primes.py",
              "old_str": "    for num in range(2, limit + 1)",
              "new_str": "    for num in range(2, limit + 1):"
            }
          }
        ]
      },
      {
        "role": "user",
        "content": [
          {
            "type": "tool_result",
            "tool_use_id": "toolu_01PqRsTuVwXyZAbCdEfGh",
            "content": "Successfully replaced text at exactly one location."
          }
        ]
      }
    ]
  }'
```

```bash CLI nocheck
ant messages create <<'YAML'
model: claude-opus-4-8
max_tokens: 1024
tools:
  - type: text_editor_20250728
    name: str_replace_based_edit_tool
messages:
  # Previous messages...
  - role: assistant
    content:
      - type: text
        text: >-
          I found the syntax error in your primes.py file. In the `get_primes`
          function, there is a missing colon (:) at the end of the for loop
          line. Let me fix that for you.
      - type: tool_use
        id: toolu_01PqRsTuVwXyZAbCdEfGh
        name: str_replace_based_edit_tool
        input:
          command: str_replace
          path: primes.py
          old_str: "    for num in range(2, limit + 1)"
          new_str: "    for num in range(2, limit + 1):"
  - role: user
    content:
      - type: tool_result
        tool_use_id: toolu_01PqRsTuVwXyZAbCdEfGh
        content: Successfully replaced text at exactly one location.
YAML
```

```python Python
response = client.messages.create(
    model="claude-opus-4-8",
    max_tokens=1024,
    tools=[{"type": "text_editor_20250728", "name": "str_replace_based_edit_tool"}],
    messages=[
        # Previous messages...
        {
            "role": "assistant",
            "content": [
                {
                    "type": "text",
                    "text": "I found the syntax error in your primes.py file. In the `get_primes` function, there is a missing colon (:) at the end of the for loop line. Let me fix that for you.",
                },
                {
                    "type": "tool_use",
                    "id": "toolu_01PqRsTuVwXyZAbCdEfGh",
                    "name": "str_replace_based_edit_tool",
                    "input": {
                        "command": "str_replace",
                        "path": "primes.py",
                        "old_str": "    for num in range(2, limit + 1)",
                        "new_str": "    for num in range(2, limit + 1):",
                    },
                },
            ],
        },
        {
            "role": "user",
            "content": [
                {
                    "type": "tool_result",
                    "tool_use_id": "toolu_01PqRsTuVwXyZAbCdEfGh",
                    "content": "Successfully replaced text at exactly one location.",
                }
            ],
        },
    ],
)

print(response)
```

```typescript TypeScript
const response = await client.messages.create({
  model: "claude-opus-4-8",
  max_tokens: 1024,
  tools: [
    {
      type: "text_editor_20250728",
      name: "str_replace_based_edit_tool"
    }
  ],
  messages: [
    // Previous messages...
    {
      role: "assistant",
      content: [
        {
          type: "text",
          text: "I found the syntax error in your primes.py file. In the `get_primes` function, there is a missing colon (:) at the end of the for loop line. Let me fix that for you."
        },
        {
          type: "tool_use",
          id: "toolu_01PqRsTuVwXyZAbCdEfGh",
          name: "str_replace_based_edit_tool",
          input: {
            command: "str_replace",
            path: "primes.py",
            old_str: "    for num in range(2, limit + 1)",
            new_str: "    for num in range(2, limit + 1):"
          }
        }
      ]
    },
    {
      role: "user",
      content: [
        {
          type: "tool_result",
          tool_use_id: "toolu_01PqRsTuVwXyZAbCdEfGh",
          content: "Successfully replaced text at exactly one location."
        }
      ]
    }
  ]
});

console.log(response);
```

```csharp C# hidelines={1..4}
using System.Text.Json;
using Anthropic;
using Anthropic.Models.Messages;

var client = new AnthropicClient();

var response = await client.Messages.Create(
    new()
    {
        Model = Model.ClaudeOpus4_8,
        MaxTokens = 1024,
        Tools = [new ToolTextEditor20250728()],
        Messages =
        [
            // Previous messages...
            new()
            {
                Role = Role.Assistant,
                Content = new MessageParamContent(new List<ContentBlockParam>
                {
                    new ContentBlockParam(new TextBlockParam()
                    {
                        Text = "I found the syntax error in your primes.py file. In the `get_primes` function, there is a missing colon (:) at the end of the for loop line. Let me fix that for you.",
                    }),
                    new ContentBlockParam(new ToolUseBlockParam()
                    {
                        ID = "toolu_01PqRsTuVwXyZAbCdEfGh",
                        Name = "str_replace_based_edit_tool",
                        Input = new Dictionary<string, JsonElement>
                        {
                            ["command"] = JsonSerializer.SerializeToElement("str_replace"),
                            ["path"] = JsonSerializer.SerializeToElement("primes.py"),
                            ["old_str"] = JsonSerializer.SerializeToElement("    for num in range(2, limit + 1)"),
                            ["new_str"] = JsonSerializer.SerializeToElement("    for num in range(2, limit + 1):"),
                        },
                    }),
                }),
            },
            new()
            {
                Role = Role.User,
                Content = new MessageParamContent(new List<ContentBlockParam>
                {
                    new ContentBlockParam(new ToolResultBlockParam()
                    {
                        ToolUseID = "toolu_01PqRsTuVwXyZAbCdEfGh",
                        Content = "Successfully replaced text at exactly one location.",
                    }),
                }),
            },
        ],
    }
);

Console.WriteLine(response);
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

	response, err := client.Messages.New(context.TODO(), anthropic.MessageNewParams{
		Model:     anthropic.ModelClaudeOpus4_8,
		MaxTokens: 1024,
		Tools: []anthropic.ToolUnionParam{
			{OfTextEditor20250728: &anthropic.ToolTextEditor20250728Param{}},
		},
		Messages: []anthropic.MessageParam{
			// Previous messages...
			anthropic.NewAssistantMessage(
				anthropic.NewTextBlock("I found the syntax error in your primes.py file. In the `get_primes` function, there is a missing colon (:) at the end of the for loop line. Let me fix that for you."),
				anthropic.NewToolUseBlock(
					"toolu_01PqRsTuVwXyZAbCdEfGh",
					map[string]any{
						"command": "str_replace",
						"path":    "primes.py",
						"old_str": "    for num in range(2, limit + 1)",
						"new_str": "    for num in range(2, limit + 1):",
					},
					"str_replace_based_edit_tool",
				),
			),
			anthropic.NewUserMessage(
				anthropic.NewToolResultBlock(
					"toolu_01PqRsTuVwXyZAbCdEfGh",
					"Successfully replaced text at exactly one location.",
					false,
				),
			),
		},
	})
	if err != nil {
		log.Fatal(err)
	}
	fmt.Println(response)
}
```

```java Java hidelines={1..9,11..16,-2..}
import com.anthropic.client.AnthropicClient;
import com.anthropic.client.okhttp.AnthropicOkHttpClient;
import com.anthropic.core.JsonValue;
import com.anthropic.models.messages.ContentBlockParam;
import com.anthropic.models.messages.Message;
import com.anthropic.models.messages.MessageCreateParams;
import com.anthropic.models.messages.Model;
import com.anthropic.models.messages.TextBlockParam;
import com.anthropic.models.messages.ToolResultBlockParam;
import com.anthropic.models.messages.ToolTextEditor20250728;
import com.anthropic.models.messages.ToolUseBlockParam;
import java.util.List;

public class TextEditorConversationExample {

  public static void main(String[] args) {
    AnthropicClient client = AnthropicOkHttpClient.fromEnv();

    MessageCreateParams params = MessageCreateParams.builder()
      .model(Model.CLAUDE_OPUS_4_8)
      .maxTokens(1024)
      .addTool(ToolTextEditor20250728.builder().build())
      // Previous messages would go here
      .addAssistantMessageOfBlockParams(
        List.of(
          ContentBlockParam.ofText(
            TextBlockParam.builder()
              .text(
                "I found the syntax error in your primes.py file. In the `get_primes` function, there is a missing colon (:) at the end of the for loop line. Let me fix that for you."
              )
              .build()
          ),
          ContentBlockParam.ofToolUse(
            ToolUseBlockParam.builder()
              .id("toolu_01PqRsTuVwXyZAbCdEfGh")
              .name("str_replace_based_edit_tool")
              .input(
                ToolUseBlockParam.Input.builder()
                  .putAdditionalProperty("command", JsonValue.from("str_replace"))
                  .putAdditionalProperty("path", JsonValue.from("primes.py"))
                  .putAdditionalProperty(
                    "old_str",
                    JsonValue.from("    for num in range(2, limit + 1)")
                  )
                  .putAdditionalProperty(
                    "new_str",
                    JsonValue.from("    for num in range(2, limit + 1):")
                  )
                  .build()
              )
              .build()
          )
        )
      )
      .addUserMessageOfBlockParams(
        List.of(
          ContentBlockParam.ofToolResult(
            ToolResultBlockParam.builder()
              .toolUseId("toolu_01PqRsTuVwXyZAbCdEfGh")
              .content("Successfully replaced text at exactly one location.")
              .build()
          )
        )
      )
      .build();

    Message message = client.messages().create(params);
    System.out.println(message);
  }
}
```

```php PHP hidelines={1..5}
<?php

use Anthropic\Client;
use Anthropic\Messages\ToolTextEditor20250728;

$client = new Client();

$response = $client->messages->create(
    model: 'claude-opus-4-8',
    maxTokens: 1024,
    tools: [new ToolTextEditor20250728()],
    messages: [
        // Previous messages...
        [
            'role' => 'assistant',
            'content' => [
                [
                    'type' => 'text',
                    'text' => 'I found the syntax error in your primes.py file. In the `get_primes` function, there is a missing colon (:) at the end of the for loop line. Let me fix that for you.',
                ],
                [
                    'type' => 'tool_use',
                    'id' => 'toolu_01PqRsTuVwXyZAbCdEfGh',
                    'name' => 'str_replace_based_edit_tool',
                    'input' => [
                        'command' => 'str_replace',
                        'path' => 'primes.py',
                        'old_str' => '    for num in range(2, limit + 1)',
                        'new_str' => '    for num in range(2, limit + 1):',
                    ],
                ],
            ],
        ],
        [
            'role' => 'user',
            'content' => [
                [
                    'type' => 'tool_result',
                    'tool_use_id' => 'toolu_01PqRsTuVwXyZAbCdEfGh',
                    'content' => 'Successfully replaced text at exactly one location.',
                ],
            ],
        ],
    ],
);

echo $response;
```

```ruby Ruby hidelines={1..2}
require "anthropic"

client = Anthropic::Client.new

response = client.messages.create(
  model: "claude-opus-4-8",
  max_tokens: 1024,
  tools: [{type: "text_editor_20250728", name: "str_replace_based_edit_tool"}],
  messages: [
    # Previous messages...
    {
      role: "assistant",
      content: [
        {
          type: "text",
          text: "I found the syntax error in your primes.py file. In the `get_primes` function, there is a missing colon (:) at the end of the for loop line. Let me fix that for you."
        },
        {
          type: "tool_use",
          id: "toolu_01PqRsTuVwXyZAbCdEfGh",
          name: "str_replace_based_edit_tool",
          input: {
            command: "str_replace",
            path: "primes.py",
            old_str: "    for num in range(2, limit + 1)",
            new_str: "    for num in range(2, limit + 1):"
          }
        }
      ]
    },
    {
      role: "user",
      content: [
        {
          type: "tool_result",
          tool_use_id: "toolu_01PqRsTuVwXyZAbCdEfGh",
          content: "Successfully replaced text at exactly one location."
        }
      ]
    }
  ]
)

puts response
```
</CodeGroup>

Finally, Claude provides a complete explanation of the fix:

```json Output
{
  "id": "msg_01IjKlMnOpQrStUvWxYzAb",
  "model": "claude-opus-4-8",
  "stop_reason": "end_turn",
  "role": "assistant",
  "content": [
    {
      "type": "text",
      "text": "I've fixed the syntax error in your primes.py file. The issue was in the `get_primes` function at line 19. There was a missing colon (:) at the end of the for loop line.\n\nHere's what I changed:\n\nFrom:\n```python\nfor num in range(2, limit + 1)\n```\n\nTo:\n```python\nfor num in range(2, limit + 1):\n```\n\nIn Python, a colon is required at the end of statements that start a new code block, such as for loops, if statements, function definitions, etc. Without the colon, Python raises a syntax error because it doesn't know where the code block begins.\n\nYour code should now run correctly. The function will properly generate a list of prime numbers up to the specified limit."
    }
  ]
}
```

## Implement the text editor tool

The text editor tool is implemented as a schema-less tool. When using this tool, you don't need to provide an input schema as with other tools; the schema is built into Claude's model and can't be modified.

The tool type is `type: "text_editor_20250728"` for Claude 4 models.

<Steps>
  <Step title="Initialize your editor implementation">
    Create helper functions to handle file operations like reading, writing, and modifying files. Consider implementing backup functionality to recover from mistakes.
  </Step>
  <Step title="Handle editor tool calls">
    Create a function that processes tool calls from Claude based on the command type:

    
    <CodeGroup>
    ```python Python
    def handle_editor_tool(tool_call):
        input_params = tool_call.input
        command = input_params.get("command", "")
        file_path = input_params.get("path", "")

        if command == "view":
            # Read and return file contents
            pass
        elif command == "str_replace":
            # Replace text in file
            pass
        elif command == "create":
            # Create new file
            pass
        elif command == "insert":
            # Insert text at location
            pass
    ```

    ```typescript TypeScript
    function handleEditorTool(toolCall: { input: { command?: string; path?: string } }): void {
      const inputParams = toolCall.input;
      const command = inputParams.command ?? "";
      const filePath = inputParams.path ?? "";

      if (command === "view") {
        // Read and return file contents
      } else if (command === "str_replace") {
        // Replace text in file
      } else if (command === "create") {
        // Create new file
      } else if (command === "insert") {
        // Insert text at location
      }
    }
    ```

    ```csharp C# hidelines={1..3}
    using System.Collections.Generic;
    using System.Text.Json;

    static string HandleEditorTool(IReadOnlyDictionary<string, JsonElement> input)
    {
        input.TryGetValue("command", out var commandEl);
        input.TryGetValue("path", out var pathEl);
        var command = commandEl.ValueKind == JsonValueKind.String ? commandEl.GetString() : null;
        var filePath = pathEl.ValueKind == JsonValueKind.String ? pathEl.GetString() : null;

        if (command == "view")
        {
            // Read and return file contents
        }
        else if (command == "str_replace")
        {
            // Replace text in file
        }
        else if (command == "create")
        {
            // Create new file
        }
        else if (command == "insert")
        {
            // Insert text at location
        }
        return "";
    }
    ```

    ```go Go hidelines={1..2,-2..}
    package main

    func handleEditorTool(input map[string]any) string {
    	command, _ := input["command"].(string)
    	filePath, _ := input["path"].(string)
    	_ = filePath

    	switch command {
    	case "view":
    		// Read and return file contents
    	case "str_replace":
    		// Replace text in file
    	case "create":
    		// Create new file
    	case "insert":
    		// Insert text at location
    	}
    	return ""
    }

    func main() {}
    ```

    ```java Java hidelines={1..2,-2..}
    import java.util.Map;

    static void handleEditorTool(Map<String, Object> input) {
      var command = (String) input.getOrDefault("command", "");
      var filePath = (String) input.getOrDefault("path", "");

      if (command.equals("view")) {
        // Read and return file contents
      } else if (command.equals("str_replace")) {
        // Replace text in file
      } else if (command.equals("create")) {
        // Create new file
      } else if (command.equals("insert")) {
        // Insert text at location
      }
    }

    void main() {}
    ```

    ```php PHP hidelines={1..2}
    <?php

    function handle_editor_tool(array $input): string
    {
        $command = $input['command'] ?? '';
        $filePath = $input['path'] ?? '';

        if ($command === 'view') {
            // Read and return file contents
        } elseif ($command === 'str_replace') {
            // Replace text in file
        } elseif ($command === 'create') {
            // Create new file
        } elseif ($command === 'insert') {
            // Insert text at location
        }
        return '';
    }
    ```

    ```ruby Ruby
    def handle_editor_tool(input)
      command = input[:command] || ""
      file_path = input[:path] || ""

      case command
      when "view"
        # Read and return file contents
      when "str_replace"
        # Replace text in file
      when "create"
        # Create new file
      when "insert"
        # Insert text at location
      end
    end
    ```
    </CodeGroup>
  </Step>
  <Step title="Implement security measures">
    Add validation and security checks:
    - Validate file paths to prevent directory traversal
    - Create backups before making changes
    - Handle errors gracefully
    - Implement permissions checks
  </Step>
  <Step title="Process Claude's responses">
    Extract and handle tool calls from Claude's responses:

    
    <CodeGroup>
    ```python Python hidelines={1..15}
    from types import SimpleNamespace as _SN

    response = _SN(
        content=[
            _SN(
                type="tool_use", name="str_replace_based_edit_tool", input={}, id="toolu_01"
            )
        ]
    )


    def handle_editor_tool(tc):
        return "ok"


    # Process tool use in Claude's response
    for content in response.content:
        if content.type == "tool_use":
            # Execute the tool based on command
            result = handle_editor_tool(content)

            # Return result to Claude
            tool_result = {
                "type": "tool_result",
                "tool_use_id": content.id,
                "content": result,
            }
    ```

    ```typescript TypeScript hidelines={1..15}
    const response = {
      content: [
        {
          type: "tool_use",
          name: "str_replace_based_edit_tool",
          input: {},
          id: "toolu_01"
        }
      ]
    };

    function handleEditorTool(block: { input: object }): string {
      return "ok";
    }

    // Process tool use in Claude's response
    for (const block of response.content) {
      if (block.type === "tool_use") {
        // Execute the tool based on command
        const result = handleEditorTool(block);

        // Return result to Claude
        const toolResult = {
          type: "tool_result",
          tool_use_id: block.id,
          content: result
        };
      }
    }
    ```

    ```csharp C# hidelines={1..14,-6..}
    using System.Collections.Generic;
    using System.Text.Json;
    using Anthropic.Models.Messages;

    var response = new
    {
        Content = new[]
        {
            new StubBlock(new StubToolUse("toolu_01", new Dictionary<string, JsonElement>())),
        },
    };

    static string HandleEditorTool(IReadOnlyDictionary<string, JsonElement> input) => "ok";

    // Process tool use in Claude's response
    foreach (var block in response.Content)
    {
        if (block.TryPickToolUse(out var toolUse))
        {
            var result = HandleEditorTool(toolUse.Input);
            var toolResult = new ToolResultBlockParam
            {
                ToolUseID = toolUse.ID,
                Content = result,
            };
        }
    }

    record StubToolUse(string ID, IReadOnlyDictionary<string, JsonElement> Input);
    record StubBlock(StubToolUse ToolUse)
    {
        public bool TryPickToolUse(out StubToolUse toolUse) { toolUse = ToolUse; return true; }
    }
    ```

    ```go Go hidelines={1..20,-1}
    package main

    import (
    	"encoding/json"
    	"log"

    	"github.com/anthropics/anthropic-sdk-go"
    )

    func handleEditorTool(input map[string]any) string {
    	return "ok"
    }

    func main() {
    	response := anthropic.Message{
    		Content: []anthropic.ContentBlockUnion{
    			{Type: "tool_use", Name: "str_replace_based_edit_tool", ID: "toolu_01", Input: json.RawMessage(`{}`)},
    		},
    	}

    	// Process tool use in Claude's response
    	for _, block := range response.Content {
    		if block.Type == "tool_use" {
    			var input map[string]any
    			if err := json.Unmarshal(block.Input, &input); err != nil {
    				log.Fatal(err)
    			}
    			result := handleEditorTool(input)

    			toolResult := anthropic.NewToolResultBlock(block.ID, result, false)
    			_ = toolResult
    		}
    	}
    }
    ```

    ```java Java hidelines={1..15,-1}
    import java.util.List;
    import java.util.Map;

    record ContentBlock(String type, String name, Map<String, Object> input, String id) {}
    record Response(List<ContentBlock> content) {}

    static String handleEditorTool(ContentBlock block) {
      return "ok";
    }

    void main() {
      var response = new Response(List.of(
        new ContentBlock("tool_use", "str_replace_based_edit_tool", Map.of(), "toolu_01")
      ));

      // Process tool use in Claude's response
      for (var block : response.content()) {
        if (block.type().equals("tool_use")) {
          // Execute the tool based on command
          var result = handleEditorTool(block);

          // Return result to Claude
          var toolResult = Map.of(
            "type", "tool_result",
            "tool_use_id", block.id(),
            "content", result
          );
        }
      }
    }
    ```

    ```php PHP hidelines={1..18}
    <?php

    $response = (object) [
        'content' => [
            (object) [
                'type' => 'tool_use',
                'name' => 'str_replace_based_edit_tool',
                'input' => [],
                'id' => 'toolu_01',
            ],
        ],
    ];

    function handle_editor_tool(array $input): string
    {
        return 'ok';
    }

    // Process tool use in Claude's response
    foreach ($response->content as $block) {
        if ($block->type === 'tool_use') {
            // Execute the tool based on command
            $result = handle_editor_tool($block->input);

            // Return result to Claude
            $toolResult = [
                'type' => 'tool_result',
                'tool_use_id' => $block->id,
                'content' => $result,
            ];
        }
    }
    ```

    ```ruby Ruby hidelines={1..11}
    Block = Struct.new(:type, :name, :input, :id)
    Response = Struct.new(:content)

    response = Response.new([
      Block.new(:tool_use, "str_replace_based_edit_tool", {command: "view", path: "primes.py"}, "toolu_01")
    ])

    def handle_editor_tool(input)
      "ok"
    end

    # Process tool use in Claude's response
    tool_results = response.content.filter_map do |block|
      next unless block.type == :tool_use

      {type: "tool_result", tool_use_id: block.id, content: handle_editor_tool(block.input)}
    end
    ```
    </CodeGroup>
  </Step>
</Steps>

<Warning>
When implementing the text editor tool, keep in mind:

1. **Security:** The tool has access to your local filesystem, so implement proper security measures.
2. **Backup:** Always create backups before allowing edits to important files.
3. **Validation:** Validate all inputs to prevent unintended changes.
4. **Unique matching:** Make sure replacements match exactly one location to avoid unintended edits.
</Warning>

### Handle errors

When using the text editor tool, various errors may occur. Here is guidance on how to handle them:

<section title="File not found">

If Claude tries to view or modify a file that doesn't exist, return an appropriate error message in the `tool_result`:

```json
{
  "role": "user",
  "content": [
    {
      "type": "tool_result",
      "tool_use_id": "toolu_01A09q90qw90lq917835lq9",
      "content": "Error: File not found",
      "is_error": true
    }
  ]
}
```

</section>

<section title="Multiple matches for replacement">

If Claude's `str_replace` command matches multiple locations in the file, return an appropriate error message:

```json
{
  "role": "user",
  "content": [
    {
      "type": "tool_result",
      "tool_use_id": "toolu_01A09q90qw90lq917835lq9",
      "content": "Error: Found 3 matches for replacement text. Please provide more context to make a unique match.",
      "is_error": true
    }
  ]
}
```

</section>

<section title="No matches for replacement">

If Claude's `str_replace` command doesn't match any text in the file, return an appropriate error message:

```json
{
  "role": "user",
  "content": [
    {
      "type": "tool_result",
      "tool_use_id": "toolu_01A09q90qw90lq917835lq9",
      "content": "Error: No match found for replacement. Please check your text and try again.",
      "is_error": true
    }
  ]
}
```

</section>

<section title="Permission errors">

If there are permission issues with creating, reading, or modifying files, return an appropriate error message:

```json
{
  "role": "user",
  "content": [
    {
      "type": "tool_result",
      "tool_use_id": "toolu_01A09q90qw90lq917835lq9",
      "content": "Error: Permission denied. Cannot write to file.",
      "is_error": true
    }
  ]
}
```

</section>

### Follow implementation best practices

<section title="Provide clear context">

When asking Claude to fix or modify code, be specific about what files need to be examined or what issues need to be addressed. Clear context helps Claude identify the right files and make appropriate changes.

**Less helpful prompt**: "Can you fix my code?"

**Better prompt**: "There's a syntax error in my primes.py file that prevents it from running. Can you fix it?"

</section>

<section title="Be explicit about file paths">

Specify file paths clearly when needed, especially if you're working with multiple files or files in different directories.

**Less helpful prompt**: "Review my helper file"

**Better prompt**: "Can you check my utils/helpers.py file for any performance issues?"

</section>

<section title="Create backups before editing">

Implement a backup system in your application that creates copies of files before allowing Claude to edit them, especially for important or production code.

<CodeGroup>
```python Python hidelines={1..3}
import os


def backup_file(file_path):
    """Create a backup of a file before editing."""
    backup_path = f"{file_path}.backup"
    if os.path.exists(file_path):
        with open(file_path, "r") as src, open(backup_path, "w") as dst:
            dst.write(src.read())
```

```typescript TypeScript hidelines={1..2}
import { access, copyFile } from "node:fs/promises";

async function backupFile(filePath: string): Promise<void> {
  const backupPath = `${filePath}.backup`;
  try {
    await access(filePath);
    await copyFile(filePath, backupPath);
  } catch {
    // File does not exist; nothing to back up
  }
}
```

```csharp C# hidelines={1..2}
using System.IO;

static void BackupFile(string filePath)
{
    var backupPath = $"{filePath}.backup";
    if (File.Exists(filePath))
    {
        File.Copy(filePath, backupPath, overwrite: true);
    }
}
```

```go Go hidelines={1..4,-2..}
package main

import "os"

func backupFile(filePath string) error {
	backupPath := filePath + ".backup"
	data, err := os.ReadFile(filePath)
	if err != nil {
		if os.IsNotExist(err) {
			return nil
		}
		return err
	}
	return os.WriteFile(backupPath, data, 0o644)
}

func main() {}
```

```java Java hidelines={1..5,-2..}
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.StandardCopyOption;

static void backupFile(String filePath) throws IOException {
  Path source = Path.of(filePath);
  Path backupPath = Path.of(filePath + ".backup");
  if (Files.exists(source)) {
    Files.copy(source, backupPath, StandardCopyOption.REPLACE_EXISTING);
  }
}

void main() {}
```

```php PHP hidelines={1..2}
<?php

function backup_file(string $filePath): void
{
    $backupPath = $filePath . '.backup';
    if (file_exists($filePath)) {
        copy($filePath, $backupPath);
    }
}
```

```ruby Ruby hidelines={1..2}
require "fileutils"

def backup_file(file_path)
  backup_path = "#{file_path}.backup"
  FileUtils.cp(file_path, backup_path) if File.exist?(file_path)
end
```
</CodeGroup>

</section>

<section title="Handle unique text replacement carefully">

The `str_replace` command requires an exact match for the text to be replaced. Your application should ensure that there is exactly one match for the old text or provide appropriate error messages.

<CodeGroup>
```python Python
def safe_replace(file_path, old_text, new_text):
    """Replace text only if there's exactly one match."""
    with open(file_path, "r") as f:
        content = f.read()

    count = content.count(old_text)
    if count == 0:
        return "Error: No match found"
    elif count > 1:
        return f"Error: Found {count} matches"
    else:
        new_content = content.replace(old_text, new_text)
        with open(file_path, "w") as f:
            f.write(new_content)
        return "Successfully replaced text"
```

```typescript TypeScript hidelines={1..2}
import { readFile, writeFile } from "node:fs/promises";

async function safeReplace(
  filePath: string,
  oldText: string,
  newText: string
): Promise<string> {
  const content = await readFile(filePath, "utf8");

  const count = content.split(oldText).length - 1;
  if (count === 0) {
    return "Error: No match found";
  } else if (count > 1) {
    return `Error: Found ${count} matches`;
  } else {
    const newContent = content.replace(oldText, newText);
    await writeFile(filePath, newContent, "utf8");
    return "Successfully replaced text";
  }
}
```

```csharp C# hidelines={1..2}
using System.IO;

static string SafeReplace(string filePath, string oldText, string newText)
{
    var content = File.ReadAllText(filePath);

    var count = content.Split(oldText).Length - 1;
    if (count == 0)
    {
        return "Error: No match found";
    }
    else if (count > 1)
    {
        return $"Error: Found {count} matches";
    }
    else
    {
        var newContent = content.Replace(oldText, newText);
        File.WriteAllText(filePath, newContent);
        return "Successfully replaced text";
    }
}
```

```go Go hidelines={1..8,-2..}
package main

import (
	"fmt"
	"os"
	"strings"
)

func safeReplace(filePath, oldText, newText string) string {
	data, err := os.ReadFile(filePath)
	if err != nil {
		return fmt.Sprintf("Error: %v", err)
	}
	content := string(data)

	count := strings.Count(content, oldText)
	if count == 0 {
		return "Error: No match found"
	} else if count > 1 {
		return fmt.Sprintf("Error: Found %d matches", count)
	}

	newContent := strings.Replace(content, oldText, newText, 1)
	if err := os.WriteFile(filePath, []byte(newContent), 0o644); err != nil {
		return fmt.Sprintf("Error: %v", err)
	}
	return "Successfully replaced text"
}

func main() {}
```

```java Java hidelines={1..5,-2..}
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.regex.Pattern;

static String safeReplace(String filePath, String oldText, String newText) throws IOException {
  String content = Files.readString(Path.of(filePath));

  int count = content.split(Pattern.quote(oldText), -1).length - 1;
  if (count == 0) {
    return "Error: No match found";
  } else if (count > 1) {
    return "Error: Found " + count + " matches";
  } else {
    String newContent = content.replace(oldText, newText);
    Files.writeString(Path.of(filePath), newContent);
    return "Successfully replaced text";
  }
}

void main() {}
```

```php PHP hidelines={1..2}
<?php

function safe_replace(string $filePath, string $oldText, string $newText): string
{
    $content = file_get_contents($filePath);

    $count = substr_count($content, $oldText);
    if ($count === 0) {
        return 'Error: No match found';
    } elseif ($count > 1) {
        return "Error: Found {$count} matches";
    } else {
        $newContent = str_replace($oldText, $newText, $content);
        file_put_contents($filePath, $newContent);
        return 'Successfully replaced text';
    }
}
```

```ruby Ruby
def safe_replace(file_path, old_text, new_text)
  content = File.read(file_path)

  count = content.scan(old_text).length
  if count == 0
    "Error: No match found"
  elsif count > 1
    "Error: Found #{count} matches"
  else
    new_content = content.sub(old_text) { new_text }
    File.write(file_path, new_content)
    "Successfully replaced text"
  end
end
```
</CodeGroup>

</section>

<section title="Verify changes">

After Claude makes changes to a file, verify the changes by running tests or checking that the code still works as expected.

<CodeGroup>
```python Python
def verify_changes(file_path):
    """Run tests or checks after making changes."""
    try:
        # For Python files, check for syntax errors
        if file_path.endswith(".py"):
            import ast

            with open(file_path, "r") as f:
                ast.parse(f.read())
            return "Syntax check passed"
    except Exception as e:
        return f"Verification failed: {str(e)}"
```

```typescript TypeScript hidelines={1..2}
import { execFileSync } from "node:child_process";

function verifyChanges(filePath: string): string {
  try {
    // For Python files, check for syntax errors
    if (filePath.endsWith(".py")) {
      execFileSync("python3", ["-m", "py_compile", filePath]);
      return "Syntax check passed";
    }
    return "No checks defined for this file type";
  } catch (err) {
    return `Verification failed: ${err}`;
  }
}
```

```csharp C# hidelines={1..2}
using System.Diagnostics;

static string VerifyChanges(string filePath)
{
    try
    {
        // For Python files, check for syntax errors
        if (filePath.EndsWith(".py"))
        {
            var psi = new ProcessStartInfo("python3")
            {
                RedirectStandardError = true,
            };
            psi.ArgumentList.Add("-m");
            psi.ArgumentList.Add("py_compile");
            psi.ArgumentList.Add(filePath);
            using var proc = Process.Start(psi)!;
            proc.WaitForExit();
            if (proc.ExitCode != 0)
            {
                return $"Verification failed: {proc.StandardError.ReadToEnd()}";
            }
            return "Syntax check passed";
        }
        return "No checks defined for this file type";
    }
    catch (Exception e)
    {
        return $"Verification failed: {e.Message}";
    }
}
```

```go Go hidelines={1..8,-2..}
package main

import (
	"fmt"
	"os/exec"
	"strings"
)

func verifyChanges(filePath string) string {
	// For Python files, check for syntax errors
	if strings.HasSuffix(filePath, ".py") {
		cmd := exec.Command("python3", "-m", "py_compile", filePath)
		if out, err := cmd.CombinedOutput(); err != nil {
			return fmt.Sprintf("Verification failed: %v: %s", err, out)
		}
		return "Syntax check passed"
	}
	return "No checks defined for this file type"
}

func main() {}
```

```java Java hidelines={1..2,-2..}
import java.io.IOException;

static String verifyChanges(String filePath) {
  try {
    // For Python files, check for syntax errors
    if (filePath.endsWith(".py")) {
      Process proc = new ProcessBuilder("python3", "-m", "py_compile", filePath)
        .redirectErrorStream(true)
        .start();
      if (proc.waitFor() != 0) {
        return "Verification failed: " + new String(proc.getInputStream().readAllBytes());
      }
      return "Syntax check passed";
    }
    return "No checks defined for this file type";
  } catch (IOException | InterruptedException e) {
    return "Verification failed: " + e.getMessage();
  }
}

void main() {}
```

```php PHP hidelines={1..2}
<?php

function verify_changes(string $filePath): string
{
    // For Python files, check for syntax errors
    if (str_ends_with($filePath, '.py')) {
        exec('python3 -m py_compile ' . escapeshellarg($filePath) . ' 2>&1', $output, $exitCode);
        if ($exitCode !== 0) {
            return 'Verification failed: ' . implode("\n", $output);
        }
        return 'Syntax check passed';
    }
    return 'No checks defined for this file type';
}
```

```ruby Ruby
def verify_changes(file_path)
  # For Python files, check for syntax errors
  if file_path.end_with?(".py")
    if system("python3", "-m", "py_compile", file_path)
      "Syntax check passed"
    else
      "Verification failed: syntax error in #{file_path}"
    end
  else
    "No checks defined for this file type"
  end
end
```
</CodeGroup>

</section>

---

## Pricing and token usage

The text editor tool uses the same pricing structure as other tools used with Claude. It follows the standard input and output token pricing based on the Claude model you're using.

In addition to the base tokens, the following additional input tokens are needed for the text editor tool:

| Tool | Additional input tokens |
| ----------------------------------------- | --------------------------------------- |
| `text_editor_20250429` (Claude 4.x) | 700 tokens |

For more detailed information about tool pricing, see [Tool use pricing](/docs/en/agents-and-tools/tool-use/overview#pricing).

## Integrate the text editor tool with other tools

The text editor tool can be used alongside other Claude tools. When combining tools, ensure you:
- Match the tool version with the model you're using
- Account for the additional token usage for all tools included in your request

## Change log

| Date | Version | Changes |
| ---- | ------- | ------- |
| July 28, 2025 | `text_editor_20250728` | Release of an updated text editor Tool that fixes some issues and adds an optional `max_characters` parameter. It is otherwise identical to `text_editor_20250429`. |
| April 29, 2025 | `text_editor_20250429` | Release of the text editor Tool for Claude 4. This version removes the `undo_edit` command but maintains all other capabilities. The tool name has been updated to reflect its str_replace-based architecture. |
| March 13, 2025 | `text_editor_20250124` | Introduction of standalone text editor Tool documentation. This version is optimized for Claude Sonnet 3.7 but has identical capabilities to the previous version. |
| October 22, 2024 | `text_editor_20241022` | Initial release of the text editor Tool with Claude Sonnet 3.5 ([retired](/docs/en/about-claude/model-deprecations)). Provides capabilities for viewing, creating, and editing files through the `view`, `create`, `str_replace`, `insert`, and `undo_edit` commands. |

## Next steps

Here are some ideas for how to use the text editor tool in more convenient and powerful ways:

- **Integrate with your development workflow**: Build the text editor tool into your development tools or IDE
- **Create a code review system**: Have Claude review your code and make improvements
- **Build a debugging assistant**: Create a system where Claude can help you diagnose and fix issues in your code
- **Implement file format conversion**: Let Claude help you convert files from one format to another
- **Automate documentation**: Set up workflows for Claude to automatically document your code

The text editor tool enables Claude to work directly with your codebase, supporting workflows from debugging to automated documentation.

<CardGroup cols={3}>
  <Card
    title="Tool use overview"
    icon="wrench"
    href="/docs/en/agents-and-tools/tool-use/overview"
  >
    Learn how to implement tool workflows for use with Claude.
  </Card>

  <Card
    title="Bash tool"
    icon="terminal"
    href="/docs/en/agents-and-tools/tool-use/bash-tool"
  >
    Execute shell commands with Claude.
  </Card>
</CardGroup>