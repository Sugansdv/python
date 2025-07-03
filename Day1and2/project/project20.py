## 20. Data Type Explorer

print("========================================")
print("            Data Type Explorer          ")
print("========================================")

# 1. Ask the user to enter any value
user_input = input("Enter any value: ")

# 2. Print the value and its current type
print(f"\n You entered: {user_input}")
print(f"Original type: {type(user_input)}")

# 3. Ask the user for a desired type conversion
conversion_type = input("\nConvert to (int, float, bool, str): ").strip().lower()

# 4. Attempt conversion and display result and type
try:
    if conversion_type == "int":
        converted_value = int(user_input)
    elif conversion_type == "float":
        converted_value = float(user_input)
    elif conversion_type == "bool":
        converted_value = bool(user_input)
    elif conversion_type == "str":
        converted_value = str(user_input)
    else:
        print(" Invalid conversion type selected.")
        converted_value = None

    if converted_value is not None:
        print(f"\n Converted Value: {converted_value}")
        print(f"New type: {type(converted_value)}")

except ValueError:
    print(" Conversion failed: Value is not compatible with selected type.")
