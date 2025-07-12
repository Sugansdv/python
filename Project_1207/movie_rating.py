# 16. Movie Rating Collector
# Concepts: list, while, strings, functions.
# • Collect movie names and user ratings.
# • Store in nested lists.
# • Show top-rated movies.

movies = []

def add_movie():
    name = input("Enter movie name: ")
    rating = input("Enter your rating (0-10): ")
    if rating.replace('.', '', 1).isdigit():
        rating = float(rating)
        if 0 <= rating <= 10:
            movies.append([name, rating])
        else:
            print("Rating must be between 0 and 10.\n")
    else:
        print("Invalid rating.\n")

def show_top_movies():
    if not movies:
        print("No movies rated yet.\n")
        return
    sorted_movies = sorted(movies, key=lambda x: x[1], reverse=True)
    print("\n--- Top Rated Movies ---")
    for i, movie in enumerate(sorted_movies, start=1):
        print(f"{i}. {movie[0]} - {movie[1]}/10")
    print()

while True:
    print("1. Add Movie Rating")
    print("2. Show Top Rated Movies")
    print("3. Exit")
    choice = input("Choose an option: ")

    if choice == "1":
        add_movie()
    elif choice == "2":
        show_top_movies()
    elif choice == "3":
        break
    else:
        print("Invalid option.\n")
