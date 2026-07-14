# API Keys

## Get API Key

**get** `/v1/organizations/api_keys/{api_key_id}`

Get API Key

### Path Parameters

- `api_key_id: string`

  ID of the API key.

### Returns

- `APIKey object { id, created_at, created_by, 7 more }`

  - `id: string`

    ID of the API key.

  - `created_at: string`

    RFC 3339 datetime string indicating when the API Key was created.

  - `created_by: object { id, type }`

    The ID and type of the actor that created the API key.

    - `id: string`

      ID of the actor that created the object.

    - `type: string`

      Type of the actor that created the object.

  - `expires_at: string`

    RFC 3339 datetime string indicating when the API Key expires, or `null` if it never expires.

  - `name: string`

    Name of the API key.

  - `partial_key_hint: string`

    Partially redacted hint for the API key.

  - `principal: object { id, type }`

    The ID and type of the principal the API key acts as, or `null` if the key is not bound to a principal.

    - `id: string`

      ID of the principal the API key acts as: a User ID (`user_...`) when the type is `user`, or a Service Account ID (`svac_...`) when the type is `service_account`.

    - `type: "service_account" or "user"`

      Type of the principal the API key acts as.

      - `"service_account"`

      - `"user"`

  - `status: "active" or "archived" or "expired" or "inactive"`

    Status of the API key.

    - `"active"`

    - `"archived"`

    - `"expired"`

    - `"inactive"`

  - `type: "api_key"`

    Object type.

    For API Keys, this is always `"api_key"`.

    - `"api_key"`

  - `workspace_id: string`

    ID of the Workspace associated with the API key, or `null` if the API key belongs to the default Workspace.

### Example

```http
curl https://api.anthropic.com/v1/organizations/api_keys/$API_KEY_ID \
    -H 'anthropic-version: 2023-06-01' \
    -H "Authorization: Bearer $ANTHROPIC_OAUTH_TOKEN"
```

#### Response

```json
{
  "id": "apikey_01Rj2N8SVvo6BePZj99NhmiT",
  "created_at": "2024-10-30T23:58:27.427722Z",
  "created_by": {
    "id": "user_01WCz1FkmYMm4gnmykNKUu3Q",
    "type": "user"
  },
  "expires_at": "2024-10-30T23:58:27.427722Z",
  "name": "Developer Key",
  "partial_key_hint": "sk-ant-api03-R2D...igAA",
  "principal": {
    "id": "user_01WCz1FkmYMm4gnmykNKUu3Q",
    "type": "user"
  },
  "status": "active",
  "type": "api_key",
  "workspace_id": "wrkspc_01JwQvzr7rXLA5AGx3HKfFUJ"
}
```

## List API Keys

**get** `/v1/organizations/api_keys`

List API Keys

### Query Parameters

- `after_id: optional string`

  ID of the object to use as a cursor for pagination. When provided, returns the page of results immediately after this object.

- `before_id: optional string`

  ID of the object to use as a cursor for pagination. When provided, returns the page of results immediately before this object.

- `created_by_user_id: optional string`

  Filter by the ID of the User who created the object.

- `limit: optional number`

  Number of items to return per page.

  Defaults to `20`. Ranges from `1` to `1000`.

- `status: optional "active" or "archived" or "expired" or "inactive"`

  Filter by API key status.

  - `"active"`

  - `"archived"`

  - `"expired"`

  - `"inactive"`

- `workspace_id: optional string`

  Filter by Workspace ID.

### Returns

- `data: array of APIKey`

  - `id: string`

    ID of the API key.

  - `created_at: string`

    RFC 3339 datetime string indicating when the API Key was created.

  - `created_by: object { id, type }`

    The ID and type of the actor that created the API key.

    - `id: string`

      ID of the actor that created the object.

    - `type: string`

      Type of the actor that created the object.

  - `expires_at: string`

    RFC 3339 datetime string indicating when the API Key expires, or `null` if it never expires.

  - `name: string`

    Name of the API key.

  - `partial_key_hint: string`

    Partially redacted hint for the API key.

  - `principal: object { id, type }`

    The ID and type of the principal the API key acts as, or `null` if the key is not bound to a principal.

    - `id: string`

      ID of the principal the API key acts as: a User ID (`user_...`) when the type is `user`, or a Service Account ID (`svac_...`) when the type is `service_account`.

    - `type: "service_account" or "user"`

      Type of the principal the API key acts as.

      - `"service_account"`

      - `"user"`

  - `status: "active" or "archived" or "expired" or "inactive"`

    Status of the API key.

    - `"active"`

    - `"archived"`

    - `"expired"`

    - `"inactive"`

  - `type: "api_key"`

    Object type.

    For API Keys, this is always `"api_key"`.

    - `"api_key"`

  - `workspace_id: string`

    ID of the Workspace associated with the API key, or `null` if the API key belongs to the default Workspace.

- `first_id: string`

  First ID in the `data` list. Can be used as the `before_id` for the previous page.

- `has_more: boolean`

  Indicates if there are more results in the requested page direction.

- `last_id: string`

  Last ID in the `data` list. Can be used as the `after_id` for the next page.

### Example

```http
curl https://api.anthropic.com/v1/organizations/api_keys \
    -H 'anthropic-version: 2023-06-01' \
    -H "Authorization: Bearer $ANTHROPIC_OAUTH_TOKEN"
```

#### Response

```json
{
  "data": [
    {
      "id": "apikey_01Rj2N8SVvo6BePZj99NhmiT",
      "created_at": "2024-10-30T23:58:27.427722Z",
      "created_by": {
        "id": "user_01WCz1FkmYMm4gnmykNKUu3Q",
        "type": "user"
      },
      "expires_at": "2024-10-30T23:58:27.427722Z",
      "name": "Developer Key",
      "partial_key_hint": "sk-ant-api03-R2D...igAA",
      "principal": {
        "id": "user_01WCz1FkmYMm4gnmykNKUu3Q",
        "type": "user"
      },
      "status": "active",
      "type": "api_key",
      "workspace_id": "wrkspc_01JwQvzr7rXLA5AGx3HKfFUJ"
    }
  ],
  "first_id": "first_id",
  "has_more": true,
  "last_id": "last_id"
}
```

## Update API Key

**post** `/v1/organizations/api_keys/{api_key_id}`

Update API Key

### Path Parameters

- `api_key_id: string`

  ID of the API key.

### Body Parameters

- `name: optional string`

  Name of the API key.

- `status: optional "active" or "archived" or "inactive"`

  Status of the API key.

  - `"active"`

  - `"archived"`

  - `"inactive"`

### Returns

- `APIKey object { id, created_at, created_by, 7 more }`

  - `id: string`

    ID of the API key.

  - `created_at: string`

    RFC 3339 datetime string indicating when the API Key was created.

  - `created_by: object { id, type }`

    The ID and type of the actor that created the API key.

    - `id: string`

      ID of the actor that created the object.

    - `type: string`

      Type of the actor that created the object.

  - `expires_at: string`

    RFC 3339 datetime string indicating when the API Key expires, or `null` if it never expires.

  - `name: string`

    Name of the API key.

  - `partial_key_hint: string`

    Partially redacted hint for the API key.

  - `principal: object { id, type }`

    The ID and type of the principal the API key acts as, or `null` if the key is not bound to a principal.

    - `id: string`

      ID of the principal the API key acts as: a User ID (`user_...`) when the type is `user`, or a Service Account ID (`svac_...`) when the type is `service_account`.

    - `type: "service_account" or "user"`

      Type of the principal the API key acts as.

      - `"service_account"`

      - `"user"`

  - `status: "active" or "archived" or "expired" or "inactive"`

    Status of the API key.

    - `"active"`

    - `"archived"`

    - `"expired"`

    - `"inactive"`

  - `type: "api_key"`

    Object type.

    For API Keys, this is always `"api_key"`.

    - `"api_key"`

  - `workspace_id: string`

    ID of the Workspace associated with the API key, or `null` if the API key belongs to the default Workspace.

### Example

```http
curl https://api.anthropic.com/v1/organizations/api_keys/$API_KEY_ID \
    -H 'Content-Type: application/json' \
    -H 'anthropic-version: 2023-06-01' \
    -H "Authorization: Bearer $ANTHROPIC_OAUTH_TOKEN" \
    -d '{}'
```

#### Response

```json
{
  "id": "apikey_01Rj2N8SVvo6BePZj99NhmiT",
  "created_at": "2024-10-30T23:58:27.427722Z",
  "created_by": {
    "id": "user_01WCz1FkmYMm4gnmykNKUu3Q",
    "type": "user"
  },
  "expires_at": "2024-10-30T23:58:27.427722Z",
  "name": "Developer Key",
  "partial_key_hint": "sk-ant-api03-R2D...igAA",
  "principal": {
    "id": "user_01WCz1FkmYMm4gnmykNKUu3Q",
    "type": "user"
  },
  "status": "active",
  "type": "api_key",
  "workspace_id": "wrkspc_01JwQvzr7rXLA5AGx3HKfFUJ"
}
```
