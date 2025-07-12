# 5. Library Book Catalog
# Description: Track books in a library.

# Create a list of books (each as [title, author])
books = [
    ["The Alchemist", "Paulo Coelho"],
    ["1984", "George Orwell"],
    ["To Kill a Mockingbird", "Harper Lee"]
]

# Function to display all books
def display_books():
    print("\nCurrent Book Catalog:")
    for i, book in enumerate(books, start=1):
        print(f"{i}. {book[0]} by {book[1]}")

# Display initial catalog
display_books()

# Add a new book
books.append(["Atomic Habits", "James Clear"])
print("\nAdded new book: 'Atomic Habits' by James Clear")

# Update book details (change author of '1984')
for book in books:
    if book[0] == "1984":
        book[1] = "G. Orwell"
        print("Updated author for '1984'.")

# Remove a book
book_to_remove = "To Kill a Mockingbird"
for book in books:
    if book[0] == book_to_remove:
        books.remove(book)
        print(f"Removed book: '{book_to_remove}'")
        break

# Search for a book using `in` and index()
search_title = "The Alchemist"
titles = [book[0] for book in books]
if search_title in titles:
    index = titles.index(search_title)
    print(f"\nFound '{search_title}' at index {index}: {books[index]}")
else:
    print(f"\nBook '{search_title}' not found.")

# Slice list for "recent additions" (last 2 books)
recent_books = books[-2:]
print("\nRecent Additions:")
for title, author in recent_books:
    print(f"- {title} by {author}")

# Final catalog display
display_books()
