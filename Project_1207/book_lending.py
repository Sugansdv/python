# 19. Book Lending App
# Concepts: lists, while, functions.
# • Books available in a list.
# • Borrow books (remove from list).
# • Return books (add to list).
# • Menu-driven loop.

books = ["Harry Potter", "The Hobbit", "1984", "To Kill a Mockingbird"]

def show_books():
    if books:
        print("\nAvailable Books:")
        for i, book in enumerate(books, start=1):
            print(f"{i}. {book}")
    else:
        print("\nNo books currently available.")

def borrow_book():
    show_books()
    choice = input("Enter the name of the book to borrow: ")
    if choice in books:
        books.remove(choice)
        print(f"You borrowed '{choice}'\n")
    else:
        print("Book not available.\n")

def return_book():
    book = input("Enter the name of the book to return: ")
    books.append(book)
    print(f"'{book}' returned successfully.\n")

while True:
    print("1. Show Available Books")
    print("2. Borrow a Book")
    print("3. Return a Book")
    print("4. Exit")
    option = input("Choose an option: ")

    if option == "1":
        show_books()
    elif option == "2":
        borrow_book()
    elif option == "3":
        return_book()
    elif option == "4":
        break
    else:
        print("Invalid choice.\n")
