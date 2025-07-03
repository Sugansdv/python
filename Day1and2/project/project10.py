## 10. Currency Converter

print("========================================")
print("           Currency Converter           ")
print("========================================")

# 1. Ask the user for an amount in USD
usd = float(input("Enter amount in USD: "))

# 2. Convert it to INR (fixed rate: 1 USD = 83 INR)
inr = usd * 83

# 3. Print the result using an f-string
print(f"\n {usd} USD is equal to ₹{inr:.2f} INR.")

# 4. Show the type after conversion
print(f"Type of 'inr': {type(inr)}")
