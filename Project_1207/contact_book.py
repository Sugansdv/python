# 8. Contact Book App
# Concepts: strings, functions, lists, while.
# • Add new contact: name, phone, email.
# • Store in list of lists.
# • Search contact using string in operator.
# • Loop for multiple options (search, delete, show all).

contacts = []

def add_contact():
    name = input("Enter name: ")
    phone = input("Enter phone: ")
    email = input("Enter email: ")
    contacts.append([name, phone, email])

def show_contacts():
    if not contacts:
        print("No contacts found.\n")
    else:
        print("\n--- Contact List ---")
        for i, c in enumerate(contacts, start=1):
            print(f"{i}. Name: {c[0]}, Phone: {c[1]}, Email: {c[2]}")
        print()

def search_contact():
    keyword = input("Enter name/email/phone to search: ")
    found = False
    for c in contacts:
        if keyword.lower() in c[0].lower() or keyword in c[1] or keyword.lower() in c[2].lower():
            print(f"Found - Name: {c[0]}, Phone: {c[1]}, Email: {c[2]}")
            found = True
    if not found:
        print("No matching contact found.\n")

def delete_contact():
    keyword = input("Enter name or phone to delete: ")
    for c in contacts:
        if keyword in c[0] or keyword in c[1]:
            contacts.remove(c)
            print("Contact deleted.\n")
            return
    print("Contact not found.\n")

while True:
    print("1. Add Contact")
    print("2. Show All Contacts")
    print("3. Search Contact")
    print("4. Delete Contact")
    print("5. Exit")
    choice = input("Choose an option: ")

    if choice == "1":
        add_contact()
    elif choice == "2":
        show_contacts()
    elif choice == "3":
        search_contact()
    elif choice == "4":
        delete_contact()
    elif choice == "5":
        break
    else:
        print("Invalid option.\n")
