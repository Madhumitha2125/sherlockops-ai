import json

EXPECTED = "data/configs/expected_config.json"
CURRENT = "data/configs/current_config.json"


def detect_drift():
    with open(EXPECTED) as f:
        expected = json.load(f)

    with open(CURRENT) as f:
        current = json.load(f)

    drift = {}

    for key in expected:
        if key in current and expected[key] != current[key]:
            drift[key] = {
                "expected": expected[key],
                "current": current[key]
            }

    return drift