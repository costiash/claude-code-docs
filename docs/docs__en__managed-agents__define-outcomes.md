# Define outcomes

Tell the agent what 'done' looks like, and let it iterate until it gets there.

---

<Tip>
Outcomes is a Research Preview feature. [Request access](https://claude.com/form/claude-managed-agents) to try it.
</Tip>

The `outcome` elevates a session from *conversation* to *work*. You define what the end result should look like and how to measure quality. The agent works toward that target, self-evaluating and iterating until the outcome is met.

When you define an outcome, the harness automatically provisions a *grader* to evaluate the artifact against a rubric. It leverages a separate context window to avoid being influenced by the main agent's implementation choices.

The grader returns a per-criterion breakdown: either confirmation that the artifact satisfies the rubric, or the specific gaps between the current work and the requirements. That feedback is handed back to the agent for the next iteration.

<Note>
All Managed Agents API requests require the `managed-agents-2026-04-01` beta header. Research preview features additionally require `managed-agents-2026-04-01-research-preview`. The SDK sets these beta headers automatically.
</Note>

## Create a rubric

A rubric is a markdown document describing per-criterion scoring. The rubric is required.

<section title="Tips for writing effective rubrics">

Structure the rubric as explicit, gradeable criteria, such as "The CSV contains a price column with numeric values" rather than "The data looks good." The grader scores each criterion independently, so vague criteria produce noisy evaluations.

If you don't have a rubric on hand, try giving Claude an example of a known-good artifact and asking it to analyze what makes that content good, then turn that analysis into a rubric. This middle-ground approach often produces better results than writing criteria from scratch.

</section>

Example rubric:

```markdown
# DCF Model Rubric

## Revenue Projections
- Uses historical revenue data from the last 5 fiscal years
- Projects revenue for at least 5 years forward
- Growth rate assumptions are explicitly stated and reasonable

## Cost Structure
- COGS and operating expenses are modeled separately
- Margins are consistent with historical trends or deviations are justified

## Discount Rate
- WACC is calculated with stated assumptions for cost of equity and cost of debt
- Beta, risk-free rate, and equity risk premium are sourced or justified

## Terminal Value
- Uses either perpetuity growth or exit multiple method (stated which)
- Terminal growth rate does not exceed long-term GDP growth

## Output Quality
- All figures are in a single .xlsx file with clearly labeled sheets
- Key assumptions are on a separate "Assumptions" sheet
- Sensitivity analysis on WACC and terminal growth rate is included
```

Pass the rubric as inline text on `user.define_outcome` (shown in the next section), or upload it via the Files API for reuse across sessions:

**Requires beta header `files-api-2025-04-14`.**

<CodeGroup>
  
  ```bash curl
  rubric=$(curl -fsSL https://api.anthropic.com/v1/files \
    -H "x-api-key: $ANTHROPIC_API_KEY" \
    -H "anthropic-version: 2023-06-01" \
    -H "anthropic-beta: managed-agents-2026-04-01,files-api-2025-04-14" \
    -F file=@/path/to/pr_review_rubric.md)
  rubric_id=$(jq -r '.id' <<<"$rubric")
  printf 'Uploaded rubric: %s\n' "$rubric_id"
  ```
  
  ```bash CLI
  RUBRIC_ID=$(ant beta:files upload \
    --file /path/to/pr_review_rubric.md \
    --transform id --format yaml)
  ```
  ```python Python
  from pathlib import Path

  rubric = client.beta.files.upload(file=Path("/path/to/pr_review_rubric.md"))
  print(f"Uploaded rubric: {rubric.id}")
  ```
  ```typescript TypeScript
  import { readFile } from "node:fs/promises";
  import { toFile } from "@anthropic-ai/sdk";

  const rubric = await client.beta.files.upload({
    file: await toFile(readFile("/path/to/pr_review_rubric.md"), "pr_review_rubric.md")
  });
  console.log(`Uploaded rubric: ${rubric.id}`);
  ```
  ```csharp C#
  var rubric = await client.Beta.Files.Upload(new()
  {
      File = File.OpenRead("/path/to/pr_review_rubric.md"),
  });
  Console.WriteLine($"Uploaded rubric: {rubric.ID}");
  ```
  ```go Go
  f, err := os.Open("/path/to/pr_review_rubric.md")
  if err != nil {
  	panic(err)
  }

  rubric, err := client.Beta.Files.Upload(ctx, anthropic.BetaFileUploadParams{
  	File: anthropic.File(f, "pr_review_rubric.md", "text/markdown"),
  })
  if err != nil {
  	panic(err)
  }
  fmt.Printf("Uploaded rubric: %s\n", rubric.ID)
  ```
  ```java Java
  var rubric = client.beta().files().upload(
      FileUploadParams.builder()
          .file(Path.of("/path/to/pr_review_rubric.md"))
          .build()
  );
  IO.println("Uploaded rubric: " + rubric.id());
  ```
  ```php PHP
  $rubric = $client->beta->files->upload(
      file: fopen('/path/to/pr_review_rubric.md', 'r'),
  );
  echo "Uploaded rubric: {$rubric->id}\n";
  ```
  ```ruby Ruby
  require "pathname"

  rubric = client.beta.files.upload(file: Pathname.new("/path/to/pr_review_rubric.md"))
  puts "Uploaded rubric: #{rubric.id}"
  ```
</CodeGroup>

## Create a session with an outcome

After creating a session, send a `user.define_outcome` event. The agent begins work immediately; no additional user message event is required.

<CodeGroup>
  
  ```bash curl
  # Create a session
  session=$(curl -fsSL https://api.anthropic.com/v1/sessions \
    -H "x-api-key: $ANTHROPIC_API_KEY" \
    -H "anthropic-version: 2023-06-01" \
    -H "anthropic-beta: managed-agents-2026-04-01-research-preview" \
    --json @- <<EOF
  {
    "agent": "$agent_id",
    "environment_id": "$environment_id",
    "title": "Financial analysis on Costco"
  }
  EOF
  )
  session_id=$(jq -r '.id' <<<"$session")

  # Define the outcome — agent starts working on receipt
  curl -fsSL "https://api.anthropic.com/v1/sessions/$session_id/events" \
    -H "x-api-key: $ANTHROPIC_API_KEY" \
    -H "anthropic-version: 2023-06-01" \
    -H "anthropic-beta: managed-agents-2026-04-01-research-preview" \
    --json @- >/dev/null <<EOF
  {
    "events": [
      {
        "type": "user.define_outcome",
        "description": "Build a DCF model for Costco in .xlsx",
        "rubric": {"type": "text", "content": "# DCF Model Rubric\n..."},
        "max_iterations": 5
      }
    ]
  }
  EOF
  # or: "rubric": {"type": "file", "file_id": "$rubric_id"}
  # "max_iterations" is optional; default 3, max 20
  ```
  
  ```bash CLI
  # Create a session
  SESSION_ID=$(ant beta:sessions create \
    --agent "$AGENT_ID" \
    --environment-id "$ENVIRONMENT_ID" \
    --title "Financial analysis on Costco" \
    --transform id --format yaml)

  # Define the outcome — agent starts working on receipt
  ant beta:sessions:events send \
    --session-id "$SESSION_ID" <<YAML
  events:
    - type: user.define_outcome
      description: Build a DCF model for Costco in .xlsx
      rubric: {type: file, file_id: $RUBRIC_ID}
      # or: rubric: {type: text, content: "..."}
      max_iterations: 5  # optional; default 3, max 20
  YAML
  ```
  ```python Python
  # Create a session
  session = client.beta.sessions.create(
      agent=agent.id,
      environment_id=environment.id,
      title="Financial analysis on Costco",
  )

  # Define the outcome — agent starts working on receipt
  client.beta.sessions.events.send(
      session_id=session.id,
      events=[
          {
              "type": "user.define_outcome",
              "description": "Build a DCF model for Costco in .xlsx",
              "rubric": {"type": "text", "content": RUBRIC},
              # or: "rubric": {"type": "file", "file_id": rubric.id},
              "max_iterations": 5,  # optional; default 3, max 20
          }
      ],
  )
  ```
  ```typescript TypeScript
  // Create a session
  const session = await client.beta.sessions.create({
    agent: agent.id,
    environment_id: environment.id,
    title: "Financial analysis on Costco"
  });

  // Define the outcome — agent starts working on receipt
  await client.beta.sessions.events.send(session.id, {
    events: [
      {
        type: "user.define_outcome",
        description: "Build a DCF model for Costco in .xlsx",
        rubric: { type: "text", content: RUBRIC },
        // or: rubric: { type: "file", file_id: rubric.id },
        max_iterations: 5 // optional; default 3, max 20
      }
    ]
  });
  ```
  ```csharp C#
  // Create a session
  var session = await client.Beta.Sessions.Create(new()
  {
      Agent = agent.ID,
      EnvironmentID = environment.ID,
      Title = "Financial analysis on Costco",
  });

  // Define the outcome — agent starts working on receipt
  await client.Beta.Sessions.Events.Send(session.ID, new()
  {
      Events =
      [
          new BetaManagedAgentsUserDefineOutcomeEventParams
          {
              Type = "user.define_outcome",
              Description = "Build a DCF model for Costco in .xlsx",
              Rubric = new BetaManagedAgentsTextRubricParams { Type = "text", Content = Rubric },
              // or: Rubric = new BetaManagedAgentsFileRubricParams { Type = "file", FileID = rubric.id },
              MaxIterations = 5,  // optional; default 3, max 20
          },
      ],
  });
  ```
  ```go Go
  	// Create a session
  	session, err := client.Beta.Sessions.New(ctx, anthropic.BetaSessionNewParams{
  		Agent: anthropic.BetaSessionNewParamsAgentUnion{
  			OfString: anthropic.String(agent.ID),
  		},
  		EnvironmentID: environment.ID,
  		Title:         anthropic.String("Financial analysis on Costco"),
  	})
  	if err != nil {
  		panic(err)
  	}

  	// Define the outcome — agent starts working on receipt
  	_, err = client.Beta.Sessions.Events.Send(ctx, session.ID, anthropic.BetaSessionEventSendParams{
  		Events: []anthropic.SendEventsParamsUnion{{
  			OfUserDefineOutcome: &anthropic.BetaManagedAgentsUserDefineOutcomeEventParams{
  				Description: "Build a DCF model for Costco in .xlsx",
  				Rubric: anthropic.BetaManagedAgentsUserDefineOutcomeEventParamsRubricUnion{
  					OfText: &anthropic.BetaManagedAgentsTextRubricParams{Content: rubric},
  				},
  				// or: OfFile: &anthropic.BetaManagedAgentsFileRubricParams{FileID: rubric.id},
  				MaxIterations: anthropic.Int(5), // optional; default 3, max 20
  			},
  		}},
  	})
  	if err != nil {
  		panic(err)
  	}
  ```
  ```java Java
      // Create a session
      var session = client.beta().sessions().create(
          SessionCreateParams.builder()
              .agent(agent.id())
              .environmentId(environment.id())
              .title("Financial analysis on Costco")
              .build()
      );

      // Define the outcome — agent starts working on receipt
      client.beta().sessions().events().send(
          session.id(),
          EventSendParams.builder()
              .addEvent(
                  BetaManagedAgentsUserDefineOutcomeEventParams.builder()
                      .description("Build a DCF model for Costco in .xlsx")
                      .rubric(BetaTextRubric.builder().content(RUBRIC).build())
                      // or: .rubric(BetaFileRubric.builder().fileId(rubric.id()).build())
                      .maxIterations(5)  // optional; default 3, max 20
                      .build()
              )
              .build()
      );
  ```
  ```php PHP
  // Create a session
  $session = $client->beta->sessions->create(
      agent: $agent->id,
      environmentID: $environment->id,
      title: 'Financial analysis on Costco',
  );

  // Define the outcome — agent starts working on receipt
  $client->beta->sessions->events->send(
      $session->id,
      events: [
          [
              'type' => 'user.define_outcome',
              'description' => 'Build a DCF model for Costco in .xlsx',
              'rubric' => ['type' => 'text', 'content' => $rubric],
              // or: 'rubric' => ['type' => 'file', 'file_id' => $rubric->id],
              'max_iterations' => 5,  // optional; default 3, max 20
          ],
      ],
  );
  ```
  ```ruby Ruby
  # Create a session
  session = client.beta.sessions.create(
    agent: agent.id,
    environment_id: environment.id,
    title: "Financial analysis on Costco"
  )

  # Define the outcome — agent starts working on receipt
  client.beta.sessions.events.send_(
    session.id,
    events: [
      {
        type: "user.define_outcome",
        description: "Build a DCF model for Costco in .xlsx",
        rubric: {type: "text", content: rubric},
        # or: rubric: {type: "file", file_id: rubric.id},
        max_iterations: 5 # optional; default 3, max 20
      }
    ]
  )
  ```
</CodeGroup>

## Outcome events

Progress on an outcome-oriented session is surfaced on the events [stream](/docs/en/managed-agents/events-and-streaming).

- `agent.*` events (messages, tool use, etc.) show progress towards the outcome.
- `span.outcome_evaluation_*` events are only emitted for outcome-oriented sessions and show the number of iteration loops and the grader's feedback process.
- You can also send `user.message` [events](/docs/en/managed-agents/events-and-streaming#user-events) to an outcome-oriented session, to direct the agent's work as it progresses, but these are not as necessary; the agent knows to work until it has exhausted its iterations or achieved the outcome.
- A `user.interrupt` event will pause work on the current outcome and mark the `span.outcome_evaluation_end.result` as `interrupted`, allowing you to kick off a new outcome.
- After the final outcome evaluation, the session can be continued as a conversational session, or a new outcome can be kicked off. The session will retain history of the prior outcome.

### Define outcome user event
<Note>
Only one outcome supported at a time, but you may chain together outcomes in sequence. To do this, send a new `user.define_outcome` event after the terminal event of the previous outcome.
</Note>

This is the event you send to initiate an outcome. It is echoed back on receipt, including a `processed_at` timestamp and `outcome_id`.

```json
{
  "type": "user.define_outcome",
  "description": "Build a DCF model for Costco in .xlsx",
  "rubric": { "type": "file", "file_id": "file_01..." },
  "max_iterations": 5
}
```

### Outcome evaluation start

Emitted once the grader starts an evaluation over one iteration loop. The `iteration` field is a 0-indexed revision counter: `0` is the first evaluation, `1` is the re-evaluation after the first revision, and so on.

```json
{
  "type": "span.outcome_evaluation_start",
  "id": "sevt_01def...",
  "outcome_id": "outc_01a...",
  "iteration": 0,
  "processed_at": "2026-03-25T14:01:45Z"
}
```

### Outcome evaluation ongoing

Heartbeat emitted while the grader runs. The grader's internal reasoning is opaque: you see that it's working, not what it's thinking.

```json
{
  "type": "span.outcome_evaluation_ongoing",
  "id": "sevt_01ghi...",
  "outcome_id": "outc_01a...",
  "processed_at": "2026-03-25T14:02:10Z"
}
```

### Outcome evaluation end

Emitted after the grader finishes evaluating one iteration. The `result` field indicates what happens next.

| Result | Next |
| --- | --- |
| `satisfied` | Session transitions to `idle`. |
| `needs_revision` | Agent starts a new iteration cycle. |
| `max_iterations_reached` | No further evaluation cycles. The agent may run one final revision before the session transitions to `idle`. |
| `failed` | Session transitions to `idle`. Returned when the rubric fundamentally does not match the task, for example if the description and rubric contradict each other. |
| `interrupted` | Only emitted if `outcome_evaluation_start` already fired before the interrupt. |

```json
{
  "type": "span.outcome_evaluation_end",
  "id": "sevt_01jkl...",
  "outcome_evaluation_start_id": "sevt_01def...",
  "outcome_id": "outc_01a...",
  "result": "satisfied",
  "explanation": "All 12 criteria met: revenue projections use 5 years of historical data, WACC assumptions are stated, sensitivity table is included...",
  "iteration": 0,
  "usage": {
    "input_tokens": 2400,
    "output_tokens": 350,
    "cache_creation_input_tokens": 0,
    "cache_read_input_tokens": 1800
  },
  "processed_at": "2026-03-25T14:03:00Z"
}
```

## Checking on outcome status

You can either listen on the [event stream](/docs/en/managed-agents/events-and-streaming) for `span.outcome_evaluation_end`, or poll `GET /v1/sessions/:id` and read `outcome_evaluations[].result`:

<CodeGroup>
  
  ```bash curl
  session=$(curl -fsSL "https://api.anthropic.com/v1/sessions/$session_id" \
    -H "x-api-key: $ANTHROPIC_API_KEY" \
    -H "anthropic-version: 2023-06-01" \
    -H "anthropic-beta: managed-agents-2026-04-01-research-preview")

  jq -r '.outcome_evaluations[] | "\(.outcome_id): \(.result)"' <<<"$session"
  # outc_01a...: satisfied
  ```
  
  ```bash CLI
  ant beta:sessions retrieve --session-id "$SESSION_ID"
  ```
  ```python Python
  session = client.beta.sessions.retrieve(session.id)

  for outcome in session.outcome_evaluations:
      print(f"{outcome.outcome_id}: {outcome.result}")
      # outc_01a...: satisfied
  ```
  ```typescript TypeScript
  const retrieved = await client.beta.sessions.retrieve(session.id);

  for (const outcome of retrieved.outcome_evaluations) {
    console.log(`${outcome.outcome_id}: ${outcome.result}`);
    // outc_01a...: satisfied
  }
  ```
  ```csharp C#
  session = await client.Beta.Sessions.Retrieve(session.ID);

  foreach (var outcome in session.OutcomeEvaluations)
  {
      Console.WriteLine($"{outcome.OutcomeID}: {outcome.Result}");
      // outc_01a...: satisfied
  }
  ```
  ```go Go
  	session, err = client.Beta.Sessions.Get(ctx, session.ID, anthropic.BetaSessionGetParams{})
  	if err != nil {
  		panic(err)
  	}

  	for _, outcome := range session.OutcomeEvaluations {
  		fmt.Printf("%s: %s\n", outcome.OutcomeID, outcome.Result)
  		// outc_01a...: satisfied
  	}
  ```
  ```java Java
      var retrieved = client.beta().sessions().retrieve(session.id());

      for (var outcome : retrieved.outcomeEvaluations()) {
          IO.println(outcome.outcomeId() + ": " + outcome.result());
          // outc_01a...: satisfied
      }
  ```
  ```php PHP
  $session = $client->beta->sessions->retrieve($session->id);

  foreach ($session->outcomeEvaluations as $outcome) {
      echo "{$outcome->outcomeID}: {$outcome->result}\n";
      // outc_01a...: satisfied
  }
  ```
  ```ruby Ruby
  session = client.beta.sessions.retrieve(session.id)

  session.outcome_evaluations.each do
    puts "#{it.outcome_id}: #{it.result}"
    # outc_01a...: satisfied
  end
  ```
</CodeGroup>

## Retrieving deliverables

The agent writes output files to `/mnt/session/outputs/` inside the container. Once the session is idle, fetch them via the [Files API](/docs/en/build-with-claude/files) scoped to the session:

<CodeGroup>
  ```bash curl
  # List files produced by this session
  curl -fsSL "https://api.anthropic.com/v1/files?scope_id=$session_id" \
    -H "x-api-key: $ANTHROPIC_API_KEY" \
    -H "anthropic-version: 2023-06-01" \
    -H "anthropic-beta: files-api-2025-04-14,managed-agents-2026-04-01-research-preview" \
  | jq '.data[] | {id, filename, size_bytes}'

  # Download by file_id
  curl -fsSL "https://api.anthropic.com/v1/files/$file_id/content" \
    -H "x-api-key: $ANTHROPIC_API_KEY" \
    -H "anthropic-version: 2023-06-01" \
    -H "anthropic-beta: files-api-2025-04-14" \
    -o costco_dcf.xlsx
  ```
  ```python Python
  files = client.beta.files.list(scope_id=session.id)
  for f in files.data:
      print(f"{f.id}: {f.filename} ({f.size_bytes} bytes)")

  content = client.beta.files.download(files.data[0].id)
  content.write_to_file("costco_dcf.xlsx")
  ```
</CodeGroup>