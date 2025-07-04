
print("=======================================")
print("         Username Availability Checker         ")
print("=======================================\n")

# Predefined list of taken usernames
taken_usernames = ["admin", "john_doe", "sugan", "guest", "techie"]

# Input: username to check
new_username = input("Enter a username to check availability: ")

# Check using membership operators and if-else
if new_username in taken_usernames:
    print(f"\n Sorry, the username '{new_username}' is already taken.")
else:
    print(f"\n Great! The username '{new_username}' is available.")
