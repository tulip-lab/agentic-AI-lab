# M03 Flowise labs: shared technical pathway

These labs are the English, offering-independent M03 pathway. Begin with a working Flowise instance, build a minimal chatflow, then add context, memory, retrieval, a bounded tool, and a review of sharing controls. The examples use fictional public data; no faculty-specific course design or private teaching material is needed.

| Order | Lab | Main evidence |
| --- | --- | --- |
| 0 | [M03X — environment and model connection](M03X-Flowise-Environment-Setup.md) | A persistent Flowise instance and a successful model reply |
| 1 | [M03A — first Chatflow](M03A-Flowise-Interface-First-Chatflow.md) | Correct node connections and three behaviour tests |
| 2 | [M03B — prompt, context, and memory](M03B-Flowise-Chatbot-Prompt-Memory.md) | Controlled comparisons with and without context/history |
| 3 | [M03C — RAG over public documents](M03C-Flowise-RAG-Public-Unit-Docs.md) | Non-zero indexing, retrieved evidence, and grounded answers |
| 4 | [M03D — Agentflow and a safe tool](M03D-Flowise-AgentFlow-Safe-Tools.md) | A visible tool call, parameters, result, and boundary tests |
| 5 | [M03E — embed/API readiness](M03E-Flowise-Embed-API-Deployment-Readiness.md) | A local access and data-boundary review |
| Optional | [M03F — Ollama local models](M03F-Flowise-Ollama-Local-Models.md) | Local embeddings or a local chat-model comparison |

M03C uses two downloadable files: the [sample outline](examples/public-course-outline.md) and the [monthly-report case](examples/public-salary-case.md). The default low-cost path is DeepSeek for generation and a small Ollama model for embeddings. A fully local chat comparison is optional. Each lab identifies its node settings, expected observations, normal and failure tests, and evidence to keep.

The screenshots show Flowise 3.1.3 running on a local machine. A credential's display name is only a local label; use your own credential. Interface labels may move in other versions, so follow the named fields and verify the resulting execution trace. The [runtime templates](runtime/) belong in a private working directory once copied; never place a real .env file or API key in this repository.

For an educator-specific application of these shared concepts, see the separate [Faculty F02 practice](../../Faculty/F02-AI-Engineering/practice.zh-CN.md).
