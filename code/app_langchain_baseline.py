# code/app_langchain_baseline.py
import os
from langchain.agents import initialize_agent, AgentType
from langchain_huggingface import HuggingFaceEndpoint

assert os.getenv("HUGGINGFACEHUB_API_TOKEN"), "Set HUGGINGFACEHUB_API_TOKEN"

llm = HuggingFaceEndpoint(
    repo_id="google/flan-t5-xl",
    temperature=0.2,
    max_new_tokens=64,
    huggingfacehub_api_token=os.getenv("HUGGINGFACEHUB_API_TOKEN"),
)

agent = initialize_agent(
    tools=[],
    llm=llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True,
    handle_parsing_errors=True,
)

if __name__ == "__main__":
    print(agent.run("In one sentence, why does dependency pinning matter?"))
