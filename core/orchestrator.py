from agents.router import classify_question
from agents.sql_agent import get_transaction_failures   
from agents.log_agent import analyze_logs
from agents.config_agent import detect_drift
from services.llm_service import generate_ai_rca

def classify_question(question):

    question = question.lower()

    tools = []


    sql_keywords = [
        "sql",
        "database",
        "query",
        "transaction",
        "table",
        "index",
        "postgres",
        "mysql",
        "db"
    ]


    log_keywords = [
        "log",
        "error",
        "exception",
        "failure",
        "crash",
        "warning",
        "incident",
        "latency",
        "timeout"
    ]


    config_keywords = [
        "config",
        "configuration",
        "drift",
        "setting",
        "environment",
        "deployment",
        "version"
    ]



    if any(word in question for word in sql_keywords):
        tools.append("sql")


    if any(word in question for word in log_keywords):
        tools.append("logs")


    if any(word in question for word in config_keywords):
        tools.append("config")


    return tools




def run_investigation(question):


    print("\n========== INCIDENT ==========")
    print(question)
    print("==============================\n")


    tools = classify_question(question)


    print("========== TOOLS SELECTED ==========")
    print(tools)
    print("====================================\n")



    evidence = {}



    # SQL ANALYSIS
    if "sql" in tools:

        try:

            evidence["sql"] = get_transaction_failures()

        except Exception as e:

            evidence["sql"] = {
                "error": str(e)
            }



    # LOG ANALYSIS
    if "logs" in tools:

        try:

            evidence["logs"] = analyze_logs()

        except Exception as e:

            evidence["logs"] = {
                "error": str(e)
            }



    # CONFIG ANALYSIS
    if "config" in tools:

        try:

            evidence["config"] = detect_drift()

        except Exception as e:

            evidence["config"] = {
                "error": str(e)
            }




    # FALLBACK
    # If no agent selected,
    # run everything

    if not evidence:


        print(
            "No matching agent found. Running full investigation..."
        )


        try:
            evidence["logs"] = analyze_logs()
        except Exception as e:
            evidence["logs"] = str(e)



        try:
            evidence["sql"] = get_transaction_failures()
        except Exception as e:
            evidence["sql"] = str(e)



        try:
            evidence["config"] = detect_drift()
        except Exception as e:
            evidence["config"] = str(e)




    print("\n========== FINAL EVIDENCE ==========")
    print(evidence)
    print("====================================\n")



    # SEND TO LLM

    result = generate_ai_rca(
        question,
        evidence
    )


    return result