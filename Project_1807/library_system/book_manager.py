# book_manager.py

from data.genres import available_genres

def add_book(books, isbn, title, author, genre):
    if genre not in available_genres:
        print(f"Genre '{genre}' is not available.")
        return
    if isbn in books:
        print("Book already exists.")
        return
    books[isbn] = {
        "title": title,
        "author": author,
        "genre": genre
    }
    print(f"Book '{title}' added.")

def view_books(books):
    if not books:
        print("No books available.")
        return
    for isbn, info in books.items():
        print(f"\nISBN: {isbn[0]}")
        print(f"Title: {info['title']}")
        print(f"Author: {info['author']}")
        print(f"Genre: {info['genre']}")
