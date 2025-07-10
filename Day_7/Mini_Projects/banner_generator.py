#15. Banner Generator
# Input: title text from the user
title = input("Enter your banner title: ") 

# Create a border line using * repeated 50 times
border = "*" * 50

# Center the title within 50 characters, padded with spaces
centered_title = title.center(50)

# Print the banner with border and centered title
print(border)
print(centered_title)
print(border)
