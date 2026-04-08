# Using memory

Give your agents persistent memory that survives across sessions using memory stores.

---

<Tip>
Agent Memory is a Research Preview feature. [Request access](https://claude.com/form/claude-managed-agents) to try it.
</Tip>

Agent API sessions are ephemeral by default. When a session ends, anything the agent learned is gone. Memory stores let the agent carry learnings across sessions: user preferences, project conventions, prior mistakes, and domain context.

<Note>
All Managed Agents API requests require the `managed-agents-2026-04-01` beta header. An additional beta header is needed for research preview features. The SDK sets these beta headers automatically.
</Note>

## Overview
A **memory store** is a workspace-scoped collection of text documents optimized for Claude. When one or more memory stores are attached to a session, the agent automatically checks the stores before starting a task and writes durable learnings when done - no additional prompting or configuration is needed on your side.

Each **memory** in a store can be accessed and edited directly via the API or Console, allowing for tuning, importing, and exporting memories.

Every change to a memory creates an immutable **memory_version** to support auditing and rolling back memory changes.

## Create a memory store

Give the store a `name` and a `description`. The description is passed to the agent, telling it what the store contains.

<CodeGroup>
  ```bash curl
  store=$(curl -fsS https://api.anthropic.com/v1/memory_stores \
    -H "x-api-key: $ANTHROPIC_API_KEY" \
    -H "anthropic-version: 2023-06-01" \
    -H "anthropic-beta: managed-agents-2026-04-01" \
    -H "content-type: application/json" \
    --data @- <<EOF
  {
    "name": "User Preferences",
    "description": "Per-user preferences and project context."
  }
  EOF
  )
  store_id=$(jq -r '.id' <<< "$store")
  echo "$store_id"  # memstore_01Hx...
  ```
  ```bash CLI
  store_id=$(ant beta:memory-stores create \
    --name "User Preferences" \
    --description "Per-user preferences and project context." \
    --transform id --format yaml)
  ```
  ```python Python
  store = client.beta.memory_stores.create(
      name="User Preferences",
      description="Per-user preferences and project context.",
  )
  print(store.id)  # memstore_01Hx...
  ```
  ```typescript TypeScript
  const store = await client.beta.memoryStores.create({
    name: "User Preferences",
    description: "Per-user preferences and project context."
  });
  console.log(store.id); // memstore_01Hx...
  ```
  ```csharp C#
  var store = await client.Beta.MemoryStores.Create(new()
  {
      Name = "User Preferences",
      Description = "Per-user preferences and project context.",
  });
  Console.WriteLine(store.ID);  // memstore_01Hx...
  ```
  ```go Go
  	store, err := client.Beta.MemoryStores.New(ctx, anthropic.BetaMemoryStoreNewParams{
  		Name:        "User Preferences",
  		Description: anthropic.String("Per-user preferences and project context."),
  	})
  	if err != nil {
  		panic(err)
  	}
  	fmt.Println(store.ID) // memstore_01Hx...
  ```
  ```java Java
      var store = client.beta().memoryStores().create(
          MemoryStoreCreateParams.builder()
              .name("User Preferences")
              .description("Per-user preferences and project context.")
              .build()
      );
      IO.println(store.id());  // memstore_01Hx...
  ```
  ```php PHP
  $store = $client->beta->memoryStores->create(
      name: 'User Preferences',
      description: 'Per-user preferences and project context.',
  );
  echo "{$store->id}\n"; // memstore_01Hx...
  ```
  ```ruby Ruby
  store = client.beta.memory_stores.create(
    name: "User Preferences",
    description: "Per-user preferences and project context."
  )
  puts store.id # memstore_01Hx...
  ```
</CodeGroup>

The memory store `id` (`memstore_...`) is what you pass when attaching the store to a session.

### Seed it with content (optional)

Pre-load a store with reference material before any agent runs:

<CodeGroup>
  
  ```bash curl
  curl -fsS "https://api.anthropic.com/v1/memory_stores/$store_id/memories" \
    -H "x-api-key: $ANTHROPIC_API_KEY" \
    -H "anthropic-version: 2023-06-01" \
    -H "anthropic-beta: managed-agents-2026-04-01" \
    -H "content-type: application/json" \
    --data @- > /dev/null <<EOF
  {
    "path": "/formatting_standards.md",
    "content": "All reports use GAAP formatting. Dates are ISO-8601..."
  }
  EOF
  ```
  
  ```bash CLI
  ant beta:memory-stores:memories write \
    --memory-store-id "$store_id" \
    --path "/formatting_standards.md" \
    --content "All reports use GAAP formatting. Dates are ISO-8601..." \
    > /dev/null
  ```
  ```python Python
  client.beta.memory_stores.memories.write(
      memory_store_id=store.id,
      path="/formatting_standards.md",
      content="All reports use GAAP formatting. Dates are ISO-8601...",
  )
  ```
  ```typescript TypeScript
  await client.beta.memoryStores.memories.write(store.id, {
    path: "/formatting_standards.md",
    content: "All reports use GAAP formatting. Dates are ISO-8601..."
  });
  ```
  ```csharp C#
  await client.Beta.MemoryStores.Memories.Create(store.ID, new()
  {
      Path = "/formatting_standards.md",
      Content = "All reports use GAAP formatting. Dates are ISO-8601...",
  });
  ```
  ```go Go
  	_, err = client.Beta.MemoryStores.Memories.New(ctx, store.ID, anthropic.BetaMemoryStoreMemoryNewParams{
  		Path:    "/formatting_standards.md",
  		Content: "All reports use GAAP formatting. Dates are ISO-8601...",
  	})
  	if err != nil {
  		panic(err)
  	}
  ```
  ```java Java
      client.beta().memoryStores().memories().create(
          store.id(),
          MemoryCreateParams.builder()
              .path("/formatting_standards.md")
              .content("All reports use GAAP formatting. Dates are ISO-8601...")
              .build()
      );
  ```
  ```php PHP
  $client->beta->memoryStores->memories->create(
      $store->id,
      path: '/formatting_standards.md',
      content: 'All reports use GAAP formatting. Dates are ISO-8601...',
  );
  ```
  ```ruby Ruby
  client.beta.memory_stores.memories.create(
    store.id,
    path: "/formatting_standards.md",
    content: "All reports use GAAP formatting. Dates are ISO-8601..."
  )
  ```
</CodeGroup>

<Tip>
Individual memories within the store are capped at 100KB (~25K tokens). Structure memory as many small focused files, not a few large ones.
</Tip>

## Attach memory to a session

Memory stores are attached in the session's `resources[]` array.

Optionally include a `prompt` if you want to provide session-specific instructions to Claude for how to use this memory store. It is provided to Claude in addition to the memory store's `name` and `description`, and is capped at 4,096 characters.

You can configure `access` as well. It defaults to `read_write`, but `read_only` is also supported (shown explicitly in the example below).

<CodeGroup>
  
  ```bash curl
  session=$(curl -fsS https://api.anthropic.com/v1/sessions \
    -H "x-api-key: $ANTHROPIC_API_KEY" \
    -H "anthropic-version: 2023-06-01" \
    -H "anthropic-beta: managed-agents-2026-04-01" \
    -H "content-type: application/json" \
    --data @- <<EOF
  {
    "agent": "$agent_id",
    "environment_id": "$environment_id",
    "resources": [
      {
        "type": "memory_store",
        "memory_store_id": "$store_id",
        "access": "read_write",
        "prompt": "User preferences and project context. Check before starting any task."
      }
    ]
  }
  EOF
  )
  ```
  
  ```bash CLI
  ant beta:sessions create <<YAML
  agent: $agent_id
  environment_id: $environment_id
  resources:
    - type: memory_store
      memory_store_id: $store_id
      access: read_write
      prompt: User preferences and project context. Check before starting any task.
  YAML
  ```
  ```python Python
  session = client.beta.sessions.create(
      agent=agent.id,
      environment_id=environment.id,
      resources=[
          {
              "type": "memory_store",
              "memory_store_id": store.id,
              "access": "read_write",
              "prompt": "User preferences and project context. Check before starting any task.",
          }
      ],
  )
  ```
  ```typescript TypeScript
  const session = await client.beta.sessions.create({
    agent: agent.id,
    environment_id: environment.id,
    resources: [
      {
        type: "memory_store",
        memory_store_id: store.id,
        access: "read_write",
        prompt: "User preferences and project context. Check before starting any task."
      }
    ]
  });
  ```
  ```csharp C#
  var session = await client.Beta.Sessions.Create(new()
  {
      Agent = agent.ID,
      EnvironmentID = environment.ID,
      Resources =
      [
          new BetaManagedAgentsMemoryStoreResourceParams
          {
              Type = "memory_store",
              MemoryStoreID = store.ID,
              Access = "read_write",
              Prompt = "User preferences and project context. Check before starting any task.",
          },
      ],
  });
  ```
  ```go Go
  	session, err := client.Beta.Sessions.New(ctx, anthropic.BetaSessionNewParams{
  		Agent: anthropic.BetaSessionNewParamsAgentUnion{
  			OfString: anthropic.String(agent.ID),
  		},
  		EnvironmentID: environment.ID,
  		Resources: []anthropic.BetaSessionNewParamsResourceUnion{{
  			OfMemoryStore: &anthropic.BetaManagedAgentsMemoryStoreResourceParams{
  				MemoryStoreID: store.ID,
  				Access:        anthropic.BetaManagedAgentsMemoryStoreResourceParamsAccessReadWrite,
  				Prompt:        anthropic.String("User preferences and project context. Check before starting any task."),
  			},
  		}},
  	})
  	if err != nil {
  		panic(err)
  	}
  ```
  ```java Java
      var session = client.beta().sessions().create(
          SessionCreateParams.builder()
              .agent(agent.id())
              .environmentId(environment.id())
              .addResource(
                  BetaManagedAgentsMemoryStoreResourceParams.builder()
                      .memoryStoreId(store.id())
                      .access(BetaManagedAgentsMemoryStoreResourceParams.Access.READ_WRITE)
                      .prompt("User preferences and project context. Check before starting any task.")
                      .build()
              )
              .build()
      );
  ```
  ```php PHP
  $session = $client->beta->sessions->create(
      agent: $agent->id,
      environmentID: $environment->id,
      resources: [
          [
              'type' => 'memory_store',
              'memory_store_id' => $store->id,
              'access' => 'read_write',
              'prompt' => 'User preferences and project context. Check before starting any task.',
          ],
      ],
  );
  ```
  ```ruby Ruby
  session = client.beta.sessions.create(
    agent: agent.id,
    environment_id: environment.id,
    resources: [
      {
        type: "memory_store",
        memory_store_id: store.id,
        access: "read_write",
        prompt: "User preferences and project context. Check before starting any task."
      }
    ]
  )
  ```
</CodeGroup>

A maximum of **8 memory stores** are supported per session. Attach multiple stores when different parts of memory have different owners or access rules. Common reasons:

- **Shared reference material** - one read-only store attached to many sessions (standards, conventions, domain knowledge), kept separate from each session's own read-write learnings.
- **Mapping to your product's structure** - one store per end-user, per-team, or per-project, while sharing a single agent configuration.
- **Different lifecycles** - a store that outlives any single session, or one you want to archive on its own schedule.

### Memory tools
When memory stores are attached to a session, the agent automatically gains access to memory tools. The agent's interactions with memory stores are registered as `agent.tool_use` events in the [event stream](/docs/en/managed-agents/events-and-streaming).

| Tool | Description |
| --- | --- |
| `memory_list` | List documents in a store, optionally filtered by path prefix. |
| `memory_search` | Full-text search across document contents. |
| `memory_read` | Read a document's contents. |
| `memory_write` | Create or overwrite a document at a path. |
| `memory_edit` | Modify an existing document. |
| `memory_delete` | Remove a document. |

## Inspect and correct memory

Memory stores can be managed directly via the API. Use this for building review workflows, correcting bad memories, or seeding stores before any session runs.

### List memories
List does not return memory content, just object metadata. Use `path_prefix` for directory-scoped lists (include a trailing slash: `/notes/` matches `/notes/a.md` but not `/notes_backup/old.md`).

<CodeGroup>
  
  ```bash curl
  page=$(curl -fsS "https://api.anthropic.com/v1/memory_stores/$store_id/memories?path_prefix=/" \
    -H "x-api-key: $ANTHROPIC_API_KEY" \
    -H "anthropic-version: 2023-06-01" \
    -H "anthropic-beta: managed-agents-2026-04-01")
  jq -r '.data[] | "\(.path)  (\(.size_bytes) bytes, sha=\(.content_sha256[0:8]))"' <<< "$page"
  ```
  
  ```bash CLI
  ant beta:memory-stores:memories list \
    --memory-store-id "$store_id" \
    --path-prefix "/"
  ```
  ```python Python
  page = client.beta.memory_stores.memories.list(
      store.id,
      path_prefix="/",
  )
  for memory in page.data:
      print(
          f"{memory.path}  ({memory.size_bytes} bytes, sha={memory.content_sha256[:8]})"
      )
  ```
  ```typescript TypeScript
  const page = await client.beta.memoryStores.memories.list(store.id, {
    path_prefix: "/"
  });
  for (const memory of page.data) {
    console.log(
      `${memory.path}  (${memory.size_bytes} bytes, sha=${memory.content_sha256.slice(0, 8)})`
    );
  }
  ```
  ```csharp C#
  var page = await client.Beta.MemoryStores.Memories.List(store.ID, new() { PathPrefix = "/" });
  foreach (var memory in page.Data)
  {
      Console.WriteLine($"{memory.Path}  ({memory.SizeBytes} bytes, sha={memory.ContentSha256[..8]})");
  }
  ```
  ```go Go
  	page, err := client.Beta.MemoryStores.Memories.List(ctx, store.ID, anthropic.BetaMemoryStoreMemoryListParams{
  		PathPrefix: anthropic.String("/"),
  	})
  	if err != nil {
  		panic(err)
  	}
  	for _, memory := range page.Data {
  		fmt.Printf("%s  (%d bytes, sha=%s)\n", memory.Path, memory.SizeBytes, memory.ContentSha256[:8])
  	}
  ```
  ```java Java
      var page = client.beta().memoryStores().memories().list(
          store.id(),
          MemoryListParams.builder().pathPrefix("/").build()
      );
      for (var memory : page.data()) {
          IO.println("%s  (%d bytes, sha=%s)".formatted(
              memory.path(), memory.sizeBytes(), memory.contentSha256().substring(0, 8)
          ));
      }
  ```
  ```php PHP
  $page = $client->beta->memoryStores->memories->list($store->id, pathPrefix: '/');
  foreach ($page->data as $memory) {
      printf("%s  (%d bytes, sha=%s)\n", $memory->path, $memory->sizeBytes, substr($memory->contentSha256, 0, 8));
  }
  ```
  ```ruby Ruby
  page = client.beta.memory_stores.memories.list(
    store.id,
    path_prefix: "/"
  )
  page.data.each do
    puts "#{it.path}  (#{it.size_bytes} bytes, sha=#{it.content_sha256[0, 8]})"
  end
  ```
</CodeGroup>

### Read a memory
Fetching an individual memory returns the full document content.

<CodeGroup>
  
  ```bash curl
  mem=$(curl -fsS "https://api.anthropic.com/v1/memory_stores/$store_id/memories/$memory_id" \
    -H "x-api-key: $ANTHROPIC_API_KEY" \
    -H "anthropic-version: 2023-06-01" \
    -H "anthropic-beta: managed-agents-2026-04-01")
  jq -r '.content' <<< "$mem"
  ```
  
  ```bash CLI
  ant beta:memory-stores:memories retrieve \
    --memory-store-id "$store_id" \
    --memory-id "$memory_id"
  ```
  ```python Python
  mem = client.beta.memory_stores.memories.retrieve(
      memory_id,
      memory_store_id=store.id,
  )
  print(mem.content)
  ```
  ```typescript TypeScript
  const memory = await client.beta.memoryStores.memories.retrieve(memoryId, {
    memory_store_id: store.id
  });
  console.log(memory.content);
  ```
  ```csharp C#
  var mem = await client.Beta.MemoryStores.Memories.Retrieve(memoryId, new()
  {
      MemoryStoreID = store.ID,
  });
  Console.WriteLine(mem.Content);
  ```
  ```go Go
  	memory, err := client.Beta.MemoryStores.Memories.Get(ctx, memoryID, anthropic.BetaMemoryStoreMemoryGetParams{
  		MemoryStoreID: store.ID,
  	})
  	if err != nil {
  		panic(err)
  	}
  	fmt.Println(memory.Content)
  ```
  ```java Java
      var mem = client.beta().memoryStores().memories().retrieve(
          memoryId,
          MemoryRetrieveParams.builder().memoryStoreId(store.id()).build()
      );
      IO.println(mem.content());
  ```
  ```php PHP
  $memory = $client->beta->memoryStores->memories->retrieve($memoryId, memoryStoreID: $store->id);
  echo "{$memory->content}\n";
  ```
  ```ruby Ruby
  mem = client.beta.memory_stores.memories.retrieve(
    memory_id,
    memory_store_id: store.id
  )
  puts mem.content
  ```
</CodeGroup>

### Write a document

Use `memories.write` to upsert a document **by path**. If nothing exists at the path, it is created; if a document already exists there, its content is replaced. To mutate an existing document **by `mem_...` ID** (for example, to rename its path or safely apply a content edit), use `memories.update` instead (see [Update](#update) below).

<CodeGroup>
  
  ```bash curl
  mem=$(curl -fsS "https://api.anthropic.com/v1/memory_stores/$store_id/memories" \
    -H "x-api-key: $ANTHROPIC_API_KEY" \
    -H "anthropic-version: 2023-06-01" \
    -H "anthropic-beta: managed-agents-2026-04-01" \
    -H "content-type: application/json" \
    --data @- <<EOF
  {
    "path": "/preferences/formatting.md",
    "content": "Always use tabs, not spaces."
  }
  EOF
  )
  ```
  
  ```bash CLI
  mem_sha=$(ant beta:memory-stores:memories write \
    --memory-store-id "$store_id" \
    --path "/preferences/formatting.md" \
    --content "Always use tabs, not spaces." \
    --transform content_sha256 --format yaml)
  ```
  ```python Python
  mem = client.beta.memory_stores.memories.write(
      memory_store_id=store.id,
      path="/preferences/formatting.md",
      content="Always use tabs, not spaces.",
  )
  ```
  ```typescript TypeScript
  const mem = await client.beta.memoryStores.memories.write(store.id, {
    path: "/preferences/formatting.md",
    content: "Always use tabs, not spaces."
  });
  ```
  ```csharp C#
  mem = await client.Beta.MemoryStores.Memories.Create(store.ID, new()
  {
      Path = "/preferences/formatting.md",
      Content = "Always use tabs, not spaces.",
  });
  ```
  ```go Go
  	mem, err := client.Beta.MemoryStores.Memories.New(ctx, store.ID, anthropic.BetaMemoryStoreMemoryNewParams{
  		Path:    "/preferences/formatting.md",
  		Content: "Always use tabs, not spaces.",
  	})
  	if err != nil {
  		panic(err)
  	}
  ```
  ```java Java
      var mem = client.beta().memoryStores().memories().create(
          store.id(),
          MemoryCreateParams.builder()
              .path("/preferences/formatting.md")
              .content("Always use tabs, not spaces.")
              .build()
      );
  ```
  ```php PHP
  $mem = $client->beta->memoryStores->memories->create(
      $store->id,
      path: '/preferences/formatting.md',
      content: 'Always use tabs, not spaces.',
  );
  ```
  ```ruby Ruby
  mem = client.beta.memory_stores.memories.create(
    store.id,
    path: "/preferences/formatting.md",
    content: "Always use tabs, not spaces."
  )
  ```
</CodeGroup>

### Create only if the path is free

Pass `precondition={"type": "not_exists"}` to `memories.write` to make it a create-only guard. If a document already exists at the path, the write returns `409 memory_precondition_failed` instead of replacing it. Use this when seeding a store and you want to avoid clobbering existing content.

<CodeGroup>
  
  ```bash curl
  curl -fsS "https://api.anthropic.com/v1/memory_stores/$store_id/memories" \
    -H "x-api-key: $ANTHROPIC_API_KEY" \
    -H "anthropic-version: 2023-06-01" \
    -H "anthropic-beta: managed-agents-2026-04-01" \
    -H "content-type: application/json" \
    --data @- > /dev/null <<EOF
  {
    "path": "/preferences/formatting.md",
    "content": "Always use 2-space indentation.",
    "precondition": {"type": "not_exists"}
  }
  EOF
  ```
  
  ```bash CLI
  ant beta:memory-stores:memories write \
    --memory-store-id "$store_id" \
    > /dev/null <<YAML
  path: /preferences/formatting.md
  content: "CORRECTED: Always use 2-space indentation."
  precondition:
    type: content_sha256
    content_sha256: $mem_sha
  YAML
  ```
  ```python Python
  client.beta.memory_stores.memories.write(
      memory_store_id=store.id,
      path="/preferences/formatting.md",
      content="Always use 2-space indentation.",
      precondition={"type": "not_exists"},
  )
  ```
  ```typescript TypeScript
  await client.beta.memoryStores.memories.write(store.id, {
    path: "/preferences/formatting.md",
    content: "Always use 2-space indentation.",
    precondition: { type: "not_exists" }
  });
  ```
  ```csharp C#
  await client.Beta.MemoryStores.Memories.Create(store.ID, new()
  {
      Path = "/preferences/formatting.md",
      Content = "Always use 2-space indentation.",
      Precondition = new NotExistsPrecondition { Type = "not_exists" },
  });
  ```
  ```go Go
  	_, err = client.Beta.MemoryStores.Memories.New(ctx, store.ID, anthropic.BetaMemoryStoreMemoryNewParams{
  		Path:    "/preferences/formatting.md",
  		Content: "Always use 2-space indentation.",
  		Precondition: anthropic.BetaMemoryStoreMemoryNewParamsPreconditionUnion{
  			OfNotExists: &anthropic.BetaManagedAgentsNotExistsPreconditionParams{},
  		},
  	})
  	if err != nil {
  		panic(err)
  	}
  ```
  ```java Java
      client.beta().memoryStores().memories().create(
          store.id(),
          MemoryCreateParams.builder()
              .path("/preferences/formatting.md")
              .content("Always use 2-space indentation.")
              .precondition(
                  MemoryCreateParams.Precondition.builder()
                      .type(MemoryCreateParams.Precondition.Type.NOT_EXISTS)
                      .build()
              )
              .build()
      );
  ```
  ```php PHP
  $client->beta->memoryStores->memories->create(
      $store->id,
      path: '/preferences/formatting.md',
      content: 'Always use 2-space indentation.',
      precondition: ['type' => 'not_exists'],
  );
  ```
  ```ruby Ruby
  client.beta.memory_stores.memories.create(
    store.id,
    path: "/preferences/formatting.md",
    content: "Always use 2-space indentation.",
    precondition: {type: "not_exists"}
  )
  ```
</CodeGroup>

To safely edit an existing document (read, modify, write back without clobbering a concurrent change), use `memories.update` with a `content_sha256` precondition instead. See [Update](#update) below.

### Update

`memories.update()` modifies an existing document by its `mem_...` ID. You can change `content`, `path` (a rename), or both in one call.

Renaming onto an occupied path returns `409 conflict`. The caller must delete or rename the blocker first, or pass `precondition={"type": "not_exists"}` to make the rename a no-op if anything already exists at the target.

The example below renames a document to an archive path:

<CodeGroup>
  
  ```bash curl
  curl -fsS -X PATCH "https://api.anthropic.com/v1/memory_stores/$store_id/memories/$mem_id" \
    -H "x-api-key: $ANTHROPIC_API_KEY" \
    -H "anthropic-version: 2023-06-01" \
    -H "anthropic-beta: managed-agents-2026-04-01" \
    -H "content-type: application/json" \
    -d '{"path": "/archive/2026_q1_formatting.md"}' > /dev/null
  ```
  
  ```bash CLI
  ant beta:memory-stores:memories update \
    --memory-store-id "$store_id" \
    --memory-id "$mem_id" \
    --path "/archive/2026_q1_formatting.md" \
    > /dev/null
  ```
  ```python Python
  client.beta.memory_stores.memories.update(
      mem.id,
      memory_store_id=store.id,
      path="/archive/2026_q1_formatting.md",
  )
  ```
  ```typescript TypeScript
  await client.beta.memoryStores.memories.update(mem.id, {
    memory_store_id: store.id,
    path: "/archive/2026_q1_formatting.md"
  });
  ```
  ```csharp C#
  await client.Beta.MemoryStores.Memories.Update(mem.ID, new()
  {
      MemoryStoreID = store.ID,
      Path = "/archive/2026_q1_formatting.md",
  });
  ```
  ```go Go
  	_, err = client.Beta.MemoryStores.Memories.Update(ctx, mem.ID, anthropic.BetaMemoryStoreMemoryUpdateParams{
  		MemoryStoreID: store.ID,
  		Path:          anthropic.String("/archive/2026_q1_formatting.md"),
  	})
  	if err != nil {
  		panic(err)
  	}
  ```
  ```java Java
      client.beta().memoryStores().memories().update(
          mem.id(),
          MemoryUpdateParams.builder()
              .memoryStoreId(store.id())
              .path("/archive/2026_q1_formatting.md")
              .build()
      );
  ```
  ```php PHP
  $client->beta->memoryStores->memories->update(
      $mem->id,
      memoryStoreID: $store->id,
      path: '/archive/2026_q1_formatting.md',
  );
  ```
  ```ruby Ruby
  client.beta.memory_stores.memories.update(
    mem.id,
    memory_store_id: store.id,
    path: "/archive/2026_q1_formatting.md"
  )
  ```
</CodeGroup>

#### Safe content edits (optimistic concurrency)

To edit a document's content without clobbering a concurrent write, pass a `content_sha256` precondition. The update only applies if the stored hash still matches the one you read; on mismatch it returns `409 memory_precondition_failed`, at which point you re-read the document and retry against the fresh state.

<CodeGroup>
  ```bash curl
  curl -fsS -X PATCH "https://api.anthropic.com/v1/memory_stores/$store_id/memories/$mem_id" \
    -H "x-api-key: $ANTHROPIC_API_KEY" \
    -H "anthropic-version: 2023-06-01" \
    -H "anthropic-beta: managed-agents-2026-04-01" \
    -H "content-type: application/json" \
    --data @- > /dev/null <<EOF
  {
    "content": "CORRECTED: Always use 2-space indentation.",
    "precondition": {"type": "content_sha256", "content_sha256": "$mem_sha"}
  }
  EOF
  ```
  ```python Python
  client.beta.memory_stores.memories.update(
      memory_id=mem.id,
      memory_store_id=store.id,
      content="CORRECTED: Always use 2-space indentation.",
      precondition={"type": "content_sha256", "content_sha256": mem.content_sha256},
  )
  ```
  ```typescript TypeScript
  await client.beta.memoryStores.memories.update(mem.id, {
    memory_store_id: store.id,
    content: "CORRECTED: Always use 2-space indentation.",
    precondition: { type: "content_sha256", content_sha256: mem.content_sha256 }
  });
  ```
  ```csharp C#
  await client.Beta.MemoryStores.Memories.Update(mem.ID, new()
  {
      MemoryStoreID = store.ID,
      Content = "CORRECTED: Always use 2-space indentation.",
      Precondition = new ContentSha256Precondition
      {
          Type = "content_sha256",
          ContentSha256 = mem.ContentSha256,
      },
  });
  ```
  ```go Go
  	_, err = client.Beta.MemoryStores.Memories.Update(ctx, mem.ID, anthropic.BetaMemoryStoreMemoryUpdateParams{
  		MemoryStoreID: store.ID,
  		Content:       anthropic.String("CORRECTED: Always use 2-space indentation."),
  		Precondition: anthropic.BetaMemoryStoreMemoryUpdateParamsPreconditionUnion{
  			OfContentSha256: &anthropic.BetaManagedAgentsContentSha256PreconditionParams{
  				ContentSha256: mem.ContentSha256,
  			},
  		},
  	})
  	if err != nil {
  		panic(err)
  	}
  ```
  ```java Java
      client.beta().memoryStores().memories().update(
          mem.id(),
          MemoryUpdateParams.builder()
              .memoryStoreId(store.id())
              .content("CORRECTED: Always use 2-space indentation.")
              .precondition(
                  MemoryUpdateParams.Precondition.builder()
                      .type(MemoryUpdateParams.Precondition.Type.CONTENT_SHA256)
                      .contentSha256(mem.contentSha256())
                      .build()
              )
              .build()
      );
  ```
  ```php PHP
  $client->beta->memoryStores->memories->update(
      $mem->id,
      memoryStoreID: $store->id,
      content: 'CORRECTED: Always use 2-space indentation.',
      precondition: ['type' => 'content_sha256', 'content_sha256' => $mem->contentSha256],
  );
  ```
  ```ruby Ruby
  client.beta.memory_stores.memories.update(
    mem.id,
    memory_store_id: store.id,
    content: "CORRECTED: Always use 2-space indentation.",
    precondition: {type: "content_sha256", content_sha256: mem.content_sha256}
  )
  ```
</CodeGroup>

### Delete a document

<CodeGroup>
  
  ```bash curl
  curl -fsS -X DELETE "https://api.anthropic.com/v1/memory_stores/$store_id/memories/$mem_id" \
    -H "x-api-key: $ANTHROPIC_API_KEY" \
    -H "anthropic-version: 2023-06-01" \
    -H "anthropic-beta: managed-agents-2026-04-01" > /dev/null
  ```
  
  ```bash CLI
  ant beta:memory-stores:memories delete \
    --memory-store-id "$store_id" \
    --memory-id "$mem_id" \
    > /dev/null
  ```
  ```python Python
  client.beta.memory_stores.memories.delete(
      mem.id,
      memory_store_id=store.id,
  )
  ```
  ```typescript TypeScript
  await client.beta.memoryStores.memories.delete(mem.id, {
    memory_store_id: store.id
  });
  ```
  ```csharp C#
  await client.Beta.MemoryStores.Memories.Delete(mem.ID, new()
  {
      MemoryStoreID = store.ID,
  });
  ```
  ```go Go
  	_, err = client.Beta.MemoryStores.Memories.Delete(ctx, mem.ID, anthropic.BetaMemoryStoreMemoryDeleteParams{
  		MemoryStoreID: store.ID,
  	})
  	if err != nil {
  		panic(err)
  	}
  ```
  ```java Java
      client.beta().memoryStores().memories().delete(
          mem.id(),
          MemoryDeleteParams.builder().memoryStoreId(store.id()).build()
      );
  ```
  ```php PHP
  $client->beta->memoryStores->memories->delete($mem->id, memoryStoreID: $store->id);
  ```
  ```ruby Ruby
  client.beta.memory_stores.memories.delete(
    mem.id,
    memory_store_id: store.id
  )
  ```
</CodeGroup>

Optionally pass `expected_content_sha256` for a conditional delete.

## Memory versions

Every mutation to a memory creates an immutable **memory version** (`memver_...`). Versions accumulate for the lifetime of the parent memory and form the audit and rollback surface underneath it. The live `memories.retrieve` call always returns the current head; the version endpoints give you the full history.

A new version is written on every mutation:

- The first `memories.write` to a path creates a version with `operation: "created"`.
- `memories.update` that changes `content`, `path`, or both creates a version with `operation: "modified"`.
- `memories.delete` creates a version with `operation: "deleted"`.

Use the version endpoints to audit which user or agent changed what and when, to inspect or restore a prior snapshot, and to scrub sensitive content out of history with redact.

### List versions

List paginated version metadata for a store, newest-first. Filter by `memory_id`, `operation` (`created`, `modified`, or `deleted`), `session_id`, `api_key_id`, or a `created_at_gte`/`created_at_lte` time range. The list response does not include the `content` body; fetch individual versions with `retrieve` when you need the full content.

<CodeGroup>
  ```bash curl
  curl -fsS "https://api.anthropic.com/v1/memory_stores/$store_id/memory_versions?memory_id=$mem_id" \
    -H "x-api-key: $ANTHROPIC_API_KEY" \
    -H "anthropic-version: 2023-06-01" \
    -H "anthropic-beta: managed-agents-2026-04-01" \
    | jq -r '.data[] | "\(.id): \(.operation)"'
  ```
  ```python Python
  for v in client.beta.memory_stores.memory_versions.list(
      store.id,
      memory_id=mem.id,
  ):
      print(f"{v.id}: {v.operation}")
  ```
  ```typescript TypeScript
  const versions = await client.beta.memoryStores.memoryVersions.list(store.id, {
    memory_id: mem.id
  });
  for await (const v of versions) {
    console.log(`${v.id}: ${v.operation}`);
  }
  ```
  ```csharp C#
  var versions = await client.Beta.MemoryStores.MemoryVersions.List(store.ID, new()
  {
      MemoryID = mem.ID,
  });
  await foreach (var v in versions.Paginate())
  {
      Console.WriteLine($"{v.ID}: {v.Operation.Raw()}");
  }
  ```
  ```go Go
  	page := client.Beta.MemoryStores.MemoryVersions.ListAutoPaging(ctx, store.ID, anthropic.BetaMemoryStoreMemoryVersionListParams{
  		MemoryID: anthropic.String(mem.ID),
  	})
  	for page.Next() {
  		v := page.Current()
  		fmt.Printf("%s: %s\n", v.ID, v.Operation)
  	}
  	if err := page.Err(); err != nil {
  		panic(err)
  	}
  ```
  ```java Java
      for (var v : client.beta().memoryStores().memoryVersions().list(
          store.id(),
          MemoryVersionListParams.builder().memoryId(mem.id()).build()
      ).autoPager()) {
          IO.println(v.id() + ": " + v.operation());
      }
  ```
  ```php PHP
  foreach ($client->beta->memoryStores->memoryVersions->list(
      $store->id,
      memoryID: $mem->id,
  )->pagingEachItem() as $v) {
      echo "{$v->id}: {$v->operation}\n";
  }
  ```
  ```ruby Ruby
  client.beta.memory_stores.memory_versions.list(
    store.id,
    memory_id: mem.id
  ).auto_paging_each do |v|
    puts "#{v.id}: #{v.operation}"
  end
  ```
</CodeGroup>

### Retrieve a version

Fetching an individual version returns the same fields as the list response plus the full `content` body.

<CodeGroup>
  ```bash curl
  curl -fsS "https://api.anthropic.com/v1/memory_stores/$store_id/memory_versions/$version_id" \
    -H "x-api-key: $ANTHROPIC_API_KEY" \
    -H "anthropic-version: 2023-06-01" \
    -H "anthropic-beta: managed-agents-2026-04-01"
  ```
  ```python Python
  version = client.beta.memory_stores.memory_versions.retrieve(
      version_id,
      memory_store_id=store.id,
  )
  print(version.content)
  ```
  ```typescript TypeScript
  const version = await client.beta.memoryStores.memoryVersions.retrieve(versionId, {
    memory_store_id: store.id
  });
  console.log(version.content);
  ```
  ```csharp C#
  var version = await client.Beta.MemoryStores.MemoryVersions.Retrieve(versionId, new()
  {
      MemoryStoreID = store.ID,
  });
  Console.WriteLine(version.Content);
  ```
  ```go Go
  	version, err := client.Beta.MemoryStores.MemoryVersions.Get(ctx, versionID, anthropic.BetaMemoryStoreMemoryVersionGetParams{
  		MemoryStoreID: store.ID,
  	})
  	if err != nil {
  		panic(err)
  	}
  	fmt.Println(version.Content)
  ```
  ```java Java
      var version = client.beta().memoryStores().memoryVersions().retrieve(
          versionId,
          MemoryVersionRetrieveParams.builder().memoryStoreId(store.id()).build()
      );
      IO.println(version.content());
  ```
  ```php PHP
  $version = $client->beta->memoryStores->memoryVersions->retrieve(
      $versionId,
      memoryStoreID: $store->id,
  );
  echo "{$version->content}\n";
  ```
  ```ruby Ruby
  version = client.beta.memory_stores.memory_versions.retrieve(
    version_id,
    memory_store_id: store.id
  )
  puts version.content
  ```
</CodeGroup>

### Redact a version

Redact scrubs content out of a historical version while preserving the audit trail (who did what, when). Use it for compliance workflows such as removing leaked secrets, PII, or user deletion requests. Redact hard clears `content`, `content_sha256`, `content_size_bytes`, and `path`; all other fields, including the actor and timestamps, are preserved.

<CodeGroup>
  ```bash curl
  curl -fsS -X POST "https://api.anthropic.com/v1/memory_stores/$store_id/memory_versions/$version_id/redact" \
    -H "x-api-key: $ANTHROPIC_API_KEY" \
    -H "anthropic-version: 2023-06-01" \
    -H "anthropic-beta: managed-agents-2026-04-01" \
    -H "content-type: application/json" \
    -d '{}'
  ```
  ```python Python
  client.beta.memory_stores.memory_versions.redact(
      version_id,
      memory_store_id=store.id,
  )
  ```
  ```typescript TypeScript
  await client.beta.memoryStores.memoryVersions.redact(versionId, {
    memory_store_id: store.id
  });
  ```
  ```csharp C#
  await client.Beta.MemoryStores.MemoryVersions.Redact(versionId, new()
  {
      MemoryStoreID = store.ID,
  });
  ```
  ```go Go
  	_, err = client.Beta.MemoryStores.MemoryVersions.Redact(ctx, versionID, anthropic.BetaMemoryStoreMemoryVersionRedactParams{
  		MemoryStoreID: store.ID,
  	})
  	if err != nil {
  		panic(err)
  	}
  ```
  ```java Java
      client.beta().memoryStores().memoryVersions().redact(
          versionId,
          MemoryVersionRedactParams.builder().memoryStoreId(store.id()).build()
      );
  ```
  ```php PHP
  $client->beta->memoryStores->memoryVersions->redact(
      $versionId,
      memoryStoreID: $store->id,
  );
  ```
  ```ruby Ruby
  client.beta.memory_stores.memory_versions.redact(
    version_id,
    memory_store_id: store.id
  )
  ```
</CodeGroup>