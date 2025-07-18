

def search_by_genre(books, genre):
    found = False
    for book in books.values():
        if book['genre'].lower() == genre.lower():
            print(f"\nTitle: {book['title']} | Author: {book['author']}")
            found = True
    if not found:
        print(f"No books found in genre '{genre}'.")
