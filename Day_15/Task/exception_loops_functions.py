# 41. Ask user to enter 5 valid integers using a loop, handle bad inputs.
def input_five_integers():
    numbers = []
    count = 0
    while count < 5:
        try:
            num = int(input(f"Enter integer #{count + 1}: "))
            numbers.append(num)
            count += 1
        except ValueError:
            print("Invalid input. Please enter a valid integer.")
    print("Collected numbers:", numbers)

# 42. Write a function that opens and reads file and handles any error.
def read_file_safely(filename):
    try:
        with open(filename, 'r') as f:
            content = f.read()
            print("File Content:\n", content)
    except FileNotFoundError:
        print("Error: File not found.")
    except IOError:
        print("Error: Could not read the file.")

# 43. Handle exception in recursive function (e.g., factorial).
def factorial(n):
    try:
        if n < 0:
            raise ValueError("Factorial is not defined for negative numbers.")
        if n == 0 or n == 1:
            return 1
        return n * factorial(n - 1)
    except RecursionError:
        print("Error: Maximum recursion depth reached.")
        return None
    except ValueError as ve:
        print("Error:", ve)
        return None

# 44. Inside a loop, catch and skip bad inputs instead of crashing.
def process_user_inputs():
    results = []
    for i in range(5):
        try:
            value = int(input(f"Enter value #{i + 1}: "))
            results.append(value * 2)
        except ValueError:
            print("Invalid input, skipping...")
            results.append(None)
    print("Processed Results:", results)

# 45. Demonstrate try-except inside a list comprehension (with filtering).
def safe_conversion_list(data):
    valid_numbers = [int(x) for x in data if x.isdigit()]
    print("Converted Numbers:", valid_numbers)

# === Run tasks ===
if __name__ == "__main__":
    # 41
    input_five_integers()

    # 42
    read_file_safely("sample.txt") 

    # 43
    print("Factorial of 5:", factorial(5))
    print("Factorial of -3:", factorial(-3))

    # 44
    process_user_inputs()

    # 45
    raw_data = ["12", "abc", "45", "", "100"]
    safe_conversion_list(raw_data)
