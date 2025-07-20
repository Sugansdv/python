def search_by_actor(collection):
    name = input("Enter actor name: ").strip().lower()
    results = [m for m in collection if any(name in a.lower() for a in m["actors"])]
    if not results:
        print("No movies found.")
    for m in results:
        print(f"{m['title']} ({m['year']}) - Actors: {', '.join(m['actors'])}")

def search_by_genre(collection):
    genre = input("Enter genre: ").strip().lower()
    results = [m for m in collection if genre in (g.lower() for g in m["genres"])]
    if not results:
        print("No movies found.")
    for m in results:
        print(f"{m['title']} ({m['year']}) - Genres: {', '.join(m['genres'])}")
