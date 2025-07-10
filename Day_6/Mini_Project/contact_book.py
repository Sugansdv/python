#15. Contact Book
# Global dictionary to store contacts
contacts = {}

# • Add new contact using **kwargs
def add_contact(**kwargs):
    name = kwargs.get("name")
    if name:
        contacts[name] = kwargs
        print(f"Contact '{name}' added successfully.")
    else:
        print("Name is required to add a contact.")

# • Return sorted contact list
def get_sorted_contacts():
    return sorted(contacts.keys())

# • Search function to return contact details
def search_contact(name):
    return contacts.get(name, "Contact not found.")

# Sample usage
add_contact(name="Dharun", phone="9876543210", email="dharun@example.com")
add_contact(name="Vishwa", phone="9123456780", email="vishwa@example.com")
add_contact(name="Santoz", phone="9012345678")

print("\nSorted Contact Names:")
print(get_sorted_contacts())

print("\nSearch for Vishwa:")
print(search_contact("Vishwa"))

print("\nSearch for David:")
print(search_contact("David"))
