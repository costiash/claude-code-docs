# Webhooks

## Domain Types

### Beta Webhook Agent Archived Event Data

- `BetaWebhookAgentArchivedEventData object { id, organization_id, type, workspace_id }`

  - `id: string`

    ID of the agent that triggered the event.

  - `organization_id: string`

  - `type: "agent.archived"`

    - `"agent.archived"`

  - `workspace_id: string`

### Beta Webhook Agent Created Event Data

- `BetaWebhookAgentCreatedEventData object { id, organization_id, type, workspace_id }`

  - `id: string`

    ID of the agent that triggered the event.

  - `organization_id: string`

  - `type: "agent.created"`

    - `"agent.created"`

  - `workspace_id: string`

### Beta Webhook Agent Deleted Event Data

- `BetaWebhookAgentDeletedEventData object { id, organization_id, type, workspace_id }`

  - `id: string`

    ID of the agent that triggered the event.

  - `organization_id: string`

  - `type: "agent.deleted"`

    - `"agent.deleted"`

  - `workspace_id: string`

### Beta Webhook Agent Updated Event Data

- `BetaWebhookAgentUpdatedEventData object { id, organization_id, type, workspace_id }`

  - `id: string`

    ID of the agent that triggered the event.

  - `organization_id: string`

  - `type: "agent.updated"`

    - `"agent.updated"`

  - `workspace_id: string`

### Beta Webhook Deployment Archived Event Data

- `BetaWebhookDeploymentArchivedEventData object { id, organization_id, type, workspace_id }`

  - `id: string`

    ID of the deployment that triggered the event.

  - `organization_id: string`

  - `type: "deployment.archived"`

    - `"deployment.archived"`

  - `workspace_id: string`

### Beta Webhook Deployment Created Event Data

- `BetaWebhookDeploymentCreatedEventData object { id, organization_id, type, workspace_id }`

  - `id: string`

    ID of the deployment that triggered the event.

  - `organization_id: string`

  - `type: "deployment.created"`

    - `"deployment.created"`

  - `workspace_id: string`

### Beta Webhook Deployment Deleted Event Data

- `BetaWebhookDeploymentDeletedEventData object { id, organization_id, type, workspace_id }`

  - `id: string`

    ID of the deployment that triggered the event.

  - `organization_id: string`

  - `type: "deployment.deleted"`

    - `"deployment.deleted"`

  - `workspace_id: string`

### Beta Webhook Deployment Paused Event Data

- `BetaWebhookDeploymentPausedEventData object { id, organization_id, type, workspace_id }`

  - `id: string`

    ID of the deployment that triggered the event.

  - `organization_id: string`

  - `type: "deployment.paused"`

    - `"deployment.paused"`

  - `workspace_id: string`

### Beta Webhook Deployment Run Failed Event Data

- `BetaWebhookDeploymentRunFailedEventData object { id, organization_id, type, workspace_id }`

  - `id: string`

    ID of the deployment run that triggered the event.

  - `organization_id: string`

  - `type: "deployment_run.failed"`

    - `"deployment_run.failed"`

  - `workspace_id: string`

### Beta Webhook Deployment Run Started Event Data

- `BetaWebhookDeploymentRunStartedEventData object { id, organization_id, type, workspace_id }`

  - `id: string`

    ID of the deployment run that triggered the event.

  - `organization_id: string`

  - `type: "deployment_run.started"`

    - `"deployment_run.started"`

  - `workspace_id: string`

### Beta Webhook Deployment Run Succeeded Event Data

- `BetaWebhookDeploymentRunSucceededEventData object { id, organization_id, type, workspace_id }`

  - `id: string`

    ID of the deployment run that triggered the event.

  - `organization_id: string`

  - `type: "deployment_run.succeeded"`

    - `"deployment_run.succeeded"`

  - `workspace_id: string`

### Beta Webhook Deployment Unpaused Event Data

- `BetaWebhookDeploymentUnpausedEventData object { id, organization_id, type, workspace_id }`

  - `id: string`

    ID of the deployment that triggered the event.

  - `organization_id: string`

  - `type: "deployment.unpaused"`

    - `"deployment.unpaused"`

  - `workspace_id: string`

### Beta Webhook Deployment Updated Event Data

- `BetaWebhookDeploymentUpdatedEventData object { id, organization_id, type, workspace_id }`

  - `id: string`

    ID of the deployment that triggered the event.

  - `organization_id: string`

  - `type: "deployment.updated"`

    - `"deployment.updated"`

  - `workspace_id: string`

### Beta Webhook Environment Archived Event Data

- `BetaWebhookEnvironmentArchivedEventData object { id, organization_id, type, workspace_id }`

  - `id: string`

    ID of the environment that triggered the event.

  - `organization_id: string`

  - `type: "environment.archived"`

    - `"environment.archived"`

  - `workspace_id: string`

### Beta Webhook Environment Created Event Data

- `BetaWebhookEnvironmentCreatedEventData object { id, organization_id, type, workspace_id }`

  - `id: string`

    ID of the environment that triggered the event.

  - `organization_id: string`

  - `type: "environment.created"`

    - `"environment.created"`

  - `workspace_id: string`

### Beta Webhook Environment Deleted Event Data

- `BetaWebhookEnvironmentDeletedEventData object { id, organization_id, type, workspace_id }`

  - `id: string`

    ID of the environment that triggered the event.

  - `organization_id: string`

  - `type: "environment.deleted"`

    - `"environment.deleted"`

  - `workspace_id: string`

### Beta Webhook Environment Updated Event Data

- `BetaWebhookEnvironmentUpdatedEventData object { id, organization_id, type, workspace_id }`

  - `id: string`

    ID of the environment that triggered the event.

  - `organization_id: string`

  - `type: "environment.updated"`

    - `"environment.updated"`

  - `workspace_id: string`

### Beta Webhook Event

- `BetaWebhookEvent object { id, created_at, data, type }`

  - `id: string`

    Unique event identifier for idempotency.

  - `created_at: string`

    RFC 3339 timestamp when the event occurred.

  - `data: BetaWebhookEventData`

    - `BetaWebhookSessionCreatedEventData object { id, organization_id, type, workspace_id }`

      - `id: string`

        ID of the session that triggered the event.

      - `organization_id: string`

      - `type: "session.created"`

        - `"session.created"`

      - `workspace_id: string`

    - `BetaWebhookSessionPendingEventData object { id, organization_id, type, workspace_id }`

      - `id: string`

        ID of the session that triggered the event.

      - `organization_id: string`

      - `type: "session.pending"`

        - `"session.pending"`

      - `workspace_id: string`

    - `BetaWebhookSessionRunningEventData object { id, organization_id, type, workspace_id }`

      - `id: string`

        ID of the session that triggered the event.

      - `organization_id: string`

      - `type: "session.running"`

        - `"session.running"`

      - `workspace_id: string`

    - `BetaWebhookSessionIdledEventData object { id, organization_id, type, workspace_id }`

      - `id: string`

        ID of the session that triggered the event.

      - `organization_id: string`

      - `type: "session.idled"`

        - `"session.idled"`

      - `workspace_id: string`

    - `BetaWebhookSessionRequiresActionEventData object { id, organization_id, type, workspace_id }`

      - `id: string`

        ID of the session that triggered the event.

      - `organization_id: string`

      - `type: "session.requires_action"`

        - `"session.requires_action"`

      - `workspace_id: string`

    - `BetaWebhookSessionArchivedEventData object { id, organization_id, type, workspace_id }`

      - `id: string`

        ID of the session that triggered the event.

      - `organization_id: string`

      - `type: "session.archived"`

        - `"session.archived"`

      - `workspace_id: string`

    - `BetaWebhookSessionDeletedEventData object { id, organization_id, type, workspace_id }`

      - `id: string`

        ID of the session that triggered the event.

      - `organization_id: string`

      - `type: "session.deleted"`

        - `"session.deleted"`

      - `workspace_id: string`

    - `BetaWebhookSessionStatusRescheduledEventData object { id, organization_id, type, workspace_id }`

      - `id: string`

        ID of the session that triggered the event.

      - `organization_id: string`

      - `type: "session.status_rescheduled"`

        - `"session.status_rescheduled"`

      - `workspace_id: string`

    - `BetaWebhookSessionStatusRunStartedEventData object { id, organization_id, type, workspace_id }`

      - `id: string`

        ID of the session that triggered the event.

      - `organization_id: string`

      - `type: "session.status_run_started"`

        - `"session.status_run_started"`

      - `workspace_id: string`

    - `BetaWebhookSessionStatusIdledEventData object { id, organization_id, type, workspace_id }`

      - `id: string`

        ID of the session that triggered the event.

      - `organization_id: string`

      - `type: "session.status_idled"`

        - `"session.status_idled"`

      - `workspace_id: string`

    - `BetaWebhookSessionStatusTerminatedEventData object { id, organization_id, type, workspace_id }`

      - `id: string`

        ID of the session that triggered the event.

      - `organization_id: string`

      - `type: "session.status_terminated"`

        - `"session.status_terminated"`

      - `workspace_id: string`

    - `BetaWebhookSessionThreadCreatedEventData object { id, organization_id, session_thread_id, 2 more }`

      - `id: string`

        ID of the session that triggered the event.

      - `organization_id: string`

      - `session_thread_id: string`

        ID of the session thread this event refers to.

      - `type: "session.thread_created"`

        - `"session.thread_created"`

      - `workspace_id: string`

    - `BetaWebhookSessionThreadIdledEventData object { id, organization_id, session_thread_id, 2 more }`

      - `id: string`

        ID of the session that triggered the event.

      - `organization_id: string`

      - `session_thread_id: string`

        ID of the session thread this event refers to.

      - `type: "session.thread_idled"`

        - `"session.thread_idled"`

      - `workspace_id: string`

    - `BetaWebhookSessionThreadTerminatedEventData object { id, organization_id, session_thread_id, 2 more }`

      - `id: string`

        ID of the session that triggered the event.

      - `organization_id: string`

      - `session_thread_id: string`

        ID of the session thread this event refers to.

      - `type: "session.thread_terminated"`

        - `"session.thread_terminated"`

      - `workspace_id: string`

    - `BetaWebhookSessionOutcomeEvaluationEndedEventData object { id, organization_id, type, workspace_id }`

      - `id: string`

        ID of the session that triggered the event.

      - `organization_id: string`

      - `type: "session.outcome_evaluation_ended"`

        - `"session.outcome_evaluation_ended"`

      - `workspace_id: string`

    - `BetaWebhookVaultCreatedEventData object { id, organization_id, type, workspace_id }`

      - `id: string`

        ID of the vault that triggered the event.

      - `organization_id: string`

      - `type: "vault.created"`

        - `"vault.created"`

      - `workspace_id: string`

    - `BetaWebhookVaultArchivedEventData object { id, organization_id, type, workspace_id }`

      - `id: string`

        ID of the vault that triggered the event.

      - `organization_id: string`

      - `type: "vault.archived"`

        - `"vault.archived"`

      - `workspace_id: string`

    - `BetaWebhookVaultDeletedEventData object { id, organization_id, type, workspace_id }`

      - `id: string`

        ID of the vault that triggered the event.

      - `organization_id: string`

      - `type: "vault.deleted"`

        - `"vault.deleted"`

      - `workspace_id: string`

    - `BetaWebhookVaultCredentialCreatedEventData object { id, organization_id, type, 2 more }`

      - `id: string`

        ID of the vault credential that triggered the event.

      - `organization_id: string`

      - `type: "vault_credential.created"`

        - `"vault_credential.created"`

      - `vault_id: string`

        ID of the vault that owns this credential.

      - `workspace_id: string`

    - `BetaWebhookVaultCredentialArchivedEventData object { id, organization_id, type, 2 more }`

      - `id: string`

        ID of the vault credential that triggered the event.

      - `organization_id: string`

      - `type: "vault_credential.archived"`

        - `"vault_credential.archived"`

      - `vault_id: string`

        ID of the vault that owns this credential.

      - `workspace_id: string`

    - `BetaWebhookVaultCredentialDeletedEventData object { id, organization_id, type, 2 more }`

      - `id: string`

        ID of the vault credential that triggered the event.

      - `organization_id: string`

      - `type: "vault_credential.deleted"`

        - `"vault_credential.deleted"`

      - `vault_id: string`

        ID of the vault that owns this credential.

      - `workspace_id: string`

    - `BetaWebhookVaultCredentialRefreshFailedEventData object { id, organization_id, type, 2 more }`

      - `id: string`

        ID of the vault credential that triggered the event.

      - `organization_id: string`

      - `type: "vault_credential.refresh_failed"`

        - `"vault_credential.refresh_failed"`

      - `vault_id: string`

        ID of the vault that owns this credential.

      - `workspace_id: string`

    - `BetaWebhookSessionUpdatedEventData object { id, organization_id, type, workspace_id }`

      - `id: string`

        ID of the session that triggered the event.

      - `organization_id: string`

      - `type: "session.updated"`

        - `"session.updated"`

      - `workspace_id: string`

    - `BetaWebhookAgentCreatedEventData object { id, organization_id, type, workspace_id }`

      - `id: string`

        ID of the agent that triggered the event.

      - `organization_id: string`

      - `type: "agent.created"`

        - `"agent.created"`

      - `workspace_id: string`

    - `BetaWebhookAgentArchivedEventData object { id, organization_id, type, workspace_id }`

      - `id: string`

        ID of the agent that triggered the event.

      - `organization_id: string`

      - `type: "agent.archived"`

        - `"agent.archived"`

      - `workspace_id: string`

    - `BetaWebhookAgentDeletedEventData object { id, organization_id, type, workspace_id }`

      - `id: string`

        ID of the agent that triggered the event.

      - `organization_id: string`

      - `type: "agent.deleted"`

        - `"agent.deleted"`

      - `workspace_id: string`

    - `BetaWebhookDeploymentPausedEventData object { id, organization_id, type, workspace_id }`

      - `id: string`

        ID of the deployment that triggered the event.

      - `organization_id: string`

      - `type: "deployment.paused"`

        - `"deployment.paused"`

      - `workspace_id: string`

    - `BetaWebhookDeploymentRunFailedEventData object { id, organization_id, type, workspace_id }`

      - `id: string`

        ID of the deployment run that triggered the event.

      - `organization_id: string`

      - `type: "deployment_run.failed"`

        - `"deployment_run.failed"`

      - `workspace_id: string`

    - `BetaWebhookDeploymentCreatedEventData object { id, organization_id, type, workspace_id }`

      - `id: string`

        ID of the deployment that triggered the event.

      - `organization_id: string`

      - `type: "deployment.created"`

        - `"deployment.created"`

      - `workspace_id: string`

    - `BetaWebhookDeploymentUpdatedEventData object { id, organization_id, type, workspace_id }`

      - `id: string`

        ID of the deployment that triggered the event.

      - `organization_id: string`

      - `type: "deployment.updated"`

        - `"deployment.updated"`

      - `workspace_id: string`

    - `BetaWebhookDeploymentUnpausedEventData object { id, organization_id, type, workspace_id }`

      - `id: string`

        ID of the deployment that triggered the event.

      - `organization_id: string`

      - `type: "deployment.unpaused"`

        - `"deployment.unpaused"`

      - `workspace_id: string`

    - `BetaWebhookAgentUpdatedEventData object { id, organization_id, type, workspace_id }`

      - `id: string`

        ID of the agent that triggered the event.

      - `organization_id: string`

      - `type: "agent.updated"`

        - `"agent.updated"`

      - `workspace_id: string`

    - `BetaWebhookDeploymentArchivedEventData object { id, organization_id, type, workspace_id }`

      - `id: string`

        ID of the deployment that triggered the event.

      - `organization_id: string`

      - `type: "deployment.archived"`

        - `"deployment.archived"`

      - `workspace_id: string`

    - `BetaWebhookDeploymentRunStartedEventData object { id, organization_id, type, workspace_id }`

      - `id: string`

        ID of the deployment run that triggered the event.

      - `organization_id: string`

      - `type: "deployment_run.started"`

        - `"deployment_run.started"`

      - `workspace_id: string`

    - `BetaWebhookDeploymentDeletedEventData object { id, organization_id, type, workspace_id }`

      - `id: string`

        ID of the deployment that triggered the event.

      - `organization_id: string`

      - `type: "deployment.deleted"`

        - `"deployment.deleted"`

      - `workspace_id: string`

    - `BetaWebhookDeploymentRunSucceededEventData object { id, organization_id, type, workspace_id }`

      - `id: string`

        ID of the deployment run that triggered the event.

      - `organization_id: string`

      - `type: "deployment_run.succeeded"`

        - `"deployment_run.succeeded"`

      - `workspace_id: string`

    - `BetaWebhookEnvironmentCreatedEventData object { id, organization_id, type, workspace_id }`

      - `id: string`

        ID of the environment that triggered the event.

      - `organization_id: string`

      - `type: "environment.created"`

        - `"environment.created"`

      - `workspace_id: string`

    - `BetaWebhookEnvironmentUpdatedEventData object { id, organization_id, type, workspace_id }`

      - `id: string`

        ID of the environment that triggered the event.

      - `organization_id: string`

      - `type: "environment.updated"`

        - `"environment.updated"`

      - `workspace_id: string`

    - `BetaWebhookEnvironmentArchivedEventData object { id, organization_id, type, workspace_id }`

      - `id: string`

        ID of the environment that triggered the event.

      - `organization_id: string`

      - `type: "environment.archived"`

        - `"environment.archived"`

      - `workspace_id: string`

    - `BetaWebhookEnvironmentDeletedEventData object { id, organization_id, type, workspace_id }`

      - `id: string`

        ID of the environment that triggered the event.

      - `organization_id: string`

      - `type: "environment.deleted"`

        - `"environment.deleted"`

      - `workspace_id: string`

    - `BetaWebhookMemoryStoreCreatedEventData object { id, organization_id, type, workspace_id }`

      - `id: string`

        ID of the memory store that triggered the event.

      - `organization_id: string`

      - `type: "memory_store.created"`

        - `"memory_store.created"`

      - `workspace_id: string`

    - `BetaWebhookMemoryStoreArchivedEventData object { id, organization_id, type, workspace_id }`

      - `id: string`

        ID of the memory store that triggered the event.

      - `organization_id: string`

      - `type: "memory_store.archived"`

        - `"memory_store.archived"`

      - `workspace_id: string`

    - `BetaWebhookMemoryStoreDeletedEventData object { id, organization_id, type, workspace_id }`

      - `id: string`

        ID of the memory store that triggered the event.

      - `organization_id: string`

      - `type: "memory_store.deleted"`

        - `"memory_store.deleted"`

      - `workspace_id: string`

  - `type: "event"`

    Object type. Always `event` for webhook payloads.

    - `"event"`

### Beta Webhook Event Data

- `BetaWebhookEventData = BetaWebhookSessionCreatedEventData or BetaWebhookSessionPendingEventData or BetaWebhookSessionRunningEventData or 40 more`

  - `BetaWebhookSessionCreatedEventData object { id, organization_id, type, workspace_id }`

    - `id: string`

      ID of the session that triggered the event.

    - `organization_id: string`

    - `type: "session.created"`

      - `"session.created"`

    - `workspace_id: string`

  - `BetaWebhookSessionPendingEventData object { id, organization_id, type, workspace_id }`

    - `id: string`

      ID of the session that triggered the event.

    - `organization_id: string`

    - `type: "session.pending"`

      - `"session.pending"`

    - `workspace_id: string`

  - `BetaWebhookSessionRunningEventData object { id, organization_id, type, workspace_id }`

    - `id: string`

      ID of the session that triggered the event.

    - `organization_id: string`

    - `type: "session.running"`

      - `"session.running"`

    - `workspace_id: string`

  - `BetaWebhookSessionIdledEventData object { id, organization_id, type, workspace_id }`

    - `id: string`

      ID of the session that triggered the event.

    - `organization_id: string`

    - `type: "session.idled"`

      - `"session.idled"`

    - `workspace_id: string`

  - `BetaWebhookSessionRequiresActionEventData object { id, organization_id, type, workspace_id }`

    - `id: string`

      ID of the session that triggered the event.

    - `organization_id: string`

    - `type: "session.requires_action"`

      - `"session.requires_action"`

    - `workspace_id: string`

  - `BetaWebhookSessionArchivedEventData object { id, organization_id, type, workspace_id }`

    - `id: string`

      ID of the session that triggered the event.

    - `organization_id: string`

    - `type: "session.archived"`

      - `"session.archived"`

    - `workspace_id: string`

  - `BetaWebhookSessionDeletedEventData object { id, organization_id, type, workspace_id }`

    - `id: string`

      ID of the session that triggered the event.

    - `organization_id: string`

    - `type: "session.deleted"`

      - `"session.deleted"`

    - `workspace_id: string`

  - `BetaWebhookSessionStatusRescheduledEventData object { id, organization_id, type, workspace_id }`

    - `id: string`

      ID of the session that triggered the event.

    - `organization_id: string`

    - `type: "session.status_rescheduled"`

      - `"session.status_rescheduled"`

    - `workspace_id: string`

  - `BetaWebhookSessionStatusRunStartedEventData object { id, organization_id, type, workspace_id }`

    - `id: string`

      ID of the session that triggered the event.

    - `organization_id: string`

    - `type: "session.status_run_started"`

      - `"session.status_run_started"`

    - `workspace_id: string`

  - `BetaWebhookSessionStatusIdledEventData object { id, organization_id, type, workspace_id }`

    - `id: string`

      ID of the session that triggered the event.

    - `organization_id: string`

    - `type: "session.status_idled"`

      - `"session.status_idled"`

    - `workspace_id: string`

  - `BetaWebhookSessionStatusTerminatedEventData object { id, organization_id, type, workspace_id }`

    - `id: string`

      ID of the session that triggered the event.

    - `organization_id: string`

    - `type: "session.status_terminated"`

      - `"session.status_terminated"`

    - `workspace_id: string`

  - `BetaWebhookSessionThreadCreatedEventData object { id, organization_id, session_thread_id, 2 more }`

    - `id: string`

      ID of the session that triggered the event.

    - `organization_id: string`

    - `session_thread_id: string`

      ID of the session thread this event refers to.

    - `type: "session.thread_created"`

      - `"session.thread_created"`

    - `workspace_id: string`

  - `BetaWebhookSessionThreadIdledEventData object { id, organization_id, session_thread_id, 2 more }`

    - `id: string`

      ID of the session that triggered the event.

    - `organization_id: string`

    - `session_thread_id: string`

      ID of the session thread this event refers to.

    - `type: "session.thread_idled"`

      - `"session.thread_idled"`

    - `workspace_id: string`

  - `BetaWebhookSessionThreadTerminatedEventData object { id, organization_id, session_thread_id, 2 more }`

    - `id: string`

      ID of the session that triggered the event.

    - `organization_id: string`

    - `session_thread_id: string`

      ID of the session thread this event refers to.

    - `type: "session.thread_terminated"`

      - `"session.thread_terminated"`

    - `workspace_id: string`

  - `BetaWebhookSessionOutcomeEvaluationEndedEventData object { id, organization_id, type, workspace_id }`

    - `id: string`

      ID of the session that triggered the event.

    - `organization_id: string`

    - `type: "session.outcome_evaluation_ended"`

      - `"session.outcome_evaluation_ended"`

    - `workspace_id: string`

  - `BetaWebhookVaultCreatedEventData object { id, organization_id, type, workspace_id }`

    - `id: string`

      ID of the vault that triggered the event.

    - `organization_id: string`

    - `type: "vault.created"`

      - `"vault.created"`

    - `workspace_id: string`

  - `BetaWebhookVaultArchivedEventData object { id, organization_id, type, workspace_id }`

    - `id: string`

      ID of the vault that triggered the event.

    - `organization_id: string`

    - `type: "vault.archived"`

      - `"vault.archived"`

    - `workspace_id: string`

  - `BetaWebhookVaultDeletedEventData object { id, organization_id, type, workspace_id }`

    - `id: string`

      ID of the vault that triggered the event.

    - `organization_id: string`

    - `type: "vault.deleted"`

      - `"vault.deleted"`

    - `workspace_id: string`

  - `BetaWebhookVaultCredentialCreatedEventData object { id, organization_id, type, 2 more }`

    - `id: string`

      ID of the vault credential that triggered the event.

    - `organization_id: string`

    - `type: "vault_credential.created"`

      - `"vault_credential.created"`

    - `vault_id: string`

      ID of the vault that owns this credential.

    - `workspace_id: string`

  - `BetaWebhookVaultCredentialArchivedEventData object { id, organization_id, type, 2 more }`

    - `id: string`

      ID of the vault credential that triggered the event.

    - `organization_id: string`

    - `type: "vault_credential.archived"`

      - `"vault_credential.archived"`

    - `vault_id: string`

      ID of the vault that owns this credential.

    - `workspace_id: string`

  - `BetaWebhookVaultCredentialDeletedEventData object { id, organization_id, type, 2 more }`

    - `id: string`

      ID of the vault credential that triggered the event.

    - `organization_id: string`

    - `type: "vault_credential.deleted"`

      - `"vault_credential.deleted"`

    - `vault_id: string`

      ID of the vault that owns this credential.

    - `workspace_id: string`

  - `BetaWebhookVaultCredentialRefreshFailedEventData object { id, organization_id, type, 2 more }`

    - `id: string`

      ID of the vault credential that triggered the event.

    - `organization_id: string`

    - `type: "vault_credential.refresh_failed"`

      - `"vault_credential.refresh_failed"`

    - `vault_id: string`

      ID of the vault that owns this credential.

    - `workspace_id: string`

  - `BetaWebhookSessionUpdatedEventData object { id, organization_id, type, workspace_id }`

    - `id: string`

      ID of the session that triggered the event.

    - `organization_id: string`

    - `type: "session.updated"`

      - `"session.updated"`

    - `workspace_id: string`

  - `BetaWebhookAgentCreatedEventData object { id, organization_id, type, workspace_id }`

    - `id: string`

      ID of the agent that triggered the event.

    - `organization_id: string`

    - `type: "agent.created"`

      - `"agent.created"`

    - `workspace_id: string`

  - `BetaWebhookAgentArchivedEventData object { id, organization_id, type, workspace_id }`

    - `id: string`

      ID of the agent that triggered the event.

    - `organization_id: string`

    - `type: "agent.archived"`

      - `"agent.archived"`

    - `workspace_id: string`

  - `BetaWebhookAgentDeletedEventData object { id, organization_id, type, workspace_id }`

    - `id: string`

      ID of the agent that triggered the event.

    - `organization_id: string`

    - `type: "agent.deleted"`

      - `"agent.deleted"`

    - `workspace_id: string`

  - `BetaWebhookDeploymentPausedEventData object { id, organization_id, type, workspace_id }`

    - `id: string`

      ID of the deployment that triggered the event.

    - `organization_id: string`

    - `type: "deployment.paused"`

      - `"deployment.paused"`

    - `workspace_id: string`

  - `BetaWebhookDeploymentRunFailedEventData object { id, organization_id, type, workspace_id }`

    - `id: string`

      ID of the deployment run that triggered the event.

    - `organization_id: string`

    - `type: "deployment_run.failed"`

      - `"deployment_run.failed"`

    - `workspace_id: string`

  - `BetaWebhookDeploymentCreatedEventData object { id, organization_id, type, workspace_id }`

    - `id: string`

      ID of the deployment that triggered the event.

    - `organization_id: string`

    - `type: "deployment.created"`

      - `"deployment.created"`

    - `workspace_id: string`

  - `BetaWebhookDeploymentUpdatedEventData object { id, organization_id, type, workspace_id }`

    - `id: string`

      ID of the deployment that triggered the event.

    - `organization_id: string`

    - `type: "deployment.updated"`

      - `"deployment.updated"`

    - `workspace_id: string`

  - `BetaWebhookDeploymentUnpausedEventData object { id, organization_id, type, workspace_id }`

    - `id: string`

      ID of the deployment that triggered the event.

    - `organization_id: string`

    - `type: "deployment.unpaused"`

      - `"deployment.unpaused"`

    - `workspace_id: string`

  - `BetaWebhookAgentUpdatedEventData object { id, organization_id, type, workspace_id }`

    - `id: string`

      ID of the agent that triggered the event.

    - `organization_id: string`

    - `type: "agent.updated"`

      - `"agent.updated"`

    - `workspace_id: string`

  - `BetaWebhookDeploymentArchivedEventData object { id, organization_id, type, workspace_id }`

    - `id: string`

      ID of the deployment that triggered the event.

    - `organization_id: string`

    - `type: "deployment.archived"`

      - `"deployment.archived"`

    - `workspace_id: string`

  - `BetaWebhookDeploymentRunStartedEventData object { id, organization_id, type, workspace_id }`

    - `id: string`

      ID of the deployment run that triggered the event.

    - `organization_id: string`

    - `type: "deployment_run.started"`

      - `"deployment_run.started"`

    - `workspace_id: string`

  - `BetaWebhookDeploymentDeletedEventData object { id, organization_id, type, workspace_id }`

    - `id: string`

      ID of the deployment that triggered the event.

    - `organization_id: string`

    - `type: "deployment.deleted"`

      - `"deployment.deleted"`

    - `workspace_id: string`

  - `BetaWebhookDeploymentRunSucceededEventData object { id, organization_id, type, workspace_id }`

    - `id: string`

      ID of the deployment run that triggered the event.

    - `organization_id: string`

    - `type: "deployment_run.succeeded"`

      - `"deployment_run.succeeded"`

    - `workspace_id: string`

  - `BetaWebhookEnvironmentCreatedEventData object { id, organization_id, type, workspace_id }`

    - `id: string`

      ID of the environment that triggered the event.

    - `organization_id: string`

    - `type: "environment.created"`

      - `"environment.created"`

    - `workspace_id: string`

  - `BetaWebhookEnvironmentUpdatedEventData object { id, organization_id, type, workspace_id }`

    - `id: string`

      ID of the environment that triggered the event.

    - `organization_id: string`

    - `type: "environment.updated"`

      - `"environment.updated"`

    - `workspace_id: string`

  - `BetaWebhookEnvironmentArchivedEventData object { id, organization_id, type, workspace_id }`

    - `id: string`

      ID of the environment that triggered the event.

    - `organization_id: string`

    - `type: "environment.archived"`

      - `"environment.archived"`

    - `workspace_id: string`

  - `BetaWebhookEnvironmentDeletedEventData object { id, organization_id, type, workspace_id }`

    - `id: string`

      ID of the environment that triggered the event.

    - `organization_id: string`

    - `type: "environment.deleted"`

      - `"environment.deleted"`

    - `workspace_id: string`

  - `BetaWebhookMemoryStoreCreatedEventData object { id, organization_id, type, workspace_id }`

    - `id: string`

      ID of the memory store that triggered the event.

    - `organization_id: string`

    - `type: "memory_store.created"`

      - `"memory_store.created"`

    - `workspace_id: string`

  - `BetaWebhookMemoryStoreArchivedEventData object { id, organization_id, type, workspace_id }`

    - `id: string`

      ID of the memory store that triggered the event.

    - `organization_id: string`

    - `type: "memory_store.archived"`

      - `"memory_store.archived"`

    - `workspace_id: string`

  - `BetaWebhookMemoryStoreDeletedEventData object { id, organization_id, type, workspace_id }`

    - `id: string`

      ID of the memory store that triggered the event.

    - `organization_id: string`

    - `type: "memory_store.deleted"`

      - `"memory_store.deleted"`

    - `workspace_id: string`

### Beta Webhook Memory Store Archived Event Data

- `BetaWebhookMemoryStoreArchivedEventData object { id, organization_id, type, workspace_id }`

  - `id: string`

    ID of the memory store that triggered the event.

  - `organization_id: string`

  - `type: "memory_store.archived"`

    - `"memory_store.archived"`

  - `workspace_id: string`

### Beta Webhook Memory Store Created Event Data

- `BetaWebhookMemoryStoreCreatedEventData object { id, organization_id, type, workspace_id }`

  - `id: string`

    ID of the memory store that triggered the event.

  - `organization_id: string`

  - `type: "memory_store.created"`

    - `"memory_store.created"`

  - `workspace_id: string`

### Beta Webhook Memory Store Deleted Event Data

- `BetaWebhookMemoryStoreDeletedEventData object { id, organization_id, type, workspace_id }`

  - `id: string`

    ID of the memory store that triggered the event.

  - `organization_id: string`

  - `type: "memory_store.deleted"`

    - `"memory_store.deleted"`

  - `workspace_id: string`

### Beta Webhook Session Archived Event Data

- `BetaWebhookSessionArchivedEventData object { id, organization_id, type, workspace_id }`

  - `id: string`

    ID of the session that triggered the event.

  - `organization_id: string`

  - `type: "session.archived"`

    - `"session.archived"`

  - `workspace_id: string`

### Beta Webhook Session Created Event Data

- `BetaWebhookSessionCreatedEventData object { id, organization_id, type, workspace_id }`

  - `id: string`

    ID of the session that triggered the event.

  - `organization_id: string`

  - `type: "session.created"`

    - `"session.created"`

  - `workspace_id: string`

### Beta Webhook Session Deleted Event Data

- `BetaWebhookSessionDeletedEventData object { id, organization_id, type, workspace_id }`

  - `id: string`

    ID of the session that triggered the event.

  - `organization_id: string`

  - `type: "session.deleted"`

    - `"session.deleted"`

  - `workspace_id: string`

### Beta Webhook Session Idled Event Data

- `BetaWebhookSessionIdledEventData object { id, organization_id, type, workspace_id }`

  - `id: string`

    ID of the session that triggered the event.

  - `organization_id: string`

  - `type: "session.idled"`

    - `"session.idled"`

  - `workspace_id: string`

### Beta Webhook Session Outcome Evaluation Ended Event Data

- `BetaWebhookSessionOutcomeEvaluationEndedEventData object { id, organization_id, type, workspace_id }`

  - `id: string`

    ID of the session that triggered the event.

  - `organization_id: string`

  - `type: "session.outcome_evaluation_ended"`

    - `"session.outcome_evaluation_ended"`

  - `workspace_id: string`

### Beta Webhook Session Pending Event Data

- `BetaWebhookSessionPendingEventData object { id, organization_id, type, workspace_id }`

  - `id: string`

    ID of the session that triggered the event.

  - `organization_id: string`

  - `type: "session.pending"`

    - `"session.pending"`

  - `workspace_id: string`

### Beta Webhook Session Requires Action Event Data

- `BetaWebhookSessionRequiresActionEventData object { id, organization_id, type, workspace_id }`

  - `id: string`

    ID of the session that triggered the event.

  - `organization_id: string`

  - `type: "session.requires_action"`

    - `"session.requires_action"`

  - `workspace_id: string`

### Beta Webhook Session Running Event Data

- `BetaWebhookSessionRunningEventData object { id, organization_id, type, workspace_id }`

  - `id: string`

    ID of the session that triggered the event.

  - `organization_id: string`

  - `type: "session.running"`

    - `"session.running"`

  - `workspace_id: string`

### Beta Webhook Session Status Idled Event Data

- `BetaWebhookSessionStatusIdledEventData object { id, organization_id, type, workspace_id }`

  - `id: string`

    ID of the session that triggered the event.

  - `organization_id: string`

  - `type: "session.status_idled"`

    - `"session.status_idled"`

  - `workspace_id: string`

### Beta Webhook Session Status Rescheduled Event Data

- `BetaWebhookSessionStatusRescheduledEventData object { id, organization_id, type, workspace_id }`

  - `id: string`

    ID of the session that triggered the event.

  - `organization_id: string`

  - `type: "session.status_rescheduled"`

    - `"session.status_rescheduled"`

  - `workspace_id: string`

### Beta Webhook Session Status Run Started Event Data

- `BetaWebhookSessionStatusRunStartedEventData object { id, organization_id, type, workspace_id }`

  - `id: string`

    ID of the session that triggered the event.

  - `organization_id: string`

  - `type: "session.status_run_started"`

    - `"session.status_run_started"`

  - `workspace_id: string`

### Beta Webhook Session Status Terminated Event Data

- `BetaWebhookSessionStatusTerminatedEventData object { id, organization_id, type, workspace_id }`

  - `id: string`

    ID of the session that triggered the event.

  - `organization_id: string`

  - `type: "session.status_terminated"`

    - `"session.status_terminated"`

  - `workspace_id: string`

### Beta Webhook Session Thread Created Event Data

- `BetaWebhookSessionThreadCreatedEventData object { id, organization_id, session_thread_id, 2 more }`

  - `id: string`

    ID of the session that triggered the event.

  - `organization_id: string`

  - `session_thread_id: string`

    ID of the session thread this event refers to.

  - `type: "session.thread_created"`

    - `"session.thread_created"`

  - `workspace_id: string`

### Beta Webhook Session Thread Idled Event Data

- `BetaWebhookSessionThreadIdledEventData object { id, organization_id, session_thread_id, 2 more }`

  - `id: string`

    ID of the session that triggered the event.

  - `organization_id: string`

  - `session_thread_id: string`

    ID of the session thread this event refers to.

  - `type: "session.thread_idled"`

    - `"session.thread_idled"`

  - `workspace_id: string`

### Beta Webhook Session Thread Terminated Event Data

- `BetaWebhookSessionThreadTerminatedEventData object { id, organization_id, session_thread_id, 2 more }`

  - `id: string`

    ID of the session that triggered the event.

  - `organization_id: string`

  - `session_thread_id: string`

    ID of the session thread this event refers to.

  - `type: "session.thread_terminated"`

    - `"session.thread_terminated"`

  - `workspace_id: string`

### Beta Webhook Session Updated Event Data

- `BetaWebhookSessionUpdatedEventData object { id, organization_id, type, workspace_id }`

  - `id: string`

    ID of the session that triggered the event.

  - `organization_id: string`

  - `type: "session.updated"`

    - `"session.updated"`

  - `workspace_id: string`

### Beta Webhook Vault Archived Event Data

- `BetaWebhookVaultArchivedEventData object { id, organization_id, type, workspace_id }`

  - `id: string`

    ID of the vault that triggered the event.

  - `organization_id: string`

  - `type: "vault.archived"`

    - `"vault.archived"`

  - `workspace_id: string`

### Beta Webhook Vault Created Event Data

- `BetaWebhookVaultCreatedEventData object { id, organization_id, type, workspace_id }`

  - `id: string`

    ID of the vault that triggered the event.

  - `organization_id: string`

  - `type: "vault.created"`

    - `"vault.created"`

  - `workspace_id: string`

### Beta Webhook Vault Credential Archived Event Data

- `BetaWebhookVaultCredentialArchivedEventData object { id, organization_id, type, 2 more }`

  - `id: string`

    ID of the vault credential that triggered the event.

  - `organization_id: string`

  - `type: "vault_credential.archived"`

    - `"vault_credential.archived"`

  - `vault_id: string`

    ID of the vault that owns this credential.

  - `workspace_id: string`

### Beta Webhook Vault Credential Created Event Data

- `BetaWebhookVaultCredentialCreatedEventData object { id, organization_id, type, 2 more }`

  - `id: string`

    ID of the vault credential that triggered the event.

  - `organization_id: string`

  - `type: "vault_credential.created"`

    - `"vault_credential.created"`

  - `vault_id: string`

    ID of the vault that owns this credential.

  - `workspace_id: string`

### Beta Webhook Vault Credential Deleted Event Data

- `BetaWebhookVaultCredentialDeletedEventData object { id, organization_id, type, 2 more }`

  - `id: string`

    ID of the vault credential that triggered the event.

  - `organization_id: string`

  - `type: "vault_credential.deleted"`

    - `"vault_credential.deleted"`

  - `vault_id: string`

    ID of the vault that owns this credential.

  - `workspace_id: string`

### Beta Webhook Vault Credential Refresh Failed Event Data

- `BetaWebhookVaultCredentialRefreshFailedEventData object { id, organization_id, type, 2 more }`

  - `id: string`

    ID of the vault credential that triggered the event.

  - `organization_id: string`

  - `type: "vault_credential.refresh_failed"`

    - `"vault_credential.refresh_failed"`

  - `vault_id: string`

    ID of the vault that owns this credential.

  - `workspace_id: string`

### Beta Webhook Vault Deleted Event Data

- `BetaWebhookVaultDeletedEventData object { id, organization_id, type, workspace_id }`

  - `id: string`

    ID of the vault that triggered the event.

  - `organization_id: string`

  - `type: "vault.deleted"`

    - `"vault.deleted"`

  - `workspace_id: string`

### Unwrap Webhook Event

- `UnwrapWebhookEvent object { id, created_at, data, type }`

  - `id: string`

    Unique event identifier for idempotency.

  - `created_at: string`

    RFC 3339 timestamp when the event occurred.

  - `data: BetaWebhookEventData`

    - `BetaWebhookSessionCreatedEventData object { id, organization_id, type, workspace_id }`

      - `id: string`

        ID of the session that triggered the event.

      - `organization_id: string`

      - `type: "session.created"`

        - `"session.created"`

      - `workspace_id: string`

    - `BetaWebhookSessionPendingEventData object { id, organization_id, type, workspace_id }`

      - `id: string`

        ID of the session that triggered the event.

      - `organization_id: string`

      - `type: "session.pending"`

        - `"session.pending"`

      - `workspace_id: string`

    - `BetaWebhookSessionRunningEventData object { id, organization_id, type, workspace_id }`

      - `id: string`

        ID of the session that triggered the event.

      - `organization_id: string`

      - `type: "session.running"`

        - `"session.running"`

      - `workspace_id: string`

    - `BetaWebhookSessionIdledEventData object { id, organization_id, type, workspace_id }`

      - `id: string`

        ID of the session that triggered the event.

      - `organization_id: string`

      - `type: "session.idled"`

        - `"session.idled"`

      - `workspace_id: string`

    - `BetaWebhookSessionRequiresActionEventData object { id, organization_id, type, workspace_id }`

      - `id: string`

        ID of the session that triggered the event.

      - `organization_id: string`

      - `type: "session.requires_action"`

        - `"session.requires_action"`

      - `workspace_id: string`

    - `BetaWebhookSessionArchivedEventData object { id, organization_id, type, workspace_id }`

      - `id: string`

        ID of the session that triggered the event.

      - `organization_id: string`

      - `type: "session.archived"`

        - `"session.archived"`

      - `workspace_id: string`

    - `BetaWebhookSessionDeletedEventData object { id, organization_id, type, workspace_id }`

      - `id: string`

        ID of the session that triggered the event.

      - `organization_id: string`

      - `type: "session.deleted"`

        - `"session.deleted"`

      - `workspace_id: string`

    - `BetaWebhookSessionStatusRescheduledEventData object { id, organization_id, type, workspace_id }`

      - `id: string`

        ID of the session that triggered the event.

      - `organization_id: string`

      - `type: "session.status_rescheduled"`

        - `"session.status_rescheduled"`

      - `workspace_id: string`

    - `BetaWebhookSessionStatusRunStartedEventData object { id, organization_id, type, workspace_id }`

      - `id: string`

        ID of the session that triggered the event.

      - `organization_id: string`

      - `type: "session.status_run_started"`

        - `"session.status_run_started"`

      - `workspace_id: string`

    - `BetaWebhookSessionStatusIdledEventData object { id, organization_id, type, workspace_id }`

      - `id: string`

        ID of the session that triggered the event.

      - `organization_id: string`

      - `type: "session.status_idled"`

        - `"session.status_idled"`

      - `workspace_id: string`

    - `BetaWebhookSessionStatusTerminatedEventData object { id, organization_id, type, workspace_id }`

      - `id: string`

        ID of the session that triggered the event.

      - `organization_id: string`

      - `type: "session.status_terminated"`

        - `"session.status_terminated"`

      - `workspace_id: string`

    - `BetaWebhookSessionThreadCreatedEventData object { id, organization_id, session_thread_id, 2 more }`

      - `id: string`

        ID of the session that triggered the event.

      - `organization_id: string`

      - `session_thread_id: string`

        ID of the session thread this event refers to.

      - `type: "session.thread_created"`

        - `"session.thread_created"`

      - `workspace_id: string`

    - `BetaWebhookSessionThreadIdledEventData object { id, organization_id, session_thread_id, 2 more }`

      - `id: string`

        ID of the session that triggered the event.

      - `organization_id: string`

      - `session_thread_id: string`

        ID of the session thread this event refers to.

      - `type: "session.thread_idled"`

        - `"session.thread_idled"`

      - `workspace_id: string`

    - `BetaWebhookSessionThreadTerminatedEventData object { id, organization_id, session_thread_id, 2 more }`

      - `id: string`

        ID of the session that triggered the event.

      - `organization_id: string`

      - `session_thread_id: string`

        ID of the session thread this event refers to.

      - `type: "session.thread_terminated"`

        - `"session.thread_terminated"`

      - `workspace_id: string`

    - `BetaWebhookSessionOutcomeEvaluationEndedEventData object { id, organization_id, type, workspace_id }`

      - `id: string`

        ID of the session that triggered the event.

      - `organization_id: string`

      - `type: "session.outcome_evaluation_ended"`

        - `"session.outcome_evaluation_ended"`

      - `workspace_id: string`

    - `BetaWebhookVaultCreatedEventData object { id, organization_id, type, workspace_id }`

      - `id: string`

        ID of the vault that triggered the event.

      - `organization_id: string`

      - `type: "vault.created"`

        - `"vault.created"`

      - `workspace_id: string`

    - `BetaWebhookVaultArchivedEventData object { id, organization_id, type, workspace_id }`

      - `id: string`

        ID of the vault that triggered the event.

      - `organization_id: string`

      - `type: "vault.archived"`

        - `"vault.archived"`

      - `workspace_id: string`

    - `BetaWebhookVaultDeletedEventData object { id, organization_id, type, workspace_id }`

      - `id: string`

        ID of the vault that triggered the event.

      - `organization_id: string`

      - `type: "vault.deleted"`

        - `"vault.deleted"`

      - `workspace_id: string`

    - `BetaWebhookVaultCredentialCreatedEventData object { id, organization_id, type, 2 more }`

      - `id: string`

        ID of the vault credential that triggered the event.

      - `organization_id: string`

      - `type: "vault_credential.created"`

        - `"vault_credential.created"`

      - `vault_id: string`

        ID of the vault that owns this credential.

      - `workspace_id: string`

    - `BetaWebhookVaultCredentialArchivedEventData object { id, organization_id, type, 2 more }`

      - `id: string`

        ID of the vault credential that triggered the event.

      - `organization_id: string`

      - `type: "vault_credential.archived"`

        - `"vault_credential.archived"`

      - `vault_id: string`

        ID of the vault that owns this credential.

      - `workspace_id: string`

    - `BetaWebhookVaultCredentialDeletedEventData object { id, organization_id, type, 2 more }`

      - `id: string`

        ID of the vault credential that triggered the event.

      - `organization_id: string`

      - `type: "vault_credential.deleted"`

        - `"vault_credential.deleted"`

      - `vault_id: string`

        ID of the vault that owns this credential.

      - `workspace_id: string`

    - `BetaWebhookVaultCredentialRefreshFailedEventData object { id, organization_id, type, 2 more }`

      - `id: string`

        ID of the vault credential that triggered the event.

      - `organization_id: string`

      - `type: "vault_credential.refresh_failed"`

        - `"vault_credential.refresh_failed"`

      - `vault_id: string`

        ID of the vault that owns this credential.

      - `workspace_id: string`

    - `BetaWebhookSessionUpdatedEventData object { id, organization_id, type, workspace_id }`

      - `id: string`

        ID of the session that triggered the event.

      - `organization_id: string`

      - `type: "session.updated"`

        - `"session.updated"`

      - `workspace_id: string`

    - `BetaWebhookAgentCreatedEventData object { id, organization_id, type, workspace_id }`

      - `id: string`

        ID of the agent that triggered the event.

      - `organization_id: string`

      - `type: "agent.created"`

        - `"agent.created"`

      - `workspace_id: string`

    - `BetaWebhookAgentArchivedEventData object { id, organization_id, type, workspace_id }`

      - `id: string`

        ID of the agent that triggered the event.

      - `organization_id: string`

      - `type: "agent.archived"`

        - `"agent.archived"`

      - `workspace_id: string`

    - `BetaWebhookAgentDeletedEventData object { id, organization_id, type, workspace_id }`

      - `id: string`

        ID of the agent that triggered the event.

      - `organization_id: string`

      - `type: "agent.deleted"`

        - `"agent.deleted"`

      - `workspace_id: string`

    - `BetaWebhookDeploymentPausedEventData object { id, organization_id, type, workspace_id }`

      - `id: string`

        ID of the deployment that triggered the event.

      - `organization_id: string`

      - `type: "deployment.paused"`

        - `"deployment.paused"`

      - `workspace_id: string`

    - `BetaWebhookDeploymentRunFailedEventData object { id, organization_id, type, workspace_id }`

      - `id: string`

        ID of the deployment run that triggered the event.

      - `organization_id: string`

      - `type: "deployment_run.failed"`

        - `"deployment_run.failed"`

      - `workspace_id: string`

    - `BetaWebhookDeploymentCreatedEventData object { id, organization_id, type, workspace_id }`

      - `id: string`

        ID of the deployment that triggered the event.

      - `organization_id: string`

      - `type: "deployment.created"`

        - `"deployment.created"`

      - `workspace_id: string`

    - `BetaWebhookDeploymentUpdatedEventData object { id, organization_id, type, workspace_id }`

      - `id: string`

        ID of the deployment that triggered the event.

      - `organization_id: string`

      - `type: "deployment.updated"`

        - `"deployment.updated"`

      - `workspace_id: string`

    - `BetaWebhookDeploymentUnpausedEventData object { id, organization_id, type, workspace_id }`

      - `id: string`

        ID of the deployment that triggered the event.

      - `organization_id: string`

      - `type: "deployment.unpaused"`

        - `"deployment.unpaused"`

      - `workspace_id: string`

    - `BetaWebhookAgentUpdatedEventData object { id, organization_id, type, workspace_id }`

      - `id: string`

        ID of the agent that triggered the event.

      - `organization_id: string`

      - `type: "agent.updated"`

        - `"agent.updated"`

      - `workspace_id: string`

    - `BetaWebhookDeploymentArchivedEventData object { id, organization_id, type, workspace_id }`

      - `id: string`

        ID of the deployment that triggered the event.

      - `organization_id: string`

      - `type: "deployment.archived"`

        - `"deployment.archived"`

      - `workspace_id: string`

    - `BetaWebhookDeploymentRunStartedEventData object { id, organization_id, type, workspace_id }`

      - `id: string`

        ID of the deployment run that triggered the event.

      - `organization_id: string`

      - `type: "deployment_run.started"`

        - `"deployment_run.started"`

      - `workspace_id: string`

    - `BetaWebhookDeploymentDeletedEventData object { id, organization_id, type, workspace_id }`

      - `id: string`

        ID of the deployment that triggered the event.

      - `organization_id: string`

      - `type: "deployment.deleted"`

        - `"deployment.deleted"`

      - `workspace_id: string`

    - `BetaWebhookDeploymentRunSucceededEventData object { id, organization_id, type, workspace_id }`

      - `id: string`

        ID of the deployment run that triggered the event.

      - `organization_id: string`

      - `type: "deployment_run.succeeded"`

        - `"deployment_run.succeeded"`

      - `workspace_id: string`

    - `BetaWebhookEnvironmentCreatedEventData object { id, organization_id, type, workspace_id }`

      - `id: string`

        ID of the environment that triggered the event.

      - `organization_id: string`

      - `type: "environment.created"`

        - `"environment.created"`

      - `workspace_id: string`

    - `BetaWebhookEnvironmentUpdatedEventData object { id, organization_id, type, workspace_id }`

      - `id: string`

        ID of the environment that triggered the event.

      - `organization_id: string`

      - `type: "environment.updated"`

        - `"environment.updated"`

      - `workspace_id: string`

    - `BetaWebhookEnvironmentArchivedEventData object { id, organization_id, type, workspace_id }`

      - `id: string`

        ID of the environment that triggered the event.

      - `organization_id: string`

      - `type: "environment.archived"`

        - `"environment.archived"`

      - `workspace_id: string`

    - `BetaWebhookEnvironmentDeletedEventData object { id, organization_id, type, workspace_id }`

      - `id: string`

        ID of the environment that triggered the event.

      - `organization_id: string`

      - `type: "environment.deleted"`

        - `"environment.deleted"`

      - `workspace_id: string`

    - `BetaWebhookMemoryStoreCreatedEventData object { id, organization_id, type, workspace_id }`

      - `id: string`

        ID of the memory store that triggered the event.

      - `organization_id: string`

      - `type: "memory_store.created"`

        - `"memory_store.created"`

      - `workspace_id: string`

    - `BetaWebhookMemoryStoreArchivedEventData object { id, organization_id, type, workspace_id }`

      - `id: string`

        ID of the memory store that triggered the event.

      - `organization_id: string`

      - `type: "memory_store.archived"`

        - `"memory_store.archived"`

      - `workspace_id: string`

    - `BetaWebhookMemoryStoreDeletedEventData object { id, organization_id, type, workspace_id }`

      - `id: string`

        ID of the memory store that triggered the event.

      - `organization_id: string`

      - `type: "memory_store.deleted"`

        - `"memory_store.deleted"`

      - `workspace_id: string`

  - `type: "event"`

    Object type. Always `event` for webhook payloads.

    - `"event"`
