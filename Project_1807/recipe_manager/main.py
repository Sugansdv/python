

from recipe_book import add_recipe, view_recipes

def main():
    while True:
        print("\n--- Recipe Manager ---")
        print("1. Add Recipe")
        print("2. View Recipes")
        print("3. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            title = input("Enter recipe title: ")

            ing = input("Enter ingredients (comma-separated): ")
            ingredients = [i.strip() for i in ing.split(",")]

            uts = input("Enter utensils (comma-separated): ")
            utensils = [u.strip() for u in uts.split(",")]

            steps = []
            print("Enter steps (type 'done' to finish):")
            while True:
                step = input("→ ")
                if step.lower() == "done":
                    break
                steps.append(step)

            add_recipe(title, ingredients, utensils, steps)

        elif choice == "2":
            view_recipes()

        elif choice == "3":
            print("Goodbye! Exiting Recipe Manager.")
            break

        else:
            print("Invalid option.")

if __name__ == "__main__":
    main()
