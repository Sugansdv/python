from expensesplitter.members import GroupMembers
from expensesplitter.split import ExpenseSplitter
from expensesplitter.report import generate_csv_report

# Step 1: Add members
group = GroupMembers()
group.add_member("Alice")
group.add_member("Bob")
group.add_member("Charlie")

# Step 2: Split expenses
splitter = ExpenseSplitter(group.get_members())
splitter.add_expense("Alice", "150.00", "Dinner")
splitter.add_expense("Bob", "90.00", "Groceries")
splitter.add_expense("Charlie", "60.00", "Snacks")

# Step 3: Calculate and report
balances = splitter.calculate_balances()
for member, balance in balances.items():
    print(f"{member}: {'owes' if balance < 0 else 'gets'} {abs(balance):.2f}")

generate_csv_report("group_balances.csv", balances)
