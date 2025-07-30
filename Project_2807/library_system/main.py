from core.book import Book
from core.library import Library

def main():
    library = Library()

    while True:
        print("\n--- Library Menu ---")
        print("1. Add Book")
        print("2. Borrow Book")
        print("3. Return Book")
        print("4. Search Book")
        print("5. List Available Books")
        print("6. Delete Book (Admin Only)")
        print("7. Exit")

        choice = input("Choose an option: ")

        try:
            if choice == "1":
                title = input("Title: ")
                author = input("Author: ")
                library.add_book(Book(title, author))
                print("Book added.")

            elif choice == "2":
                title = input("Enter book title: ")
                borrower = input("Your name: ")
                library.borrow_book(title, borrower)

            elif choice == "3":
                title = input("Enter book title to return: ")
                library.return_book(title)

            elif choice == "4":
                keyword = input("Enter keyword: ")
                found = library.search_books(keyword)
                for book in found:
                    print(book)

            elif choice == "5":
                print("\nAvailable Books:")
                library.list_available_books()

            elif choice == "6":
                title = input("Title to delete: ")
                library.delete_book(title)

            elif choice == "7":
                print("Goodbye!")
                break

            else:
                print("Invalid choice.")
        except ValueError as ve:
            print("Error:", ve)

if __name__ == "__main__":
    main()
