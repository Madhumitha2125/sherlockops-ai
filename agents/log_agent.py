import re
from collections import Counter

LOG_FILE = "data/logs/app.log"


def analyze_logs():
    with open(LOG_FILE, "r") as f:
        logs = f.readlines()

    errors = []
    timeouts = 0
    db_errors = 0

    for log in logs:
        if "ERROR" in log:
            errors.append(log)

        if "timeout" in log.lower():
            timeouts += 1

        if "sql" in log.lower():
            db_errors += 1

    return {
        "total_logs": len(logs),
        "error_count": len(errors),
        "timeout_count": timeouts,
        "db_error_count": db_errors,
        "sample_errors": errors[:5]
    }