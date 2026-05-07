# Webhooks

## Domain Types

### Beta Webhook Event

- `BetaWebhookEvent`

  - `id: string`

    Unique event identifier for idempotency.

  - `created_at: string`

    RFC 3339 timestamp when the event occurred.

  - `data: BetaWebhookEventData`

    - `BetaWebhookSessionCreatedEventData`

      - `id: string`

        ID of the resource that triggered the event.

      - `organization_id: string`

      - `type: "session.created"`

        - `"session.created"`

      - `workspace_id: string`

    - `BetaWebhookSessionPendingEventData`

      - `id: string`

        ID of the resource that triggered the event.

      - `organization_id: string`

      - `type: "session.pending"`

        - `"session.pending"`

      - `workspace_id: string`

    - `BetaWebhookSessionRunningEventData`

      - `id: string`

        ID of the resource that triggered the event.

      - `organization_id: string`

      - `type: "session.running"`

        - `"session.running"`

      - `workspace_id: string`

    - `BetaWebhookSessionIdledEventData`

      - `id: string`

        ID of the resource that triggered the event.

      - `organization_id: string`

      - `type: "session.idled"`

        - `"session.idled"`

      - `workspace_id: string`

    - `BetaWebhookSessionRequiresActionEventData`

      - `id: string`

        ID of the resource that triggered the event.

      - `organization_id: string`

      - `type: "session.requires_action"`

        - `"session.requires_action"`

      - `workspace_id: string`

    - `BetaWebhookSessionArchivedEventData`

      - `id: string`

        ID of the resource that triggered the event.

      - `organization_id: string`

      - `type: "session.archived"`

        - `"session.archived"`

      - `workspace_id: string`

    - `BetaWebhookSessionDeletedEventData`

      - `id: string`

        ID of the resource that triggered the event.

      - `organization_id: string`

      - `type: "session.deleted"`

        - `"session.deleted"`

      - `workspace_id: string`

    - `BetaWebhookSessionStatusRescheduledEventData`

      - `id: string`

        ID of the resource that triggered the event.

      - `organization_id: string`

      - `type: "session.status_rescheduled"`

        - `"session.status_rescheduled"`

      - `workspace_id: string`

    - `BetaWebhookSessionStatusRunStartedEventData`

      - `id: string`

        ID of the resource that triggered the event.

      - `organization_id: string`

      - `type: "session.status_run_started"`

        - `"session.status_run_started"`

      - `workspace_id: string`

    - `BetaWebhookSessionStatusIdledEventData`

      - `id: string`

        ID of the resource that triggered the event.

      - `organization_id: string`

      - `type: "session.status_idled"`

        - `"session.status_idled"`

      - `workspace_id: string`

    - `BetaWebhookSessionStatusTerminatedEventData`

      - `id: string`

        ID of the resource that triggered the event.

      - `organization_id: string`

      - `type: "session.status_terminated"`

        - `"session.status_terminated"`

      - `workspace_id: string`

    - `BetaWebhookSessionThreadCreatedEventData`

      - `id: string`

        ID of the resource that triggered the event.

      - `organization_id: string`

      - `type: "session.thread_created"`

        - `"session.thread_created"`

      - `workspace_id: string`

    - `BetaWebhookSessionThreadIdledEventData`

      - `id: string`

        ID of the resource that triggered the event.

      - `organization_id: string`

      - `type: "session.thread_idled"`

        - `"session.thread_idled"`

      - `workspace_id: string`

    - `BetaWebhookSessionThreadTerminatedEventData`

      - `id: string`

        ID of the resource that triggered the event.

      - `organization_id: string`

      - `type: "session.thread_terminated"`

        - `"session.thread_terminated"`

      - `workspace_id: string`

    - `BetaWebhookSessionOutcomeEvaluationEndedEventData`

      - `id: string`

        ID of the resource that triggered the event.

      - `organization_id: string`

      - `type: "session.outcome_evaluation_ended"`

        - `"session.outcome_evaluation_ended"`

      - `workspace_id: string`

    - `BetaWebhookVaultCreatedEventData`

      - `id: string`

        ID of the resource that triggered the event.

      - `organization_id: string`

      - `type: "vault.created"`

        - `"vault.created"`

      - `workspace_id: string`

    - `BetaWebhookVaultArchivedEventData`

      - `id: string`

        ID of the resource that triggered the event.

      - `organization_id: string`

      - `type: "vault.archived"`

        - `"vault.archived"`

      - `workspace_id: string`

    - `BetaWebhookVaultDeletedEventData`

      - `id: string`

        ID of the resource that triggered the event.

      - `organization_id: string`

      - `type: "vault.deleted"`

        - `"vault.deleted"`

      - `workspace_id: string`

    - `BetaWebhookVaultCredentialCreatedEventData`

      - `id: string`

        ID of the resource that triggered the event.

      - `organization_id: string`

      - `type: "vault_credential.created"`

        - `"vault_credential.created"`

      - `vault_id: string`

        ID of the vault that owns this credential.

      - `workspace_id: string`

    - `BetaWebhookVaultCredentialArchivedEventData`

      - `id: string`

        ID of the resource that triggered the event.

      - `organization_id: string`

      - `type: "vault_credential.archived"`

        - `"vault_credential.archived"`

      - `vault_id: string`

        ID of the vault that owns this credential.

      - `workspace_id: string`

    - `BetaWebhookVaultCredentialDeletedEventData`

      - `id: string`

        ID of the resource that triggered the event.

      - `organization_id: string`

      - `type: "vault_credential.deleted"`

        - `"vault_credential.deleted"`

      - `vault_id: string`

        ID of the vault that owns this credential.

      - `workspace_id: string`

    - `BetaWebhookVaultCredentialRefreshFailedEventData`

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

- `BetaWebhookEventData = BetaWebhookSessionCreatedEventData | BetaWebhookSessionPendingEventData | BetaWebhookSessionRunningEventData | 19 more`

  - `BetaWebhookSessionCreatedEventData`

    - `id: string`

      ID of the resource that triggered the event.

    - `organization_id: string`

    - `type: "session.created"`

      - `"session.created"`

    - `workspace_id: string`

  - `BetaWebhookSessionPendingEventData`

    - `id: string`

      ID of the resource that triggered the event.

    - `organization_id: string`

    - `type: "session.pending"`

      - `"session.pending"`

    - `workspace_id: string`

  - `BetaWebhookSessionRunningEventData`

    - `id: string`

      ID of the resource that triggered the event.

    - `organization_id: string`

    - `type: "session.running"`

      - `"session.running"`

    - `workspace_id: string`

  - `BetaWebhookSessionIdledEventData`

    - `id: string`

      ID of the resource that triggered the event.

    - `organization_id: string`

    - `type: "session.idled"`

      - `"session.idled"`

    - `workspace_id: string`

  - `BetaWebhookSessionRequiresActionEventData`

    - `id: string`

      ID of the resource that triggered the event.

    - `organization_id: string`

    - `type: "session.requires_action"`

      - `"session.requires_action"`

    - `workspace_id: string`

  - `BetaWebhookSessionArchivedEventData`

    - `id: string`

      ID of the resource that triggered the event.

    - `organization_id: string`

    - `type: "session.archived"`

      - `"session.archived"`

    - `workspace_id: string`

  - `BetaWebhookSessionDeletedEventData`

    - `id: string`

      ID of the resource that triggered the event.

    - `organization_id: string`

    - `type: "session.deleted"`

      - `"session.deleted"`

    - `workspace_id: string`

  - `BetaWebhookSessionStatusRescheduledEventData`

    - `id: string`

      ID of the resource that triggered the event.

    - `organization_id: string`

    - `type: "session.status_rescheduled"`

      - `"session.status_rescheduled"`

    - `workspace_id: string`

  - `BetaWebhookSessionStatusRunStartedEventData`

    - `id: string`

      ID of the resource that triggered the event.

    - `organization_id: string`

    - `type: "session.status_run_started"`

      - `"session.status_run_started"`

    - `workspace_id: string`

  - `BetaWebhookSessionStatusIdledEventData`

    - `id: string`

      ID of the resource that triggered the event.

    - `organization_id: string`

    - `type: "session.status_idled"`

      - `"session.status_idled"`

    - `workspace_id: string`

  - `BetaWebhookSessionStatusTerminatedEventData`

    - `id: string`

      ID of the resource that triggered the event.

    - `organization_id: string`

    - `type: "session.status_terminated"`

      - `"session.status_terminated"`

    - `workspace_id: string`

  - `BetaWebhookSessionThreadCreatedEventData`

    - `id: string`

      ID of the resource that triggered the event.

    - `organization_id: string`

    - `type: "session.thread_created"`

      - `"session.thread_created"`

    - `workspace_id: string`

  - `BetaWebhookSessionThreadIdledEventData`

    - `id: string`

      ID of the resource that triggered the event.

    - `organization_id: string`

    - `type: "session.thread_idled"`

      - `"session.thread_idled"`

    - `workspace_id: string`

  - `BetaWebhookSessionThreadTerminatedEventData`

    - `id: string`

      ID of the resource that triggered the event.

    - `organization_id: string`

    - `type: "session.thread_terminated"`

      - `"session.thread_terminated"`

    - `workspace_id: string`

  - `BetaWebhookSessionOutcomeEvaluationEndedEventData`

    - `id: string`

      ID of the resource that triggered the event.

    - `organization_id: string`

    - `type: "session.outcome_evaluation_ended"`

      - `"session.outcome_evaluation_ended"`

    - `workspace_id: string`

  - `BetaWebhookVaultCreatedEventData`

    - `id: string`

      ID of the resource that triggered the event.

    - `organization_id: string`

    - `type: "vault.created"`

      - `"vault.created"`

    - `workspace_id: string`

  - `BetaWebhookVaultArchivedEventData`

    - `id: string`

      ID of the resource that triggered the event.

    - `organization_id: string`

    - `type: "vault.archived"`

      - `"vault.archived"`

    - `workspace_id: string`

  - `BetaWebhookVaultDeletedEventData`

    - `id: string`

      ID of the resource that triggered the event.

    - `organization_id: string`

    - `type: "vault.deleted"`

      - `"vault.deleted"`

    - `workspace_id: string`

  - `BetaWebhookVaultCredentialCreatedEventData`

    - `id: string`

      ID of the resource that triggered the event.

    - `organization_id: string`

    - `type: "vault_credential.created"`

      - `"vault_credential.created"`

    - `vault_id: string`

      ID of the vault that owns this credential.

    - `workspace_id: string`

  - `BetaWebhookVaultCredentialArchivedEventData`

    - `id: string`

      ID of the resource that triggered the event.

    - `organization_id: string`

    - `type: "vault_credential.archived"`

      - `"vault_credential.archived"`

    - `vault_id: string`

      ID of the vault that owns this credential.

    - `workspace_id: string`

  - `BetaWebhookVaultCredentialDeletedEventData`

    - `id: string`

      ID of the resource that triggered the event.

    - `organization_id: string`

    - `type: "vault_credential.deleted"`

      - `"vault_credential.deleted"`

    - `vault_id: string`

      ID of the vault that owns this credential.

    - `workspace_id: string`

  - `BetaWebhookVaultCredentialRefreshFailedEventData`

    - `id: string`

      ID of the resource that triggered the event.

    - `organization_id: string`

    - `type: "vault_credential.refresh_failed"`

      - `"vault_credential.refresh_failed"`

    - `vault_id: string`

      ID of the vault that owns this credential.

    - `workspace_id: string`

### Beta Webhook Session Archived Event Data

- `BetaWebhookSessionArchivedEventData`

  - `id: string`

    ID of the resource that triggered the event.

  - `organization_id: string`

  - `type: "session.archived"`

    - `"session.archived"`

  - `workspace_id: string`

### Beta Webhook Session Created Event Data

- `BetaWebhookSessionCreatedEventData`

  - `id: string`

    ID of the resource that triggered the event.

  - `organization_id: string`

  - `type: "session.created"`

    - `"session.created"`

  - `workspace_id: string`

### Beta Webhook Session Deleted Event Data

- `BetaWebhookSessionDeletedEventData`

  - `id: string`

    ID of the resource that triggered the event.

  - `organization_id: string`

  - `type: "session.deleted"`

    - `"session.deleted"`

  - `workspace_id: string`

### Beta Webhook Session Idled Event Data

- `BetaWebhookSessionIdledEventData`

  - `id: string`

    ID of the resource that triggered the event.

  - `organization_id: string`

  - `type: "session.idled"`

    - `"session.idled"`

  - `workspace_id: string`

### Beta Webhook Session Outcome Evaluation Ended Event Data

- `BetaWebhookSessionOutcomeEvaluationEndedEventData`

  - `id: string`

    ID of the resource that triggered the event.

  - `organization_id: string`

  - `type: "session.outcome_evaluation_ended"`

    - `"session.outcome_evaluation_ended"`

  - `workspace_id: string`

### Beta Webhook Session Pending Event Data

- `BetaWebhookSessionPendingEventData`

  - `id: string`

    ID of the resource that triggered the event.

  - `organization_id: string`

  - `type: "session.pending"`

    - `"session.pending"`

  - `workspace_id: string`

### Beta Webhook Session Requires Action Event Data

- `BetaWebhookSessionRequiresActionEventData`

  - `id: string`

    ID of the resource that triggered the event.

  - `organization_id: string`

  - `type: "session.requires_action"`

    - `"session.requires_action"`

  - `workspace_id: string`

### Beta Webhook Session Running Event Data

- `BetaWebhookSessionRunningEventData`

  - `id: string`

    ID of the resource that triggered the event.

  - `organization_id: string`

  - `type: "session.running"`

    - `"session.running"`

  - `workspace_id: string`

### Beta Webhook Session Status Idled Event Data

- `BetaWebhookSessionStatusIdledEventData`

  - `id: string`

    ID of the resource that triggered the event.

  - `organization_id: string`

  - `type: "session.status_idled"`

    - `"session.status_idled"`

  - `workspace_id: string`

### Beta Webhook Session Status Rescheduled Event Data

- `BetaWebhookSessionStatusRescheduledEventData`

  - `id: string`

    ID of the resource that triggered the event.

  - `organization_id: string`

  - `type: "session.status_rescheduled"`

    - `"session.status_rescheduled"`

  - `workspace_id: string`

### Beta Webhook Session Status Run Started Event Data

- `BetaWebhookSessionStatusRunStartedEventData`

  - `id: string`

    ID of the resource that triggered the event.

  - `organization_id: string`

  - `type: "session.status_run_started"`

    - `"session.status_run_started"`

  - `workspace_id: string`

### Beta Webhook Session Status Terminated Event Data

- `BetaWebhookSessionStatusTerminatedEventData`

  - `id: string`

    ID of the resource that triggered the event.

  - `organization_id: string`

  - `type: "session.status_terminated"`

    - `"session.status_terminated"`

  - `workspace_id: string`

### Beta Webhook Session Thread Created Event Data

- `BetaWebhookSessionThreadCreatedEventData`

  - `id: string`

    ID of the resource that triggered the event.

  - `organization_id: string`

  - `type: "session.thread_created"`

    - `"session.thread_created"`

  - `workspace_id: string`

### Beta Webhook Session Thread Idled Event Data

- `BetaWebhookSessionThreadIdledEventData`

  - `id: string`

    ID of the resource that triggered the event.

  - `organization_id: string`

  - `type: "session.thread_idled"`

    - `"session.thread_idled"`

  - `workspace_id: string`

### Beta Webhook Session Thread Terminated Event Data

- `BetaWebhookSessionThreadTerminatedEventData`

  - `id: string`

    ID of the resource that triggered the event.

  - `organization_id: string`

  - `type: "session.thread_terminated"`

    - `"session.thread_terminated"`

  - `workspace_id: string`

### Beta Webhook Vault Archived Event Data

- `BetaWebhookVaultArchivedEventData`

  - `id: string`

    ID of the resource that triggered the event.

  - `organization_id: string`

  - `type: "vault.archived"`

    - `"vault.archived"`

  - `workspace_id: string`

### Beta Webhook Vault Created Event Data

- `BetaWebhookVaultCreatedEventData`

  - `id: string`

    ID of the resource that triggered the event.

  - `organization_id: string`

  - `type: "vault.created"`

    - `"vault.created"`

  - `workspace_id: string`

### Beta Webhook Vault Credential Archived Event Data

- `BetaWebhookVaultCredentialArchivedEventData`

  - `id: string`

    ID of the resource that triggered the event.

  - `organization_id: string`

  - `type: "vault_credential.archived"`

    - `"vault_credential.archived"`

  - `vault_id: string`

    ID of the vault that owns this credential.

  - `workspace_id: string`

### Beta Webhook Vault Credential Created Event Data

- `BetaWebhookVaultCredentialCreatedEventData`

  - `id: string`

    ID of the resource that triggered the event.

  - `organization_id: string`

  - `type: "vault_credential.created"`

    - `"vault_credential.created"`

  - `vault_id: string`

    ID of the vault that owns this credential.

  - `workspace_id: string`

### Beta Webhook Vault Credential Deleted Event Data

- `BetaWebhookVaultCredentialDeletedEventData`

  - `id: string`

    ID of the resource that triggered the event.

  - `organization_id: string`

  - `type: "vault_credential.deleted"`

    - `"vault_credential.deleted"`

  - `vault_id: string`

    ID of the vault that owns this credential.

  - `workspace_id: string`

### Beta Webhook Vault Credential Refresh Failed Event Data

- `BetaWebhookVaultCredentialRefreshFailedEventData`

  - `id: string`

    ID of the resource that triggered the event.

  - `organization_id: string`

  - `type: "vault_credential.refresh_failed"`

    - `"vault_credential.refresh_failed"`

  - `vault_id: string`

    ID of the vault that owns this credential.

  - `workspace_id: string`

### Beta Webhook Vault Deleted Event Data

- `BetaWebhookVaultDeletedEventData`

  - `id: string`

    ID of the resource that triggered the event.

  - `organization_id: string`

  - `type: "vault.deleted"`

    - `"vault.deleted"`

  - `workspace_id: string`

### Unwrap Webhook Event

- `UnwrapWebhookEvent`

  - `id: string`

    Unique event identifier for idempotency.

  - `created_at: string`

    RFC 3339 timestamp when the event occurred.

  - `data: BetaWebhookEventData`

    - `BetaWebhookSessionCreatedEventData`

      - `id: string`

        ID of the resource that triggered the event.

      - `organization_id: string`

      - `type: "session.created"`

        - `"session.created"`

      - `workspace_id: string`

    - `BetaWebhookSessionPendingEventData`

      - `id: string`

        ID of the resource that triggered the event.

      - `organization_id: string`

      - `type: "session.pending"`

        - `"session.pending"`

      - `workspace_id: string`

    - `BetaWebhookSessionRunningEventData`

      - `id: string`

        ID of the resource that triggered the event.

      - `organization_id: string`

      - `type: "session.running"`

        - `"session.running"`

      - `workspace_id: string`

    - `BetaWebhookSessionIdledEventData`

      - `id: string`

        ID of the resource that triggered the event.

      - `organization_id: string`

      - `type: "session.idled"`

        - `"session.idled"`

      - `workspace_id: string`

    - `BetaWebhookSessionRequiresActionEventData`

      - `id: string`

        ID of the resource that triggered the event.

      - `organization_id: string`

      - `type: "session.requires_action"`

        - `"session.requires_action"`

      - `workspace_id: string`

    - `BetaWebhookSessionArchivedEventData`

      - `id: string`

        ID of the resource that triggered the event.

      - `organization_id: string`

      - `type: "session.archived"`

        - `"session.archived"`

      - `workspace_id: string`

    - `BetaWebhookSessionDeletedEventData`

      - `id: string`

        ID of the resource that triggered the event.

      - `organization_id: string`

      - `type: "session.deleted"`

        - `"session.deleted"`

      - `workspace_id: string`

    - `BetaWebhookSessionStatusRescheduledEventData`

      - `id: string`

        ID of the resource that triggered the event.

      - `organization_id: string`

      - `type: "session.status_rescheduled"`

        - `"session.status_rescheduled"`

      - `workspace_id: string`

    - `BetaWebhookSessionStatusRunStartedEventData`

      - `id: string`

        ID of the resource that triggered the event.

      - `organization_id: string`

      - `type: "session.status_run_started"`

        - `"session.status_run_started"`

      - `workspace_id: string`

    - `BetaWebhookSessionStatusIdledEventData`

      - `id: string`

        ID of the resource that triggered the event.

      - `organization_id: string`

      - `type: "session.status_idled"`

        - `"session.status_idled"`

      - `workspace_id: string`

    - `BetaWebhookSessionStatusTerminatedEventData`

      - `id: string`

        ID of the resource that triggered the event.

      - `organization_id: string`

      - `type: "session.status_terminated"`

        - `"session.status_terminated"`

      - `workspace_id: string`

    - `BetaWebhookSessionThreadCreatedEventData`

      - `id: string`

        ID of the resource that triggered the event.

      - `organization_id: string`

      - `type: "session.thread_created"`

        - `"session.thread_created"`

      - `workspace_id: string`

    - `BetaWebhookSessionThreadIdledEventData`

      - `id: string`

        ID of the resource that triggered the event.

      - `organization_id: string`

      - `type: "session.thread_idled"`

        - `"session.thread_idled"`

      - `workspace_id: string`

    - `BetaWebhookSessionThreadTerminatedEventData`

      - `id: string`

        ID of the resource that triggered the event.

      - `organization_id: string`

      - `type: "session.thread_terminated"`

        - `"session.thread_terminated"`

      - `workspace_id: string`

    - `BetaWebhookSessionOutcomeEvaluationEndedEventData`

      - `id: string`

        ID of the resource that triggered the event.

      - `organization_id: string`

      - `type: "session.outcome_evaluation_ended"`

        - `"session.outcome_evaluation_ended"`

      - `workspace_id: string`

    - `BetaWebhookVaultCreatedEventData`

      - `id: string`

        ID of the resource that triggered the event.

      - `organization_id: string`

      - `type: "vault.created"`

        - `"vault.created"`

      - `workspace_id: string`

    - `BetaWebhookVaultArchivedEventData`

      - `id: string`

        ID of the resource that triggered the event.

      - `organization_id: string`

      - `type: "vault.archived"`

        - `"vault.archived"`

      - `workspace_id: string`

    - `BetaWebhookVaultDeletedEventData`

      - `id: string`

        ID of the resource that triggered the event.

      - `organization_id: string`

      - `type: "vault.deleted"`

        - `"vault.deleted"`

      - `workspace_id: string`

    - `BetaWebhookVaultCredentialCreatedEventData`

      - `id: string`

        ID of the resource that triggered the event.

      - `organization_id: string`

      - `type: "vault_credential.created"`

        - `"vault_credential.created"`

      - `vault_id: string`

        ID of the vault that owns this credential.

      - `workspace_id: string`

    - `BetaWebhookVaultCredentialArchivedEventData`

      - `id: string`

        ID of the resource that triggered the event.

      - `organization_id: string`

      - `type: "vault_credential.archived"`

        - `"vault_credential.archived"`

      - `vault_id: string`

        ID of the vault that owns this credential.

      - `workspace_id: string`

    - `BetaWebhookVaultCredentialDeletedEventData`

      - `id: string`

        ID of the resource that triggered the event.

      - `organization_id: string`

      - `type: "vault_credential.deleted"`

        - `"vault_credential.deleted"`

      - `vault_id: string`

        ID of the vault that owns this credential.

      - `workspace_id: string`

    - `BetaWebhookVaultCredentialRefreshFailedEventData`

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
