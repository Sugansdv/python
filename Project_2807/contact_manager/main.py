from manager.contact_book import ContactBook
from manager.contact import Contact
from manager.utils import contact_generator

def print_menu():
    print("\n--- Personal Contact Manager ---")
    print("1. Add Contact")
    print("2. Delete Contact")
    print("3. Update Contact")
    print("4. Search Contact")
    print("5. List All Contacts")
    print("6. Exit")

def main():
    book = ContactBook()

    while True:
        print_menu()
        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            try:
                name = input("Name: ")
                phone = input("Phone (10 digits): ")
                email = input("Email: ")
                contact = Contact(name, phone, email)
                book.add_contact(contact)
                print("Contact added successfully.")
            except ValueError as ve:
                print(f"Error: {ve}")

        elif choice == '2':
            name = input("Enter name to delete: ")
            if book.delete_contact(name):
                print("Contact deleted.")
            else:
                print("Contact not found.")

        elif choice == '3':
            name = input("Enter name to update: ")
            if name in book.contacts:
                try:
                    phone = input("New Phone: ")
                    email = input("New Email: ")
                    contact = Contact(name, phone, email)
                    book.update_contact(name, contact)
                    print("Contact updated.")
                except ValueError as ve:
                    print(f"Error: {ve}")
            else:
                print("Contact not found.")

        elif choice == '4':
            keyword = input("Search keyword (name): ")
            found = False
            for contact in contact_generator(book.contacts, keyword):
                print("\n" + str(contact))
                found = True
            if not found:
                print("No matching contacts found.")

        elif choice == '5':
            if not book.contacts:
                print("No contacts found.")
            else:
                for contact in book.contacts.values():
                    print("\n" + str(contact))

        elif choice == '6':
            book.save_contacts()
            print("Contacts saved. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter 1-6.")

if __name__ == "__main__":
    main()
