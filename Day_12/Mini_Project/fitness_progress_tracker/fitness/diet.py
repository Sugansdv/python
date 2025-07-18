import json
from datetime import datetime
import os

def log_meal():
    food = input("Food item: ")
    calories = float(input("Calories consumed: "))

    data = {
        "food": food,
        "calories": calories,
        "date": datetime.now().strftime("%Y-%m-%d %H:%M")
    }

    _save_data("meals.json", data)
    print(f"Meal logged! Consumed {calories} kcal")

def _save_data(filename, entry):
    if os.path.exists(filename):
        with open(filename, "r") as f:
            data = json.load(f)
    else:
        data = []

    data.append(entry)

    with open(filename, "w") as f:
        json.dump(data, f, indent=2)
