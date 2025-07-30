import json
import os
from core.book import Book
from core.decorators import admin_only

class Library:
    def __init__(self, filepath="data/books.json"):
        self.filepath = filepath
        self.books = []
        self.load_books()

    def load_books(self):
        if os.path.exists(self.filepath):
            try:
                with open(self.filepath, "r") as f:
                    content = f.read().strip()
                    if content:
                        data = json.loads(content)
                        self.books = [Book.from_dict(b) for b in data]
                    else:
                        self.books = []
            except json.JSONDecodeError:
                print("Corrupted JSON. Starting with empty library.")
                self.books = []
        else:
            self.books = []

    def save_books(self):
        with open(self.filepath, "w") as f:
            json.dump([book.to_dict() for book in self.books], f, indent=4)

    def add_book(self, book):
        self.books.append(book)
        self.save_books()

    def borrow_book(self, title, borrower):
        for book in self.books:
            if book.title.lower() == title.lower():
                if book.available:
                    book.available = False
                    book.borrower = borrower
                    self.save_books()
                    print(f"You borrowed '{book.title}'")
                    return
                else:
                    print("Book already borrowed.")
                    return
        raise ValueError("Book not found.")

    def return_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                if not book.available:
                    book.available = True
                    book.borrower = None
                    self.save_books()
                    print(f"Returned '{book.title}'")
                    return
                else:
                    print("This book wasn't borrowed.")
                    return
        raise ValueError("Book not found.")

    def search_books(self, keyword):
        found = [book for book in self.books if keyword.lower() in book.title.lower()]
        return found

    def list_available_books(self):
        for book in self.books:
            if book.available:
                print(book)

    def __iter__(self):
        return (book for book in self.books if book.available)

    @admin_only
    def delete_book(self, title):
        self.books = [b for b in self.books if b.title.lower() != title.lower()]
        self.save_books()
        print(f"Book '{title}' deleted.")
