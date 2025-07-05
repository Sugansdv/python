# ==== MINI PROJECT 3: CUSTOM MULTIPLICATION TABLE GENERATOR ====

print("====================")
print("Custom Multiplication Table Generator")
print("====================")

# Input: any number
num = int(input("Enter a number to generate its multiplication table: "))

# Use range(1, 11) in a for loop
for i in range(1, 11):
    # Print in the format: num x i = result
    # Use f-string for output
    print(f"{num} x {i} = {num * i}")
