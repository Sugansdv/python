from contact_book.operations import (
    load_contacts, save_contacts, add_contact, update_contact,
    delete_contact, search_contact, list_contacts
)
from contact_book.validator import validate_phone, validate_email

def get_input(prompt):
    return input(prompt).strip()

def main():
    contacts = load_contacts()

    while True:
        print("\n---  Personal Contact Book ---")
        print("1. Add Contact")
        print("2. Update Contact")
        print("3. Delete Contact")
        print("4. Search Contact")
        print("5. List All Contacts")
        print("6. Exit")

        choice = get_input("Enter your choice (1-6): ")

        if choice == "1":
            name = get_input("Name: ")
            phone = get_input("Phone (10 digits): ")
            if not validate_phone(phone):
                print(" Invalid phone number!")
                continue
            email = get_input("Email: ")
            if not validate_email(email):
                print(" Invalid email format!")
                continue
            tags = set(get_input("Tags (comma separated): ").split(","))
            category = tuple(get_input("Category (one word): ").split())
            add_contact(contacts, name, phone, email, tags, category)

        elif choice == "2":
            name = get_input("Name of contact to update: ")
            phone = get_input("New phone (or leave blank): ")
            email = get_input("New email (or leave blank): ")
            tags = get_input("New tags (comma-separated or blank): ")
            category = get_input("New category (or blank): ")
            update_contact(
                contacts, name,
                phone if phone else None,
                email if email else None,
                set(tags.split(",")) if tags else None,
                tuple(category.split()) if category else None
            )

        elif choice == "3":
            name = get_input("Name of contact to delete: ")
            delete_contact(contacts, name)

        elif choice == "4":
            name = get_input("Name to search: ")
            contact = search_contact(contacts, name)
            if contact:
                print(f"\n👤 {name}")
                print(f" Phone: {contact['phone']}")
                print(f" Email: {contact['email']}")
                print(f" Tags: {', '.join(contact['tags'])}")
                print(f" Category: {contact['category']}")
            else:
                print(" Contact not found.")

        elif choice == "5":
            list_contacts(contacts)

        elif choice == "6":
            save_contacts(contacts)
            print(" Contacts saved. Exiting...")
            break

        else:
            print(" Invalid option. Try again.")

if __name__ == "__main__":
    main()
