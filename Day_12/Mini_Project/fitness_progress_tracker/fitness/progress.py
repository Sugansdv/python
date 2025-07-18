import json
import os

def view_progress():
    workouts = _load_data("workouts.json")
    meals = _load_data("meals.json")

    total_burned = sum(w["calories"] for w in workouts)
    total_consumed = sum(m["calories"] for m in meals)

    print("\n--- Progress Summary ---")
    print(f"Workouts Logged: {len(workouts)}")
    print(f"Total Calories Burned: {total_burned} kcal")
    print(f"Meals Logged: {len(meals)}")
    print(f"Total Calories Consumed: {total_consumed} kcal")
    print(f"Net Calories: {total_consumed - total_burned} kcal")

def _load_data(filename):
    if os.path.exists(filename):
        with open(filename, "r") as f:
            return json.load(f)
    return []
