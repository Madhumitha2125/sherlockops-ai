from services.llm_service import generate_ai_rca

def generate_rca(sql_data, log_data, config_data, question):

    context = {
        "question": question,
        "sql_evidence": sql_data,
        "log_evidence": log_data,
        "config_evidence": config_data
    }

    prompt = f"""
You are an expert Site Reliability Engineer.

Analyze the following incident data and determine the root cause.

DATA:
{context}

Rules:
- Use ONLY the evidence provided
- Correlate signals across SQL, logs, and config
- Do NOT use templates
- Explain reasoning step by step
- Provide root cause + confidence score
"""

    return generate_ai_rca(prompt)