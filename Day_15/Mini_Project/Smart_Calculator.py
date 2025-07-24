import logging

# Configure logging
logging.basicConfig(filename='calculator_errors.log', level=logging.ERROR, format='%(asctime)s - %(levelname)s - %(message)s')

# Custom Exception
class InvalidOperationError(Exception):
    pass

def smart_calculator():
    try:
        num1 = float(input("Enter first number: "))
        operator = input("Enter operator (+, -, *, /, %): ")
        num2 = float(input("Enter second number: "))

        if operator == '+':
            result = num1 + num2
        elif operator == '-':
            result = num1 - num2
        elif operator == '*':
            result = num1 * num2
        elif operator == '/':
            if num2 == 0:
                raise ZeroDivisionError("Cannot divide by zero.")
            result = num1 / num2
        elif operator == '%':
            if num2 == 0:
                raise ZeroDivisionError("Cannot take modulus by zero.")
            result = num1 % num2
        else:
            raise InvalidOperationError(f"'{operator}' is not a valid operation.")

    except ValueError as ve:
        print(" Invalid numeric input.")
        logging.error("ValueError: %s", ve)
    except ZeroDivisionError as zde:
        print(" Cannot divide or modulus by zero.")
        logging.error("ZeroDivisionError: %s", zde)
    except InvalidOperationError as ioe:
        print("Invalid operation entered.")
        logging.error("InvalidOperationError: %s", ioe)
    else:
        print(" Result:", result)
    finally:
        print(" Calculation complete.")

# Run the calculator
if __name__ == "__main__":
    smart_calculator()
