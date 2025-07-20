from datetime import datetime

def send_reminders(books):
    today = datetime.today().date()
    print("\n Reminders:")
    reminders_sent = False
    for title, (borrower, due) in books.items():
        due_date = datetime.strptime(due, "%Y-%m-%d").date()
        days_left = (due_date - today).days
        if 0 <= days_left <= 3:
            print(f"Reminder: {borrower}, please return '{title.title()}' by {due} ({days_left} days left).")
            reminders_sent = True
    if not reminders_sent:
        print("No reminders needed today.")
