# 18. Mini Email Formatter
# Concepts: strings, string methods, functions.
# • Take name and domain from user.
# • Generate formatted email.
# • E.g., john.doe@example.com.

def format_email(first_name, last_name, domain):
    email = f"{first_name.lower()}.{last_name.lower()}@{domain.lower()}"
    return email

first = input("Enter first name: ")
last = input("Enter last name: ")
domain = input("Enter email domain (e.g., example.com): ")

formatted = format_email(first, last, domain)
print(f"\nFormatted Email: {formatted}")
