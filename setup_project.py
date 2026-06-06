import os

folders = [
    "core",
    "agents",
    "data/logs",
    "data/configs",
    "services",
    "prompts",
    "ui",
    "static",
    "tests"
]

files = [
    "app.py",
    "requirements.txt",
    "README.md",
    "config.py",

    "core/__init__.py",
    "core/orchestrator.py",
    "core/evidence_collector.py",
    "core/rca_engine.py",
    "core/timeline_engine.py",
    "core/utils.py",

    "agents/__init__.py",
    "agents/sql_agent.py",
    "agents/log_agent.py",
    "agents/config_agent.py",

    "services/__init__.py",
    "services/sql_service.py",
    "services/log_service.py",
    "services/config_service.py",
    "services/llm_service.py",

    "ui/__init__.py",
    "ui/dashboard.py",
    "ui/components.py",
    "ui/timeline_ui.py",
    "ui/styles.py",

    "prompts/rca_prompt.txt",
    "prompts/summary_prompt.txt",
    "prompts/recommendation_prompt.txt",

    "data/sample_data.sql",
    "data/logs/app_logs.txt",
    "data/configs/expected_config.json",
    "data/configs/current_config.json",

    "static/styles.css",
    "static/logo.png",

    "tests/test_sql_agent.py",
    "tests/test_log_agent.py",
    "tests/test_config_agent.py"
]

# Create folders
for folder in folders:
    os.makedirs(folder, exist_ok=True)

# Create files
for file in files:
    with open(file, "w") as f:
        pass

print("✅ SherlockOps AI structure created successfully!")