

from data.recipes_data import recipes

def add_recipe(title, ingredients, utensils, steps):
    key = (title,)
    if key in recipes:
        print(f" Recipe '{title}' already exists.")
        return
    
    unique_utensils = set(utensils)

    recipes[key] = {
        "ingredients": ingredients,
        "utensils": unique_utensils,
        "steps": steps
    }
    print(f"Recipe '{title}' added successfully.")

def view_recipes():
    if not recipes:
        print("No recipes available.")
        return
    print("\n Recipe List:")
    for key, details in recipes.items():
        print(f"\n Title: {key[0]}")
        print("Ingredients:")
        for item in details["ingredients"]:
            print(f" - {item}")
        print("Utensils:", ', '.join(details["utensils"]))
        print("Steps:")
        for i, step in enumerate(details["steps"], 1):
            print(f" {i}. {step}")
