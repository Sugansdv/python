## 18. Simple BMI Calculator
print("========================================")
print("           Simple BMI Calculator        ")
print("========================================")

# 1. Ask for weight (kg) and height (m)
weight = float(input("Enter your weight in kilograms (kg): "))
height = float(input("Enter your height in meters (m): "))

# 2. Calculate BMI: BMI = weight / (height^2)
bmi = weight / (height ** 2)

# 3. Print BMI with a message using f-string
print(f"\nYour BMI is: {bmi:.2f}")

# 4. Show the type of BMI variable
print(f"Type of 'bmi' variable: {type(bmi)}")
