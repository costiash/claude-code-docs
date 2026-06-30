# Self-hosted sandboxes

Run agent sessions in your own self-hosted sandbox environment.

---

By default, Managed Agents executes tools and code inside [Anthropic-managed cloud sandboxes](/docs/en/managed-agents/cloud-sandboxes-reference). Self-hosted sandboxes keep the orchestration on Anthropic's side but move tool execution into infrastructure you control, so the agent's code, filesystem, and network egress never leave your environment.

Tool execution stays on your host: the filesystem the agent reads and writes, the processes it spawns, and the network it can reach are all under your control. Tool inputs and outputs still flow to Anthropic's control plane (where Claude runs) so the model can see results and determine what to do next. See the [security model](/docs/en/managed-agents/self-hosted-sandboxes-security) for the full data-flow boundary.

<Note>
  Self-hosted sandboxes support all Claude models available in Managed Agents, including Claude Opus 4.8. The model is configured on the [agent](/docs/en/managed-agents/agent-setup), not the environment.
</Note>

## How it differs from cloud environments

|                               | Cloud environment           | Self-hosted sandbox |
| ----------------------------- | --------------------------- | ------------------- |
| Where tools run               | Anthropic-managed sandboxes | Your infrastructure |
| Network reach                 | Anthropic's egress controls | Your network policy |
| File and GitHub repo mounting | Managed by Anthropic        | Managed by you      |
| Lifecycle                     | Managed by Anthropic        | Managed by you      |

Self-hosting is a good fit when the agent needs to operate on data that cannot leave your network boundary, reach internal services that are not publicly routable, or run under your organization's own compliance and audit controls.

For Zero Data Retention and HIPAA BAA eligibility, see [API and data retention](/docs/en/manage-claude/api-and-data-retention#feature-eligibility).

## When to combine with MCP tunnels

Self-hosting controls *where the agent's code executes*. [MCP tunnels](/docs/en/agents-and-tools/mcp-tunnels/overview) control *how Anthropic reaches MCP servers in your network*. They are independent: a session running in Anthropic's cloud sandboxes can still reach private MCP servers through a tunnel, and a self-hosted session can use either tunneled or public MCP servers. Use both when you want execution and tool access to stay inside your boundary.

## Environment worker

<Tip>
  This guide describes how to build a worker with any generic sandboxing platform. Additional, platform-specific guides are available for [AWS Lambda MicroVMs](https://docs.aws.amazon.com/lambda/latest/dg/microvms-integrations-claude-managed-agents.html), [Blaxel](https://docs.blaxel.ai/Tutorials/Claude-Managed-Agents), [Cloudflare](https://developers.cloudflare.com/sandbox/claude-managed-agents/), [Daytona](https://www.daytona.io/docs/en/guides/claude/claude-managed-agents), [E2B](https://e2b.dev/docs/agents/claude-managed-agents), [GKE Agent Sandbox](https://github.com/GoogleCloudPlatform/kubernetes-engine-samples/tree/main/ai-ml/anthropic-agent-sandbox), [Modal](https://github.com/modal-labs/claude-managed-agents-modal-sandbox), [Namespace](https://namespace.so/docs/integrations/claude), [Superserve](https://docs.superserve.ai/integrations/managed-agents/claude-managed-agents), and [Vercel](https://vercel.com/kb/guide/run-claude-managed-agent-tools-with-vercel-sandbox).
</Tip>

An environment worker is a process you run on your own infrastructure. It receives tool execution requests from Anthropic and runs them locally. The `self_hosted` environment acts as a work queue: when a [session](/docs/en/managed-agents/sessions) is assigned to it, Anthropic enqueues the session as a work item. Your worker claims work items from that queue, spawns an execution context for each one, downloads the agent's [skills](/docs/en/managed-agents/skills) (reusable, filesystem-based resources that give the agent domain-specific expertise), runs the tool calls, and posts the results back.

Work items are claimed by polling the environment's queue: either by an **always-on worker** that polls continuously, or a **webhook-triggered handler** that wakes on `session.status_run_started` and starts polling.

The CLI and SDK both ship pre-built workers. The `ant` CLI supports the always-on pattern only; the SDK supports both always-on and webhook-triggered. Both are configurable: see [Self-hosted worker](/docs/en/managed-agents/reference#self-hosted-worker) in the reference for CLI flags, and [SDK helpers](#sdk-helpers) on this page for the SDK options. For more control, call the [Environments Work endpoints](/docs/en/api/beta/environments/work) directly and implement your own worker.

### Sandbox filesystem

* **`/workspace`:** the system default working directory for tool execution and skill download. The CLI's `--workdir` flag defaults to the current directory; pass `--workdir /workspace` to match the system default. Skills are downloaded to `<workdir>/skills/<name>/`. If you use a different working directory, update your agent's system prompt so Claude can locate the skill files.
* **`/mnt/session/outputs`:** the worker harness instructs Claude to write final deliverables here. In sandbox mode, mount a host directory at this path to retrieve outputs after the session ends. In in-process mode, the worker's file tools write under the working directory instead, so this path does not apply.

## Before you begin

You need:

* **An existing agent.** If you don't have one, complete the [Quickstart](/docs/en/managed-agents/quickstart) first and note its agent ID.
* **A Linux host** with `/bin/bash` at that exact path. The TypeScript SDK additionally requires `unzip`, `tar`, and Node.js 22 or later; the Python SDK uses the standard library for archive extraction and has no additional binary requirements. These dependencies are resolved at fixed paths and do not respect `PATH` overrides.
* **The `ant` CLI or an Anthropic SDK** (Python, TypeScript, or Go) on the worker host.
* **Two credentials:** an environment key (generated in the steps that follow) authenticates the worker to its queue; your Claude API key creates sessions and reads queue stats from outside the worker host.

<Note>
  On [Claude Platform on AWS](/docs/en/build-with-claude/claude-platform-on-aws), the worker authenticates with AWS IAM (SigV4) or an [API key generated in the AWS Console](/docs/en/build-with-claude/claude-platform-on-aws#api-key-authentication), not an environment key. Attach the [`AnthropicSelfHostedEnvironmentAccess`](/docs/en/api/claude-platform-on-aws-iam-actions#managed-policies) managed policy to the IAM principal your worker runs as. Environment keys generated in the Claude Console don't work with the Claude Platform on AWS endpoint.
</Note>

<Steps>
  <Step title="Create a self-hosted environment">
    In the [Console](https://platform.claude.com/workspaces/default/environments): **Workspace > Environments > New > Self-hosted**

    Or through the API:

    <CodeGroup>
      ```bash cURL
      curl -sS --fail-with-body https://api.anthropic.com/v1/environments \
        -H "x-api-key: $ANTHROPIC_API_KEY" \
        -H "anthropic-version: 2023-06-01" \
        -H "anthropic-beta: managed-agents-2026-04-01" \
        -H "content-type: application/json" \
        -d '{
          "name": "self-hosted",
          "config": {"type": "self_hosted"}
        }'
      ```

      ```bash CLI
      ant beta:environments create \
        --name self-hosted \
        --config '{"type": "self_hosted"}'
      ```

      ```python Python
      client = anthropic.Anthropic()

      environment = client.beta.environments.create(
          name="self-hosted", config={"type": "self_hosted"}
      )
      print(environment.id)
      ```

      ```typescript TypeScript
      const client = new Anthropic();

      const environment = await client.beta.environments.create({
        name: "self-hosted",
        config: { type: "self_hosted" }
      });
      console.log(environment.id);
      ```

      ```csharp C#
      using Anthropic.Models.Beta.Environments;

      var client = new AnthropicClient();

      var environment = await client.Beta.Environments.Create(
          new EnvironmentCreateParams
          {
              Name = "self-hosted",
              Config = new BetaSelfHostedConfigParams(),
          }
      );
      Console.WriteLine(environment.ID);
      ```

      ```go Go
      client := anthropic.NewClient()

      environment, err := client.Beta.Environments.New(context.Background(), anthropic.BetaEnvironmentNewParams{
      	Name: "self-hosted",
      	Config: anthropic.BetaEnvironmentNewParamsConfigUnion{
      		OfSelfHosted: &anthropic.BetaSelfHostedConfigParams{},
      	},
      })
      if err != nil {
      	panic(err)
      }
      fmt.Println(environment.ID)
      ```

      ```java Java
      import com.anthropic.models.beta.environments.BetaSelfHostedConfigParams;
      import com.anthropic.models.beta.environments.EnvironmentCreateParams;

      void main() {
          var client = AnthropicOkHttpClient.fromEnv();

          var environment = client.beta().environments().create(
              EnvironmentCreateParams.builder()
                  .name("self-hosted")
                  .config(BetaSelfHostedConfigParams.builder().build())
                  .build()
          );
          IO.println(environment.id());
      }
      ```

      ```php PHP
      $client = new Anthropic\Client();

      $environment = $client->beta->environments->create(
          name: 'self-hosted',
          config: ['type' => 'self_hosted'],
      );
      echo $environment->id, PHP_EOL;
      ```

      ```ruby Ruby
      client = Anthropic::Client.new

      environment = client.beta.environments.create(
        name: "self-hosted",
        config: {type: :self_hosted}
      )
      puts environment.id
      ```
    </CodeGroup>
  </Step>

  <Step title="Generate an environment key">
    In the Console, open the environment and click **Generate environment key**. Key generation is Console-only, regardless of whether you created the environment through the Console or the API. Then export the environment ID and key on the worker host:

    ```bash
    export ANTHROPIC_ENVIRONMENT_KEY="sk-ant-oat01-..."
    export ANTHROPIC_ENVIRONMENT_ID="env_..."
    ```
  </Step>
</Steps>

<Note>
  Skills can include executables that the agent may run directly. The CLI and SDK workers automatically mark downloaded skill files as executable in the sandbox. If you implement skills download manually, you are responsible for setting executable permissions.
</Note>

## Run a worker

Choose **always-on** for the simplest setup: a long-running process polls the queue continuously and needs only outbound HTTPS. Choose **webhook-triggered** to avoid running an idle poller; it requires a webhook endpoint that Anthropic can reach (see [Webhooks](/docs/en/managed-agents/webhooks) for endpoint setup and signature verification).

<Tabs>
  <Tab title="Always-on (ant CLI)">
    <Steps>
      <Step title="Install the ant CLI">
        Run this on the worker host.

        ```bash
        VERSION=1.12.0
        OS=$(uname -s | tr '[:upper:]' '[:lower:]')
        case $(uname -m) in
          x86_64) ARCH=amd64 ;;
          aarch64) ARCH=arm64 ;;
        esac
        curl -fsSL "https://github.com/anthropics/anthropic-cli/releases/download/v${VERSION}/ant_${VERSION}_${OS}_${ARCH}.tar.gz" \
          | sudo tar -xz -C /usr/local/bin ant
        ```
      </Step>

      <Step title="Run the worker">
        **In-process**

        `ant beta:worker poll` claims work items assigned to the environment, downloads skills, executes tool calls in the working directory, and posts results back.

        ```bash
        ant beta:worker poll \
          --workdir "/workspace"
        ```

        The worker exits cleanly on SIGTERM or SIGINT, draining in-flight tool calls before stopping.

        **Sandbox per session**

        If you need stronger isolation (a fresh filesystem, resource limits, or per-session network controls), run each session in its own sandbox. Build an image with `ant` installed and `ant beta:worker run` as the entrypoint. The base image must provide `/bin/bash`; `curl` is only used at build time. When a sandbox starts, it reads session details from environment variables, handles that session, and exits:

        ```text
        FROM your-base-image
        ARG ANT_VERSION=1.12.0
        ARG TARGETARCH
        RUN ARCH=$([ "$TARGETARCH" = "arm64" ] && echo arm64 || echo amd64) && \
            curl -fsSL "https://github.com/anthropics/anthropic-cli/releases/download/v${ANT_VERSION}/ant_${ANT_VERSION}_linux_${ARCH}.tar.gz" \
              | tar -xz -C /usr/local/bin ant
        WORKDIR /workspace
        VOLUME /mnt/session/outputs
        ENTRYPOINT ["ant", "beta:worker", "run"]
        ```

        Then write a spawn script that forwards session details into a fresh sandbox. The poller injects `ANTHROPIC_SESSION_ID`, `ANTHROPIC_WORK_ID`, `ANTHROPIC_ENVIRONMENT_ID`, and `ANTHROPIC_ENVIRONMENT_KEY` into the script's environment. `ANTHROPIC_BASE_URL` is optional and is passed through only if it was set on the poller host; it overrides the default API endpoint. In the example, `/host/outputs` is a host directory you choose; it is bind-mounted to the sandbox's `/mnt/session/outputs` so you can retrieve session deliverables after the sandbox exits.

        ```bash
        #!/bin/bash
        # spawn.sh: called once per session
        mkdir -p "/host/outputs/$ANTHROPIC_SESSION_ID"
        exec docker run --rm \
          -e ANTHROPIC_SESSION_ID -e ANTHROPIC_ENVIRONMENT_KEY \
          -e ANTHROPIC_WORK_ID -e ANTHROPIC_ENVIRONMENT_ID -e ANTHROPIC_BASE_URL \
          -v "/host/outputs/$ANTHROPIC_SESSION_ID":/mnt/session/outputs \
          your-image
        ```

        Start the poller pointing at the script:

        ```bash
        ant beta:worker poll \
          --on-work ./spawn.sh
        ```
      </Step>
    </Steps>
  </Tab>

  <Tab title="Always-on (SDK)">
    <Steps>
      <Step title="Run the worker">
        `EnvironmentWorker` claims work items assigned to the environment, downloads skills, executes tool calls in the working directory, and posts results back. Authenticate with the environment key you generated in [Before you begin](#before-you-begin).

        <CodeGroup>
          ```python Python
          import asyncio
          import os
          from anthropic import AsyncAnthropic
          from anthropic.lib.environments import EnvironmentWorker


          async def main() -> None:
              environment_key = os.environ["ANTHROPIC_ENVIRONMENT_KEY"]
              environment_id = os.environ["ANTHROPIC_ENVIRONMENT_ID"]
              async with AsyncAnthropic(auth_token=environment_key) as client:
                  await EnvironmentWorker(
                      client,
                      environment_id=environment_id,
                      environment_key=environment_key,
                      workdir="/workspace",
                  ).run()


          asyncio.run(main())
          ```

          ```typescript TypeScript
          import Anthropic from "@anthropic-ai/sdk";
          import { EnvironmentWorker } from "@anthropic-ai/sdk/helpers/beta/environments";

          const environmentKey = process.env.ANTHROPIC_ENVIRONMENT_KEY!;
          const environmentId = process.env.ANTHROPIC_ENVIRONMENT_ID!;
          const client = new Anthropic({ authToken: environmentKey });
          const controller = new AbortController();
          process.once("SIGTERM", () => controller.abort());

          await new EnvironmentWorker({
            client,
            environmentId,
            environmentKey,
            workdir: "/workspace",
            signal: controller.signal
          }).run();
          ```

          ```csharp C#
          // EnvironmentWorker is not currently available in the C# SDK. See the Always-on (ant CLI) tab.
          ```

          ```go Go
          package main

          import (
          	"context"
          	"log"
          	"os"
          	"os/signal"
          	"syscall"

          	"github.com/anthropics/anthropic-sdk-go"
          	"github.com/anthropics/anthropic-sdk-go/lib/environments"
          	"github.com/anthropics/anthropic-sdk-go/option"
          )

          func main() {
          	environmentKey := os.Getenv("ANTHROPIC_ENVIRONMENT_KEY")
          	environmentID := os.Getenv("ANTHROPIC_ENVIRONMENT_ID")

          	ctx, stop := signal.NotifyContext(context.Background(), os.Interrupt, syscall.SIGTERM)
          	defer stop()

          	client := anthropic.NewClient(option.WithAuthToken(environmentKey))

          	worker := environments.NewEnvironmentWorker(client, environments.EnvironmentWorkerOptions{
          		EnvironmentID:  environmentID,
          		EnvironmentKey: environmentKey,
          		Workdir:        "/workspace",
          	})
          	if err := worker.Run(ctx); err != nil {
          		log.Fatalf("worker: %v", err)
          	}
          }

          ```

          ```java Java
          // EnvironmentWorker is not currently available in the Java SDK. See the Always-on (ant CLI) tab.
          ```

          ```php PHP
          // EnvironmentWorker is not currently available in the PHP SDK. See the Always-on (ant CLI) tab.
          ```

          ```ruby Ruby
          # EnvironmentWorker is not currently available in the Ruby SDK. See the Always-on (ant CLI) tab.
          ```
        </CodeGroup>
      </Step>
    </Steps>
  </Tab>

  <Tab title="Webhook-triggered (SDK)">
    <Steps>
      <Step title="Subscribe to session webhooks">
        In the [Console](https://platform.claude.com/settings/workspaces/default/webhooks), define a webhook endpoint that listens for `session.status_run_started` events. See [Webhooks](/docs/en/managed-agents/webhooks) for details.
      </Step>

      <Step title="Export the webhook signing key">
        In addition to the environment ID and key from [Before you begin](#before-you-begin), export the webhook signing key on your handler host so the handler can verify incoming payloads:

        ```bash
        export ANTHROPIC_WEBHOOK_SIGNING_KEY="whsec_..."
        ```
      </Step>

      <Step title="Implement the webhook handler">
        `EnvironmentWorker` claims the work item, downloads skills, executes tool calls in the working directory, posts results back, and exits. Invoke it when `session.status_run_started` fires.

        <CodeGroup>
          ```python Python
          import os
          import anthropic

          environment_key = os.environ["ANTHROPIC_ENVIRONMENT_KEY"]
          environment_id = os.environ["ANTHROPIC_ENVIRONMENT_ID"]
          client = anthropic.AsyncAnthropic(
              auth_token=environment_key,
          )


          async def handle(raw: bytes, headers: dict[str, str]) -> dict:
              event = client.beta.webhooks.unwrap(raw.decode(), headers=headers)
              if event.data.type != "session.status_run_started":
                  return {"status": "ignored"}
              async for work in client.beta.environments.work.poller(
                  environment_id=environment_id,
                  environment_key=environment_key,
                  block_ms=None,
                  reclaim_older_than_ms=2000,
                  drain=True,
                  auto_stop=False,
              ):
                  await client.beta.environments.work.worker(workdir="/workspace").handle_item(
                      work_id=work.id,
                      environment_id=environment_id,
                      session_id=work.data.id,
                      environment_key=environment_key,
                  )
              return {"status": "ok"}
          ```

          ```typescript TypeScript
          import Anthropic from "@anthropic-ai/sdk";

          const environmentKey = process.env.ANTHROPIC_ENVIRONMENT_KEY!;
          const environmentId = process.env.ANTHROPIC_ENVIRONMENT_ID!;
          const client = new Anthropic({
            authToken: environmentKey
          });

          export async function handle(req: Request): Promise<Response> {
            const body = await req.text();
            let event;
            try {
              event = client.beta.webhooks.unwrap(body, { headers: Object.fromEntries(req.headers) });
            } catch {
              return new Response("signature verification failed", { status: 401 });
            }
            if (event.data.type !== "session.status_run_started") {
              return Response.json({ status: "ignored" });
            }

            for await (const work of client.beta.environments.work.poller({
              environmentId,
              environmentKey,
              blockMs: null,
              reclaimOlderThanMs: 2000,
              drain: true,
              autoStop: false
            })) {
              await client.beta.environments.work.worker({ workdir: "/workspace" }).handleItem({
                workId: work.id,
                environmentId,
                sessionId: work.data.id,
                environmentKey
              });
            }
            return Response.json({ status: "ok" });
          }
          ```

          ```csharp C#
          // EnvironmentWorker is not currently available in the C# SDK.
          // To handle work items directly, see the Environments Work endpoints.
          ```

          ```go Go
          package main

          import (
          	"context"
          	"encoding/json"
          	"io"
          	"log/slog"
          	"net/http"
          	"os"

          	"github.com/anthropics/anthropic-sdk-go"
          	"github.com/anthropics/anthropic-sdk-go/lib/environments"
          	"github.com/anthropics/anthropic-sdk-go/option"
          	"github.com/anthropics/anthropic-sdk-go/packages/param"
          )

          var (
          	environmentKey = os.Getenv("ANTHROPIC_ENVIRONMENT_KEY")
          	environmentID  = os.Getenv("ANTHROPIC_ENVIRONMENT_ID")
          	client         = anthropic.NewClient(
          		option.WithAuthToken(environmentKey),
          		option.WithWebhookKey(os.Getenv("ANTHROPIC_WEBHOOK_SIGNING_KEY")),
          	)
          	worker = environments.NewEnvironmentWorker(client, environments.EnvironmentWorkerOptions{
          		Workdir: "/workspace",
          	})
          )

          func handle(w http.ResponseWriter, r *http.Request) {
          	body, err := io.ReadAll(r.Body)
          	if err != nil {
          		http.Error(w, "bad request", http.StatusBadRequest)
          		return
          	}
          	event, err := client.Beta.Webhooks.Unwrap(body, r.Header)
          	if err != nil {
          		http.Error(w, "signature verification failed", http.StatusUnauthorized)
          		return
          	}
          	if event.Data.Type != "session.status_run_started" {
          		json.NewEncoder(w).Encode(map[string]string{"status": "ignored"})
          		return
          	}

          	// The Go SDK does not provide a RunOne convenience: drain pending items
          	// with WorkPoller and run each one with HandleItem.
          	// Detach from r.Context(): the session can outlive the webhook delivery timeout.
          	ctx := context.Background()
          	poller := environments.NewWorkPoller(ctx, client, environments.WorkPollerOptions{
          		EnvironmentID:      environmentID,
          		EnvironmentKey:     environmentKey,
          		BlockMs:            param.Null[int64](),
          		ReclaimOlderThanMs: param.NewOpt[int64](2000),
          		Drain:              true,
          	})
          	defer poller.Close()
          	for poller.Next() {
          		item := poller.Current()
          		if err := worker.HandleItem(ctx, environments.HandleItemOptions{
          			WorkID:         item.ID,
          			EnvironmentID:  item.EnvironmentID,
          			SessionID:      item.Data.ID,
          			EnvironmentKey: environmentKey,
          		}); err != nil {
          			slog.Error("handle work item", "work_id", item.ID, "err", err)
          			http.Error(w, "internal error", http.StatusInternalServerError)
          			return
          		}
          	}
          	if err := poller.Err(); err != nil {
          		slog.Error("poll work queue", "err", err)
          		http.Error(w, "internal error", http.StatusInternalServerError)
          		return
          	}
          	json.NewEncoder(w).Encode(map[string]string{"status": "ok"})
          }

          func main() {
          	http.HandleFunc("POST /webhook", handle)
          	if err := http.ListenAndServe(":8080", nil); err != nil {
          		slog.Error("http server", "err", err)
          		os.Exit(1)
          	}
          }

          ```

          ```java Java
          // EnvironmentWorker is not currently available in the Java SDK.
          // To handle work items directly, see the Environments Work endpoints.
          ```

          ```php PHP
          // EnvironmentWorker is not currently available in the PHP SDK.
          // To handle work items directly, see the Environments Work endpoints.
          ```

          ```ruby Ruby
          # EnvironmentWorker is not currently available in the Ruby SDK.
          # To handle work items directly, see the Environments Work endpoints.
          ```
        </CodeGroup>
      </Step>
    </Steps>
  </Tab>
</Tabs>

### SDK helpers

The SDK provides three helpers at different levels of control. `EnvironmentWorker` covers most use cases; drop to the lower-level helpers when you need to launch your own per-session process or run tools against an already-claimed session.

* **`EnvironmentWorker`:** the out-of-the-box worker. Handles polling, setup, and execution end to end.

  * `.run()`: runs indefinitely, picking up sessions as they arrive. Exits cleanly on SIGTERM.
  * `.handle_item()`: picks up one pending session, handles it, and exits.

* **`work.poller()`:** polls the work queue on your behalf and gives you each claimed session. Use this when you want to decide what happens for each session, for example launching a sandbox rather than running tools in-process.

  * `drain`: whether to stop polling once the queue is empty rather than waiting for new work.
  * `block_ms`: how long to wait for work to arrive before returning, in milliseconds. Must be between 1 and 999 (per-poll wait; the helper re-polls automatically). Pass `null` (`None` in Python, `param.Null[int64]()` in Go) for a non-blocking check; omitting the parameter uses the default 999 ms long-poll.
  * `reclaim_older_than_ms`: re-claim work items leased to a worker that has stopped responding.
  * `auto_stop`: whether to post a stop signal on the work item after the iterator exits. The Go poller has no opt-out and always posts the stop signal, so block in the loop body until the session completes rather than detaching.

* **`client.beta.sessions.events.tool_runner()`:** runs tool calls for a single session, given the session ID and a tool list. Use when you've already claimed the work and only need the execution layer.

Use the work poller directly when you want to launch your own per-session process, for example spinning up a sandbox for each claimed session:

<CodeGroup>
  ```bash cURL
  # The work poller is an SDK helper (Python, TypeScript, Go), not a raw
  # endpoint. From the shell, use `ant beta:worker poll --on-work` instead;
  # see the Always-on (ant CLI) tab.
  ```

  ```bash CLI
  # The work poller is an SDK helper (Python, TypeScript, Go), not a raw
  # endpoint. From the shell, use `ant beta:worker poll --on-work` instead;
  # see the Always-on (ant CLI) tab.
  ```

  ```python Python
  import asyncio
  import os

  from anthropic import AsyncAnthropic
  from anthropic.types.beta.environments import BetaSelfHostedWork


  async def launch_container(work: BetaSelfHostedWork) -> None:
      # Replace with your own per-session sandbox launcher. Pass
      # ANTHROPIC_ENVIRONMENT_KEY into the launched sandbox, never
      # your API key.
      print(f"claimed session {work.data.id}")


  async def main() -> None:
      environment_key = os.environ["ANTHROPIC_ENVIRONMENT_KEY"]
      environment_id = os.environ["ANTHROPIC_ENVIRONMENT_ID"]
      async with AsyncAnthropic(auth_token=environment_key) as client:
          async for work in client.beta.environments.work.poller(
              environment_id=environment_id,
              environment_key=environment_key,
              auto_stop=False,  # the launched sandbox owns the stop call
          ):
              await launch_container(work)


  asyncio.run(main())
  ```

  ```typescript TypeScript
  import Anthropic from "@anthropic-ai/sdk";
  import { WorkPoller } from "@anthropic-ai/sdk/helpers/beta/environments";
  import type { BetaSelfHostedWork } from "@anthropic-ai/sdk/resources/beta/environments";

  const environmentKey = process.env.ANTHROPIC_ENVIRONMENT_KEY!;
  const environmentId = process.env.ANTHROPIC_ENVIRONMENT_ID!;
  const client = new Anthropic({ authToken: environmentKey });

  async function launchContainer(work: BetaSelfHostedWork): Promise<void> {
    // Replace with your own per-session sandbox launcher. Pass
    // ANTHROPIC_ENVIRONMENT_KEY into the launched sandbox, never
    // your API key.
    console.log(`claimed session ${work.data.id}`);
  }

  const poller = new WorkPoller({
    client,
    environmentId,
    environmentKey,
    autoStop: false // the launched sandbox owns the stop call
  });

  for await (const work of poller) {
    await launchContainer(work);
  }
  ```

  ```csharp C#
  // Work polling is not currently available in the C# SDK.
  // From the shell, use `ant beta:worker poll --on-work` instead.
  ```

  ```go Go
  package main

  import (
  	"context"
  	"fmt"
  	"log"
  	"os"

  	"github.com/anthropics/anthropic-sdk-go"
  	"github.com/anthropics/anthropic-sdk-go/lib/environments"
  	"github.com/anthropics/anthropic-sdk-go/option"
  )

  func launchContainer(work *anthropic.BetaSelfHostedWork) {
  	// Replace with your own per-session sandbox launcher. The Go poller
  	// calls work.Stop when this function returns (it has no auto-stop
  	// opt-out), so block here until the session completes rather than
  	// detaching as the Python and TypeScript tabs do.
  	fmt.Printf("claimed session %s\n", work.Data.ID)
  }

  func main() {
  	environmentID := os.Getenv("ANTHROPIC_ENVIRONMENT_ID")
  	environmentKey := os.Getenv("ANTHROPIC_ENVIRONMENT_KEY")

  	client := anthropic.NewClient(option.WithAuthToken(environmentKey))

  	ctx := context.Background()

  	poller := environments.NewWorkPoller(ctx, client, environments.WorkPollerOptions{
  		EnvironmentID:  environmentID,
  		EnvironmentKey: environmentKey,
  	})
  	defer poller.Close()

  	for work, err := range poller.All() {
  		if err != nil {
  			log.Fatal(err)
  		}
  		launchContainer(work)
  	}
  }
  ```

  ```java Java
  // Work polling is not currently available in the Java SDK.
  // From the shell, use `ant beta:worker poll --on-work` instead.
  ```

  ```php PHP
  // Work polling is not currently available in the PHP SDK.
  // From the shell, use `ant beta:worker poll --on-work` instead.
  ```

  ```ruby Ruby
  # Work polling is not currently available in the Ruby SDK.
  # From the shell, use `ant beta:worker poll --on-work` instead.
  ```
</CodeGroup>

**`AgentToolContext`** is the execution context for tool calls. It defines the working directory and path policy, and optionally downloads the session's skills when used as a context manager. **`beta_agent_toolset_20260401(env)`** takes an `AgentToolContext` and returns the standard tool implementations (`bash`, `read`, `write`, `edit`, `glob`, `grep`).

**With `EnvironmentWorker`:** both are managed automatically. Pass a `tools` factory to customize the tool list:

```python Python
EnvironmentWorker(client, ..., tools=lambda env: [beta_bash_tool(env), my_custom_tool])
```

**With `work.poller()` and `tool_runner()`:** pass a tool list as `tools` to `client.beta.sessions.events.tool_runner()`. To build that list, set up `AgentToolContext` yourself and call `beta_agent_toolset_20260401(env)`:

<CodeGroup>
  ```python Python
  from anthropic.lib.tools.agent_toolset import (
      AgentToolContext,
      beta_agent_toolset_20260401,
  )

  async with AgentToolContext(
      workdir="/workspace", client=client, session_id=work.data.id
  ) as env:
      # skills downloaded to /workspace/skills/<name>/
      tools = beta_agent_toolset_20260401(env)
  ```

  ```typescript TypeScript
  import {
    setupSkills,
    betaAgentToolset20260401
  } from "@anthropic-ai/sdk/tools/agent-toolset/node";

  const ctx = { workdir: "/workspace", client, sessionId: work.data.id };
  await setupSkills(ctx);
  const tools = betaAgentToolset20260401(ctx);
  ```

  ```csharp C#
  // AgentToolContext is not currently available in the C# SDK.
  ```

  ```go Go
  env := &agenttoolset.AgentToolContext{Workdir: "/workspace"}
  if err := env.SetupSkills(ctx, client, work.Data.ID); err != nil {
  	panic(err)
  }
  // skills downloaded to /workspace/skills/<name>/
  tools := agenttoolset.BetaAgentToolset20260401(env)
  ```

  ```java Java
  // AgentToolContext is not currently available in the Java SDK.
  ```

  ```php PHP
  // AgentToolContext is not currently available in the PHP SDK.
  ```

  ```ruby Ruby
  # AgentToolContext is not currently available in the Ruby SDK.
  ```
</CodeGroup>

### Verify the worker is connected

From a separate shell, using your Claude API key (not the environment key), confirm `workers_polling` is at least 1:

```bash
ant beta:environments:work stats --environment-id "$ANTHROPIC_ENVIRONMENT_ID"
```

If `workers_polling` stays at 0, the worker isn't reaching the queue: confirm `ANTHROPIC_ENVIRONMENT_KEY` and `ANTHROPIC_ENVIRONMENT_ID` are set on the worker host. See [Read queue depth](#read-queue-depth) for the full stats response and other language examples.

## Start a session

Once your worker is running, create a session that targets the environment. The session enters the environment's work queue and waits there until a worker claims it; if no worker is connected, the session stays queued rather than failing.

Anthropic doesn't mount files or GitHub repositories into self-hosted sandboxes. To make session-specific files available, pass file references (such as an S3 path or commit SHA) in the session `metadata` field. Your spawn script or `--on-work` handler reads that metadata from the claimed work item (through the [Environments Work endpoints](/docs/en/api/beta/environments/work)) and stages the files into the working directory before tool execution begins.

<CodeGroup>
  ```bash cURL
  curl -sS --fail-with-body https://api.anthropic.com/v1/sessions \
    -H "x-api-key: $ANTHROPIC_API_KEY" \
    -H "anthropic-version: 2023-06-01" \
    -H "anthropic-beta: managed-agents-2026-04-01" \
    -H "content-type: application/json" \
    -d @- <<EOF
  {
    "agent": "$AGENT_ID",
    "environment_id": "$ANTHROPIC_ENVIRONMENT_ID",
    "metadata": {"input_file": "s3://my-bucket/data.csv"}
  }
  EOF
  ```

  ```bash CLI
  ant beta:sessions create \
    --agent "$AGENT_ID" \
    --environment-id "$ANTHROPIC_ENVIRONMENT_ID" \
    --metadata '{"input_file": "s3://my-bucket/data.csv"}'
  ```

  ```python Python
  session = client.beta.sessions.create(
      agent=agent.id,
      environment_id=environment.id,
      metadata={"input_file": "s3://my-bucket/data.csv"},
  )
  ```

  ```typescript TypeScript
  const session = await client.beta.sessions.create({
    agent: agent.id,
    environment_id: environment.id,
    metadata: { input_file: "s3://my-bucket/data.csv" }
  });
  ```

  ```csharp C#
  var session = await client.Beta.Sessions.Create(new()
  {
      Agent = agent.ID,
      EnvironmentID = environment.ID,
      Metadata = new Dictionary<string, string> { ["input_file"] = "s3://my-bucket/data.csv" },
  });
  ```

  ```go Go
  session, err := client.Beta.Sessions.New(ctx, anthropic.BetaSessionNewParams{
  	Agent:         anthropic.BetaSessionNewParamsAgentUnion{OfString: anthropic.String(agent.ID)},
  	EnvironmentID: environment.ID,
  	Metadata: map[string]string{
  		"input_file": "s3://my-bucket/data.csv",
  	},
  })
  if err != nil {
  	panic(err)
  }
  ```

  ```java Java
  var session = client.beta().sessions().create(SessionCreateParams.builder()
      .agent(agent.id())
      .environmentId(environment.id())
      .metadata(SessionCreateParams.Metadata.builder()
          .putAdditionalProperty("input_file", JsonValue.from("s3://my-bucket/data.csv"))
          .build())
      .build());
  ```

  ```php PHP
  $session = $client->beta->sessions->create(
      agent: $agent->id,
      environmentID: $environment->id,
      metadata: ['input_file' => 's3://my-bucket/data.csv'],
  );
  ```

  ```ruby Ruby
  session = client.beta.sessions.create(
    agent: agent.id,
    environment_id: environment.id,
    metadata: {input_file: "s3://my-bucket/data.csv"}
  )
  ```
</CodeGroup>

<Note>
  [Memory](/docs/en/managed-agents/memory) is not currently supported with self-hosted sandboxes.
</Note>

See [Self-hosted worker](/docs/en/managed-agents/reference#self-hosted-worker) in the reference for the full list of CLI flags, and [SDK helpers](#sdk-helpers) for the SDK helper options.

## Monitoring and operations

These calls run from your monitoring or operations tooling, authenticated with your Claude API key, to observe and manage the worker fleet. The claim and keep-alive loop is handled inside the worker helpers, so you don't call those endpoints directly.

<Warning>
  These endpoints authenticate with your organization API key, not the environment key. Call them from outside the worker host. Setting `ANTHROPIC_API_KEY` on the worker host exposes an organization-scoped credential to agent tool calls.
</Warning>

### Read queue depth

`work.stats` returns the queue state for an environment:

* `depth` is the number of items waiting to be claimed. Scale your worker fleet or alert on backlog based on this value.
* `pending` is the number of items a worker has claimed and is currently processing.
* `oldest_queued_at` is the timestamp of the oldest item in the queue, or `null` if the queue is empty.
* `workers_polling` is the number of workers that have polled in the last 30 seconds. Use this for liveness alerting.

<CodeGroup>
  ```bash cURL
  curl -sS "https://api.anthropic.com/v1/environments/$ANTHROPIC_ENVIRONMENT_ID/work/stats" \
    -H "x-api-key: $ANTHROPIC_API_KEY" \
    -H "anthropic-beta: managed-agents-2026-04-01" \
    -H "anthropic-version: 2023-06-01"
  ```

  ```bash CLI
  ant beta:environments:work stats --environment-id "$ANTHROPIC_ENVIRONMENT_ID"
  ```

  ```python Python
  import os

  import anthropic

  client = anthropic.Anthropic()

  stats = client.beta.environments.work.stats(os.environ["ANTHROPIC_ENVIRONMENT_ID"])
  print(f"depth={stats.depth} pending={stats.pending}")
  ```

  ```typescript TypeScript
  import Anthropic from "@anthropic-ai/sdk";

  const client = new Anthropic();

  const stats = await client.beta.environments.work.stats(process.env.ANTHROPIC_ENVIRONMENT_ID!);

  console.log(`depth=${stats.depth} pending=${stats.pending}`);
  ```

  ```csharp C#
  using Anthropic;

  var client = new AnthropicClient();

  var environmentId = Environment.GetEnvironmentVariable("ANTHROPIC_ENVIRONMENT_ID")!;

  var stats = await client.Beta.Environments.Work.Stats(environmentId);

  Console.WriteLine($"depth={stats.Depth} pending={stats.Pending}");
  ```

  ```go Go
  package main

  import (
  	"context"
  	"fmt"
  	"os"

  	"github.com/anthropics/anthropic-sdk-go"
  )

  func main() {
  	client := anthropic.NewClient()
  	environmentID := os.Getenv("ANTHROPIC_ENVIRONMENT_ID")

  	stats, err := client.Beta.Environments.Work.Stats(
  		context.Background(),
  		environmentID,
  		anthropic.BetaEnvironmentWorkStatsParams{},
  	)
  	if err != nil {
  		panic(err)
  	}

  	fmt.Printf("depth=%d pending=%d\n", stats.Depth, stats.Pending)
  }
  ```

  ```java Java
  import com.anthropic.client.AnthropicClient;
  import com.anthropic.client.okhttp.AnthropicOkHttpClient;
  import com.anthropic.models.beta.environments.work.BetaSelfHostedWorkQueueStats;

  void main() {
      AnthropicClient client = AnthropicOkHttpClient.fromEnv();

      BetaSelfHostedWorkQueueStats stats = client.beta()
          .environments()
          .work()
          .stats(System.getenv("ANTHROPIC_ENVIRONMENT_ID"));

      IO.println("depth=" + stats.depth() + " pending=" + stats.pending());
  }
  ```

  ```php PHP
  <?php

  use Anthropic\Client;

  $client = new Client();

  $stats = $client->beta->environments->work->stats(getenv('ANTHROPIC_ENVIRONMENT_ID'));

  printf("depth=%d pending=%d\n", $stats->depth, $stats->pending);
  ```

  ```ruby Ruby
  require "anthropic"

  client = Anthropic::Client.new

  stats = client.beta.environments.work.stats(ENV.fetch("ANTHROPIC_ENVIRONMENT_ID"))

  puts "depth=#{stats.depth} pending=#{stats.pending}"
  ```
</CodeGroup>

```text wrap
{
  "type": "work_queue_stats",
  "depth": 0,
  "pending": 0,
  "oldest_queued_at": null,
  "workers_polling": 0
}
```

### Stop a session gracefully

Use `work.stop` to ask the worker handling a specific session to shut it down cleanly. The worker finishes any in-flight tool call, posts a final status, and releases the session. Pass `force: true` in the request body to interrupt immediately instead of waiting for the current tool call to complete.

Because these calls run from your operations tooling rather than the worker host, `ANTHROPIC_WORK_ID` isn't set automatically. Set it to the target work item's ID before running the following examples.

<CodeGroup>
  ```bash cURL
  curl -sS "https://api.anthropic.com/v1/environments/$ANTHROPIC_ENVIRONMENT_ID/work/$ANTHROPIC_WORK_ID/stop" \
    -H "x-api-key: $ANTHROPIC_API_KEY" \
    -H "anthropic-beta: managed-agents-2026-04-01" \
    -H "anthropic-version: 2023-06-01" \
    -H "content-type: application/json" \
    -d '{}'
  ```

  ```bash CLI
  ant beta:environments:work stop \
    --environment-id "$ANTHROPIC_ENVIRONMENT_ID" \
    --work-id "$ANTHROPIC_WORK_ID"
  ```

  ```python Python
  import os

  import anthropic

  client = anthropic.Anthropic()

  work = client.beta.environments.work.stop(
      os.environ["ANTHROPIC_WORK_ID"],
      environment_id=os.environ["ANTHROPIC_ENVIRONMENT_ID"],
  )
  print(work.state)
  ```

  ```typescript TypeScript
  import Anthropic from "@anthropic-ai/sdk";

  const client = new Anthropic();

  const work = await client.beta.environments.work.stop(process.env.ANTHROPIC_WORK_ID!, {
    environment_id: process.env.ANTHROPIC_ENVIRONMENT_ID!
  });

  console.log(work.state);
  ```

  ```csharp C#
  using Anthropic;

  var client = new AnthropicClient();

  var work = await client.Beta.Environments.Work.Stop(
      Environment.GetEnvironmentVariable("ANTHROPIC_WORK_ID")!,
      new()
      {
          EnvironmentID = Environment.GetEnvironmentVariable("ANTHROPIC_ENVIRONMENT_ID")!
      }
  );

  Console.WriteLine(work.State);
  ```

  ```go Go
  package main

  import (
  	"context"
  	"fmt"
  	"os"

  	"github.com/anthropics/anthropic-sdk-go"
  )

  func main() {
  	client := anthropic.NewClient()

  	work, err := client.Beta.Environments.Work.Stop(
  		context.Background(),
  		os.Getenv("ANTHROPIC_WORK_ID"),
  		anthropic.BetaEnvironmentWorkStopParams{
  			EnvironmentID: os.Getenv("ANTHROPIC_ENVIRONMENT_ID"),
  		},
  	)
  	if err != nil {
  		panic(err)
  	}
  	fmt.Println(work.State)
  }
  ```

  ```java Java
  import com.anthropic.client.AnthropicClient;
  import com.anthropic.client.okhttp.AnthropicOkHttpClient;
  import com.anthropic.models.beta.environments.work.BetaSelfHostedWork;
  import com.anthropic.models.beta.environments.work.BetaSelfHostedWorkStopRequest;
  import com.anthropic.models.beta.environments.work.WorkStopParams;

  void main() {
      AnthropicClient client = AnthropicOkHttpClient.fromEnv();

      BetaSelfHostedWork work = client.beta().environments().work().stop(
          WorkStopParams.builder()
              .environmentId(System.getenv("ANTHROPIC_ENVIRONMENT_ID"))
              .workId(System.getenv("ANTHROPIC_WORK_ID"))
              .betaSelfHostedWorkStopRequest(BetaSelfHostedWorkStopRequest.builder().build())
              .build()
      );

      IO.println(work.state());
  }
  ```

  ```php PHP
  <?php

  use Anthropic\Client;

  $client = new Client();

  $work = $client->beta->environments->work->stop(
      getenv('ANTHROPIC_WORK_ID'),
      environmentID: getenv('ANTHROPIC_ENVIRONMENT_ID'),
  );

  echo $work->state . "\n";
  ```

  ```ruby Ruby
  require "anthropic"

  client = Anthropic::Client.new

  work = client.beta.environments.work.stop(
    ENV.fetch("ANTHROPIC_WORK_ID"),
    environment_id: ENV.fetch("ANTHROPIC_ENVIRONMENT_ID")
  )

  puts work.state
  ```
</CodeGroup>

## Next steps

<CardGroup cols={2}>
  <Card title="Managed Agent sessions" icon="settings" href="/docs/en/managed-agents/sessions">
    Create a session to run your agent and begin executing tasks.
  </Card>

  <Card title="MCP tunnels overview" icon="bolt" href="/docs/en/agents-and-tools/mcp-tunnels/overview">
    Reach MCP servers inside your private network from any execution environment.
  </Card>

  <Card title="Security model" icon="lock" href="/docs/en/managed-agents/self-hosted-sandboxes-security">
    Understand the shared responsibility model for self-hosted sandbox environments.
  </Card>
</CardGroup>
