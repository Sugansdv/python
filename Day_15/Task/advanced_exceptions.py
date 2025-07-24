
# 11. Demonstrate try with else: divide numbers only if no exception.
def try_with_else():
    print("\n[11] Try with else:")
    try:
        a = int(input("Enter numerator: "))
        b = int(input("Enter denominator: "))
        result = a / b
    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")
    except ValueError:
        print("Error: Invalid input.")
    else:
        print("Result:", result)

# 12. Demonstrate try with finally: print "Done" regardless of error.
def try_with_finally():
    print("\n[12] Try with finally:")
    try:
        num = int(input("Enter a number: "))
        print("You entered:", num)
    except ValueError:
        print("Invalid input.")
    finally:
        print("Done")

# 13. Use multiple except blocks to catch ValueError and ZeroDivisionError.
def multiple_except_blocks():
    print("\n[13] Multiple except blocks:")
    try:
        x = int(input("Enter numerator: "))
        y = int(input("Enter denominator: "))
        print("Division:", x / y)
    except ValueError:
        print("Error: Please enter numeric values.")
    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")

# 14. Show that finally runs even when exception is raised and not caught.
def finally_without_catch():
    print("\n[14] Finally block without catch:")
    try:
        print("Before error")
        raise RuntimeError("Unexpected error")
    finally:
        print("Finally block runs even if exception isn't caught.")

# 15. Demonstrate combining else and finally together.
def else_and_finally():
    print("\n[15] Else with finally:")
    try:
        a = int(input("Enter value A: "))
        b = int(input("Enter value B: "))
        result = a + b
    except ValueError:
        print("Invalid input.")
    else:
        print("Sum is:", result)
    finally:
        print("Execution finished.")

# 16. Handle exception in file reading and ensure file is closed using finally.
def file_read_with_finally():
    print("\n[16] File read with finally:")
    try:
        f = open("sample.txt", "r")
        print(f.read())
    except FileNotFoundError:
        print("Error: File not found.")
    finally:
        try:
            f.close()
            print("File closed.")
        except:
            print("File was never opened, so cannot close.")

# 17. Nested try-except blocks: one inside another.
def nested_try_except():
    print("\n[17] Nested try-except:")
    try:
        x = int(input("Enter a number: "))
        try:
            result = 10 / x
            print("Result is:", result)
        except ZeroDivisionError:
            print("Inner: Cannot divide by zero.")
    except ValueError:
        print("Outer: Invalid input.")

# 18. Handle a situation where multiple types of exceptions might occur.
def handle_multiple_exceptions():
    print("\n[18] Multiple exception types:")
    try:
        a = int(input("Enter a number: "))
        b = int(input("Enter another number: "))
        print("Result:", a / b)
        lst = [1, 2, 3]
        print("List value:", lst[5])
    except ZeroDivisionError:
        print("Cannot divide by zero.")
    except ValueError:
        print("Invalid input.")
    except IndexError:
        print("Index out of range.")

# 19. Use except Exception as a generic fallback and explain it.
def generic_exception():
    print("\n[19] Generic exception fallback:")
    try:
        name = input("Enter your name: ")
        print("Length of name:", len(name))
        print("Access undefined:", xyz)  # xyz is not defined
    except Exception as e:
        print("Caught an unexpected error:", e)
        print("This is a generic fallback handler for any exception.")

# 20. Demonstrate incorrect nesting of try-except-finally and correct it.
def incorrect_then_correct_nesting():
    print("\n[20] Corrected nesting of try-except-finally:")
    try:
        print("Main try")
    except:
        print("Main except")
    finally:
        try:
            print("Inner try inside finally (valid)")
        except:
            print("Inner except inside finally (valid)")

# Run all tasks 
if __name__ == "__main__":
    function_list = [
        try_with_else,
        try_with_finally,
        multiple_except_blocks,
        finally_without_catch,     # Raises unhandled error inside, so we handle it outside
        else_and_finally,
        file_read_with_finally,
        nested_try_except,
        handle_multiple_exceptions,
        generic_exception,
        incorrect_then_correct_nesting
    ]

    for func in function_list:
        try:
            func()
        except Exception as e:
            print(f"\nUnhandled exception caught from {func.__name__}: {e}")
