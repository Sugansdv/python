from core.recommendation import recommend_by_genre, recommend_by_author
from core.book_data import load_books

def main():
    books, genre_map = load_books()

    while True:
        print("\nBook Recommendation System")
        print("1. Recommend by Genre")
        print("2. Recommend by Author")
        print("3. Exit")
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            genre = input("Enter a genre: ").strip()
            recommend_by_genre(genre_map, genre)
        elif choice == "2":
            author = input("Enter an author name: ").strip()
            recommend_by_author(books, author)
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
