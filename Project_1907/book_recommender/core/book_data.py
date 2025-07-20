def load_books():
    books = [
        { "id": ("The Hobbit", "J.R.R. Tolkien"), "genres": {"Fantasy", "Adventure"} },
        { "id": ("1984", "George Orwell"), "genres": {"Dystopian", "Political"} },
        { "id": ("To Kill a Mockingbird", "Harper Lee"), "genres": {"Classic", "Drama"} },
        { "id": ("Brave New World", "Aldous Huxley"), "genres": {"Dystopian", "Science Fiction"} },
        { "id": ("The Fellowship of the Ring", "J.R.R. Tolkien"), "genres": {"Fantasy", "Adventure"} }
    ]

    genre_map = {}

    for book in books:
        for genre in book["genres"]:
            genre_map.setdefault(genre, []).append(book)

    return books, genre_map
