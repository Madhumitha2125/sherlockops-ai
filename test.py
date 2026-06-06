from core.orchestrator import run_investigation

question = "Why did transaction failures increase?"

result = run_investigation(question)

print("\n===== FINAL RCA =====\n")
print(result)