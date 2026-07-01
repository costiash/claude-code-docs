## List Service Accounts

**get** `/v1/organizations/service_accounts`

List service accounts in the caller's organization.

Results are ordered by creation time, newest first. Use `limit` and the
`next_page` cursor to paginate; set `include_archived=true` to include
archived service accounts.

### Query Parameters

- `include_archived: optional boolean`

  Include archived resources. Defaults to false.

- `limit: optional number`

  Number of results per page.

- `page: optional string`

  Opaque cursor from a previous response's `next_page`.

### Header Parameters

- `"anthropic-beta": optional array of string`

  Optional header to specify the beta version(s) you want to use.

  To use multiple betas, use a comma separated list like `beta1,beta2` or specify the header multiple times for each beta.

### Returns

- `data: array of ServiceAccount`

  - `id: string`

    Tagged ID of the service account.

  - `archived_at: string`

    If set, this service account is archived.

  - `archived_by_actor_id: string`

    Tagged ID (`user_`/`svac_`) of the actor that archived this service account.

  - `created_at: string`

    When this service account was created.

  - `created_by_actor_id: string`

    Tagged ID (`user_`/`svac_`) of the actor that created this service account.

  - `description: string`

    Optional free-text description.

  - `name: string`

    Admin-chosen slug identifier.

  - `organization_role: "admin" or "developer"`

    Org-level role. A federation rule may only be created or retargeted to grant `org:admin` scope when this is `admin`. A rule granting `org:admin` whose target is later demoted to `developer` is rejected at token exchange. Rules granting `org:admin` are managed in the Console.

    - `"admin"`

    - `"developer"`

  - `type: "service_account"`

    - `"service_account"`

  - `updated_at: string`

    When this service account was last updated.

  - `updated_by_actor_id: string`

    Tagged ID (`user_`/`svac_`) of the actor that last updated this service account.

- `next_page: string`

  Opaque cursor for the next page, or null if no more results.

### Example

```http
curl https://api.anthropic.com/v1/organizations/service_accounts \
    -H 'anthropic-version: 2023-06-01' \
    -H "Authorization: Bearer $ANTHROPIC_OAUTH_TOKEN"
```

#### Response

```json
{
  "data": [
    {
      "id": "svac_01SDCCSbTxrXDpWc1phhtcfK",
      "archived_at": "2019-12-27T18:11:19.117Z",
      "archived_by_actor_id": "archived_by_actor_id",
      "created_at": "2024-10-30T23:58:27.427722Z",
      "created_by_actor_id": "created_by_actor_id",
      "description": "description",
      "name": "ci-deploy-bot",
      "organization_role": "admin",
      "type": "service_account",
      "updated_at": "2024-10-30T23:58:27.427722Z",
      "updated_by_actor_id": "updated_by_actor_id"
    }
  ],
  "next_page": "next_page"
}
```
