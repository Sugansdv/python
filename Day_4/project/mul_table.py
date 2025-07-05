# ==== MINI PROJECT 0: CUSTOM SIZE MULTIPLICATION TABLE ====

print("====================")
print("Custom Size Multiplication Table")
print("====================")

# Input: table size (e.g., 5x5 or 10x10)
rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))

# Outer loop: rows
for i in range(1, rows + 1):
    # Inner loop: columns
    for j in range(1, cols + 1):
        # Use print(f"{i} x {j} = {i*j}")
        print(f"{i} x {j} = {i*j}", end="\t")
    print()  # Move to next line after each row
