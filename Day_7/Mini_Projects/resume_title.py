# 6. Resume Title Generator
# Input: first name, last name, and role
first = input("Enter your first name: ")      
last = input("Enter your last name: ")      
role = input("Enter your job role: ")     

# Convert all inputs to uppercase using .upper()
first = first.upper()
last = last.upper()
role = role.upper()

# Join the fields using .join() with ' | ' as separator
title = " | ".join([first, last, role])

print(f"Resume Title: {title}")
