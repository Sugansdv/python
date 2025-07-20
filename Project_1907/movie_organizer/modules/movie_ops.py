def add_movie(collection):
    title = input("Title: ").strip()
    year = input("Year: ").strip()
    genres = set(input("Genres (comma-separated): ").strip().split(','))
    actors = input("Actors (comma-separated): ").strip().split(',')
    movie = {
        "id": (title, year),
        "title": title,
        "year": year,
        "genres": set(g.strip() for g in genres),
        "actors": [a.strip() for a in actors]
    }
    collection.append(movie)
    print("Movie added.")

def list_movies(collection):
    if not collection:
        print("No movies in collection.")
        return
    for m in collection:
        print(f"Title: {m['title']}, Year: {m['year']}, Genres: {', '.join(m['genres'])}, Actors: {', '.join(m['actors'])}")

def group_by_genre(collection):
    genre_dict = {}
    for m in collection:
        for genre in m["genres"]:
            genre_dict.setdefault(genre, []).append(m)
    for genre, movies in genre_dict.items():
        print(f"\nGenre: {genre}")
        for m in movies:
            print(f" - {m['title']} ({m['year']})")
