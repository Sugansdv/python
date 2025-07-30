def date_range_generator(expenses, start, end):
    from datetime import datetime
    start_date = datetime.strptime(start, "%Y-%m-%d")
    end_date = datetime.strptime(end, "%Y-%m-%d")
    for expense in expenses:
        if start_date <= expense.date <= end_date:
            yield expense

def unique_categories(expenses):
    return set(e.category for e in expenses)
