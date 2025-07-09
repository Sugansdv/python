# 5. Multiplication Table Generator
# Objective: Display multiplication table for any number.

# • Input: number
num = int(input("Enter a number to generate its multiplication table: "))

i = 1

# • Use a while loop to print table from 1 to 10.
while i <= 10:
    print(f"{num} x {i} = {num * i}")
    i += 1

# • Use else to say “Table completed”.
else:
    print("Table completed.")
