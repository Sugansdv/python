def search_movie(collection, keyword):
    results = []
    for movie in collection:
        if keyword.lower() in movie['title'].lower():
            results.append(movie)
    return results
