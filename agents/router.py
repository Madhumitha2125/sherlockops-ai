def classify_question(question: str):
    q = question.lower()

    score_sql = 0
    score_logs = 0
    score_config = 0

    # SQL related intent
    if any(word in q for word in ["transaction", "payment", "revenue", "sales", "failure"]):
        score_sql += 2

    # Log related intent
    if any(word in q for word in ["error", "timeout", "exception", "crash", "slow", "latency"]):
        score_logs += 2

    # Config related intent
    if any(word in q for word in ["config", "deployment", "change", "update"]):
        score_config += 2

    # fallback when nothing matches
    if score_sql + score_logs + score_config == 0:
        return ["logs"]  # safest default

    tools = []

    if score_sql > 0:
        tools.append("sql")
    if score_logs > 0:
        tools.append("logs")
    if score_config > 0:
        tools.append("config")

    return tools