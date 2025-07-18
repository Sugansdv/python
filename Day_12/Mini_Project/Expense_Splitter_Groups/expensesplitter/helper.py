from decimal import Decimal, InvalidOperation

def validate_decimal(value):
    try:
        return Decimal(value)
    except (InvalidOperation, ValueError):
        raise ValueError(f"Invalid amount: {value}")

def validate_non_empty_string(value, field="Value"):
    if not value or not value.strip():
        raise ValueError(f"{field} cannot be empty.")
    return value.strip()
