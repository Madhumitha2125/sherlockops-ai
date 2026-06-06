from agents.router import classify_question
from agents.sql_agent import get_transaction_failures   
from agents.log_agent import analyze_logs
from agents.config_agent import detect_drift
from services.llm_service import generate_ai_rca


def run_investigation(question):

    tools = classify_question(question)

    evidence = {}

    if "sql" in tools:
        evidence["sql"] = get_transaction_failures()

    if "logs" in tools:
        evidence["logs"] = analyze_logs()

    if "config" in tools:
        evidence["config"] = detect_drift()

    # 🔥 IMPORTANT FIX (handles unknown questions)
    if not evidence:
        evidence["logs"] = analyze_logs()

    return generate_ai_rca(question, evidence)