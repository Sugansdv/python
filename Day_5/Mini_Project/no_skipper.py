# 15. Even Number Skipper
# Objective: Skip even numbers and print squares of odds.

i = 1

# • Range: 1 to 20
# • Use while loop
while i <= 20:

    # • Use continue for even numbers.
    if i % 2 == 0:
        i += 1
        continue

    # • Print number and its square.
    print(f"{i} → Square = {i**2}")

    i += 1
