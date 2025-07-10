#13. Username Creator
# Input: full name from the user
full_name = input("Enter your full name: ")  

# Split the name into first and last using .split()
parts = full_name.strip().split()

# Check if both first and last name are provided
if len(parts) >= 2:
    first_name = parts[0]
    last_name = parts[-1]

    # Slice: first 3 letters of first name, last 2 letters of last name
    username = first_name[:3] + last_name[-2:]

    # Print the generated username
    print("Username:", username)
else:
    print("Please enter both first and last names.")

