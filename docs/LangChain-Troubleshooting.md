# LangChain/LangGraph — GAIA Troubleshooting

1) **Missing `langchain_community`** → `pip install -U langchain-community`; update imports.  
2) **OpenAI key error** while using HF → remove `ChatOpenAI`; use `HuggingFaceEndpoint`.  
3) **`HuggingFaceHub` deprecated** → `pip install -U langchain-huggingface`; import `HuggingFaceEndpoint`.  
4) **Params in `model_kwargs`** → put `temperature`, `max_new_tokens` top-level.  
5) **Missing `duckduckgo-search`** → `pip install -U duckduckgo-search`.  
6) **Unsupported model for provider/task** → choose text-generation-capable model.  
7) **Wrong `AgentType`** → `AgentType.ZERO_SHOT_REACT_DESCRIPTION`.  
8) **`max_length`** → use `max_new_tokens`.  
9) **`generator raised StopIteration`** → guard tool returns; align model/task; minimal repro; `handle_parsing_errors=True`.
