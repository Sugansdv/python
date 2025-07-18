from calc.interface import build_parser, execute_command

def main():
    parser = build_parser()
    args = parser.parse_args()

    try:
        result = execute_command(args)
        print(f" Result: {result}")
    except Exception as e:
        print(f" Error: {e}")

if __name__ == "__main__":
    main()
#python main.py add 5 3