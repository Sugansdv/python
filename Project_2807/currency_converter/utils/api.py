import json

def fetch_live_rates():
    # Mock API Response
    with open("data/mock_rates.json", "r") as f:
        return json.load(f)
