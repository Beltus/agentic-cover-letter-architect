# 🚀  Agentic Career Architect
A Multi-Agent Workflow for Personalized Job Applications

# 📌 Overview
Agentic Career Architect is a specialized job application assistant that transforms a raw job description into a high-impact, tailored resume summary and cover letter. Unlike simple one-shot AI prompts, this application utilizes a Prompt Chaining Workflow powered by LangGraph to ensure deep alignment between the candidate's output and the employer's specific requirements.

By breaking the process into specialized "nodes," the system mimics the thought process of a professional career coach: first extracting key qualifications, then architecting a narrative that bridges the gap between the role and the applicant.

# 🛠️ The Tech Stack
Orchestration: LangGraph(State-based multi-agent design)

Intelligence: Ollama(Running Llama 3.2 Vision 11B locally)

Interface: Streamlit(Clean, reactive web UI)

Language: Python 3.11+

# 🧠 The Workflow Pattern: Prompt Chaining
This app implements a directed acyclic graph (DAG) to handle the complexity of document generation:

Extraction Node: Analyzes the job_descriptionto identify "Must-Have" skills and company culture signals.

Resume Summary Node: Generates a concise, high-impact professional summary.

Cover Letter Node: Uses the extracted insights to draft a personalized letter that focuses on "The Fit," ensuring the tone is professional yet engaging.

# ✨ Key Features
Local-First AI: Privacy-focused processing using Ollama—no data leaves your machine.

State Management: Built with TypedDictstate tracking to ensure consistency across the generation chain.

Reactive UI: A streamlined Streamlit interface with "one-click" copy functionality for rapid applications.

Modular Design: Easily extensible to add “Reviewer” or “Fact-Checker” agents.

# 🚀 Getting Started
Prerequisites

InstallOllama

Pull the model:ollama pull llama3.2-vision:11b

# installation

```Bash
git clone https://github.com/YOUR_USERNAME/agentic-career-architect.git
cd agentic-career-architect
pip install -r requirements.txt
Run the App
```
```bash
streamlit run app.py
```
👨‍💻 Author

[Beltus Nkwawir](https://www.linkedin.com/in/beltus/) Data Scientist and PhD Candidate. Passionate about Agentic AI and building tools that bridge the gap between human intent and machine intelligence.