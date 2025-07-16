# 5. Library Book Catalog
# Description: Manage books in a library.
# Requirements:
# - Book info: {book_id: {"title": ..., "author": ..., "copies": ...}}
# - Add new book
# - Borrow book: reduce copies
# - Return book: increase copies
# - Delete book if copies = 0
# - Use .get() to avoid missing key errors
# - Use .items() to display list of available books

library = {
    101: {"title": "The Alchemist", "author": "Paulo Coelho", "copies": 3},
    102: {"title": "1984", "author": "George Orwell", "copies": 2},
    103: {"title": "To Kill a Mockingbird", "author": "Harper Lee", "copies": 1}
}

def add_book(book_id, title, author, copies):
    if book_id not in library:
        library[book_id] = {"title": title, "author": author, "copies": copies}
        print(f"Book '{title}' added.")
    else:
        print("Book ID already exists.")

def borrow_book(book_id):
    book = library.get(book_id)
    if book and book["copies"] > 0:
        book["copies"] -= 1
        print(f"Borrowed '{book['title']}'")
        if book["copies"] == 0:
            del library[book_id]
            print(f"'{book['title']}' removed (no more copies).")
    else:
        print("Book not available or invalid ID.")

def return_book(book_id, title, author):
    if book_id in library:
        library[book_id]["copies"] += 1
        print(f"Returned '{library[book_id]['title']}'")
    else:
        library[book_id] = {"title": title, "author": author, "copies": 1}
        print(f"New book '{title}' returned and added to catalog.")

def show_books():
    print("\nAvailable Books:")
    for book_id, info in library.items():
        print(f"{book_id}: {info['title']} by {info['author']} (Copies: {info['copies']})")

add_book(104, "Sapiens", "Yuval Noah Harari", 4)
borrow_book(101)
borrow_book(103)
return_book(103, "To Kill a Mockingbird", "Harper Lee")
show_books()
