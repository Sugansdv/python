# ==== MINI PROJECT 11: TRIANGLE NUMBER PATTERN APP ====

print("====================")
print("Triangle Number Pattern App")
print("====================")

# Input: number of rows for the triangle
rows = int(input("Enter the number of rows: "))

# Use nested for loops:
# Outer loop: controls the number of rows
for i in range(1, rows + 1):
    # Inner loop: prints numbers from 1 to current row number
    for j in range(1, i + 1):
        print(j, end=" ")
    print()  # New line after each row

