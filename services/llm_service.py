from groq import Groq
import os

client = Groq(api_key=os.getenv("GROQ_API_KEY"))


def generate_ai_rca(user_question, evidence):
    prompt = f"""
You are SherlockOps AI, an enterprise SRE incident investigator.

You MUST ONLY use the provided evidence. Do NOT assume anything outside it.

User Question:
{user_question}

Evidence:
{evidence}

Generate a structured RCA with:

1. Root Cause
2. Evidence Used
3. Business Impact
4. Technical Impact
5. Confidence Score (0-100)
6. Recommendations
"""

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {"role": "system", "content": "You are an expert SRE investigator."},
            {"role": "user", "content": prompt}
        ]
    )

    return response.choices[0].message.content