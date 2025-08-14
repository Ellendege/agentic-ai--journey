# SmolAgents — GAIA Troubleshooting

## 1) Missing or wrong model class imports
**Symptom**
```
ImportError: cannot import name 'HfApiModel' from 'smolagents'
```
or
```
ImportError: cannot import name 'HuggingFaceInferenceModel' from 'smolagents'
```
**Cause** API names/exports changed across versions.  
**Fix** Confirm installed version; use current exports or `InferenceClient` from `huggingface_hub`.

## 2) Version mismatch
**Symptom** `No matching distribution found for smolagents==0.1.36`  
**Fix** Install an available version (e.g., `smolagents==1.21.0`) and then freeze with `pip freeze > requirements.txt`.

## 3) Old internal file structure
**Symptom** `ModuleNotFoundError: smolagents.models.huggingface`  
**Fix** Stop importing old subpaths; use public API or `InferenceClient`.

## 4) Provider & task mismatch
**Symptom** provider rejects model for `text-generation`.  
**Fix** Use a compatible model (e.g., `mistralai/Mistral-7B-Instruct-v0.3`, `google/flan-t5-large`) and set task where needed.

## 5) Missing secrets
**Symptom** `ValueError: Missing HUGGINGFACEHUB_API_TOKEN`  
**Fix** Add token in environment/Space Secrets.

## 6) GAIA compliance (output wrapper)
Return only the **final answer** string; no logs or extra commentary.
