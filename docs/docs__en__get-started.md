# Get started with Claude

Make your first API call to Claude and build a simple web search assistant.

---

## Prerequisites

- An Anthropic [Console account](/)
- An [API key](/settings/keys)

## Call the API

<Tabs>
  <Tab title="cURL">
    <Steps>
      <Step title="Set your API key">
        Get your API key from the [Claude Console](/settings/keys) and set it as an environment variable:

        ```bash
        export ANTHROPIC_API_KEY='your-api-key-here'
        ```

        To persist the key across shell sessions, add the line to your shell profile (such as `~/.zshrc` or `~/.bashrc`).
      </Step>

      <Step title="Make your first API call">
        Run this command to create a simple web search assistant:

        ```bash cURL
        curl https://api.anthropic.com/v1/messages \
          -H "Content-Type: application/json" \
          -H "x-api-key: $ANTHROPIC_API_KEY" \
          -H "anthropic-version: 2023-06-01" \
          -d '{
            "model": "claude-opus-4-7",
            "max_tokens": 1000,
            "messages": [
              {
                "role": "user",
                "content": "What should I search for to find the latest developments in renewable energy?"
              }
            ]
          }'
        ```

        **Example output:**
        ```json Output
        {
          "id": "msg_01HCDu5LRGeP2o7s2xGmxyx8",
          "type": "message",
          "role": "assistant",
          "content": [
            {
              "type": "text",
              "text": "Here are some effective search strategies to find the latest renewable energy developments:\n\n## Search Terms to Use:\n- \"renewable energy news 2024\"\n- \"clean energy breakthrough\"\n- \"solar/wind/battery technology advances\"\n- \"green energy innovations\"\n- \"climate tech developments\"\n- \"energy storage solutions\"\n\n## Best Sources to Check:\n\n**News & Industry Sites:**\n- Renewable Energy World\n- GreenTech Media (now Wood Mackenzie)\n- Energy Storage News\n- CleanTechnica\n- PV Magazine (for solar)\n- WindPower Engineering & Development..."
            }
          ],
          "model": "claude-opus-4-7",
          "stop_reason": "end_turn",
          "usage": {
            "input_tokens": 21,
            "output_tokens": 305
          }
        }
        ```
      </Step>
    </Steps>
  </Tab>

  <Tab title="CLI">
    <Steps>
      <Step title="Set your API key">
        Get your API key from the [Claude Console](/settings/keys) and set it as an environment variable:

        ```bash
        export ANTHROPIC_API_KEY='your-api-key-here'
        ```

        To persist the key across shell sessions, add the line to your shell profile (such as `~/.zshrc` or `~/.bashrc`).
      </Step>

      <Step title="Install the CLI">
        Install the Anthropic CLI with Homebrew:

        ```bash
        brew install anthropics/tap/ant
        ```

        For other installation methods, see [Installation](/docs/en/api/sdks/cli#installation) in the CLI reference.
      </Step>

      <Step title="Make your first API call">
        Run this command to create a simple web search assistant:

        ```bash
        ant messages create \
          --model claude-opus-4-7 \
          --max-tokens 1000 \
          --message '{
            role: user,
            content: "What should I search for to find the latest developments in renewable energy?"
          }'
        ```

        **Example output:**
        ```json Output
        {
          "id": "msg_01HCDu5LRGeP2o7s2xGmxyx8",
          "type": "message",
          "role": "assistant",
          "content": [
            {
              "type": "text",
              "text": "Here are some effective search strategies to find the latest renewable energy developments:\n\n## Search Terms to Use:\n- \"renewable energy news 2024\"\n- \"clean energy breakthrough\"\n- \"solar/wind/battery technology advances\"\n- \"green energy innovations\"\n- \"climate tech developments\"\n- \"energy storage solutions\"\n\n## Best Sources to Check:\n\n**News & Industry Sites:**\n- Renewable Energy World\n- GreenTech Media (now Wood Mackenzie)\n- Energy Storage News\n- CleanTechnica\n- PV Magazine (for solar)\n- WindPower Engineering & Development..."
            }
          ],
          "model": "claude-opus-4-7",
          "stop_reason": "end_turn",
          "usage": {
            "input_tokens": 21,
            "output_tokens": 305
          }
        }
        ```
      </Step>
    </Steps>
  </Tab>

  <Tab title="Python">
    <Steps>
      <Step title="Set your API key">
        Get your API key from the [Claude Console](/settings/keys) and set it as an environment variable:

        ```bash
        export ANTHROPIC_API_KEY='your-api-key-here'
        ```

        To persist the key across shell sessions, add the line to your shell profile (such as `~/.zshrc` or `~/.bashrc`).
      </Step>

      <Step title="Install the SDK">
        Install the Anthropic Python SDK:

        ```bash
        pip install anthropic
        ```
      </Step>

      <Step title="Create your code">
        Save this as `quickstart.py`:

        ```python
        import anthropic

        client = anthropic.Anthropic()

        message = client.messages.create(
            model="claude-opus-4-7",
            max_tokens=1000,
            messages=[
                {
                    "role": "user",
                    "content": "What should I search for to find the latest developments in renewable energy?",
                }
            ],
        )
        print(message.content)
        ```
      </Step>

      <Step title="Run your code">
        ```bash
        python quickstart.py
        ```

        **Example output:**
        ```text Output
        [
            TextBlock(
                text='Here are some effective search strategies for finding the latest renewable energy developments:\n\n**Search Terms to Use:**\n- "renewable energy news 2024"\n- "clean energy breakthroughs"\n- "solar/wind/battery technology advances"\n- "energy storage innovations"\n- "green hydrogen developments"\n- "renewable energy policy updates"\n\n**Reliable Sources to Check:**\n- **News & Analysis:** Reuters Energy, Bloomberg New Energy Finance, Greentech Media, Energy Storage News\n- **Industry Publications:** Renewable Energy World, PV Magazine, Wind Power Engineering\n- **Research Organizations:** International Energy Agency (IEA), National Renewable Energy Laboratory (NREL)\n- **Government Sources:** Department of Energy websites, EPA clean energy updates\n\n**Specific Topics to Explore:**\n- Perovskite and next-gen solar cells\n- Offshore wind expansion\n- Grid-scale battery storage\n- Green hydrogen production\n- Carbon capture technologies\n- Smart grid innovations\n- Energy policy changes and incentives...',
                type="text",
            )
        ]
        ```
      </Step>
    </Steps>
  </Tab>

  <Tab title="TypeScript">
    <Steps>
      <Step title="Set your API key">
        Get your API key from the [Claude Console](/settings/keys) and set it as an environment variable:

        ```bash
        export ANTHROPIC_API_KEY='your-api-key-here'
        ```

        To persist the key across shell sessions, add the line to your shell profile (such as `~/.zshrc` or `~/.bashrc`).
      </Step>

      <Step title="Install the SDK">
        Install the Anthropic TypeScript SDK:

        ```bash
        npm install @anthropic-ai/sdk
        ```
      </Step>

      <Step title="Create your code">
        Save this as `quickstart.ts`:

```typescript
import Anthropic from "@anthropic-ai/sdk";

async function main() {
  const anthropic = new Anthropic();

  const msg = await anthropic.messages.create({
    model: "claude-opus-4-7",
    max_tokens: 1000,
    messages: [
      {
        role: "user",
        content:
          "What should I search for to find the latest developments in renewable energy?"
      }
    ]
  });
  console.log(msg);
}

main().catch(console.error);
        ```
      </Step>

      <Step title="Run your code">
        ```bash
        npx tsx quickstart.ts
        ```

        **Example output:**
        ```javascript Output hidelines={1..2}
        const _ =
          // output
          {
            id: "msg_01ThFHzad6Bh4TpQ6cHux9t8",
            type: "message",
            role: "assistant",
            model: "claude-opus-4-7",
            content: [
              {
                type: "text",
                text:
                  "Here are some effective search strategies to find the latest renewable energy developments:\n\n" +
                  "## Search Terms to Use:\n" +
                  '- "renewable energy news 2024"\n' +
                  '- "clean energy breakthroughs"\n' +
                  '- "solar wind technology advances"\n' +
                  '- "energy storage innovations"\n' +
                  '- "green hydrogen developments"\n' +
                  '- "offshore wind projects"\n' +
                  '- "battery technology renewable"\n\n' +
                  "## Best Sources to Check:\n\n" +
                  "**News & Industry Sites:**\n" +
                  "- Renewable Energy World\n" +
                  "- CleanTechnica\n" +
                  "- GreenTech Media (now Wood Mackenzie)\n" +
                  "- Energy Storage News\n" +
                  "- PV Magazine (for solar)..."
              }
            ],
            stop_reason: "end_turn",
            usage: {
              input_tokens: 21,
              output_tokens: 302
            }
          }
        ```
      </Step>
    </Steps>
  </Tab>

  <Tab title="Java">
    <Steps>
      <Step title="Set your API key">
        Get your API key from the [Claude Console](/settings/keys) and set it as an environment variable:

        ```bash
        export ANTHROPIC_API_KEY='your-api-key-here'
        ```

        To persist the key across shell sessions, add the line to your shell profile (such as `~/.zshrc` or `~/.bashrc`).
      </Step>

      <Step title="Set up your project">
        You need a JDK (25 or later) and either [Gradle](https://gradle.org/install/) or [Maven](https://maven.apache.org/install.html) on your `PATH`. Create a directory for your project with a Java source directory inside it:

        ```bash
        mkdir -p claude-quickstart/src/main/java && cd claude-quickstart
        ```

        Then add a build file. Find the current SDK version on [Maven Central](https://central.sonatype.com/artifact/com.anthropic/anthropic-java).

        <Tabs>
          <Tab title="Gradle">
            Save this as `build.gradle.kts`:

            ```kotlin
            plugins {
                application
            }

            repositories {
                mavenCentral()
            }

            java {
                toolchain {
                    languageVersion = JavaLanguageVersion.of(25)
                }
            }

            dependencies {
                implementation("com.anthropic:anthropic-java:2.30.0")
            }

            application {
                mainClass = "QuickStart"
            }
            ```
          </Tab>
          <Tab title="Maven">
            Save this as `pom.xml`:

            ```xml
            <project xmlns="http://maven.apache.org/POM/4.0.0">
              <modelVersion>4.0.0</modelVersion>
              <groupId>com.example</groupId>
              <artifactId>quickstart</artifactId>
              <version>1.0-SNAPSHOT</version>
              <properties>
                <maven.compiler.release>25</maven.compiler.release>
                <project.build.sourceEncoding>UTF-8</project.build.sourceEncoding>
              </properties>
              <dependencies>
                <dependency>
                  <groupId>com.anthropic</groupId>
                  <artifactId>anthropic-java</artifactId>
                  <version>2.30.0</version>
                </dependency>
              </dependencies>
            </project>
            ```
          </Tab>
        </Tabs>
      </Step>

      <Step title="Create your code">
        Save this as `QuickStart.java` in your project's Java source directory (usually `src/main/java/`):

        ```java
        import com.anthropic.client.okhttp.AnthropicOkHttpClient;
        import com.anthropic.models.messages.Message;
        import com.anthropic.models.messages.MessageCreateParams;
        import com.anthropic.models.messages.Model;

        static void main() {
            var client = AnthropicOkHttpClient.fromEnv();

            var params = MessageCreateParams.builder()
                .model(Model.CLAUDE_OPUS_4_7)
                .maxTokens(1000)
                .addUserMessage(
                    "What should I search for to find the latest developments in renewable energy?"
                )
                .build();

            Message message = client.messages().create(params);
            IO.println(message.content());
        }
        ```
      </Step>

      <Step title="Run your code">
        <Tabs>
          <Tab title="Gradle">
            ```bash
            gradle run
            ```
          </Tab>
          <Tab title="Maven">
            ```bash
            mvn compile exec:java -Dexec.mainClass=QuickStart
            ```
          </Tab>
        </Tabs>

        **Example output:**
        ```text Output
        [ContentBlock{text=TextBlock{text=Here are some effective search strategies to find the latest renewable energy developments:

        ## Search Terms to Use:
        - "renewable energy news 2024"
        - "clean energy breakthroughs"
        - "solar/wind/battery technology advances"
        - "energy storage innovations"
        - "green hydrogen developments"
        - "renewable energy policy updates"

        ## Best Sources to Check:
        - **News & Analysis:** Reuters Energy, Bloomberg New Energy Finance, Greentech Media
        - **Industry Publications:** Renewable Energy World, PV Magazine, Wind Power Engineering
        - **Research Organizations:** International Energy Agency (IEA), National Renewable Energy Laboratory (NREL)
        - **Government Sources:** Department of Energy websites, EPA clean energy updates

        ## Specific Topics to Explore:
        - Perovskite and next-gen solar cells
        - Offshore wind expansion
        - Grid-scale battery storage
        - Green hydrogen production..., type=text}}]
        ```
      </Step>
    </Steps>
  </Tab>
</Tabs>

## Next steps

You made your first API call. Next, learn the Messages API patterns you'll use in every Claude integration.

<Card title="Working with the Messages API" icon="messages" href="/docs/en/build-with-claude/working-with-messages">
  Learn multi-turn conversations, system prompts, stop reasons, and other core patterns.
</Card>

Once you're comfortable with the basics, explore further:

<CardGroup cols={3}>
  <Card title="Models overview" icon="brain" href="/docs/en/about-claude/models/overview">
    Compare Claude models by capability and cost.
  </Card>
  <Card title="Features overview" icon="list" href="/docs/en/build-with-claude/overview">
    Browse all Claude capabilities: tools, context management, structured outputs, and more.
  </Card>
  <Card title="Client SDKs" icon="code-brackets" href="/docs/en/api/client-sdks">
    Reference documentation for Python, TypeScript, Java, and other client libraries.
  </Card>
</CardGroup>