 ## 19. Email Formatter

print("========================================")
print("             Email Formatter            ")
print("========================================")

# 1. Ask for user’s first and last name
first_name = input("Enter your first name: ").lower()
last_name = input("Enter your last name: ").lower()

# 2. Generate a simple email using f-string
email = f"{first_name}.{last_name}@example.com"

# 3. Print the email and its type
print(f"\n Generated Email: {email}")
print(f"Type of 'email' variable: {type(email)}")

