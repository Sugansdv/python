# Task 21: Loop from 1 to 10 and break if number is 5
for i in range(1, 11):
    if i == 5:
        break
    print(i)

print('-' * 30)

# Task 22: Loop from 1 to 10 and skip number 5
for i in range(1, 11):
    if i == 5:
        continue
    print(i)

print('-' * 30)

# Task 23: Use pass in a loop where code will be added later
for i in range(5):
    pass  # Placeholder for future logic
print("Pass used in loop without error.")

print('-' * 30)

# Task 24: Ask the user to enter 5 numbers, break if number is negative
for i in range(5):
    num = int(input(f"Enter number {i+1}: "))
    if num < 0:
        print("Negative number entered. Breaking loop.")
        break
    print("You entered:", num)

print('-' * 30)

# Task 25: Skip even numbers and print odd numbers from 1 to 10
for i in range(1, 11):
    if i % 2 == 0:
        continue
    print(i)

print('-' * 30)

# Task 26: Print numbers from 1 to 3, use else to say "Loop complete!"
for i in range(1, 4):
    print(i)
else:
    print("Loop complete!")

print('-' * 30)

# Task 27: Print elements from list, stop if item is "Stop"
items = ["Pen", "Pencil", "Stop", "Eraser", "Sharpener"]
for item in items:
    if item == "Stop":
        break
    print(item)

print('-' * 30)

# Task 28: Loop through "VetriTech" and skip letter "T"
for ch in "VetriTech":
    if ch == 'T' or ch == 't':
        continue
    print(ch)

print('-' * 30)

# Task 29: Loop through 1 to 10. Use pass when number is divisible by 3
for i in range(1, 11):
    if i % 3 == 0:
        pass  # Placeholder, no action taken
    else:
        print(i)

print('-' * 30)

# Task 30: Demonstrate for loop with else that runs if loop completes (no break)
for i in range(1, 6):
    print(i)
else:
    print("Loop finished without break.")
