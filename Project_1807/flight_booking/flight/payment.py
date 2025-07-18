
payment_records = {}  # passenger_id (tuple) → paid or not

def process_payment(passenger_id: tuple, amount: float):
    if payment_records.get(passenger_id) == "Paid":
        return "Payment already completed."

    payment_records[passenger_id] = "Paid"
    return f"Payment of ₹{amount:.2f} successful."


def check_payment_status(passenger_id: tuple):
    return payment_records.get(passenger_id, "Pending")
