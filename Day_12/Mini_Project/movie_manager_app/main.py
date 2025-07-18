from movies import *
from pprint import pprint

def main():
    movies = load_movies()
    while True:
        print("\n--- Movie Collection Manager ---")
        print("1. Add Movie")
        print("2. Remove Movie")
        print("3. View All Movies")
        print("4. Add Rating")
        print("5. View Ratings")
        print("6. Search Movie")
        print("7. Export to CSV")
        print("8. Exit")

        choice = input("Choose: ")
        if choice == '1':
            title = input("Title: ")
            genre = input("Genre: ")
            year = input("Year: ")
            add_movie(movies, title, genre, year)
        elif choice == '2':
            title = input("Enter title to remove: ")
            movies = remove_movie(movies, title)
        elif choice == '3':
            view_movies(movies)
        elif choice == '4':
            title = input("Enter movie title to rate: ")
            rating = input("Rating (1-5): ")
            if not add_rating(movies, title, rating):
                print("Movie not found.")
        elif choice == '5':
            view_ratings(movies)
        elif choice == '6':
            keyword = input("Search keyword: ")
            results = search_movie(movies, keyword)
            pprint(results)
        elif choice == '7':
            export_movies(movies)
            print("Exported to movies/export.csv")
        elif choice == '8':
            save_movies(movies)
            print("Saved and exiting...")
            break

if __name__ == "__main__":
    main()
