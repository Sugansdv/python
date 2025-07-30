from calculator import sin, cos, tan, log, sqrt, add, subtract, multiply, divide

def main():
    print("=== Scientific Calculator ===")
    print("Available operations: sin, cos, tan, log, sqrt, add, subtract, multiply, divide")
    print("Type 'exit' to quit.\n")

    while True:
        try:
            command = input("Enter operation: ").lower()
            if command == "exit":
                print("Goodbye!")
                break

            if command in ("sin", "cos", "tan", "sqrt", "log"):
                x = float(input("Enter number: "))
                if command == "log":
                    base = input("Enter base (default 10): ")
                    base = float(base) if base else 10
                    print(f"Result: {log(x, base)}")
                elif command == "sqrt":
                    print(f"Result: {sqrt(x)}")
                elif command == "sin":
                    print(f"Result: {sin(x)}")
                elif command == "cos":
                    print(f"Result: {cos(x)}")
                elif command == "tan":
                    print(f"Result: {tan(x)}")

            elif command in ("add", "subtract", "multiply", "divide"):
                a = float(input("Enter first number: "))
                b = float(input("Enter second number: "))
                if command == "add":
                    print(f"Result: {add(a, b)}")
                elif command == "subtract":
                    print(f"Result: {subtract(a, b)}")
                elif command == "multiply":
                    print(f"Result: {multiply(a, b)}")
                elif command == "divide":
                    print(f"Result: {divide(a, b)}")
            else:
                print("Unsupported operation.")

        except ZeroDivisionError as zde:
            print("Math error:", zde)
        except ValueError:
            print("Invalid input. Please enter valid numbers.")
        except Exception as e:
            print("Error:", e)

if __name__ == "__main__":
    main()
