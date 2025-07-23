import json
import os

FILE_NAME = "contacts.json"

# Ensure file exists
if not os.path.exists(FILE_NAME):
    with open(FILE_NAME, "w") as f:
        json.dump({}, f)

# Load contacts
def load_contacts():
    with open(FILE_NAME, "r") as f:
        return json.load(f)

# Save contacts
def save_contacts(contacts):
    with open(FILE_NAME, "w") as f:
        json.dump(contacts, f, indent=4)

# Add contact
def add_contact():
    name = input("Enter name: ")
    phone = input("Enter phone: ")
    email = input("Enter email: ")

    contacts = load_contacts()
    if name in contacts:
        print("Contact already exists!")
    else:
        contacts[name] = {"phone": phone, "email": email}
        save_contacts(contacts)
        print("Contact added successfully.")

# View all contacts
def view_contacts():
    contacts = load_contacts()
    if not contacts:
        print("No contacts found.")
        return
    for name, details in contacts.items():
        print(f"{name}:  {details['phone']} |  {details['email']}")

# Update contact
def update_contact():
    name = input("Enter contact name to update: ")
    contacts = load_contacts()
    if name in contacts:
        phone = input("New phone (leave blank to keep current): ")
        email = input("New email (leave blank to keep current): ")

        if phone:
            contacts[name]["phone"] = phone
        if email:
            contacts[name]["email"] = email

        save_contacts(contacts)
        print("Contact updated.")
    else:
        print("Contact not found.")

# Delete contact
def delete_contact():
    name = input("Enter contact name to delete: ")
    contacts = load_contacts()
    if name in contacts:
        del contacts[name]
        save_contacts(contacts)
        print("Contact deleted.")
    else:
        print("Contact not found.")

# Main menu
def main():
    while True:
        print("\n--- Contact Manager ---")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Update Contact")
        print("4. Delete Contact")
        print("5. Exit")

        choice = input("Select option: ")

        if choice == "1":
            add_contact()
        elif choice == "2":
            view_contacts()
        elif choice == "3":
            update_contact()
        elif choice == "4":
            delete_contact()
        elif choice == "5":
            print("Exiting Contact Manager.")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
