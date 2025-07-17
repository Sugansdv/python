# 2. Email Duplicate Remover
# Goal: Remove duplicate emails from a contact import.
# Requirements:
# - Import contacts from a list (with duplicates).
# - Convert to a set to remove duplicates.
# - Export the cleaned set to a list.
# - Check if certain email is present using in.
# Concepts Covered: Set creation, in, list-to-set conversion.

imported_contacts = [
    "alice@example.com", "bob@example.com", "carol@example.com",
    "bob@example.com", "dave@example.com", "alice@example.com"
]

unique_contacts = set(imported_contacts)
cleaned_contacts = list(unique_contacts)

email_to_check = "carol@example.com"
if email_to_check in unique_contacts:
    print(f"{email_to_check} is in the contact list.")
else:
    print(f"{email_to_check} is not in the contact list.")

print("Cleaned contact list:", cleaned_contacts)
