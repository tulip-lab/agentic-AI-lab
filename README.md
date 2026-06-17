[![GitHub issues](https://img.shields.io/github/issues/tulip-lab/agentic-ai)](https://github.com/tulip-lab/agentic-ai/issues)
[![GitHub pull requests](https://img.shields.io/github/issues-pr/tulip-lab/agentic-ai)](https://github.com/tulip-lab/agentic-ai/pulls)
[![GitHub stars](https://img.shields.io/github/stars/tulip-lab/agentic-ai.svg?style=social&label=Star)](https://github.com/tulip-lab/agentic-ai/stargazers/)

---

![FLIP Banner](Assets/images/flip-banner.png)

# FLIP: Agentic AI in Practice

**FLIP** stands for **Fundamentals of Learning and Intelligent Processing**.

This repository contains student-facing practical materials for building generative and agentic AI systems through Python notebooks, visual workflows, retrieval-augmented generation, multi-agent systems, model adaptation, evaluation and coding-agent practice.

---

- Materials in this repository support practical learning in generative AI and agentic AI systems.
- Public course documents and public datasets should be used wherever possible in exercises.
- Public data for simple practical tasks should preferably come from [tulip-lab/open-data](https://github.com/tulip-lab/open-data).
- If you find an issue or bug, please submit an issue at [tulip-lab/agentic-ai](https://github.com/tulip-lab/agentic-ai/issues).
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

More details are available in [Docs/DATA_POLICY.md](Docs/DATA_POLICY.md).

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
| :one: | Preliminary | Foundations | <ul><li>[M01A-Python-Colab-API-Safety](Jupyter/M01-Foundations/M01A-Python-Colab-API-Safety.ipynb)</li><li>[M01B-GenAI-Fundamentals](Jupyter/M01-Foundations/M01B-GenAI-Fundamentals.ipynb)</li><li>[M01C-LLMs-FunctionCalling-APIs](Jupyter/M01-Foundations/M01C-LLMs-FunctionCalling-APIs.ipynb)</li></ul> |
| :two: | Preliminary | AI Modelling Basics | <ul><li>[M02A-Regression-ML-Basics](Jupyter/M02-AIModeling/M02A-Regression-ML-Basics.ipynb)</li><li>[M02B-DeepLearning-ImageClassification](Jupyter/M02-AIModeling/M02B-DeepLearning-ImageClassification.ipynb)</li><li>[M02C-Embeddings-VectorData-Similarity](Jupyter/M02-AIModeling/M02C-Embeddings-VectorData-Similarity.ipynb)</li></ul> |
| :three: | Core | Visual Workflows with Flowise | <ul><li>[M03A-Flowise-Setup-Interface](Flowise/M03-VisualWorkflows/M03A-Flowise-Setup-Interface.md)</li><li>[M03B-Flowise-Chatbot](Flowise/M03-VisualWorkflows/M03B-Flowise-Chatbot.md)</li><li>[M03C-Flowise-RAG-CourseDocs](Flowise/M03-VisualWorkflows/M03C-Flowise-RAG-CourseDocs.md)</li><li>[M03D-Flowise-AgentFlow-Tools](Flowise/M03-VisualWorkflows/M03D-Flowise-AgentFlow-Tools.md)</li><li>[M03E-Flowise-Hosting-WebIntegration](Flowise/M03-VisualWorkflows/M03E-Flowise-Hosting-WebIntegration.md)</li></ul> |
| :four: | Core | LangChain Programming | <ul><li>[M04A-LangChain-Fundamentals](Jupyter/M04-LangChain/M04A-LangChain-Fundamentals.ipynb)</li><li>[M04B-LangChain-ToolAgents](Jupyter/M04-LangChain/M04B-LangChain-ToolAgents.ipynb)</li><li>[M04C-CustomTools-Storage-Actions](Jupyter/M04-LangChain/M04C-CustomTools-Storage-Actions.ipynb)</li><li>[M04D-LeadResearch-WritingAgent](Jupyter/M04-LangChain/M04D-LeadResearch-WritingAgent.ipynb)</li></ul> |
| :five: | Core | Knowledge Agents and Stateful Workflows | <ul><li>[M05A-Basic-RAG-System](Jupyter/M05-KnowledgeState/M05A-Basic-RAG-System.ipynb)</li><li>[M05B-RAG-CourseMaterials-Assistant](Jupyter/M05-KnowledgeState/M05B-RAG-CourseMaterials-Assistant.ipynb)</li><li>[M05C-LangGraph-StatefulWorkflows](Jupyter/M05-KnowledgeState/M05C-LangGraph-StatefulWorkflows.ipynb)</li><li>[M05D-Copilot-Vision-TaskExecution](Jupyter/M05-KnowledgeState/M05D-Copilot-Vision-TaskExecution.ipynb)</li></ul> |
| :six: | Core | Multi-Agent Systems and Safety | <ul><li>[M06A-MultiAgent-Collaboration](Jupyter/M06-MultiAgentSafety/M06A-MultiAgent-Collaboration.ipynb)</li><li>[M06B-LLM-Malicious-Instruction-Defense](Jupyter/M06-MultiAgentSafety/M06B-LLM-Malicious-Instruction-Defense.ipynb)</li><li>[M06C-PrivateAgents-Ollama](Jupyter/M06-MultiAgentSafety/M06C-PrivateAgents-Ollama.ipynb)</li><li>[M06D-AgentSecurity-LegalRisks](Jupyter/M06-MultiAgentSafety/M06D-AgentSecurity-LegalRisks.ipynb)</li></ul> |
| :seven: | Advanced | Model Adaptation and Multimodal GenAI | <ul><li>[M07A-Finetuning-LLM](Jupyter/M07-ModelAdaptation/M07A-Finetuning-LLM.ipynb)</li><li>[M07B-Finetuning-Forgetting](Jupyter/M07-ModelAdaptation/M07B-Finetuning-Forgetting.ipynb)</li><li>[M07C-Diffusion-Customization](Jupyter/M07-ModelAdaptation/M07C-Diffusion-Customization.ipynb)</li><li>[M07D-Speech-Generation](Jupyter/M07-ModelAdaptation/M07D-Speech-Generation.ipynb)</li><li>[M07E-FastInference-ProviderComparison](Jupyter/M07-ModelAdaptation/M07E-FastInference-ProviderComparison.ipynb)</li></ul> |
| :eight: | Advanced | Advanced Agentic AI | <ul><li>[M08A-HuggingFace-Evaluation](Jupyter/M08-Advanced/M08A-HuggingFace-Evaluation.ipynb)</li><li>[M08B-Codex-Codebase-Understanding-and-Development](Codex/M08-Advanced/M08B-Codex-Codebase-Understanding-and-Development.md)</li><li>[M08C-Productised-AIAgents-GoToMarket](Codex/M08-Advanced/M08C-Productised-AIAgents-GoToMarket.md)</li></ul> |

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

## Contributors

Thanks goes to these wonderful people :tulip:

<a href="https://github.com/tulip-lab/agentic-ai/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=tulip-lab/agentic-ai" />
</a>

Made with [contributors-img](https://contrib.rocks).
