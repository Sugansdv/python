import math

history = []
memory = None

def evaluate_expression(expr):
    try:
        result = eval(expr, {"__builtins__": None}, math.__dict__)
        history.append(f"{expr} = {result}")
        return result
    except Exception as e:
        return f" Error: {str(e)}"

def memory_store(value):
    global memory
    memory = value
    print(f" Stored in memory: {memory}")

def memory_recall():
    if memory is not None:
        print(f" Recalled from memory: {memory}")
        return memory
    print(" Memory is empty.")
    return 0

def memory_clear():
    global memory
    memory = None
    print(" Memory cleared.")

def show_history():
    if not history:
        print("🕳️ No history yet.")
    else:
        print("\n Calculation History:")
        for item in history:
            print(item)

def convert_units():
    print("""
 Unit Conversion Menu
1. Length: cm <-> m <-> in <-> ft
2. Weight: kg <-> g <-> lb <-> oz
""")
    choice = input("Select option: ").strip()

    if choice == "1":
        length = float(input("Enter length: "))
        from_unit = input("From (cm/m/in/ft): ").lower()
        to_unit = input("To (cm/m/in/ft): ").lower()
        converted = convert_length(length, from_unit, to_unit)
        print(f" {length} {from_unit} = {converted} {to_unit}")
    elif choice == "2":
        weight = float(input("Enter weight: "))
        from_unit = input("From (kg/g/lb/oz): ").lower()
        to_unit = input("To (kg/g/lb/oz): ").lower()
        converted = convert_weight(weight, from_unit, to_unit)
        print(f" {weight} {from_unit} = {converted} {to_unit}")
    else:
        print(" Invalid choice.")

def convert_length(value, from_u, to_u):
    units = {
        "cm": 1,
        "m": 100,
        "in": 2.54,
        "ft": 30.48
    }
    return round(value * units[from_u] / units[to_u], 4)

def convert_weight(value, from_u, to_u):
    units = {
        "kg": 1,
        "g": 0.001,
        "lb": 0.453592,
        "oz": 0.0283495
    }
    return round(value * units[from_u] / units[to_u], 4)

def main():
    print("===  Simple Calculator ===")
    while True:
        print("""
 Menu:
1. Enter expression (e.g., 5 + 3 * (2 + 1))
2. Store value in memory (MS)
3. Recall memory (MR)
4. Clear memory (MC)
5. View calculation history
6. Unit conversion
7. Exit
""")
        choice = input("Choose an option: ").strip()

        if choice == "1":
            expr = input("Enter expression: ")
            result = evaluate_expression(expr)
            print(f" Result: {result}")
        elif choice == "2":
            val = float(input("Enter value to store: "))
            memory_store(val)
        elif choice == "3":
            memory_recall()
        elif choice == "4":
            memory_clear()
        elif choice == "5":
            show_history()
        elif choice == "6":
            convert_units()
        elif choice == "7":
            print("Exiting calculator.")
            break
        else:
            print(" Invalid option. Try again.")

if __name__ == "__main__":
    main()
