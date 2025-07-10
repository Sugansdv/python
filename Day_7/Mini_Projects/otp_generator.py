#19. OTP Generator (One-Time Password)
import random
import string

# Input: user's mobile number
mobile = input("Enter your mobile number: ") 

# Get last 4 digits using slicing
last_four = mobile[-4:]

# Generate 2 random uppercase letters using random.choice() and string.ascii_uppercase
letters = random.choice(string.ascii_uppercase) + random.choice(string.ascii_uppercase)

# Create OTP by mixing last 4 digits and random letters (shuffle optional)
otp = last_four[:2] + letters[0] + last_four[2:] + letters[1]

# Print the generated OTP
print("Your OTP is:", otp)

