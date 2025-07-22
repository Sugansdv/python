from datetime import datetime, timedelta
from abc import ABC, abstractmethod

# ---------------- Book Class ----------------
class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_available = True

    def __str__(self):
        return f"'{self.title}' by {self.author} (ISBN: {self.isbn})"

# ---------------- Member Abstract Class ----------------
class Member(ABC):
    def __init__(self, name, member_id):
        self.__name = name                 # private
        self.__member_id = member_id      # private
        self.borrowed_books = []

    @abstractmethod
    def borrow_book(self, book, library): pass

    @abstractmethod
    def return_book(self, book, library): pass

    def get_member_info(self):
        return f"Name: {self.__name}, ID: {self.__member_id}"

# ---------------- Librarian Class ----------------
class Librarian(Member):
    def borrow_book(self, book, library):
        print("Librarians do not borrow books.")

    def return_book(self, book, library):
        print("Librarians do not return books.")

    def add_book(self, book, library):
        library.books.append(book)
        print(f"Book added: {book}")

    def remove_book(self, isbn, library):
        for b in library.books:
            if b.isbn == isbn:
                library.books.remove(b)
                print(f"Book removed: {b}")
                return
        print("Book not found.")

# ---------------- RegularMember Class ----------------
class RegularMember(Member):
    def borrow_book(self, book, library):
        if book.is_available:
            book.is_available = False
            self.borrowed_books.append(book)
            library.transactions.append(Transaction("borrow", self, book))
            print(f"{self.get_member_info()} borrowed {book}")
        else:
            print(f"{book} is currently unavailable.")

    def return_book(self, book, library):
        if book in self.borrowed_books:
            book.is_available = True
            self.borrowed_books.remove(book)
            library.transactions.append(Transaction("return", self, book))
            print(f"{self.get_member_info()} returned {book}")
        else:
            print("You didn't borrow this book.")

# ---------------- Transaction Class ----------------
class Transaction:
    def __init__(self, type, member, book):
        self.type = type
        self.member = member
        self.book = book
        self.date = datetime.now()
        self.due_date = self.date + timedelta(days=14) if type == "borrow" else None

    def __str__(self):
        action = "Borrowed" if self.type == "borrow" else "Returned"
        return f"{action} {self.book} on {self.date.strftime('%Y-%m-%d')}"

# ---------------- Library Class ----------------
class Library:
    def __init__(self, name):
        self.name = name
        self.books = []
        self.transactions = []

    def __len__(self):
        return len(self.books)

    def search_book(self, keyword):
        result = [book for book in self.books if keyword.lower() in book.title.lower() or keyword.lower() in book.author.lower()]
        return result

    def __str__(self):
        return f"{self.name} Library with {len(self)} books"

# ---------------- Testing ----------------
if __name__ == "__main__":
    # Create Library
    my_library = Library("City Central")

    # Create Librarian
    lib = Librarian("Alice", "L001")

    # Add Books
    book1 = Book("Python Programming", "John Zelle", "1111")
    book2 = Book("Clean Code", "Robert C. Martin", "2222")
    book3 = Book("The Alchemist", "Paulo Coelho", "3333")

    lib.add_book(book1, my_library)
    lib.add_book(book2, my_library)
    lib.add_book(book3, my_library)

    # Create Member
    member = RegularMember("Bob", "M001")

    # Search Books
    print("\nSearch Results for 'Python':")
    for b in my_library.search_book("Python"):
        print(b)

    # Borrow and Return
    print("\nBorrowing:")
    member.borrow_book(book1, my_library)
    member.borrow_book(book2, my_library)

    print("\nReturning:")
    member.return_book(book1, my_library)

    # Remove a book
    print("\nRemove Book:")
    lib.remove_book("3333", my_library)

    # View Transactions
    print("\nTransaction History:")
    for t in my_library.transactions:
        print(t)

    # Show Library Summary
    print(f"\n{my_library}")
