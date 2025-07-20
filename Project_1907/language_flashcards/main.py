from modules.card_ops import add_flashcard, review_flashcards, delete_flashcard, quiz_mode
from modules.stats import show_stats

flashcards = []  # List of tuples: (word, translation, category)
categories = set()
quiz_results = {"correct": 0, "incorrect": 0}

def main():
    print("Welcome to Language Flashcards App")

    while True:
        print("\nMenu:")
        print("1. Add Flashcard")
        print("2. Review Flashcards")
        print("3. Delete Flashcard")
        print("4. Quiz Mode")
        print("5. Show Quiz Stats")
        print("6. Exit")
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            add_flashcard(flashcards, categories)
        elif choice == "2":
            review_flashcards(flashcards)
        elif choice == "3":
            delete_flashcard(flashcards)
        elif choice == "4":
            quiz_mode(flashcards, quiz_results)
        elif choice == "5":
            show_stats(quiz_results)
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
