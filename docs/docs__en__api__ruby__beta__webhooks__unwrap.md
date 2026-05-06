## Unwrap

`beta.webhooks.unwrap() -> void`

**** ``

### Example

```ruby
require "anthropic"

anthropic = Anthropic::Client.new(api_key: "my-anthropic-api-key")

result = anthropic.beta.webhooks.unwrap

puts(result)
```
