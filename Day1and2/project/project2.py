## 2. Simple Contact Book
print("========================================")
print("         Simple Contact Book            ")
print("========================================")
# 1. Ask the user for their name, phone, and email
name = input("Enter your name: ")
phone = int(input("Enter your phone number: "))
email = input("Enter your email: ")

# 2. Store these in a dictionary
contact = {
    "Name": name,
    "Phone": phone,
    "Email": email
}

# 3. Print the contact information with labels
print("\n Contact Information:")
print(f"Name : {contact['Name']}")
print(f"Phone: {contact['Phone']}")
print(f"Email: {contact['Email']}")

# 4. Display the type of each value using type()
print("\n Data Types:")
print(f"Type of Name : {type(contact['Name'])}")
print(f"Type of Phone: {type(contact['Phone'])}")
print(f"Type of Email: {type(contact['Email'])}")
