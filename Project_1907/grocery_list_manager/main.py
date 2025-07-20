from grocery.operations import (
    add_item, remove_item, mark_bought,
    display_by_category, search_items
)
from grocery.utils.printer import print_header

def get_input(prompt):
    return input(prompt).strip()

def main():
    items_by_category = {}
    bought_items = set()

    while True:
        print_header("🛒 Grocery List Manager")
        print("1. Add Item")
        print("2. Remove Item")
        print("3. Mark Item as Bought")
        print("4. Display by Category")
        print("5. Search Items")
        print("6. Exit")

        choice = get_input("Enter your choice (1-6): ")

        if choice == "1":
            item = get_input("Enter item name: ")
            category = get_input("Enter category: ")
            add_item(items_by_category, item, category)

        elif choice == "2":
            item = get_input("Enter item name to remove: ")
            remove_item(items_by_category, item)

        elif choice == "3":
            item = get_input("Enter item name to mark as bought: ")
            mark_bought(items_by_category, bought_items, item)

        elif choice == "4":
            display_by_category(items_by_category, bought_items)

        elif choice == "5":
            keyword = get_input("Enter keyword to search: ")
            search_items(items_by_category, keyword)

        elif choice == "6":
            print(" Exiting Grocery List Manager. Bye!")
            break

        else:
            print(" Invalid option. Try again.")

if __name__ == "__main__":
    main()
