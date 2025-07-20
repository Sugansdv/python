def show_summary(balances):
    print("\n--- Balance Summary ---")
    for person, balance in balances.items():
        status = "owes" if balance < 0 else "is owed"
        print(f"{person}: {status} ₹{abs(round(balance, 2))}")
    print("------------------------")

def settle_balances(balances):
    creditors = {k: v for k, v in balances.items() if v > 0}
    debtors = {k: -v for k, v in balances.items() if v < 0}

    print("\n--- Settlement Suggestions ---")
    for debtor, debt_amt in debtors.items():
        for creditor, cred_amt in creditors.items():
            if debt_amt == 0:
                break
            pay = min(debt_amt, cred_amt)
            if pay > 0:
                print(f"{debtor} pays {creditor} ₹{round(pay, 2)}")
                debt_amt -= pay
                creditors[creditor] -= pay
    print("-------------------------------")
