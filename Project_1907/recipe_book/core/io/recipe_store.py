import json
import os

FILENAME = "recipes.json"

def load_recipes():
    if not os.path.exists(FILENAME):
        return {}
    with open(FILENAME, "r") as f:
        return json.load(f)

def save_recipes(recipes):
    with open(FILENAME, "w") as f:
        json.dump(recipes, f, indent=2)
