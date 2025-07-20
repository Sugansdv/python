from datetime import datetime

def add_book(books, borrowers):
    title = input("Enter book title: ").strip().lower()
    if title in books:
        print("Book already lent.")
        return
    borrower = input("Enter borrower name: ").strip().title()
    due_date = input("Enter due date (YYYY-MM-DD): ").strip()
    try:
        datetime.strptime(due_date, "%Y-%m-%d")
        books[title] = (borrower, due_date)
        borrowers.add(borrower)
        print(" Book added.")
    except ValueError:
        print("Invalid date format.")

def return_book(books, borrowers):
    title = input("Enter book title to return: ").strip().lower()
    if title in books:
        borrower, _ = books[title]
        del books[title]
        if borrower not in [b for b, _ in books.values()]:
            borrowers.discard(borrower)
        print(" Book returned.")
    else:
        print("Book not found.")

def check_overdue(books):
    today = datetime.today().date()
    print("\n Overdue Books:")
    found = False
    for title, (borrower, due) in books.items():
        due_date = datetime.strptime(due, "%Y-%m-%d").date()
        if due_date < today:
            print(f" - {title.title()} (Borrower: {borrower}, Due: {due})")
            found = True
    if not found:
        print("No overdue books.")
