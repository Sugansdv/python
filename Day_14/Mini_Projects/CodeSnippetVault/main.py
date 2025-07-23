import os
import json

VAULT_FILE = "snippets.json"
SNIPPET_DIR = "snippets"


def load_snippets():
    if not os.path.exists(VAULT_FILE):
        return []
    with open(VAULT_FILE, "r") as f:
        return json.load(f)


def save_snippets(snippets):
    with open(VAULT_FILE, "w") as f:
        json.dump(snippets, f, indent=4)


def add_snippet():
    title = input("Title: ")
    description = input("Description: ")
    code = input("Code:\n")
    tags = input("Tags (comma-separated): ").split(',')

    snippet = {
        "title": title.strip(),
        "description": description.strip(),
        "code": code,
        "tags": [t.strip() for t in tags]
    }

    # Save to JSON
    snippets = load_snippets()
    snippets.append(snippet)
    save_snippets(snippets)

    # Save to .txt files in tag folders
    for tag in snippet["tags"]:
        folder = os.path.join(SNIPPET_DIR, tag)
        os.makedirs(folder, exist_ok=True)
        filename = os.path.join(folder, f"{title.replace(' ', '_')}.txt")
        with open(filename, "w") as f:
            f.write(f"Title: {title}\n")
            f.write(f"Description: {description}\n")
            f.write("Code:\n")
            f.write(code)
    print("Snippet saved successfully.\n")


def search_snippets():
    query = input("Search by tag or title: ").lower()
    snippets = load_snippets()
    results = [
        snip for snip in snippets
        if query in snip["title"].lower() or query in [t.lower() for t in snip["tags"]]
    ]

    if not results:
        print("No matching snippets found.\n")
        return

    for snip in results:
        print(f"Title: {snip['title']}")
        print(f"Description: {snip['description']}")
        print("Code:")
        print(snip['code'])
        print("Tags:", ', '.join(snip['tags']))
        print('-' * 40)


def menu():
    while True:
        print("\n--- Code Snippet Vault ---")
        print("1. Add Snippet")
        print("2. Search Snippets")
        print("3. Exit")

        choice = input("Choose an option: ")
        if choice == '1':
            add_snippet()
        elif choice == '2':
            search_snippets()
        elif choice == '3':
            break
        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    os.makedirs(SNIPPET_DIR, exist_ok=True)
    menu()
