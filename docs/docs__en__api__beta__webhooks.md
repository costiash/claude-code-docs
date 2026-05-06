# Webhooks

## Unwrap

**** ``

## Domain Types

### Beta Webhook Event

- `BetaWebhookEvent = object { id, created_at, data, type }`

  - `id: string`

    Unique event identifier for idempotency.

  - `created_at: string`

    RFC 3339 timestamp when the event occurred.

  - `data: BetaWebhookEventData`

    - `BetaWebhookSessionCreatedEventData = object { id, organization_id, type, workspace_id }`

      - `id: string`

        ID of the resource that triggered the event.

      - `organization_id: string`

      - `type: "session.created"`

        - `"session.created"`

      - `workspace_id: string`

    - `BetaWebhookSessionPendingEventData = object { id, organization_id, type, workspace_id }`

      - `id: string`

        ID of the resource that triggered the event.

      - `organization_id: string`

      - `type: "session.pending"`

        - `"session.pending"`

      - `workspace_id: string`

    - `BetaWebhookSessionRunningEventData = object { id, organization_id, type, workspace_id }`

      - `id: string`

        ID of the resource that triggered the event.

      - `organization_id: string`

      - `type: "session.running"`

        - `"session.running"`

      - `workspace_id: string`

    - `BetaWebhookSessionIdledEventData = object { id, organization_id, type, workspace_id }`

      - `id: string`

        ID of the resource that triggered the event.

      - `organization_id: string`

      - `type: "session.idled"`

        - `"session.idled"`

      - `workspace_id: string`

    - `BetaWebhookSessionRequiresActionEventData = object { id, organization_id, type, workspace_id }`

      - `id: string`

        ID of the resource that triggered the event.

      - `organization_id: string`

      - `type: "session.requires_action"`

        - `"session.requires_action"`

      - `workspace_id: string`

    - `BetaWebhookSessionArchivedEventData = object { id, organization_id, type, workspace_id }`

      - `id: string`

        ID of the resource that triggered the event.

      - `organization_id: string`

      - `type: "session.archived"`

        - `"session.archived"`

      - `workspace_id: string`

    - `BetaWebhookSessionDeletedEventData = object { id, organization_id, type, workspace_id }`

      - `id: string`

        ID of the resource that triggered the event.

      - `organization_id: string`

      - `type: "session.deleted"`

        - `"session.deleted"`

      - `workspace_id: string`

    - `BetaWebhookSessionStatusScheduledEventData = object { id, organization_id, type, workspace_id }`

      - `id: string`

        ID of the resource that triggered the event.

      - `organization_id: string`

      - `type: "session.status_scheduled"`

        - `"session.status_scheduled"`

      - `workspace_id: string`

    - `BetaWebhookSessionStatusRunStartedEventData = object { id, organization_id, type, workspace_id }`

      - `id: string`

        ID of the resource that triggered the event.

      - `organization_id: string`

      - `type: "session.status_run_started"`

        - `"session.status_run_started"`

      - `workspace_id: string`

    - `BetaWebhookSessionStatusIdledEventData = object { id, organization_id, type, workspace_id }`

      - `id: string`

        ID of the resource that triggered the event.

      - `organization_id: string`

      - `type: "session.status_idled"`

        - `"session.status_idled"`

      - `workspace_id: string`

    - `BetaWebhookSessionStatusTerminatedEventData = object { id, organization_id, type, workspace_id }`

      - `id: string`

        ID of the resource that triggered the event.

      - `organization_id: string`

      - `type: "session.status_terminated"`

        - `"session.status_terminated"`

      - `workspace_id: string`

    - `BetaWebhookSessionThreadCreatedEventData = object { id, organization_id, type, workspace_id }`

      - `id: string`

        ID of the resource that triggered the event.

      - `organization_id: string`

      - `type: "session.thread_created"`

        - `"session.thread_created"`

      - `workspace_id: string`

    - `BetaWebhookSessionThreadIdledEventData = object { id, organization_id, type, workspace_id }`

      - `id: string`

        ID of the resource that triggered the event.

      - `organization_id: string`

      - `type: "session.thread_idled"`

        - `"session.thread_idled"`

      - `workspace_id: string`

    - `BetaWebhookSessionThreadTerminatedEventData = object { id, organization_id, type, workspace_id }`

      - `id: string`

        ID of the resource that triggered the event.

      - `organization_id: string`

      - `type: "session.thread_terminated"`

        - `"session.thread_terminated"`

      - `workspace_id: string`

    - `BetaWebhookSessionOutcomeEvaluationEndedEventData = object { id, organization_id, type, workspace_id }`

      - `id: string`

        ID of the resource that triggered the event.

      - `organization_id: string`

      - `type: "session.outcome_evaluation_ended"`

        - `"session.outcome_evaluation_ended"`

      - `workspace_id: string`

    - `BetaWebhookVaultCreatedEventData = object { id, organization_id, type, workspace_id }`

      - `id: string`

        ID of the resource that triggered the event.

      - `organization_id: string`

      - `type: "vault.created"`

        - `"vault.created"`

      - `workspace_id: string`

    - `BetaWebhookVaultArchivedEventData = object { id, organization_id, type, workspace_id }`

      - `id: string`

        ID of the resource that triggered the event.

      - `organization_id: string`

      - `type: "vault.archived"`

        - `"vault.archived"`

      - `workspace_id: string`

    - `BetaWebhookVaultDeletedEventData = object { id, organization_id, type, workspace_id }`

      - `id: string`

        ID of the resource that triggered the event.

      - `organization_id: string`

      - `type: "vault.deleted"`

        - `"vault.deleted"`

      - `workspace_id: string`

    - `BetaWebhookVaultCredentialCreatedEventData = object { id, organization_id, type, 2 more }`

      - `id: string`

        ID of the resource that triggered the event.

      - `organization_id: string`

      - `type: "vault_credential.created"`

        - `"vault_credential.created"`

      - `vault_id: string`

        ID of the vault that owns this credential.

      - `workspace_id: string`

    - `BetaWebhookVaultCredentialArchivedEventData = object { id, organization_id, type, 2 more }`

      - `id: string`

        ID of the resource that triggered the event.

      - `organization_id: string`

      - `type: "vault_credential.archived"`

        - `"vault_credential.archived"`

      - `vault_id: string`

        ID of the vault that owns this credential.

      - `workspace_id: string`

    - `BetaWebhookVaultCredentialDeletedEventData = object { id, organization_id, type, 2 more }`

      - `id: string`

        ID of the resource that triggered the event.

      - `organization_id: string`

      - `type: "vault_credential.deleted"`

        - `"vault_credential.deleted"`

      - `vault_id: string`

        ID of the vault that owns this credential.

      - `workspace_id: string`

    - `BetaWebhookVaultCredentialRefreshFailedEventData = object { id, organization_id, type, 2 more }`

      - `id: string`

        ID of the resource that triggered the event.

      - `organization_id: string`

      - `type: "vault_credential.refresh_failed"`

        - `"vault_credential.refresh_failed"`

      - `vault_id: string`

        ID of the vault that owns this credential.

      - `workspace_id: string`

  - `type: "event"`

    Object type. Always `event` for webhook payloads.

    - `"event"`

### Beta Webhook Event Data

- `BetaWebhookEventData = BetaWebhookSessionCreatedEventData or BetaWebhookSessionPendingEventData or BetaWebhookSessionRunningEventData or 19 more`

  - `BetaWebhookSessionCreatedEventData = object { id, organization_id, type, workspace_id }`

    - `id: string`

      ID of the resource that triggered the event.

    - `organization_id: string`

    - `type: "session.created"`

      - `"session.created"`

    - `workspace_id: string`

  - `BetaWebhookSessionPendingEventData = object { id, organization_id, type, workspace_id }`

    - `id: string`

      ID of the resource that triggered the event.

    - `organization_id: string`

    - `type: "session.pending"`

      - `"session.pending"`

    - `workspace_id: string`

  - `BetaWebhookSessionRunningEventData = object { id, organization_id, type, workspace_id }`

    - `id: string`

      ID of the resource that triggered the event.

    - `organization_id: string`

    - `type: "session.running"`

      - `"session.running"`

    - `workspace_id: string`

  - `BetaWebhookSessionIdledEventData = object { id, organization_id, type, workspace_id }`

    - `id: string`

      ID of the resource that triggered the event.

    - `organization_id: string`

    - `type: "session.idled"`

      - `"session.idled"`

    - `workspace_id: string`

  - `BetaWebhookSessionRequiresActionEventData = object { id, organization_id, type, workspace_id }`

    - `id: string`

      ID of the resource that triggered the event.

    - `organization_id: string`

    - `type: "session.requires_action"`

      - `"session.requires_action"`

    - `workspace_id: string`

  - `BetaWebhookSessionArchivedEventData = object { id, organization_id, type, workspace_id }`

    - `id: string`

      ID of the resource that triggered the event.

    - `organization_id: string`

    - `type: "session.archived"`

      - `"session.archived"`

    - `workspace_id: string`

  - `BetaWebhookSessionDeletedEventData = object { id, organization_id, type, workspace_id }`

    - `id: string`

      ID of the resource that triggered the event.

    - `organization_id: string`

    - `type: "session.deleted"`

      - `"session.deleted"`

    - `workspace_id: string`

  - `BetaWebhookSessionStatusScheduledEventData = object { id, organization_id, type, workspace_id }`

    - `id: string`

      ID of the resource that triggered the event.

    - `organization_id: string`

    - `type: "session.status_scheduled"`

      - `"session.status_scheduled"`

    - `workspace_id: string`

  - `BetaWebhookSessionStatusRunStartedEventData = object { id, organization_id, type, workspace_id }`

    - `id: string`

      ID of the resource that triggered the event.

    - `organization_id: string`

    - `type: "session.status_run_started"`

      - `"session.status_run_started"`

    - `workspace_id: string`

  - `BetaWebhookSessionStatusIdledEventData = object { id, organization_id, type, workspace_id }`

    - `id: string`

      ID of the resource that triggered the event.

    - `organization_id: string`

    - `type: "session.status_idled"`

      - `"session.status_idled"`

    - `workspace_id: string`

  - `BetaWebhookSessionStatusTerminatedEventData = object { id, organization_id, type, workspace_id }`

    - `id: string`

      ID of the resource that triggered the event.

    - `organization_id: string`

    - `type: "session.status_terminated"`

      - `"session.status_terminated"`

    - `workspace_id: string`

  - `BetaWebhookSessionThreadCreatedEventData = object { id, organization_id, type, workspace_id }`

    - `id: string`

      ID of the resource that triggered the event.

    - `organization_id: string`

    - `type: "session.thread_created"`

      - `"session.thread_created"`

    - `workspace_id: string`

  - `BetaWebhookSessionThreadIdledEventData = object { id, organization_id, type, workspace_id }`

    - `id: string`

      ID of the resource that triggered the event.

    - `organization_id: string`

    - `type: "session.thread_idled"`

      - `"session.thread_idled"`

    - `workspace_id: string`

  - `BetaWebhookSessionThreadTerminatedEventData = object { id, organization_id, type, workspace_id }`

    - `id: string`

      ID of the resource that triggered the event.

    - `organization_id: string`

    - `type: "session.thread_terminated"`

      - `"session.thread_terminated"`

    - `workspace_id: string`

  - `BetaWebhookSessionOutcomeEvaluationEndedEventData = object { id, organization_id, type, workspace_id }`

    - `id: string`

      ID of the resource that triggered the event.

    - `organization_id: string`

    - `type: "session.outcome_evaluation_ended"`

      - `"session.outcome_evaluation_ended"`

    - `workspace_id: string`

  - `BetaWebhookVaultCreatedEventData = object { id, organization_id, type, workspace_id }`

    - `id: string`

      ID of the resource that triggered the event.

    - `organization_id: string`

    - `type: "vault.created"`

      - `"vault.created"`

    - `workspace_id: string`

  - `BetaWebhookVaultArchivedEventData = object { id, organization_id, type, workspace_id }`

    - `id: string`

      ID of the resource that triggered the event.

    - `organization_id: string`

    - `type: "vault.archived"`

      - `"vault.archived"`

    - `workspace_id: string`

  - `BetaWebhookVaultDeletedEventData = object { id, organization_id, type, workspace_id }`

    - `id: string`

      ID of the resource that triggered the event.

    - `organization_id: string`

    - `type: "vault.deleted"`

      - `"vault.deleted"`

    - `workspace_id: string`

  - `BetaWebhookVaultCredentialCreatedEventData = object { id, organization_id, type, 2 more }`

    - `id: string`

      ID of the resource that triggered the event.

    - `organization_id: string`

    - `type: "vault_credential.created"`

      - `"vault_credential.created"`

    - `vault_id: string`

      ID of the vault that owns this credential.

    - `workspace_id: string`

  - `BetaWebhookVaultCredentialArchivedEventData = object { id, organization_id, type, 2 more }`

    - `id: string`

      ID of the resource that triggered the event.

    - `organization_id: string`

    - `type: "vault_credential.archived"`

      - `"vault_credential.archived"`

    - `vault_id: string`

      ID of the vault that owns this credential.

    - `workspace_id: string`

  - `BetaWebhookVaultCredentialDeletedEventData = object { id, organization_id, type, 2 more }`

    - `id: string`

      ID of the resource that triggered the event.

    - `organization_id: string`

    - `type: "vault_credential.deleted"`

      - `"vault_credential.deleted"`

    - `vault_id: string`

      ID of the vault that owns this credential.

    - `workspace_id: string`

  - `BetaWebhookVaultCredentialRefreshFailedEventData = object { id, organization_id, type, 2 more }`

    - `id: string`

      ID of the resource that triggered the event.

    - `organization_id: string`

    - `type: "vault_credential.refresh_failed"`

      - `"vault_credential.refresh_failed"`

    - `vault_id: string`

      ID of the vault that owns this credential.

    - `workspace_id: string`

### Beta Webhook Session Archived Event Data

- `BetaWebhookSessionArchivedEventData = object { id, organization_id, type, workspace_id }`

  - `id: string`

    ID of the resource that triggered the event.

  - `organization_id: string`

  - `type: "session.archived"`

    - `"session.archived"`

  - `workspace_id: string`

### Beta Webhook Session Created Event Data

- `BetaWebhookSessionCreatedEventData = object { id, organization_id, type, workspace_id }`

  - `id: string`

    ID of the resource that triggered the event.

  - `organization_id: string`

  - `type: "session.created"`

    - `"session.created"`

  - `workspace_id: string`

### Beta Webhook Session Deleted Event Data

- `BetaWebhookSessionDeletedEventData = object { id, organization_id, type, workspace_id }`

  - `id: string`

    ID of the resource that triggered the event.

  - `organization_id: string`

  - `type: "session.deleted"`

    - `"session.deleted"`

  - `workspace_id: string`

### Beta Webhook Session Idled Event Data

- `BetaWebhookSessionIdledEventData = object { id, organization_id, type, workspace_id }`

  - `id: string`

    ID of the resource that triggered the event.

  - `organization_id: string`

  - `type: "session.idled"`

    - `"session.idled"`

  - `workspace_id: string`

### Beta Webhook Session Outcome Evaluation Ended Event Data

- `BetaWebhookSessionOutcomeEvaluationEndedEventData = object { id, organization_id, type, workspace_id }`

  - `id: string`

    ID of the resource that triggered the event.

  - `organization_id: string`

  - `type: "session.outcome_evaluation_ended"`

    - `"session.outcome_evaluation_ended"`

  - `workspace_id: string`

### Beta Webhook Session Pending Event Data

- `BetaWebhookSessionPendingEventData = object { id, organization_id, type, workspace_id }`

  - `id: string`

    ID of the resource that triggered the event.

  - `organization_id: string`

  - `type: "session.pending"`

    - `"session.pending"`

  - `workspace_id: string`

### Beta Webhook Session Requires Action Event Data

- `BetaWebhookSessionRequiresActionEventData = object { id, organization_id, type, workspace_id }`

  - `id: string`

    ID of the resource that triggered the event.

  - `organization_id: string`

  - `type: "session.requires_action"`

    - `"session.requires_action"`

  - `workspace_id: string`

### Beta Webhook Session Running Event Data

- `BetaWebhookSessionRunningEventData = object { id, organization_id, type, workspace_id }`

  - `id: string`

    ID of the resource that triggered the event.

  - `organization_id: string`

  - `type: "session.running"`

    - `"session.running"`

  - `workspace_id: string`

### Beta Webhook Session Status Idled Event Data

- `BetaWebhookSessionStatusIdledEventData = object { id, organization_id, type, workspace_id }`

  - `id: string`

    ID of the resource that triggered the event.

  - `organization_id: string`

  - `type: "session.status_idled"`

    - `"session.status_idled"`

  - `workspace_id: string`

### Beta Webhook Session Status Run Started Event Data

- `BetaWebhookSessionStatusRunStartedEventData = object { id, organization_id, type, workspace_id }`

  - `id: string`

    ID of the resource that triggered the event.

  - `organization_id: string`

  - `type: "session.status_run_started"`

    - `"session.status_run_started"`

  - `workspace_id: string`

### Beta Webhook Session Status Scheduled Event Data

- `BetaWebhookSessionStatusScheduledEventData = object { id, organization_id, type, workspace_id }`

  - `id: string`

    ID of the resource that triggered the event.

  - `organization_id: string`

  - `type: "session.status_scheduled"`

    - `"session.status_scheduled"`

  - `workspace_id: string`

### Beta Webhook Session Status Terminated Event Data

- `BetaWebhookSessionStatusTerminatedEventData = object { id, organization_id, type, workspace_id }`

  - `id: string`

    ID of the resource that triggered the event.

  - `organization_id: string`

  - `type: "session.status_terminated"`

    - `"session.status_terminated"`

  - `workspace_id: string`

### Beta Webhook Session Thread Created Event Data

- `BetaWebhookSessionThreadCreatedEventData = object { id, organization_id, type, workspace_id }`

  - `id: string`

    ID of the resource that triggered the event.

  - `organization_id: string`

  - `type: "session.thread_created"`

    - `"session.thread_created"`

  - `workspace_id: string`

### Beta Webhook Session Thread Idled Event Data

- `BetaWebhookSessionThreadIdledEventData = object { id, organization_id, type, workspace_id }`

  - `id: string`

    ID of the resource that triggered the event.

  - `organization_id: string`

  - `type: "session.thread_idled"`

    - `"session.thread_idled"`

  - `workspace_id: string`

### Beta Webhook Session Thread Terminated Event Data

- `BetaWebhookSessionThreadTerminatedEventData = object { id, organization_id, type, workspace_id }`

  - `id: string`

    ID of the resource that triggered the event.

  - `organization_id: string`

  - `type: "session.thread_terminated"`

    - `"session.thread_terminated"`

  - `workspace_id: string`

### Beta Webhook Vault Archived Event Data

- `BetaWebhookVaultArchivedEventData = object { id, organization_id, type, workspace_id }`

  - `id: string`

    ID of the resource that triggered the event.

  - `organization_id: string`

  - `type: "vault.archived"`

    - `"vault.archived"`

  - `workspace_id: string`

### Beta Webhook Vault Created Event Data

- `BetaWebhookVaultCreatedEventData = object { id, organization_id, type, workspace_id }`

  - `id: string`

    ID of the resource that triggered the event.

  - `organization_id: string`

  - `type: "vault.created"`

    - `"vault.created"`

  - `workspace_id: string`

### Beta Webhook Vault Credential Archived Event Data

- `BetaWebhookVaultCredentialArchivedEventData = object { id, organization_id, type, 2 more }`

  - `id: string`

    ID of the resource that triggered the event.

  - `organization_id: string`

  - `type: "vault_credential.archived"`

    - `"vault_credential.archived"`

  - `vault_id: string`

    ID of the vault that owns this credential.

  - `workspace_id: string`

### Beta Webhook Vault Credential Created Event Data

- `BetaWebhookVaultCredentialCreatedEventData = object { id, organization_id, type, 2 more }`

  - `id: string`

    ID of the resource that triggered the event.

  - `organization_id: string`

  - `type: "vault_credential.created"`

    - `"vault_credential.created"`

  - `vault_id: string`

    ID of the vault that owns this credential.

  - `workspace_id: string`

### Beta Webhook Vault Credential Deleted Event Data

- `BetaWebhookVaultCredentialDeletedEventData = object { id, organization_id, type, 2 more }`

  - `id: string`

    ID of the resource that triggered the event.

  - `organization_id: string`

  - `type: "vault_credential.deleted"`

    - `"vault_credential.deleted"`

  - `vault_id: string`

    ID of the vault that owns this credential.

  - `workspace_id: string`

### Beta Webhook Vault Credential Refresh Failed Event Data

- `BetaWebhookVaultCredentialRefreshFailedEventData = object { id, organization_id, type, 2 more }`

  - `id: string`

    ID of the resource that triggered the event.

  - `organization_id: string`

  - `type: "vault_credential.refresh_failed"`

    - `"vault_credential.refresh_failed"`

  - `vault_id: string`

    ID of the vault that owns this credential.

  - `workspace_id: string`

### Beta Webhook Vault Deleted Event Data

- `BetaWebhookVaultDeletedEventData = object { id, organization_id, type, workspace_id }`

  - `id: string`

    ID of the resource that triggered the event.

  - `organization_id: string`

  - `type: "vault.deleted"`

    - `"vault.deleted"`

  - `workspace_id: string`

### Unwrap Webhook Event

- `UnwrapWebhookEvent = object { id, created_at, data, type }`

  - `id: string`

    Unique event identifier for idempotency.

  - `created_at: string`

    RFC 3339 timestamp when the event occurred.

  - `data: BetaWebhookEventData`

    - `BetaWebhookSessionCreatedEventData = object { id, organization_id, type, workspace_id }`

      - `id: string`

        ID of the resource that triggered the event.

      - `organization_id: string`

      - `type: "session.created"`

        - `"session.created"`

      - `workspace_id: string`

    - `BetaWebhookSessionPendingEventData = object { id, organization_id, type, workspace_id }`

      - `id: string`

        ID of the resource that triggered the event.

      - `organization_id: string`

      - `type: "session.pending"`

        - `"session.pending"`

      - `workspace_id: string`

    - `BetaWebhookSessionRunningEventData = object { id, organization_id, type, workspace_id }`

      - `id: string`

        ID of the resource that triggered the event.

      - `organization_id: string`

      - `type: "session.running"`

        - `"session.running"`

      - `workspace_id: string`

    - `BetaWebhookSessionIdledEventData = object { id, organization_id, type, workspace_id }`

      - `id: string`

        ID of the resource that triggered the event.

      - `organization_id: string`

      - `type: "session.idled"`

        - `"session.idled"`

      - `workspace_id: string`

    - `BetaWebhookSessionRequiresActionEventData = object { id, organization_id, type, workspace_id }`

      - `id: string`

        ID of the resource that triggered the event.

      - `organization_id: string`

      - `type: "session.requires_action"`

        - `"session.requires_action"`

      - `workspace_id: string`

    - `BetaWebhookSessionArchivedEventData = object { id, organization_id, type, workspace_id }`

      - `id: string`

        ID of the resource that triggered the event.

      - `organization_id: string`

      - `type: "session.archived"`

        - `"session.archived"`

      - `workspace_id: string`

    - `BetaWebhookSessionDeletedEventData = object { id, organization_id, type, workspace_id }`

      - `id: string`

        ID of the resource that triggered the event.

      - `organization_id: string`

      - `type: "session.deleted"`

        - `"session.deleted"`

      - `workspace_id: string`

    - `BetaWebhookSessionStatusScheduledEventData = object { id, organization_id, type, workspace_id }`

      - `id: string`

        ID of the resource that triggered the event.

      - `organization_id: string`

      - `type: "session.status_scheduled"`

        - `"session.status_scheduled"`

      - `workspace_id: string`

    - `BetaWebhookSessionStatusRunStartedEventData = object { id, organization_id, type, workspace_id }`

      - `id: string`

        ID of the resource that triggered the event.

      - `organization_id: string`

      - `type: "session.status_run_started"`

        - `"session.status_run_started"`

      - `workspace_id: string`

    - `BetaWebhookSessionStatusIdledEventData = object { id, organization_id, type, workspace_id }`

      - `id: string`

        ID of the resource that triggered the event.

      - `organization_id: string`

      - `type: "session.status_idled"`

        - `"session.status_idled"`

      - `workspace_id: string`

    - `BetaWebhookSessionStatusTerminatedEventData = object { id, organization_id, type, workspace_id }`

      - `id: string`

        ID of the resource that triggered the event.

      - `organization_id: string`

      - `type: "session.status_terminated"`

        - `"session.status_terminated"`

      - `workspace_id: string`

    - `BetaWebhookSessionThreadCreatedEventData = object { id, organization_id, type, workspace_id }`

      - `id: string`

        ID of the resource that triggered the event.

      - `organization_id: string`

      - `type: "session.thread_created"`

        - `"session.thread_created"`

      - `workspace_id: string`

    - `BetaWebhookSessionThreadIdledEventData = object { id, organization_id, type, workspace_id }`

      - `id: string`

        ID of the resource that triggered the event.

      - `organization_id: string`

      - `type: "session.thread_idled"`

        - `"session.thread_idled"`

      - `workspace_id: string`

    - `BetaWebhookSessionThreadTerminatedEventData = object { id, organization_id, type, workspace_id }`

      - `id: string`

        ID of the resource that triggered the event.

      - `organization_id: string`

      - `type: "session.thread_terminated"`

        - `"session.thread_terminated"`

      - `workspace_id: string`

    - `BetaWebhookSessionOutcomeEvaluationEndedEventData = object { id, organization_id, type, workspace_id }`

      - `id: string`

        ID of the resource that triggered the event.

      - `organization_id: string`

      - `type: "session.outcome_evaluation_ended"`

        - `"session.outcome_evaluation_ended"`

      - `workspace_id: string`

    - `BetaWebhookVaultCreatedEventData = object { id, organization_id, type, workspace_id }`

      - `id: string`

        ID of the resource that triggered the event.

      - `organization_id: string`

      - `type: "vault.created"`

        - `"vault.created"`

      - `workspace_id: string`

    - `BetaWebhookVaultArchivedEventData = object { id, organization_id, type, workspace_id }`

      - `id: string`

        ID of the resource that triggered the event.

      - `organization_id: string`

      - `type: "vault.archived"`

        - `"vault.archived"`

      - `workspace_id: string`

    - `BetaWebhookVaultDeletedEventData = object { id, organization_id, type, workspace_id }`

      - `id: string`

        ID of the resource that triggered the event.

      - `organization_id: string`

      - `type: "vault.deleted"`

        - `"vault.deleted"`

      - `workspace_id: string`

    - `BetaWebhookVaultCredentialCreatedEventData = object { id, organization_id, type, 2 more }`

      - `id: string`

        ID of the resource that triggered the event.

      - `organization_id: string`

      - `type: "vault_credential.created"`

        - `"vault_credential.created"`

      - `vault_id: string`

        ID of the vault that owns this credential.

      - `workspace_id: string`

    - `BetaWebhookVaultCredentialArchivedEventData = object { id, organization_id, type, 2 more }`

      - `id: string`

        ID of the resource that triggered the event.

      - `organization_id: string`

      - `type: "vault_credential.archived"`

        - `"vault_credential.archived"`

      - `vault_id: string`

        ID of the vault that owns this credential.

      - `workspace_id: string`

    - `BetaWebhookVaultCredentialDeletedEventData = object { id, organization_id, type, 2 more }`

      - `id: string`

        ID of the resource that triggered the event.

      - `organization_id: string`

      - `type: "vault_credential.deleted"`

        - `"vault_credential.deleted"`

      - `vault_id: string`

        ID of the vault that owns this credential.

      - `workspace_id: string`

    - `BetaWebhookVaultCredentialRefreshFailedEventData = object { id, organization_id, type, 2 more }`

      - `id: string`

        ID of the resource that triggered the event.

      - `organization_id: string`

      - `type: "vault_credential.refresh_failed"`

        - `"vault_credential.refresh_failed"`

      - `vault_id: string`

        ID of the vault that owns this credential.

      - `workspace_id: string`

  - `type: "event"`

    Object type. Always `event` for webhook payloads.

    - `"event"`
