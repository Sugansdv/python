print("=======================================")
print("      Electricity Bill Calculator      ")
print("=======================================\n")
# Input: name and units
name = input("Enter your name: ")        
units = int(input("Enter total units consumed: "))

# Assignment operator: Initialize bill amount
bill_amount = 0

# Comparison and arithmetic operators to calculate bill
if units <= 100:
    bill_amount = units * 2         
elif units <= 300:
    bill_amount = units * 3         
else:
    bill_amount = units * 5        

# f-string used to format and display the bill
print("\n========== Electricity Bill ==========")
print(f"Customer Name     : {name}")
print(f"Units Consumed    : {units}")
print(f"Bill Amount (₹)   : ₹{bill_amount}")
print("=======================================")