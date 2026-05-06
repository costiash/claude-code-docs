# Webhooks

## Domain Types

### Beta Webhook Event

- `beta_webhook_event: object { id, created_at, data, type }`

  - `id: string`

    Unique event identifier for idempotency.

  - `created_at: string`

    RFC 3339 timestamp when the event occurred.

  - `data: BetaWebhookSessionCreatedEventData or BetaWebhookSessionPendingEventData or BetaWebhookSessionRunningEventData or 19 more`

    - `beta_webhook_session_created_event_data: object { id, organization_id, type, workspace_id }`

      - `id: string`

        ID of the resource that triggered the event.

      - `organization_id: string`

      - `type: "session.created"`

      - `workspace_id: string`

    - `beta_webhook_session_pending_event_data: object { id, organization_id, type, workspace_id }`

      - `id: string`

        ID of the resource that triggered the event.

      - `organization_id: string`

      - `type: "session.pending"`

      - `workspace_id: string`

    - `beta_webhook_session_running_event_data: object { id, organization_id, type, workspace_id }`

      - `id: string`

        ID of the resource that triggered the event.

      - `organization_id: string`

      - `type: "session.running"`

      - `workspace_id: string`

    - `beta_webhook_session_idled_event_data: object { id, organization_id, type, workspace_id }`

      - `id: string`

        ID of the resource that triggered the event.

      - `organization_id: string`

      - `type: "session.idled"`

      - `workspace_id: string`

    - `beta_webhook_session_requires_action_event_data: object { id, organization_id, type, workspace_id }`

      - `id: string`

        ID of the resource that triggered the event.

      - `organization_id: string`

      - `type: "session.requires_action"`

      - `workspace_id: string`

    - `beta_webhook_session_archived_event_data: object { id, organization_id, type, workspace_id }`

      - `id: string`

        ID of the resource that triggered the event.

      - `organization_id: string`

      - `type: "session.archived"`

      - `workspace_id: string`

    - `beta_webhook_session_deleted_event_data: object { id, organization_id, type, workspace_id }`

      - `id: string`

        ID of the resource that triggered the event.

      - `organization_id: string`

      - `type: "session.deleted"`

      - `workspace_id: string`

    - `beta_webhook_session_status_scheduled_event_data: object { id, organization_id, type, workspace_id }`

      - `id: string`

        ID of the resource that triggered the event.

      - `organization_id: string`

      - `type: "session.status_scheduled"`

      - `workspace_id: string`

    - `beta_webhook_session_status_run_started_event_data: object { id, organization_id, type, workspace_id }`

      - `id: string`

        ID of the resource that triggered the event.

      - `organization_id: string`

      - `type: "session.status_run_started"`

      - `workspace_id: string`

    - `beta_webhook_session_status_idled_event_data: object { id, organization_id, type, workspace_id }`

      - `id: string`

        ID of the resource that triggered the event.

      - `organization_id: string`

      - `type: "session.status_idled"`

      - `workspace_id: string`

    - `beta_webhook_session_status_terminated_event_data: object { id, organization_id, type, workspace_id }`

      - `id: string`

        ID of the resource that triggered the event.

      - `organization_id: string`

      - `type: "session.status_terminated"`

      - `workspace_id: string`

    - `beta_webhook_session_thread_created_event_data: object { id, organization_id, type, workspace_id }`

      - `id: string`

        ID of the resource that triggered the event.

      - `organization_id: string`

      - `type: "session.thread_created"`

      - `workspace_id: string`

    - `beta_webhook_session_thread_idled_event_data: object { id, organization_id, type, workspace_id }`

      - `id: string`

        ID of the resource that triggered the event.

      - `organization_id: string`

      - `type: "session.thread_idled"`

      - `workspace_id: string`

    - `beta_webhook_session_thread_terminated_event_data: object { id, organization_id, type, workspace_id }`

      - `id: string`

        ID of the resource that triggered the event.

      - `organization_id: string`

      - `type: "session.thread_terminated"`

      - `workspace_id: string`

    - `beta_webhook_session_outcome_evaluation_ended_event_data: object { id, organization_id, type, workspace_id }`

      - `id: string`

        ID of the resource that triggered the event.

      - `organization_id: string`

      - `type: "session.outcome_evaluation_ended"`

      - `workspace_id: string`

    - `beta_webhook_vault_created_event_data: object { id, organization_id, type, workspace_id }`

      - `id: string`

        ID of the resource that triggered the event.

      - `organization_id: string`

      - `type: "vault.created"`

      - `workspace_id: string`

    - `beta_webhook_vault_archived_event_data: object { id, organization_id, type, workspace_id }`

      - `id: string`

        ID of the resource that triggered the event.

      - `organization_id: string`

      - `type: "vault.archived"`

      - `workspace_id: string`

    - `beta_webhook_vault_deleted_event_data: object { id, organization_id, type, workspace_id }`

      - `id: string`

        ID of the resource that triggered the event.

      - `organization_id: string`

      - `type: "vault.deleted"`

      - `workspace_id: string`

    - `beta_webhook_vault_credential_created_event_data: object { id, organization_id, type, 2 more }`

      - `id: string`

        ID of the resource that triggered the event.

      - `organization_id: string`

      - `type: "vault_credential.created"`

      - `vault_id: string`

        ID of the vault that owns this credential.

      - `workspace_id: string`

    - `beta_webhook_vault_credential_archived_event_data: object { id, organization_id, type, 2 more }`

      - `id: string`

        ID of the resource that triggered the event.

      - `organization_id: string`

      - `type: "vault_credential.archived"`

      - `vault_id: string`

        ID of the vault that owns this credential.

      - `workspace_id: string`

    - `beta_webhook_vault_credential_deleted_event_data: object { id, organization_id, type, 2 more }`

      - `id: string`

        ID of the resource that triggered the event.

      - `organization_id: string`

      - `type: "vault_credential.deleted"`

      - `vault_id: string`

        ID of the vault that owns this credential.

      - `workspace_id: string`

    - `beta_webhook_vault_credential_refresh_failed_event_data: object { id, organization_id, type, 2 more }`

      - `id: string`

        ID of the resource that triggered the event.

      - `organization_id: string`

      - `type: "vault_credential.refresh_failed"`

      - `vault_id: string`

        ID of the vault that owns this credential.

      - `workspace_id: string`

  - `type: "event"`

    Object type. Always `event` for webhook payloads.

### Beta Webhook Event Data

- `beta_webhook_event_data: BetaWebhookSessionCreatedEventData or BetaWebhookSessionPendingEventData or BetaWebhookSessionRunningEventData or 19 more`

  - `beta_webhook_session_created_event_data: object { id, organization_id, type, workspace_id }`

    - `id: string`

      ID of the resource that triggered the event.

    - `organization_id: string`

    - `type: "session.created"`

    - `workspace_id: string`

  - `beta_webhook_session_pending_event_data: object { id, organization_id, type, workspace_id }`

    - `id: string`

      ID of the resource that triggered the event.

    - `organization_id: string`

    - `type: "session.pending"`

    - `workspace_id: string`

  - `beta_webhook_session_running_event_data: object { id, organization_id, type, workspace_id }`

    - `id: string`

      ID of the resource that triggered the event.

    - `organization_id: string`

    - `type: "session.running"`

    - `workspace_id: string`

  - `beta_webhook_session_idled_event_data: object { id, organization_id, type, workspace_id }`

    - `id: string`

      ID of the resource that triggered the event.

    - `organization_id: string`

    - `type: "session.idled"`

    - `workspace_id: string`

  - `beta_webhook_session_requires_action_event_data: object { id, organization_id, type, workspace_id }`

    - `id: string`

      ID of the resource that triggered the event.

    - `organization_id: string`

    - `type: "session.requires_action"`

    - `workspace_id: string`

  - `beta_webhook_session_archived_event_data: object { id, organization_id, type, workspace_id }`

    - `id: string`

      ID of the resource that triggered the event.

    - `organization_id: string`

    - `type: "session.archived"`

    - `workspace_id: string`

  - `beta_webhook_session_deleted_event_data: object { id, organization_id, type, workspace_id }`

    - `id: string`

      ID of the resource that triggered the event.

    - `organization_id: string`

    - `type: "session.deleted"`

    - `workspace_id: string`

  - `beta_webhook_session_status_scheduled_event_data: object { id, organization_id, type, workspace_id }`

    - `id: string`

      ID of the resource that triggered the event.

    - `organization_id: string`

    - `type: "session.status_scheduled"`

    - `workspace_id: string`

  - `beta_webhook_session_status_run_started_event_data: object { id, organization_id, type, workspace_id }`

    - `id: string`

      ID of the resource that triggered the event.

    - `organization_id: string`

    - `type: "session.status_run_started"`

    - `workspace_id: string`

  - `beta_webhook_session_status_idled_event_data: object { id, organization_id, type, workspace_id }`

    - `id: string`

      ID of the resource that triggered the event.

    - `organization_id: string`

    - `type: "session.status_idled"`

    - `workspace_id: string`

  - `beta_webhook_session_status_terminated_event_data: object { id, organization_id, type, workspace_id }`

    - `id: string`

      ID of the resource that triggered the event.

    - `organization_id: string`

    - `type: "session.status_terminated"`

    - `workspace_id: string`

  - `beta_webhook_session_thread_created_event_data: object { id, organization_id, type, workspace_id }`

    - `id: string`

      ID of the resource that triggered the event.

    - `organization_id: string`

    - `type: "session.thread_created"`

    - `workspace_id: string`

  - `beta_webhook_session_thread_idled_event_data: object { id, organization_id, type, workspace_id }`

    - `id: string`

      ID of the resource that triggered the event.

    - `organization_id: string`

    - `type: "session.thread_idled"`

    - `workspace_id: string`

  - `beta_webhook_session_thread_terminated_event_data: object { id, organization_id, type, workspace_id }`

    - `id: string`

      ID of the resource that triggered the event.

    - `organization_id: string`

    - `type: "session.thread_terminated"`

    - `workspace_id: string`

  - `beta_webhook_session_outcome_evaluation_ended_event_data: object { id, organization_id, type, workspace_id }`

    - `id: string`

      ID of the resource that triggered the event.

    - `organization_id: string`

    - `type: "session.outcome_evaluation_ended"`

    - `workspace_id: string`

  - `beta_webhook_vault_created_event_data: object { id, organization_id, type, workspace_id }`

    - `id: string`

      ID of the resource that triggered the event.

    - `organization_id: string`

    - `type: "vault.created"`

    - `workspace_id: string`

  - `beta_webhook_vault_archived_event_data: object { id, organization_id, type, workspace_id }`

    - `id: string`

      ID of the resource that triggered the event.

    - `organization_id: string`

    - `type: "vault.archived"`

    - `workspace_id: string`

  - `beta_webhook_vault_deleted_event_data: object { id, organization_id, type, workspace_id }`

    - `id: string`

      ID of the resource that triggered the event.

    - `organization_id: string`

    - `type: "vault.deleted"`

    - `workspace_id: string`

  - `beta_webhook_vault_credential_created_event_data: object { id, organization_id, type, 2 more }`

    - `id: string`

      ID of the resource that triggered the event.

    - `organization_id: string`

    - `type: "vault_credential.created"`

    - `vault_id: string`

      ID of the vault that owns this credential.

    - `workspace_id: string`

  - `beta_webhook_vault_credential_archived_event_data: object { id, organization_id, type, 2 more }`

    - `id: string`

      ID of the resource that triggered the event.

    - `organization_id: string`

    - `type: "vault_credential.archived"`

    - `vault_id: string`

      ID of the vault that owns this credential.

    - `workspace_id: string`

  - `beta_webhook_vault_credential_deleted_event_data: object { id, organization_id, type, 2 more }`

    - `id: string`

      ID of the resource that triggered the event.

    - `organization_id: string`

    - `type: "vault_credential.deleted"`

    - `vault_id: string`

      ID of the vault that owns this credential.

    - `workspace_id: string`

  - `beta_webhook_vault_credential_refresh_failed_event_data: object { id, organization_id, type, 2 more }`

    - `id: string`

      ID of the resource that triggered the event.

    - `organization_id: string`

    - `type: "vault_credential.refresh_failed"`

    - `vault_id: string`

      ID of the vault that owns this credential.

    - `workspace_id: string`

### Beta Webhook Session Archived Event Data

- `beta_webhook_session_archived_event_data: object { id, organization_id, type, workspace_id }`

  - `id: string`

    ID of the resource that triggered the event.

  - `organization_id: string`

  - `type: "session.archived"`

  - `workspace_id: string`

### Beta Webhook Session Created Event Data

- `beta_webhook_session_created_event_data: object { id, organization_id, type, workspace_id }`

  - `id: string`

    ID of the resource that triggered the event.

  - `organization_id: string`

  - `type: "session.created"`

  - `workspace_id: string`

### Beta Webhook Session Deleted Event Data

- `beta_webhook_session_deleted_event_data: object { id, organization_id, type, workspace_id }`

  - `id: string`

    ID of the resource that triggered the event.

  - `organization_id: string`

  - `type: "session.deleted"`

  - `workspace_id: string`

### Beta Webhook Session Idled Event Data

- `beta_webhook_session_idled_event_data: object { id, organization_id, type, workspace_id }`

  - `id: string`

    ID of the resource that triggered the event.

  - `organization_id: string`

  - `type: "session.idled"`

  - `workspace_id: string`

### Beta Webhook Session Outcome Evaluation Ended Event Data

- `beta_webhook_session_outcome_evaluation_ended_event_data: object { id, organization_id, type, workspace_id }`

  - `id: string`

    ID of the resource that triggered the event.

  - `organization_id: string`

  - `type: "session.outcome_evaluation_ended"`

  - `workspace_id: string`

### Beta Webhook Session Pending Event Data

- `beta_webhook_session_pending_event_data: object { id, organization_id, type, workspace_id }`

  - `id: string`

    ID of the resource that triggered the event.

  - `organization_id: string`

  - `type: "session.pending"`

  - `workspace_id: string`

### Beta Webhook Session Requires Action Event Data

- `beta_webhook_session_requires_action_event_data: object { id, organization_id, type, workspace_id }`

  - `id: string`

    ID of the resource that triggered the event.

  - `organization_id: string`

  - `type: "session.requires_action"`

  - `workspace_id: string`

### Beta Webhook Session Running Event Data

- `beta_webhook_session_running_event_data: object { id, organization_id, type, workspace_id }`

  - `id: string`

    ID of the resource that triggered the event.

  - `organization_id: string`

  - `type: "session.running"`

  - `workspace_id: string`

### Beta Webhook Session Status Idled Event Data

- `beta_webhook_session_status_idled_event_data: object { id, organization_id, type, workspace_id }`

  - `id: string`

    ID of the resource that triggered the event.

  - `organization_id: string`

  - `type: "session.status_idled"`

  - `workspace_id: string`

### Beta Webhook Session Status Run Started Event Data

- `beta_webhook_session_status_run_started_event_data: object { id, organization_id, type, workspace_id }`

  - `id: string`

    ID of the resource that triggered the event.

  - `organization_id: string`

  - `type: "session.status_run_started"`

  - `workspace_id: string`

### Beta Webhook Session Status Scheduled Event Data

- `beta_webhook_session_status_scheduled_event_data: object { id, organization_id, type, workspace_id }`

  - `id: string`

    ID of the resource that triggered the event.

  - `organization_id: string`

  - `type: "session.status_scheduled"`

  - `workspace_id: string`

### Beta Webhook Session Status Terminated Event Data

- `beta_webhook_session_status_terminated_event_data: object { id, organization_id, type, workspace_id }`

  - `id: string`

    ID of the resource that triggered the event.

  - `organization_id: string`

  - `type: "session.status_terminated"`

  - `workspace_id: string`

### Beta Webhook Session Thread Created Event Data

- `beta_webhook_session_thread_created_event_data: object { id, organization_id, type, workspace_id }`

  - `id: string`

    ID of the resource that triggered the event.

  - `organization_id: string`

  - `type: "session.thread_created"`

  - `workspace_id: string`

### Beta Webhook Session Thread Idled Event Data

- `beta_webhook_session_thread_idled_event_data: object { id, organization_id, type, workspace_id }`

  - `id: string`

    ID of the resource that triggered the event.

  - `organization_id: string`

  - `type: "session.thread_idled"`

  - `workspace_id: string`

### Beta Webhook Session Thread Terminated Event Data

- `beta_webhook_session_thread_terminated_event_data: object { id, organization_id, type, workspace_id }`

  - `id: string`

    ID of the resource that triggered the event.

  - `organization_id: string`

  - `type: "session.thread_terminated"`

  - `workspace_id: string`

### Beta Webhook Vault Archived Event Data

- `beta_webhook_vault_archived_event_data: object { id, organization_id, type, workspace_id }`

  - `id: string`

    ID of the resource that triggered the event.

  - `organization_id: string`

  - `type: "vault.archived"`

  - `workspace_id: string`

### Beta Webhook Vault Created Event Data

- `beta_webhook_vault_created_event_data: object { id, organization_id, type, workspace_id }`

  - `id: string`

    ID of the resource that triggered the event.

  - `organization_id: string`

  - `type: "vault.created"`

  - `workspace_id: string`

### Beta Webhook Vault Credential Archived Event Data

- `beta_webhook_vault_credential_archived_event_data: object { id, organization_id, type, 2 more }`

  - `id: string`

    ID of the resource that triggered the event.

  - `organization_id: string`

  - `type: "vault_credential.archived"`

  - `vault_id: string`

    ID of the vault that owns this credential.

  - `workspace_id: string`

### Beta Webhook Vault Credential Created Event Data

- `beta_webhook_vault_credential_created_event_data: object { id, organization_id, type, 2 more }`

  - `id: string`

    ID of the resource that triggered the event.

  - `organization_id: string`

  - `type: "vault_credential.created"`

  - `vault_id: string`

    ID of the vault that owns this credential.

  - `workspace_id: string`

### Beta Webhook Vault Credential Deleted Event Data

- `beta_webhook_vault_credential_deleted_event_data: object { id, organization_id, type, 2 more }`

  - `id: string`

    ID of the resource that triggered the event.

  - `organization_id: string`

  - `type: "vault_credential.deleted"`

  - `vault_id: string`

    ID of the vault that owns this credential.

  - `workspace_id: string`

### Beta Webhook Vault Credential Refresh Failed Event Data

- `beta_webhook_vault_credential_refresh_failed_event_data: object { id, organization_id, type, 2 more }`

  - `id: string`

    ID of the resource that triggered the event.

  - `organization_id: string`

  - `type: "vault_credential.refresh_failed"`

  - `vault_id: string`

    ID of the vault that owns this credential.

  - `workspace_id: string`

### Beta Webhook Vault Deleted Event Data

- `beta_webhook_vault_deleted_event_data: object { id, organization_id, type, workspace_id }`

  - `id: string`

    ID of the resource that triggered the event.

  - `organization_id: string`

  - `type: "vault.deleted"`

  - `workspace_id: string`

### Unwrap Webhook Event

- `unwrap_webhook_event: object { id, created_at, data, type }`

  - `id: string`

    Unique event identifier for idempotency.

  - `created_at: string`

    RFC 3339 timestamp when the event occurred.

  - `data: BetaWebhookSessionCreatedEventData or BetaWebhookSessionPendingEventData or BetaWebhookSessionRunningEventData or 19 more`

    - `beta_webhook_session_created_event_data: object { id, organization_id, type, workspace_id }`

      - `id: string`

        ID of the resource that triggered the event.

      - `organization_id: string`

      - `type: "session.created"`

      - `workspace_id: string`

    - `beta_webhook_session_pending_event_data: object { id, organization_id, type, workspace_id }`

      - `id: string`

        ID of the resource that triggered the event.

      - `organization_id: string`

      - `type: "session.pending"`

      - `workspace_id: string`

    - `beta_webhook_session_running_event_data: object { id, organization_id, type, workspace_id }`

      - `id: string`

        ID of the resource that triggered the event.

      - `organization_id: string`

      - `type: "session.running"`

      - `workspace_id: string`

    - `beta_webhook_session_idled_event_data: object { id, organization_id, type, workspace_id }`

      - `id: string`

        ID of the resource that triggered the event.

      - `organization_id: string`

      - `type: "session.idled"`

      - `workspace_id: string`

    - `beta_webhook_session_requires_action_event_data: object { id, organization_id, type, workspace_id }`

      - `id: string`

        ID of the resource that triggered the event.

      - `organization_id: string`

      - `type: "session.requires_action"`

      - `workspace_id: string`

    - `beta_webhook_session_archived_event_data: object { id, organization_id, type, workspace_id }`

      - `id: string`

        ID of the resource that triggered the event.

      - `organization_id: string`

      - `type: "session.archived"`

      - `workspace_id: string`

    - `beta_webhook_session_deleted_event_data: object { id, organization_id, type, workspace_id }`

      - `id: string`

        ID of the resource that triggered the event.

      - `organization_id: string`

      - `type: "session.deleted"`

      - `workspace_id: string`

    - `beta_webhook_session_status_scheduled_event_data: object { id, organization_id, type, workspace_id }`

      - `id: string`

        ID of the resource that triggered the event.

      - `organization_id: string`

      - `type: "session.status_scheduled"`

      - `workspace_id: string`

    - `beta_webhook_session_status_run_started_event_data: object { id, organization_id, type, workspace_id }`

      - `id: string`

        ID of the resource that triggered the event.

      - `organization_id: string`

      - `type: "session.status_run_started"`

      - `workspace_id: string`

    - `beta_webhook_session_status_idled_event_data: object { id, organization_id, type, workspace_id }`

      - `id: string`

        ID of the resource that triggered the event.

      - `organization_id: string`

      - `type: "session.status_idled"`

      - `workspace_id: string`

    - `beta_webhook_session_status_terminated_event_data: object { id, organization_id, type, workspace_id }`

      - `id: string`

        ID of the resource that triggered the event.

      - `organization_id: string`

      - `type: "session.status_terminated"`

      - `workspace_id: string`

    - `beta_webhook_session_thread_created_event_data: object { id, organization_id, type, workspace_id }`

      - `id: string`

        ID of the resource that triggered the event.

      - `organization_id: string`

      - `type: "session.thread_created"`

      - `workspace_id: string`

    - `beta_webhook_session_thread_idled_event_data: object { id, organization_id, type, workspace_id }`

      - `id: string`

        ID of the resource that triggered the event.

      - `organization_id: string`

      - `type: "session.thread_idled"`

      - `workspace_id: string`

    - `beta_webhook_session_thread_terminated_event_data: object { id, organization_id, type, workspace_id }`

      - `id: string`

        ID of the resource that triggered the event.

      - `organization_id: string`

      - `type: "session.thread_terminated"`

      - `workspace_id: string`

    - `beta_webhook_session_outcome_evaluation_ended_event_data: object { id, organization_id, type, workspace_id }`

      - `id: string`

        ID of the resource that triggered the event.

      - `organization_id: string`

      - `type: "session.outcome_evaluation_ended"`

      - `workspace_id: string`

    - `beta_webhook_vault_created_event_data: object { id, organization_id, type, workspace_id }`

      - `id: string`

        ID of the resource that triggered the event.

      - `organization_id: string`

      - `type: "vault.created"`

      - `workspace_id: string`

    - `beta_webhook_vault_archived_event_data: object { id, organization_id, type, workspace_id }`

      - `id: string`

        ID of the resource that triggered the event.

      - `organization_id: string`

      - `type: "vault.archived"`

      - `workspace_id: string`

    - `beta_webhook_vault_deleted_event_data: object { id, organization_id, type, workspace_id }`

      - `id: string`

        ID of the resource that triggered the event.

      - `organization_id: string`

      - `type: "vault.deleted"`

      - `workspace_id: string`

    - `beta_webhook_vault_credential_created_event_data: object { id, organization_id, type, 2 more }`

      - `id: string`

        ID of the resource that triggered the event.

      - `organization_id: string`

      - `type: "vault_credential.created"`

      - `vault_id: string`

        ID of the vault that owns this credential.

      - `workspace_id: string`

    - `beta_webhook_vault_credential_archived_event_data: object { id, organization_id, type, 2 more }`

      - `id: string`

        ID of the resource that triggered the event.

      - `organization_id: string`

      - `type: "vault_credential.archived"`

      - `vault_id: string`

        ID of the vault that owns this credential.

      - `workspace_id: string`

    - `beta_webhook_vault_credential_deleted_event_data: object { id, organization_id, type, 2 more }`

      - `id: string`

        ID of the resource that triggered the event.

      - `organization_id: string`

      - `type: "vault_credential.deleted"`

      - `vault_id: string`

        ID of the vault that owns this credential.

      - `workspace_id: string`

    - `beta_webhook_vault_credential_refresh_failed_event_data: object { id, organization_id, type, 2 more }`

      - `id: string`

        ID of the resource that triggered the event.

      - `organization_id: string`

      - `type: "vault_credential.refresh_failed"`

      - `vault_id: string`

        ID of the vault that owns this credential.

      - `workspace_id: string`

  - `type: "event"`

    Object type. Always `event` for webhook payloads.
