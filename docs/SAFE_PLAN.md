# Safe Plan

1) Sanity: venv + `pip install -r requirements.txt` (after freezing).  
2) Provider: set `HUGGINGFACEHUB_API_TOKEN`; smoke-test endpoint.  
3) Baseline first (no tools).  
4) Add agent minimal.  
5) Add tools one-by-one; guard outputs.  
6) Pin versions; record models.  
7) GAIA: wrap output to return only the final answer.
