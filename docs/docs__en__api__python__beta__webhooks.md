# Webhooks

## Domain Types

### Beta Webhook Event

- `class BetaWebhookEvent: …`

  - `id: str`

    Unique event identifier for idempotency.

  - `created_at: datetime`

    RFC 3339 timestamp when the event occurred.

  - `data: BetaWebhookEventData`

    - `class BetaWebhookSessionCreatedEventData: …`

      - `id: str`

        ID of the resource that triggered the event.

      - `organization_id: str`

      - `type: Literal["session.created"]`

        - `"session.created"`

      - `workspace_id: str`

    - `class BetaWebhookSessionPendingEventData: …`

      - `id: str`

        ID of the resource that triggered the event.

      - `organization_id: str`

      - `type: Literal["session.pending"]`

        - `"session.pending"`

      - `workspace_id: str`

    - `class BetaWebhookSessionRunningEventData: …`

      - `id: str`

        ID of the resource that triggered the event.

      - `organization_id: str`

      - `type: Literal["session.running"]`

        - `"session.running"`

      - `workspace_id: str`

    - `class BetaWebhookSessionIdledEventData: …`

      - `id: str`

        ID of the resource that triggered the event.

      - `organization_id: str`

      - `type: Literal["session.idled"]`

        - `"session.idled"`

      - `workspace_id: str`

    - `class BetaWebhookSessionRequiresActionEventData: …`

      - `id: str`

        ID of the resource that triggered the event.

      - `organization_id: str`

      - `type: Literal["session.requires_action"]`

        - `"session.requires_action"`

      - `workspace_id: str`

    - `class BetaWebhookSessionArchivedEventData: …`

      - `id: str`

        ID of the resource that triggered the event.

      - `organization_id: str`

      - `type: Literal["session.archived"]`

        - `"session.archived"`

      - `workspace_id: str`

    - `class BetaWebhookSessionDeletedEventData: …`

      - `id: str`

        ID of the resource that triggered the event.

      - `organization_id: str`

      - `type: Literal["session.deleted"]`

        - `"session.deleted"`

      - `workspace_id: str`

    - `class BetaWebhookSessionStatusRescheduledEventData: …`

      - `id: str`

        ID of the resource that triggered the event.

      - `organization_id: str`

      - `type: Literal["session.status_rescheduled"]`

        - `"session.status_rescheduled"`

      - `workspace_id: str`

    - `class BetaWebhookSessionStatusRunStartedEventData: …`

      - `id: str`

        ID of the resource that triggered the event.

      - `organization_id: str`

      - `type: Literal["session.status_run_started"]`

        - `"session.status_run_started"`

      - `workspace_id: str`

    - `class BetaWebhookSessionStatusIdledEventData: …`

      - `id: str`

        ID of the resource that triggered the event.

      - `organization_id: str`

      - `type: Literal["session.status_idled"]`

        - `"session.status_idled"`

      - `workspace_id: str`

    - `class BetaWebhookSessionStatusTerminatedEventData: …`

      - `id: str`

        ID of the resource that triggered the event.

      - `organization_id: str`

      - `type: Literal["session.status_terminated"]`

        - `"session.status_terminated"`

      - `workspace_id: str`

    - `class BetaWebhookSessionThreadCreatedEventData: …`

      - `id: str`

        ID of the resource that triggered the event.

      - `organization_id: str`

      - `type: Literal["session.thread_created"]`

        - `"session.thread_created"`

      - `workspace_id: str`

    - `class BetaWebhookSessionThreadIdledEventData: …`

      - `id: str`

        ID of the resource that triggered the event.

      - `organization_id: str`

      - `type: Literal["session.thread_idled"]`

        - `"session.thread_idled"`

      - `workspace_id: str`

    - `class BetaWebhookSessionThreadTerminatedEventData: …`

      - `id: str`

        ID of the resource that triggered the event.

      - `organization_id: str`

      - `type: Literal["session.thread_terminated"]`

        - `"session.thread_terminated"`

      - `workspace_id: str`

    - `class BetaWebhookSessionOutcomeEvaluationEndedEventData: …`

      - `id: str`

        ID of the resource that triggered the event.

      - `organization_id: str`

      - `type: Literal["session.outcome_evaluation_ended"]`

        - `"session.outcome_evaluation_ended"`

      - `workspace_id: str`

    - `class BetaWebhookVaultCreatedEventData: …`

      - `id: str`

        ID of the resource that triggered the event.

      - `organization_id: str`

      - `type: Literal["vault.created"]`

        - `"vault.created"`

      - `workspace_id: str`

    - `class BetaWebhookVaultArchivedEventData: …`

      - `id: str`

        ID of the resource that triggered the event.

      - `organization_id: str`

      - `type: Literal["vault.archived"]`

        - `"vault.archived"`

      - `workspace_id: str`

    - `class BetaWebhookVaultDeletedEventData: …`

      - `id: str`

        ID of the resource that triggered the event.

      - `organization_id: str`

      - `type: Literal["vault.deleted"]`

        - `"vault.deleted"`

      - `workspace_id: str`

    - `class BetaWebhookVaultCredentialCreatedEventData: …`

      - `id: str`

        ID of the resource that triggered the event.

      - `organization_id: str`

      - `type: Literal["vault_credential.created"]`

        - `"vault_credential.created"`

      - `vault_id: str`

        ID of the vault that owns this credential.

      - `workspace_id: str`

    - `class BetaWebhookVaultCredentialArchivedEventData: …`

      - `id: str`

        ID of the resource that triggered the event.

      - `organization_id: str`

      - `type: Literal["vault_credential.archived"]`

        - `"vault_credential.archived"`

      - `vault_id: str`

        ID of the vault that owns this credential.

      - `workspace_id: str`

    - `class BetaWebhookVaultCredentialDeletedEventData: …`

      - `id: str`

        ID of the resource that triggered the event.

      - `organization_id: str`

      - `type: Literal["vault_credential.deleted"]`

        - `"vault_credential.deleted"`

      - `vault_id: str`

        ID of the vault that owns this credential.

      - `workspace_id: str`

    - `class BetaWebhookVaultCredentialRefreshFailedEventData: …`

      - `id: str`

        ID of the resource that triggered the event.

      - `organization_id: str`

      - `type: Literal["vault_credential.refresh_failed"]`

        - `"vault_credential.refresh_failed"`

      - `vault_id: str`

        ID of the vault that owns this credential.

      - `workspace_id: str`

  - `type: Literal["event"]`

    Object type. Always `event` for webhook payloads.

    - `"event"`

### Beta Webhook Event Data

- `BetaWebhookEventData`

  - `class BetaWebhookSessionCreatedEventData: …`

    - `id: str`

      ID of the resource that triggered the event.

    - `organization_id: str`

    - `type: Literal["session.created"]`

      - `"session.created"`

    - `workspace_id: str`

  - `class BetaWebhookSessionPendingEventData: …`

    - `id: str`

      ID of the resource that triggered the event.

    - `organization_id: str`

    - `type: Literal["session.pending"]`

      - `"session.pending"`

    - `workspace_id: str`

  - `class BetaWebhookSessionRunningEventData: …`

    - `id: str`

      ID of the resource that triggered the event.

    - `organization_id: str`

    - `type: Literal["session.running"]`

      - `"session.running"`

    - `workspace_id: str`

  - `class BetaWebhookSessionIdledEventData: …`

    - `id: str`

      ID of the resource that triggered the event.

    - `organization_id: str`

    - `type: Literal["session.idled"]`

      - `"session.idled"`

    - `workspace_id: str`

  - `class BetaWebhookSessionRequiresActionEventData: …`

    - `id: str`

      ID of the resource that triggered the event.

    - `organization_id: str`

    - `type: Literal["session.requires_action"]`

      - `"session.requires_action"`

    - `workspace_id: str`

  - `class BetaWebhookSessionArchivedEventData: …`

    - `id: str`

      ID of the resource that triggered the event.

    - `organization_id: str`

    - `type: Literal["session.archived"]`

      - `"session.archived"`

    - `workspace_id: str`

  - `class BetaWebhookSessionDeletedEventData: …`

    - `id: str`

      ID of the resource that triggered the event.

    - `organization_id: str`

    - `type: Literal["session.deleted"]`

      - `"session.deleted"`

    - `workspace_id: str`

  - `class BetaWebhookSessionStatusRescheduledEventData: …`

    - `id: str`

      ID of the resource that triggered the event.

    - `organization_id: str`

    - `type: Literal["session.status_rescheduled"]`

      - `"session.status_rescheduled"`

    - `workspace_id: str`

  - `class BetaWebhookSessionStatusRunStartedEventData: …`

    - `id: str`

      ID of the resource that triggered the event.

    - `organization_id: str`

    - `type: Literal["session.status_run_started"]`

      - `"session.status_run_started"`

    - `workspace_id: str`

  - `class BetaWebhookSessionStatusIdledEventData: …`

    - `id: str`

      ID of the resource that triggered the event.

    - `organization_id: str`

    - `type: Literal["session.status_idled"]`

      - `"session.status_idled"`

    - `workspace_id: str`

  - `class BetaWebhookSessionStatusTerminatedEventData: …`

    - `id: str`

      ID of the resource that triggered the event.

    - `organization_id: str`

    - `type: Literal["session.status_terminated"]`

      - `"session.status_terminated"`

    - `workspace_id: str`

  - `class BetaWebhookSessionThreadCreatedEventData: …`

    - `id: str`

      ID of the resource that triggered the event.

    - `organization_id: str`

    - `type: Literal["session.thread_created"]`

      - `"session.thread_created"`

    - `workspace_id: str`

  - `class BetaWebhookSessionThreadIdledEventData: …`

    - `id: str`

      ID of the resource that triggered the event.

    - `organization_id: str`

    - `type: Literal["session.thread_idled"]`

      - `"session.thread_idled"`

    - `workspace_id: str`

  - `class BetaWebhookSessionThreadTerminatedEventData: …`

    - `id: str`

      ID of the resource that triggered the event.

    - `organization_id: str`

    - `type: Literal["session.thread_terminated"]`

      - `"session.thread_terminated"`

    - `workspace_id: str`

  - `class BetaWebhookSessionOutcomeEvaluationEndedEventData: …`

    - `id: str`

      ID of the resource that triggered the event.

    - `organization_id: str`

    - `type: Literal["session.outcome_evaluation_ended"]`

      - `"session.outcome_evaluation_ended"`

    - `workspace_id: str`

  - `class BetaWebhookVaultCreatedEventData: …`

    - `id: str`

      ID of the resource that triggered the event.

    - `organization_id: str`

    - `type: Literal["vault.created"]`

      - `"vault.created"`

    - `workspace_id: str`

  - `class BetaWebhookVaultArchivedEventData: …`

    - `id: str`

      ID of the resource that triggered the event.

    - `organization_id: str`

    - `type: Literal["vault.archived"]`

      - `"vault.archived"`

    - `workspace_id: str`

  - `class BetaWebhookVaultDeletedEventData: …`

    - `id: str`

      ID of the resource that triggered the event.

    - `organization_id: str`

    - `type: Literal["vault.deleted"]`

      - `"vault.deleted"`

    - `workspace_id: str`

  - `class BetaWebhookVaultCredentialCreatedEventData: …`

    - `id: str`

      ID of the resource that triggered the event.

    - `organization_id: str`

    - `type: Literal["vault_credential.created"]`

      - `"vault_credential.created"`

    - `vault_id: str`

      ID of the vault that owns this credential.

    - `workspace_id: str`

  - `class BetaWebhookVaultCredentialArchivedEventData: …`

    - `id: str`

      ID of the resource that triggered the event.

    - `organization_id: str`

    - `type: Literal["vault_credential.archived"]`

      - `"vault_credential.archived"`

    - `vault_id: str`

      ID of the vault that owns this credential.

    - `workspace_id: str`

  - `class BetaWebhookVaultCredentialDeletedEventData: …`

    - `id: str`

      ID of the resource that triggered the event.

    - `organization_id: str`

    - `type: Literal["vault_credential.deleted"]`

      - `"vault_credential.deleted"`

    - `vault_id: str`

      ID of the vault that owns this credential.

    - `workspace_id: str`

  - `class BetaWebhookVaultCredentialRefreshFailedEventData: …`

    - `id: str`

      ID of the resource that triggered the event.

    - `organization_id: str`

    - `type: Literal["vault_credential.refresh_failed"]`

      - `"vault_credential.refresh_failed"`

    - `vault_id: str`

      ID of the vault that owns this credential.

    - `workspace_id: str`

### Beta Webhook Session Archived Event Data

- `class BetaWebhookSessionArchivedEventData: …`

  - `id: str`

    ID of the resource that triggered the event.

  - `organization_id: str`

  - `type: Literal["session.archived"]`

    - `"session.archived"`

  - `workspace_id: str`

### Beta Webhook Session Created Event Data

- `class BetaWebhookSessionCreatedEventData: …`

  - `id: str`

    ID of the resource that triggered the event.

  - `organization_id: str`

  - `type: Literal["session.created"]`

    - `"session.created"`

  - `workspace_id: str`

### Beta Webhook Session Deleted Event Data

- `class BetaWebhookSessionDeletedEventData: …`

  - `id: str`

    ID of the resource that triggered the event.

  - `organization_id: str`

  - `type: Literal["session.deleted"]`

    - `"session.deleted"`

  - `workspace_id: str`

### Beta Webhook Session Idled Event Data

- `class BetaWebhookSessionIdledEventData: …`

  - `id: str`

    ID of the resource that triggered the event.

  - `organization_id: str`

  - `type: Literal["session.idled"]`

    - `"session.idled"`

  - `workspace_id: str`

### Beta Webhook Session Outcome Evaluation Ended Event Data

- `class BetaWebhookSessionOutcomeEvaluationEndedEventData: …`

  - `id: str`

    ID of the resource that triggered the event.

  - `organization_id: str`

  - `type: Literal["session.outcome_evaluation_ended"]`

    - `"session.outcome_evaluation_ended"`

  - `workspace_id: str`

### Beta Webhook Session Pending Event Data

- `class BetaWebhookSessionPendingEventData: …`

  - `id: str`

    ID of the resource that triggered the event.

  - `organization_id: str`

  - `type: Literal["session.pending"]`

    - `"session.pending"`

  - `workspace_id: str`

### Beta Webhook Session Requires Action Event Data

- `class BetaWebhookSessionRequiresActionEventData: …`

  - `id: str`

    ID of the resource that triggered the event.

  - `organization_id: str`

  - `type: Literal["session.requires_action"]`

    - `"session.requires_action"`

  - `workspace_id: str`

### Beta Webhook Session Running Event Data

- `class BetaWebhookSessionRunningEventData: …`

  - `id: str`

    ID of the resource that triggered the event.

  - `organization_id: str`

  - `type: Literal["session.running"]`

    - `"session.running"`

  - `workspace_id: str`

### Beta Webhook Session Status Idled Event Data

- `class BetaWebhookSessionStatusIdledEventData: …`

  - `id: str`

    ID of the resource that triggered the event.

  - `organization_id: str`

  - `type: Literal["session.status_idled"]`

    - `"session.status_idled"`

  - `workspace_id: str`

### Beta Webhook Session Status Rescheduled Event Data

- `class BetaWebhookSessionStatusRescheduledEventData: …`

  - `id: str`

    ID of the resource that triggered the event.

  - `organization_id: str`

  - `type: Literal["session.status_rescheduled"]`

    - `"session.status_rescheduled"`

  - `workspace_id: str`

### Beta Webhook Session Status Run Started Event Data

- `class BetaWebhookSessionStatusRunStartedEventData: …`

  - `id: str`

    ID of the resource that triggered the event.

  - `organization_id: str`

  - `type: Literal["session.status_run_started"]`

    - `"session.status_run_started"`

  - `workspace_id: str`

### Beta Webhook Session Status Terminated Event Data

- `class BetaWebhookSessionStatusTerminatedEventData: …`

  - `id: str`

    ID of the resource that triggered the event.

  - `organization_id: str`

  - `type: Literal["session.status_terminated"]`

    - `"session.status_terminated"`

  - `workspace_id: str`

### Beta Webhook Session Thread Created Event Data

- `class BetaWebhookSessionThreadCreatedEventData: …`

  - `id: str`

    ID of the resource that triggered the event.

  - `organization_id: str`

  - `type: Literal["session.thread_created"]`

    - `"session.thread_created"`

  - `workspace_id: str`

### Beta Webhook Session Thread Idled Event Data

- `class BetaWebhookSessionThreadIdledEventData: …`

  - `id: str`

    ID of the resource that triggered the event.

  - `organization_id: str`

  - `type: Literal["session.thread_idled"]`

    - `"session.thread_idled"`

  - `workspace_id: str`

### Beta Webhook Session Thread Terminated Event Data

- `class BetaWebhookSessionThreadTerminatedEventData: …`

  - `id: str`

    ID of the resource that triggered the event.

  - `organization_id: str`

  - `type: Literal["session.thread_terminated"]`

    - `"session.thread_terminated"`

  - `workspace_id: str`

### Beta Webhook Vault Archived Event Data

- `class BetaWebhookVaultArchivedEventData: …`

  - `id: str`

    ID of the resource that triggered the event.

  - `organization_id: str`

  - `type: Literal["vault.archived"]`

    - `"vault.archived"`

  - `workspace_id: str`

### Beta Webhook Vault Created Event Data

- `class BetaWebhookVaultCreatedEventData: …`

  - `id: str`

    ID of the resource that triggered the event.

  - `organization_id: str`

  - `type: Literal["vault.created"]`

    - `"vault.created"`

  - `workspace_id: str`

### Beta Webhook Vault Credential Archived Event Data

- `class BetaWebhookVaultCredentialArchivedEventData: …`

  - `id: str`

    ID of the resource that triggered the event.

  - `organization_id: str`

  - `type: Literal["vault_credential.archived"]`

    - `"vault_credential.archived"`

  - `vault_id: str`

    ID of the vault that owns this credential.

  - `workspace_id: str`

### Beta Webhook Vault Credential Created Event Data

- `class BetaWebhookVaultCredentialCreatedEventData: …`

  - `id: str`

    ID of the resource that triggered the event.

  - `organization_id: str`

  - `type: Literal["vault_credential.created"]`

    - `"vault_credential.created"`

  - `vault_id: str`

    ID of the vault that owns this credential.

  - `workspace_id: str`

### Beta Webhook Vault Credential Deleted Event Data

- `class BetaWebhookVaultCredentialDeletedEventData: …`

  - `id: str`

    ID of the resource that triggered the event.

  - `organization_id: str`

  - `type: Literal["vault_credential.deleted"]`

    - `"vault_credential.deleted"`

  - `vault_id: str`

    ID of the vault that owns this credential.

  - `workspace_id: str`

### Beta Webhook Vault Credential Refresh Failed Event Data

- `class BetaWebhookVaultCredentialRefreshFailedEventData: …`

  - `id: str`

    ID of the resource that triggered the event.

  - `organization_id: str`

  - `type: Literal["vault_credential.refresh_failed"]`

    - `"vault_credential.refresh_failed"`

  - `vault_id: str`

    ID of the vault that owns this credential.

  - `workspace_id: str`

### Beta Webhook Vault Deleted Event Data

- `class BetaWebhookVaultDeletedEventData: …`

  - `id: str`

    ID of the resource that triggered the event.

  - `organization_id: str`

  - `type: Literal["vault.deleted"]`

    - `"vault.deleted"`

  - `workspace_id: str`

### Unwrap Webhook Event

- `class UnwrapWebhookEvent: …`

  - `id: str`

    Unique event identifier for idempotency.

  - `created_at: datetime`

    RFC 3339 timestamp when the event occurred.

  - `data: BetaWebhookEventData`

    - `class BetaWebhookSessionCreatedEventData: …`

      - `id: str`

        ID of the resource that triggered the event.

      - `organization_id: str`

      - `type: Literal["session.created"]`

        - `"session.created"`

      - `workspace_id: str`

    - `class BetaWebhookSessionPendingEventData: …`

      - `id: str`

        ID of the resource that triggered the event.

      - `organization_id: str`

      - `type: Literal["session.pending"]`

        - `"session.pending"`

      - `workspace_id: str`

    - `class BetaWebhookSessionRunningEventData: …`

      - `id: str`

        ID of the resource that triggered the event.

      - `organization_id: str`

      - `type: Literal["session.running"]`

        - `"session.running"`

      - `workspace_id: str`

    - `class BetaWebhookSessionIdledEventData: …`

      - `id: str`

        ID of the resource that triggered the event.

      - `organization_id: str`

      - `type: Literal["session.idled"]`

        - `"session.idled"`

      - `workspace_id: str`

    - `class BetaWebhookSessionRequiresActionEventData: …`

      - `id: str`

        ID of the resource that triggered the event.

      - `organization_id: str`

      - `type: Literal["session.requires_action"]`

        - `"session.requires_action"`

      - `workspace_id: str`

    - `class BetaWebhookSessionArchivedEventData: …`

      - `id: str`

        ID of the resource that triggered the event.

      - `organization_id: str`

      - `type: Literal["session.archived"]`

        - `"session.archived"`

      - `workspace_id: str`

    - `class BetaWebhookSessionDeletedEventData: …`

      - `id: str`

        ID of the resource that triggered the event.

      - `organization_id: str`

      - `type: Literal["session.deleted"]`

        - `"session.deleted"`

      - `workspace_id: str`

    - `class BetaWebhookSessionStatusRescheduledEventData: …`

      - `id: str`

        ID of the resource that triggered the event.

      - `organization_id: str`

      - `type: Literal["session.status_rescheduled"]`

        - `"session.status_rescheduled"`

      - `workspace_id: str`

    - `class BetaWebhookSessionStatusRunStartedEventData: …`

      - `id: str`

        ID of the resource that triggered the event.

      - `organization_id: str`

      - `type: Literal["session.status_run_started"]`

        - `"session.status_run_started"`

      - `workspace_id: str`

    - `class BetaWebhookSessionStatusIdledEventData: …`

      - `id: str`

        ID of the resource that triggered the event.

      - `organization_id: str`

      - `type: Literal["session.status_idled"]`

        - `"session.status_idled"`

      - `workspace_id: str`

    - `class BetaWebhookSessionStatusTerminatedEventData: …`

      - `id: str`

        ID of the resource that triggered the event.

      - `organization_id: str`

      - `type: Literal["session.status_terminated"]`

        - `"session.status_terminated"`

      - `workspace_id: str`

    - `class BetaWebhookSessionThreadCreatedEventData: …`

      - `id: str`

        ID of the resource that triggered the event.

      - `organization_id: str`

      - `type: Literal["session.thread_created"]`

        - `"session.thread_created"`

      - `workspace_id: str`

    - `class BetaWebhookSessionThreadIdledEventData: …`

      - `id: str`

        ID of the resource that triggered the event.

      - `organization_id: str`

      - `type: Literal["session.thread_idled"]`

        - `"session.thread_idled"`

      - `workspace_id: str`

    - `class BetaWebhookSessionThreadTerminatedEventData: …`

      - `id: str`

        ID of the resource that triggered the event.

      - `organization_id: str`

      - `type: Literal["session.thread_terminated"]`

        - `"session.thread_terminated"`

      - `workspace_id: str`

    - `class BetaWebhookSessionOutcomeEvaluationEndedEventData: …`

      - `id: str`

        ID of the resource that triggered the event.

      - `organization_id: str`

      - `type: Literal["session.outcome_evaluation_ended"]`

        - `"session.outcome_evaluation_ended"`

      - `workspace_id: str`

    - `class BetaWebhookVaultCreatedEventData: …`

      - `id: str`

        ID of the resource that triggered the event.

      - `organization_id: str`

      - `type: Literal["vault.created"]`

        - `"vault.created"`

      - `workspace_id: str`

    - `class BetaWebhookVaultArchivedEventData: …`

      - `id: str`

        ID of the resource that triggered the event.

      - `organization_id: str`

      - `type: Literal["vault.archived"]`

        - `"vault.archived"`

      - `workspace_id: str`

    - `class BetaWebhookVaultDeletedEventData: …`

      - `id: str`

        ID of the resource that triggered the event.

      - `organization_id: str`

      - `type: Literal["vault.deleted"]`

        - `"vault.deleted"`

      - `workspace_id: str`

    - `class BetaWebhookVaultCredentialCreatedEventData: …`

      - `id: str`

        ID of the resource that triggered the event.

      - `organization_id: str`

      - `type: Literal["vault_credential.created"]`

        - `"vault_credential.created"`

      - `vault_id: str`

        ID of the vault that owns this credential.

      - `workspace_id: str`

    - `class BetaWebhookVaultCredentialArchivedEventData: …`

      - `id: str`

        ID of the resource that triggered the event.

      - `organization_id: str`

      - `type: Literal["vault_credential.archived"]`

        - `"vault_credential.archived"`

      - `vault_id: str`

        ID of the vault that owns this credential.

      - `workspace_id: str`

    - `class BetaWebhookVaultCredentialDeletedEventData: …`

      - `id: str`

        ID of the resource that triggered the event.

      - `organization_id: str`

      - `type: Literal["vault_credential.deleted"]`

        - `"vault_credential.deleted"`

      - `vault_id: str`

        ID of the vault that owns this credential.

      - `workspace_id: str`

    - `class BetaWebhookVaultCredentialRefreshFailedEventData: …`

      - `id: str`

        ID of the resource that triggered the event.

      - `organization_id: str`

      - `type: Literal["vault_credential.refresh_failed"]`

        - `"vault_credential.refresh_failed"`

      - `vault_id: str`

        ID of the vault that owns this credential.

      - `workspace_id: str`

  - `type: Literal["event"]`

    Object type. Always `event` for webhook payloads.

    - `"event"`
