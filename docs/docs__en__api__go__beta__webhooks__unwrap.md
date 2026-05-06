## Unwrap

`client.Beta.Webhooks.Unwrap(ctx) error`

**** ``

### Example

```go
package main

import (
  "context"

  "github.com/anthropics/anthropic-sdk-go"
  "github.com/anthropics/anthropic-sdk-go/option"
)

func main() {
  client := anthropic.NewClient(
    option.WithAPIKey("my-anthropic-api-key"),
  )
  err := client.Beta.Webhooks.Unwrap(context.TODO())
  if err != nil {
    panic(err.Error())
  }
}
```
