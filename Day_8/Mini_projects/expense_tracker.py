# 13. Budget Expense Tracker
# Description: Track user expenses using a list.

# Initial list of expenses (amounts in ₹)
expenses = [1200, 500, 800, 2500, 1000]

# Display initial expenses
print(" Current Expenses:", expenses)

# Add new expenses
expenses.append(1500)
expenses.append(750)
print("\nAdded new expenses: 1500 and 750")

# Update old expense (e.g., change ₹500 to ₹550)
for i in range(len(expenses)):
    if expenses[i] == 500:
        expenses[i] = 550
        print("Updated ₹500 to ₹550")
        break

# Remove wrong entry (e.g., remove ₹2500 if it's incorrect)
wrong_entry = 2500
if wrong_entry in expenses:
    expenses.remove(wrong_entry)
    print(f"Removed wrong entry: ₹{wrong_entry}")

# Show last 3 expenses using slicing
last_three = expenses[-3:]
print("\n Last 3 Expenses:", last_three)

# Final list of expenses
print(" Updated Expense List:", expenses)
