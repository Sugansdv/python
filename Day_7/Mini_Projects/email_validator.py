# 17. Email Validator
# Input: email from the user
email = input("Enter your email: ") 

# Check if email contains both '@' and '.'
if "@" in email and "." in email:
    # Find position of '@'
    at_pos = email.find("@")
    
    # Extract username and domain using slicing
    username = email[:at_pos]
    domain = email[at_pos+1:]
    
    # Check if domain is 'gmail.com' and username is longer than 5 characters
    if domain == "gmail.com" and len(username) > 5:
        print("Valid Gmail address!")
    else:
        print("Invalid: Must be a Gmail address with username > 5 characters.")
else:
    print(" Invalid: Email must contain '@' and '.'")

