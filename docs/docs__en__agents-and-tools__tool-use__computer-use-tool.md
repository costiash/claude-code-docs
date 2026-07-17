# Computer use tool

Give Claude screenshot, mouse, and keyboard control of a desktop environment with the computer use tool.

---

Claude can interact with computer environments through the computer use tool, which provides screenshot capabilities and mouse/keyboard control for autonomous desktop interaction.

<Note>
  Computer use is in beta and requires a [beta header](/docs/en/api/beta-headers):

  * `"computer-use-2025-11-24"` for Claude Sonnet 5, Claude Opus 4.8, Claude Opus 4.7, Claude Opus 4.6, Claude Sonnet 4.6, and Claude Opus 4.5
  * `"computer-use-2025-01-24"` for Claude Sonnet 4.5, Claude Haiku 4.5, Claude Opus 4.1 ([deprecated](/docs/en/about-claude/model-deprecations)), Claude Sonnet 4 ([retired, except on Bedrock and Google Cloud](/docs/en/about-claude/model-deprecations)), and Claude Opus 4 ([retired, except on Google Cloud](/docs/en/about-claude/model-deprecations))

  Reach out through the [feedback form](https://forms.gle/H6UFuXaaLywri9hz6) to share your feedback on this feature.
</Note>

<Note>
  For how zero data retention (ZDR) applies to this feature, see [API and data retention](/docs/en/manage-claude/api-and-data-retention).
</Note>

## Overview

Computer use is a beta feature that enables Claude to interact with desktop environments. This tool provides:

* **Screenshot capture:** See what's currently displayed on screen
* **Mouse control:** Click, drag, and move the cursor
* **Keyboard input:** Type text and use keyboard shortcuts
* **Desktop automation:** Interact with any application or interface

While computer use can be augmented with other tools such as bash and text editor for more comprehensive automation workflows, computer use specifically refers to the computer use tool's capability to see and control desktop environments.

For model support, see the [Tool reference](/docs/en/agents-and-tools/tool-use/tool-reference).

## Security considerations

Computer use is a beta feature with unique risks distinct from standard API features. These risks are heightened when interacting with the internet.

<Warning>
  To minimize risks, consider taking precautions such as:

  1. Using a dedicated virtual machine or container with minimal privileges to prevent direct system attacks or accidents.
  2. Avoiding giving the model access to sensitive data, such as account login information, to prevent information theft.
  3. Limiting internet access to an allowlist of domains to reduce exposure to malicious content.
  4. Asking a human to confirm decisions that might result in meaningful real-world consequences and any tasks requiring affirmative consent, such as accepting cookies, completing financial transactions, or agreeing to terms of service.
</Warning>

In some circumstances, Claude will follow commands found in content even when they conflict with your instructions. For example, instructions on webpages or contained in images might override your instructions or cause Claude to make mistakes. Take precautions to isolate Claude from sensitive data and actions to avoid risks related to prompt injection.

Anthropic has trained the model to resist these prompt injections and has added an extra layer of defense. If you use the computer use tools, classifiers will automatically run on your prompts to flag potential instances of prompt injections. When these classifiers identify potential prompt injections in screenshots, they will automatically steer the model to ask for user confirmation before proceeding with the next action. This extra protection won't be ideal for every use case (for example, use cases without a human in the loop), so if you'd like to opt out and turn it off, [contact support](https://support.claude.com/en/).

These precautions remain important even with the classifier defense layer in place.

Inform end users of relevant risks and obtain their consent prior to enabling computer use in your own products.

<Card title="Computer use reference implementation" icon="computer" href="https://github.com/anthropics/anthropic-quickstarts/tree/main/computer-use-demo">
  Get started with the computer use reference implementation that includes a web interface, Docker container, example tool implementations, and an agent loop.
</Card>

## Quick start

Here's how to get started with computer use:

<CodeGroup>
  ```bash cURL
  curl https://api.anthropic.com/v1/messages \
    -H "content-type: application/json" \
    -H "x-api-key: $ANTHROPIC_API_KEY" \
    -H "anthropic-version: 2023-06-01" \
    -H "anthropic-beta: computer-use-2025-11-24" \
    -d '{
      "model": "claude-opus-4-8",
      "max_tokens": 1024,
      "tools": [
        {
          "type": "computer_20251124",
          "name": "computer",
          "display_width_px": 1024,
          "display_height_px": 768,
          "display_number": 1
        },
        {
          "type": "text_editor_20250728",
          "name": "str_replace_based_edit_tool"
        },
        {
          "type": "bash_20250124",
          "name": "bash"
        }
      ],
      "messages": [
        {
          "role": "user",
          "content": "Save a picture of a cat to my desktop."
        }
      ]
    }'
  ```

  ```bash CLI
  ant beta:messages create --beta computer-use-2025-11-24 <<'YAML'
  model: claude-opus-4-8
  max_tokens: 1024
  tools:
    - type: computer_20251124
      name: computer
      display_width_px: 1024
      display_height_px: 768
      display_number: 1
    - type: text_editor_20250728
      name: str_replace_based_edit_tool
    - type: bash_20250124
      name: bash
  messages:
    - role: user
      content: Save a picture of a cat to my desktop.
  YAML
  ```

  ```python Python
  client = anthropic.Anthropic()

  response = client.beta.messages.create(
      model="claude-opus-4-8",  # or another compatible model
      max_tokens=1024,
      tools=[
          {
              "type": "computer_20251124",
              "name": "computer",
              "display_width_px": 1024,
              "display_height_px": 768,
              "display_number": 1,
          },
          {"type": "text_editor_20250728", "name": "str_replace_based_edit_tool"},
          {"type": "bash_20250124", "name": "bash"},
      ],
      messages=[{"role": "user", "content": "Save a picture of a cat to my desktop."}],
      betas=["computer-use-2025-11-24"],
  )
  print(response)
  ```

  ```typescript TypeScript
  const client = new Anthropic();

  const response = await client.beta.messages.create({
    model: "claude-opus-4-8",
    max_tokens: 1024,
    tools: [
      {
        type: "computer_20251124",
        name: "computer",
        display_width_px: 1024,
        display_height_px: 768,
        display_number: 1
      },
      {
        type: "text_editor_20250728",
        name: "str_replace_based_edit_tool"
      },
      {
        type: "bash_20250124",
        name: "bash"
      }
    ],
    messages: [{ role: "user", content: "Save a picture of a cat to my desktop." }],
    betas: ["computer-use-2025-11-24"]
  });

  console.log(response);
  ```

  ```csharp C#
  using Anthropic.Models.Beta.Messages;
  using Messages = Anthropic.Models.Messages;

  var client = new AnthropicClient();

  var parameters = new MessageCreateParams
  {
      Model = Messages::Model.ClaudeOpus4_8,
      MaxTokens = 1024,
      Tools = new BetaToolUnion[]
      {
          new BetaToolComputerUse20251124
          {
              DisplayWidthPx = 1024,
              DisplayHeightPx = 768,
              DisplayNumber = 1
          },
          new BetaToolTextEditor20250728(),
          new BetaToolBash20250124()
      },
      Messages =
      [
          new BetaMessageParam
          {
              Role = Role.User,
              Content = "Save a picture of a cat to my desktop."
          }
      ],
      Betas = ["computer-use-2025-11-24"]
  };

  var response = await client.Beta.Messages.Create(parameters);
  Console.WriteLine(response);
  ```

  ```go Go
  client := anthropic.NewClient()

  response, err := client.Beta.Messages.New(context.TODO(), anthropic.BetaMessageNewParams{
  	Model:     anthropic.ModelClaudeOpus4_8,
  	MaxTokens: 1024,
  	Tools: []anthropic.BetaToolUnionParam{
  		{OfComputerUseTool20251124: &anthropic.BetaToolComputerUse20251124Param{
  			DisplayWidthPx:  1024,
  			DisplayHeightPx: 768,
  			DisplayNumber:   anthropic.Int(1),
  		}},
  		{OfTextEditor20250728: &anthropic.BetaToolTextEditor20250728Param{}},
  		{OfBashTool20250124: &anthropic.BetaToolBash20250124Param{}},
  	},
  	Messages: []anthropic.BetaMessageParam{
  		anthropic.NewBetaUserMessage(anthropic.NewBetaTextBlock("Save a picture of a cat to my desktop.")),
  	},
  	Betas: []anthropic.AnthropicBeta{
  		"computer-use-2025-11-24", // no SDK exposes a named constant for this beta yet
  	},
  })
  if err != nil {
  	log.Fatal(err)
  }
  fmt.Println(response)
  ```

  ```java Java
  import com.anthropic.models.beta.messages.BetaMessage;
  import com.anthropic.models.beta.messages.BetaToolBash20250124;
  import com.anthropic.models.beta.messages.BetaToolComputerUse20251124;
  import com.anthropic.models.beta.messages.BetaToolTextEditor20250728;
  import com.anthropic.models.beta.messages.MessageCreateParams;
  import com.anthropic.models.messages.Model;

  void main() {
      AnthropicClient client = AnthropicOkHttpClient.fromEnv();

      MessageCreateParams params = MessageCreateParams.builder()
          .model(Model.CLAUDE_OPUS_4_8)
          .maxTokens(1024L)
          .addTool(BetaToolComputerUse20251124.builder()
              .displayWidthPx(1024L)
              .displayHeightPx(768L)
              .displayNumber(1L)
              .build())
          .addTool(BetaToolTextEditor20250728.builder().build())
          .addTool(BetaToolBash20250124.builder().build())
          .addUserMessage("Save a picture of a cat to my desktop.")
          .addBeta("computer-use-2025-11-24")
          .build();

      BetaMessage response = client.beta().messages().create(params);
      IO.println(response);
  }
  ```

  ```php PHP
  $client = new Client();

  $response = $client->beta->messages->create(
      maxTokens: 1024,
      messages: [
          ['role' => 'user', 'content' => 'Save a picture of a cat to my desktop.'],
      ],
      model: 'claude-opus-4-8',
      tools: [
          [
              'type' => 'computer_20251124',
              'name' => 'computer',
              'display_width_px' => 1024,
              'display_height_px' => 768,
              'display_number' => 1,
          ],
          [
              'type' => 'text_editor_20250728',
              'name' => 'str_replace_based_edit_tool',
          ],
          [
              'type' => 'bash_20250124',
              'name' => 'bash',
          ],
      ],
      betas: ['computer-use-2025-11-24'],
  );

  echo $response;
  ```

  ```ruby Ruby
  client = Anthropic::Client.new

  response = client.beta.messages.create(
    model: "claude-opus-4-8",
    max_tokens: 1024,
    tools: [
      {
        type: "computer_20251124",
        name: "computer",
        display_width_px: 1024,
        display_height_px: 768,
        display_number: 1
      },
      {
        type: "text_editor_20250728",
        name: "str_replace_based_edit_tool"
      },
      {
        type: "bash_20250124",
        name: "bash"
      }
    ],
    messages: [
      { role: "user", content: "Save a picture of a cat to my desktop." }
    ],
    betas: ["computer-use-2025-11-24"]
  )

  puts response
  ```
</CodeGroup>

<Note>
  A beta header is only required for the computer use tool.

  The preceding example shows all three tools being used together, which requires the beta header because it includes the computer use tool.
</Note>

***

## How computer use works

<Steps>
  <Step title="Provide Claude with the computer use tool and a user prompt" icon="tool">
    * Add the computer use tool (and optionally other tools) to your API request.
    * Include a user prompt that requires desktop interaction, for example, "Save a picture of a cat to my desktop."
  </Step>

  <Step title="Claude selects the computer use tool" icon="wrench">
    * Claude assesses if the computer use tool can help with the user's query.
    * If yes, Claude constructs a properly formatted tool use request.
    * The API response has a `stop_reason` of `tool_use`, signaling a tool use request.
  </Step>

  <Step title="Extract tool input, evaluate the tool on a computer, and return results" icon="computer">
    * On your end, extract the tool name and input from Claude's request.
    * Use the tool on a container or virtual machine.
    * Continue the conversation with a new `user` message containing a `tool_result` content block.
  </Step>

  <Step title="Claude continues calling computer use tools until it's completed the task" icon="arrows-clockwise">
    * Claude analyzes the tool results to determine if more tool use is needed or the task has been completed.
    * If Claude determines another tool is needed, it responds with another `tool_use` `stop_reason` and you should return to step 3.
    * Otherwise, it crafts a text response to the user.
  </Step>
</Steps>

The repetition of steps 3 and 4 without user input is referred to as the "agent loop" (that is, Claude responding with a tool use request and your application responding to Claude with the results of evaluating that request).

### The computing environment

Computer use requires a sandboxed computing environment where Claude can safely interact with applications and the web. This environment includes:

1. **Virtual display:** A virtual X11 display server (using Xvfb) that renders the desktop interface Claude will see through screenshots and control with mouse/keyboard actions.

2. **Desktop environment:** A lightweight UI with window manager (Mutter) and panel (Tint2) running on Linux, which provides a consistent graphical interface for Claude to interact with.

3. **Applications:** Pre-installed Linux applications such as Firefox, LibreOffice, text editors, and file managers that Claude can use to complete tasks.

4. **Tool implementations:** Integration code that translates Claude's abstract tool requests (such as "move mouse" or "take screenshot") into actual operations in the virtual environment.

5. **Agent loop:** A program that handles communication between Claude and the environment, sending Claude's actions to the environment and returning the results (screenshots, command outputs) back to Claude.

When you use computer use, Claude doesn't directly connect to this environment. Instead, your application:

1. Receives Claude's tool use requests
2. Translates them into actions in your computing environment
3. Captures the results (such as screenshots and command outputs)
4. Returns these results to Claude

For security and isolation, the reference implementation runs all of this inside a Docker container with appropriate port mappings for viewing and interacting with the environment.

***

## How to implement computer use

### Start with the reference implementation

A [reference implementation](https://github.com/anthropics/anthropic-quickstarts/tree/main/computer-use-demo) is available that includes everything you need to get started with computer use:

* A [containerized environment](https://github.com/anthropics/anthropic-quickstarts/blob/main/computer-use-demo/Dockerfile) suitable for computer use with Claude
* Implementations of [the computer use tools](https://github.com/anthropics/anthropic-quickstarts/tree/main/computer-use-demo/computer_use_demo/tools)
* An [agent loop](https://github.com/anthropics/anthropic-quickstarts/blob/main/computer-use-demo/computer_use_demo/loop.py) that interacts with the Claude API and runs the computer use tools
* A web interface to interact with the container, agent loop, and tools.

### Understand the agent loop

The core of computer use is the "agent loop": a cycle where Claude requests tool actions, your application runs them, and returns results to Claude. The loop uses the client you created in the [Quick start](#quick-start), a tool list shaped like the Quick start's `tools` array, and the tool-call processing helper defined in [Process Claude's tool calls](#implement-the-computer-use-tool). Here's a simplified example:

<CodeGroup>
  ```bash cURL
  # The agent loop is a stateful, multi-turn pattern that doesn't translate to a
  # one-off shell command. See the SDK tabs for the implementation.
  ```

  ```bash CLI
  # The agent loop is a stateful, multi-turn pattern that doesn't translate to a
  # one-off shell command. See the SDK tabs for the implementation.
  ```

  ```python Python
  def sampling_loop(model, messages, max_iterations=10):
      """
      Run the computer-use agent loop until Claude stops requesting tools
      or the iteration limit is reached.
      """
      for _ in range(max_iterations):
          response = client.beta.messages.create(
              model=model,
              max_tokens=4096,
              messages=messages,
              tools=TOOLS,
              betas=["computer-use-2025-11-24"],
          )

          # Add Claude's response to the conversation history
          messages.append({"role": "assistant", "content": response.content})

          # Run any tools Claude requested and collect results
          tool_results = process_tool_calls(response)
          if not tool_results:
              return messages  # No more tool use; task complete

          # Send tool results back to Claude for the next iteration
          messages.append({"role": "user", "content": tool_results})

      return messages
  ```

  ```typescript TypeScript
  async function samplingLoop(
    model: string,
    messages: Anthropic.Beta.BetaMessageParam[],
    maxIterations = 10,
  ): Promise<Anthropic.Beta.BetaMessageParam[]> {
    // Run the computer-use agent loop until Claude stops requesting tools
    // or the iteration limit is reached.
    for (let i = 0; i < maxIterations; i++) {
      const response = await client.beta.messages.create({
        model,
        max_tokens: 4096,
        messages,
        tools,
        betas: ["computer-use-2025-11-24"],
      });

      // Add Claude's response to the conversation history
      messages.push({ role: "assistant", content: response.content });

      // Run any tools Claude requested and collect results
      const toolResults = processToolCalls(response);
      if (toolResults.length === 0) {
        return messages; // No more tool use; task complete
      }

      // Send tool results back to Claude for the next iteration
      messages.push({ role: "user", content: toolResults });
    }

    return messages;
  }
  ```

  ```csharp C#
  async Task<List<BetaMessageParam>> SamplingLoop(
      Model model,
      List<BetaMessageParam> messages,
      int maxIterations = 10
  )
  {
      // Run the computer-use agent loop until Claude stops requesting tools
      // or the iteration limit is reached.
      for (var i = 0; i < maxIterations; i++)
      {
          var response = await client.Beta.Messages.Create(
              new MessageCreateParams
              {
                  Model = model,
                  MaxTokens = 4096,
                  Messages = messages,
                  Tools = tools,
                  Betas = ["computer-use-2025-11-24"],
              }
          );

          // Add Claude's response to the conversation history
          messages.Add(
              new()
              {
                  Role = Role.Assistant,
                  Content = response
                      .Content.Select(block => new BetaContentBlockParam(block.Json))
                      .ToList(),
              }
          );

          // Run any tools Claude requested and collect results
          var toolResults = ProcessToolCalls(response);
          if (toolResults.Count == 0)
          {
              return messages; // No more tool use; task complete
          }

          // Send tool results back to Claude for the next iteration
          messages.Add(new() { Role = Role.User, Content = toolResults });
      }

      return messages;
  }
  ```

  ```go Go
  // samplingLoop runs the computer-use agent loop until Claude stops
  // requesting tools or the iteration limit is reached.
  func samplingLoop(ctx context.Context, model anthropic.Model, messages []anthropic.BetaMessageParam, maxIterations int) ([]anthropic.BetaMessageParam, error) {
  	for range maxIterations {
  		response, err := client.Beta.Messages.New(ctx, anthropic.BetaMessageNewParams{
  			Model:     model,
  			MaxTokens: 4096,
  			Messages:  messages,
  			Tools:     tools,
  			Betas:     []anthropic.AnthropicBeta{"computer-use-2025-11-24"},
  		})
  		if err != nil {
  			return nil, err
  		}

  		// Add Claude's response to the conversation history
  		messages = append(messages, response.ToParam())

  		// Run any tools Claude requested and collect results
  		toolResults := processToolCalls(response)
  		if len(toolResults) == 0 {
  			return messages, nil // No more tool use; task complete
  		}

  		// Send tool results back to Claude for the next iteration
  		messages = append(messages, anthropic.BetaMessageParam{
  			Role:    anthropic.BetaMessageParamRoleUser,
  			Content: toolResults,
  		})
  	}
  	return messages, nil
  }

  ```

  ```java Java
  /**
   * Run the computer-use agent loop until Claude stops requesting tools
   * or the iteration limit is reached.
   */
  List<BetaMessageParam> samplingLoop(Model model, List<BetaMessageParam> messages, int maxIterations) {
      for (int i = 0; i < maxIterations; i++) {
          BetaMessage response = client.beta().messages().create(MessageCreateParams.builder()
                  .model(model)
                  .maxTokens(4096)
                  .messages(messages)
                  .addTool(COMPUTER_TOOL)
                  .addBeta("computer-use-2025-11-24")
                  .build());

          // Add Claude's response to the conversation history
          messages.add(BetaMessageParam.builder()
                  .role(BetaMessageParam.Role.ASSISTANT)
                  .contentOfBetaContentBlockParams(
                          response.content().stream().map(BetaContentBlock::toParam).toList())
                  .build());

          // Run any tools Claude requested and collect results
          List<BetaContentBlockParam> toolResults = processToolCalls(response);
          if (toolResults.isEmpty()) {
              return messages; // No more tool use; task complete
          }

          // Send tool results back to Claude for the next iteration
          messages.add(BetaMessageParam.builder()
                  .role(BetaMessageParam.Role.USER)
                  .contentOfBetaContentBlockParams(toolResults)
                  .build());
      }
      return messages;
  }
  ```

  ```php PHP
  /**
   * Run the computer-use agent loop until Claude stops requesting tools
   * or the iteration limit is reached.
   */
  function samplingLoop(string $model, array $messages, int $maxIterations = 10): array
  {
      global $client, $tools;

      for ($i = 0; $i < $maxIterations; $i++) {
          $response = $client->beta->messages->create(
              model: $model,
              maxTokens: 4096,
              messages: $messages,
              tools: $tools,
              betas: ['computer-use-2025-11-24'],
          );

          // Add Claude's response to the conversation history
          $messages[] = BetaMessageParam::with(role: Role::ASSISTANT, content: $response->content);

          // Run any tools Claude requested and collect results
          $toolResults = processToolCalls($response);
          if ($toolResults === []) {
              return $messages; // No more tool use; task complete
          }

          // Send tool results back to Claude for the next iteration
          $messages[] = BetaMessageParam::with(role: Role::USER, content: $toolResults);
      }

      return $messages;
  }
  ```

  ```ruby Ruby
  # Run the computer-use agent loop until Claude stops requesting tools
  # or the iteration limit is reached.
  def sampling_loop(model, messages, max_iterations: 10)
    max_iterations.times do
      response = CLIENT.beta.messages.create(
        model: model,
        max_tokens: 4096,
        messages: messages,
        tools: TOOLS,
        betas: ["computer-use-2025-11-24"]
      )

      # Add Claude's response to the conversation history
      messages << {role: "assistant", content: response.content}

      # Run any tools Claude requested and collect results
      tool_results = process_tool_calls(response)
      return messages if tool_results.empty? # No more tool use; task complete

      # Send tool results back to Claude for the next iteration
      messages << {role: "user", content: tool_results}
    end

    messages
  end
  ```
</CodeGroup>

The loop continues until either Claude responds without requesting any tools (task completion) or the maximum iteration limit is reached. This safeguard prevents potential infinite loops that could result in unexpected API costs.

Try the reference implementation out before reading the rest of this documentation.

### Optimize model performance with prompting

Here are some tips on how to get the best quality outputs:

1. Specify simple, well-defined tasks and provide explicit instructions for each step.
2. Claude sometimes assumes outcomes of its actions without explicitly checking their results. To prevent this you can prompt Claude with `After each step, take a screenshot and carefully evaluate if you have achieved the right outcome. Explicitly show your thinking: "I have evaluated step X..." If not correct, try again. Only when you confirm a step was executed correctly should you move on to the next one.`
3. Some UI elements (such as dropdowns and scrollbars) might be tricky for Claude to manipulate using mouse movements. If you experience this, try prompting the model to use keyboard shortcuts.
4. For repeatable tasks or UI interactions, include example screenshots and tool calls of successful outcomes in your prompt.
5. If you need the model to log in, provide it with the username and password in your prompt inside XML tags such as `<robot_credentials>`. Using computer use within applications that require login increases the risk of bad outcomes as a result of prompt injection. Review [Mitigate jailbreaks and prompt injections](/docs/en/test-and-evaluate/strengthen-guardrails/mitigate-jailbreaks) before providing the model with login credentials.
6. When constructing a user turn's `content` array, place the instruction text *before* the screenshot image. Providing the target description before the image is processed improves click accuracy.
7. When using `computer_20251124` with `enable_zoom: true` set, Claude zooms in on a region when asked about small text or specific UI elements that aren't legible at the screenshot's default resolution, such as file names in a sidebar, tab titles, status-bar text, line numbers, or button labels. If Claude isn't zooming when you expect, ask about a specific region or element rather than the screen as a whole.

<Tip>
  If you repeatedly encounter a clear set of issues or know in advance the tasks Claude will need to complete, use the system prompt to provide Claude with explicit tips or instructions on how to do the tasks successfully.
</Tip>

<Tip>
  For agents that span multiple sessions, run end-to-end verification at the start of each session, not only after implementation. Browser-based checks catch regressions from prior sessions that code-level review alone misses. See [Effective harnesses for long-running agents](https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents) for details.
</Tip>

### System prompts

When one of the Anthropic-schema tools is requested through the Claude API, a computer use-specific system prompt is generated. It's similar to the [tool use system prompt](/docs/en/agents-and-tools/tool-use/define-tools#tool-use-system-prompt) but starts with:

> You have access to a set of functions you can use to answer the user's question. This includes access to a sandboxed computing environment. You do NOT currently have the ability to inspect files or interact with external resources, except by invoking the below functions.

As with regular tool use, the user-provided `system` parameter is still respected and used in the construction of the combined system prompt.

### Available actions

The computer use tool supports these actions:

**Basic actions (all versions)**

* **screenshot:** Capture the current display
* **left\_click:** Click at coordinates `[x, y]`
* **type:** Type text string
* **key:** Press key or key combination (for example, "ctrl+s")
* **mouse\_move:** Move cursor to coordinates

**Enhanced actions (`computer_20250124` and later)** Available in `computer_20250124` and `computer_20251124`:

* **scroll:** Scroll in any direction with amount control
* **left\_click\_drag:** Click and drag between coordinates
* **right\_click**, **middle\_click:** Additional mouse buttons
* **double\_click**, **triple\_click:** Multiple clicks
* **left\_mouse\_down**, **left\_mouse\_up:** Fine-grained click control
* **hold\_key:** Hold down a key for a specified duration (in seconds)
* **wait:** Pause between actions

**Enhanced actions (`computer_20251124`)** Available in Claude Sonnet 5, Claude Opus 4.8, Claude Opus 4.7, Claude Opus 4.6, Claude Sonnet 4.6, and Claude Opus 4.5:

* All actions from `computer_20250124`
* **zoom:** View a specific region of the screen at full resolution. Requires `enable_zoom: true` in tool definition. Takes a `region` parameter with coordinates `[x1, y1, x2, y2]` defining top-left and bottom-right corners of the area to inspect.

<Accordion title="Example actions">
  Take a screenshot:

  ```json
  {
    "action": "screenshot"
  }
  ```

  Click at position:

  ```json
  {
    "action": "left_click",
    "coordinate": [500, 300]
  }
  ```

  Type text:

  ```json
  {
    "action": "type",
    "text": "Hello, world!"
  }
  ```

  Scroll down:

  ```json
  {
    "action": "scroll",
    "coordinate": [500, 400],
    "scroll_direction": "down",
    "scroll_amount": 3
  }
  ```

  Zoom to view region in detail (Claude Sonnet 5, Opus 4.8, Opus 4.7, Opus 4.6, Sonnet 4.6, and Opus 4.5):

  ```json
  {
    "action": "zoom",
    "region": [100, 200, 400, 350]
  }
  ```
</Accordion>

<Accordion title="Modifier keys with click and scroll actions">
  To hold modifier keys (such as Shift, Ctrl, or Alt) while performing click or scroll actions, use the `text` parameter on those actions. This is different from `hold_key`, which holds a key for a duration without performing other actions.

  Shift+click (for example, to select a range of items):

  ```json
  {
    "action": "left_click",
    "coordinate": [500, 300],
    "text": "shift"
  }
  ```

  Ctrl+click (for example, to multi-select on Windows/Linux):

  ```json
  {
    "action": "left_click",
    "coordinate": [500, 300],
    "text": "ctrl"
  }
  ```

  Cmd+click (for example, to multi-select on macOS):

  ```json
  {
    "action": "left_click",
    "coordinate": [500, 300],
    "text": "super"
  }
  ```

  Shift+scroll (for example, to scroll horizontally):

  ```json
  {
    "action": "scroll",
    "coordinate": [500, 400],
    "scroll_direction": "down",
    "scroll_amount": 3,
    "text": "shift"
  }
  ```

  The `text` parameter in click/scroll actions accepts modifier keys such as `shift`, `ctrl`, `alt`, and `super` (for the Command/Windows key).
</Accordion>

### Tool parameters

| Parameter           | Required | Description                                                                                                                         |
| ------------------- | -------- | ----------------------------------------------------------------------------------------------------------------------------------- |
| `type`              | Yes      | Tool version (`computer_20251124` or `computer_20250124`)                                                                           |
| `name`              | Yes      | Must be "computer"                                                                                                                  |
| `display_width_px`  | Yes      | Display width in pixels                                                                                                             |
| `display_height_px` | Yes      | Display height in pixels                                                                                                            |
| `display_number`    | No       | Display number for X11 environments                                                                                                 |
| `enable_zoom`       | No       | Enable zoom action (`computer_20251124` only). Set to `true` to allow Claude to zoom into specific screen regions. Default: `false` |

<Note>
  **Important:** Your application must explicitly run the computer use tool; Claude cannot run it directly. You are responsible for implementing the screenshot capture, mouse movements, keyboard inputs, and other actions based on Claude's requests.
</Note>

### Combining with extended thinking

For combining computer use with extended thinking, see [Extended thinking](/docs/en/build-with-claude/extended-thinking).

<Tip>
  For computer use specifically, internal benchmarking suggests these `effort` settings:

  * **Claude Opus 4.7:** use `high` as the default; use `low` for high-throughput or cost-sensitive workloads.
  * **Claude Sonnet 4.6 and Claude Opus 4.6:** use `medium` as the default (best accuracy-to-cost ratio). Avoid `max`, which adds token cost without improving accuracy on UI tasks. On these models, `low` uses *fewer* output tokens than disabling thinking entirely (fewer mistakes mean fewer retries), making it a strong option for cost-sensitive loops.
</Tip>

### Augmenting computer use with other tools

To add other tools alongside computer use, include them in the same `tools` array. The [Quick start](#quick-start) section shows this pattern with the [bash tool](/docs/en/agents-and-tools/tool-use/bash-tool) and [text editor tool](/docs/en/agents-and-tools/tool-use/text-editor-tool). You can add your own [custom tool definitions](/docs/en/agents-and-tools/tool-use/define-tools) the same way.

### Build a custom computer use environment

The [reference implementation](https://github.com/anthropics/anthropic-quickstarts/tree/main/computer-use-demo) is meant to help you get started with computer use. It includes all of the components needed to have Claude use a computer. However, you can build your own environment for computer use to suit your needs. You'll need:

* A virtualized or containerized environment suitable for computer use with Claude
* An implementation of at least one of the Anthropic-schema computer use tools
* An agent loop that interacts with the Claude API and runs the `tool_use` results using your tool implementations
* An API or UI that allows user input to start the agent loop

#### Implement the computer use tool

The computer use tool is implemented as a schema-less tool. When using this tool, you don't need to provide an input schema as with other tools; the schema is built into Claude's model and can't be modified.

<Steps>
  <Step title="Set up your computing environment">
    Create a virtual display or connect to an existing display that Claude will interact with. This typically involves setting up Xvfb (X Virtual Framebuffer) or similar technology.
  </Step>

  <Step title="Implement action handlers">
    Create functions to handle each action type that Claude might request:

    <CodeGroup>
      ```bash cURL
      # This is application-side helper code with no API request. See the SDK tabs
      # for the pattern.
      ```

      ```bash CLI
      # This is application-side helper code with no API request. See the SDK tabs
      # for the pattern.
      ```

      ```python Python
      def capture_screenshot():
          return "<screenshot data>"


      def click_at(x, y):
          return f"clicked at ({x}, {y})"


      def type_text(text):
          return f"typed: {text}"


      def handle_computer_action(action_type, params):
          if action_type == "screenshot":
              return capture_screenshot()
          elif action_type == "left_click":
              x, y = params["coordinate"]
              return click_at(x, y)
          elif action_type == "type":
              return type_text(params["text"])
          # Handle other actions as needed
          return f"unhandled action: {action_type}"
      ```

      ```typescript TypeScript
      function captureScreenshot(): string {
        return "<screenshot data>";
      }

      function clickAt(x: number, y: number): string {
        return `clicked at (${x}, ${y})`;
      }

      function typeText(text: string): string {
        return `typed: ${text}`;
      }

      function handleComputerAction(
        actionType: string,
        params: Record<string, unknown>,
      ): string {
        if (actionType === "screenshot") {
          return captureScreenshot();
        } else if (actionType === "left_click") {
          const [x, y] = params.coordinate as [number, number];
          return clickAt(x, y);
        } else if (actionType === "type") {
          return typeText(params.text as string);
        }
        // Handle other actions as needed
        return `unhandled action: ${actionType}`;
      }
      ```

      ```csharp C#
      string CaptureScreenshot() => "<screenshot data>";

      string ClickAt(int x, int y) => $"clicked at ({x}, {y})";

      string TypeText(string text) => $"typed: {text}";

      string HandleComputerAction(string actionType, IReadOnlyDictionary<string, JsonElement> input) =>
          actionType switch
          {
              "screenshot" => CaptureScreenshot(),
              "left_click" => ClickAt(
                  input["coordinate"][0].GetInt32(),
                  input["coordinate"][1].GetInt32()
              ),
              "type" => TypeText(input["text"].GetString()!),
              // Handle other actions as needed
              _ => $"unhandled action: {actionType}",
          };
      ```

      ```go Go
      func captureScreenshot() string {
      	return "<screenshot data>"
      }

      func clickAt(x, y int) string {
      	return fmt.Sprintf("clicked at (%d, %d)", x, y)
      }

      func typeText(text string) string {
      	return fmt.Sprintf("typed: %s", text)
      }

      func handleComputerAction(actionType string, params map[string]any) string {
      	switch actionType {
      	case "screenshot":
      		return captureScreenshot()
      	case "left_click":
      		coord := params["coordinate"].([]any)
      		return clickAt(int(coord[0].(float64)), int(coord[1].(float64)))
      	case "type":
      		return typeText(params["text"].(string))
      	// Handle other actions as needed
      	default:
      		return fmt.Sprintf("unhandled action: %s", actionType)
      	}
      }

      ```

      ```java Java
      String captureScreenshot() {
          return "<screenshot data>";
      }

      String clickAt(long x, long y) {
          return "clicked at (" + x + ", " + y + ")";
      }

      String typeText(String text) {
          return "typed: " + text;
      }

      String handleComputerAction(String actionType, Map<String, JsonValue> params) {
          return switch (actionType) {
              case "screenshot" -> captureScreenshot();
              case "left_click" -> {
                  List<JsonValue> coordinate = (List<JsonValue>) params.get("coordinate").asArray().get();
                  long x = ((Number) coordinate.get(0).asNumber().get()).longValue();
                  long y = ((Number) coordinate.get(1).asNumber().get()).longValue();
                  yield clickAt(x, y);
              }
              case "type" -> typeText(params.get("text").asStringOrThrow());
              // Handle other actions as needed
              default -> "unhandled action: " + actionType;
          };
      }
      ```

      ```php PHP
      function captureScreenshot(): string
      {
          return '<screenshot data>';
      }

      function clickAt(int $x, int $y): string
      {
          return "clicked at ({$x}, {$y})";
      }

      function typeText(string $text): string
      {
          return "typed: {$text}";
      }

      function handleComputerAction(string $actionType, array $params): string
      {
          return match ($actionType) {
              'screenshot' => captureScreenshot(),
              'left_click' => clickAt(...$params['coordinate']),
              'type' => typeText($params['text']),
              // Handle other actions as needed
              default => "unhandled action: {$actionType}",
          };
      }
      ```

      ```ruby Ruby
      def capture_screenshot
        "<screenshot data>"
      end

      def click_at(x, y)
        "clicked at (#{x}, #{y})"
      end

      def type_text(text)
        "typed: #{text}"
      end

      def handle_computer_action(action_type, params)
        case action_type
        when "screenshot"
          capture_screenshot
        when "left_click"
          x, y = params[:coordinate]
          click_at(x, y)
        when "type"
          type_text(params[:text])
        # Handle other actions as needed
        else
          "unhandled action: #{action_type}"
        end
      end
      ```
    </CodeGroup>
  </Step>

  <Step title="Process Claude's tool calls">
    Extract and run tool calls from Claude's responses:

    <CodeGroup>
      ```bash cURL
      # This is application-side helper code with no API request. See the SDK tabs
      # for the pattern.
      ```

      ```bash CLI
      # This is application-side helper code with no API request. See the SDK tabs
      # for the pattern.
      ```

      ```python Python
      def process_tool_calls(response):
          tool_results = []
          for block in response.content:
              if block.type == "tool_use":
                  action = block.input["action"]
                  result = handle_computer_action(action, block.input)
                  tool_results.append(
                      {
                          "type": "tool_result",
                          "tool_use_id": block.id,
                          "content": result,
                      }
                  )
          return tool_results
      ```

      ```typescript TypeScript
      function processToolCalls(
        response: Anthropic.Beta.BetaMessage,
      ): Anthropic.Beta.BetaToolResultBlockParam[] {
        const toolResults: Anthropic.Beta.BetaToolResultBlockParam[] = [];
        for (const block of response.content) {
          if (block.type === "tool_use") {
            const input = block.input as Record<string, unknown>;
            const action = input.action as string;
            const result = handleComputerAction(action, input);
            toolResults.push({
              type: "tool_result",
              tool_use_id: block.id,
              content: result,
            });
          }
        }
        return toolResults;
      }
      ```

      ```csharp C#
      List<BetaContentBlockParam> ProcessToolCalls(BetaMessage response)
      {
          List<BetaContentBlockParam> toolResults = [];
          foreach (var block in response.Content)
          {
              if (block.TryPickToolUse(out var toolUse))
              {
                  var action = toolUse.Input["action"].GetString()!;
                  var result = HandleComputerAction(action, toolUse.Input);
                  toolResults.Add(new BetaToolResultBlockParam(toolUse.ID) { Content = result });
              }
          }
          return toolResults;
      }
      ```

      ```go Go
      func processToolCalls(response *anthropic.BetaMessage) []anthropic.BetaContentBlockParamUnion {
      	var toolResults []anthropic.BetaContentBlockParamUnion
      	for _, block := range response.Content {
      		switch variant := block.AsAny().(type) {
      		case anthropic.BetaToolUseBlock:
      			input := variant.Input.(map[string]any)
      			action := input["action"].(string)
      			result := handleComputerAction(action, input)
      			toolResults = append(toolResults, anthropic.NewBetaToolResultBlock(variant.ID, result, false))
      		}
      	}
      	return toolResults
      }

      ```

      ```java Java
      List<BetaContentBlockParam> processToolCalls(BetaMessage response) {
          List<BetaContentBlockParam> toolResults = new ArrayList<>();
          for (BetaContentBlock block : response.content()) {
              if (block.isToolUse()) {
                  BetaToolUseBlock toolUse = block.asToolUse();
                  Map<String, JsonValue> input =
                          (Map<String, JsonValue>) toolUse._input().asObject().get();
                  String action = input.get("action").asStringOrThrow();
                  String result = handleComputerAction(action, input);
                  toolResults.add(BetaContentBlockParam.ofToolResult(
                          BetaToolResultBlockParam.builder()
                                  .toolUseId(toolUse.id())
                                  .content(result)
                                  .build()));
              }
          }
          return toolResults;
      }
      ```

      ```php PHP
      function processToolCalls(BetaMessage $response): array
      {
          $toolResults = [];
          foreach ($response->content as $block) {
              if ($block instanceof BetaToolUseBlock) {
                  $action = $block->input['action'];
                  $result = handleComputerAction($action, $block->input);
                  $toolResults[] = BetaToolResultBlockParam::with(
                      toolUseID: $block->id,
                      content: $result,
                  );
              }
          }
          return $toolResults;
      }
      ```

      ```ruby Ruby
      def process_tool_calls(response)
        tool_results = []
        response.content.each do |block|
          next unless block.type == :tool_use

          action = block.input[:action]
          result = handle_computer_action(action, block.input)
          tool_results << {
            type: "tool_result",
            tool_use_id: block.id,
            content: result
          }
        end
        tool_results
      end
      ```
    </CodeGroup>
  </Step>

  <Step title="Implement the agent loop">
    Create a loop that continues until Claude completes the task:

    <CodeGroup>
      ```bash cURL
      # The agent loop is a stateful, multi-turn pattern that doesn't translate to a
      # one-off shell command. See the SDK tabs for the implementation.
      ```

      ```bash CLI
      # The agent loop is a stateful, multi-turn pattern that doesn't translate to a
      # one-off shell command. See the SDK tabs for the implementation.
      ```

      ```python Python
      def sampling_loop(model, messages, max_iterations=10):
          """
          Run the computer-use agent loop until Claude stops requesting tools
          or the iteration limit is reached.
          """
          for _ in range(max_iterations):
              response = client.beta.messages.create(
                  model=model,
                  max_tokens=4096,
                  messages=messages,
                  tools=TOOLS,
                  betas=["computer-use-2025-11-24"],
              )

              # Add Claude's response to the conversation history
              messages.append({"role": "assistant", "content": response.content})

              # Run any tools Claude requested and collect results
              tool_results = process_tool_calls(response)
              if not tool_results:
                  return messages  # No more tool use; task complete

              # Send tool results back to Claude for the next iteration
              messages.append({"role": "user", "content": tool_results})

          return messages
      ```

      ```typescript TypeScript
      async function samplingLoop(
        model: string,
        messages: Anthropic.Beta.BetaMessageParam[],
        maxIterations = 10,
      ): Promise<Anthropic.Beta.BetaMessageParam[]> {
        // Run the computer-use agent loop until Claude stops requesting tools
        // or the iteration limit is reached.
        for (let i = 0; i < maxIterations; i++) {
          const response = await client.beta.messages.create({
            model,
            max_tokens: 4096,
            messages,
            tools,
            betas: ["computer-use-2025-11-24"],
          });

          // Add Claude's response to the conversation history
          messages.push({ role: "assistant", content: response.content });

          // Run any tools Claude requested and collect results
          const toolResults = processToolCalls(response);
          if (toolResults.length === 0) {
            return messages; // No more tool use; task complete
          }

          // Send tool results back to Claude for the next iteration
          messages.push({ role: "user", content: toolResults });
        }

        return messages;
      }
      ```

      ```csharp C#
      async Task<List<BetaMessageParam>> SamplingLoop(
          Model model,
          List<BetaMessageParam> messages,
          int maxIterations = 10
      )
      {
          // Run the computer-use agent loop until Claude stops requesting tools
          // or the iteration limit is reached.
          for (var i = 0; i < maxIterations; i++)
          {
              var response = await client.Beta.Messages.Create(
                  new MessageCreateParams
                  {
                      Model = model,
                      MaxTokens = 4096,
                      Messages = messages,
                      Tools = tools,
                      Betas = ["computer-use-2025-11-24"],
                  }
              );

              // Add Claude's response to the conversation history
              messages.Add(
                  new()
                  {
                      Role = Role.Assistant,
                      Content = response
                          .Content.Select(block => new BetaContentBlockParam(block.Json))
                          .ToList(),
                  }
              );

              // Run any tools Claude requested and collect results
              var toolResults = ProcessToolCalls(response);
              if (toolResults.Count == 0)
              {
                  return messages; // No more tool use; task complete
              }

              // Send tool results back to Claude for the next iteration
              messages.Add(new() { Role = Role.User, Content = toolResults });
          }

          return messages;
      }
      ```

      ```go Go
      // samplingLoop runs the computer-use agent loop until Claude stops
      // requesting tools or the iteration limit is reached.
      func samplingLoop(ctx context.Context, model anthropic.Model, messages []anthropic.BetaMessageParam, maxIterations int) ([]anthropic.BetaMessageParam, error) {
      	for range maxIterations {
      		response, err := client.Beta.Messages.New(ctx, anthropic.BetaMessageNewParams{
      			Model:     model,
      			MaxTokens: 4096,
      			Messages:  messages,
      			Tools:     tools,
      			Betas:     []anthropic.AnthropicBeta{"computer-use-2025-11-24"},
      		})
      		if err != nil {
      			return nil, err
      		}

      		// Add Claude's response to the conversation history
      		messages = append(messages, response.ToParam())

      		// Run any tools Claude requested and collect results
      		toolResults := processToolCalls(response)
      		if len(toolResults) == 0 {
      			return messages, nil // No more tool use; task complete
      		}

      		// Send tool results back to Claude for the next iteration
      		messages = append(messages, anthropic.BetaMessageParam{
      			Role:    anthropic.BetaMessageParamRoleUser,
      			Content: toolResults,
      		})
      	}
      	return messages, nil
      }

      ```

      ```java Java
      /**
       * Run the computer-use agent loop until Claude stops requesting tools
       * or the iteration limit is reached.
       */
      List<BetaMessageParam> samplingLoop(Model model, List<BetaMessageParam> messages, int maxIterations) {
          for (int i = 0; i < maxIterations; i++) {
              BetaMessage response = client.beta().messages().create(MessageCreateParams.builder()
                      .model(model)
                      .maxTokens(4096)
                      .messages(messages)
                      .addTool(COMPUTER_TOOL)
                      .addBeta("computer-use-2025-11-24")
                      .build());

              // Add Claude's response to the conversation history
              messages.add(BetaMessageParam.builder()
                      .role(BetaMessageParam.Role.ASSISTANT)
                      .contentOfBetaContentBlockParams(
                              response.content().stream().map(BetaContentBlock::toParam).toList())
                      .build());

              // Run any tools Claude requested and collect results
              List<BetaContentBlockParam> toolResults = processToolCalls(response);
              if (toolResults.isEmpty()) {
                  return messages; // No more tool use; task complete
              }

              // Send tool results back to Claude for the next iteration
              messages.add(BetaMessageParam.builder()
                      .role(BetaMessageParam.Role.USER)
                      .contentOfBetaContentBlockParams(toolResults)
                      .build());
          }
          return messages;
      }
      ```

      ```php PHP
      /**
       * Run the computer-use agent loop until Claude stops requesting tools
       * or the iteration limit is reached.
       */
      function samplingLoop(string $model, array $messages, int $maxIterations = 10): array
      {
          global $client, $tools;

          for ($i = 0; $i < $maxIterations; $i++) {
              $response = $client->beta->messages->create(
                  model: $model,
                  maxTokens: 4096,
                  messages: $messages,
                  tools: $tools,
                  betas: ['computer-use-2025-11-24'],
              );

              // Add Claude's response to the conversation history
              $messages[] = BetaMessageParam::with(role: Role::ASSISTANT, content: $response->content);

              // Run any tools Claude requested and collect results
              $toolResults = processToolCalls($response);
              if ($toolResults === []) {
                  return $messages; // No more tool use; task complete
              }

              // Send tool results back to Claude for the next iteration
              $messages[] = BetaMessageParam::with(role: Role::USER, content: $toolResults);
          }

          return $messages;
      }
      ```

      ```ruby Ruby
      # Run the computer-use agent loop until Claude stops requesting tools
      # or the iteration limit is reached.
      def sampling_loop(model, messages, max_iterations: 10)
        max_iterations.times do
          response = CLIENT.beta.messages.create(
            model: model,
            max_tokens: 4096,
            messages: messages,
            tools: TOOLS,
            betas: ["computer-use-2025-11-24"]
          )

          # Add Claude's response to the conversation history
          messages << {role: "assistant", content: response.content}

          # Run any tools Claude requested and collect results
          tool_results = process_tool_calls(response)
          return messages if tool_results.empty? # No more tool use; task complete

          # Send tool results back to Claude for the next iteration
          messages << {role: "user", content: tool_results}
        end

        messages
      end
      ```
    </CodeGroup>
  </Step>
</Steps>

#### Handle errors

When implementing the computer use tool, various errors might occur. Here's how to handle them:

<AccordionGroup>
  <Accordion title="Screenshot capture failure">
    If screenshot capture fails, return an appropriate error message:

    ```json
    {
      "role": "user",
      "content": [
        {
          "type": "tool_result",
          "tool_use_id": "toolu_01A09q90qw90lq917835lq9",
          "content": "Error: Failed to capture screenshot. Display may be locked or unavailable.",
          "is_error": true
        }
      ]
    }
    ```
  </Accordion>

  <Accordion title="Invalid coordinates">
    If Claude provides coordinates outside the display bounds:

    ```json
    {
      "role": "user",
      "content": [
        {
          "type": "tool_result",
          "tool_use_id": "toolu_01A09q90qw90lq917835lq9",
          "content": "Error: Coordinates (1200, 900) are outside display bounds (1024x768).",
          "is_error": true
        }
      ]
    }
    ```
  </Accordion>

  <Accordion title="Action execution failure">
    If an action fails to run:

    ```json
    {
      "role": "user",
      "content": [
        {
          "type": "tool_result",
          "tool_use_id": "toolu_01A09q90qw90lq917835lq9",
          "content": "Error: Failed to perform click action. The application may be unresponsive.",
          "is_error": true
        }
      ]
    }
    ```
  </Accordion>
</AccordionGroup>

#### Size screenshots to fit image limits

Screenshots sent to the computer tool should fit within Claude's image size limits (see [image size limits](/docs/en/build-with-claude/vision#evaluate-image-size)). The API downscales oversized images before Claude sees them, and Claude returns coordinates for the image it sees, so relying on the server-side downscale leaves you without the scale factor you need to map those coordinates back to your screen. Only images over the API's separate [request limits](/docs/en/build-with-claude/vision#request-limits) (for example, more than 8,000 px on a side) are rejected with a validation error rather than downscaled.

<Note>
  Limits vary by model. Claude Sonnet 5, Claude Opus 4.8, and Claude Opus 4.7 accept up to 2576 pixels on the long edge; earlier models accept up to 1568 pixels on the long edge and approximately 1.15 megapixels total. The following example uses the earlier-model 1568 px / 1.15 MP limits; substitute your model's limit.
</Note>

If your screen is larger than the limit, resize the screenshot before sending it, set `display_width_px`/`display_height_px` to the resized dimensions, and scale Claude's returned coordinates back to the original screen space:

<CodeGroup>
  ```bash cURL
  # Coordinate scaling and screenshot resizing happen in your application code, not
  # in the API request. See the SDK tabs for the helper pattern.
  ```

  ```bash CLI
  # Coordinate scaling and screenshot resizing happen in your application code, not
  # in the API request. See the SDK tabs for the helper pattern.
  ```

  ```python Python
  import math


  def get_scale_factor(width, height):
      """Calculate scale factor to meet API constraints."""
      long_edge = max(width, height)
      total_pixels = width * height

      long_edge_scale = 1568 / long_edge
      total_pixels_scale = math.sqrt(1_150_000 / total_pixels)

      return min(1.0, long_edge_scale, total_pixels_scale)


  # When capturing screenshot
  scale = get_scale_factor(screen_width, screen_height)
  scaled_width = int(screen_width * scale)
  scaled_height = int(screen_height * scale)

  # Resize image to scaled dimensions before sending to Claude
  screenshot = capture_and_resize(scaled_width, scaled_height)


  # When handling Claude's coordinates, scale them back up
  def execute_click(x, y):
      screen_x = x / scale
      screen_y = y / scale
      perform_click(screen_x, screen_y)
  ```

  ```typescript TypeScript
  const MAX_LONG_EDGE = 1568;
  const MAX_PIXELS = 1_150_000;

  function getScaleFactor(width: number, height: number): number {
    const longEdge = Math.max(width, height);
    const totalPixels = width * height;

    const longEdgeScale = MAX_LONG_EDGE / longEdge;
    const totalPixelsScale = Math.sqrt(MAX_PIXELS / totalPixels);

    return Math.min(1.0, longEdgeScale, totalPixelsScale);
  }

  // When capturing screenshot
  const scale = getScaleFactor(screenWidth, screenHeight);
  const scaledWidth = Math.floor(screenWidth * scale);
  const scaledHeight = Math.floor(screenHeight * scale);

  // Resize image to scaled dimensions before sending to Claude
  const screenshot = captureAndResize(scaledWidth, scaledHeight);

  // When handling Claude's coordinates, scale them back up
  function executeClick(x: number, y: number): void {
    const screenX = x / scale;
    const screenY = y / scale;
    performClick(screenX, screenY);
  }
  ```

  ```csharp C#
  double GetScaleFactor(int width, int height)
  {
      // Calculate scale factor to meet API constraints.
      int longEdge = Math.Max(width, height);
      int totalPixels = width * height;

      double longEdgeScale = 1568.0 / longEdge;
      double totalPixelsScale = Math.Sqrt(1_150_000.0 / totalPixels);

      return Math.Min(1.0, Math.Min(longEdgeScale, totalPixelsScale));
  }

  // When capturing screenshot
  double scale = GetScaleFactor(screenWidth, screenHeight);
  int scaledWidth = (int)(screenWidth * scale);
  int scaledHeight = (int)(screenHeight * scale);

  // Resize image to scaled dimensions before sending to Claude
  var screenshot = CaptureAndResize(scaledWidth, scaledHeight);

  // When handling Claude's coordinates, scale them back up
  void ExecuteClick(int x, int y)
  {
      double screenX = x / scale;
      double screenY = y / scale;
      PerformClick(screenX, screenY);
  }
  ```

  ```go Go
  func getScaleFactor(width, height int) float64 {
  	longest := float64(max(width, height))
  	area := float64(width * height)
  	return min(1.0, 1568/longest, math.Sqrt(1_150_000/area))
  }

  // ...
  	// When capturing screenshot
  	scale := getScaleFactor(screenWidth, screenHeight)
  	scaledWidth := int(float64(screenWidth) * scale)
  	scaledHeight := int(float64(screenHeight) * scale)

  	// Resize image to scaled dimensions before sending to Claude
  	screenshot := captureAndResize(scaledWidth, scaledHeight)

  	// When handling Claude's coordinates, scale them back up
  	executeClick := func(x, y int) {
  		performClick(float64(x)/scale, float64(y)/scale)
  	}
  ```

  ```java Java
  static double getScaleFactor(int width, int height) {
      return Math.min(
          1.0,
          Math.min(
              1568.0 / Math.max(width, height),
              Math.sqrt(1_150_000.0 / (width * height))
          )
      );
  }

  void main() {
  // ...
      // When capturing screenshot
      double scale = getScaleFactor(screenWidth, screenHeight);
      int scaledWidth = (int)(screenWidth * scale);
      int scaledHeight = (int)(screenHeight * scale);

      // Resize image to scaled dimensions before sending to Claude
      var screenshot = captureAndResize(scaledWidth, scaledHeight);

      // When handling Claude's coordinates, scale them back up
      BiConsumer<Integer, Integer> executeClick =
          (x, y) -> performClick(x / scale, y / scale);
  // ...
  }
  ```

  ```php PHP
  function getScaleFactor(int $width, int $height): float
  {
      return min(
          1.0,
          1568 / max($width, $height),
          sqrt(1_150_000 / ($width * $height)),
      );
  }
  // ...
  // When capturing screenshot
  $scale = getScaleFactor($screenWidth, $screenHeight);
  $scaledWidth = (int)($screenWidth * $scale);
  $scaledHeight = (int)($screenHeight * $scale);

  // Resize image to scaled dimensions before sending to Claude
  $screenshot = captureAndResize($scaledWidth, $scaledHeight);

  // When handling Claude's coordinates, scale them back up
  $executeClick = fn(int $x, int $y) => performClick($x / $scale, $y / $scale);
  ```

  ```ruby Ruby
  def get_scale_factor(width, height)
    [1.0, 1568.0 / [width, height].max, Math.sqrt(1_150_000.0 / (width * height))].min
  end
  # ...
  # When capturing screenshot
  scale = get_scale_factor(screen_width, screen_height)
  scaled_width = (screen_width * scale).to_i
  scaled_height = (screen_height * scale).to_i

  # Resize image to scaled dimensions before sending to Claude
  screenshot = capture_and_resize(scaled_width, scaled_height)

  # When handling Claude's coordinates, scale them back up
  execute_click = ->(x, y) { perform_click(x / scale, y / scale) }
  ```
</CodeGroup>

<Note>
  **macOS Retina displays** capture screenshots at a device pixel ratio of 2, so the image is twice the resolution of the logical screen coordinates. Either downscale the screenshot by 2x before sending, or halve the coordinates Claude returns before issuing the click.
</Note>

#### Diagnose click issues

If clicks miss their targets, the cause is usually one of the following:

| Symptom                                           | Likely cause                                                                                  | Try                                                                                                               |
| ------------------------------------------------- | --------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------- |
| Clicks consistently offset in one direction       | `display_width_px`/`display_height_px` don't match the image dimensions actually sent         | Ensure display dimensions exactly match the screenshot you send                                                   |
| Clicks land in the right area but miss the target | Target is very small, detail was lost downscaling a 4K+ source, or aspect ratio was distorted | Set `enable_zoom: true`; capture at lower DPI or crop to the relevant region; preserve aspect ratio when resizing |
| Claude clicks the wrong element entirely          | Ambiguous instruction, or visually similar elements nearby                                    | Use positional prompts ("the blue Submit button in the bottom-right"); break the interaction into smaller steps   |
| Accuracy is consistently poor                     | Resolution too low                                                                            | Try 1280x720 as a baseline                                                                                        |

<Tip>
  **Model choice affects click precision.** Claude Sonnet 4.6 is more mechanically precise at clicking than Claude Opus 4.6 and is more robust when screenshots require heavy downscaling. Claude Opus 4.7 narrows that gap: its click precision is roughly comparable to Sonnet 4.6, and its higher resolution limit means less downscaling is needed.
</Tip>

#### Follow implementation best practices

<AccordionGroup>
  <Accordion title="Use appropriate display resolution">
    Set display dimensions that match your use case while staying within recommended limits:

    * For general desktop tasks: 1024x768 or 1280x720
    * For web applications: 1280x800 or 1366x768
    * Avoid resolutions above 1920x1080 to prevent performance issues
  </Accordion>

  <Accordion title="Implement proper screenshot handling">
    When returning screenshots to Claude:

    * Encode screenshots as base64 PNG or JPEG
    * Consider compressing large screenshots to improve performance
    * Include relevant metadata such as timestamp or display state
    * If using higher resolutions, ensure coordinates are accurately scaled

    A screenshot goes back as an image content block inside the `tool_result` content array (see [Handle tool calls](/docs/en/agents-and-tools/tool-use/handle-tool-calls)):

    ```json
    {
      "role": "user",
      "content": [
        {
          "type": "tool_result",
          "tool_use_id": "toolu_01A09q90qw90lq917835lq9",
          "content": [
            {
              "type": "image",
              "source": {
                "type": "base64",
                "media_type": "image/png",
                "data": "iVBORw0KGgo..."
              }
            }
          ]
        }
      ]
    }
    ```
  </Accordion>

  <Accordion title="Manage screenshot history for prompt caching">
    Long agent loops accumulate screenshots quickly (roughly 1,000–1,800 input tokens each). To keep [Prompt caching](/docs/en/build-with-claude/prompt-caching) effective while bounding context:

    * Place one `cache_control` breakpoint after the system prompt and tool definitions, and up to three more on the most recent `tool_result` blocks, advancing them each turn.
    * Prune old screenshots in *batches*, not one each turn. Dropping a screenshot every turn changes the prefix every turn and invalidates the cache. A reasonable default is to keep the last three screenshots and prune every 25 turns, so the prefix stays byte-identical between prune events.
  </Accordion>

  <Accordion title="Add action delays">
    Some applications need time to respond to actions:

    <CodeGroup>
      ```bash cURL
      # This is application-side helper code with no API request. See the SDK tabs for
      # the pattern.
      ```

      ```bash CLI
      # This is application-side helper code with no API request. See the SDK tabs for
      # the pattern.
      ```

      ```python Python
      def click_and_wait(x, y, wait_time=0.5):
          click_at(x, y)
          time.sleep(wait_time)  # Allow UI to update
      ```

      ```typescript TypeScript
      async function clickAndWait(x: number, y: number, waitMs = 500): Promise<void> {
        clickAt(x, y);
        await setTimeout(waitMs); // Allow UI to update
      }
      ```

      ```csharp C#
      static void ClickAndWait(int x, int y, double waitSeconds = 0.5)
      {
          ClickAt(x, y);
          Thread.Sleep(TimeSpan.FromSeconds(waitSeconds));  // Allow UI to update
      }
      ```

      ```go Go
      func clickAndWaitFor(x, y int, wait time.Duration) {
      	clickAt(x, y)
      	time.Sleep(wait) // Allow UI to update
      }

      func clickAndWait(x, y int) {
      	clickAndWaitFor(x, y, 500*time.Millisecond)
      }
      ```

      ```java Java
      void clickAndWait(int x, int y) throws InterruptedException {
          clickAndWait(x, y, 500);
      }

      void clickAndWait(int x, int y, long waitTimeMillis) throws InterruptedException {
          clickAt(x, y);
          Thread.sleep(waitTimeMillis);  // Allow UI to update
      }
      ```

      ```php PHP
      function clickAndWait(int $x, int $y, float $waitSeconds = 0.5): void
      {
          clickAt($x, $y);
          usleep((int) ($waitSeconds * 1_000_000));  // Allow UI to update
      }
      ```

      ```ruby Ruby
      def click_and_wait(x, y, wait_time: 0.5)
        click_at(x, y)
        sleep(wait_time) # Allow UI to update
      end
      ```
    </CodeGroup>
  </Accordion>

  <Accordion title="Validate actions before running them">
    Check that requested actions are safe and valid:

    <CodeGroup>
      ```bash cURL
      # This is application-side helper code with no API request. See the SDK tabs for
      # the pattern.
      ```

      ```bash CLI
      # This is application-side helper code with no API request. See the SDK tabs for
      # the pattern.
      ```

      ```python Python
      def validate_action(action_type, params):
          if action_type == "left_click":
              x, y = params.get("coordinate", (0, 0))
              if not (0 <= x < display_width and 0 <= y < display_height):
                  return False, "Coordinates out of bounds"
          return True, None
      ```

      ```typescript TypeScript
      interface ActionParams {
        coordinate?: [number, number];
      }

      function validateAction(actionType: string, params: ActionParams): [boolean, string | null] {
        if (actionType === "left_click") {
          const [x, y] = params.coordinate ?? [0, 0];
          if (!(x >= 0 && x < displayWidth && y >= 0 && y < displayHeight)) {
            return [false, "Coordinates out of bounds"];
          }
        }
        return [true, null];
      }
      ```

      ```csharp C#
      const int DisplayWidth = 1024;
      const int DisplayHeight = 768;
      // ...
      static (bool IsValid, string? Error) ValidateAction(string actionType, IReadOnlyDictionary<string, JsonElement> parameters)
      {
          if (actionType == "left_click")
          {
              int x = parameters["coordinate"][0].GetInt32();
              int y = parameters["coordinate"][1].GetInt32();
              if (x is < 0 or >= DisplayWidth || y is < 0 or >= DisplayHeight)
              {
                  return (false, "Coordinates out of bounds");
              }
          }
          return (true, null);
      }
      ```

      ```go Go
      const (
      	displayWidth  = 1024
      	displayHeight = 768
      )

      func validateAction(actionType string, params map[string]any) (bool, string) {
      	if actionType == "left_click" {
      		coord, ok := params["coordinate"].([]any)
      		if !ok || len(coord) != 2 {
      			return false, "Invalid coordinate"
      		}
      		x, y := int(coord[0].(float64)), int(coord[1].(float64))
      		if !(0 <= x && x < displayWidth && 0 <= y && y < displayHeight) {
      			return false, "Coordinates out of bounds"
      		}
      	}
      	return true, ""
      }
      ```

      ```java Java
      static final int DISPLAY_WIDTH = 1024;
      static final int DISPLAY_HEIGHT = 768;

      record Validation(boolean valid, String error) {}

      Validation validateAction(String actionType, Map<String, JsonValue> params) {
          if (actionType.equals("left_click")) {
              List<JsonValue> coord = (List<JsonValue>) params.get("coordinate").asArray().get();
              long x = ((Number) coord.get(0).asNumber().get()).longValue();
              long y = ((Number) coord.get(1).asNumber().get()).longValue();
              if (!(0 <= x && x < DISPLAY_WIDTH && 0 <= y && y < DISPLAY_HEIGHT)) {
                  return new Validation(false, "Coordinates out of bounds");
              }
          }
          return new Validation(true, null);
      }
      ```

      ```php PHP
      const DISPLAY_WIDTH = 1024;
      const DISPLAY_HEIGHT = 768;

      /** @return array{bool, ?string} */
      function validateAction(string $actionType, array $params): array
      {
          if ($actionType === 'left_click') {
              [$x, $y] = $params['coordinate'] ?? [0, 0];
              if (!(0 <= $x && $x < DISPLAY_WIDTH && 0 <= $y && $y < DISPLAY_HEIGHT)) {
                  return [false, 'Coordinates out of bounds'];
              }
          }
          return [true, null];
      }
      ```

      ```ruby Ruby
      DISPLAY_WIDTH = 1024
      DISPLAY_HEIGHT = 768

      def validate_action(action_type, params)
        if action_type == "left_click"
          x, y = params.fetch(:coordinate, [0, 0])
          unless (0...DISPLAY_WIDTH).cover?(x) && (0...DISPLAY_HEIGHT).cover?(y)
            return [false, "Coordinates out of bounds"]
          end
        end
        [true, nil]
      end
      ```
    </CodeGroup>
  </Accordion>

  <Accordion title="Log actions for debugging">
    Keep a log of all actions for troubleshooting:

    <CodeGroup>
      ```bash cURL
      # This is application-side helper code with no API request. See the SDK tabs for
      # the pattern.
      ```

      ```bash CLI
      # This is application-side helper code with no API request. See the SDK tabs for
      # the pattern.
      ```

      ```python Python
      import logging


      def log_action(action_type, params, result):
          logging.info(f"Action: {action_type}, Params: {params}, Result: {result}")
      ```

      ```typescript TypeScript
      function logAction(actionType: string, params: unknown, result: unknown): void {
        console.error(
          `Action: ${actionType}, Params: ${JSON.stringify(params)}, Result: ${JSON.stringify(
            result
          )}`
        );
      }
      ```

      ```csharp C#
      static void LogAction(string actionType, object? parameters, object? result)
      {
          Console.Error.WriteLine($"Action: {actionType}, Params: {parameters}, Result: {result}");
      }
      ```

      ```go Go
      func logAction(actionType string, params map[string]any, result any) {
      	log.Printf("Action: %s, Params: %v, Result: %v", actionType, params, result)
      }
      ```

      ```java Java
      import static java.lang.System.Logger.Level.INFO;

      static final System.Logger LOGGER = System.getLogger("computer-use");

      void logAction(String actionType, Object params, Object result) {
          LOGGER.log(INFO, "Action: {0}, Params: {1}, Result: {2}", actionType, params, result);
      }
      ```

      ```php PHP
      function logAction(string $actionType, array $params, mixed $result): void
      {
          error_log(sprintf(
              'Action: %s, Params: %s, Result: %s',
              $actionType,
              json_encode($params),
              json_encode($result),
          ));
      }
      ```

      ```ruby Ruby
      require "logger"

      LOGGER = Logger.new($stderr)

      def log_action(action_type, params, result)
        LOGGER.info("Action: #{action_type}, Params: #{params}, Result: #{result}")
      end
      ```
    </CodeGroup>
  </Accordion>
</AccordionGroup>

***

## Understand computer use limitations

Computer use is in beta. Keep the following limitations in mind:

1. **Latency:** The current computer use latency for human-AI interactions might be too slow compared to regular human-directed computer actions. Focus on use cases where speed isn't critical (for example, background information gathering, automated software testing) in trusted environments.

2. **Computer vision accuracy and reliability:** Claude might make mistakes or hallucinate when outputting specific coordinates while generating actions. Extended thinking can help you understand the model's reasoning and identify potential issues.

3. **Tool selection accuracy and reliability:** Claude might make mistakes or hallucinate when selecting tools while generating actions or take unexpected actions to solve problems. Additionally, reliability might be lower when interacting with niche applications or multiple applications at once. Prompt the model carefully when requesting complex tasks.

4. **Scrolling reliability:** The scroll action supports direction control (up, down, left, right) and a specified amount. In applications where scrolling doesn't take effect, keyboard alternatives such as Page Down can help.

5. **Spreadsheet interaction:** Use the fine-grained mouse control actions (`left_mouse_down`, `left_mouse_up`) and modifier-key combinations to select individual cells. Complex spreadsheet operations might still require multiple attempts.

6. **Account creation and content generation on social and communications platforms:** While Claude will visit websites, Claude's ability to create accounts or generate and share content or otherwise engage in human impersonation across social media websites and platforms is limited. This capability might be updated in the future.

7. **Vulnerabilities:** Vulnerabilities such as jailbreaking or prompt injection might persist across frontier AI systems, including the beta computer use API. In some circumstances, Claude will follow commands found in content, sometimes even when they conflict with your instructions. For example, instructions on webpages or contained in images might override your instructions or cause Claude to make mistakes. Consider the following:

   * Limiting computer use to trusted environments such as virtual machines or containers with minimal privileges
   * Avoiding giving computer use access to sensitive accounts or data without strict oversight
   * Informing end users of relevant risks and obtaining their consent before enabling or requesting permissions necessary for computer use features in your applications

8. **Inappropriate or illegal actions:** Under Anthropic's Terms of Service, you must not employ computer use to violate any laws or the Acceptable Use Policy.

Always carefully review and verify Claude's computer use actions and logs. Do not use Claude for tasks requiring perfect precision or sensitive user information without human oversight.

## Data retention

Computer use is a client-side tool. All screenshots, mouse actions, keyboard inputs, and any files involved in a session are captured and stored in your environment, not by Anthropic. Anthropic processes the screenshot images and action requests in real time as part of the API call. Retention for those API requests is governed by [API and data retention](/docs/en/manage-claude/api-and-data-retention).

Because your application controls where and how computer use data is stored, computer use is ZDR eligible. For ZDR eligibility across all features, see [API and data retention](/docs/en/manage-claude/api-and-data-retention).

## Pricing

Computer use follows the standard [tool use pricing](/docs/en/agents-and-tools/tool-use/overview#pricing). When using the computer use tool:

**System prompt overhead:** The computer use beta adds 466–499 tokens to the system prompt

**Computer use tool token usage:**

| Model             | Input tokens per tool definition |
| ----------------- | -------------------------------- |
| Claude 4.x models | 735 tokens                       |

**Additional token consumption:**

* Screenshot images (see [Vision pricing](/docs/en/build-with-claude/vision))
* Tool execution results returned to Claude

<Note>
  If you're also using bash or text editor tools alongside computer use, those tools have their own token costs as documented in their respective pages.
</Note>

## Next steps

<CardGroup cols={2}>
  <Card title="Troubleshooting tool use" icon="wrench" href="/docs/en/agents-and-tools/tool-use/troubleshooting-tool-use">
    Fix the most common tool-use errors with symptom-to-fix diagnostic tables.
  </Card>

  <Card title="Reference implementation" icon="github-logo" href="https://github.com/anthropics/anthropic-quickstarts/tree/main/computer-use-demo">
    Get started with the complete Docker-based implementation
  </Card>

  <Card title="Tool use with Claude" icon="tool" href="/docs/en/agents-and-tools/tool-use/overview">
    Connect Claude to external tools and APIs. See where tools execute, when Claude calls them, and which tool fits your task.
  </Card>

  <Card title="Best practices in detail" icon="book" href="https://claude.com/blog/best-practices-for-computer-and-browser-use-with-claude">
    Benchmarked recommendations for resolution, thinking effort, and context management
  </Card>
</CardGroup>
