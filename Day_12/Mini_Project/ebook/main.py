from library import catalog, search, reader

def main():
    while True:
        print("\n eBook Library Organizer")
        print("1. List all eBooks")
        print("2. Search eBooks")
        print("3. Read an eBook (txt only)")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            books = catalog.list_books()
            if books:
                print("\nAvailable eBooks:")
                for idx, book in enumerate(books, 1):
                    print(f"{idx}. {book}")
            else:
                print("No eBooks found.")

        elif choice == '2':
            keyword = input("Enter keyword to search: ")
            matches = search.search_books(keyword)
            if matches:
                print("Matching eBooks:")
                for book in matches:
                    print(f"- {book}")
            else:
                print("No matches found.")

        elif choice == '3':
            book_name = input("Enter book name (e.g., sample1.txt): ")
            reader.read_book(book_name)

        elif choice == '4':
            print("Goodbye!")
            break

        else:
            print("Invalid option. Try again.")

if __name__ == "__main__":
    main()
