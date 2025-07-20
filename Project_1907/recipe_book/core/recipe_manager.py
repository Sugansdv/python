def add_recipe(recipes):
    name = input("Recipe name: ").strip()
    if name in recipes:
        print("Recipe already exists.")
        return
    ingredients = input("Enter ingredients (comma-separated): ").split(",")
    steps = input("Enter steps (semicolon-separated): ").split(";")
    recipes[name] = (ingredients, steps)
    print(f"Added '{name}'.")

def remove_recipe(recipes):
    name = input("Recipe to remove: ").strip()
    if name in recipes:
        del recipes[name]
        print(f"Removed '{name}'.")
    else:
        print("Recipe not found.")

def modify_recipe(recipes):
    name = input("Recipe to modify: ").strip()
    if name not in recipes:
        print("Recipe not found.")
        return
    ingredients = input("New ingredients (comma-separated): ").split(",")
    steps = input("New steps (semicolon-separated): ").split(";")
    recipes[name] = (ingredients, steps)
    print(f"Updated '{name}'.")

def search_by_ingredient(recipes, ingredient):
    print(f"Searching for recipes with '{ingredient}'...")
    found = False
    for name, (ingredients, _) in recipes.items():
        if ingredient.lower() in {i.strip().lower() for i in ingredients}:
            print(f"- {name}")
            found = True
    if not found:
        print("No recipes found with that ingredient.")

def list_recipes(recipes):
    if not recipes:
        print("No recipes available.")
        return
    print("📖 Recipe List:")
    for name in sorted(recipes):
        print(f"- {name}")
