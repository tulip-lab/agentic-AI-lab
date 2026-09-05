[![GitHub issues](https://img.shields.io/github/issues/tulip-lab/agentic-AI-lab)](https://github.com/tulip-lab/agentic-AI-lab/issues)
[![GitHub pull requests](https://img.shields.io/github/issues-pr/tulip-lab/agentic-AI-lab)](https://github.com/tulip-lab/agentic-AI-lab/pulls)
[![GitHub stars](https://img.shields.io/github/stars/tulip-lab/agentic-AI-lab.svg?style=social&label=Star)](https://github.com/tulip-lab/agentic-AI-lab)

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

| Module | Category | Topic | Learning transition |
| :----: | :---: | ------- | ------- |
| M01 | Preliminary | Foundations | From Python and safe inputs to LLM, API and tool-call mental models. |
| M02 | Preliminary | Prompt Engineering and RAG | From writing prompts to testing them as specifications and grounding answers in retrieved evidence. |
| M03 | Core | Context Engineering and Agent Orchestration | From text-only concepts to visible Flowise workflows with memory, retrieval, tools and exposure controls. |
| M04 | Core | LangChain Programming | From visual workflows to inspectable Python chains, tools, state-changing actions and evidence-grounded drafting. |
| M05 | Core | Knowledge Agents and Stateful Workflows | From individual components to knowledge-grounded, stateful and human-confirmed workflows. |
| M06 | Core | Multi-Agent Systems and Safety | From one workflow to collaborating roles, prompt-injection defence, private runtimes and governance. |
| M07 | Advanced | Model Adaptation and Multimodal GenAI | From orchestrating existing models to evaluating adaptation, forgetting, multimodal generation and inference trade-offs. |
| M08 | Advanced | Agent Engineering | From lab prototypes to evaluation, coding-agent practice, productisation, MCP and workflow guards. |

## Learning Path and Prerequisites

The default path is sequential: complete the preliminary modules before the core modules, then use the advanced modules to compare and integrate the design patterns. Each module deliberately reuses a concept from earlier work in a more capable setting.

- Complete M01 before any API-backed or tool-using lab; its secret-handling and validation patterns apply throughout the unit.
- Complete M02 before M03C or M05A–M05B; those sessions assume you can distinguish retrieval quality from answer quality.
- Complete M03X before the remaining M03 sessions. M03A–M03D form a progression from visible information flow to memory, retrieval and safe tool use; M03E reviews one completed workflow at the deployment boundary. M03F is an optional local-model branch after M03B and prepares students for the privacy-boundary analysis in M06C.
- Complete M04A before M04B–M04D. M04B introduces tool routing, M04C adds state-changing actions, and M04D combines retrieval with controlled writing.
- Complete M05C before M06A; explicit workflow state makes multi-agent hand-offs and failure branches easier to reason about.
- Treat M07 and M08 as advanced labs. They assume you can inspect evidence, define a safety boundary and test normal, edge or missing-information, and failure or refusal behaviour.

## Practical Learning Pattern

Most sessions are designed for approximately two hours and use the same learning rhythm:

1. establish the purpose, expected output and prior connection;
2. run or build a small deterministic baseline;
3. inspect intermediate state, evidence, parameters or traces;
4. test normal, edge or missing-information, and failure or safety behaviour;
5. extend the baseline through clearly separated student tasks; and
6. restart and run from the top, complete quality checks, and reflect on transfer to the next session.

Optional API, model or package sections are extensions, not prerequisites for completing the core learning outcome. When a live service is unavailable, students should record the documented skipped result and continue with the mandatory local path.

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
|  | M03F | Flowise with Local Models through Ollama (Optional) | `M03-Context-Orchestration/Flowise/M03F-Flowise-Ollama-Local-Models.md` |
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
- Flowise setup, visual workflow construction, chatbot workflows, RAG, AgentFlow and an optional Ollama local-model path.
- Tool integration, custom tools, local storage and action execution.
- RAG over public course documents and public datasets.
- Hosting, web embedding and UI integration.
- Copilot-style assistants with vision and task execution.
- Private and open-source agents using local LLMs.
- Agent safety, prompt injection, data poisoning and legal risk.
- Productised AI agents, customer workflows and go-to-market thinking.

## Demonstration Guidance

For a live walkthrough, demonstrate the shortest complete story rather than every optional branch: state the intended output, run the baseline, inspect one intermediate trace, compare a normal case with one refusal or insufficient-context case, then show the student extension point. Use the existing recorded or mock path when network access, quota or credentials would make a live API call unreliable.

The strongest cross-module demonstration sequence is M02C (transparent RAG), M03C (the same architecture on a visual canvas), M05A (the architecture rebuilt in Python) and M08A (evaluation of workflow behaviour). For tools, use M01C, M03D, M04B, M05C and M08E to show the progression from a proposed tool call to validation, explicit state transitions and pre/post execution guards.

## Assessment and Responsible Use

Session tasks are formative unless an offering-specific brief states otherwise. Students should submit the evidence named in each lab: completed code or workflow, test results, relevant traces or screenshots, limitations and reflection. Offering-specific assessment packages are listed in [Assignments/README.md](Assignments/README.md); submission dates, weighting and LMS details are supplied separately for each teaching offering.

All work must use approved public or synthetic material. Do not upload private files, student records, credentials, instructor-only content or unpublished assessment material to notebooks, model providers, Flowise, repositories or screenshots. A successful refusal, abstention or skipped optional section is valid evidence when it demonstrates the required boundary honestly.
