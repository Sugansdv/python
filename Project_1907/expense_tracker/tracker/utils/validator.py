import re

def validate_date(date_str):
    return re.fullmatch(r"\d{4}-\d{2}-\d{2}", date_str) is not None

def validate_amount(amount_str):
    try:
        float(amount_str)
        return True
    except ValueError:
        return False
