# ==== MINI PROJECT 12: EVEN NUMBER SKIPPER ====

print("====================")
print("Even Number Skipper")
print("====================")

# Use for loop with range()
for i in range(1, 11):
    # Use continue to skip even numbers
    if i % 2 == 0:
        continue
    print(i)
