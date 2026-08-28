[![GitHub issues](https://img.shields.io/github/issues/tulip-lab/agentic-AI-lab)](https://github.com/tulip-lab/agentic-AI-lab/issues)
[![GitHub pull requests](https://img.shields.io/github/issues-pr/tulip-lab/agentic-AI-lab)](https://github.com/tulip-lab/agentic-AI-lab/pulls)
[![GitHub stars](https://img.shields.io/github/stars/tulip-lab/agentic-AI-lab.svg?style=social&label=Star)](https://github.com/tulip-lab/agentic-AI-lab/stargazers/)

---

![FLIP Banner](Assets/images/flip-banner.png)

# FLIP: Agentic AI in Practice

**FLIP** stands for **Fundamentals of Learning and Intelligent Processing**.

This repository contains student-facing practical materials for building generative and agentic AI systems through Python notebooks, visual workflows, retrieval-augmented generation, multi-agent systems, model adaptation, evaluation and coding-agent practice.

---

- Materials in this repository support practical learning in generative AI and agentic AI systems.
- Public course documents and public datasets should be used wherever possible in exercises.
- Public data for simple practical tasks should preferably come from [tulip-lab/open-data](https://github.com/tulip-lab/open-data).
- If you find an issue or bug, please submit an issue in [this repository](https://github.com/tulip-lab/agentic-AI-lab/issues).
- Pull requests that improve clarity, reproducibility or safety are welcome.
- Point of contact: [Prof. Gang Li](https://github.com/tuliplab)

Prepared by :tulip: **[TULIP Lab](https://www.tulip.academy), Australia**

---

## Unit Materials

This repository contains the public practical materials for **FLIP: Agentic AI in Practice**.

The detailed schedule, learning outcomes, practical structure, assessment guidance and responsible-use requirements are available in [SYLLABUS.md](SYLLABUS.md).

Instructor-only materials, reference solutions, rubrics and teaching notes are maintained separately in the private instructor repository.

---

## Data and Documents for Labs

When a lab requires documents or data, use the following source order:

1. Public materials in this repository, such as `README.md`, `SYLLABUS.md`, public Markdown handouts and public notebook text.
2. Public datasets from [tulip-lab/open-data](https://github.com/tulip-lab/open-data).
3. Small synthetic examples created inside the notebook or tutorial.
4. External public data only when the lab objective cannot be achieved with the first three options.

More details are available in the [Data policy](Data/README.md).

---

## Recommended Platforms

- [Google Colab](https://colab.research.google.com): Python notebook practical sessions.
- [Flowise](https://flowiseai.com): visual construction of chatbot, RAG and agent workflows.
- [Hugging Face](https://huggingface.co): open-source models, embeddings and evaluation activities.
- [GitHub](https://github.com): repository access, version control and project submission.
- Local tools such as Ollama or VS Code may be used in selected advanced sessions where explicitly stated.

---

## Modules

| Module | Category | Topic | Module Materials |
| :----: | :---: | ------- | :----- |
| :one: | Preliminary | [Foundations](https://github.com/tulip-lab/agentic-AI/tree/develop/M01-Foundations/README.md) | <ul><li>[M01A-Python-Colab-API-Safety](M01-Foundations/Jupyter/M01A-Python-Colab-API-Safety.ipynb)</li><li>[M01B-GenAI-Fundamentals](M01-Foundations/Jupyter/M01B-GenAI-Fundamentals.ipynb)</li><li>[M01C-LLMs-FunctionCalling-APIs](M01-Foundations/Jupyter/M01C-LLMs-FunctionCalling-APIs.ipynb)</li></ul> |
| :two: | Preliminary | [Prompt Engineering and RAG](https://github.com/tulip-lab/agentic-AI/tree/develop/M02-Prompt-RAG/README.md) | <ul><li>[M02A-Prompt-Foundations](M02-Prompt-RAG/Jupyter/M02A-Prompt-Foundations.ipynb)</li><li>[M02B-Prompt-Engineering-Control-Loop](M02-Prompt-RAG/Jupyter/M02B-Prompt-Engineering-Control-Loop.ipynb)</li><li>[M02C-Retrieval-Augmented-Generation](M02-Prompt-RAG/Jupyter/M02C-Retrieval-Augmented-Generation.ipynb)</li></ul> |
| :three: | Core | [Context Engineering and Agent Orchestration](https://github.com/tulip-lab/agentic-AI/tree/develop/M03-Context-Orchestration/README.md) | <ul><li>[M03X-Flowise-Environment-Setup](M03-Context-Orchestration/Flowise/M03X-Flowise-Environment-Setup.md)</li><li>[M03A-Flowise-Interface-First-Chatflow](M03-Context-Orchestration/Flowise/M03A-Flowise-Interface-First-Chatflow.md)</li><li>[M03B-Flowise-Chatbot-Prompt-Memory](M03-Context-Orchestration/Flowise/M03B-Flowise-Chatbot-Prompt-Memory.md)</li><li>[M03C-Flowise-RAG-Public-Unit-Docs](M03-Context-Orchestration/Flowise/M03C-Flowise-RAG-Public-Unit-Docs.md)</li><li>[M03D-Flowise-AgentFlow-Safe-Tools](M03-Context-Orchestration/Flowise/M03D-Flowise-AgentFlow-Safe-Tools.md)</li><li>[M03E-Flowise-Embed-API-Deployment-Readiness](M03-Context-Orchestration/Flowise/M03E-Flowise-Embed-API-Deployment-Readiness.md)</li></ul> |
| :four: | Core | [LangChain Programming](https://github.com/tulip-lab/agentic-AI/tree/develop/M04-Agent-Programming/README.md) | <ul><li>[M04A-LangChain-Fundamentals](M04-Agent-Programming/Jupyter/M04A-LangChain-Fundamentals.ipynb)</li><li>[M04B-LangChain-ToolAgents](M04-Agent-Programming/Jupyter/M04B-LangChain-ToolAgents.ipynb)</li><li>[M04C-CustomTools-Storage-Actions](M04-Agent-Programming/Jupyter/M04C-CustomTools-Storage-Actions.ipynb)</li><li>[M04D-LeadResearch-WritingAgent](M04-Agent-Programming/Jupyter/M04D-LeadResearch-WritingAgent.ipynb)</li></ul> |
| :five: | Core | [Knowledge Agents and Stateful Workflows](https://github.com/tulip-lab/agentic-AI/tree/develop/M05-Knowledge-Agents/README.md) | <ul><li>[M05A-Basic-RAG-System](M05-Knowledge-Agents/Jupyter/M05A-Basic-RAG-System.ipynb)</li><li>[M05B-RAG-CourseMaterials-Assistant](M05-Knowledge-Agents/Jupyter/M05B-RAG-CourseMaterials-Assistant.ipynb)</li><li>[M05C-LangGraph-StatefulWorkflows](M05-Knowledge-Agents/Jupyter/M05C-LangGraph-StatefulWorkflows.ipynb)</li><li>[M05D-Copilot-Vision-TaskExecution](M05-Knowledge-Agents/Jupyter/M05D-Copilot-Vision-TaskExecution.ipynb)</li></ul> |
| :six: | Core | [Multi-Agent Systems and Safety](https://github.com/tulip-lab/agentic-AI/tree/develop/M06-Multi-Agent-Safety/README.md) | <ul><li>[M06A-MultiAgent-Collaboration](M06-Multi-Agent-Safety/Jupyter/M06A-MultiAgent-Collaboration.ipynb)</li><li>[M06B-LLM-Malicious-Instruction-Defense](M06-Multi-Agent-Safety/Jupyter/M06B-LLM-Malicious-Instruction-Defense.ipynb)</li><li>[M06C-PrivateAgents-Ollama](M06-Multi-Agent-Safety/Jupyter/M06C-PrivateAgents-Ollama.ipynb)</li><li>[M06D-AgentSecurity-LegalRisks](M06-Multi-Agent-Safety/Jupyter/M06D-AgentSecurity-LegalRisks.ipynb)</li></ul> |
| :seven: | Advanced | [Model Adaptation and Multimodal GenAI](https://github.com/tulip-lab/agentic-AI/tree/develop/M07-Model-Adaptation/README.md) | <ul><li>[M07A-Finetuning-LLM](M07-Model-Adaptation/Jupyter/M07A-Finetuning-LLM.ipynb)</li><li>[M07B-Finetuning-Forgetting](M07-Model-Adaptation/Jupyter/M07B-Finetuning-Forgetting.ipynb)</li><li>[M07C-Diffusion-Customization](M07-Model-Adaptation/Jupyter/M07C-Diffusion-Customization.ipynb)</li><li>[M07D-Speech-Generation](M07-Model-Adaptation/Jupyter/M07D-Speech-Generation.ipynb)</li><li>[M07E-FastInference-ProviderComparison](M07-Model-Adaptation/Jupyter/M07E-FastInference-ProviderComparison.ipynb)</li></ul> |
| :eight: | Advanced | [Agent Engineering](https://github.com/tulip-lab/agentic-AI/tree/develop/M08-Agent-Engineering/README.md) | <ul><li>[M08A-HuggingFace-Evaluation](M08-Agent-Engineering/Jupyter/M08A-HuggingFace-Evaluation.ipynb)</li><li>[M08B-Codex-Codebase-Understanding-and-Development](M08-Agent-Engineering/Codex/M08B-Codex-Codebase-Understanding-and-Development.md)</li><li>[M08C-Productised-AIAgents-GoToMarket](M08-Agent-Engineering/Codex/M08C-Productised-AIAgents-GoToMarket.md)</li><li>[M08D-MCP-Fundamentals-ToolContextServers](M08-Agent-Engineering/Jupyter/M08D-MCP-Fundamentals-ToolContextServers.ipynb)</li><li>[M08E-Agent-Hooks-WorkflowGuards](M08-Agent-Engineering/Jupyter/M08E-Agent-Hooks-WorkflowGuards.ipynb)</li></ul> |

---

## Software and Environment Requirements

Most Python notebooks are designed to run in Google Colab. Individual notebooks may install only the packages required for that session.

For local setup, install the common Python dependencies with:

```bash
pip install -r requirements.txt
```

Students are not required to install all packages at the beginning of the unit. Flowise, Codex, Ollama and local deployment tools are used separately and are not installed through `requirements.txt`.

Some sessions require API keys for external model providers. Do not hard-code API keys in notebooks, scripts, Markdown files, Flowise exports, screenshots or logs. Use Google Colab Secrets, environment variables, or temporary input through `getpass`.

---

## Public Repository Safety

This repository is public. Do not commit API keys, tokens, passwords, `.env` files, private credentials, private datasets, student submissions, unpublished assessment solutions, large model weights, local runtime outputs, generated caches or instructor-only materials.

Reference solutions and teaching notes must be kept in the private instructor repository.

---

## Lab Session Screencasts

Screencasts and supplementary demonstrations may be published through [TULIP Lab on YouTube](https://www.youtube.com/@tuliplab).

---

## Licensing

Teaching content and code use separate licences. See [LICENSING.md](LICENSING.md) for the exact scope, attribution requirements, and exclusions.

---

## Contributors

Thanks goes to these wonderful people :tulip:

<a href="https://github.com/tulip-lab/agentic-AI-lab/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=tulip-lab/agentic-AI-lab" />
</a>

Made with [contributors-img](https://contrib.rocks).
