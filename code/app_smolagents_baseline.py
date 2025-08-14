# code/app_smolagents_baseline.py
import os
from huggingface_hub import InferenceClient

client = InferenceClient(token=os.getenv("HUGGINGFACEHUB_API_TOKEN"))
MODEL_ID = os.getenv("HF_MODEL_ID", "google/flan-t5-large")

def run_agent(prompt: str) -> str:
    out = client.text_generation(MODEL_ID, prompt, max_new_tokens=128, temperature=0.2)
    return out  # GAIA-friendly: only final answer string

if __name__ == "__main__":
    print(run_agent("Explain dependency pinning in one sentence."))
