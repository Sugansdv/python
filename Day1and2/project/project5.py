## 5. Temperature Converter
print("========================================")
print("         Temperature Converter          ")
print("========================================")

# 1. Ask the user to enter temperature in Celsius
celsius = input("Enter temperature in Celsius: ")

# 2. Display the type before conversion
print(f"Before conversion, type of 'celsius' is: {type(celsius)}")

# 3. Convert to float
celsius = float(celsius)

# 4. Convert to Fahrenheit
fahrenheit = (celsius * 9/5) + 32

# 5. Print the result with an f-string
print(f"\n{celsius}°C is equal to {fahrenheit}°F.")

# 6. Display the type after conversion
print(f"After conversion, type of 'celsius' is: {type(celsius)}")
