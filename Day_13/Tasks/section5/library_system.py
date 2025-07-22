class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.available = True


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        print(f"Added '{book.title}' to the library.")

    def search_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                return book
        return None

    def borrow_book(self, title):
        book = self.search_book(title)
        if book and book.available:
            book.available = False
            print(f"You borrowed '{book.title}'")
        elif book:
            print("Book is already borrowed.")
        else:
            print("Book not found.")

    def return_book(self, title):
        book = self.search_book(title)
        if book and not book.available:
            book.available = True
            print(f"Returned '{book.title}' successfully.")
        elif book:
            print("This book was not borrowed.")
        else:
            print("Book not found.")

# Example
lib = Library()
lib.add_book(Book("Python 101", "Mike"))
lib.add_book(Book("OOP in Python", "Jane"))
lib.borrow_book("Python 101")
lib.return_book("Python 101")
