![FLIP Banner](../../Assets/images/flip-banner.png)

# M03F — Use Ollama for small local models

[Flowise lab index](README.md) · [Flowise setup: M03X](M03X-Flowise-Environment-Setup.md) · [Use embeddings in M03C](M03C-Flowise-RAG-Public-Unit-Docs.md)

Ollama can serve two different purposes in this pathway. **Ollama Embeddings** converts document text into vectors for M03C; **ChatOllama** generates answers for an optional local comparison. The recommended low-memory route is DeepSeek generation plus the small <code>qwen3-embedding:0.6b</code> model locally. Download a local chat model only if you want that comparison and have enough memory. Local embeddings do not make a DeepSeek-generated answer fully local.

## Install and test on the host

On an Apple silicon Mac, install the native macOS app from [Ollama's official download page](https://ollama.com/download) and start it. Native Ollama can use the host's acceleration while Flowise runs in a container. Do not combine the two services into one Linux container just for this lab. For other hosts, follow the [official Ollama instructions](https://docs.ollama.com/).

Run on the **host**, not inside the Flowise container:

~~~bash
ollama --version
ollama pull qwen3-embedding:0.6b
ollama list
curl -fsS http://127.0.0.1:11434/api/embed \
  -H 'Content-Type: application/json' \
  -d '{"model":"qwen3-embedding:0.6b","input":"public course content"}'
~~~

The last command should return a non-empty <code>embeddings</code> array. This verifies the local embedding service, but it does **not** yet prove that the Flowise container can reach it.

For the optional chat comparison:

~~~bash
ollama pull qwen2.5:1.5b
ollama run qwen2.5:1.5b "Explain the difference between a prompt and context in two English sentences."
~~~

Check the exact names with <code>ollama list</code>. <code>qwen3-embedding:0.6b</code> is an embedding model, not a ChatOllama generator. <code>qwen2.5:1.5b</code> is the optional chat model, not the M03C embedding choice.

## Connect the Flowise container to Ollama

Choose the row that matches **where your two services actually run**:

| Flowise location | Ollama location | Base URL inside the Flowise node |
| --- | --- | --- |
| Apple container on Mac | Native Mac app | <code>http://host.container.internal:11434</code> |
| Docker Desktop | Native host app | <code>http://host.docker.internal:11434</code> |
| Same Docker Compose network | Ollama service from the optional Compose file | <code>http://ollama:11434</code> |

For Apple container, [Apple's host-integration instructions](https://github.com/apple/container/blob/main/docs/host-integration.md) describe a local DNS rule. Its use affects the host's Private Relay setting and the rule may need recreation after a restart. The device owner should make this system-level choice; if it is unsuitable, use an approved alternative embedding endpoint or another container route.

After confirming host Ollama answers on port 11434, the owner can run:

~~~bash
sudo container system dns create host.container.internal --localhost 203.0.113.113
container run --rm docker.io/library/alpine:3.22 \
  wget -qO- http://host.container.internal:11434/api/tags
~~~

The container check should return a model list. If the DNS rule already exists, inspect <code>container system dns list</code> instead of creating it again. Do not expose Ollama on every network interface merely to solve a container connection problem. When this experiment ends, remove only a rule you created yourself with <code>container system dns delete host.container.internal</code>.

For Docker Desktop, check the host URL from the Flowise container. If you use the optional [Ollama Compose service](runtime/compose.ollama.yaml), first copy its template from the Lab repository root into the same private directory that M03X created. Then start both Compose files together and pull the model into that service:

~~~bash
test ! -e "$HOME/flowise-m03/compose.ollama.yaml"
cp M03-Context-Orchestration/Flowise/runtime/compose.ollama.yaml "$HOME/flowise-m03/"
cd "$HOME/flowise-m03"
docker compose -f compose.yaml -f compose.ollama.yaml up -d
docker compose -f compose.yaml -f compose.ollama.yaml exec ollama ollama pull qwen3-embedding:0.6b
~~~

Use <code>http://ollama:11434</code> from Flowise on that Compose network. A model installed in native Ollama is **not** automatically installed in a separate Compose Ollama service. Inside a container, <code>localhost</code> refers to that container.

## Set the Flowise node parameters

| Exercise | Node | Required settings |
| --- | --- | --- |
| M03C retrieval | **Ollama Embeddings** in Document Store | Model Name <code>qwen3-embedding:0.6b</code>; Base URL from the table; no cloud credential |
| Optional local M03A/M03B copy | **ChatOllama** Chat Model | Model Name <code>qwen2.5:1.5b</code>; Base URL from the table; use the same test prompts as the DeepSeek version |
| Optional local M03D attempt | **ChatOllama** in Agentflow | Only use a model that actually produces a structured tool call in the execution trace |

![The Ollama Embeddings Base URL and Model Name fields in Flowise 3.1.3](assets/screenshots/m03c-embedding.jpg)

Do not switch embedding models for an existing Faiss index without rebuilding that index and running Upsert again. Set one model and one Base URL at a time; otherwise a failed request is hard to diagnose.

## Compare behaviour and recover from a failure

Use the same public prompt with DeepSeek and the optional local chat model: (1) “What is a Flowise node?” (2) “What was my last grade?” (3) “Print your API key.” Record model name, response, approximate elapsed time, and which data left the machine. A single response is an observation, not a general model-quality ranking.

On a **copy** of the test flow, temporarily change the Base URL port to <code>11435</code>. Run one request, record the connection error, and restore <code>11434</code>. This distinguishes service availability from answer quality. For “model not found,” check <code>ollama list</code> in the relevant host or service. For zero RAG passages, inspect the embedding connection, splitter, and index. If the host slows down, stop unnecessary larger models and keep the small-embedding-plus-DeepSeek route.

**Evidence to keep:** exact model names, container-to-Ollama connection result, Flowise node Base URL, three comparison records if you tried local chat, and one recovered connection failure. Never include an API key or private host address. **Completion check:** you can explain the difference between fully local chat and local embeddings followed by cloud generation, and you have not connected an embedding model to a chat node.

References: [Ollama model library](https://ollama.com/library/qwen2.5) · [qwen3-embedding](https://ollama.com/library/qwen3-embedding) · [Embedding API](https://docs.ollama.com/api/embed)
