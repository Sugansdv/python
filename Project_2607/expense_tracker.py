import csv
import os
from datetime import datetime
import matplotlib.pyplot as plt
import pandas as pd

DATA_FILE = "expenses.csv"

# Ensure file exists
if not os.path.exists(DATA_FILE):
    with open(DATA_FILE, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['Date', 'Category', 'Description', 'Amount'])

# Record a new expense
def record_expense():
    date = input("Enter date (YYYY-MM-DD) [Leave blank for today]: ").strip()
    if not date:
        date = datetime.today().strftime('%Y-%m-%d')
    category = input("Category (e.g., Food, Transport, Rent): ").strip()
    description = input("Description: ").strip()
    amount = float(input("Amount spent: "))

    with open(DATA_FILE, 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([date, category, description, amount])
    print(" Expense recorded!")

# Monthly budget tracking
def monthly_budget():
    month = input("Enter month (YYYY-MM): ").strip()
    budget = float(input("Enter your budget for the month: "))

    df = pd.read_csv(DATA_FILE, parse_dates=['Date'])
    df['Month'] = df['Date'].dt.strftime('%Y-%m')
    monthly_expenses = df[df['Month'] == month]['Amount'].sum()

    print(f"\n Expenses in {month}: ₹{monthly_expenses:.2f}")
    print(f" Remaining Budget: ₹{budget - monthly_expenses:.2f}\n")

# Generate report
def spending_report():
    df = pd.read_csv(DATA_FILE, parse_dates=['Date'])
    df['Month'] = df['Date'].dt.strftime('%Y-%m')

    print("\n Total Spending by Category:")
    report = df.groupby('Category')['Amount'].sum()
    for cat, amt in report.items():
        print(f"- {cat}: ₹{amt:.2f}")
    print()

# Visualize with charts
def show_chart():
    df = pd.read_csv(DATA_FILE)
    report = df.groupby('Category')['Amount'].sum()

    report.plot(kind='bar', title="Spending by Category")
    plt.ylabel("Amount (₹)")
    plt.tight_layout()
    plt.show()

# Export data
def export_to_csv():
    export_file = "expense_export.csv"
    df = pd.read_csv(DATA_FILE)
    df.to_csv(export_file, index=False)
    print(f" Data exported to: {export_file}")

# Main Menu
def main():
    while True:
        print("\n=====  Expense Tracker =====")
        print("1. Record Daily Expense")
        print("2. Monthly Budget Tracking")
        print("3. Generate Spending Report")
        print("4. Visualize Data (Chart)")
        print("5. Export Data to Spreadsheet")
        print("6. Exit")

        choice = input("Select an option: ").strip()

        if choice == '1':
            record_expense()
        elif choice == '2':
            monthly_budget()
        elif choice == '3':
            spending_report()
        elif choice == '4':
            show_chart()
        elif choice == '5':
            export_to_csv()
        elif choice == '6':
            print(" Exiting. Goodbye!")
            break
        else:
            print(" Invalid option. Try again.")

if __name__ == "__main__":
    main()
