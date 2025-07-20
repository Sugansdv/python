from modules.movie_ops import add_movie, list_movies, group_by_genre
from modules.search_ops import search_by_actor, search_by_genre

movie_collection = []

def main():
    while True:
        print("\nMovie Collection Organizer")
        print("1. Add Movie")
        print("2. List All Movies")
        print("3. Group by Genre")
        print("4. Search by Actor")
        print("5. Search by Genre")
        print("6. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            add_movie(movie_collection)
        elif choice == "2":
            list_movies(movie_collection)
        elif choice == "3":
            group_by_genre(movie_collection)
        elif choice == "4":
            search_by_actor(movie_collection)
        elif choice == "5":
            search_by_genre(movie_collection)
        elif choice == "6":
            break
        else:
            print("Invalid choice.")
            
if __name__ == "__main__":
    main()
