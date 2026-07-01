# Webhooks

## Domain Types

### Beta Webhook Agent Archived Event Data

- `beta_webhook_agent_archived_event_data: object { id, organization_id, type, workspace_id }`

  - `id: string`

    ID of the agent that triggered the event.

  - `organization_id: string`

  - `type: "agent.archived"`

  - `workspace_id: string`

### Beta Webhook Agent Created Event Data

- `beta_webhook_agent_created_event_data: object { id, organization_id, type, workspace_id }`

  - `id: string`

    ID of the agent that triggered the event.

  - `organization_id: string`

  - `type: "agent.created"`

  - `workspace_id: string`

### Beta Webhook Agent Deleted Event Data

- `beta_webhook_agent_deleted_event_data: object { id, organization_id, type, workspace_id }`

  - `id: string`

    ID of the agent that triggered the event.

  - `organization_id: string`

  - `type: "agent.deleted"`

  - `workspace_id: string`

### Beta Webhook Agent Updated Event Data

- `beta_webhook_agent_updated_event_data: object { id, organization_id, type, workspace_id }`

  - `id: string`

    ID of the agent that triggered the event.

  - `organization_id: string`

  - `type: "agent.updated"`

  - `workspace_id: string`

### Beta Webhook Deployment Archived Event Data

- `beta_webhook_deployment_archived_event_data: object { id, organization_id, type, workspace_id }`

  - `id: string`

    ID of the deployment that triggered the event.

  - `organization_id: string`

  - `type: "deployment.archived"`

  - `workspace_id: string`

### Beta Webhook Deployment Created Event Data

- `beta_webhook_deployment_created_event_data: object { id, organization_id, type, workspace_id }`

  - `id: string`

    ID of the deployment that triggered the event.

  - `organization_id: string`

  - `type: "deployment.created"`

  - `workspace_id: string`

### Beta Webhook Deployment Deleted Event Data

- `beta_webhook_deployment_deleted_event_data: object { id, organization_id, type, workspace_id }`

  - `id: string`

    ID of the deployment that triggered the event.

  - `organization_id: string`

  - `type: "deployment.deleted"`

  - `workspace_id: string`

### Beta Webhook Deployment Paused Event Data

- `beta_webhook_deployment_paused_event_data: object { id, organization_id, type, workspace_id }`

  - `id: string`

    ID of the deployment that triggered the event.

  - `organization_id: string`

  - `type: "deployment.paused"`

  - `workspace_id: string`

### Beta Webhook Deployment Run Failed Event Data

- `beta_webhook_deployment_run_failed_event_data: object { id, organization_id, type, workspace_id }`

  - `id: string`

    ID of the deployment run that triggered the event.

  - `organization_id: string`

  - `type: "deployment_run.failed"`

  - `workspace_id: string`

### Beta Webhook Deployment Run Started Event Data

- `beta_webhook_deployment_run_started_event_data: object { id, organization_id, type, workspace_id }`

  - `id: string`

    ID of the deployment run that triggered the event.

  - `organization_id: string`

  - `type: "deployment_run.started"`

  - `workspace_id: string`

### Beta Webhook Deployment Run Succeeded Event Data

- `beta_webhook_deployment_run_succeeded_event_data: object { id, organization_id, type, workspace_id }`

  - `id: string`

    ID of the deployment run that triggered the event.

  - `organization_id: string`

  - `type: "deployment_run.succeeded"`

  - `workspace_id: string`

### Beta Webhook Deployment Unpaused Event Data

- `beta_webhook_deployment_unpaused_event_data: object { id, organization_id, type, workspace_id }`

  - `id: string`

    ID of the deployment that triggered the event.

  - `organization_id: string`

  - `type: "deployment.unpaused"`

  - `workspace_id: string`

### Beta Webhook Deployment Updated Event Data

- `beta_webhook_deployment_updated_event_data: object { id, organization_id, type, workspace_id }`

  - `id: string`

    ID of the deployment that triggered the event.

  - `organization_id: string`

  - `type: "deployment.updated"`

  - `workspace_id: string`

### Beta Webhook Environment Archived Event Data

- `beta_webhook_environment_archived_event_data: object { id, organization_id, type, workspace_id }`

  - `id: string`

    ID of the environment that triggered the event.

  - `organization_id: string`

  - `type: "environment.archived"`

  - `workspace_id: string`

### Beta Webhook Environment Created Event Data

- `beta_webhook_environment_created_event_data: object { id, organization_id, type, workspace_id }`

  - `id: string`

    ID of the environment that triggered the event.

  - `organization_id: string`

  - `type: "environment.created"`

  - `workspace_id: string`

### Beta Webhook Environment Deleted Event Data

- `beta_webhook_environment_deleted_event_data: object { id, organization_id, type, workspace_id }`

  - `id: string`

    ID of the environment that triggered the event.

  - `organization_id: string`

  - `type: "environment.deleted"`

    - `"environment.deleted"`

  - `workspace_id: string`

### Beta Webhook Environment Deleted Event Type

- `beta_webhook_environment_deleted_event_type: "environment.deleted"`

  - `"environment.deleted"`

### Beta Webhook Environment Updated Event Data

- `beta_webhook_environment_updated_event_data: object { id, organization_id, type, workspace_id }`

  - `id: string`

    ID of the environment that triggered the event.

  - `organization_id: string`

  - `type: "environment.updated"`

  - `workspace_id: string`

### Beta Webhook Event

- `beta_webhook_event: object { id, created_at, data, type }`

  - `id: string`

    Unique event identifier for idempotency.

  - `created_at: string`

    RFC 3339 timestamp when the event occurred.

  - `data: BetaWebhookSessionCreatedEventData or BetaWebhookSessionPendingEventData or BetaWebhookSessionRunningEventData or 40 more`

    - `beta_webhook_session_created_event_data: object { id, organization_id, type, workspace_id }`

      - `id: string`

        ID of the session that triggered the event.

      - `organization_id: string`

      - `type: "session.created"`

      - `workspace_id: string`

    - `beta_webhook_session_pending_event_data: object { id, organization_id, type, workspace_id }`

      - `id: string`

        ID of the session that triggered the event.

      - `organization_id: string`

      - `type: "session.pending"`

      - `workspace_id: string`

    - `beta_webhook_session_running_event_data: object { id, organization_id, type, workspace_id }`

      - `id: string`

        ID of the session that triggered the event.

      - `organization_id: string`

      - `type: "session.running"`

      - `workspace_id: string`

    - `beta_webhook_session_idled_event_data: object { id, organization_id, type, workspace_id }`

      - `id: string`

        ID of the session that triggered the event.

      - `organization_id: string`

      - `type: "session.idled"`

      - `workspace_id: string`

    - `beta_webhook_session_requires_action_event_data: object { id, organization_id, type, workspace_id }`

      - `id: string`

        ID of the session that triggered the event.

      - `organization_id: string`

      - `type: "session.requires_action"`

      - `workspace_id: string`

    - `beta_webhook_session_archived_event_data: object { id, organization_id, type, workspace_id }`

      - `id: string`

        ID of the session that triggered the event.

      - `organization_id: string`

      - `type: "session.archived"`

      - `workspace_id: string`

    - `beta_webhook_session_deleted_event_data: object { id, organization_id, type, workspace_id }`

      - `id: string`

        ID of the session that triggered the event.

      - `organization_id: string`

      - `type: "session.deleted"`

      - `workspace_id: string`

    - `beta_webhook_session_status_rescheduled_event_data: object { id, organization_id, type, workspace_id }`

      - `id: string`

        ID of the session that triggered the event.

      - `organization_id: string`

      - `type: "session.status_rescheduled"`

      - `workspace_id: string`

    - `beta_webhook_session_status_run_started_event_data: object { id, organization_id, type, workspace_id }`

      - `id: string`

        ID of the session that triggered the event.

      - `organization_id: string`

      - `type: "session.status_run_started"`

      - `workspace_id: string`

    - `beta_webhook_session_status_idled_event_data: object { id, organization_id, type, workspace_id }`

      - `id: string`

        ID of the session that triggered the event.

      - `organization_id: string`

      - `type: "session.status_idled"`

      - `workspace_id: string`

    - `beta_webhook_session_status_terminated_event_data: object { id, organization_id, type, workspace_id }`

      - `id: string`

        ID of the session that triggered the event.

      - `organization_id: string`

      - `type: "session.status_terminated"`

      - `workspace_id: string`

    - `beta_webhook_session_thread_created_event_data: object { id, organization_id, session_thread_id, 2 more }`

      - `id: string`

        ID of the session that triggered the event.

      - `organization_id: string`

      - `session_thread_id: string`

        ID of the session thread this event refers to.

      - `type: "session.thread_created"`

      - `workspace_id: string`

    - `beta_webhook_session_thread_idled_event_data: object { id, organization_id, session_thread_id, 2 more }`

      - `id: string`

        ID of the session that triggered the event.

      - `organization_id: string`

      - `session_thread_id: string`

        ID of the session thread this event refers to.

      - `type: "session.thread_idled"`

      - `workspace_id: string`

    - `beta_webhook_session_thread_terminated_event_data: object { id, organization_id, session_thread_id, 2 more }`

      - `id: string`

        ID of the session that triggered the event.

      - `organization_id: string`

      - `session_thread_id: string`

        ID of the session thread this event refers to.

      - `type: "session.thread_terminated"`

      - `workspace_id: string`

    - `beta_webhook_session_outcome_evaluation_ended_event_data: object { id, organization_id, type, workspace_id }`

      - `id: string`

        ID of the session that triggered the event.

      - `organization_id: string`

      - `type: "session.outcome_evaluation_ended"`

      - `workspace_id: string`

    - `beta_webhook_vault_created_event_data: object { id, organization_id, type, workspace_id }`

      - `id: string`

        ID of the vault that triggered the event.

      - `organization_id: string`

      - `type: "vault.created"`

      - `workspace_id: string`

    - `beta_webhook_vault_archived_event_data: object { id, organization_id, type, workspace_id }`

      - `id: string`

        ID of the vault that triggered the event.

      - `organization_id: string`

      - `type: "vault.archived"`

      - `workspace_id: string`

    - `beta_webhook_vault_deleted_event_data: object { id, organization_id, type, workspace_id }`

      - `id: string`

        ID of the vault that triggered the event.

      - `organization_id: string`

      - `type: "vault.deleted"`

      - `workspace_id: string`

    - `beta_webhook_vault_credential_created_event_data: object { id, organization_id, type, 2 more }`

      - `id: string`

        ID of the vault credential that triggered the event.

      - `organization_id: string`

      - `type: "vault_credential.created"`

      - `vault_id: string`

        ID of the vault that owns this credential.

      - `workspace_id: string`

    - `beta_webhook_vault_credential_archived_event_data: object { id, organization_id, type, 2 more }`

      - `id: string`

        ID of the vault credential that triggered the event.

      - `organization_id: string`

      - `type: "vault_credential.archived"`

      - `vault_id: string`

        ID of the vault that owns this credential.

      - `workspace_id: string`

    - `beta_webhook_vault_credential_deleted_event_data: object { id, organization_id, type, 2 more }`

      - `id: string`

        ID of the vault credential that triggered the event.

      - `organization_id: string`

      - `type: "vault_credential.deleted"`

      - `vault_id: string`

        ID of the vault that owns this credential.

      - `workspace_id: string`

    - `beta_webhook_vault_credential_refresh_failed_event_data: object { id, organization_id, type, 2 more }`

      - `id: string`

        ID of the vault credential that triggered the event.

      - `organization_id: string`

      - `type: "vault_credential.refresh_failed"`

      - `vault_id: string`

        ID of the vault that owns this credential.

      - `workspace_id: string`

    - `beta_webhook_session_updated_event_data: object { id, organization_id, type, workspace_id }`

      - `id: string`

        ID of the session that triggered the event.

      - `organization_id: string`

      - `type: "session.updated"`

      - `workspace_id: string`

    - `beta_webhook_agent_created_event_data: object { id, organization_id, type, workspace_id }`

      - `id: string`

        ID of the agent that triggered the event.

      - `organization_id: string`

      - `type: "agent.created"`

      - `workspace_id: string`

    - `beta_webhook_agent_archived_event_data: object { id, organization_id, type, workspace_id }`

      - `id: string`

        ID of the agent that triggered the event.

      - `organization_id: string`

      - `type: "agent.archived"`

      - `workspace_id: string`

    - `beta_webhook_agent_deleted_event_data: object { id, organization_id, type, workspace_id }`

      - `id: string`

        ID of the agent that triggered the event.

      - `organization_id: string`

      - `type: "agent.deleted"`

      - `workspace_id: string`

    - `beta_webhook_deployment_paused_event_data: object { id, organization_id, type, workspace_id }`

      - `id: string`

        ID of the deployment that triggered the event.

      - `organization_id: string`

      - `type: "deployment.paused"`

      - `workspace_id: string`

    - `beta_webhook_deployment_run_failed_event_data: object { id, organization_id, type, workspace_id }`

      - `id: string`

        ID of the deployment run that triggered the event.

      - `organization_id: string`

      - `type: "deployment_run.failed"`

      - `workspace_id: string`

    - `beta_webhook_deployment_created_event_data: object { id, organization_id, type, workspace_id }`

      - `id: string`

        ID of the deployment that triggered the event.

      - `organization_id: string`

      - `type: "deployment.created"`

      - `workspace_id: string`

    - `beta_webhook_deployment_updated_event_data: object { id, organization_id, type, workspace_id }`

      - `id: string`

        ID of the deployment that triggered the event.

      - `organization_id: string`

      - `type: "deployment.updated"`

      - `workspace_id: string`

    - `beta_webhook_deployment_unpaused_event_data: object { id, organization_id, type, workspace_id }`

      - `id: string`

        ID of the deployment that triggered the event.

      - `organization_id: string`

      - `type: "deployment.unpaused"`

      - `workspace_id: string`

    - `beta_webhook_agent_updated_event_data: object { id, organization_id, type, workspace_id }`

      - `id: string`

        ID of the agent that triggered the event.

      - `organization_id: string`

      - `type: "agent.updated"`

      - `workspace_id: string`

    - `beta_webhook_deployment_archived_event_data: object { id, organization_id, type, workspace_id }`

      - `id: string`

        ID of the deployment that triggered the event.

      - `organization_id: string`

      - `type: "deployment.archived"`

      - `workspace_id: string`

    - `beta_webhook_deployment_run_started_event_data: object { id, organization_id, type, workspace_id }`

      - `id: string`

        ID of the deployment run that triggered the event.

      - `organization_id: string`

      - `type: "deployment_run.started"`

      - `workspace_id: string`

    - `beta_webhook_deployment_deleted_event_data: object { id, organization_id, type, workspace_id }`

      - `id: string`

        ID of the deployment that triggered the event.

      - `organization_id: string`

      - `type: "deployment.deleted"`

      - `workspace_id: string`

    - `beta_webhook_deployment_run_succeeded_event_data: object { id, organization_id, type, workspace_id }`

      - `id: string`

        ID of the deployment run that triggered the event.

      - `organization_id: string`

      - `type: "deployment_run.succeeded"`

      - `workspace_id: string`

    - `beta_webhook_environment_created_event_data: object { id, organization_id, type, workspace_id }`

      - `id: string`

        ID of the environment that triggered the event.

      - `organization_id: string`

      - `type: "environment.created"`

      - `workspace_id: string`

    - `beta_webhook_environment_updated_event_data: object { id, organization_id, type, workspace_id }`

      - `id: string`

        ID of the environment that triggered the event.

      - `organization_id: string`

      - `type: "environment.updated"`

      - `workspace_id: string`

    - `beta_webhook_environment_archived_event_data: object { id, organization_id, type, workspace_id }`

      - `id: string`

        ID of the environment that triggered the event.

      - `organization_id: string`

      - `type: "environment.archived"`

      - `workspace_id: string`

    - `beta_webhook_environment_deleted_event_data: object { id, organization_id, type, workspace_id }`

      - `id: string`

        ID of the environment that triggered the event.

      - `organization_id: string`

      - `type: "environment.deleted"`

        - `"environment.deleted"`

      - `workspace_id: string`

    - `beta_webhook_memory_store_created_event_data: object { id, organization_id, type, workspace_id }`

      - `id: string`

        ID of the memory store that triggered the event.

      - `organization_id: string`

      - `type: "memory_store.created"`

      - `workspace_id: string`

    - `beta_webhook_memory_store_archived_event_data: object { id, organization_id, type, workspace_id }`

      - `id: string`

        ID of the memory store that triggered the event.

      - `organization_id: string`

      - `type: "memory_store.archived"`

      - `workspace_id: string`

    - `beta_webhook_memory_store_deleted_event_data: object { id, organization_id, type, workspace_id }`

      - `id: string`

        ID of the memory store that triggered the event.

      - `organization_id: string`

      - `type: "memory_store.deleted"`

      - `workspace_id: string`

  - `type: "event"`

    Object type. Always `event` for webhook payloads.

### Beta Webhook Event Data

- `beta_webhook_event_data: BetaWebhookSessionCreatedEventData or BetaWebhookSessionPendingEventData or BetaWebhookSessionRunningEventData or 40 more`

  - `beta_webhook_session_created_event_data: object { id, organization_id, type, workspace_id }`

    - `id: string`

      ID of the session that triggered the event.

    - `organization_id: string`

    - `type: "session.created"`

    - `workspace_id: string`

  - `beta_webhook_session_pending_event_data: object { id, organization_id, type, workspace_id }`

    - `id: string`

      ID of the session that triggered the event.

    - `organization_id: string`

    - `type: "session.pending"`

    - `workspace_id: string`

  - `beta_webhook_session_running_event_data: object { id, organization_id, type, workspace_id }`

    - `id: string`

      ID of the session that triggered the event.

    - `organization_id: string`

    - `type: "session.running"`

    - `workspace_id: string`

  - `beta_webhook_session_idled_event_data: object { id, organization_id, type, workspace_id }`

    - `id: string`

      ID of the session that triggered the event.

    - `organization_id: string`

    - `type: "session.idled"`

    - `workspace_id: string`

  - `beta_webhook_session_requires_action_event_data: object { id, organization_id, type, workspace_id }`

    - `id: string`

      ID of the session that triggered the event.

    - `organization_id: string`

    - `type: "session.requires_action"`

    - `workspace_id: string`

  - `beta_webhook_session_archived_event_data: object { id, organization_id, type, workspace_id }`

    - `id: string`

      ID of the session that triggered the event.

    - `organization_id: string`

    - `type: "session.archived"`

    - `workspace_id: string`

  - `beta_webhook_session_deleted_event_data: object { id, organization_id, type, workspace_id }`

    - `id: string`

      ID of the session that triggered the event.

    - `organization_id: string`

    - `type: "session.deleted"`

    - `workspace_id: string`

  - `beta_webhook_session_status_rescheduled_event_data: object { id, organization_id, type, workspace_id }`

    - `id: string`

      ID of the session that triggered the event.

    - `organization_id: string`

    - `type: "session.status_rescheduled"`

    - `workspace_id: string`

  - `beta_webhook_session_status_run_started_event_data: object { id, organization_id, type, workspace_id }`

    - `id: string`

      ID of the session that triggered the event.

    - `organization_id: string`

    - `type: "session.status_run_started"`

    - `workspace_id: string`

  - `beta_webhook_session_status_idled_event_data: object { id, organization_id, type, workspace_id }`

    - `id: string`

      ID of the session that triggered the event.

    - `organization_id: string`

    - `type: "session.status_idled"`

    - `workspace_id: string`

  - `beta_webhook_session_status_terminated_event_data: object { id, organization_id, type, workspace_id }`

    - `id: string`

      ID of the session that triggered the event.

    - `organization_id: string`

    - `type: "session.status_terminated"`

    - `workspace_id: string`

  - `beta_webhook_session_thread_created_event_data: object { id, organization_id, session_thread_id, 2 more }`

    - `id: string`

      ID of the session that triggered the event.

    - `organization_id: string`

    - `session_thread_id: string`

      ID of the session thread this event refers to.

    - `type: "session.thread_created"`

    - `workspace_id: string`

  - `beta_webhook_session_thread_idled_event_data: object { id, organization_id, session_thread_id, 2 more }`

    - `id: string`

      ID of the session that triggered the event.

    - `organization_id: string`

    - `session_thread_id: string`

      ID of the session thread this event refers to.

    - `type: "session.thread_idled"`

    - `workspace_id: string`

  - `beta_webhook_session_thread_terminated_event_data: object { id, organization_id, session_thread_id, 2 more }`

    - `id: string`

      ID of the session that triggered the event.

    - `organization_id: string`

    - `session_thread_id: string`

      ID of the session thread this event refers to.

    - `type: "session.thread_terminated"`

    - `workspace_id: string`

  - `beta_webhook_session_outcome_evaluation_ended_event_data: object { id, organization_id, type, workspace_id }`

    - `id: string`

      ID of the session that triggered the event.

    - `organization_id: string`

    - `type: "session.outcome_evaluation_ended"`

    - `workspace_id: string`

  - `beta_webhook_vault_created_event_data: object { id, organization_id, type, workspace_id }`

    - `id: string`

      ID of the vault that triggered the event.

    - `organization_id: string`

    - `type: "vault.created"`

    - `workspace_id: string`

  - `beta_webhook_vault_archived_event_data: object { id, organization_id, type, workspace_id }`

    - `id: string`

      ID of the vault that triggered the event.

    - `organization_id: string`

    - `type: "vault.archived"`

    - `workspace_id: string`

  - `beta_webhook_vault_deleted_event_data: object { id, organization_id, type, workspace_id }`

    - `id: string`

      ID of the vault that triggered the event.

    - `organization_id: string`

    - `type: "vault.deleted"`

    - `workspace_id: string`

  - `beta_webhook_vault_credential_created_event_data: object { id, organization_id, type, 2 more }`

    - `id: string`

      ID of the vault credential that triggered the event.

    - `organization_id: string`

    - `type: "vault_credential.created"`

    - `vault_id: string`

      ID of the vault that owns this credential.

    - `workspace_id: string`

  - `beta_webhook_vault_credential_archived_event_data: object { id, organization_id, type, 2 more }`

    - `id: string`

      ID of the vault credential that triggered the event.

    - `organization_id: string`

    - `type: "vault_credential.archived"`

    - `vault_id: string`

      ID of the vault that owns this credential.

    - `workspace_id: string`

  - `beta_webhook_vault_credential_deleted_event_data: object { id, organization_id, type, 2 more }`

    - `id: string`

      ID of the vault credential that triggered the event.

    - `organization_id: string`

    - `type: "vault_credential.deleted"`

    - `vault_id: string`

      ID of the vault that owns this credential.

    - `workspace_id: string`

  - `beta_webhook_vault_credential_refresh_failed_event_data: object { id, organization_id, type, 2 more }`

    - `id: string`

      ID of the vault credential that triggered the event.

    - `organization_id: string`

    - `type: "vault_credential.refresh_failed"`

    - `vault_id: string`

      ID of the vault that owns this credential.

    - `workspace_id: string`

  - `beta_webhook_session_updated_event_data: object { id, organization_id, type, workspace_id }`

    - `id: string`

      ID of the session that triggered the event.

    - `organization_id: string`

    - `type: "session.updated"`

    - `workspace_id: string`

  - `beta_webhook_agent_created_event_data: object { id, organization_id, type, workspace_id }`

    - `id: string`

      ID of the agent that triggered the event.

    - `organization_id: string`

    - `type: "agent.created"`

    - `workspace_id: string`

  - `beta_webhook_agent_archived_event_data: object { id, organization_id, type, workspace_id }`

    - `id: string`

      ID of the agent that triggered the event.

    - `organization_id: string`

    - `type: "agent.archived"`

    - `workspace_id: string`

  - `beta_webhook_agent_deleted_event_data: object { id, organization_id, type, workspace_id }`

    - `id: string`

      ID of the agent that triggered the event.

    - `organization_id: string`

    - `type: "agent.deleted"`

    - `workspace_id: string`

  - `beta_webhook_deployment_paused_event_data: object { id, organization_id, type, workspace_id }`

    - `id: string`

      ID of the deployment that triggered the event.

    - `organization_id: string`

    - `type: "deployment.paused"`

    - `workspace_id: string`

  - `beta_webhook_deployment_run_failed_event_data: object { id, organization_id, type, workspace_id }`

    - `id: string`

      ID of the deployment run that triggered the event.

    - `organization_id: string`

    - `type: "deployment_run.failed"`

    - `workspace_id: string`

  - `beta_webhook_deployment_created_event_data: object { id, organization_id, type, workspace_id }`

    - `id: string`

      ID of the deployment that triggered the event.

    - `organization_id: string`

    - `type: "deployment.created"`

    - `workspace_id: string`

  - `beta_webhook_deployment_updated_event_data: object { id, organization_id, type, workspace_id }`

    - `id: string`

      ID of the deployment that triggered the event.

    - `organization_id: string`

    - `type: "deployment.updated"`

    - `workspace_id: string`

  - `beta_webhook_deployment_unpaused_event_data: object { id, organization_id, type, workspace_id }`

    - `id: string`

      ID of the deployment that triggered the event.

    - `organization_id: string`

    - `type: "deployment.unpaused"`

    - `workspace_id: string`

  - `beta_webhook_agent_updated_event_data: object { id, organization_id, type, workspace_id }`

    - `id: string`

      ID of the agent that triggered the event.

    - `organization_id: string`

    - `type: "agent.updated"`

    - `workspace_id: string`

  - `beta_webhook_deployment_archived_event_data: object { id, organization_id, type, workspace_id }`

    - `id: string`

      ID of the deployment that triggered the event.

    - `organization_id: string`

    - `type: "deployment.archived"`

    - `workspace_id: string`

  - `beta_webhook_deployment_run_started_event_data: object { id, organization_id, type, workspace_id }`

    - `id: string`

      ID of the deployment run that triggered the event.

    - `organization_id: string`

    - `type: "deployment_run.started"`

    - `workspace_id: string`

  - `beta_webhook_deployment_deleted_event_data: object { id, organization_id, type, workspace_id }`

    - `id: string`

      ID of the deployment that triggered the event.

    - `organization_id: string`

    - `type: "deployment.deleted"`

    - `workspace_id: string`

  - `beta_webhook_deployment_run_succeeded_event_data: object { id, organization_id, type, workspace_id }`

    - `id: string`

      ID of the deployment run that triggered the event.

    - `organization_id: string`

    - `type: "deployment_run.succeeded"`

    - `workspace_id: string`

  - `beta_webhook_environment_created_event_data: object { id, organization_id, type, workspace_id }`

    - `id: string`

      ID of the environment that triggered the event.

    - `organization_id: string`

    - `type: "environment.created"`

    - `workspace_id: string`

  - `beta_webhook_environment_updated_event_data: object { id, organization_id, type, workspace_id }`

    - `id: string`

      ID of the environment that triggered the event.

    - `organization_id: string`

    - `type: "environment.updated"`

    - `workspace_id: string`

  - `beta_webhook_environment_archived_event_data: object { id, organization_id, type, workspace_id }`

    - `id: string`

      ID of the environment that triggered the event.

    - `organization_id: string`

    - `type: "environment.archived"`

    - `workspace_id: string`

  - `beta_webhook_environment_deleted_event_data: object { id, organization_id, type, workspace_id }`

    - `id: string`

      ID of the environment that triggered the event.

    - `organization_id: string`

    - `type: "environment.deleted"`

      - `"environment.deleted"`

    - `workspace_id: string`

  - `beta_webhook_memory_store_created_event_data: object { id, organization_id, type, workspace_id }`

    - `id: string`

      ID of the memory store that triggered the event.

    - `organization_id: string`

    - `type: "memory_store.created"`

    - `workspace_id: string`

  - `beta_webhook_memory_store_archived_event_data: object { id, organization_id, type, workspace_id }`

    - `id: string`

      ID of the memory store that triggered the event.

    - `organization_id: string`

    - `type: "memory_store.archived"`

    - `workspace_id: string`

  - `beta_webhook_memory_store_deleted_event_data: object { id, organization_id, type, workspace_id }`

    - `id: string`

      ID of the memory store that triggered the event.

    - `organization_id: string`

    - `type: "memory_store.deleted"`

    - `workspace_id: string`

### Beta Webhook Memory Store Archived Event Data

- `beta_webhook_memory_store_archived_event_data: object { id, organization_id, type, workspace_id }`

  - `id: string`

    ID of the memory store that triggered the event.

  - `organization_id: string`

  - `type: "memory_store.archived"`

  - `workspace_id: string`

### Beta Webhook Memory Store Created Event Data

- `beta_webhook_memory_store_created_event_data: object { id, organization_id, type, workspace_id }`

  - `id: string`

    ID of the memory store that triggered the event.

  - `organization_id: string`

  - `type: "memory_store.created"`

  - `workspace_id: string`

### Beta Webhook Memory Store Deleted Event Data

- `beta_webhook_memory_store_deleted_event_data: object { id, organization_id, type, workspace_id }`

  - `id: string`

    ID of the memory store that triggered the event.

  - `organization_id: string`

  - `type: "memory_store.deleted"`

  - `workspace_id: string`

### Beta Webhook Session Archived Event Data

- `beta_webhook_session_archived_event_data: object { id, organization_id, type, workspace_id }`

  - `id: string`

    ID of the session that triggered the event.

  - `organization_id: string`

  - `type: "session.archived"`

  - `workspace_id: string`

### Beta Webhook Session Created Event Data

- `beta_webhook_session_created_event_data: object { id, organization_id, type, workspace_id }`

  - `id: string`

    ID of the session that triggered the event.

  - `organization_id: string`

  - `type: "session.created"`

  - `workspace_id: string`

### Beta Webhook Session Deleted Event Data

- `beta_webhook_session_deleted_event_data: object { id, organization_id, type, workspace_id }`

  - `id: string`

    ID of the session that triggered the event.

  - `organization_id: string`

  - `type: "session.deleted"`

  - `workspace_id: string`

### Beta Webhook Session Idled Event Data

- `beta_webhook_session_idled_event_data: object { id, organization_id, type, workspace_id }`

  - `id: string`

    ID of the session that triggered the event.

  - `organization_id: string`

  - `type: "session.idled"`

  - `workspace_id: string`

### Beta Webhook Session Outcome Evaluation Ended Event Data

- `beta_webhook_session_outcome_evaluation_ended_event_data: object { id, organization_id, type, workspace_id }`

  - `id: string`

    ID of the session that triggered the event.

  - `organization_id: string`

  - `type: "session.outcome_evaluation_ended"`

  - `workspace_id: string`

### Beta Webhook Session Pending Event Data

- `beta_webhook_session_pending_event_data: object { id, organization_id, type, workspace_id }`

  - `id: string`

    ID of the session that triggered the event.

  - `organization_id: string`

  - `type: "session.pending"`

  - `workspace_id: string`

### Beta Webhook Session Requires Action Event Data

- `beta_webhook_session_requires_action_event_data: object { id, organization_id, type, workspace_id }`

  - `id: string`

    ID of the session that triggered the event.

  - `organization_id: string`

  - `type: "session.requires_action"`

  - `workspace_id: string`

### Beta Webhook Session Running Event Data

- `beta_webhook_session_running_event_data: object { id, organization_id, type, workspace_id }`

  - `id: string`

    ID of the session that triggered the event.

  - `organization_id: string`

  - `type: "session.running"`

  - `workspace_id: string`

### Beta Webhook Session Status Idled Event Data

- `beta_webhook_session_status_idled_event_data: object { id, organization_id, type, workspace_id }`

  - `id: string`

    ID of the session that triggered the event.

  - `organization_id: string`

  - `type: "session.status_idled"`

  - `workspace_id: string`

### Beta Webhook Session Status Rescheduled Event Data

- `beta_webhook_session_status_rescheduled_event_data: object { id, organization_id, type, workspace_id }`

  - `id: string`

    ID of the session that triggered the event.

  - `organization_id: string`

  - `type: "session.status_rescheduled"`

  - `workspace_id: string`

### Beta Webhook Session Status Run Started Event Data

- `beta_webhook_session_status_run_started_event_data: object { id, organization_id, type, workspace_id }`

  - `id: string`

    ID of the session that triggered the event.

  - `organization_id: string`

  - `type: "session.status_run_started"`

  - `workspace_id: string`

### Beta Webhook Session Status Terminated Event Data

- `beta_webhook_session_status_terminated_event_data: object { id, organization_id, type, workspace_id }`

  - `id: string`

    ID of the session that triggered the event.

  - `organization_id: string`

  - `type: "session.status_terminated"`

  - `workspace_id: string`

### Beta Webhook Session Thread Created Event Data

- `beta_webhook_session_thread_created_event_data: object { id, organization_id, session_thread_id, 2 more }`

  - `id: string`

    ID of the session that triggered the event.

  - `organization_id: string`

  - `session_thread_id: string`

    ID of the session thread this event refers to.

  - `type: "session.thread_created"`

  - `workspace_id: string`

### Beta Webhook Session Thread Idled Event Data

- `beta_webhook_session_thread_idled_event_data: object { id, organization_id, session_thread_id, 2 more }`

  - `id: string`

    ID of the session that triggered the event.

  - `organization_id: string`

  - `session_thread_id: string`

    ID of the session thread this event refers to.

  - `type: "session.thread_idled"`

  - `workspace_id: string`

### Beta Webhook Session Thread Terminated Event Data

- `beta_webhook_session_thread_terminated_event_data: object { id, organization_id, session_thread_id, 2 more }`

  - `id: string`

    ID of the session that triggered the event.

  - `organization_id: string`

  - `session_thread_id: string`

    ID of the session thread this event refers to.

  - `type: "session.thread_terminated"`

  - `workspace_id: string`

### Beta Webhook Session Updated Event Data

- `beta_webhook_session_updated_event_data: object { id, organization_id, type, workspace_id }`

  - `id: string`

    ID of the session that triggered the event.

  - `organization_id: string`

  - `type: "session.updated"`

  - `workspace_id: string`

### Beta Webhook Vault Archived Event Data

- `beta_webhook_vault_archived_event_data: object { id, organization_id, type, workspace_id }`

  - `id: string`

    ID of the vault that triggered the event.

  - `organization_id: string`

  - `type: "vault.archived"`

  - `workspace_id: string`

### Beta Webhook Vault Created Event Data

- `beta_webhook_vault_created_event_data: object { id, organization_id, type, workspace_id }`

  - `id: string`

    ID of the vault that triggered the event.

  - `organization_id: string`

  - `type: "vault.created"`

  - `workspace_id: string`

### Beta Webhook Vault Credential Archived Event Data

- `beta_webhook_vault_credential_archived_event_data: object { id, organization_id, type, 2 more }`

  - `id: string`

    ID of the vault credential that triggered the event.

  - `organization_id: string`

  - `type: "vault_credential.archived"`

  - `vault_id: string`

    ID of the vault that owns this credential.

  - `workspace_id: string`

### Beta Webhook Vault Credential Created Event Data

- `beta_webhook_vault_credential_created_event_data: object { id, organization_id, type, 2 more }`

  - `id: string`

    ID of the vault credential that triggered the event.

  - `organization_id: string`

  - `type: "vault_credential.created"`

  - `vault_id: string`

    ID of the vault that owns this credential.

  - `workspace_id: string`

### Beta Webhook Vault Credential Deleted Event Data

- `beta_webhook_vault_credential_deleted_event_data: object { id, organization_id, type, 2 more }`

  - `id: string`

    ID of the vault credential that triggered the event.

  - `organization_id: string`

  - `type: "vault_credential.deleted"`

  - `vault_id: string`

    ID of the vault that owns this credential.

  - `workspace_id: string`

### Beta Webhook Vault Credential Refresh Failed Event Data

- `beta_webhook_vault_credential_refresh_failed_event_data: object { id, organization_id, type, 2 more }`

  - `id: string`

    ID of the vault credential that triggered the event.

  - `organization_id: string`

  - `type: "vault_credential.refresh_failed"`

  - `vault_id: string`

    ID of the vault that owns this credential.

  - `workspace_id: string`

### Beta Webhook Vault Deleted Event Data

- `beta_webhook_vault_deleted_event_data: object { id, organization_id, type, workspace_id }`

  - `id: string`

    ID of the vault that triggered the event.

  - `organization_id: string`

  - `type: "vault.deleted"`

  - `workspace_id: string`

### Unwrap Webhook Event

- `unwrap_webhook_event: object { id, created_at, data, type }`

  - `id: string`

    Unique event identifier for idempotency.

  - `created_at: string`

    RFC 3339 timestamp when the event occurred.

  - `data: BetaWebhookSessionCreatedEventData or BetaWebhookSessionPendingEventData or BetaWebhookSessionRunningEventData or 40 more`

    - `beta_webhook_session_created_event_data: object { id, organization_id, type, workspace_id }`

      - `id: string`

        ID of the session that triggered the event.

      - `organization_id: string`

      - `type: "session.created"`

      - `workspace_id: string`

    - `beta_webhook_session_pending_event_data: object { id, organization_id, type, workspace_id }`

      - `id: string`

        ID of the session that triggered the event.

      - `organization_id: string`

      - `type: "session.pending"`

      - `workspace_id: string`

    - `beta_webhook_session_running_event_data: object { id, organization_id, type, workspace_id }`

      - `id: string`

        ID of the session that triggered the event.

      - `organization_id: string`

      - `type: "session.running"`

      - `workspace_id: string`

    - `beta_webhook_session_idled_event_data: object { id, organization_id, type, workspace_id }`

      - `id: string`

        ID of the session that triggered the event.

      - `organization_id: string`

      - `type: "session.idled"`

      - `workspace_id: string`

    - `beta_webhook_session_requires_action_event_data: object { id, organization_id, type, workspace_id }`

      - `id: string`

        ID of the session that triggered the event.

      - `organization_id: string`

      - `type: "session.requires_action"`

      - `workspace_id: string`

    - `beta_webhook_session_archived_event_data: object { id, organization_id, type, workspace_id }`

      - `id: string`

        ID of the session that triggered the event.

      - `organization_id: string`

      - `type: "session.archived"`

      - `workspace_id: string`

    - `beta_webhook_session_deleted_event_data: object { id, organization_id, type, workspace_id }`

      - `id: string`

        ID of the session that triggered the event.

      - `organization_id: string`

      - `type: "session.deleted"`

      - `workspace_id: string`

    - `beta_webhook_session_status_rescheduled_event_data: object { id, organization_id, type, workspace_id }`

      - `id: string`

        ID of the session that triggered the event.

      - `organization_id: string`

      - `type: "session.status_rescheduled"`

      - `workspace_id: string`

    - `beta_webhook_session_status_run_started_event_data: object { id, organization_id, type, workspace_id }`

      - `id: string`

        ID of the session that triggered the event.

      - `organization_id: string`

      - `type: "session.status_run_started"`

      - `workspace_id: string`

    - `beta_webhook_session_status_idled_event_data: object { id, organization_id, type, workspace_id }`

      - `id: string`

        ID of the session that triggered the event.

      - `organization_id: string`

      - `type: "session.status_idled"`

      - `workspace_id: string`

    - `beta_webhook_session_status_terminated_event_data: object { id, organization_id, type, workspace_id }`

      - `id: string`

        ID of the session that triggered the event.

      - `organization_id: string`

      - `type: "session.status_terminated"`

      - `workspace_id: string`

    - `beta_webhook_session_thread_created_event_data: object { id, organization_id, session_thread_id, 2 more }`

      - `id: string`

        ID of the session that triggered the event.

      - `organization_id: string`

      - `session_thread_id: string`

        ID of the session thread this event refers to.

      - `type: "session.thread_created"`

      - `workspace_id: string`

    - `beta_webhook_session_thread_idled_event_data: object { id, organization_id, session_thread_id, 2 more }`

      - `id: string`

        ID of the session that triggered the event.

      - `organization_id: string`

      - `session_thread_id: string`

        ID of the session thread this event refers to.

      - `type: "session.thread_idled"`

      - `workspace_id: string`

    - `beta_webhook_session_thread_terminated_event_data: object { id, organization_id, session_thread_id, 2 more }`

      - `id: string`

        ID of the session that triggered the event.

      - `organization_id: string`

      - `session_thread_id: string`

        ID of the session thread this event refers to.

      - `type: "session.thread_terminated"`

      - `workspace_id: string`

    - `beta_webhook_session_outcome_evaluation_ended_event_data: object { id, organization_id, type, workspace_id }`

      - `id: string`

        ID of the session that triggered the event.

      - `organization_id: string`

      - `type: "session.outcome_evaluation_ended"`

      - `workspace_id: string`

    - `beta_webhook_vault_created_event_data: object { id, organization_id, type, workspace_id }`

      - `id: string`

        ID of the vault that triggered the event.

      - `organization_id: string`

      - `type: "vault.created"`

      - `workspace_id: string`

    - `beta_webhook_vault_archived_event_data: object { id, organization_id, type, workspace_id }`

      - `id: string`

        ID of the vault that triggered the event.

      - `organization_id: string`

      - `type: "vault.archived"`

      - `workspace_id: string`

    - `beta_webhook_vault_deleted_event_data: object { id, organization_id, type, workspace_id }`

      - `id: string`

        ID of the vault that triggered the event.

      - `organization_id: string`

      - `type: "vault.deleted"`

      - `workspace_id: string`

    - `beta_webhook_vault_credential_created_event_data: object { id, organization_id, type, 2 more }`

      - `id: string`

        ID of the vault credential that triggered the event.

      - `organization_id: string`

      - `type: "vault_credential.created"`

      - `vault_id: string`

        ID of the vault that owns this credential.

      - `workspace_id: string`

    - `beta_webhook_vault_credential_archived_event_data: object { id, organization_id, type, 2 more }`

      - `id: string`

        ID of the vault credential that triggered the event.

      - `organization_id: string`

      - `type: "vault_credential.archived"`

      - `vault_id: string`

        ID of the vault that owns this credential.

      - `workspace_id: string`

    - `beta_webhook_vault_credential_deleted_event_data: object { id, organization_id, type, 2 more }`

      - `id: string`

        ID of the vault credential that triggered the event.

      - `organization_id: string`

      - `type: "vault_credential.deleted"`

      - `vault_id: string`

        ID of the vault that owns this credential.

      - `workspace_id: string`

    - `beta_webhook_vault_credential_refresh_failed_event_data: object { id, organization_id, type, 2 more }`

      - `id: string`

        ID of the vault credential that triggered the event.

      - `organization_id: string`

      - `type: "vault_credential.refresh_failed"`

      - `vault_id: string`

        ID of the vault that owns this credential.

      - `workspace_id: string`

    - `beta_webhook_session_updated_event_data: object { id, organization_id, type, workspace_id }`

      - `id: string`

        ID of the session that triggered the event.

      - `organization_id: string`

      - `type: "session.updated"`

      - `workspace_id: string`

    - `beta_webhook_agent_created_event_data: object { id, organization_id, type, workspace_id }`

      - `id: string`

        ID of the agent that triggered the event.

      - `organization_id: string`

      - `type: "agent.created"`

      - `workspace_id: string`

    - `beta_webhook_agent_archived_event_data: object { id, organization_id, type, workspace_id }`

      - `id: string`

        ID of the agent that triggered the event.

      - `organization_id: string`

      - `type: "agent.archived"`

      - `workspace_id: string`

    - `beta_webhook_agent_deleted_event_data: object { id, organization_id, type, workspace_id }`

      - `id: string`

        ID of the agent that triggered the event.

      - `organization_id: string`

      - `type: "agent.deleted"`

      - `workspace_id: string`

    - `beta_webhook_deployment_paused_event_data: object { id, organization_id, type, workspace_id }`

      - `id: string`

        ID of the deployment that triggered the event.

      - `organization_id: string`

      - `type: "deployment.paused"`

      - `workspace_id: string`

    - `beta_webhook_deployment_run_failed_event_data: object { id, organization_id, type, workspace_id }`

      - `id: string`

        ID of the deployment run that triggered the event.

      - `organization_id: string`

      - `type: "deployment_run.failed"`

      - `workspace_id: string`

    - `beta_webhook_deployment_created_event_data: object { id, organization_id, type, workspace_id }`

      - `id: string`

        ID of the deployment that triggered the event.

      - `organization_id: string`

      - `type: "deployment.created"`

      - `workspace_id: string`

    - `beta_webhook_deployment_updated_event_data: object { id, organization_id, type, workspace_id }`

      - `id: string`

        ID of the deployment that triggered the event.

      - `organization_id: string`

      - `type: "deployment.updated"`

      - `workspace_id: string`

    - `beta_webhook_deployment_unpaused_event_data: object { id, organization_id, type, workspace_id }`

      - `id: string`

        ID of the deployment that triggered the event.

      - `organization_id: string`

      - `type: "deployment.unpaused"`

      - `workspace_id: string`

    - `beta_webhook_agent_updated_event_data: object { id, organization_id, type, workspace_id }`

      - `id: string`

        ID of the agent that triggered the event.

      - `organization_id: string`

      - `type: "agent.updated"`

      - `workspace_id: string`

    - `beta_webhook_deployment_archived_event_data: object { id, organization_id, type, workspace_id }`

      - `id: string`

        ID of the deployment that triggered the event.

      - `organization_id: string`

      - `type: "deployment.archived"`

      - `workspace_id: string`

    - `beta_webhook_deployment_run_started_event_data: object { id, organization_id, type, workspace_id }`

      - `id: string`

        ID of the deployment run that triggered the event.

      - `organization_id: string`

      - `type: "deployment_run.started"`

      - `workspace_id: string`

    - `beta_webhook_deployment_deleted_event_data: object { id, organization_id, type, workspace_id }`

      - `id: string`

        ID of the deployment that triggered the event.

      - `organization_id: string`

      - `type: "deployment.deleted"`

      - `workspace_id: string`

    - `beta_webhook_deployment_run_succeeded_event_data: object { id, organization_id, type, workspace_id }`

      - `id: string`

        ID of the deployment run that triggered the event.

      - `organization_id: string`

      - `type: "deployment_run.succeeded"`

      - `workspace_id: string`

    - `beta_webhook_environment_created_event_data: object { id, organization_id, type, workspace_id }`

      - `id: string`

        ID of the environment that triggered the event.

      - `organization_id: string`

      - `type: "environment.created"`

      - `workspace_id: string`

    - `beta_webhook_environment_updated_event_data: object { id, organization_id, type, workspace_id }`

      - `id: string`

        ID of the environment that triggered the event.

      - `organization_id: string`

      - `type: "environment.updated"`

      - `workspace_id: string`

    - `beta_webhook_environment_archived_event_data: object { id, organization_id, type, workspace_id }`

      - `id: string`

        ID of the environment that triggered the event.

      - `organization_id: string`

      - `type: "environment.archived"`

      - `workspace_id: string`

    - `beta_webhook_environment_deleted_event_data: object { id, organization_id, type, workspace_id }`

      - `id: string`

        ID of the environment that triggered the event.

      - `organization_id: string`

      - `type: "environment.deleted"`

        - `"environment.deleted"`

      - `workspace_id: string`

    - `beta_webhook_memory_store_created_event_data: object { id, organization_id, type, workspace_id }`

      - `id: string`

        ID of the memory store that triggered the event.

      - `organization_id: string`

      - `type: "memory_store.created"`

      - `workspace_id: string`

    - `beta_webhook_memory_store_archived_event_data: object { id, organization_id, type, workspace_id }`

      - `id: string`

        ID of the memory store that triggered the event.

      - `organization_id: string`

      - `type: "memory_store.archived"`

      - `workspace_id: string`

    - `beta_webhook_memory_store_deleted_event_data: object { id, organization_id, type, workspace_id }`

      - `id: string`

        ID of the memory store that triggered the event.

      - `organization_id: string`

      - `type: "memory_store.deleted"`

      - `workspace_id: string`

  - `type: "event"`

    Object type. Always `event` for webhook payloads.
