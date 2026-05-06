# Webhooks

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

## Domain Types

### Beta Webhook Event

- `class BetaWebhookEvent`

  - `id: String`

    Unique event identifier for idempotency.

  - `created_at: Time`

    RFC 3339 timestamp when the event occurred.

  - `data: BetaWebhookEventData`

    - `class BetaWebhookSessionCreatedEventData`

      - `id: String`

        ID of the resource that triggered the event.

      - `organization_id: String`

      - `type: :"session.created"`

        - `:"session.created"`

      - `workspace_id: String`

    - `class BetaWebhookSessionPendingEventData`

      - `id: String`

        ID of the resource that triggered the event.

      - `organization_id: String`

      - `type: :"session.pending"`

        - `:"session.pending"`

      - `workspace_id: String`

    - `class BetaWebhookSessionRunningEventData`

      - `id: String`

        ID of the resource that triggered the event.

      - `organization_id: String`

      - `type: :"session.running"`

        - `:"session.running"`

      - `workspace_id: String`

    - `class BetaWebhookSessionIdledEventData`

      - `id: String`

        ID of the resource that triggered the event.

      - `organization_id: String`

      - `type: :"session.idled"`

        - `:"session.idled"`

      - `workspace_id: String`

    - `class BetaWebhookSessionRequiresActionEventData`

      - `id: String`

        ID of the resource that triggered the event.

      - `organization_id: String`

      - `type: :"session.requires_action"`

        - `:"session.requires_action"`

      - `workspace_id: String`

    - `class BetaWebhookSessionArchivedEventData`

      - `id: String`

        ID of the resource that triggered the event.

      - `organization_id: String`

      - `type: :"session.archived"`

        - `:"session.archived"`

      - `workspace_id: String`

    - `class BetaWebhookSessionDeletedEventData`

      - `id: String`

        ID of the resource that triggered the event.

      - `organization_id: String`

      - `type: :"session.deleted"`

        - `:"session.deleted"`

      - `workspace_id: String`

    - `class BetaWebhookSessionStatusScheduledEventData`

      - `id: String`

        ID of the resource that triggered the event.

      - `organization_id: String`

      - `type: :"session.status_scheduled"`

        - `:"session.status_scheduled"`

      - `workspace_id: String`

    - `class BetaWebhookSessionStatusRunStartedEventData`

      - `id: String`

        ID of the resource that triggered the event.

      - `organization_id: String`

      - `type: :"session.status_run_started"`

        - `:"session.status_run_started"`

      - `workspace_id: String`

    - `class BetaWebhookSessionStatusIdledEventData`

      - `id: String`

        ID of the resource that triggered the event.

      - `organization_id: String`

      - `type: :"session.status_idled"`

        - `:"session.status_idled"`

      - `workspace_id: String`

    - `class BetaWebhookSessionStatusTerminatedEventData`

      - `id: String`

        ID of the resource that triggered the event.

      - `organization_id: String`

      - `type: :"session.status_terminated"`

        - `:"session.status_terminated"`

      - `workspace_id: String`

    - `class BetaWebhookSessionThreadCreatedEventData`

      - `id: String`

        ID of the resource that triggered the event.

      - `organization_id: String`

      - `type: :"session.thread_created"`

        - `:"session.thread_created"`

      - `workspace_id: String`

    - `class BetaWebhookSessionThreadIdledEventData`

      - `id: String`

        ID of the resource that triggered the event.

      - `organization_id: String`

      - `type: :"session.thread_idled"`

        - `:"session.thread_idled"`

      - `workspace_id: String`

    - `class BetaWebhookSessionThreadTerminatedEventData`

      - `id: String`

        ID of the resource that triggered the event.

      - `organization_id: String`

      - `type: :"session.thread_terminated"`

        - `:"session.thread_terminated"`

      - `workspace_id: String`

    - `class BetaWebhookSessionOutcomeEvaluationEndedEventData`

      - `id: String`

        ID of the resource that triggered the event.

      - `organization_id: String`

      - `type: :"session.outcome_evaluation_ended"`

        - `:"session.outcome_evaluation_ended"`

      - `workspace_id: String`

    - `class BetaWebhookVaultCreatedEventData`

      - `id: String`

        ID of the resource that triggered the event.

      - `organization_id: String`

      - `type: :"vault.created"`

        - `:"vault.created"`

      - `workspace_id: String`

    - `class BetaWebhookVaultArchivedEventData`

      - `id: String`

        ID of the resource that triggered the event.

      - `organization_id: String`

      - `type: :"vault.archived"`

        - `:"vault.archived"`

      - `workspace_id: String`

    - `class BetaWebhookVaultDeletedEventData`

      - `id: String`

        ID of the resource that triggered the event.

      - `organization_id: String`

      - `type: :"vault.deleted"`

        - `:"vault.deleted"`

      - `workspace_id: String`

    - `class BetaWebhookVaultCredentialCreatedEventData`

      - `id: String`

        ID of the resource that triggered the event.

      - `organization_id: String`

      - `type: :"vault_credential.created"`

        - `:"vault_credential.created"`

      - `vault_id: String`

        ID of the vault that owns this credential.

      - `workspace_id: String`

    - `class BetaWebhookVaultCredentialArchivedEventData`

      - `id: String`

        ID of the resource that triggered the event.

      - `organization_id: String`

      - `type: :"vault_credential.archived"`

        - `:"vault_credential.archived"`

      - `vault_id: String`

        ID of the vault that owns this credential.

      - `workspace_id: String`

    - `class BetaWebhookVaultCredentialDeletedEventData`

      - `id: String`

        ID of the resource that triggered the event.

      - `organization_id: String`

      - `type: :"vault_credential.deleted"`

        - `:"vault_credential.deleted"`

      - `vault_id: String`

        ID of the vault that owns this credential.

      - `workspace_id: String`

    - `class BetaWebhookVaultCredentialRefreshFailedEventData`

      - `id: String`

        ID of the resource that triggered the event.

      - `organization_id: String`

      - `type: :"vault_credential.refresh_failed"`

        - `:"vault_credential.refresh_failed"`

      - `vault_id: String`

        ID of the vault that owns this credential.

      - `workspace_id: String`

  - `type: :event`

    Object type. Always `event` for webhook payloads.

    - `:event`

### Beta Webhook Event Data

- `BetaWebhookEventData = BetaWebhookSessionCreatedEventData | BetaWebhookSessionPendingEventData | BetaWebhookSessionRunningEventData | 19 more`

  - `class BetaWebhookSessionCreatedEventData`

    - `id: String`

      ID of the resource that triggered the event.

    - `organization_id: String`

    - `type: :"session.created"`

      - `:"session.created"`

    - `workspace_id: String`

  - `class BetaWebhookSessionPendingEventData`

    - `id: String`

      ID of the resource that triggered the event.

    - `organization_id: String`

    - `type: :"session.pending"`

      - `:"session.pending"`

    - `workspace_id: String`

  - `class BetaWebhookSessionRunningEventData`

    - `id: String`

      ID of the resource that triggered the event.

    - `organization_id: String`

    - `type: :"session.running"`

      - `:"session.running"`

    - `workspace_id: String`

  - `class BetaWebhookSessionIdledEventData`

    - `id: String`

      ID of the resource that triggered the event.

    - `organization_id: String`

    - `type: :"session.idled"`

      - `:"session.idled"`

    - `workspace_id: String`

  - `class BetaWebhookSessionRequiresActionEventData`

    - `id: String`

      ID of the resource that triggered the event.

    - `organization_id: String`

    - `type: :"session.requires_action"`

      - `:"session.requires_action"`

    - `workspace_id: String`

  - `class BetaWebhookSessionArchivedEventData`

    - `id: String`

      ID of the resource that triggered the event.

    - `organization_id: String`

    - `type: :"session.archived"`

      - `:"session.archived"`

    - `workspace_id: String`

  - `class BetaWebhookSessionDeletedEventData`

    - `id: String`

      ID of the resource that triggered the event.

    - `organization_id: String`

    - `type: :"session.deleted"`

      - `:"session.deleted"`

    - `workspace_id: String`

  - `class BetaWebhookSessionStatusScheduledEventData`

    - `id: String`

      ID of the resource that triggered the event.

    - `organization_id: String`

    - `type: :"session.status_scheduled"`

      - `:"session.status_scheduled"`

    - `workspace_id: String`

  - `class BetaWebhookSessionStatusRunStartedEventData`

    - `id: String`

      ID of the resource that triggered the event.

    - `organization_id: String`

    - `type: :"session.status_run_started"`

      - `:"session.status_run_started"`

    - `workspace_id: String`

  - `class BetaWebhookSessionStatusIdledEventData`

    - `id: String`

      ID of the resource that triggered the event.

    - `organization_id: String`

    - `type: :"session.status_idled"`

      - `:"session.status_idled"`

    - `workspace_id: String`

  - `class BetaWebhookSessionStatusTerminatedEventData`

    - `id: String`

      ID of the resource that triggered the event.

    - `organization_id: String`

    - `type: :"session.status_terminated"`

      - `:"session.status_terminated"`

    - `workspace_id: String`

  - `class BetaWebhookSessionThreadCreatedEventData`

    - `id: String`

      ID of the resource that triggered the event.

    - `organization_id: String`

    - `type: :"session.thread_created"`

      - `:"session.thread_created"`

    - `workspace_id: String`

  - `class BetaWebhookSessionThreadIdledEventData`

    - `id: String`

      ID of the resource that triggered the event.

    - `organization_id: String`

    - `type: :"session.thread_idled"`

      - `:"session.thread_idled"`

    - `workspace_id: String`

  - `class BetaWebhookSessionThreadTerminatedEventData`

    - `id: String`

      ID of the resource that triggered the event.

    - `organization_id: String`

    - `type: :"session.thread_terminated"`

      - `:"session.thread_terminated"`

    - `workspace_id: String`

  - `class BetaWebhookSessionOutcomeEvaluationEndedEventData`

    - `id: String`

      ID of the resource that triggered the event.

    - `organization_id: String`

    - `type: :"session.outcome_evaluation_ended"`

      - `:"session.outcome_evaluation_ended"`

    - `workspace_id: String`

  - `class BetaWebhookVaultCreatedEventData`

    - `id: String`

      ID of the resource that triggered the event.

    - `organization_id: String`

    - `type: :"vault.created"`

      - `:"vault.created"`

    - `workspace_id: String`

  - `class BetaWebhookVaultArchivedEventData`

    - `id: String`

      ID of the resource that triggered the event.

    - `organization_id: String`

    - `type: :"vault.archived"`

      - `:"vault.archived"`

    - `workspace_id: String`

  - `class BetaWebhookVaultDeletedEventData`

    - `id: String`

      ID of the resource that triggered the event.

    - `organization_id: String`

    - `type: :"vault.deleted"`

      - `:"vault.deleted"`

    - `workspace_id: String`

  - `class BetaWebhookVaultCredentialCreatedEventData`

    - `id: String`

      ID of the resource that triggered the event.

    - `organization_id: String`

    - `type: :"vault_credential.created"`

      - `:"vault_credential.created"`

    - `vault_id: String`

      ID of the vault that owns this credential.

    - `workspace_id: String`

  - `class BetaWebhookVaultCredentialArchivedEventData`

    - `id: String`

      ID of the resource that triggered the event.

    - `organization_id: String`

    - `type: :"vault_credential.archived"`

      - `:"vault_credential.archived"`

    - `vault_id: String`

      ID of the vault that owns this credential.

    - `workspace_id: String`

  - `class BetaWebhookVaultCredentialDeletedEventData`

    - `id: String`

      ID of the resource that triggered the event.

    - `organization_id: String`

    - `type: :"vault_credential.deleted"`

      - `:"vault_credential.deleted"`

    - `vault_id: String`

      ID of the vault that owns this credential.

    - `workspace_id: String`

  - `class BetaWebhookVaultCredentialRefreshFailedEventData`

    - `id: String`

      ID of the resource that triggered the event.

    - `organization_id: String`

    - `type: :"vault_credential.refresh_failed"`

      - `:"vault_credential.refresh_failed"`

    - `vault_id: String`

      ID of the vault that owns this credential.

    - `workspace_id: String`

### Beta Webhook Session Archived Event Data

- `class BetaWebhookSessionArchivedEventData`

  - `id: String`

    ID of the resource that triggered the event.

  - `organization_id: String`

  - `type: :"session.archived"`

    - `:"session.archived"`

  - `workspace_id: String`

### Beta Webhook Session Created Event Data

- `class BetaWebhookSessionCreatedEventData`

  - `id: String`

    ID of the resource that triggered the event.

  - `organization_id: String`

  - `type: :"session.created"`

    - `:"session.created"`

  - `workspace_id: String`

### Beta Webhook Session Deleted Event Data

- `class BetaWebhookSessionDeletedEventData`

  - `id: String`

    ID of the resource that triggered the event.

  - `organization_id: String`

  - `type: :"session.deleted"`

    - `:"session.deleted"`

  - `workspace_id: String`

### Beta Webhook Session Idled Event Data

- `class BetaWebhookSessionIdledEventData`

  - `id: String`

    ID of the resource that triggered the event.

  - `organization_id: String`

  - `type: :"session.idled"`

    - `:"session.idled"`

  - `workspace_id: String`

### Beta Webhook Session Outcome Evaluation Ended Event Data

- `class BetaWebhookSessionOutcomeEvaluationEndedEventData`

  - `id: String`

    ID of the resource that triggered the event.

  - `organization_id: String`

  - `type: :"session.outcome_evaluation_ended"`

    - `:"session.outcome_evaluation_ended"`

  - `workspace_id: String`

### Beta Webhook Session Pending Event Data

- `class BetaWebhookSessionPendingEventData`

  - `id: String`

    ID of the resource that triggered the event.

  - `organization_id: String`

  - `type: :"session.pending"`

    - `:"session.pending"`

  - `workspace_id: String`

### Beta Webhook Session Requires Action Event Data

- `class BetaWebhookSessionRequiresActionEventData`

  - `id: String`

    ID of the resource that triggered the event.

  - `organization_id: String`

  - `type: :"session.requires_action"`

    - `:"session.requires_action"`

  - `workspace_id: String`

### Beta Webhook Session Running Event Data

- `class BetaWebhookSessionRunningEventData`

  - `id: String`

    ID of the resource that triggered the event.

  - `organization_id: String`

  - `type: :"session.running"`

    - `:"session.running"`

  - `workspace_id: String`

### Beta Webhook Session Status Idled Event Data

- `class BetaWebhookSessionStatusIdledEventData`

  - `id: String`

    ID of the resource that triggered the event.

  - `organization_id: String`

  - `type: :"session.status_idled"`

    - `:"session.status_idled"`

  - `workspace_id: String`

### Beta Webhook Session Status Run Started Event Data

- `class BetaWebhookSessionStatusRunStartedEventData`

  - `id: String`

    ID of the resource that triggered the event.

  - `organization_id: String`

  - `type: :"session.status_run_started"`

    - `:"session.status_run_started"`

  - `workspace_id: String`

### Beta Webhook Session Status Scheduled Event Data

- `class BetaWebhookSessionStatusScheduledEventData`

  - `id: String`

    ID of the resource that triggered the event.

  - `organization_id: String`

  - `type: :"session.status_scheduled"`

    - `:"session.status_scheduled"`

  - `workspace_id: String`

### Beta Webhook Session Status Terminated Event Data

- `class BetaWebhookSessionStatusTerminatedEventData`

  - `id: String`

    ID of the resource that triggered the event.

  - `organization_id: String`

  - `type: :"session.status_terminated"`

    - `:"session.status_terminated"`

  - `workspace_id: String`

### Beta Webhook Session Thread Created Event Data

- `class BetaWebhookSessionThreadCreatedEventData`

  - `id: String`

    ID of the resource that triggered the event.

  - `organization_id: String`

  - `type: :"session.thread_created"`

    - `:"session.thread_created"`

  - `workspace_id: String`

### Beta Webhook Session Thread Idled Event Data

- `class BetaWebhookSessionThreadIdledEventData`

  - `id: String`

    ID of the resource that triggered the event.

  - `organization_id: String`

  - `type: :"session.thread_idled"`

    - `:"session.thread_idled"`

  - `workspace_id: String`

### Beta Webhook Session Thread Terminated Event Data

- `class BetaWebhookSessionThreadTerminatedEventData`

  - `id: String`

    ID of the resource that triggered the event.

  - `organization_id: String`

  - `type: :"session.thread_terminated"`

    - `:"session.thread_terminated"`

  - `workspace_id: String`

### Beta Webhook Vault Archived Event Data

- `class BetaWebhookVaultArchivedEventData`

  - `id: String`

    ID of the resource that triggered the event.

  - `organization_id: String`

  - `type: :"vault.archived"`

    - `:"vault.archived"`

  - `workspace_id: String`

### Beta Webhook Vault Created Event Data

- `class BetaWebhookVaultCreatedEventData`

  - `id: String`

    ID of the resource that triggered the event.

  - `organization_id: String`

  - `type: :"vault.created"`

    - `:"vault.created"`

  - `workspace_id: String`

### Beta Webhook Vault Credential Archived Event Data

- `class BetaWebhookVaultCredentialArchivedEventData`

  - `id: String`

    ID of the resource that triggered the event.

  - `organization_id: String`

  - `type: :"vault_credential.archived"`

    - `:"vault_credential.archived"`

  - `vault_id: String`

    ID of the vault that owns this credential.

  - `workspace_id: String`

### Beta Webhook Vault Credential Created Event Data

- `class BetaWebhookVaultCredentialCreatedEventData`

  - `id: String`

    ID of the resource that triggered the event.

  - `organization_id: String`

  - `type: :"vault_credential.created"`

    - `:"vault_credential.created"`

  - `vault_id: String`

    ID of the vault that owns this credential.

  - `workspace_id: String`

### Beta Webhook Vault Credential Deleted Event Data

- `class BetaWebhookVaultCredentialDeletedEventData`

  - `id: String`

    ID of the resource that triggered the event.

  - `organization_id: String`

  - `type: :"vault_credential.deleted"`

    - `:"vault_credential.deleted"`

  - `vault_id: String`

    ID of the vault that owns this credential.

  - `workspace_id: String`

### Beta Webhook Vault Credential Refresh Failed Event Data

- `class BetaWebhookVaultCredentialRefreshFailedEventData`

  - `id: String`

    ID of the resource that triggered the event.

  - `organization_id: String`

  - `type: :"vault_credential.refresh_failed"`

    - `:"vault_credential.refresh_failed"`

  - `vault_id: String`

    ID of the vault that owns this credential.

  - `workspace_id: String`

### Beta Webhook Vault Deleted Event Data

- `class BetaWebhookVaultDeletedEventData`

  - `id: String`

    ID of the resource that triggered the event.

  - `organization_id: String`

  - `type: :"vault.deleted"`

    - `:"vault.deleted"`

  - `workspace_id: String`

### Unwrap Webhook Event

- `class UnwrapWebhookEvent`

  - `id: String`

    Unique event identifier for idempotency.

  - `created_at: Time`

    RFC 3339 timestamp when the event occurred.

  - `data: BetaWebhookEventData`

    - `class BetaWebhookSessionCreatedEventData`

      - `id: String`

        ID of the resource that triggered the event.

      - `organization_id: String`

      - `type: :"session.created"`

        - `:"session.created"`

      - `workspace_id: String`

    - `class BetaWebhookSessionPendingEventData`

      - `id: String`

        ID of the resource that triggered the event.

      - `organization_id: String`

      - `type: :"session.pending"`

        - `:"session.pending"`

      - `workspace_id: String`

    - `class BetaWebhookSessionRunningEventData`

      - `id: String`

        ID of the resource that triggered the event.

      - `organization_id: String`

      - `type: :"session.running"`

        - `:"session.running"`

      - `workspace_id: String`

    - `class BetaWebhookSessionIdledEventData`

      - `id: String`

        ID of the resource that triggered the event.

      - `organization_id: String`

      - `type: :"session.idled"`

        - `:"session.idled"`

      - `workspace_id: String`

    - `class BetaWebhookSessionRequiresActionEventData`

      - `id: String`

        ID of the resource that triggered the event.

      - `organization_id: String`

      - `type: :"session.requires_action"`

        - `:"session.requires_action"`

      - `workspace_id: String`

    - `class BetaWebhookSessionArchivedEventData`

      - `id: String`

        ID of the resource that triggered the event.

      - `organization_id: String`

      - `type: :"session.archived"`

        - `:"session.archived"`

      - `workspace_id: String`

    - `class BetaWebhookSessionDeletedEventData`

      - `id: String`

        ID of the resource that triggered the event.

      - `organization_id: String`

      - `type: :"session.deleted"`

        - `:"session.deleted"`

      - `workspace_id: String`

    - `class BetaWebhookSessionStatusScheduledEventData`

      - `id: String`

        ID of the resource that triggered the event.

      - `organization_id: String`

      - `type: :"session.status_scheduled"`

        - `:"session.status_scheduled"`

      - `workspace_id: String`

    - `class BetaWebhookSessionStatusRunStartedEventData`

      - `id: String`

        ID of the resource that triggered the event.

      - `organization_id: String`

      - `type: :"session.status_run_started"`

        - `:"session.status_run_started"`

      - `workspace_id: String`

    - `class BetaWebhookSessionStatusIdledEventData`

      - `id: String`

        ID of the resource that triggered the event.

      - `organization_id: String`

      - `type: :"session.status_idled"`

        - `:"session.status_idled"`

      - `workspace_id: String`

    - `class BetaWebhookSessionStatusTerminatedEventData`

      - `id: String`

        ID of the resource that triggered the event.

      - `organization_id: String`

      - `type: :"session.status_terminated"`

        - `:"session.status_terminated"`

      - `workspace_id: String`

    - `class BetaWebhookSessionThreadCreatedEventData`

      - `id: String`

        ID of the resource that triggered the event.

      - `organization_id: String`

      - `type: :"session.thread_created"`

        - `:"session.thread_created"`

      - `workspace_id: String`

    - `class BetaWebhookSessionThreadIdledEventData`

      - `id: String`

        ID of the resource that triggered the event.

      - `organization_id: String`

      - `type: :"session.thread_idled"`

        - `:"session.thread_idled"`

      - `workspace_id: String`

    - `class BetaWebhookSessionThreadTerminatedEventData`

      - `id: String`

        ID of the resource that triggered the event.

      - `organization_id: String`

      - `type: :"session.thread_terminated"`

        - `:"session.thread_terminated"`

      - `workspace_id: String`

    - `class BetaWebhookSessionOutcomeEvaluationEndedEventData`

      - `id: String`

        ID of the resource that triggered the event.

      - `organization_id: String`

      - `type: :"session.outcome_evaluation_ended"`

        - `:"session.outcome_evaluation_ended"`

      - `workspace_id: String`

    - `class BetaWebhookVaultCreatedEventData`

      - `id: String`

        ID of the resource that triggered the event.

      - `organization_id: String`

      - `type: :"vault.created"`

        - `:"vault.created"`

      - `workspace_id: String`

    - `class BetaWebhookVaultArchivedEventData`

      - `id: String`

        ID of the resource that triggered the event.

      - `organization_id: String`

      - `type: :"vault.archived"`

        - `:"vault.archived"`

      - `workspace_id: String`

    - `class BetaWebhookVaultDeletedEventData`

      - `id: String`

        ID of the resource that triggered the event.

      - `organization_id: String`

      - `type: :"vault.deleted"`

        - `:"vault.deleted"`

      - `workspace_id: String`

    - `class BetaWebhookVaultCredentialCreatedEventData`

      - `id: String`

        ID of the resource that triggered the event.

      - `organization_id: String`

      - `type: :"vault_credential.created"`

        - `:"vault_credential.created"`

      - `vault_id: String`

        ID of the vault that owns this credential.

      - `workspace_id: String`

    - `class BetaWebhookVaultCredentialArchivedEventData`

      - `id: String`

        ID of the resource that triggered the event.

      - `organization_id: String`

      - `type: :"vault_credential.archived"`

        - `:"vault_credential.archived"`

      - `vault_id: String`

        ID of the vault that owns this credential.

      - `workspace_id: String`

    - `class BetaWebhookVaultCredentialDeletedEventData`

      - `id: String`

        ID of the resource that triggered the event.

      - `organization_id: String`

      - `type: :"vault_credential.deleted"`

        - `:"vault_credential.deleted"`

      - `vault_id: String`

        ID of the vault that owns this credential.

      - `workspace_id: String`

    - `class BetaWebhookVaultCredentialRefreshFailedEventData`

      - `id: String`

        ID of the resource that triggered the event.

      - `organization_id: String`

      - `type: :"vault_credential.refresh_failed"`

        - `:"vault_credential.refresh_failed"`

      - `vault_id: String`

        ID of the vault that owns this credential.

      - `workspace_id: String`

  - `type: :event`

    Object type. Always `event` for webhook payloads.

    - `:event`
