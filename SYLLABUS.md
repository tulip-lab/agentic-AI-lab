[![GitHub issues](https://img.shields.io/github/issues/tulip-lab/agentic-AI-lab)](https://github.com/tulip-lab/agentic-AI-lab/issues)
[![GitHub pull requests](https://img.shields.io/github/issues-pr/tulip-lab/agentic-AI-lab)](https://github.com/tulip-lab/agentic-AI-lab/pulls)
[![GitHub stars](https://img.shields.io/github/stars/tulip-lab/agentic-AI-lab.svg?style=social&label=Star)](https://github.com/tulip-lab/agentic-AI-lab/stargazers/)

---

![FLIP Banner](Assets/images/flip-banner.png)

# FLIP: Agentic AI in Practice

**FLIP** stands for **Fundamentals of Learning and Intelligent Processing**.

This syllabus summarises the module structure, session schedule, learning progression and public data policy for the student-facing practical materials.

---

- Materials in this repository support practical learning in generative AI and agentic AI systems.
- Public course documents and public datasets should be used wherever possible in exercises.
- Public data for simple practical tasks should preferably come from [tulip-lab/open-data](https://github.com/tulip-lab/open-data).
- If you find an issue or bug, please submit an issue in [this repository](https://github.com/tulip-lab/agentic-AI-lab/issues).
- Pull requests that improve clarity, reproducibility or safety are welcome.
- Point of contact: [Prof. Gang Li](https://github.com/tuliplab)

Prepared by :tulip: **[TULIP Lab](https://www.tulip.academy), Australia**

---

# Syllabus

This document keeps the eight-module structure and expands the session coverage to include applied agentic AI themes: Flowise setup, first agents, function calling, tool use, local storage, RAG, hosting, copilot-style assistants, open-source local agents, productisation and responsible deployment.

## Data and Document Policy

Labs should preferentially use:

1. Public materials in this course repository, including `README.md`, `SYLLABUS.md`, public notebooks and public Markdown tutorials.
2. Public datasets from [tulip-lab/open-data](https://github.com/tulip-lab/open-data).
3. Small synthetic examples generated inside the notebook.
4. External public data only when necessary.

Do not use private files, student submissions, instructor-only notes, reference solutions, unpublished assessment material or credentials.

## Module Overview

| Module | Category | Topic |
| :----: | :---: | ------- |
| M01 | Preliminary | Foundations |
| M02 | Preliminary | Prompt Engineering and RAG |
| M03 | Core | Context Engineering and Agent Orchestration |
| M04 | Core | LangChain Programming |
| M05 | Core | Knowledge Agents and Stateful Workflows |
| M06 | Core | Multi-Agent Systems and Safety |
| M07 | Advanced | Model Adaptation and Multimodal GenAI |
| M08 | Advanced | Advanced Agentic AI |

## Session Schedule

| Module | Session | Session Title | Public File |
| ------- | :---: | ------- | ------- |
| M01: Foundations | M01A | Python, Colab and API Safety | `M01-Foundations/Jupyter/M01A-Python-Colab-API-Safety.ipynb` |
|  | M01B | GenAI and Agentic AI Fundamentals | `M01-Foundations/Jupyter/M01B-GenAI-Fundamentals.ipynb` |
|  | M01C | LLMs, Function Calling, APIs and Agent Ecosystems | `M01-Foundations/Jupyter/M01C-LLMs-FunctionCalling-APIs.ipynb` |
| M02: Prompt Engineering and RAG | M02A | Prompt Foundations | `M02-Prompt-RAG/Jupyter/M02A-Prompt-Foundations.ipynb` |
|  | M02B | Prompt Engineering as a Control Loop | `M02-Prompt-RAG/Jupyter/M02B-Prompt-Engineering-Control-Loop.ipynb` |
|  | M02C | Retrieval-Augmented Generation | `M02-Prompt-RAG/Jupyter/M02C-Retrieval-Augmented-Generation.ipynb` |
| M03: Context Engineering and Agent Orchestration | M03X | Flowise Environment Setup | `M03-Context-Orchestration/Flowise/M03X-Flowise-Environment-Setup.md` |
|  | M03A | Interface and First Chatflow | `M03-Context-Orchestration/Flowise/M03A-Flowise-Interface-First-Chatflow.md` |
|  | M03B | Chatbot Prompting and Memory | `M03-Context-Orchestration/Flowise/M03B-Flowise-Chatbot-Prompt-Memory.md` |
|  | M03C | RAG over Public Unit Documents | `M03-Context-Orchestration/Flowise/M03C-Flowise-RAG-Public-Unit-Docs.md` |
|  | M03D | AgentFlow with Safe Tools | `M03-Context-Orchestration/Flowise/M03D-Flowise-AgentFlow-Safe-Tools.md` |
|  | M03E | Embedding, API and Deployment Readiness | `M03-Context-Orchestration/Flowise/M03E-Flowise-Embed-API-Deployment-Readiness.md` |
| M04: LangChain Programming | M04A | LangChain Fundamentals | `M04-Agent-Programming/Jupyter/M04A-LangChain-Fundamentals.ipynb` |
|  | M04B | LangChain Tool-Using Agents | `M04-Agent-Programming/Jupyter/M04B-LangChain-ToolAgents.ipynb` |
|  | M04C | Custom Tools, Local Storage and Action Execution | `M04-Agent-Programming/Jupyter/M04C-CustomTools-Storage-Actions.ipynb` |
|  | M04D | Lead Research and Personalised Writing Agent | `M04-Agent-Programming/Jupyter/M04D-LeadResearch-WritingAgent.ipynb` |
| M05: Knowledge Agents and Stateful Workflows | M05A | Basic RAG System | `M05-Knowledge-Agents/Jupyter/M05A-Basic-RAG-System.ipynb` |
|  | M05B | RAG Domain Assistant using Course Materials | `M05-Knowledge-Agents/Jupyter/M05B-RAG-CourseMaterials-Assistant.ipynb` |
|  | M05C | LangGraph Stateful Workflows | `M05-Knowledge-Agents/Jupyter/M05C-LangGraph-StatefulWorkflows.ipynb` |
|  | M05D | Copilot-Style Assistant with Vision and Task Execution | `M05-Knowledge-Agents/Jupyter/M05D-Copilot-Vision-TaskExecution.ipynb` |
| M06: Multi-Agent Systems and Safety | M06A | Multi-Agent Collaboration | `M06-Multi-Agent-Safety/Jupyter/M06A-MultiAgent-Collaboration.ipynb` |
|  | M06B | LLM Malicious Instruction and Prompt Injection Defence | `M06-Multi-Agent-Safety/Jupyter/M06B-LLM-Malicious-Instruction-Defense.ipynb` |
|  | M06C | Private Agents with Open-Source LLMs and Ollama | `M06-Multi-Agent-Safety/Jupyter/M06C-PrivateAgents-Ollama.ipynb` |
|  | M06D | Agent Security, Data Poisoning and Legal Risks | `M06-Multi-Agent-Safety/Jupyter/M06D-AgentSecurity-LegalRisks.ipynb` |
| M07: Model Adaptation and Multimodal GenAI | M07A | Fine-Tuning LLMs | `M07-Model-Adaptation/Jupyter/M07A-Finetuning-LLM.ipynb` |
|  | M07B | Fine-Tuning and Forgetting | `M07-Model-Adaptation/Jupyter/M07B-Finetuning-Forgetting.ipynb` |
|  | M07C | Diffusion Customization | `M07-Model-Adaptation/Jupyter/M07C-Diffusion-Customization.ipynb` |
|  | M07D | Speech Generation | `M07-Model-Adaptation/Jupyter/M07D-Speech-Generation.ipynb` |
|  | M07E | Fast Inference and Model Provider Comparison | `M07-Model-Adaptation/Jupyter/M07E-FastInference-ProviderComparison.ipynb` |
| M08: Advanced Agentic AI | M08A | Hugging Face Evaluation | `M08-Agent-Engineering/Jupyter/M08A-HuggingFace-Evaluation.ipynb` |
|  | M08B | Codex Codebase Understanding and Development | `M08-Agent-Engineering/Codex/M08B-Codex-Codebase-Understanding-and-Development.md` |
|  | M08C | Productised AI Agents and Go-to-Market Checklist | `M08-Agent-Engineering/Codex/M08C-Productised-AIAgents-GoToMarket.md` |
|  | M08D | MCP Fundamentals and Tool Context Servers | `M08-Agent-Engineering/Jupyter/M08D-MCP-Fundamentals-ToolContextServers.ipynb` |
|  | M08E | Agent Hooks and Workflow Guards | `M08-Agent-Engineering/Jupyter/M08E-Agent-Hooks-WorkflowGuards.ipynb` |

## Theme Mapping

The expanded schedule covers the following applied themes:

- Agentic AI foundations, LLMs, APIs and function calling.
- Flowise setup, visual workflow construction, chatbot workflows, RAG and AgentFlow.
- Tool integration, custom tools, local storage and action execution.
- RAG over public course documents and public datasets.
- Hosting, web embedding and UI integration.
- Copilot-style assistants with vision and task execution.
- Private and open-source agents using local LLMs.
- Agent safety, prompt injection, data poisoning and legal risk.
- Productised AI agents, customer workflows and go-to-market thinking.
