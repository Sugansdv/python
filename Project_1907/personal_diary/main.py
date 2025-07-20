from modules.diary_ops import add_entry, edit_entry, delete_entry, search_by_tag, search_by_date, show_summary, load_entries, save_entries

def main():
    entries = load_entries()

    while True:
        print("\n Personal Diary")
        print("1. Add Entry")
        print("2. Edit Entry")
        print("3. Delete Entry")
        print("4. Search by Tag")
        print("5. Search by Date")
        print("6. Show Summary")
        print("7. Exit")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            add_entry(entries)
        elif choice == "2":
            edit_entry(entries)
        elif choice == "3":
            delete_entry(entries)
        elif choice == "4":
            search_by_tag(entries)
        elif choice == "5":
            search_by_date(entries)
        elif choice == "6":
            show_summary(entries)
        elif choice == "7":
            save_entries(entries)
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
