## Unwrap

`beta.webhooks.unwrap()`

**** ``

### Example

```python
import os
from anthropic import Anthropic

client = Anthropic(
    api_key=os.environ.get("ANTHROPIC_API_KEY"),  # This is the default and can be omitted
)
client.beta.webhooks.unwrap()
```
