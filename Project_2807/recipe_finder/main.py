from core.recipe_manager import RecipeManager

def main():
    manager = RecipeManager()

    while True:
        print("\n Recipe Finder Menu:")
        print("1. Add new recipe")
        print("2. Search by ingredient")
        print("3. Show all unique ingredients")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            name = input("Enter recipe name: ")
            ingredients = input("Enter ingredients (comma-separated): ").split(",")
            steps = input("Enter steps (separated by ';'): ").split(";")
            manager.add_recipe(name.strip(), [i.strip() for i in ingredients], [s.strip() for s in steps])

        elif choice == "2":
            ingredient = input("Enter ingredient to search: ")
            list(manager.search_by_ingredient(ingredient))  # Consume generator

        elif choice == "3":
            unique_ings = manager.get_unique_ingredients()
            print(" Unique Ingredients:\n", ", ".join(sorted(unique_ings)))

        elif choice == "4":
            print(" Exiting Recipe Finder.")
            break
        else:
            print(" Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
