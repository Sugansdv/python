import csv
from decimal import Decimal

def generate_csv_report(filename, balances):
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Member", "Balance"])
        for member, balance in balances.items():
            writer.writerow([member, f"{balance:.2f}"])
