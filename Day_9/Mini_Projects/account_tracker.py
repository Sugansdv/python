# 4. Bank Account Manager
# Goal: Manage customer account details using tuples.
# Requirements:
# • Store customer data as (account_number, name, (balance, status))
# • Use nested tuples for balance and status.
# • Access/update display using slicing and indexing.
# • Unpack customer data in reports.
# • Prevent changes to account data using immutability.

# Sample customer data
customers = [
    (1001, "Dharun", (5000.0, "Active")),
    (1002, "Manoj", (3200.5, "Active")),
    (1003, "Santoz", (0.0, "Inactive")),
    (1004, "Sugan", (820.75, "Active")),
    (1005, "Vishwa", (15000.0, "Blocked"))
]

print(" Bank Account Summary:\n")

# Accessing and reporting
for account in customers:
    acc_num, name, (balance, status) = account
    print(f"Account Number: {acc_num}")
    print(f"Name         : {name}")
    print(f"Balance      : ₹{balance:.2f}")
    print(f"Status       : {status}")
    print("-" * 30)

# Display last 3 customers using slicing
print("\n Last 3 Customers:")
for acc in customers[-3:]:
    print(f"{acc[1]} ({acc[0]}) - Status: {acc[2][1]}")
