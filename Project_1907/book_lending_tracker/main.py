from modules.lending_ops import add_book, return_book, check_overdue
from modules.reminder_ops import send_reminders

books = {}  # title → (borrower, due_date)
borrowers = set()

def main():
    print(" Book Lending Tracker")
    while True:
        print("\nMenu:")
        print("1. Add Book")
        print("2. Return Book")
        print("3. Check Overdue")
        print("4. Send Reminders")
        print("5. Exit")

        choice = input("Enter choice: ").strip()

        if choice == "1":
            add_book(books, borrowers)
        elif choice == "2":
            return_book(books, borrowers)
        elif choice == "3":
            check_overdue(books)
        elif choice == "4":
            send_reminders(books)
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid option.")
            
if __name__ == "__main__":
    main()
