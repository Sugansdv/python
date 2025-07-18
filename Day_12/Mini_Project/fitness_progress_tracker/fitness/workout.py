import json
from datetime import datetime
import os

def log_workout():
    workout = input("Workout type (e.g. running, lifting): ")
    duration = float(input("Duration (in minutes): "))
    calories = round(duration * 5.5, 2)  # Sample logic

    data = {
        "type": workout,
        "duration": duration,
        "calories": calories,
        "date": datetime.now().strftime("%Y-%m-%d %H:%M")
    }

    _save_data("workouts.json", data)
    print(f"Workout logged! Burned {calories} kcal")

def _save_data(filename, entry):
    if os.path.exists(filename):
        with open(filename, "r") as f:
            data = json.load(f)
    else:
        data = []

    data.append(entry)

    with open(filename, "w") as f:
        json.dump(data, f, indent=2)
