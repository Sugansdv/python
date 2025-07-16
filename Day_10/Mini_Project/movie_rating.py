# 9. Movie Rating System
# Description: Collect user ratings for movies.
# Requirements:
# - {movie_name: {"ratings": [int, int], "genre": ..., "avg_rating": float}}
# - Update ratings list
# - Recalculate average
# - Sort movies by avg_rating
# - Use dictionary comprehension to filter by genre

movies = {
    "Inception": {"ratings": [5, 4, 5], "genre": "Sci-Fi", "avg_rating": 4.67},
    "Titanic": {"ratings": [4, 5, 4], "genre": "Romance", "avg_rating": 4.33},
    "Interstellar": {"ratings": [5, 5], "genre": "Sci-Fi", "avg_rating": 5.00}
}

def add_rating(movie_name, rating):
    if movie_name in movies:
        movies[movie_name]["ratings"].append(rating)
        recalculate_average(movie_name)
        print(f"Rating added for '{movie_name}'.")
    else:
        print("Movie not found.")

def recalculate_average(movie_name):
    ratings = movies[movie_name]["ratings"]
    avg = sum(ratings) / len(ratings)
    movies[movie_name]["avg_rating"] = round(avg, 2)

def sort_by_average():
    sorted_movies = sorted(movies.items(), key=lambda x: x[1]["avg_rating"], reverse=True)
    print("\nMovies Sorted by Average Rating:")
    for name, info in sorted_movies:
        print(f"{name}: Avg Rating = {info['avg_rating']}")

def filter_by_genre(genre):
    genre_movies = {name: info for name, info in movies.items() if info["genre"].lower() == genre.lower()}
    print(f"\nMovies in Genre '{genre}':")
    for name, info in genre_movies.items():
        print(f"{name} → Avg Rating: {info['avg_rating']}")

add_rating("Titanic", 5)
add_rating("Inception", 4)
sort_by_average()
filter_by_genre("Sci-Fi")
