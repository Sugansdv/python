# 🔧 Bitwise Operators Tasks (36–40)

# Task 36: Take two integers and perform bitwise AND (&), OR (|), XOR (^).
print(" Task 36: Bitwise AND, OR, XOR")
a = int(input("Enter first number (a): "))
b = int(input("Enter second number (b): "))
print(f"{a} & {b} = {a & b}")
print(f"{a} | {b} = {a | b}")
print(f"{a} ^ {b} = {a ^ b}")

# Task 37: Demonstrate NOT (~) on a positive number.
print("\n Task 37: Bitwise NOT (~) on a Positive Number")
num = int(input("Enter a positive number: "))
not_result = ~num
print(f"~{num} = {not_result} (i.e., -({num} + 1))")

# Task 38: Perform left shift << and right shift >> on a number and display binary.
print("\n Task 38: Left Shift << and Right Shift >> with Binary Display")
n = int(input("Enter a number: "))
shift = int(input("Enter shift value: "))
left = n << shift
right = n >> shift
print(f"{n} << {shift} = {left} (binary: {bin(left)})")
print(f"{n} >> {shift} = {right} (binary: {bin(right)})")

# Task 39: Show binary representation using bin() and apply bitwise operations.
print("\n Task 39: Binary Representation and Bitwise Operations")
x = int(input("Enter first number: "))
y = int(input("Enter second number: "))
print(f"Binary of {x} = {bin(x)}")
print(f"Binary of {y} = {bin(y)}")
print(f"{x} & {y} = {x & y} (binary: {bin(x & y)})")
print(f"{x} | {y} = {x | y} (binary: {bin(x | y)})")
print(f"{x} ^ {y} = {x ^ y} (binary: {bin(x ^ y)})")

# Task 40: Create a bit mask simulation using bitwise operations for toggling bits.
print("\n Task 40: Bit Mask Toggle Simulation")
number = int(input("Enter original number: "))
bit_position = int(input("Enter bit position to toggle (0 = LSB): "))
mask = 1 << bit_position
toggled = number ^ mask
print(f"Original binary: {bin(number)}")
print(f"Mask for toggling bit {bit_position}: {bin(mask)}")
print(f"Result after toggle: {toggled} (binary: {bin(toggled)})")
