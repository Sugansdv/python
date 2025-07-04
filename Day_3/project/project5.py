
print("=======================================")
print("      BMI Calculator & Category Checker      ")
print("=======================================\n")

# Input: height and weight
height = float(input("Enter your height in meters: "))
weight = float(input("Enter your weight in kilograms: "))

# Arithmetic: Calculate BMI using formula
bmi = weight / (height ** 2)

# Comparison using if-elif for category
if bmi < 18.5:
    category = "Underweight"
elif bmi < 25:
    category = "Normal"
elif bmi < 30:
    category = "Overweight"
else:
    category = "Obese"

# Formatted output using f-string
print("\n========== BMI Report ==========")
print(f"Height          : {height} m")
print(f"Weight          : {weight} kg")
print(f"Calculated BMI  : {bmi:.2f}")
print(f"Category        : {category}")
print("=================================")
