# Agentic AI Journey — My First AI Agent (Hugging Face Course)

> **From learning to building.** This repo tracks my journey after finishing the **Hugging Face Agentic AI course** — building my first AI agent, experimenting with **LangChain**, **SmolAgents**, and **LangGraph**, and documenting real-world lessons about **model selection**, **tool creation**, and **debugging**.

---

## 🔎 What’s inside

- **docs/**
  - `SmolAgents-Troubleshooting.md` — errors, causes, fixes, and minimal checks.
  - `LangChain-Troubleshooting.md` — common pitfalls + solutions.
  - `KNOWN_GOOD_MODELS.md` — models + tasks that worked for me (with notes).
  - `SAFE_PLAN.md` — my “stabilize-first” workflow for avoiding rabbit holes.
- **code/**
  - `app_langchain_baseline.py` — minimal LangChain baseline (HuggingFaceEndpoint).
  - `app_smolagents_baseline.py` — minimal SmolAgents baseline (InferenceClient).
- **notion/**
  - `NOTION_issues_combined.csv` — import-ready log database for Notion.
- **linkedin/**
  - `POST_TEMPLATES.md` — short posts (hooks, lessons, CTAs) to share progress.
- `PROGRESS_JOURNAL.md` — day-by-day notes linking errors → fixes → artifacts.
- `.github/ISSUE_TEMPLATE/learning-log.md` — capture each session quickly.

---

## 🎯 Why this repo exists

- Show **hands-on progress** after the course (not just theory).
- Prove **debugging + communication**: problem → root cause → fix.
- Help others avoid the same traps (versions, imports, model/task mismatch).
- Create a public record I can reference in **Notion / GitHub / LinkedIn**.

---

## ⚙️ Quick start (local)

1) **Python env**
```bash
python -m venv .venv
# Windows
.\.venv\Scripts\Activate.ps1
# macOS/Linux
source .venv/bin/activate
python -m pip install --upgrade pip

Install

pip install -r requirements_suggestion.txt
# After a clean run:
pip freeze > requirements.txt

Secrets

# Windows (setx then open a new terminal)
setx HUGGINGFACEHUB_API_TOKEN "<your-token>"
setx HF_MODEL_ID "google/flan-t5-large"

# macOS/Linux (current shell)
export HUGGINGFACEHUB_API_TOKEN="<your-token>"

🧪 Highlights: what I learned (short)

Versions matter: match imports to the exact package version; pin working sets.

Model ↔ task compatibility: some models only support conversational, others text-generation or text2text-generation.

Tool outputs: agents fail if tools return None or unexpected types → guard returns.

GAIA compliance: return only the final answer string; avoid debug logs in output.

Safe Plan: baseline first (no tools) → add one tool at a time → freeze versions.

See full details in docs/SmolAgents-Troubleshooting.md and docs/LangChain-Troubleshooting.md.

export HF_MODEL_ID="google/flan-t5-large"

| Model                                | Provider     | Task                 | Notes                               |
| ------------------------------------ | ------------ | -------------------- | ----------------------------------- |
| `google/flan-t5-large`               | HF Inference | text2text-generation | Stable baseline                     |
| `google/flan-t5-xl`                  | HF Inference | text2text-generation | Increase `max_new_tokens` as needed |
| `mistralai/Mistral-7B-Instruct-v0.3` | HF Inference | text-generation      | Instruction-tuned                   |


python code/app_langchain_baseline.py
python code/app_smolagents_baseline.py
