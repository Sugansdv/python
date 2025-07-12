#  19. Book Reading Progress Tracker
# Description: Track books and reading progress.

# Use nested list for [book name, pages read, total pages]
books = [
    ["Atomic Habits", 120, 250],
    ["The Alchemist", 208, 208],
    ["Deep Work", 50, 300]
]

# Display current reading progress
print("Reading Progress:")
for book in books:
    name, read, total = book
    print(f"- {name}: {read}/{total} pages read")

# Update page count (e.g., +30 pages in Deep Work)
for book in books:
    if book[0] == "Deep Work":
        book[1] += 30  # Add 30 pages read
        print(f"\n Updated '{book[0]}' to {book[1]}/{book[2]} pages")

# Check if a book is finished (pages read == total pages)
print("\n Finished Books:")
for book in books:
    if book[1] >= book[2]:
        print(f"- {book[0]} is completed! ")
    else:
        print(f"- {book[0]} is still in progress.")

# Optional: Display final status neatly
print("\n Final Progress Tracker:")
for book in books:
    name, read, total = book
    status = " Completed" if read >= total else "In Progress"
    print(f"{name}: {read}/{total} pages - {status}")
