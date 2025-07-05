# Temperature Category Classifier

# Input: list of temperatures
input_str = input("Enter temperatures (comma-separated): ")
temperatures = [float(temp.strip()) for temp in input_str.split(",")]

# Use for loop + if to print category for each
print("\n====== Temperature Categories ======")
for temp in temperatures:
    if temp < 20:
        category = "Cold"
    elif 20 <= temp <= 30:
        category = "Warm"
    else:
        category = "Hot"
    
    print(f"{temp}°C → {category}")
print("====================================")
