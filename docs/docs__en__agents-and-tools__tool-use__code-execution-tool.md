# Code execution tool

Run Python and bash code in a sandboxed container to analyze data, generate files, and iterate on solutions.

---

Claude can analyze data, create visualizations, perform complex calculations, run system commands, create and edit files, and process uploaded files directly within the API conversation. The code execution tool allows Claude to run Bash commands and manipulate files, including writing code, in a secure, sandboxed environment.

**Code execution is free when used with web search or web fetch (`web_search_20260209`, `web_fetch_20260209`, or later).** When one of those tools is in your request, there are no additional charges for code execution in that request beyond standard token costs. This covers both the code execution behind dynamic filtering and any code Claude runs directly. Standard code execution pricing applies when they are not included.

Code execution also powers dynamic filtering in the [web search](/docs/en/agents-and-tools/tool-use/web-search-tool) and [web fetch](/docs/en/agents-and-tools/tool-use/web-fetch-tool) tools: Claude filters results inside the code execution environment before they reach the context window. When dynamic filtering runs, the API provisions the code execution it needs for the request automatically, so you don't add the code execution tool to your request for it.

<Note>
  Reach out through the [feedback form](https://forms.gle/LTAU6Xn2puCJMi1n6) to share your feedback on this feature.
</Note>

<Note>
  This feature is **not** eligible for [Zero Data Retention (ZDR)](/docs/en/build-with-claude/api-and-data-retention). Data is retained according to the feature's standard retention policy.
</Note>

## Model compatibility

The code execution tool is available on the following models:

| Model                                                                                               | Tool versions                                                                   |
| --------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- |
| Claude Fable 5 (claude-fable-5)                                                                     | `code_execution_20250825`, `code_execution_20260120`, `code_execution_20260521` |
| Claude Mythos 5 (claude-mythos-5)                                                                   | `code_execution_20250825`, `code_execution_20260120`, `code_execution_20260521` |
| Claude Sonnet 5 (claude-sonnet-5)                                                                   | `code_execution_20250825`, `code_execution_20260120`, `code_execution_20260521` |
| Claude Opus 4.8 (claude-opus-4-8)                                                                   | `code_execution_20250825`, `code_execution_20260120`, `code_execution_20260521` |
| Claude Opus 4.7 (claude-opus-4-7)                                                                   | `code_execution_20250825`, `code_execution_20260120`, `code_execution_20260521` |
| Claude Opus 4.6 (claude-opus-4-6)                                                                   | `code_execution_20250825`, `code_execution_20260120`, `code_execution_20260521` |
| Claude Sonnet 4.6 (claude-sonnet-4-6)                                                               | `code_execution_20250825`, `code_execution_20260120`, `code_execution_20260521` |
| Claude Opus 4.5 (claude-opus-4-5-20251101)                                                          | `code_execution_20250825`, `code_execution_20260120`, `code_execution_20260521` |
| Claude Sonnet 4.5 (claude-sonnet-4-5-20250929)                                                      | `code_execution_20250825`, `code_execution_20260120`, `code_execution_20260521` |
| Claude Haiku 4.5 (claude-haiku-4-5-20251001)                                                        | `code_execution_20250825`, `code_execution_20260120`, `code_execution_20260521` |
| Claude Opus 4.1 (claude-opus-4-1-20250805) ([deprecated](/docs/en/about-claude/model-deprecations)) | `code_execution_20250825`                                                       |

Each tool version builds on the previous one:

* `code_execution_20250825` supports Bash commands and file operations and is available on every model in the table.
* `code_execution_20260120` adds REPL state persistence and [programmatic tool calling](/docs/en/agents-and-tools/tool-use/programmatic-tool-calling) from within the sandbox. Claude Haiku 4.5 accepts the `code_execution_20260120` and `code_execution_20260521` tool types, but programmatic tool calling and the REPL state persistence that depends on it aren't available on it, so the newer versions behave like `code_execution_20250825` there.
* `code_execution_20260521` is the same runtime as `code_execution_20260120`. The difference is that the tool description tells Claude about the 90-second wall-clock limit on each Python cell in programmatic tool calling, so Claude can budget long-running cells. A cell that exceeds the limit returns a normal code execution result with a non-zero `return_code` and a `detection_timeout` status message in its output. This is separate from the `execution_time_exceeded` [error code](#errors), which the API returns when a whole tool invocation exceeds the maximum execution time.

All three tool versions are generally available and don't require an `anthropic-beta` header. The legacy code execution beta headers remain valid opt-ins.

The examples on this page use `code_execution_20250825` because every model in the table supports it. The current [web search](/docs/en/agents-and-tools/tool-use/web-search-tool) and [web fetch](/docs/en/agents-and-tools/tool-use/web-fetch-tool) tools (`web_search_20260209`, `web_fetch_20260209`, and later) require `code_execution_20260120` or later as their code execution version.

<Note>
  If you're still using the legacy `code_execution_20250522` (Python only), see [Upgrade to latest tool version](#upgrade-to-latest-tool-version) to migrate from it.
</Note>

<Warning>
  Older tool versions are not guaranteed to be backwards-compatible with newer models. Always use the tool version that corresponds to your model version.
</Warning>

## Platform availability

Code execution is available on:

* **Claude API** (Anthropic)
* **[Claude Platform on AWS](/docs/en/build-with-claude/claude-platform-on-aws)**
* **[Microsoft Foundry](/docs/en/build-with-claude/claude-in-microsoft-foundry)** (requires a [Hosted on Anthropic deployment](/docs/en/build-with-claude/claude-in-microsoft-foundry#additional-features-not-supported-when-hosted-on-azure))

Code execution is not currently available on Amazon Bedrock or Google Cloud.

<Note>
  For [Claude Mythos Preview](https://anthropic.com/glasswing), code execution is supported on the Claude API and Microsoft Foundry only. It is not available for Mythos Preview on Amazon Bedrock, Google Cloud, or Claude Platform on AWS.
</Note>

## Quick start

Here's a simple example that asks Claude to perform a calculation:

<CodeGroup>
  ```bash cURL
  curl --fail-with-body -sS https://api.anthropic.com/v1/messages \
    -H "x-api-key: $ANTHROPIC_API_KEY" \
    -H "anthropic-version: 2023-06-01" \
    -H "content-type: application/json" \
    -d '{
      "model": "claude-opus-4-8",
      "max_tokens": 4096,
      "messages": [
        {
          "role": "user",
          "content": "Use the code execution tool to calculate the mean and standard deviation of [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]"
        }
      ],
      "tools": [
        {
          "type": "code_execution_20250825",
          "name": "code_execution"
        }
      ]
    }'
  ```

  ```bash CLI
  ant messages create \
    --model claude-opus-4-8 \
    --max-tokens 4096 \
    --message '{
      role: user,
      content: "Use the code execution tool to calculate the mean and standard
        deviation of [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]"
    }' \
    --tool '{type: code_execution_20250825, name: code_execution}'
  ```

  ```python Python
  client = anthropic.Anthropic()

  response = client.messages.create(
      model="claude-opus-4-8",
      max_tokens=4096,
      messages=[
          {
              "role": "user",
              "content": "Use the code execution tool to calculate the mean and standard deviation of [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]",
          }
      ],
      tools=[{"type": "code_execution_20250825", "name": "code_execution"}],
  )

  print(response.to_json())
  ```

  ```typescript TypeScript
  const client = new Anthropic();

  const response = await client.messages.create({
    model: "claude-opus-4-8",
    max_tokens: 4096,
    messages: [
      {
        role: "user",
        content:
          "Use the code execution tool to calculate the mean and standard deviation of [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]"
      }
    ],
    tools: [{ type: "code_execution_20250825", name: "code_execution" }]
  });

  console.log(JSON.stringify(response));
  ```

  ```csharp C#
  AnthropicClient client = new();

  var message = await client.Messages.Create(new()
  {
      Model = Model.ClaudeOpus4_8,
      MaxTokens = 4096,
      Messages = [new() { Role = Role.User, Content = "Use the code execution tool to calculate the mean and standard deviation of [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]" }],
      Tools = [new CodeExecutionTool20250825()]
  });

  Console.WriteLine(message);
  ```

  ```go Go
  client := anthropic.NewClient()

  response, err := client.Messages.New(context.Background(), anthropic.MessageNewParams{
  	Model:     anthropic.ModelClaudeOpus4_8,
  	MaxTokens: 4096,
  	Messages: []anthropic.MessageParam{
  		anthropic.NewUserMessage(anthropic.NewTextBlock("Use the code execution tool to calculate the mean and standard deviation of [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]")),
  	},
  	Tools: []anthropic.ToolUnionParam{
  		{OfCodeExecutionTool20250825: &anthropic.CodeExecutionTool20250825Param{}},
  	},
  })
  if err != nil {
  	log.Fatal(err)
  }
  fmt.Println(response.RawJSON())
  ```

  ```java Java
  AnthropicClient client = AnthropicOkHttpClient.fromEnv();

  MessageCreateParams params = MessageCreateParams.builder()
      .model(Model.CLAUDE_OPUS_4_8)
      .maxTokens(4096L)
      .addUserMessage("Use the code execution tool to calculate the mean and standard deviation of [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]")
      .addTool(CodeExecutionTool20250825.builder().build())
      .build();

  Message response = client.messages().create(params);
  IO.println(ObjectMappers.jsonMapper().valueToTree(response));
  ```

  ```php PHP
  $client = new Client();

  $message = $client->messages->create(
      maxTokens: 4096,
      messages: [
          [
              'role' => 'user',
              'content' => 'Use the code execution tool to calculate the mean and standard deviation of [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]',
          ],
      ],
      model: Model::CLAUDE_OPUS_4_8,
      tools: [new CodeExecutionTool20250825()],
  );

  echo json_encode($message, JSON_PRETTY_PRINT), PHP_EOL;
  ```

  ```ruby Ruby
  client = Anthropic::Client.new

  message = client.messages.create(
    model: Anthropic::Model::CLAUDE_OPUS_4_8,
    max_tokens: 4096,
    messages: [
      {
        role: "user",
        content: "Use the code execution tool to calculate the mean and standard deviation of [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]"
      }
    ],
    tools: [Anthropic::CodeExecutionTool20250825.new]
  )

  puts message.to_json
  ```
</CodeGroup>

The response interleaves `server_tool_use` blocks (the commands Claude ran) with their tool result blocks, followed by Claude's text. The top level also includes a `container` object whose `id` you can [reuse across requests](#container-reuse). See [Response format](#response-format) for the block shapes.

## How code execution works

When you add the code execution tool to your API request:

1. Claude evaluates whether code execution would help answer your question

2. The tool automatically provides Claude with the following capabilities:

   * **Bash commands**: Execute shell commands for system operations
   * **File operations**: Create, view, and edit files directly, including writing code

3. Claude can use any combination of these capabilities in a single request

4. All operations run in a secure, sandboxed container. The container has no internet access, so Claude can't download packages at runtime: only the [pre-installed libraries](#pre-installed-libraries) are available

5. The API runs every command server-side and returns the results to Claude within the same request, so you never execute code or send back `tool_result` blocks yourself. One exception is when Claude calls one of your client tools alongside code execution: the API returns the code execution call without its result. The result arrives in a later response, after you send back the `tool_result` blocks for your client tools

6. Each request runs in a new container unless you pass an earlier response's container ID back (see [Container reuse](#container-reuse))

7. Claude provides results with any generated charts, calculations, or analysis

The container has Python pre-installed. Claude writes Python with the file operations sub-tool and runs it with a Bash command. With `code_execution_20260120` or later and [programmatic tool calling](/docs/en/agents-and-tools/tool-use/programmatic-tool-calling), the Python interpreter state (such as variable bindings) also persists across requests that reuse the container.

### When Claude runs code

Claude runs code when the request benefits from computation or file handling:

* Non-trivial math (large numbers, many steps, precision-sensitive results)
* Data analysis, file parsing, or visualization
* Algorithm execution or simulation
* Explicit requests to "run", "compute", or "execute"

Claude answers directly without running code for:

* Simple arithmetic and well-known math facts
* Factual, conversational, or creative requests
* Simple unit conversions or translations

If you want Claude to run code for a borderline request, ask explicitly (for example, "run code to verify this").

## Work with files

### Upload and analyze your own files

To analyze your own data files (such as CSV, Excel, or images), upload them through the Files API and reference them in your request:

<Note>
  Using the Files API with Code Execution requires the Files API beta header: `"anthropic-beta": "files-api-2025-04-14"`
</Note>

The Python environment can process various file types uploaded through the Files API, including:

* CSV
* Excel (.xlsx, .xls)
* JSON
* XML
* Images (JPEG, PNG, GIF, WebP)
* Text files (.txt, .md, .py, and others)

#### Upload and analyze files

1. **Upload your file** using the [Files API](/docs/en/build-with-claude/files)
2. **Reference the file** in your message using a `container_upload` content block
3. **Include the code execution tool** in your API request

<CodeGroup>
  ```bash cURL
  # First, upload a file and capture the file ID (using jq)
  FILE_ID=$(curl --fail-with-body -sS https://api.anthropic.com/v1/files \
    -H "x-api-key: $ANTHROPIC_API_KEY" \
    -H "anthropic-version: 2023-06-01" \
    -H "anthropic-beta: files-api-2025-04-14" \
    -F "file=@data.csv" | jq -r '.id')

  # Then use the file_id with code execution
  curl --fail-with-body -sS https://api.anthropic.com/v1/messages \
    -H "x-api-key: $ANTHROPIC_API_KEY" \
    -H "anthropic-version: 2023-06-01" \
    -H "anthropic-beta: files-api-2025-04-14" \
    -H "content-type: application/json" \
    -d '{
      "model": "claude-opus-4-8",
      "max_tokens": 4096,
      "messages": [{
        "role": "user",
        "content": [
          {"type": "text", "text": "Analyze this CSV data"},
          {"type": "container_upload", "file_id": "'"$FILE_ID"'"}
        ]
      }],
      "tools": [{
        "type": "code_execution_20250825",
        "name": "code_execution"
      }]
    }'
  ```

  ```bash CLI
  # First, upload a file and capture the file ID
  FILE_ID=$(ant beta:files upload \
    --file ./data.csv \
    --transform id --raw-output)

  # Then use the file_id with code execution
  ant beta:messages create \
    --beta files-api-2025-04-14 <<YAML
  model: claude-opus-4-8
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

  ```python Python
  client = anthropic.Anthropic()

  # Upload a file
  file_object = client.beta.files.upload(file=Path("data.csv"))

  # Use the file_id with code execution
  response = client.beta.messages.create(
      model="claude-opus-4-8",
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

  print(response.to_json())
  ```

  ```typescript TypeScript
  import { createReadStream } from "node:fs";
  // ...
  const client = new Anthropic();

  // Upload a file
  const fileObject = await client.beta.files.upload({
    file: createReadStream("data.csv")
  });

  // Use the file_id with code execution
  const response = await client.beta.messages.create({
    model: "claude-opus-4-8",
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

  console.log(JSON.stringify(response));
  ```

  ```csharp C#
  AnthropicClient client = new();

  // Upload a file
  var fileObject = await client.Beta.Files.Upload(new FileUploadParams
  {
      File = File.OpenRead("data.csv")
  });

  // Use the file_id with code execution
  var parameters = new MessageCreateParams
  {
      Model = Model.ClaudeOpus4_8,
      MaxTokens = 4096,
      Betas = [AnthropicBeta.FilesApi2025_04_14],
      Messages = [
          new()
          {
              Role = Role.User,
              Content = new([
                  new BetaTextBlockParam { Text = "Analyze this CSV data" },
                  new BetaContainerUploadBlockParam { FileID = fileObject.ID }
              ])
          }
      ],
      Tools = [new BetaCodeExecutionTool20250825()]
  };

  var response = await client.Beta.Messages.Create(parameters);
  Console.WriteLine(response);
  ```

  ```go Go
  ctx := context.Background()
  client := anthropic.NewClient()

  // Upload a file
  file, err := os.Open("data.csv")
  if err != nil {
  	log.Fatal(err)
  }
  defer file.Close()

  fileObject, err := client.Beta.Files.Upload(ctx, anthropic.BetaFileUploadParams{
  	File: file,
  })
  if err != nil {
  	log.Fatal(err)
  }

  // Use the file_id with code execution
  response, err := client.Beta.Messages.New(ctx, anthropic.BetaMessageNewParams{
  	Model:     anthropic.ModelClaudeOpus4_8,
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
  		anthropic.AnthropicBetaFilesAPI2025_04_14,
  	},
  })
  if err != nil {
  	log.Fatal(err)
  }

  fmt.Println(response.RawJSON())
  ```

  ```java Java
  AnthropicClient client = AnthropicOkHttpClient.fromEnv();

  // Upload a file
  FileMetadata fileObject = client.beta().files().upload(
      FileUploadParams.builder()
          .file(Path.of("data.csv"))
          .build()
  );

  // Use the file_id with code execution
  BetaMessage response = client.beta().messages().create(
      MessageCreateParams.builder()
          .model(Model.CLAUDE_OPUS_4_8)
          .addBeta(AnthropicBeta.FILES_API_2025_04_14)
          .maxTokens(4096L)
          .addUserMessageOfBetaContentBlockParams(List.of(
              BetaContentBlockParam.ofText(BetaTextBlockParam.builder()
                  .text("Analyze this CSV data")
                  .build()),
              BetaContentBlockParam.ofContainerUpload(BetaContainerUploadBlockParam.builder()
                  .fileId(fileObject.id())
                  .build())
          ))
          .addTool(BetaCodeExecutionTool20250825.builder().build())
          .build()
  );

  IO.println(ObjectMappers.jsonMapper().valueToTree(response));
  ```

  ```php PHP
  $client = new Client();

  // Upload a file
  $fileObject = $client->beta->files->upload(
      file: FileParam::fromResource(fopen('data.csv', 'r')),
  );

  // Use the file_id with code execution
  $response = $client->beta->messages->create(
      model: Model::CLAUDE_OPUS_4_8,
      maxTokens: 4096,
      betas: [AnthropicBeta::FILES_API_2025_04_14],
      messages: [
          [
              'role' => 'user',
              'content' => [
                  BetaTextBlockParam::with(text: 'Analyze this CSV data'),
                  BetaContainerUploadBlockParam::with(fileID: $fileObject->id),
              ],
          ],
      ],
      tools: [new BetaCodeExecutionTool20250825()],
  );

  echo json_encode($response), PHP_EOL;
  ```

  ```ruby Ruby
  client = Anthropic::Client.new

  # Upload a file
  file_object = client.beta.files.upload(
    file: Pathname("data.csv")
  )

  # Use the file_id with code execution
  response = client.beta.messages.create(
    model: Anthropic::Model::CLAUDE_OPUS_4_8,
    betas: [Anthropic::AnthropicBeta::FILES_API_2025_04_14],
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
      Anthropic::Beta::BetaCodeExecutionTool20250825.new
    ]
  )

  puts response.to_json
  ```
</CodeGroup>

### Retrieve generated files

When Claude creates files during code execution, each created file's ID appears in the code execution tool result, and you can download it with the [Files API](/docs/en/build-with-claude/files):

<CodeGroup>
  ```bash cURL
  # Downloading every generated file means looping over the file IDs in the tool
  # result, which doesn't translate to a one-off shell command. Use one of the
  # SDK examples instead.
  ```

  ```bash CLI
  # Extracting every file ID from the tool results and downloading each one
  # requires a loop, which doesn't translate well to a one-off CLI command.
  # Use one of the SDK examples instead.
  ```

  ```python Python
  client = Anthropic()

  # Request code execution that creates files
  response = client.beta.messages.create(
      model="claude-opus-4-8",
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
  def extract_file_ids(response: BetaMessage) -> list[str]:
      file_ids: list[str] = []
      for item in response.content:
          if item.type == "bash_code_execution_tool_result":
              content_item = item.content
              if content_item.type == "bash_code_execution_result":
                  for output_block in content_item.content:
                      file_ids.append(output_block.file_id)
      return file_ids


  # Download the created files
  for file_id in extract_file_ids(response):
      file_metadata = client.beta.files.retrieve_metadata(file_id)
      file_content = client.beta.files.download(file_id)
      file_content.write_to_file(file_metadata.filename)
      print(f"Downloaded: {file_metadata.filename}")
  ```

  ```typescript TypeScript
  import { writeFile } from "node:fs/promises";

  const client = new Anthropic();

  // Request code execution that creates files
  const response = await client.beta.messages.create({
    model: "claude-opus-4-8",
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
  });

  // Extract the file IDs from the response and download each created file
  for (const block of response.content) {
    if (block.type === "bash_code_execution_tool_result") {
      const result = block.content;
      if (result.type === "bash_code_execution_result") {
        for (const outputBlock of result.content) {
          const [fileMetadata, fileResponse] = await Promise.all([
            client.beta.files.retrieveMetadata(outputBlock.file_id),
            client.beta.files.download(outputBlock.file_id)
          ]);
          await writeFile(fileMetadata.filename, await fileResponse.bytes());
          console.log(`Downloaded: ${fileMetadata.filename}`);
        }
      }
    }
  }
  ```

  ```csharp C#
  AnthropicClient client = new();

  var parameters = new MessageCreateParams
  {
      Model = Model.ClaudeOpus4_8,
      MaxTokens = 4096,
      Betas = [AnthropicBeta.FilesApi2025_04_14],
      Messages = [new() { Role = Role.User, Content = "Create a matplotlib visualization and save it as output.png" }],
      Tools = [new BetaCodeExecutionTool20250825()]
  };

  var response = await client.Beta.Messages.Create(parameters);

  // Collect the file IDs from the tool results
  List<string> fileIds = [];
  foreach (var block in response.Content)
  {
      if (!block.TryPickBashCodeExecutionToolResult(out var toolResult))
          continue;
      if (!toolResult.Content.TryPickBetaBashCodeExecutionResultBlock(out var result))
          continue;
      foreach (var output in result.Content)
      {
          fileIds.Add(output.FileID);
      }
  }

  // Download each created file
  foreach (var fileId in fileIds)
  {
      var fileMetadata = await client.Beta.Files.RetrieveMetadata(fileId);
      using var download = await client.Beta.Files.Download(fileId);
      var downloadStream = await download.ReadAsStream();
      await using var target = File.Create(fileMetadata.Filename);
      await downloadStream.CopyToAsync(target);
      Console.WriteLine($"Downloaded: {fileMetadata.Filename}");
  }
  ```

  ```go Go
  	client := anthropic.NewClient()
  	ctx := context.Background()

  	response, err := client.Beta.Messages.New(ctx, anthropic.BetaMessageNewParams{
  		Model:     anthropic.ModelClaudeOpus4_8,
  		MaxTokens: 4096,
  		Messages: []anthropic.BetaMessageParam{
  			anthropic.NewBetaUserMessage(anthropic.NewBetaTextBlock("Create a matplotlib visualization and save it as output.png")),
  		},
  		Tools: []anthropic.BetaToolUnionParam{
  			{OfCodeExecutionTool20250825: &anthropic.BetaCodeExecutionTool20250825Param{}},
  		},
  		Betas: []anthropic.AnthropicBeta{
  			anthropic.AnthropicBetaFilesAPI2025_04_14,
  		},
  	})
  	if err != nil {
  		log.Fatal(err)
  	}

  	fileIDs := extractFileIDs(response)

  	for _, fileID := range fileIDs {
  		fileMetadata, err := client.Beta.Files.GetMetadata(ctx, fileID, anthropic.BetaFileGetMetadataParams{})
  		if err != nil {
  			log.Fatal(err)
  		}

  		fileContent, err := client.Beta.Files.Download(ctx, fileID, anthropic.BetaFileDownloadParams{})
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
  // ...

  func extractFileIDs(response *anthropic.BetaMessage) []string {
  	var fileIDs []string
  	for _, item := range response.Content {
  		switch variant := item.AsAny().(type) {
  		case anthropic.BetaBashCodeExecutionToolResultBlock:
  			// Collect the file IDs from the tool result
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

  ```java Java
  void main() throws Exception {
      AnthropicClient client = AnthropicOkHttpClient.fromEnv();

      MessageCreateParams params = MessageCreateParams.builder()
          .model(Model.CLAUDE_OPUS_4_8)
          .addBeta(AnthropicBeta.FILES_API_2025_04_14)
          .maxTokens(4096L)
          .addUserMessage("Create a matplotlib visualization and save it as output.png")
          .addTool(BetaCodeExecutionTool20250825.builder().build())
          .build();

      BetaMessage response = client.beta().messages().create(params);

      List<String> fileIds = extractFileIds(response);

      for (String fileId : fileIds) {
          FileMetadata fileMetadata = client.beta().files().retrieveMetadata(fileId);
          try (HttpResponse fileContent = client.beta().files().download(fileId)) {
              Files.copy(
                  fileContent.body(),
                  Path.of(fileMetadata.filename()),
                  StandardCopyOption.REPLACE_EXISTING);
          }
          IO.println("Downloaded: " + fileMetadata.filename());
      }
  }

  List<String> extractFileIds(BetaMessage response) {
      List<String> fileIds = new ArrayList<>();
      // Collect the file IDs from the tool results
      for (BetaContentBlock item : response.content()) {
          item.bashCodeExecutionToolResult().ifPresent(toolResult -> {
              if (toolResult.content().isBetaBashCodeExecutionResultBlock()) {
                  BetaBashCodeExecutionResultBlock result =
                      toolResult.content().asBetaBashCodeExecutionResultBlock();
                  for (BetaBashCodeExecutionOutputBlock output : result.content()) {
                      fileIds.add(output.fileId());
                  }
              }
          });
      }
      return fileIds;
  }
  ```

  ```php PHP
  $client = new Client();

  // Request code execution that creates files
  $response = $client->beta->messages->create(
      maxTokens: 4096,
      messages: [
          [
              'role' => 'user',
              'content' => 'Create a matplotlib visualization and save it as output.png',
          ],
      ],
      model: Model::CLAUDE_OPUS_4_8,
      betas: [AnthropicBeta::FILES_API_2025_04_14],
      tools: [new BetaCodeExecutionTool20250825()],
  );

  /**
   * Extract file IDs from the response.
   *
   * @return list<string>
   */
  function extractFileIds(BetaMessage $response): array
  {
      $fileIds = [];
      foreach ($response->content as $block) {
          if ($block->type !== 'bash_code_execution_tool_result') {
              continue;
          }
          $resultBlock = $block->content;
          if ($resultBlock->type !== 'bash_code_execution_result') {
              continue;
          }
          foreach ($resultBlock->content as $outputBlock) {
              $fileIds[] = $outputBlock->fileID;
          }
      }
      return $fileIds;
  }

  // Download the created files
  foreach (extractFileIds($response) as $fileId) {
      $fileMetadata = $client->beta->files->retrieveMetadata($fileId);
      $fileContent = $client->beta->files->download($fileId);

      file_put_contents($fileMetadata->filename, $fileContent);
      echo "Downloaded: {$fileMetadata->filename}\n";
  }
  ```

  ```ruby Ruby
  client = Anthropic::Client.new

  response = client.beta.messages.create(
    model: "claude-opus-4-8",
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
        # WORKAROUND for anthropic-sdk-ruby union coercion bug (SDK-636): item.content is a
        # nested content union, so the typed accessors on `item.content` are unreliable.
        # Read the raw response data through the public `BaseModel#[]` API instead.
        content_item = item.content
        if content_item[:type].to_s == "bash_code_execution_result"
          Array(content_item[:content]).each do |output_block|
            file_ids << output_block[:file_id]
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

Both fields are fixed: `type` selects the tool version, and `name` must be `code_execution`.

When this tool is provided, Claude automatically gains access to two sub-tools:

* `bash_code_execution`: Run shell commands
* `text_editor_code_execution`: View, create, and edit files, including writing code

When Claude runs code, the response also includes a top-level `container` object with the container's `id` and `expires_at` timestamp. Pass that ID back in the top-level `container` request parameter to keep using the same container. See [Container reuse](#container-reuse).

## Response format

The code execution tool can return two types of results depending on the operation:

### Bash command response

```json Output
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
    "return_code": 0,
    "content": []
  }
}
```

### File operation responses

**View file:**

```json Output
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
    "type": "text_editor_code_execution_view_result",
    "file_type": "text",
    "content": "{\n  \"setting\": \"value\",\n  \"debug\": true\n}",
    "num_lines": 4,
    "start_line": 1,
    "total_lines": 4
  }
}
```

**Create file:**

```json Output
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
    "type": "text_editor_code_execution_create_result",
    "is_file_update": false
  }
}
```

**Edit file (str\_replace):**

```json Output
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
    "type": "text_editor_code_execution_str_replace_result",
    "old_start": 3,
    "old_lines": 1,
    "new_start": 3,
    "new_lines": 1,
    "lines": ["-  \"debug\": true", "+  \"debug\": false"]
  }
}
```

### Results

Bash command results (`bash_code_execution_result`) include:

* `stdout`: Output from successful execution
* `stderr`: Error messages if execution fails
* `return_code`: 0 for success, non-zero for failure
* `content`: A list with an entry for each file the command created. Each entry carries the `file_id` to [retrieve the file](#retrieve-generated-files) with the Files API

File operation results have their own fields:

* **View** (`text_editor_code_execution_view_result`): `file_type`, `content`, `num_lines`, `start_line`, `total_lines`
* **Create** (`text_editor_code_execution_create_result`): `is_file_update` (whether the file already existed)
* **Edit** (`text_editor_code_execution_str_replace_result`): `old_start`, `old_lines`, `new_start`, `new_lines`, `lines` (diff format)

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

| Tool         | Error code                | Description                                             |
| ------------ | ------------------------- | ------------------------------------------------------- |
| All tools    | `unavailable`             | The tool is temporarily unavailable                     |
| All tools    | `execution_time_exceeded` | The tool invocation exceeded the maximum execution time |
| All tools    | `invalid_tool_input`      | Invalid parameters provided to the tool                 |
| All tools    | `too_many_requests`       | Rate limit exceeded for tool usage                      |
| bash         | `output_file_too_large`   | Command output exceeded the maximum size                |
| text\_editor | `file_not_found`          | File doesn't exist (for view/edit operations)           |

An expired container can't be reused: requests that reference it return an error instead of restoring it. Send the request again without the `container` parameter to get a new container.

### `pause_turn` stop reason

The response might include a `pause_turn` stop reason, which indicates that the API paused a long-running turn. You may provide the response back as-is in a subsequent request to let Claude continue its turn, or modify the content if you want to interrupt the conversation.

## Containers

The code execution tool runs in a secure, containerized environment designed specifically for code execution, with a higher focus on Python.

### Runtime environment

* **Python version**: 3.11
* **Operating system**: Linux-based container
* **Architecture**: x86\_64 (AMD64)

### Resource limits

* **Memory**: 5GiB RAM
* **Disk space**: 5GiB workspace storage
* **CPU**: 1 CPU
* **Execution time**: A tool invocation that runs past the maximum execution time returns an `execution_time_exceeded` [error](#errors). With [programmatic tool calling](/docs/en/agents-and-tools/tool-use/programmatic-tool-calling), each REPL cell also has a 90-second wall-clock limit

### Networking and security

* **Internet access**: Completely disabled for security
* **External connections**: No outbound network requests permitted
* **Sandbox isolation**: Full isolation from host system and other containers
* **File access**: Limited to workspace directory only
* **Workspace scoping**: Like [Files](/docs/en/build-with-claude/files), containers are scoped to the workspace of the API key
* **Expiration**: Containers expire 30 days after creation

### Pre-installed libraries

The sandboxed Python environment includes these commonly used libraries:

* **Data science**: pandas, numpy, scipy, scikit-learn, statsmodels
* **Visualization**: matplotlib, seaborn
* **File processing**: pyarrow, openpyxl, xlsxwriter, xlrd, pillow, python-pptx, python-docx, pypdf, pdfplumber, pypdfium2, pdf2image, pdfkit, tabula-py, reportlab\[pycairo], Img2pdf
* **Math and computing**: sympy, mpmath
* **Utilities**: tqdm, python-dateutil, pytz, joblib

The container also includes command-line tools such as unzip, unrar, 7zip, bc, rg (ripgrep), fd, and sqlite.

The container has no internet access, so Claude can't download or install additional packages at runtime: only the pre-installed libraries are available.

## Container reuse

You can reuse an existing container across multiple API requests by providing the container ID from a previous response. This allows you to maintain created files between requests. With `code_execution_20260120` or later and [programmatic tool calling](/docs/en/agents-and-tools/tool-use/programmatic-tool-calling), the Python interpreter state persists as well.

Containers expire 30 days after creation. After about five minutes of inactivity a container is checkpointed, and sending a request with its ID inside the 30-day window restores it. The `expires_at` timestamp in the response's `container` object is a shorter rolling value and doesn't report the 30-day limit. A container that has expired can't be reused. Send the request again without the `container` parameter to get a new container.

### Example

<CodeGroup>
  ```bash cURL
  # First request: Create a file with a random number, capturing the container ID (using jq)
  CONTAINER_ID=$(curl -s https://api.anthropic.com/v1/messages \
    -H "x-api-key: $ANTHROPIC_API_KEY" \
    -H "anthropic-version: 2023-06-01" \
    -H "content-type: application/json" \
    -d '{
      "model": "claude-opus-4-8",
      "max_tokens": 4096,
      "messages": [{
        "role": "user",
        "content": "Write a file with a random number and save it to \"/tmp/number.txt\""
      }],
      "tools": [{
        "type": "code_execution_20250825",
        "name": "code_execution"
      }]
    }' | jq -r '.container.id')

  # Second request: Reuse the container to read the file
  curl https://api.anthropic.com/v1/messages \
    -H "x-api-key: $ANTHROPIC_API_KEY" \
    -H "anthropic-version: 2023-06-01" \
    -H "content-type: application/json" \
    -d '{
      "container": "'"$CONTAINER_ID"'",
      "model": "claude-opus-4-8",
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
    --model claude-opus-4-8 \
    --max-tokens 4096 \
    --message '{role: user, content: Write a file with a random number and save it to "/tmp/number.txt"}' \
    --tool '{type: code_execution_20250825, name: code_execution}' \
    --transform container.id --raw-output)

  # Second request: Reuse the container to read the file
  ant messages create \
    --container "$CONTAINER_ID" \
    --model claude-opus-4-8 \
    --max-tokens 4096 \
    --message '{role: user, content: Read the number from "/tmp/number.txt" and calculate its square}' \
    --tool '{type: code_execution_20250825, name: code_execution}'
  ```

  ```python Python
  client = anthropic.Anthropic()

  # First request: create a file with a random number in a new container
  response1 = client.messages.create(
      model="claude-opus-4-8",
      max_tokens=4096,
      messages=[
          {
              "role": "user",
              "content": "Write a file with a random number and save it to '/tmp/number.txt'",
          }
      ],
      tools=[{"type": "code_execution_20250825", "name": "code_execution"}],
  )

  # Second request: pass the container ID back so Claude reuses the same container
  response2 = client.messages.create(
      container=response1.container.id,
      model="claude-opus-4-8",
      max_tokens=4096,
      messages=[
          {
              "role": "user",
              "content": "Read the number from '/tmp/number.txt' and calculate its square",
          }
      ],
      tools=[{"type": "code_execution_20250825", "name": "code_execution"}],
  )

  print(response2.to_json())
  ```

  ```typescript TypeScript
  const client = new Anthropic();

  // First request: Claude creates a file inside a fresh code execution container
  const response1 = await client.messages.create({
    model: "claude-opus-4-8",
    max_tokens: 4096,
    messages: [
      {
        role: "user",
        content: "Write a file with a random number and save it to '/tmp/number.txt'"
      }
    ],
    tools: [{ type: "code_execution_20250825", name: "code_execution" }]
  });

  // The response includes the container once the code execution tool has run
  if (!response1.container) {
    throw new Error("Expected the first response to include a container");
  }

  // Second request: pass the container ID back so it reuses the same container
  const response2 = await client.messages.create({
    container: response1.container.id,
    model: "claude-opus-4-8",
    max_tokens: 4096,
    messages: [
      { role: "user", content: "Read the number from /tmp/number.txt and calculate its square" }
    ],
    tools: [{ type: "code_execution_20250825", name: "code_execution" }]
  });

  console.log(JSON.stringify(response2));
  ```

  ```csharp C#
  AnthropicClient client = new();

  // First request: Claude creates a file inside a fresh code execution container
  var response1 = await client.Messages.Create(new()
  {
      Model = Model.ClaudeOpus4_8,
      MaxTokens = 4096,
      Messages = [new() { Role = Role.User, Content = "Write a file with a random number and save it to '/tmp/number.txt'" }],
      Tools = [new CodeExecutionTool20250825()]
  });

  // Second request: pass the container ID back so Claude reuses the same container
  var response2 = await client.Messages.Create(new()
  {
      Container = response1.Container!.ID,
      Model = Model.ClaudeOpus4_8,
      MaxTokens = 4096,
      Messages = [new() { Role = Role.User, Content = "Read the number from '/tmp/number.txt' and calculate its square" }],
      Tools = [new CodeExecutionTool20250825()]
  });

  Console.WriteLine(response2);
  ```

  ```go Go
  client := anthropic.NewClient()
  ctx := context.Background()

  codeExecution := []anthropic.ToolUnionParam{
  	{OfCodeExecutionTool20250825: &anthropic.CodeExecutionTool20250825Param{}},
  }

  // First request: create a file with a random number in a new container
  response1, err := client.Messages.New(ctx, anthropic.MessageNewParams{
  	Model:     anthropic.ModelClaudeOpus4_8,
  	MaxTokens: 4096,
  	Messages: []anthropic.MessageParam{
  		anthropic.NewUserMessage(anthropic.NewTextBlock("Write a file with a random number and save it to '/tmp/number.txt'")),
  	},
  	Tools: codeExecution,
  })
  if err != nil {
  	log.Fatal(err)
  }

  // Reuse the container from the first request so the file is still there.
  response2, err := client.Messages.New(ctx, anthropic.MessageNewParams{
  	Container: anthropic.String(response1.Container.ID),
  	Model:     anthropic.ModelClaudeOpus4_8,
  	MaxTokens: 4096,
  	Messages: []anthropic.MessageParam{
  		anthropic.NewUserMessage(anthropic.NewTextBlock("Read the number from '/tmp/number.txt' and calculate its square")),
  	},
  	Tools: codeExecution,
  })
  if err != nil {
  	log.Fatal(err)
  }

  fmt.Println(response2.RawJSON())
  ```

  ```java Java
  AnthropicClient client = AnthropicOkHttpClient.fromEnv();

  // First request: create a file with a random number in a new container
  MessageCreateParams params1 = MessageCreateParams.builder()
      .model(Model.CLAUDE_OPUS_4_8)
      .maxTokens(4096L)
      .addUserMessage("Write a file with a random number and save it to '/tmp/number.txt'")
      .addTool(CodeExecutionTool20250825.builder().build())
      .build();

  Message response1 = client.messages().create(params1);

  // Second request: pass the container ID back so it reuses the same container
  MessageCreateParams params2 = MessageCreateParams.builder()
      .container(response1.container().orElseThrow().id())
      .model(Model.CLAUDE_OPUS_4_8)
      .maxTokens(4096L)
      .addUserMessage("Read the number from '/tmp/number.txt' and calculate its square")
      .addTool(CodeExecutionTool20250825.builder().build())
      .build();

  Message response2 = client.messages().create(params2);
  IO.println(ObjectMappers.jsonMapper().valueToTree(response2));
  ```

  ```php PHP
  $client = new Client();

  // First request: Claude writes the file inside a fresh code execution container
  $response1 = $client->messages->create(
      maxTokens: 4096,
      messages: [
          [
              'role' => 'user',
              'content' => "Write a file with a random number and save it to '/tmp/number.txt'",
          ],
      ],
      model: Model::CLAUDE_OPUS_4_8,
      tools: [new CodeExecutionTool20250825()],
  );

  // Second request: reuse the container so '/tmp/number.txt' is still there
  $response2 = $client->messages->create(
      container: $response1->container->id,
      maxTokens: 4096,
      messages: [
          [
              'role' => 'user',
              'content' => "Read the number from '/tmp/number.txt' and calculate its square",
          ],
      ],
      model: Model::CLAUDE_OPUS_4_8,
      tools: [new CodeExecutionTool20250825()],
  );

  echo json_encode($response2), PHP_EOL;
  ```

  ```ruby Ruby
  client = Anthropic::Client.new

  # First request: Claude creates the file inside a fresh code execution container
  response1 = client.messages.create(
    model: Anthropic::Model::CLAUDE_OPUS_4_8,
    max_tokens: 4096,
    messages: [
      {
        role: "user",
        content: "Write a file with a random number and save it to '/tmp/number.txt'"
      }
    ],
    tools: [Anthropic::CodeExecutionTool20250825.new]
  )

  # Second request: pass the container ID back so Claude reuses the same container
  response2 = client.messages.create(
    container: response1.container.id,
    model: Anthropic::Model::CLAUDE_OPUS_4_8,
    max_tokens: 4096,
    messages: [
      {
        role: "user",
        content: "Read the number from '/tmp/number.txt' and calculate its square"
      }
    ],
    tools: [Anthropic::CodeExecutionTool20250825.new]
  )

  puts response2.to_json
  ```
</CodeGroup>

## Using code execution with other execution tools

When you provide code execution alongside client-provided tools that also run code (such as a [Bash tool](/docs/en/agents-and-tools/tool-use/bash-tool) or custom REPL), Claude is operating in a multi-computer environment. The code execution tool runs in Anthropic's sandboxed container, while your client-provided tools run in a separate environment that you control. Claude can sometimes confuse these environments, attempting to use the wrong tool or assuming state is shared between them.

To avoid this, add instructions to your system prompt that clarify the distinction:

```text wrap
When multiple code execution environments are available, be aware that:
- Variables, files, and state do NOT persist between different execution environments
- Use the code_execution tool for general-purpose computation in Anthropic's sandboxed environment
- Use client-provided execution tools (e.g., bash) when you need access to the user's local system, files, or data
- If you need to pass results between environments, explicitly include outputs in subsequent tool calls rather than assuming shared state
```

This is especially important when combining code execution with [web search](/docs/en/agents-and-tools/tool-use/web-search-tool) or [web fetch](/docs/en/agents-and-tools/tool-use/web-fetch-tool), which enable code execution automatically. If your application already provides a client-side shell tool, the automatic code execution creates a second execution environment that Claude needs to distinguish between.

When Claude calls one of your client tools alongside code execution, the API returns the code execution call without its result. The result arrives in a later response, after you send back the `tool_result` blocks for your client tools.

## Streaming

With [streaming](/docs/en/build-with-claude/streaming) enabled (`"stream": true`), you'll receive code execution events as they occur. The sub-tool input streams as `input_json_delta` events, and each result block arrives whole in a single `content_block_start` event:

```sse
event: content_block_start
data: {"type": "content_block_start", "index": 1, "content_block": {"type": "server_tool_use", "id": "srvtoolu_xyz789", "name": "bash_code_execution"}}

// Tool input streamed as partial JSON
event: content_block_delta
data: {"type": "content_block_delta", "index": 1, "delta": {"type": "input_json_delta", "partial_json": "{\"command\": \"python analyze.py\"}"}}

// Pause while the command runs

// Execution result delivered as a complete block
event: content_block_start
data: {"type": "content_block_start", "index": 2, "content_block": {"type": "bash_code_execution_tool_result", "tool_use_id": "srvtoolu_xyz789", "content": {"type": "bash_code_execution_result", "stdout": "   A  B  C\n0  1  2  3\n1  4  5  6", "stderr": "", "return_code": 0, "content": []}}}
```

## Batch requests

You can include the code execution tool in the [Messages Batches API](/docs/en/build-with-claude/batch-processing). Code execution tool calls through the Messages Batches API are priced the same as those in regular Messages API requests.

## Usage and pricing

**Code execution is free when used with web search or web fetch.** When `web_search_20260209` (or later) or `web_fetch_20260209` (or later) is included in your API request, there are no additional charges for code execution tool calls beyond the standard input and output token costs.

When used without these tools, code execution is billed by execution time, tracked separately from token usage:

* Execution time has a minimum of 5 minutes
* Each organization receives **1,550 free hours** of usage per month
* Additional usage beyond 1,550 hours is billed at **$0.05 per hour, per container**
* If files are included in the request, execution time is billed even if the tool is not invoked, due to files being preloaded onto the container

Code execution usage is tracked in the response:

```json
{
  "usage": {
    "input_tokens": 105,
    "output_tokens": 239,
    "server_tool_use": {
      "code_execution_requests": 1
    }
  }
}
```

## Upgrade to latest tool version

The latest tool version is `code_execution_20260521`. To move between the three current versions, update the `type` string in your request: all three return the response blocks documented in [Response format](#response-format). See [Model compatibility](#model-compatibility) for what each version adds and which models support it.

The rest of this section covers migrating from the legacy Python-only `code_execution_20250522` to the current tool versions.

### What's changed

| Component      | Legacy                      | Current                                                             |
| -------------- | --------------------------- | ------------------------------------------------------------------- |
| Beta header    | `code-execution-2025-05-22` | None required                                                       |
| Tool type      | `code_execution_20250522`   | `code_execution_20250825` or later                                  |
| Capabilities   | Python only                 | Bash commands, file operations                                      |
| Response types | `code_execution_result`     | `bash_code_execution_result`, `text_editor_code_execution_*_result` |

### Backward compatibility

* All existing Python code execution continues to work exactly as before
* No changes required to existing Python-only workflows

### Upgrade steps

To upgrade, update the tool type in your API requests:

```diff
- "type": "code_execution_20250522"
+ "type": "code_execution_20250825"
```

**Review response handling** (if parsing responses programmatically):

* The previous blocks for Python execution responses will no longer be sent
* Instead, new response types for Bash and file operations will be sent (see [Response format](#response-format))

## Data retention

Code execution runs in server-side sandbox containers. Container data, including execution artifacts, uploaded files, and outputs, is retained for up to 30 days. This retention applies to all data processed within the container environment. Files that code execution creates in the [Files API](/docs/en/build-with-claude/files) (retrievable with `client.beta.files.download()`) persist until explicitly deleted.

For ZDR eligibility across all features, see [API and data retention](/docs/en/manage-claude/api-and-data-retention).

## Next steps

<CardGroup cols={2}>
  <Card title="Advisor tool" icon="compass" href="/docs/en/agents-and-tools/tool-use/advisor-tool">
    Pair a faster executor model with a higher-intelligence advisor model that provides strategic guidance mid-generation.
  </Card>

  <Card title="Programmatic tool calling" icon="code" href="/docs/en/agents-and-tools/tool-use/programmatic-tool-calling">
    Call your own tools from code that runs inside the code execution container.
  </Card>

  <Card title="Files API" icon="file" href="/docs/en/build-with-claude/files">
    Upload files for analysis and download the files that code execution creates.
  </Card>

  <Card title="Using Agent Skills with the API" icon="book" href="/docs/en/build-with-claude/skills-guide">
    Learn how to use Agent Skills to extend Claude's capabilities through the API.
  </Card>
</CardGroup>
