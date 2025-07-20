from core.recipe_manager import (
    add_recipe, remove_recipe, modify_recipe,
    search_by_ingredient, list_recipes
)
from core.io.recipe_store import load_recipes, save_recipes

def main():
    recipes = load_recipes()

    while True:
        print("\n Recipe Book Menu:")
        print("1. List all recipes")
        print("2. Add a recipe")
        print("3. Remove a recipe")
        print("4. Modify a recipe")
        print("5. Search by ingredient")
        print("6. Exit")

        choice = input("Enter choice (1-6): ").strip()

        if choice == "1":
            list_recipes(recipes)
        elif choice == "2":
            add_recipe(recipes)
        elif choice == "3":
            remove_recipe(recipes)
        elif choice == "4":
            modify_recipe(recipes)
        elif choice == "5":
            ing = input("Enter ingredient to search: ").strip()
            search_by_ingredient(recipes, ing)
        elif choice == "6":
            save_recipes(recipes)
            print("Exiting. Recipes saved.")
            break
        else:
            print("Invalid choice. Try again.")
if __name__ == "__main__":
    main()