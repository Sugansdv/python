import json
import os
from .recipe import Recipe
from .decorators import log_search

class RecipeManager:
    def __init__(self, file_path="data/recipes.json"):
        self.file_path = file_path
        self.recipes = {}
        self.load_recipes()

    def load_recipes(self):
        if os.path.exists(self.file_path):
            try:
                with open(self.file_path, "r") as f:
                    data = json.load(f)
                    for name, info in data.items():
                        self.recipes[name] = Recipe(name, info["ingredients"], info["steps"])
            except json.JSONDecodeError:
                print("Invalid JSON format. Starting with empty recipe list.")

    def save_recipes(self):
        with open(self.file_path, "w") as f:
            data = {
                name: {
                    "ingredients": recipe.ingredients,
                    "steps": recipe.steps
                }
                for name, recipe in self.recipes.items()
            }
            json.dump(data, f, indent=4)

    def add_recipe(self, name, ingredients, steps):
        self.recipes[name] = Recipe(name, ingredients, steps)
        self.save_recipes()
        print(f" Recipe '{name}' added successfully!")

    @log_search
    def search_by_ingredient(self, ingredient):
        found = False
        for recipe in self.recipes.values():
            if ingredient.lower() in (ing.lower() for ing in recipe.ingredients):
                print(recipe, "\n")
                found = True
                yield recipe
        if not found:
            print(f" No recipes found with '{ingredient}'.")

    def get_unique_ingredients(self):
        ingredients = set()
        for recipe in self.recipes.values():
            ingredients.update(recipe.ingredients)
        return ingredients
