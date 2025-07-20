import json
from datetime import datetime

FILENAME = "diary.json"

def load_entries():
    try:
        with open(FILENAME, "r") as f:
            data = json.load(f)
            for entry in data:
                entry["tags"] = set(entry["tags"])
            return data
    except FileNotFoundError:
        return []

def save_entries(entries):
    with open(FILENAME, "w") as f:
        serializable = [{"date": e["date"], "text": e["text"], "tags": list(e["tags"])} for e in entries]
        json.dump(serializable, f, indent=2)

def add_entry(entries):
    text = input("Entry text: ").strip()
    tags = set(input("Tags (comma-separated): ").lower().split(","))
    date = datetime.now().strftime("%Y-%m-%d")
    entries.append({"date": date, "text": text, "tags": tags})
    print(" Entry added.")

def edit_entry(entries):
    date = input("Enter date to edit (YYYY-MM-DD): ").strip()
    found = False
    for entry in entries:
        if entry["date"] == date:
            entry["text"] = input("New text: ").strip()
            entry["tags"] = set(input("New tags (comma-separated): ").lower().split(","))
            print(" Entry updated.")
            found = True
            break
    if not found:
        print(" Entry not found.")

def delete_entry(entries):
    date = input("Enter date to delete: ").strip()
    for i, entry in enumerate(entries):
        if entry["date"] == date:
            del entries[i]
            print(" Entry deleted.")
            return
    print(" Entry not found.")

def search_by_tag(entries):
    tag = input("Enter tag to search: ").strip().lower()
    found = False
    for entry in entries:
        if tag in entry["tags"]:
            print(f" {entry['date']}: {entry['text']}")
            found = True
    if not found:
        print("No entries found with that tag.")

def search_by_date(entries):
    date = input("Enter date (YYYY-MM-DD): ").strip()
    for entry in entries:
        if entry["date"] == date:
            print(f"{entry['date']}: {entry['text']} (Tags: {', '.join(entry['tags'])})")
            return
    print("No entry found on that date.")

def show_summary(entries):
    print(f" Total entries: {len(entries)}")
    all_tags = set()
    for entry in entries:
        all_tags |= entry["tags"]
    print(f" Unique tags used: {', '.join(sorted(all_tags)) if all_tags else 'None'}")
