# Data residency

Manage where model inference runs and where data is stored with geographic controls.

---

Data residency controls let you manage where your data is processed and stored. Two independent settings govern this:

- **Inference geo**: Controls where model inference runs, on a per-request basis. Set via the `inference_geo` API parameter or as a workspace default.
- **Workspace geo**: Controls where data is stored at rest and where endpoint processing (image transcoding, code execution, etc.) happens. Configured at the workspace level in the [Console](https://platform.claude.com).

## Inference geo

The `inference_geo` parameter controls where model inference runs for a specific API request. Add it to any `POST /v1/messages` call.

| Value | Description |
|:------|:------------|
| `"global"` | Default. Inference may run in any available geography for optimal performance and availability. |
| `"us"` | Inference runs only in US-based infrastructure. |

### API usage

<CodeGroup>
```bash Shell
curl https://api.anthropic.com/v1/messages \
    --header "x-api-key: $ANTHROPIC_API_KEY" \
    --header "anthropic-version: 2023-06-01" \
    --header "content-type: application/json" \
    --data '{
        "model": "claude-opus-4-6",
        "max_tokens": 1024,
        "inference_geo": "us",
        "messages": [{
            "role": "user",
            "content": "Summarize the key points of this document."
        }]
    }'
```

```python Python
import anthropic

client = anthropic.Anthropic()

response = client.messages.create(
    model="claude-opus-4-6",
    max_tokens=1024,
    inference_geo="us",
    messages=[{
        "role": "user",
        "content": "Summarize the key points of this document."
    }]
)

print(response.content[0].text)
# Check where inference actually ran
print(f"Inference geo: {response.usage.inference_geo}")
```

```typescript TypeScript
import Anthropic from '@anthropic-ai/sdk';

const client = new Anthropic();

const response = await client.messages.create({
  model: "claude-opus-4-6",
  max_tokens: 1024,
  inference_geo: "us",
  messages: [{
    role: "user",
    content: "Summarize the key points of this document."
  }]
});

console.log(response.content[0].text);
// Check where inference actually ran
console.log(`Inference geo: ${response.usage.inference_geo}`);
```
</CodeGroup>

### Response

The response `usage` object includes an `inference_geo` field indicating where inference ran:

```json
{
  "usage": {
    "input_tokens": 25,
    "output_tokens": 150,
    "inference_geo": "us"
  }
}
```

### Model availability

The `inference_geo` parameter is supported on Claude Opus 4.6 and all subsequent models. Older models released before Opus 4.6 do not support the parameter. Requests with `inference_geo` on legacy models return a 400 error.

<Note>
The `inference_geo` parameter is only available on the Claude API (1P). On third-party platforms (AWS Bedrock, Google Vertex AI), the inference region is determined by the endpoint URL or inference profile, so `inference_geo` is not applicable. The `inference_geo` parameter is also not available via the [OpenAI SDK compatibility endpoint](/docs/en/api/openai-sdk).
</Note>

### Workspace-level restrictions

Workspace settings also support restricting which inference geos are available:

- **`allowed_inference_geos`**: Restricts which geos a workspace can use. If a request specifies an `inference_geo` not in this list, the API returns an error.
- **`default_inference_geo`**: Sets the fallback geo when `inference_geo` is omitted from a request. Individual requests can override this by setting `inference_geo` explicitly.

These settings can be configured through the Console or the [Admin API](/docs/en/build-with-claude/administration-api) under the `data_residency` field.

## Workspace geo

Workspace geo is set when you create a workspace and can't be changed afterwards. Currently, `"us"` is the only available workspace geo.

To set workspace geo, create a new workspace in the [Console](https://platform.claude.com):

1. Go to **Settings** > **Workspaces**.
2. Create a new workspace.
3. Select the workspace geo.

## Pricing

Data residency pricing varies by model generation:

- **Claude Opus 4.6 and newer**: US-only inference (`inference_geo: "us"`) is priced at 1.1x the standard rate across all token pricing categories (input tokens, output tokens, cache writes, and cache reads).
- **Global routing** (`inference_geo: "global"` or omitted): Standard pricing applies.
- **Older models**: Existing pricing is unchanged regardless of `inference_geo` settings.

This pricing applies to the Claude API (1P) only. Third-party platforms (AWS Bedrock, Google Vertex AI, Microsoft Foundry) have their own regional pricing. See the [pricing page](/docs/en/about-claude/pricing#data-residency-pricing) for details.

<Note>
If you use [Priority Tier](/docs/en/api/service-tiers), the 1.1x multiplier for US-only inference also affects how tokens are counted against your Priority Tier capacity. Each token consumed with `inference_geo: "us"` draws down 1.1 tokens from your committed TPM, consistent with how other pricing multipliers (prompt caching, long context) affect burndown rates.
</Note>

## Batch API support

The `inference_geo` parameter is supported on the [Batch API](/docs/en/build-with-claude/batch-processing). Each request in a batch can specify its own `inference_geo` value.

## Migration from legacy opt-outs

If your organization previously opted out of global routing to keep inference in the US, your workspace has been automatically configured with `allowed_inference_geos: ["us"]` and `default_inference_geo: "us"`. No code changes are required. Your existing data residency requirements continue to be enforced through the new geo controls.

### What changed

The legacy opt-out was an organization-level setting that restricted all requests to US-based infrastructure. The new data residency controls replace this with two mechanisms:

- **Per-request control**: The `inference_geo` parameter lets you specify `"us"` or `"global"` on each API call, giving you request-level flexibility.
- **Workspace controls**: The `default_inference_geo` and `allowed_inference_geos` settings in the Console let you enforce geo policies across all keys in a workspace.

### What happened to your workspace

Your workspace was migrated automatically:

| Legacy setting | New equivalent |
|:---------------|:---------------|
| Global routing opt-out (US only) | `allowed_inference_geos: ["us"]`, `default_inference_geo: "us"` |

All API requests using keys from your workspace continue to run on US-based infrastructure. No action is needed to maintain your current behavior.

### If you want to use global routing

If your data residency requirements have changed and you want to take advantage of global routing for better performance and availability, update your workspace's inference geo settings to include `"global"` in the allowed geos and set `default_inference_geo` to `"global"`. See [Workspace-level restrictions](#workspace-level-restrictions) for details.

### Pricing impact

Legacy models are unaffected by this migration. For current pricing on newer models, see [Pricing](#pricing).

## Current limitations

- **Shared rate limits**: Rate limits are shared across all geos.
- **Inference geo**: Only `"us"` and `"global"` are available at launch. Additional regions will be added over time.
- **Workspace geo**: Only `"us"` is currently available. Workspace geo can't be changed after workspace creation.

## Next steps

<CardGroup>
  <Card title="Pricing" icon="dollar-sign" href="/docs/en/about-claude/pricing#data-residency-pricing">
    View data residency pricing details.
  </Card>
  <Card title="Workspaces" icon="building" href="/docs/en/build-with-claude/workspaces">
    Learn about workspace configuration.
  </Card>
  <Card title="Usage and Cost API" icon="chart" href="/docs/en/build-with-claude/usage-cost-api">
    Track usage and costs by data residency.
  </Card>
</CardGroup>