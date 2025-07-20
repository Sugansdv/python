import random

def recommend_by_genre(genre_map, genre):
    genre = genre.strip()
    if genre in genre_map:
        options = genre_map[genre]
        rec = random.choice(options)
        print(f"📚 Recommended: '{rec['id'][0]}' by {rec['id'][1]}")
    else:
        print("No books found in that genre.")

def recommend_by_author(books, author):
    matches = [b for b in books if b["id"][1].lower() == author.lower()]
    if matches:
        rec = random.choice(matches)
        print(f"📖 Try: '{rec['id'][0]}' by {rec['id'][1]}")
    else:
        print("No books found by that author.")
