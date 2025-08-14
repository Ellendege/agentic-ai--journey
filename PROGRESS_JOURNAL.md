# Progress Journal

| Date | Track | Topic | Error/Issue | Root Cause | Fix | Artifact/Commit | Time Spent | Next Step |
|---|---|---|---|---|---|---|---:|---|
| 2025-08-08 | LangChain | Imports | `ModuleNotFoundError: langchain_community` | Integration split | Install `langchain-community` + update imports | (link) | 45m | Audit imports |
| 2025-08-08 | LangChain | Provider | `Did not find openai_api_key` | `ChatOpenAI` still wired | Use `HuggingFaceEndpoint` | (link) | 30m | Smoke test HF endpoint |
| 2025-08-08 | LangChain | Models | `Model not supported for task` | Wrong model/task | Choose model supporting `text-generation` | (link) | 40m | Known-good list |
| 2025-08-08 | SmolAgents | Versions | `No matching distribution smolagents==0.1.36` | Non-existent version | Use available (`1.21.0`) | (link) | 20m | Freeze deps |
| 2025-08-08 | SmolAgents | Imports | `ImportError: HfApiModel` | API changed | Use current class or `InferenceClient` | (link) | 60m | Minimal repro |
| 2025-08-08 | Runtime | Parsing | `generator raised StopIteration` | None/empty tool output + mismatch | Guard returns; align model/task | (link) | 50m | Stepwise tool tests |
