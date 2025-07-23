import os
from datetime import datetime

DIARY_FOLDER = "diary_entries"

def get_file_path(date_str=None):
    """Returns the diary file path for today or a specific date (YYYY-MM-DD)."""
    if not os.path.exists(DIARY_FOLDER):
        os.makedirs(DIARY_FOLDER)
    if date_str is None:
        date_str = datetime.now().strftime("%Y-%m-%d")
    return os.path.join(DIARY_FOLDER, f"{date_str}.txt")

def write_today_entry():
    """Prompt user to write today's diary entry and save it."""
    file_path = get_file_path()
    print(f"\n Writing diary entry for {datetime.now().strftime('%Y-%m-%d')}")
    entry = input("Enter your diary note:\n")
    
    try:
        with open(file_path, "a") as f:
            f.write(entry + "\n")
        print(" Entry saved successfully.")
    except Exception as e:
        print(" Failed to save entry:", e)

def view_entry():
    """View entry for a specific date."""
    date_str = input("Enter date to view (YYYY-MM-DD): ")
    file_path = get_file_path(date_str)
    
    try:
        with open(file_path, "r") as f:
            print("\n Diary Entry:\n" + f.read())
    except FileNotFoundError:
        print(" No entry found for that date.")
    except Exception as e:
        print(" Error reading file:", e)

def edit_entry():
    """Edit (overwrite) a diary entry for a specific date."""
    date_str = input("Enter date to edit (YYYY-MM-DD): ")
    file_path = get_file_path(date_str)

    if not os.path.exists(file_path):
        print(" No existing entry to edit.")
        return

    print("\n🖊️ Current Entry:")
    with open(file_path, "r") as f:
        print(f.read())

    new_content = input("\nEnter new content to overwrite:\n")
    try:
        with open(file_path, "w") as f:
            f.write(new_content + "\n")
        print(" Entry updated.")
    except Exception as e:
        print(" Failed to update:", e)

def main():
    while True:
        print("\n=== Simple Diary App ===")
        print("1. Write today's entry")
        print("2. View an entry")
        print("3. Edit an entry")
        print("4. Exit")
        choice = input("Choose (1-4): ")

        if choice == "1":
            write_today_entry()
        elif choice == "2":
            view_entry()
        elif choice == "3":
            edit_entry()
        elif choice == "4":
            print(" Goodbye!")
            break
        else:
            print(" Invalid choice.")

if __name__ == "__main__":
    main()
