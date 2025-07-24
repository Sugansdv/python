class InvalidCardError(Exception):
    pass

class InsufficientFundsError(Exception):
    pass

class PaymentGatewayDownError(Exception):
    pass

def validate_card(card_number):
    if not card_number.isdigit() or len(card_number) != 16:
        raise InvalidCardError(" Invalid card number. Must be 16 digits.")

def check_balance(balance, amount):
    if balance < amount:
        raise InsufficientFundsError(" Not enough balance for this transaction.")

def process_payment(card_number, amount):
    # Simulate gateway issue
    import random
    if random.choice([False, False, True]):
        raise PaymentGatewayDownError(" Payment gateway is currently unavailable. Try again later.")

    # Assume payment success
    return True

def main():
    try:
        print("=== Simulated Payment Gateway ===")
        name = input("Enter cardholder name: ").strip()
        card = input("Enter 16-digit card number: ").strip()
        amount = float(input("Enter payment amount: "))
        balance = float(input("Enter available balance: "))

        if not name:
            raise ValueError(" Cardholder name cannot be empty.")

        validate_card(card)
        check_balance(balance, amount)

        print("Processing payment...")
        if process_payment(card, amount):
            print(" Payment successful!")

    except (InvalidCardError, InsufficientFundsError, PaymentGatewayDownError, ValueError) as e:
        print(e)

    except Exception as e:
        print(" An unexpected error occurred:", e)

if __name__ == "__main__":
    main()
