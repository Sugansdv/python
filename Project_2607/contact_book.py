import csv
import json
import os

CONTACTS_FILE = "contacts.json"

def load_contacts():
    if os.path.exists(CONTACTS_FILE):
        with open(CONTACTS_FILE, 'r') as f:
            return json.load(f)
    return []

def save_contacts(contacts):
    with open(CONTACTS_FILE, 'w') as f:
        json.dump(contacts, f, indent=4)

def add_contact(contacts):
    name = input("Enter Name: ").strip()
    phone = input("Enter Phone Number: ").strip()
    email = input("Enter Email: ").strip()
    category = input("Enter Category (e.g., Family, Work, Friends): ").strip()

    contact = {
        "name": name,
        "phone": phone,
        "email": email,
        "category": category
    }
    contacts.append(contact)
    print(" Contact added.")

def view_contacts(contacts, group_by=None):
    if not contacts:
        print("📭 No contacts to display.")
        return

    if group_by:
        grouped = {}
        for c in contacts:
            key = c[group_by].capitalize()
            grouped.setdefault(key, []).append(c)

        for category, group in grouped.items():
            print(f"\n {category}:")
            for i, contact in enumerate(group, 1):
                print(f"{i}. {contact['name']} | {contact['phone']} | {contact['email']}")
    else:
        print("\n Contact List:")
        for i, contact in enumerate(contacts, 1):
            print(f"{i}. {contact['name']} | {contact['phone']} | {contact['email']} | {contact['category']}")

def search_contacts(contacts):
    query = input("Enter name or phone to search: ").strip().lower()
    found = [c for c in contacts if query in c['name'].lower() or query in c['phone']]
    if found:
        print("\n Search Results:")
        view_contacts(found)
    else:
        print(" No matching contacts found.")

def edit_contact(contacts):
    view_contacts(contacts)
    try:
        index = int(input("Enter contact number to edit: ")) - 1
        if index < 0 or index >= len(contacts):
            raise ValueError
        print("Enter new values (leave blank to keep existing):")
        contact = contacts[index]

        name = input(f"Name [{contact['name']}]: ").strip()
        phone = input(f"Phone [{contact['phone']}]: ").strip()
        email = input(f"Email [{contact['email']}]: ").strip()
        category = input(f"Category [{contact['category']}]: ").strip()

        if name:
            contact['name'] = name
        if phone:
            contact['phone'] = phone
        if email:
            contact['email'] = email
        if category:
            contact['category'] = category

        print(" Contact updated.")
    except (ValueError, IndexError):
        print(" Invalid selection.")

def delete_contact(contacts):
    view_contacts(contacts)
    try:
        index = int(input("Enter contact number to delete: ")) - 1
        removed = contacts.pop(index)
        print(f" Deleted contact: {removed['name']}")
    except (ValueError, IndexError):
        print(" Invalid selection.")

def export_to_csv(contacts):
    if not contacts:
        print(" No contacts to export.")
        return

    with open("contacts_export.csv", "w", newline='') as f:
        writer = csv.DictWriter(f, fieldnames=["name", "phone", "email", "category"])
        writer.writeheader()
        writer.writerows(contacts)
    print(" Contacts exported to contacts_export.csv")

def main():
    contacts = load_contacts()

    while True:
        print("""
=====  Contact Book Menu =====
1. Add Contact
2. View All Contacts
3. View Contacts Grouped by Category
4. Search Contact
5. Edit Contact
6. Delete Contact
7. Export Contacts to CSV
8. Exit
""")
        choice = input("Choose an option: ").strip()

        if choice == '1':
            add_contact(contacts)
        elif choice == '2':
            view_contacts(contacts)
        elif choice == '3':
            view_contacts(contacts, group_by="category")
        elif choice == '4':
            search_contacts(contacts)
        elif choice == '5':
            edit_contact(contacts)
        elif choice == '6':
            delete_contact(contacts)
        elif choice == '7':
            export_to_csv(contacts)
        elif choice == '8':
            save_contacts(contacts)
            print(" Contacts saved. Goodbye!")
            break
        else:
            print(" Invalid choice. Try again.")

if __name__ == "__main__":
    main()
