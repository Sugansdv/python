# 9. Expense Tracker

# Store expenses
expenses = []

# • Add multiple expenses using *args
def add_expenses(*args):
    for expense in args:
        expenses.append(expense)
    print(f"{len(args)} expense(s) added.")

# • Use map() to apply GST (e.g., 18%) on each item
def apply_gst():
    return list(map(lambda x: round(x * 1.18, 2), expenses))

# • Store in a list and return sum
def total_expense():
    return sum(expenses)

add_expenses(120, 250, 430)
print("Expenses without GST:", expenses)
print("Expenses with GST:", apply_gst())
print("Total Expense: ₹", total_expense())
