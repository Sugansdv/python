import os

BASE_DIR = "notes"

def create_category(category):
    path = os.path.join(BASE_DIR, category)
    os.makedirs(path, exist_ok=True)
    return path

def save_note():
    category = input("Enter category (e.g., Work, Personal): ").strip()
    title = input("Enter note title: ").strip()
    content = input("Enter note content:\n")

    folder = create_category(category)
    filepath = os.path.join(folder, f"{title}.txt")

    with open(filepath, "w") as f:
        f.write(content)

    print(f"✅ Note '{title}' saved in category '{category}'.")

def view_notes_by_category():
    category = input("Enter category to view: ").strip()
    folder = os.path.join(BASE_DIR, category)

    if not os.path.exists(folder):
        print("❌ Category not found.")
        return

    files = os.listdir(folder)
    if not files:
        print("📭 No notes found in this category.")
        return

    print(f"\n📂 Notes in category '{category}':")
    for file in files:
        print(f"- {file[:-4]}")  # Remove .txt extension

def search_notes():
    keyword = input("Enter keyword to search: ").lower()

    if not os.path.exists(BASE_DIR):
        print("⚠️ No notes available.")
        return

    print(f"\n🔍 Searching for '{keyword}'...")
    found = False

    for root, _, files in os.walk(BASE_DIR):
        for file in files:
            if file.endswith(".txt"):
                filepath = os.path.join(root, file)
                with open(filepath, "r") as f:
                    content = f.read().lower()
                    if keyword in content or keyword in file.lower():
                        print(f"✔️ Found in '{file[:-4]}' (Category: {os.path.basename(root)})")
                        found = True

    if not found:
        print("❌ No matching notes found.")

def main():
    while True:
        print("\n🗂️ Notes Organizer Menu")
        print("1. Save Note")
        print("2. View Notes by Category")
        print("3. Search Notes")
        print("4. Exit")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            save_note()
        elif choice == "2":
            view_notes_by_category()
        elif choice == "3":
            search_notes()
        elif choice == "4":
            print("👋 Exiting Notes Organizer.")
            break
        else:
            print("❌ Invalid choice. Try again.")

if __name__ == "__main__":
    main()
