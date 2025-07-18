import argparse
from calc import basic as B
from calc import advanced as A

def build_parser():
    parser = argparse.ArgumentParser(description="🧮 Command Line Calculator")

    subparsers = parser.add_subparsers(dest="command", required=True, help="Operation to perform")

    # Basic Operations
    basic_ops = {
        "add": B.add,
        "sub": B.subtract,
        "mul": B.multiply,
        "div": B.divide
    }

    for op in basic_ops:
        p = subparsers.add_parser(op, help=f"{op} two numbers")
        p.add_argument("a", type=str)
        p.add_argument("b", type=str)

    # Advanced: power
    p_pow = subparsers.add_parser("pow", help="a ^ b")
    p_pow.add_argument("a", type=str)
    p_pow.add_argument("b", type=str)

    # Advanced: sqrt
    p_sqrt = subparsers.add_parser("sqrt", help="√a")
    p_sqrt.add_argument("a", type=str)

    # Advanced: log
    p_log = subparsers.add_parser("log", help="log base b (default 10)")
    p_log.add_argument("a", type=str)
    p_log.add_argument("--base", type=str, default="10")

    return parser

def execute_command(args):
    match args.command:
        case "add":
            return B.add(args.a, args.b)
        case "sub":
            return B.subtract(args.a, args.b)
        case "mul":
            return B.multiply(args.a, args.b)
        case "div":
            return B.divide(args.a, args.b)
        case "pow":
            return A.power(args.a, args.b)
        case "sqrt":
            return A.square_root(args.a)
        case "log":
            return A.logarithm(args.a, args.base)
        case _:
            raise ValueError("Unknown command.")
