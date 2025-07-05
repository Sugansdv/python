# Task 46: Print the factorial of a number using a loop
num = int(input("Enter a number for factorial: "))
factorial = 1
for i in range(1, num + 1):
    factorial *= i
print(f"Factorial of {num} is {factorial}")

print('-' * 30)

# Task 47: Ask for 5 numbers, store them in a list, and print the maximum using loop
numbers = []
for i in range(5):
    n = int(input(f"Enter number {i+1}: "))
    numbers.append(n)

max_num = numbers[0]
for num in numbers:
    if num > max_num:
        max_num = num
print("Maximum number is:", max_num)

print('-' * 30)

# Task 48: Reverse a list manually using a for loop
original = [10, 20, 30, 40, 50]
reversed_list = []
for i in range(len(original)-1, -1, -1):
    reversed_list.append(original[i])
print("Reversed list:", reversed_list)

print('-' * 30)

# Task 49: Fibonacci series up to n terms using a for loop
n = int(input("Enter number of terms for Fibonacci: "))
a, b = 0, 1
for i in range(n):
    print(a, end=" ")
    a, b = b, a + b

print('\n' + '-' * 30)

# Task 50: Find all prime numbers from 1 to 50 using nested loops
print("Prime numbers from 1 to 50:")
for num in range(2, 51):
    is_prime = True
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        print(num, end=" ")
