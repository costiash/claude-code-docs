## Unwrap

`client.beta.webhooks.unwrap(RequestOptionsoptions?): void`

**** ``

### Example

```typescript
import Anthropic from '@anthropic-ai/sdk';

const client = new Anthropic({
  apiKey: process.env['ANTHROPIC_API_KEY'], // This is the default and can be omitted
});

await client.beta.webhooks.unwrap();
```
