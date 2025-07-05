# Daily Expense Tracker

# Input 7 daily expenses using a list
daily_expenses = []
print("Enter your expenses for 7 days:")
for i in range(7):
    amount = float(input(f"Day {i+1} expense: ₹"))
    daily_expenses.append(amount)

# Use for loop to sum total
total_expense = 0
for expense in daily_expenses:
    total_expense += expense

# If total > 3000 → print “Cut down on expenses”
print("\n======= Weekly Expense Summary =======")
print(f"Daily Expenses : {daily_expenses}")
print(f"Total Expense  : ₹{total_expense:.2f}")

if total_expense > 3000:
    print("Suggestion     : Cut down on expenses ")
else:
    print("Suggestion     : You're managing well ")
print("======================================")
