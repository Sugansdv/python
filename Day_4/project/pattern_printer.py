# ==== MINI PROJECT 5: PATTERN PRINTER APP ====

print("====================")
print("Pattern Printer App")
print("====================")

# Input: number of rows
rows = int(input("Enter number of rows: "))

# Use nested for loop:
# Outer loop for rows
for i in range(1, rows + 1):
    # Inner loop for printing *
    for j in range(i):
        print("*", end=" ")
    # Move to the next line after each row
    print()
