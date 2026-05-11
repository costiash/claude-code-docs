# Vision

Claude's vision capabilities allow it to understand and analyze images, opening up exciting possibilities for multimodal interaction.

---

This guide describes how to work with images in Claude, including best practices, code examples, and limitations to keep in mind.

---

## How to use vision

Use Claude's vision capabilities through:

- [claude.ai](https://claude.ai/). Upload an image like you would a file, or drag and drop an image directly into the chat window.
- The [Console Workbench](/workbench/). A button to add images appears at the top right of every User message block.
- API request. See the examples in this guide.

Multiple images can be included in a single request, which Claude will analyze jointly when formulating its response. This can be helpful for comparing or contrasting images.

---

## Before you upload

### General limits

The maximal number of images per message or request is:
  - 20 per message on [claude.ai](https://claude.ai/).
  - 100 per request on the API, for models with a 200k-token context window.
  - 600 per request on the API, for all other models.

The maximal dimensions per image are 8000x8000 px. If you submit more than 20 images in one API request, this limit is reduced to 2000x2000 px.

<Note>
While the API supports up to 600 images per request, [request size limits](/docs/en/api/overview#request-size-limits) (32&nbsp;MB for standard endpoints; lower on some partner-operated platforms, for example, Amazon Bedrock and Vertex AI) can be reached first. For many images, consider uploading with the [Files API](#files-api-image-example) and referencing by `file_id` to keep request payloads small.

Even when using the Files API, requests with many large images can fail before reaching the 600-image count. Reduce image dimensions or file sizes (for example, by downsampling) before uploading (see [Evaluate image size](#evaluate-image-size)).
</Note>

### Evaluate image size

An image uses approximately `width * height / 750` tokens, where the width and height are expressed in pixels.

The maximal native image resolution is:
- For Claude Opus 4.7: 4784 tokens, and at most 2576 pixels on the long edge.
- For other models: 1568 tokens, and at most 1568 pixels on the long edge.

If your input image is larger than this native resolution, it will first be resized to the largest possible size while preserving the aspect ratio. Moreover, images are padded on the bottom and right corners to a multiple of 28 pixels.

<Note>
When asking Claude to output coordinates (points, bounding boxes, etc.), they will be expressed with respect to the resized/padded image and will need to be rescaled/translated accordingly client-side based on the original and resized dimensions.
</Note>

To minimize latency and to simplify coordinate-based workflows, you should prefer resizing images before uploading them.

### Calculate image costs

Each image you include in a request to Claude counts toward your token usage. To calculate the approximate cost, multiply the approximate number of image tokens computed as above by the [per-token price of the model](https://claude.com/pricing) you're using.

Here are examples of approximate tokenization and costs for different image sizes within the API's size constraints based on Claude Sonnet 4.6 per-token price of $3 per million input tokens:

| Image size                    | \# of Tokens | Cost / image | Cost / 1k images |
| ----------------------------- | ------------ | ------------ | ---------------- |
| 200x200 px(0.04 megapixels)   | \~54         | \~$0.00016   | \~$0.16          |
| 1000x1000 px(1 megapixel)     | \~1334       | \~$0.004     | \~$4.00          |
| 1092x1092 px(1.19 megapixels) | \~1568       | \~$0.0047    | \~$4.70          |
| 1920x1080 px(2.07 megapixels) | \~1568       | \~$0.0047    | \~$4.70          |
| 2000x1500 px(3 megapixels)    | \~1568       | \~$0.0047    | \~$4.70          |

Note that the last three images are downscaled before processing.

#### High-resolution image support on Claude Opus 4.7

Claude Opus 4.7 is the first Claude model with high-resolution image support. The maximum image resolution is 2576 pixels on the long edge, up from 1568 px on prior models. This unlocks performance gains on vision-heavy workloads and is particularly valuable for computer use, screenshot understanding, and document analysis.

High-resolution support is automatic on Claude Opus 4.7 and requires no beta header or client-side opt-in.

High-resolution images on Claude Opus 4.7 can use up to approximately 3x more image tokens than on prior models (4784 versus 1568 tokens per image). If you don't need the additional fidelity, downsample images before sending to control token costs.

Here are the same image sizes tokenized for Claude Opus 4.7, based on its per-token price of $5 per million input tokens:

| Image size                    | \# of Tokens | Cost / image | Cost / 1k images |
| ----------------------------- | ------------ | ------------ | ---------------- |
| 200x200 px(0.04 megapixels)   | \~54         | \~$0.00027   | \~$0.27          |
| 1000x1000 px(1 megapixel)     | \~1334       | \~$0.0067    | \~$6.70          |
| 1092x1092 px(1.19 megapixels) | \~1590       | \~$0.0080    | \~$8.00          |
| 1920x1080 px(2.07 megapixels) | \~2765       | \~$0.014     | \~$14.00         |
| 2000x1500 px(3 megapixels)    | \~4000       | \~$0.020     | \~$20.00         |

### Ensure image quality

When providing images to Claude, keep the following in mind for best results:

- **Image format**: Use a supported image format: JPEG, PNG, GIF, or WebP.\
  Animations are unsupported, and only the first frame will be used.
- **Image clarity**: Ensure images are clear and not too blurry or pixelated.
- **Text**: If the image contains important text, make sure it's legible and not too small. Avoid cropping out key visual context just to enlarge the text.
- **Resizing**: Take into account that your image might be resized if it is too large (see above); this might for example make text less legible. Consider pre-resizing your images, cropping them, or both.
- **Image compression**: Compressing images before sending them, using a lossy format such as JPEG or WebP (lossy mode), can reduce latency by reducing the size of requests. However, this can introduce artifacts that are detrimental to model performance, especially when multiple compression passes are applied. For example, heavy JPEG compression can make text difficult to read. Confirm your compression settings are appropriate for the task by inspecting the actual images sent to the API.

---

## Prompt examples

Many of the [prompting techniques](/docs/en/build-with-claude/prompt-engineering/overview) that work well for text-based interactions with Claude can also be applied to image-based prompts.

These examples demonstrate best practice prompt structures involving images.

<Tip>
  Just as [placing long documents before your query](/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices#long-context-prompting) improves results in text prompts, Claude works best when images come before text. Images placed after text or interpolated with text still perform well, but if your use case allows it, prefer an image-then-text structure.
</Tip>

### About the prompt examples

The following examples demonstrate how to use Claude's vision capabilities using various programming languages and approaches. You can provide images to Claude in three ways:

1. As a base64-encoded image in `image` content blocks
2. As a URL reference to an image hosted online
3. Using the Files API (upload once, use multiple times)

The base64 example prompts use these variables:

<CodeGroup>
```bash cURL
    # For URL-based images, you can use the URL directly in your JSON request

    # For base64-encoded images, you need to first encode the image
    # Example of how to encode an image to base64 in bash:
    BASE64_IMAGE_DATA=$(curl -s "https://upload.wikimedia.org/wikipedia/commons/a/a7/Camponotus_flavomarginatus_ant.jpg" | base64)

    # The encoded data can now be used in your API calls
```

```python Python
import base64
import httpx

# For base64-encoded images
image1_url = "https://upload.wikimedia.org/wikipedia/commons/a/a7/Camponotus_flavomarginatus_ant.jpg"
image1_media_type = "image/jpeg"
image1_data = base64.standard_b64encode(httpx.get(image1_url).content).decode("utf-8")

image2_url = "https://upload.wikimedia.org/wikipedia/commons/b/b5/Iridescent.green.sweat.bee1.jpg"
image2_media_type = "image/jpeg"
image2_data = base64.standard_b64encode(httpx.get(image2_url).content).decode("utf-8")

# For URL-based images, you can use the URLs directly in your requests
```

```typescript TypeScript nocheck
import axios from "axios";

// For base64-encoded images
async function getBase64Image(url: string): Promise<string> {
  const response = await axios.get(url, { responseType: "arraybuffer" });
  return Buffer.from(response.data, "binary").toString("base64");
}

// Usage
async function prepareImages() {
  const imageData = await getBase64Image(
    "https://upload.wikimedia.org/wikipedia/commons/a/a7/Camponotus_flavomarginatus_ant.jpg"
  );
  // Now you can use imageData in your API calls
}

// For URL-based images, you can use the URLs directly in your requests
```

```csharp C#
using System;
using System.Net.Http;
using System.Threading.Tasks;

// For base64-encoded images
async Task<string> DownloadAndEncodeImageAsync(string url)
{
    using var client = new HttpClient();
    var bytes = await client.GetByteArrayAsync(url);
    return Convert.ToBase64String(bytes);
}

// Usage:
// var imageData = await DownloadAndEncodeImageAsync("https://upload.wikimedia.org/wikipedia/commons/a/a7/Camponotus_flavomarginatus_ant.jpg");
// For URL-based images, you can use the URLs directly in your requests
```

```go Go hidelines={1..9,-8..}
package main

import (
	"encoding/base64"
	"fmt"
	"io"
	"net/http"
)

func downloadAndEncodeImage(url string) (string, error) {
	req, err := http.NewRequest("GET", url, nil)
	if err != nil {
		return "", err
	}
	req.Header.Set("User-Agent", "AnthropicDocsBot/1.0")

	resp, err := http.DefaultClient.Do(req)
	if err != nil {
		return "", err
	}
	defer resp.Body.Close()

	data, err := io.ReadAll(resp.Body)
	if err != nil {
		return "", err
	}

	return base64.StdEncoding.EncodeToString(data), nil
}

func main() {
	imageData, err := downloadAndEncodeImage("https://upload.wikimedia.org/wikipedia/commons/a/a7/Camponotus_flavomarginatus_ant.jpg")
	if err != nil {
		panic(err)
	}
	fmt.Println(imageData[:50])
}
```

```java Java nocheck hidelines={1..7,-1}
import java.io.IOException;
import java.io.InputStream;
import java.net.URL;
import java.util.Base64;

public class ImageHandlingExample {

  public static void main(String[] args) throws IOException, InterruptedException {
    // For base64-encoded images
    String image1Url =
      "https://upload.wikimedia.org/wikipedia/commons/a/a7/Camponotus_flavomarginatus_ant.jpg";
    String image1MediaType = "image/jpeg";
    String image1Data = downloadAndEncodeImage(image1Url);

    String image2Url =
      "https://upload.wikimedia.org/wikipedia/commons/b/b5/Iridescent.green.sweat.bee1.jpg";
    String image2MediaType = "image/jpeg";
    String image2Data = downloadAndEncodeImage(image2Url);

    // For URL-based images, you can use the URLs directly in your requests
  }

  private static String downloadAndEncodeImage(String imageUrl) throws IOException {
    try (InputStream inputStream = new URL(imageUrl).openStream()) {
      return Base64.getEncoder().encodeToString(inputStream.readAllBytes());
    }
  }
}
```

```php PHP nocheck hidelines={1}
<?php
// For base64-encoded images
function downloadAndEncodeImage($url) {
    $imageData = file_get_contents($url);
    return base64_encode($imageData);
}

$image1Url = "https://upload.wikimedia.org/wikipedia/commons/a/a7/Camponotus_flavomarginatus_ant.jpg";
$image1MediaType = "image/jpeg";
$image1Data = downloadAndEncodeImage($image1Url);

// For URL-based images, you can use the URLs directly in your requests
```

```ruby Ruby
require "base64"
require "net/http"
require "uri"

# For base64-encoded images
def download_and_encode_image(url)
  uri = URI.parse(url)
  response = Net::HTTP.get_response(uri)
  Base64.strict_encode64(response.body)
end

image1_url = "https://upload.wikimedia.org/wikipedia/commons/a/a7/Camponotus_flavomarginatus_ant.jpg"
image1_media_type = "image/jpeg"
image1_data = download_and_encode_image(image1_url)

# For URL-based images, you can use the URLs directly in your requests
```
</CodeGroup>

Below are examples of how to include images in a Messages API request using base64-encoded images and URL references:

### Base64-encoded image example

<CodeGroup>
    ```bash cURL hidelines={1..2}
    BASE64_IMAGE_DATA=$(curl -s "https://upload.wikimedia.org/wikipedia/commons/a/a7/Camponotus_flavomarginatus_ant.jpg" | base64 | tr -d '\n')

    curl https://api.anthropic.com/v1/messages \
      -H "x-api-key: $ANTHROPIC_API_KEY" \
      -H "anthropic-version: 2023-06-01" \
      -H "content-type: application/json" \
      -d @- <<EOF
    {
      "model": "claude-opus-4-7",
      "max_tokens": 1024,
      "messages": [
        {
          "role": "user",
          "content": [
            {
              "type": "image",
              "source": {
                "type": "base64",
                "media_type": "image/jpeg",
                "data": "$BASE64_IMAGE_DATA"
              }
            },
            {
              "type": "text",
              "text": "Describe this image."
            }
          ]
        }
      ]
    }
    EOF
    ```
    ```bash CLI
    curl -sSo ./image.jpg \
      https://upload.wikimedia.org/wikipedia/commons/a/a7/Camponotus_flavomarginatus_ant.jpg

    ant messages create <<'YAML'
    model: claude-opus-4-7
    max_tokens: 1024
    messages:
      - role: user
        content:
          - type: image
            source:
              type: base64
              media_type: image/jpeg
              data: "@./image.jpg"
          - type: text
            text: Describe this image.
    YAML
    ```
    ```python Python hidelines={1..2}
    import anthropic

    image1_data = "iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAIAAACQd1PeAAAADElEQVR4nGP4z8AAAAMBAQDJ/pLvAAAAAElFTkSuQmCC"
    image1_media_type = "image/png"

    client = anthropic.Anthropic()
    message = client.messages.create(
        model="claude-opus-4-7",
        max_tokens=1024,
        messages=[
            {
                "role": "user",
                "content": [
                    {
                        "type": "image",
                        "source": {
                            "type": "base64",
                            "media_type": image1_media_type,
                            "data": image1_data,
                        },
                    },
                    {"type": "text", "text": "Describe this image."},
                ],
            }
        ],
    )
    print(message)
    ```
    
    ```typescript TypeScript nocheck hidelines={1..2}
    import Anthropic from "@anthropic-ai/sdk";

    const anthropic = new Anthropic({
      apiKey: process.env.ANTHROPIC_API_KEY
    });

    const message = await anthropic.messages.create({
      model: "claude-opus-4-7",
      max_tokens: 1024,
      messages: [
        {
          role: "user",
          content: [
            {
              type: "image",
              source: {
                type: "base64",
                media_type: "image/jpeg",
                data: imageData // Base64-encoded image data as string
              }
            },
            {
              type: "text",
              text: "Describe this image."
            }
          ]
        }
      ]
    });

    console.log(message);
    ```
    ```csharp C#
    using System.Collections.Generic;
    using Anthropic;
    using Anthropic.Models.Messages;

    AnthropicClient client = new();

    string imageData = "iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAIAAACQd1PeAAAADElEQVR4nGP4z8AAAAMBAQDJ/pLvAAAAAElFTkSuQmCC";

    var message = await client.Messages.Create(new MessageCreateParams
    {
        Model = Model.ClaudeOpus4_7,
        MaxTokens = 1024,
        Messages =
        [
            new()
            {
                Role = Role.User,
                Content = new MessageParamContent(new List<ContentBlockParam>
                {
                    new ContentBlockParam(new ImageBlockParam(
                        new ImageBlockParamSource(new Base64ImageSource()
                        {
                            Data = imageData,
                            MediaType = MediaType.ImagePng,
                        })
                    )),
                    new ContentBlockParam(new TextBlockParam("Describe this image.")),
                }),
            }
        ]
    });

    Console.WriteLine(message);
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

    	imageData := "iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAIAAACQd1PeAAAADElEQVR4nGP4z8AAAAMBAQDJ/pLvAAAAAElFTkSuQmCC"

    	message, err := client.Messages.New(context.TODO(), anthropic.MessageNewParams{
    		Model:     anthropic.ModelClaudeOpus4_7,
    		MaxTokens: 1024,
    		Messages: []anthropic.MessageParam{
    			anthropic.NewUserMessage(
    				anthropic.NewImageBlockBase64("image/png", imageData),
    				anthropic.NewTextBlock("Describe this image."),
    			),
    		},
    	})
    	if err != nil {
    		log.Fatal(err)
    	}

    	fmt.Println(message)
    }
    ```

    
    ```java Java nocheck hidelines={1..8,-2..}
    import com.anthropic.client.AnthropicClient;
    import com.anthropic.client.okhttp.AnthropicOkHttpClient;
    import com.anthropic.models.messages.*;
    import java.util.List;

    public class VisionExample {

      public static void main(String[] args) {
        AnthropicClient client = AnthropicOkHttpClient.fromEnv();
        String imageData = ""; // Base64-encoded image data as string

        List<ContentBlockParam> contentBlockParams = List.of(
          ContentBlockParam.ofImage(
            ImageBlockParam.builder()
              .source(
                Base64ImageSource.builder()
                  .mediaType(Base64ImageSource.MediaType.IMAGE_JPEG)
                  .data(imageData)
                  .build()
              )
              .build()
          ),
          ContentBlockParam.ofText(TextBlockParam.builder().text("Describe this image.").build())
        );
        Message message = client
          .messages()
          .create(
            MessageCreateParams.builder()
              .model(Model.CLAUDE_OPUS_4_7)
              .maxTokens(1024)
              .addUserMessageOfBlockParams(contentBlockParams)
              .build()
          );

        System.out.println(message);
      }
    }
    ```
    ```php PHP hidelines={1..4}
    <?php

    use Anthropic\Client;

    $client = new Client(apiKey: getenv("ANTHROPIC_API_KEY"));

    $imageData = "iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAIAAACQd1PeAAAADElEQVR4nGP4z8AAAAMBAQDJ/pLvAAAAAElFTkSuQmCC";

    $message = $client->messages->create(
        maxTokens: 1024,
        messages: [
            [
                'role' => 'user',
                'content' => [
                    [
                        'type' => 'image',
                        'source' => [
                            'type' => 'base64',
                            'media_type' => 'image/png',
                            'data' => $imageData,
                        ],
                    ],
                    ['type' => 'text', 'text' => 'Describe this image.'],
                ],
            ],
        ],
        model: 'claude-opus-4-7',
    );

    echo $message->content[0]->text;
    ```
    ```ruby Ruby hidelines={1..2}
    require "anthropic"

    client = Anthropic::Client.new

    image_data = "iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAIAAACQd1PeAAAADElEQVR4nGP4z8AAAAMBAQDJ/pLvAAAAAElFTkSuQmCC"

    message = client.messages.create(
      model: "claude-opus-4-7",
      max_tokens: 1024,
      messages: [
        {
          role: "user",
          content: [
            {
              type: "image",
              source: {
                type: "base64",
                media_type: "image/png",
                data: image_data
              }
            },
            { type: "text", text: "Describe this image." }
          ]
        }
      ]
    )

    puts message
    ```
</CodeGroup>

### URL-based image example

<CodeGroup>
    ```bash cURL
    curl https://api.anthropic.com/v1/messages \
      -H "x-api-key: $ANTHROPIC_API_KEY" \
      -H "anthropic-version: 2023-06-01" \
      -H "content-type: application/json" \
      -d '{
        "model": "claude-opus-4-7",
        "max_tokens": 1024,
        "messages": [
          {
            "role": "user",
            "content": [
              {
                "type": "image",
                "source": {
                  "type": "url",
                  "url": "https://upload.wikimedia.org/wikipedia/commons/a/a7/Camponotus_flavomarginatus_ant.jpg"
                }
              },
              {
                "type": "text",
                "text": "Describe this image."
              }
            ]
          }
        ]
      }'
    ```
    ```bash CLI
    ant messages create <<'YAML'
    model: claude-opus-4-7
    max_tokens: 1024
    messages:
      - role: user
        content:
          - type: image
            source:
              type: url
              url: https://upload.wikimedia.org/wikipedia/commons/a/a7/Camponotus_flavomarginatus_ant.jpg
          - type: text
            text: Describe this image.
    YAML
    ```
    ```python Python hidelines={1..2}
    import anthropic

    client = anthropic.Anthropic()
    message = client.messages.create(
        model="claude-opus-4-7",
        max_tokens=1024,
        messages=[
            {
                "role": "user",
                "content": [
                    {
                        "type": "image",
                        "source": {
                            "type": "url",
                            "url": "https://upload.wikimedia.org/wikipedia/commons/a/a7/Camponotus_flavomarginatus_ant.jpg",
                        },
                    },
                    {"type": "text", "text": "Describe this image."},
                ],
            }
        ],
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
      max_tokens: 1024,
      messages: [
        {
          role: "user",
          content: [
            {
              type: "image",
              source: {
                type: "url",
                url: "https://upload.wikimedia.org/wikipedia/commons/a/a7/Camponotus_flavomarginatus_ant.jpg"
              }
            },
            {
              type: "text",
              text: "Describe this image."
            }
          ]
        }
      ]
    });

    console.log(message);
    ```
    ```csharp C#
    using System.Collections.Generic;
    using Anthropic;
    using Anthropic.Models.Messages;

    AnthropicClient client = new();

    var message = await client.Messages.Create(new MessageCreateParams
    {
        Model = Model.ClaudeOpus4_7,
        MaxTokens = 1024,
        Messages =
        [
            new()
            {
                Role = Role.User,
                Content = new MessageParamContent(new List<ContentBlockParam>
                {
                    new ContentBlockParam(new ImageBlockParam(
                        new ImageBlockParamSource(new UrlImageSource()
                        {
                            Url = "https://upload.wikimedia.org/wikipedia/commons/a/a7/Camponotus_flavomarginatus_ant.jpg",
                        })
                    )),
                    new ContentBlockParam(new TextBlockParam("Describe this image.")),
                }),
            }
        ]
    });

    Console.WriteLine(message);
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

    	message, err := client.Messages.New(context.TODO(), anthropic.MessageNewParams{
    		Model:     anthropic.ModelClaudeOpus4_7,
    		MaxTokens: 1024,
    		Messages: []anthropic.MessageParam{
    			anthropic.NewUserMessage(
    				anthropic.NewImageBlock(anthropic.URLImageSourceParam{
    					URL: "https://upload.wikimedia.org/wikipedia/commons/a/a7/Camponotus_flavomarginatus_ant.jpg",
    				}),
    				anthropic.NewTextBlock("Describe this image."),
    			),
    		},
    	})
    	if err != nil {
    		log.Fatal(err)
    	}

    	fmt.Println(message)
    }
    ```
    ```java Java hidelines={1..9,-2..}
    import com.anthropic.client.AnthropicClient;
    import com.anthropic.client.okhttp.AnthropicOkHttpClient;
    import com.anthropic.models.messages.*;
    import java.io.IOException;
    import java.util.List;

    public class VisionExample {

      public static void main(String[] args) throws IOException, InterruptedException {
        AnthropicClient client = AnthropicOkHttpClient.fromEnv();

        List<ContentBlockParam> contentBlockParams = List.of(
          ContentBlockParam.ofImage(
            ImageBlockParam.builder()
              .source(
                UrlImageSource.builder()
                  .url(
                    "https://upload.wikimedia.org/wikipedia/commons/a/a7/Camponotus_flavomarginatus_ant.jpg"
                  )
                  .build()
              )
              .build()
          ),
          ContentBlockParam.ofText(TextBlockParam.builder().text("Describe this image.").build())
        );
        Message message = client
          .messages()
          .create(
            MessageCreateParams.builder()
              .model(Model.CLAUDE_OPUS_4_7)
              .maxTokens(1024)
              .addUserMessageOfBlockParams(contentBlockParams)
              .build()
          );
        System.out.println(message);
      }
    }
    ```
    ```php PHP hidelines={1..4}
    <?php

    use Anthropic\Client;

    $client = new Client(apiKey: getenv("ANTHROPIC_API_KEY"));

    $message = $client->messages->create(
        maxTokens: 1024,
        messages: [
            [
                'role' => 'user',
                'content' => [
                    [
                        'type' => 'image',
                        'source' => [
                            'type' => 'url',
                            'url' => 'https://upload.wikimedia.org/wikipedia/commons/a/a7/Camponotus_flavomarginatus_ant.jpg',
                        ],
                    ],
                    ['type' => 'text', 'text' => 'Describe this image.'],
                ],
            ],
        ],
        model: 'claude-opus-4-7',
    );

    echo $message->content[0]->text;
    ```
    ```ruby Ruby hidelines={1..2}
    require "anthropic"

    client = Anthropic::Client.new

    message = client.messages.create(
      model: "claude-opus-4-7",
      max_tokens: 1024,
      messages: [
        {
          role: "user",
          content: [
            {
              type: "image",
              source: {
                type: "url",
                url: "https://upload.wikimedia.org/wikipedia/commons/a/a7/Camponotus_flavomarginatus_ant.jpg"
              }
            },
            { type: "text", text: "Describe this image." }
          ]
        }
      ]
    )

    puts message
    ```
</CodeGroup>

### Files API image example

For images you'll use repeatedly or when you want to avoid encoding overhead, use the [Files API](/docs/en/build-with-claude/files). Upload the image once, then reference the returned `file_id` in subsequent messages instead of resending base64 data.

<Tip>
  In multi-turn conversations and agentic workflows, each request resends the
  full conversation history. If images are base64-encoded, the full image bytes
  are included in the payload on every turn, which can significantly increase
  request size and latency as the conversation grows. Uploading images to the
  Files API and referencing them by `file_id` keeps request payloads small
  regardless of how many images accumulate in the conversation history.
</Tip>

<CodeGroup>
```bash cURL hidelines={1..2}
cd "$(mktemp -d)"
curl -sSo image.jpg https://upload.wikimedia.org/wikipedia/commons/a/a7/Camponotus_flavomarginatus_ant.jpg
# First, upload your image to the Files API
curl -X POST https://api.anthropic.com/v1/files \
  -H "x-api-key: $ANTHROPIC_API_KEY" \
  -H "anthropic-version: 2023-06-01" \
  -H "anthropic-beta: files-api-2025-04-14" \
  -F "file=@image.jpg"

# Then use the returned file_id in your message
curl https://api.anthropic.com/v1/messages \
  -H "x-api-key: $ANTHROPIC_API_KEY" \
  -H "anthropic-version: 2023-06-01" \
  -H "anthropic-beta: files-api-2025-04-14" \
  -H "content-type: application/json" \
  -d '{
    "model": "claude-opus-4-7",
    "max_tokens": 1024,
    "messages": [
      {
        "role": "user",
        "content": [
          {
            "type": "image",
            "source": {
              "type": "file",
              "file_id": "file_abc123"
            }
          },
          {
            "type": "text",
            "text": "Describe this image."
          }
        ]
      }
    ]
  }'
```

```bash CLI nocheck hidelines={1}
cd "$(mktemp -d)"
curl -sSo image.jpg \
  https://upload.wikimedia.org/wikipedia/commons/a/a7/Camponotus_flavomarginatus_ant.jpg

# First, upload your image to the Files API
FILE_ID=$(ant beta:files upload \
  --file ./image.jpg \
  --transform id --raw-output)

# Then use the returned file_id in your message
ant beta:messages create \
  --beta files-api-2025-04-14 \
  --transform content --format yaml <<YAML
model: claude-opus-4-7
max_tokens: 1024
messages:
  - role: user
    content:
      - type: image
        source:
          type: file
          file_id: $FILE_ID
      - type: text
        text: Describe this image.
YAML
```

```python Python nocheck hidelines={1..2}
import anthropic

client = anthropic.Anthropic()

# Upload the image file
with open("image.jpg", "rb") as f:
    file_upload = client.beta.files.upload(file=("image.jpg", f, "image/jpeg"))

# Use the uploaded file in a message
message = client.beta.messages.create(
    model="claude-opus-4-7",
    max_tokens=1024,
    betas=["files-api-2025-04-14"],
    messages=[
        {
            "role": "user",
            "content": [
                {
                    "type": "image",
                    "source": {"type": "file", "file_id": file_upload.id},
                },
                {"type": "text", "text": "Describe this image."},
            ],
        }
    ],
)

print(message.content)
```

```typescript TypeScript nocheck
import Anthropic, { toFile } from "@anthropic-ai/sdk";
import fs from "fs";

const anthropic = new Anthropic();

// Upload the image file
const fileUpload = await anthropic.beta.files.upload({
  file: await toFile(fs.createReadStream("image.jpg"), undefined, { type: "image/jpeg" })
});

// Use the uploaded file in a message
const response = await anthropic.beta.messages.create({
  model: "claude-opus-4-7",
  max_tokens: 1024,
  betas: ["files-api-2025-04-14"],
  messages: [
    {
      role: "user",
      content: [
        {
          type: "image",
          source: {
            type: "file",
            file_id: fileUpload.id
          }
        },
        {
          type: "text",
          text: "Describe this image."
        }
      ]
    }
  ]
});

console.log(response);
```

```csharp C# nocheck
using Anthropic;

var client = new AnthropicClient();

// Upload the image file
var fileUpload = await client.Beta.Files.Upload(
    new FileUploadParams { File = File.OpenRead("image.jpg") });

// Use the uploaded file in a message
var response = await client.Beta.Messages.Create(
    new MessageCreateParams
    {
        Model = "claude-opus-4-7",
        MaxTokens = 1024,
        Betas = new[] { "files-api-2025-04-14" },
        Messages = new[]
        {
            new BetaMessageParam
            {
                Role = "user",
                Content = new object[]
                {
                    new
                    {
                        type = "image",
                        source = new { type = "file", file_id = fileUpload.Id }
                    },
                    new { type = "text", text = "Describe this image." }
                }
            }
        }
    });

Console.WriteLine(response);
```

```go Go nocheck hidelines={1..12,-1}
package main

import (
	"context"
	"fmt"
	"log"
	"os"

	"github.com/anthropics/anthropic-sdk-go"
)

func main() {
	client := anthropic.NewClient()

	// Upload the image file
	file, err := os.Open("image.jpg")
	if err != nil {
		log.Fatal(err)
	}
	defer file.Close()

	fileUpload, err := client.Beta.Files.Upload(context.Background(),
		anthropic.BetaFileUploadParams{
			File: file,
		})
	if err != nil {
		log.Fatal(err)
	}

	// Use the uploaded file in a message
	message, err := client.Beta.Messages.New(context.Background(),
		anthropic.BetaMessageNewParams{
			Model:     anthropic.ModelClaudeOpus4_7,
			MaxTokens: 1024,
			Betas:     []anthropic.AnthropicBeta{anthropic.AnthropicBetaFilesAPI2025_04_14},
			Messages: []anthropic.BetaMessageParam{
				anthropic.NewBetaUserMessage(
					anthropic.NewBetaImageBlock(anthropic.BetaFileImageSourceParam{
						FileID: fileUpload.ID,
					}),
					anthropic.NewBetaTextBlock("Describe this image."),
				),
			},
		})
	if err != nil {
		log.Fatal(err)
	}

	fmt.Println(message.Content)
}
```

```java Java nocheck hidelines={1..2,5..13,-2..}
import com.anthropic.client.AnthropicClient;
import com.anthropic.client.okhttp.AnthropicOkHttpClient;
import com.anthropic.models.beta.files.FileMetadata;
import com.anthropic.models.beta.files.FileUploadParams;
import com.anthropic.models.messages.*;
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.List;

public class ImageFilesExample {

  public static void main(String[] args) throws IOException {
    AnthropicClient client = AnthropicOkHttpClient.fromEnv();

    // Upload the image file
    FileMetadata file = client
      .beta()
      .files()
      .upload(
        FileUploadParams.builder().file(Files.newInputStream(Path.of("image.jpg"))).build()
      );

    // Use the uploaded file in a message
    ImageBlockParam imageParam = ImageBlockParam.builder().fileSource(file.id()).build();

    MessageCreateParams params = MessageCreateParams.builder()
      .model(Model.CLAUDE_OPUS_4_7)
      .maxTokens(1024)
      .addUserMessageOfBlockParams(
        List.of(
          ContentBlockParam.ofImage(imageParam),
          ContentBlockParam.ofText(
            TextBlockParam.builder().text("Describe this image.").build()
          )
        )
      )
      .build();

    Message message = client.messages().create(params);
    System.out.println(message.content());
  }
}
```

```php PHP nocheck hidelines={1..4}
<?php

use Anthropic\Client;

$client = new Client(apiKey: getenv("ANTHROPIC_API_KEY"));

// Upload the image file
$fileUpload = $client->beta->files->upload(
    file: fopen('image.jpg', 'r'),
);

// Use the uploaded file in a message
$message = $client->beta->messages->create(
    maxTokens: 1024,
    messages: [
        [
            'role' => 'user',
            'content' => [
                [
                    'type' => 'image',
                    'source' => ['type' => 'file', 'file_id' => $fileUpload->id],
                ],
                ['type' => 'text', 'text' => 'Describe this image.'],
            ],
        ],
    ],
    model: 'claude-opus-4-7',
    betas: ['files-api-2025-04-14'],
);

echo $message->content[0]->text;
```

```ruby Ruby nocheck hidelines={1..2}
require "anthropic"

client = Anthropic::Client.new

# Upload the image file
file_upload = client.beta.files.upload(
  file: File.open("image.jpg", "rb")
)

# Use the uploaded file in a message
message = client.beta.messages.create(
  model: "claude-opus-4-7",
  max_tokens: 1024,
  betas: ["files-api-2025-04-14"],
  messages: [
    {
      role: "user",
      content: [
        {
          type: "image",
          source: { type: "file", file_id: file_upload.id }
        },
        { type: "text", text: "Describe this image." }
      ]
    }
  ]
)

puts message.content
```
</CodeGroup>

See [Messages API examples](/docs/en/api/messages/create) for more example code and parameter details.

<section title="Example: One image">

It's best to place images earlier in the prompt than questions about them or instructions for tasks that use them.

Ask Claude to describe one image.

| Role | Content                        |
| ---- | ------------------------------ |
| User | \[Image\] Describe this image. |

<Tabs>
  <Tab title="Using Base64">
    ```python Python hidelines={1..2}
    import anthropic

    client = anthropic.Anthropic()
    image1_data = "iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAIAAACQd1PeAAAADElEQVR4nGP4z8AAAAMBAQDJ/pLvAAAAAElFTkSuQmCC"
    image1_media_type = "image/png"

    message = client.messages.create(
        model="claude-opus-4-7",
        max_tokens=1024,
        messages=[
            {
                "role": "user",
                "content": [
                    {
                        "type": "image",
                        "source": {
                            "type": "base64",
                            "media_type": image1_media_type,
                            "data": image1_data,
                        },
                    },
                    {"type": "text", "text": "Describe this image."},
                ],
            }
        ],
    )
    ```
  </Tab>
  <Tab title="Using URL">
    ```python Python
    message = client.messages.create(
        model="claude-opus-4-7",
        max_tokens=1024,
        messages=[
            {
                "role": "user",
                "content": [
                    {
                        "type": "image",
                        "source": {
                            "type": "url",
                            "url": "https://upload.wikimedia.org/wikipedia/commons/a/a7/Camponotus_flavomarginatus_ant.jpg",
                        },
                    },
                    {"type": "text", "text": "Describe this image."},
                ],
            }
        ],
    )
    ```
  </Tab>
</Tabs>

</section>
<section title="Example: Multiple images">

In situations where there are multiple images, introduce each image with `Image 1:` and `Image 2:` and so on. You don't need newlines between images or between images and the prompt.

Ask Claude to describe the differences between multiple images.
| Role | Content |
| ---- | ------------------------------------------------------------------------- |
| User | Image 1: \[Image 1\] Image 2: \[Image 2\] How are these images different? |

<Tabs>
  <Tab title="Using Base64">
    ```python Python hidelines={1..2}
    import anthropic

    client = anthropic.Anthropic()
    image1_data = "iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAIAAACQd1PeAAAADElEQVR4nGP4z8AAAAMBAQDJ/pLvAAAAAElFTkSuQmCC"
    image1_media_type = "image/png"
    image2_data = "iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAIAAACQd1PeAAAADElEQVR4nGP4z8AAAAMBAQDJ/pLvAAAAAElFTkSuQmCC"
    image2_media_type = "image/png"

    message = client.messages.create(
        model="claude-opus-4-7",
        max_tokens=1024,
        messages=[
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": "Image 1:"},
                    {
                        "type": "image",
                        "source": {
                            "type": "base64",
                            "media_type": image1_media_type,
                            "data": image1_data,
                        },
                    },
                    {"type": "text", "text": "Image 2:"},
                    {
                        "type": "image",
                        "source": {
                            "type": "base64",
                            "media_type": image2_media_type,
                            "data": image2_data,
                        },
                    },
                    {"type": "text", "text": "How are these images different?"},
                ],
            }
        ],
    )
    ```
  </Tab>
  <Tab title="Using URL">
    ```python Python
    message = client.messages.create(
        model="claude-opus-4-7",
        max_tokens=1024,
        messages=[
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": "Image 1:"},
                    {
                        "type": "image",
                        "source": {
                            "type": "url",
                            "url": "https://upload.wikimedia.org/wikipedia/commons/a/a7/Camponotus_flavomarginatus_ant.jpg",
                        },
                    },
                    {"type": "text", "text": "Image 2:"},
                    {
                        "type": "image",
                        "source": {
                            "type": "url",
                            "url": "https://upload.wikimedia.org/wikipedia/commons/b/b5/Iridescent.green.sweat.bee1.jpg",
                        },
                    },
                    {"type": "text", "text": "How are these images different?"},
                ],
            }
        ],
    )
    ```
  </Tab>
</Tabs>

</section>
<section title="Example: Multiple images with a system prompt">

Ask Claude to describe the differences between multiple images, while giving it a system prompt for how to respond.

| Content |                                                                           |
| ------- | ------------------------------------------------------------------------- |
| System  | Respond only in Spanish.                                                  |
| User    | Image 1: \[Image 1\] Image 2: \[Image 2\] How are these images different? |

<Tabs>
  <Tab title="Using Base64">
    ```python Python hidelines={1..2}
    import anthropic

    client = anthropic.Anthropic()
    image1_data = "iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAIAAACQd1PeAAAADElEQVR4nGP4z8AAAAMBAQDJ/pLvAAAAAElFTkSuQmCC"
    image1_media_type = "image/png"
    image2_data = "iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAIAAACQd1PeAAAADElEQVR4nGP4z8AAAAMBAQDJ/pLvAAAAAElFTkSuQmCC"
    image2_media_type = "image/png"

    message = client.messages.create(
        model="claude-opus-4-7",
        max_tokens=1024,
        system="Respond only in Spanish.",
        messages=[
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": "Image 1:"},
                    {
                        "type": "image",
                        "source": {
                            "type": "base64",
                            "media_type": image1_media_type,
                            "data": image1_data,
                        },
                    },
                    {"type": "text", "text": "Image 2:"},
                    {
                        "type": "image",
                        "source": {
                            "type": "base64",
                            "media_type": image2_media_type,
                            "data": image2_data,
                        },
                    },
                    {"type": "text", "text": "How are these images different?"},
                ],
            }
        ],
    )
    ```
  </Tab>
  <Tab title="Using URL">
    ```python Python
    message = client.messages.create(
        model="claude-opus-4-7",
        max_tokens=1024,
        system="Respond only in Spanish.",
        messages=[
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": "Image 1:"},
                    {
                        "type": "image",
                        "source": {
                            "type": "url",
                            "url": "https://upload.wikimedia.org/wikipedia/commons/a/a7/Camponotus_flavomarginatus_ant.jpg",
                        },
                    },
                    {"type": "text", "text": "Image 2:"},
                    {
                        "type": "image",
                        "source": {
                            "type": "url",
                            "url": "https://upload.wikimedia.org/wikipedia/commons/b/b5/Iridescent.green.sweat.bee1.jpg",
                        },
                    },
                    {"type": "text", "text": "How are these images different?"},
                ],
            }
        ],
    )
    ```
  </Tab>
</Tabs>

</section>
<section title="Example: Four images across two conversation turns">

Claude's vision capabilities shine in multimodal conversations that mix images and text. You can have extended back-and-forth exchanges with Claude, adding new images or follow-up questions at any point. This enables powerful workflows for iterative image analysis, comparison, or combining visuals with other knowledge.

Ask Claude to contrast two images, then ask a follow-up question comparing the first images to two new images.
| Role | Content |
| --------- | ------------------------------------------------------------------------------------ |
| User | Image 1: \[Image 1\] Image 2: \[Image 2\] How are these images different? |
| Assistant | \[Claude's response\] |
| User | Image 1: \[Image 3\] Image 2: \[Image 4\] Are these images similar to the first two? |
| Assistant | \[Claude's response\] |

When using the API, insert new images into the array of Messages in the `user` role as part of any standard [multiturn conversation](/docs/en/api/messages/create) structure.

</section>

---

## Limitations

While Claude's image understanding capabilities are cutting-edge, there are some limitations to be aware of:

- **People identification**: Claude [cannot be used](https://www.anthropic.com/legal/aup) to name people in images and refuses to do so.
- **Accuracy**: Claude may hallucinate or make mistakes when interpreting low-quality, rotated, or very small images under 200 pixels.
- **Spatial reasoning**: Claude's spatial reasoning abilities are limited. It may struggle with tasks requiring precise localization or layouts, like reading an analog clock face or describing exact positions of chess pieces.
- **Counting**: Claude can give approximate counts of objects in an image but may not always be precisely accurate, especially with large numbers of small objects.
- **AI generated images**: Claude does not know if an image is AI-generated and may be incorrect if asked. Do not rely on it to detect fake or synthetic images.
- **Inappropriate content**: Claude does not process inappropriate or explicit images that violate the [Acceptable Use Policy](https://www.anthropic.com/legal/aup).
- **Healthcare applications**: While Claude can analyze general medical images, it is not designed to interpret complex diagnostic scans such as CTs or MRIs. Claude's outputs should not be considered a substitute for professional medical advice or diagnosis.

Always carefully review and verify Claude's image interpretations, especially for high-stakes use cases. Do not use Claude for tasks requiring perfect precision or sensitive image analysis without human oversight.

---

## FAQ

  <section title="What image file types does Claude support?">

    Claude currently supports JPEG, PNG, GIF, and WebP image formats, specifically:
    - `image/jpeg`
    - `image/png`
    - `image/gif`
    - `image/webp`
  
</section>

{" "}

<section title="Can Claude read image URLs?">

  Yes, Claude can process images from URLs with URL image source blocks in the API.
  Simply use the "url" source type instead of "base64" in your API requests.
  Example:
  ```json
  {
    "type": "image",
    "source": {
      "type": "url",
      "url": "https://upload.wikimedia.org/wikipedia/commons/a/a7/Camponotus_flavomarginatus_ant.jpg"
    }
  }
  ```

</section>

  <section title="Is there a limit to the image file size I can upload?">

    Yes, there are limits:
    - API: Maximum 5&nbsp;MB per image
    - claude.ai: Maximum 10&nbsp;MB per image

    Images larger than these limits are rejected and return an error when using the API.

  
</section>

  <section title="How many images can I include in one request?">

    The image limits are:
    - Messages API: Up to 600 images per request (100 for models with a 200k-token context window)
    - claude.ai: Up to 20 images per turn

    Requests exceeding these limits are rejected and return an error. Requests with many large images may also fail before reaching these limits; see [General limits](#general-limits) for details.

  
</section>

{" "}

<section title="Does Claude read image metadata?">

  No, Claude does not parse or receive any metadata from images passed to it.

</section>

{" "}

<section title="Can I delete images I've uploaded?">

  No. Image uploads are ephemeral and not stored beyond the duration of the API
  request. Uploaded images are automatically deleted after they have been
  processed.

</section>

{" "}

<section title="Where can I find details on data privacy for image uploads?">

  Refer to the Anthropic privacy policy page for information on how uploaded
  images and other data are handled. Anthropic does not use uploaded images to
  train models.

</section>

  <section title="What if Claude's image interpretation seems wrong?">

    If Claude's image interpretation seems incorrect:
    1. Ensure the image is clear, high-quality, and correctly oriented.
    2. Try prompt engineering techniques to improve results.
    3. If the issue persists, flag the output in claude.ai (thumbs up/down) or contact the [support team](https://support.claude.com/).

    Your feedback helps improve Claude!

  
</section>

  <section title="Can Claude generate or edit images?">

    No, Claude is an image understanding model only. It can interpret and analyze images, but it cannot generate, produce, edit, manipulate, or create images.
  
</section>

---

## Dive deeper into vision

Ready to start building with images using Claude? Here are a few helpful resources:

- [Multimodal cookbook](https://platform.claude.com/cookbook/multimodal-getting-started-with-vision): This cookbook has tips on [getting started with images](https://platform.claude.com/cookbook/multimodal-getting-started-with-vision) and [best practice techniques](https://platform.claude.com/cookbook/multimodal-best-practices-for-vision) to ensure the highest quality performance with images. See how you can effectively prompt Claude with images to carry out tasks such as [interpreting and analyzing charts](https://platform.claude.com/cookbook/multimodal-reading-charts-graphs-powerpoints) or [extracting content from forms](https://platform.claude.com/cookbook/multimodal-how-to-transcribe-text).
- [API reference](/docs/en/api/messages/create): Documentation for the Messages API, including example [API calls involving images](/docs/en/build-with-claude/working-with-messages#vision).

If you have any other questions, reach out to the [support team](https://support.claude.com/). You can also join the [developer community](https://www.anthropic.com/discord) to connect with other creators and get help from Anthropic experts.