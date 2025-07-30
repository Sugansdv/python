def validate_input(func):
    def wrapper(*args, **kwargs):
        try:
            amount = float(kwargs.get("amount"))
            if amount <= 0:
                raise ValueError("Amount must be positive.")
        except (ValueError, TypeError):
            print("Invalid amount. Must be a positive number.")
            return

        if not kwargs.get("category"):
            print("Category is required.")
            return

        try:
            from datetime import datetime
            datetime.strptime(kwargs.get("date"), "%Y-%m-%d")
        except ValueError:
            print("Invalid date. Format must be YYYY-MM-DD.")
            return

        return func(*args, **kwargs)
    return wrapper
