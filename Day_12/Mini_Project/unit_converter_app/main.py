import argparse
from converter.temperature import c_to_f, f_to_c

parser = argparse.ArgumentParser(description="Unit Converter CLI")
parser.add_argument("category", choices=["temperature"])
parser.add_argument("conversion", help="Conversion type like c-to-f or f-to-c")
parser.add_argument("value", type=float)

args = parser.parse_args()

if args.category == "temperature":
    if args.conversion == "c-to-f":
        print(f"{args.value}°C = {c_to_f(args.value)}°F")
    elif args.conversion == "f-to-c":
        print(f"{args.value}°F = {f_to_c(args.value)}°C")
    else:
        print("Invalid conversion type")
