#  3. Odd Number Printer
# Objective: Print only odd numbers from 1 to 20.

# • Store the odd numbers in a list.
odd_numbers = []
i = 1

# • Use a while loop.
while i <= 20:
    
    # • Use continue to skip even numbers.
    if i % 2 == 0:
        i += 1
        continue

    odd_numbers.append(i)
    i += 1

print(" Odd numbers from 1 to 20:", odd_numbers)
