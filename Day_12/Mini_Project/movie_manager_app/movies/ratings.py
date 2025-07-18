def add_rating(collection, title, rating):
    for movie in collection:
        if movie['title'].lower() == title.lower():
            movie['rating'] = rating
            return True
    return False

def view_ratings(collection):
    for movie in collection:
        print(f"{movie['title']} → Rating: {movie['rating']}")
