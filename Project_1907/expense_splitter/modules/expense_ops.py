def add_expense(expenses, balances):
    try:
        amount = float(input("Enter amount: "))
        payer = input("Who paid? ").strip()
        participants = set(input("Participants (comma-separated): ").split(","))
        category = input("Category: ").strip().lower()

        share = round(amount / len(participants), 2)

        for person in participants:
            person = person.strip()
            if person not in balances:
                balances[person] = 0.0
            if person == payer:
                balances[person] += (amount - share)
            else:
                balances[person] -= share

        expenses.append({
            "amount": amount,
            "payer": payer,
            "participants": participants,
            "category": category
        })

        print(f"Expense added. {payer} paid ₹{amount} for {category}. Split among {participants}.")
    except Exception as e:
        print(f"Error: {e}")
