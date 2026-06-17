[![GitHub issues](https://img.shields.io/github/issues/tulip-lab/agentic-ai)](https://github.com/tulip-lab/agentic-ai/issues)
[![GitHub pull requests](https://img.shields.io/github/issues-pr/tulip-lab/agentic-ai)](https://github.com/tulip-lab/agentic-ai/pulls)
[![GitHub stars](https://img.shields.io/github/stars/tulip-lab/agentic-ai.svg?style=social&label=Star)](https://github.com/tulip-lab/agentic-ai/stargazers/)

---

![FLIP Banner](Assets/images/flip-banner.png)

# FLIP: Agentic AI in Practice

**FLIP** stands for **Fundamentals of Learning and Intelligent Processing**.

This syllabus summarises the module structure, session schedule, learning progression and public data policy for the student-facing practical materials.

---

- Materials in this repository support practical learning in generative AI and agentic AI systems.
- Public course documents and public datasets should be used wherever possible in exercises.
- Public data for simple practical tasks should preferably come from [tulip-lab/open-data](https://github.com/tulip-lab/open-data).
- If you find an issue or bug, please submit an issue at [tulip-lab/agentic-ai](https://github.com/tulip-lab/agentic-ai/issues).
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
| M02 | Preliminary | AI Modelling Basics |
| M03 | Core | Visual Workflows with Flowise |
| M04 | Core | LangChain Programming |
| M05 | Core | Knowledge Agents and Stateful Workflows |
| M06 | Core | Multi-Agent Systems and Safety |
| M07 | Advanced | Model Adaptation and Multimodal GenAI |
| M08 | Advanced | Advanced Agentic AI |

## Session Schedule

| Module | Session | Session Title | Public File |
| ------- | :---: | ------- | ------- |
| M01: Foundations | 1A | Python, Colab and API Safety | `Jupyter/M01-Foundations/M01A-Python-Colab-API-Safety.ipynb` |
|  | 1B | GenAI and Agentic AI Fundamentals | `Jupyter/M01-Foundations/M01B-GenAI-Fundamentals.ipynb` |
|  | 1C | LLMs, Function Calling, APIs and Agent Ecosystems | `Jupyter/M01-Foundations/M01C-LLMs-FunctionCalling-APIs.ipynb` |
| M02: AI Modelling Basics | 2A | Regression and ML Basics | `Jupyter/M02-AIModeling/M02A-Regression-ML-Basics.ipynb` |
|  | 2B | Deep Learning Image Classification | `Jupyter/M02-AIModeling/M02B-DeepLearning-ImageClassification.ipynb` |
|  | 2C | Embeddings, Vector Data and Similarity Search | `Jupyter/M02-AIModeling/M02C-Embeddings-VectorData-Similarity.ipynb` |
| M03: Visual Workflows with Flowise | 3A | Flowise Environment Setup and Interface | `Flowise/M03-VisualWorkflows/M03A-Flowise-Setup-Interface.md` |
|  | 3B | Flowise Chatbot | `Flowise/M03-VisualWorkflows/M03B-Flowise-Chatbot.md` |
|  | 3C | Flowise RAG over Course Documents | `Flowise/M03-VisualWorkflows/M03C-Flowise-RAG-CourseDocs.md` |
|  | 3D | Flowise AgentFlow with Tools | `Flowise/M03-VisualWorkflows/M03D-Flowise-AgentFlow-Tools.md` |
|  | 3E | Hosting, Web Embedding and UI Integration | `Flowise/M03-VisualWorkflows/M03E-Flowise-Hosting-WebIntegration.md` |
| M04: LangChain Programming | 4A | LangChain Fundamentals | `Jupyter/M04-LangChain/M04A-LangChain-Fundamentals.ipynb` |
|  | 4B | LangChain Tool-Using Agents | `Jupyter/M04-LangChain/M04B-LangChain-ToolAgents.ipynb` |
|  | 4C | Custom Tools, Local Storage and Action Execution | `Jupyter/M04-LangChain/M04C-CustomTools-Storage-Actions.ipynb` |
|  | 4D | Lead Research and Personalised Writing Agent | `Jupyter/M04-LangChain/M04D-LeadResearch-WritingAgent.ipynb` |
| M05: Knowledge Agents and Stateful Workflows | 5A | Basic RAG System | `Jupyter/M05-KnowledgeState/M05A-Basic-RAG-System.ipynb` |
|  | 5B | RAG Domain Assistant using Course Materials | `Jupyter/M05-KnowledgeState/M05B-RAG-CourseMaterials-Assistant.ipynb` |
|  | 5C | LangGraph Stateful Workflows | `Jupyter/M05-KnowledgeState/M05C-LangGraph-StatefulWorkflows.ipynb` |
|  | 5D | Copilot-Style Assistant with Vision and Task Execution | `Jupyter/M05-KnowledgeState/M05D-Copilot-Vision-TaskExecution.ipynb` |
| M06: Multi-Agent Systems and Safety | 6A | Multi-Agent Collaboration | `Jupyter/M06-MultiAgentSafety/M06A-MultiAgent-Collaboration.ipynb` |
|  | 6B | LLM Malicious Instruction and Prompt Injection Defence | `Jupyter/M06-MultiAgentSafety/M06B-LLM-Malicious-Instruction-Defense.ipynb` |
|  | 6C | Private Agents with Open-Source LLMs and Ollama | `Jupyter/M06-MultiAgentSafety/M06C-PrivateAgents-Ollama.ipynb` |
|  | 6D | Agent Security, Data Poisoning and Legal Risks | `Jupyter/M06-MultiAgentSafety/M06D-AgentSecurity-LegalRisks.ipynb` |
| M07: Model Adaptation and Multimodal GenAI | 7A | Fine-Tuning LLMs | `Jupyter/M07-ModelAdaptation/M07A-Finetuning-LLM.ipynb` |
|  | 7B | Fine-Tuning and Forgetting | `Jupyter/M07-ModelAdaptation/M07B-Finetuning-Forgetting.ipynb` |
|  | 7C | Diffusion Customization | `Jupyter/M07-ModelAdaptation/M07C-Diffusion-Customization.ipynb` |
|  | 7D | Speech Generation | `Jupyter/M07-ModelAdaptation/M07D-Speech-Generation.ipynb` |
|  | 7E | Fast Inference and Model Provider Comparison | `Jupyter/M07-ModelAdaptation/M07E-FastInference-ProviderComparison.ipynb` |
| M08: Advanced Agentic AI | 8A | Hugging Face Evaluation | `Jupyter/M08-Advanced/M08A-HuggingFace-Evaluation.ipynb` |
|  | 8B | Codex Codebase Understanding and Development | `Codex/M08-Advanced/M08B-Codex-Codebase-Understanding-and-Development.md` |
|  | 8C | Productised AI Agents and Go-to-Market Checklist | `Codex/M08-Advanced/M08C-Productised-AIAgents-GoToMarket.md` |

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
