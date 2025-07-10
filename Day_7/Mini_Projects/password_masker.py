# 5. Secure Password Masker
# Input a password like "MySecret123"
password = input("Enter your password: ") 

if len(password) > 2:
    # first and last char shown, rest masked using *)
    # Use slicing and repetition (* operator)
    masked = password[0] + '*' * (len(password) - 2) + password[-1]
else:
    masked = password

print("Masked Password:", masked)
