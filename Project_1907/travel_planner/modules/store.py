import json

FILENAME = "trips.json"

def load_trips():
    try:
        with open(FILENAME, "r") as f:
            data = json.load(f)
            for trip in data:
                trip["participants"] = set(trip["participants"])
            return data
    except FileNotFoundError:
        return []

def save_trips(trips):
    with open(FILENAME, "w") as f:
        json.dump([{**trip, "participants": list(trip["participants"])} for trip in trips], f, indent=2)
