import sys
import logging

# Set up logging to file
logging.basicConfig(
    filename='app_exceptions.log',
    level=logging.ERROR,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# Custom global exception hook
def log_exception(exc_type, exc_value, exc_traceback):
    if issubclass(exc_type, KeyboardInterrupt):
        # Let keyboard interrupts go unlogged (exit normally)
        sys.__excepthook__(exc_type, exc_value, exc_traceback)
        return
    logging.error("Uncaught Exception:", exc_info=(exc_type, exc_value, exc_traceback))
    print(" An unexpected error occurred. Check 'app_exceptions.log' for details.")

# Install the global hook
sys.excepthook = log_exception

# Example code that may throw unhandled exceptions
def divide(a, b):
    return a / b

def start_app():
    print("=== Welcome to Demo App ===")
    a = int(input("Enter numerator: "))
    b = int(input("Enter denominator: "))
    result = divide(a, b)
    print(f"Result: {result}")

if __name__ == "__main__":
    start_app()
