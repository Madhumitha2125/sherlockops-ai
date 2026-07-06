from services.llm_manager import llm



def generate_ai_rca(question, evidence):


    prompt = f"""

You are SherlockOps AI.

Analyze this incident.

Question:

{question}


Evidence:

{evidence}


Return:

1. Root Cause
2. Confidence Score
3. Impact
4. SQL Issue
5. Configuration Drift
6. Recovery Steps
7. Prevention Recommendations

"""


    return llm.generate_response(prompt)