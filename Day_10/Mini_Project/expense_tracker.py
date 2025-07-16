# 4. Daily Expense Tracker
# Description: Track your daily expenses.
# Requirements:
# - Structure: {date: {"food": amt, "transport": amt, "misc": amt}}
# - Calculate daily and monthly total
# - Filter days with highest spending
# - Use update(), copy() to replicate structure for new month
# - Use dictionary comprehension to extract days with food > 200

expenses = {
    "2025-07-01": {"food": 250, "transport": 100, "misc": 50},
    "2025-07-02": {"food": 180, "transport": 80, "misc": 60},
    "2025-07-03": {"food": 220, "transport": 90, "misc": 70}
}

def calculate_daily_totals():
    print("\nDaily Totals:")
    for date, items in expenses.items():
        total = sum(items.values())
        print(f"{date}: ₹{total}")

def calculate_monthly_total():
    total = sum(sum(day.values()) for day in expenses.values())
    print(f"\nTotal Monthly Expense: ₹{total}")

def find_highest_spending_days():
    max_total = max(sum(day.values()) for day in expenses.values())
    print("\nHighest Spending Day(s):")
    for date, items in expenses.items():
        if sum(items.values()) == max_total:
            print(f"{date}: ₹{max_total}")

def replicate_for_new_month(month):
    new_expenses = {f"{month}-{str(i).zfill(2)}": expenses["2025-07-01"].copy() for i in range(1, 4)}
    expenses.update(new_expenses)
    print(f"\nReplicated data for {month}:")
    for date in new_expenses:
        print(date, "→", expenses[date])

def extract_days_with_food_above(threshold):
    result = {date: data["food"] for date, data in expenses.items() if data.get("food", 0) > threshold}
    print(f"\nDays with food expense > ₹{threshold}:")
    for date, amt in result.items():
        print(f"{date}: ₹{amt}")

calculate_daily_totals()
calculate_monthly_total()
find_highest_spending_days()
replicate_for_new_month("2025-08")
extract_days_with_food_above(200)
