# 23. Mini File Organizer (Mock)
# Concepts: string list, functions.
# • Input file names.
# • Categorize by extension (.jpg, .txt).
# • Show summary.

files = []

def add_files():
    count = int(input("How many files to input? "))
    for _ in range(count):
        filename = input("Enter file name with extension: ")
        files.append(filename)

def organize_files():
    categories = {}
    for f in files:
        parts = f.lower().split(".")
        if len(parts) > 1:
            ext = parts[-1]
            categories.setdefault(ext, []).append(f)
    return categories

def show_summary():
    organized = organize_files()
    print("\n--- File Summary by Extension ---")
    for ext, items in organized.items():
        print(f".{ext}: {len(items)} file(s)")
        for file in items:
            print(f"  - {file}")
    print()

while True:
    print("1. Add Files")
    print("2. Show Summary")
    print("3. Exit")
    choice = input("Choose an option: ")

    if choice == "1":
        add_files()
    elif choice == "2":
        show_summary()
    elif choice == "3":
        break
    else:
        print("Invalid choice.\n")
