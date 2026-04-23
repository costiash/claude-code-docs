# Using agent memory

Give your agents persistent memory that survives across sessions using memory stores.

---

Each Managed Agents session starts with a fresh context by default. When a session ends, anything the agent learned is gone. Memory stores let the agent carry information across sessions: user preferences, project conventions, prior mistakes, and domain context.

<Note>
All Managed Agents API requests require the `managed-agents-2026-04-01` beta header. The SDKs set the beta header automatically.
</Note>

## Overview
A **memory store** is a workspace-scoped collection of text documents optimized for Claude. When you attach a store to a session, it is mounted as a directory inside the session's container. The agent reads and writes it with the same file tools it uses for the rest of the filesystem, and a note describing each mount is automatically added to the system prompt so the agent knows where to look. The [agent toolset](/docs/en/managed-agents/tools) is required for these interactions; make sure to enable it during [agent creation](/docs/en/managed-agents/agent-setup).

Each **memory** in a store is addressed by a path and can be read and edited directly via the API or Console, allowing for tuning, importing, and exporting.

Every change to a memory creates an immutable **memory version**, giving you an audit trail and point-in-time recovery for everything the agent writes.

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
  
  ```bash CLI nocheck
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
  
  ```bash CLI nocheck
  ant beta:memory-stores:memories create \
    --memory-store-id "$store_id" \
    --path "/formatting_standards.md" \
    --content "All reports use GAAP formatting. Dates are ISO-8601..." \
    > /dev/null
  ```
  ```python Python
  client.beta.memory_stores.memories.create(
      store.id,
      path="/formatting_standards.md",
      content="All reports use GAAP formatting. Dates are ISO-8601...",
  )
  ```
  ```typescript TypeScript
  await client.beta.memoryStores.memories.create(store.id, {
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

## Attach a memory store to a session

Memory stores are attached in the session's `resources[]` array when the session is created. Unlike file and repository resources, memory stores can only be attached at session creation time; adding or removing one from a running session is not supported.

Optionally include `instructions` to provide session-specific guidance for how the agent should use this store. It is shown to the agent alongside the store's `name` and `description`, and is capped at 4,096 characters.

You can configure `access` as well. It defaults to `read_write`, but `read_only` is also supported (shown explicitly in the example below).

<CodeGroup>
  
  ```bash curl nocheck
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
        "instructions": "User preferences and project context. Check before starting any task."
      }
    ]
  }
  EOF
  )
  ```
  
  ```bash CLI nocheck
  ant beta:sessions create <<YAML
  agent: $agent_id
  environment_id: $environment_id
  resources:
    - type: memory_store
      memory_store_id: $store_id
      access: read_write
      instructions: User preferences and project context. Check before starting any task.
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
              "instructions": "User preferences and project context. Check before starting any task.",
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
        instructions: "User preferences and project context. Check before starting any task."
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
              Instructions = "User preferences and project context. Check before starting any task.",
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
  				Instructions:  anthropic.String("User preferences and project context. Check before starting any task."),
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
                      .instructions("User preferences and project context. Check before starting any task.")
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
              'instructions' => 'User preferences and project context. Check before starting any task.',
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
        instructions: "User preferences and project context. Check before starting any task."
      }
    ]
  )
  ```
</CodeGroup>

<Warning>
Memory stores attach with `read_write` access by default. If the agent processes untrusted input (user-supplied prompts, fetched web content, or third-party tool output), a successful prompt injection could write malicious content into the store. Later sessions then read that content as trusted memory. Use `read_only` for reference material, shared lookups, and any store the agent does not need to modify.
</Warning>

A maximum of **8 memory stores** are supported per session. Attach multiple stores when different parts of memory have different owners or access rules. Common reasons:

- **Shared reference material:** one read-only store attached to many sessions (standards, conventions, domain knowledge), kept separate from each session's own read-write store.
- **Mapping to your product's structure:** one store per end user, per team, or per project, while sharing a single agent configuration.
- **Different lifecycles:** a store that outlives any single session, or one you want to archive on its own schedule.

### How the agent accesses memory

Each attached store is mounted inside the session's container as a directory under `/mnt/memory/`, and the agent reads and writes it with the standard [agent toolset](/docs/en/managed-agents/tools). Writes are persisted back to the store and stay in sync across sessions that share it. A short description of each mount (path, access mode, store `description`, and any `instructions`) is automatically added to the system prompt.

`access` is enforced at the filesystem level: a `read_only` mount rejects writes, while writes to a `read_write` mount produce [memory versions](#audit-memory-changes) attributed to the session.

The agent's reads and writes appear in the [event stream](/docs/en/managed-agents/events-and-streaming) as ordinary `agent.tool_use` and `agent.tool_result` events for whichever tool touched the mount.

## View and edit memories

Memory stores can be managed directly via the API. Use this for building review workflows, correcting bad memories, or seeding stores before any session runs.

### List memories

List the memories in a store, optionally filtered by `path_prefix` to browse a path like a directory:

<CodeGroup>
  
  ```bash curl
  page=$(curl -fsS "https://api.anthropic.com/v1/memory_stores/$store_id/memories?path_prefix=/&order_by=path&depth=2" \
    -H "x-api-key: $ANTHROPIC_API_KEY" \
    -H "anthropic-version: 2023-06-01" \
    -H "anthropic-beta: managed-agents-2026-04-01")
  jq -r '.data[] | "\(.type)  \(.path)"' <<< "$page"
  ```
  
  ```bash CLI nocheck
  ant beta:memory-stores:memories list \
    --memory-store-id "$store_id" \
    --path-prefix "/" --order-by path --depth 2
  ```
  ```python Python
  page = client.beta.memory_stores.memories.list(
      store.id,
      path_prefix="/",
      order_by="path",
      depth=2,
  )
  for item in page.data:
      print(item.type, item.path)
  ```
  ```typescript TypeScript
  const page = await client.beta.memoryStores.memories.list(store.id, {
    path_prefix: "/",
    order_by: "path",
    depth: 2
  });
  for (const item of page.data) {
    console.log(item.type, item.path);
  }
  ```
  ```csharp C#
  var page = await client.Beta.MemoryStores.Memories.List(store.ID, new()
  {
      PathPrefix = "/",
      OrderBy = "path",
      Depth = 2,
  });
  foreach (var item in page.Data)
  {
      Console.WriteLine($"{item.Type.Raw()}  {item.Path}");
  }
  ```
  ```go Go
  	page, err := client.Beta.MemoryStores.Memories.List(ctx, store.ID, anthropic.BetaMemoryStoreMemoryListParams{
  		PathPrefix: anthropic.String("/"),
  		OrderBy:    anthropic.BetaMemoryStoreMemoryListParamsOrderByPath,
  		Depth:      anthropic.Int(2),
  	})
  	if err != nil {
  		panic(err)
  	}
  	for _, item := range page.Data {
  		fmt.Println(item.Type, item.Path)
  	}
  ```
  ```java Java
      var page = client.beta().memoryStores().memories().list(
          store.id(),
          MemoryListParams.builder()
              .pathPrefix("/")
              .orderBy(MemoryListParams.OrderBy.PATH)
              .depth(2L)
              .build()
      );
      for (var item : page.data()) {
          IO.println(item.type() + "  " + item.path());
      }
  ```
  ```php PHP
  $page = $client->beta->memoryStores->memories->list(
      $store->id,
      pathPrefix: '/',
      orderBy: 'path',
      depth: 2,
  );
  foreach ($page->data as $item) {
      echo "{$item->type}  {$item->path}\n";
  }
  ```
  ```ruby Ruby
  page = client.beta.memory_stores.memories.list(
    store.id,
    path_prefix: "/",
    order_by: "path",
    depth: 2
  )
  page.data.each do |entry|
    puts "#{entry.type}  #{entry.path}"
  end
  ```
</CodeGroup>

See the [List memories reference](/docs/en/api/memory-stores-memories-list) for full parameters and response schema.

### Read a memory
Fetching an individual memory returns the full content.

<CodeGroup>
  
  ```bash curl
  mem=$(curl -fsS "https://api.anthropic.com/v1/memory_stores/$store_id/memories/$mem_id" \
    -H "x-api-key: $ANTHROPIC_API_KEY" \
    -H "anthropic-version: 2023-06-01" \
    -H "anthropic-beta: managed-agents-2026-04-01")
  jq -r '.content' <<< "$mem"
  ```
  
  ```bash CLI nocheck
  ant beta:memory-stores:memories retrieve \
    --memory-store-id "$store_id" \
    --memory-id "$mem_id"
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

See the [Retrieve a memory reference](/docs/en/api/memory-stores-memories-retrieve) for full parameters and response schema.

### Create a memory

`memories.create` creates a memory at a given `path`. Create does not overwrite; to change an existing memory, use [`memories.update`](#update-a-memory).

<CodeGroup>
  
  ```bash curl nocheck {-2..-1}
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
  mem_id=$(jq -r '.id' <<< "$mem")
  mem_sha=$(jq -r '.content_sha256' <<< "$mem")
  ```
  
  ```bash CLI nocheck {-2..-1}
  mem=$(ant beta:memory-stores:memories create \
    --memory-store-id "$store_id" \
    --path "/preferences/formatting.md" \
    --content "Always use tabs, not spaces." \
    --format json)
  mem_id=$(jq -r '.id' <<< "$mem")
  mem_sha=$(jq -r '.content_sha256' <<< "$mem")
  ```
  ```python Python
  mem = client.beta.memory_stores.memories.create(
      store.id,
      path="/preferences/formatting.md",
      content="Always use tabs, not spaces.",
  )
  ```
  ```typescript TypeScript
  const mem = await client.beta.memoryStores.memories.create(store.id, {
    path: "/preferences/formatting.md",
    content: "Always use tabs, not spaces."
  });
  ```
  ```csharp C#
  var mem = await client.Beta.MemoryStores.Memories.Create(store.ID, new()
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

See the [Create a memory reference](/docs/en/api/memory-stores-memories-create) for full parameters and response schema.

### Update a memory

`memories.update()` modifies an existing memory by ID. You can change `content`, `path` (a rename), or both. The example renames a memory to an archive path:

<CodeGroup>
  
  ```bash curl
  curl -fsS -X POST "https://api.anthropic.com/v1/memory_stores/$store_id/memories/$mem_id" \
    -H "x-api-key: $ANTHROPIC_API_KEY" \
    -H "anthropic-version: 2023-06-01" \
    -H "anthropic-beta: managed-agents-2026-04-01" \
    -H "content-type: application/json" \
    -d '{"path": "/archive/2026_q1_formatting.md"}' > /dev/null
  ```
  
  ```bash CLI nocheck
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

See the [Update a memory reference](/docs/en/api/memory-stores-memories-update) for full parameters and response schema.

#### Safe content edits (optimistic concurrency)

To avoid clobbering a concurrent write, pass a `content_sha256` precondition. The update only applies if the stored content hash still matches the one you read; on mismatch, re-read the memory and retry against the fresh state.

<CodeGroup>
  
  ```bash curl nocheck
  curl -fsS -X POST "https://api.anthropic.com/v1/memory_stores/$store_id/memories/$mem_id" \
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

### Delete a memory

<CodeGroup>
  
  ```bash curl
  curl -fsS -X DELETE "https://api.anthropic.com/v1/memory_stores/$store_id/memories/$mem_id" \
    -H "x-api-key: $ANTHROPIC_API_KEY" \
    -H "anthropic-version: 2023-06-01" \
    -H "anthropic-beta: managed-agents-2026-04-01" > /dev/null
  ```
  
  ```bash CLI nocheck
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

See the [Delete a memory reference](/docs/en/api/memory-stores-memories-delete) for full parameters and response schema.

## Audit memory changes

Every mutation to a memory creates an immutable **memory version** (`memver_...`). Use the version endpoints to audit who changed what and when, to inspect or restore a prior snapshot, and to scrub sensitive content out of history with redact.

Versions belong to the store (not the individual memory) and survive even after the memory itself is deleted, so the audit trail stays complete. Versions are retained for 30 days; however, the recent versions are always kept regardless of age, so memories that change infrequently may retain history beyond 30 days. The live `memories.retrieve` call always returns the latest version; the version endpoints give you the retained history.

 There is no dedicated restore endpoint; to roll back, retrieve the version you want and write its `content` back with `memories.update` (or `memories.create` if the parent memory has been deleted, since versions outlive their parent).

Past memory versions may be deleted after 30 days. If you'd like to preserve memory history for longer, export versions via the API.

### List versions

List version history for a store, newest first. The example filters to a single memory's history:

<CodeGroup>
  
  ```bash curl nocheck {-1}
  versions=$(curl -fsS "https://api.anthropic.com/v1/memory_stores/$store_id/memory_versions?memory_id=$mem_id" \
    -H "x-api-key: $ANTHROPIC_API_KEY" \
    -H "anthropic-version: 2023-06-01" \
    -H "anthropic-beta: managed-agents-2026-04-01")
  jq -r '.data[] | "\(.id): \(.operation)"' <<< "$versions"
  version_id=$(jq -r '.data[0].id' <<< "$versions")
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

See the [List memory versions reference](/docs/en/api/memory-stores-memory-versions-list) for full parameters and response schema.

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

See the [Retrieve a memory version reference](/docs/en/api/memory-stores-memory-versions-retrieve) for full parameters and response schema.

### Redact a version

Redact scrubs content out of a historical version while preserving the audit trail (who did what, when). Use it for compliance workflows such as removing leaked secrets, PII, or user deletion requests.

A version that is the current head of a live memory cannot be redacted. Write a new version first (or delete the memory), then redact the old one.

<CodeGroup>
  
  ```bash curl nocheck
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

See the [Redact a memory version reference](/docs/en/api/memory-stores-memory-versions-redact) for full parameters and response schema.

## Manage memory stores

In addition to [`create`](/docs/en/api/memory-stores-create), memory stores support [`retrieve`](/docs/en/api/memory-stores-retrieve), [`update`](/docs/en/api/memory-stores-update), [`list`](/docs/en/api/memory-stores-list), [`archive`](/docs/en/api/memory-stores-archive), and [`delete`](/docs/en/api/memory-stores-delete).

### List stores

List stores in the workspace. Archived stores are excluded by default; pass `include_archived: true` to include them.

<CodeGroup>
  ```bash curl
  curl -fsS "https://api.anthropic.com/v1/memory_stores?include_archived=true" \
    -H "x-api-key: $ANTHROPIC_API_KEY" \
    -H "anthropic-version: 2023-06-01" \
    -H "anthropic-beta: managed-agents-2026-04-01" | jq '.data[] | {id, name, archived_at}'
  ```
  
  ```bash CLI nocheck
  ant beta:memory-stores list --include-archived
  ```
  ```python Python
  for s in client.beta.memory_stores.list(include_archived=True):
      print(s.id, s.name, s.archived_at)
  ```
  ```typescript TypeScript
  for await (const s of client.beta.memoryStores.list({ include_archived: true })) {
    console.log(s.id, s.name, s.archived_at);
  }
  ```
  ```csharp C#
  var stores = await client.Beta.MemoryStores.List(new() { IncludeArchived = true });
  await foreach (var s in stores.Paginate())
  {
      Console.WriteLine($"{s.ID} {s.Name} {s.ArchivedAt}");
  }
  ```
  ```go Go
  	stores := client.Beta.MemoryStores.ListAutoPaging(ctx, anthropic.BetaMemoryStoreListParams{
  		IncludeArchived: anthropic.Bool(true),
  	})
  	for stores.Next() {
  		s := stores.Current()
  		fmt.Println(s.ID, s.Name, s.ArchivedAt)
  	}
  	if err := stores.Err(); err != nil {
  		panic(err)
  	}
  ```
  ```java Java
      for (var s : client.beta().memoryStores().list(
          MemoryStoreListParams.builder().includeArchived(true).build()
      ).autoPager()) {
          IO.println(s.id() + " " + s.name() + " " + s.archivedAt());
      }
  ```
  ```php PHP
  foreach ($client->beta->memoryStores->list(includeArchived: true)->pagingEachItem() as $s) {
      echo "{$s->id} {$s->name} {$s->archivedAt}\n";
  }
  ```
  ```ruby Ruby
  client.beta.memory_stores.list(include_archived: true).auto_paging_each do |s|
    puts "#{s.id} #{s.name} #{s.archived_at}"
  end
  ```
</CodeGroup>

See the [List memory stores reference](/docs/en/api/memory-stores-list) for full parameters and response schema.

### Archive a store

Archiving makes a store read-only and prevents it from being attached to new sessions. Archiving is one-way; there is no unarchive.

<CodeGroup>
  
  ```bash curl nocheck
  curl -fsS -X POST "https://api.anthropic.com/v1/memory_stores/$store_id/archive" \
    -H "x-api-key: $ANTHROPIC_API_KEY" \
    -H "anthropic-version: 2023-06-01" \
    -H "anthropic-beta: managed-agents-2026-04-01" > /dev/null
  ```
  
  ```bash CLI nocheck
  ant beta:memory-stores archive --memory-store-id "$store_id"
  ```
  ```python Python
  client.beta.memory_stores.archive(store.id)
  ```
  ```typescript TypeScript
  await client.beta.memoryStores.archive(store.id);
  ```
  ```csharp C#
  await client.Beta.MemoryStores.Archive(store.ID);
  ```
  ```go Go
  	_, err = client.Beta.MemoryStores.Archive(ctx, store.ID)
  	if err != nil {
  		panic(err)
  	}
  ```
  ```java Java
      client.beta().memoryStores().archive(store.id());
  ```
  ```php PHP
  $client->beta->memoryStores->archive($store->id);
  ```
  ```ruby Ruby
  client.beta.memory_stores.archive(store.id)
  ```
</CodeGroup>

See the [Archive a memory store reference](/docs/en/api/memory-stores-archive) for full parameters and response schema.

To permanently remove a store along with all of its memories and versions, use [`memory_stores.delete`](/docs/en/api/memory-stores-delete).

## Limits

The following limits apply while this feature is in beta. [Contact support](https://support.claude.com) if you need higher limits.

| Limit | Value |
| --- | --- |
| Memory stores per organization | 1,000 |
| Memories per store | 2,000 |
| Total storage per store | 100 MB (104,857,600 bytes) |
| Versions per store | 250,000 |
| Size per memory | 100 kB (102,400 bytes) |
| Version history retention | 30 days |
| Memory stores per session | 8 |
| `instructions` field per attachment | 4,096 characters |