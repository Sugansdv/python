def add_book(books, title, author, year, genres):
    book_info = (title, author, year)
    books.append({
        "info": book_info,
        "genres": set(genres),
        "available": True
    })
    print(f"Book '{title}' added.")

def search_books(books, keyword):
    keyword = keyword.lower()
    found = False
    for book in books:
        title, author, _ = book["info"]
        if keyword in title.lower() or keyword in author.lower():
            status = "Available" if book["available"] else "Borrowed"
            print(f"{title} by {author} - {status}")
            found = True
    if not found:
        print("No matching books found.")

def list_books(books):
    if not books:
        print("No books in library.")
        return
    for book in books:
        title, author, year = book["info"]
        status = "Available" if book["available"] else "Borrowed"
        print(f"{title} ({year}) by {author} - {status}")

def list_genres(books):
    genres = set()
    for book in books:
        genres.update(book["genres"])
    print("Genres:", ", ".join(sorted(genres)))
