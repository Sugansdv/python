from core.converter import CurrencyConverter

def main():
    converter = CurrencyConverter()
    
    while True:
        print("\nCurrency Converter")
        print("1. Convert Currency")
        print("2. Supported Currencies")
        print("3. View Historical Rates")
        print("4. Exit")
        choice = input("Enter choice: ")

        if choice == "1":
            from_cur = input("From Currency (e.g., USD): ").upper()
            to_cur = input("To Currency (e.g., INR): ").upper()
            amount = float(input("Amount: "))
            result = converter.convert(from_cur, to_cur, amount)
            print(f"{amount} {from_cur} = {result:.2f} {to_cur}")
        elif choice == "2":
            print("Supported Currencies:", ", ".join(converter.get_supported_currencies()))
        elif choice == "3":
            for date, rate in converter.historical_rates("USD", "INR"):
                print(f"{date}: {rate}")
        elif choice == "4":
            print("Exiting Currency Converter.")
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()
