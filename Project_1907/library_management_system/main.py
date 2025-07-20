from library.book_ops import (
    add_book, search_books, list_books, list_genres
)
from library.user_ops import borrow_book, return_book

def get_input(prompt):
    return input(prompt).strip()

def main():
    books = []

    while True:
        print("\nSimple Library Management System")
        print("1. Add Book")
        print("2. List All Books")
        print("3. Search Books by Title/Author")
        print("4. Borrow Book")
        print("5. Return Book")
        print("6. List All Genres")
        print("7. Exit")

        choice = get_input("Enter your choice (1-7): ")

        if choice == "1":
            title = get_input("Title: ")
            author = get_input("Author: ")
            year = int(get_input("Year: "))
            genres = set(get_input("Genres (comma-separated): ").split(","))
            add_book(books, title, author, year, genres)

        elif choice == "2":
            list_books(books)

        elif choice == "3":
            keyword = get_input("Enter keyword to search (title/author): ")
            search_books(books, keyword)

        elif choice == "4":
            title = get_input("Enter title to borrow: ")
            borrow_book(books, title)

        elif choice == "5":
            title = get_input("Enter title to return: ")
            return_book(books, title)

        elif choice == "6":
            list_genres(books)

        elif choice == "7":
            print("Exiting Library System.")
            break

        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
