# main.py

from book_manager import add_book, view_books
from user_manager import search_by_genre

def main():
    books = {}

    while True:
        print("\n--- Library System ---")
        print("1. Add Book")
        print("2. View All Books")
        print("3. Search by Genre")
        print("4. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            isbn_input = input("Enter ISBN: ")
            isbn = (isbn_input,)
            title = input("Enter book title: ")
            author = input("Enter author name: ")
            genre = input("Enter genre: ")
            add_book(books, isbn, title, author, genre)

        elif choice == "2":
            view_books(books)

        elif choice == "3":
            genre = input("Enter genre to search: ")
            search_by_genre(books, genre)

        elif choice == "4":
            print("Exiting system.")
            break

        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
