import argparse
from utils import math_utils

def main():
    parser = argparse.ArgumentParser(description="Simple CLI Math Utility")
    parser.add_argument("operation", choices=["add", "subtract"], help="Operation to perform")
    parser.add_argument("x", type=int, help="First number")
    parser.add_argument("y", type=int, help="Second number")

    args = parser.parse_args()

    if args.operation == "add":
        result = math_utils.add(args.x, args.y)
    elif args.operation == "subtract":
        result = math_utils.subtract(args.x, args.y)
    
    print(f"Result: {result}")

if __name__ == "__main__":
    main()

