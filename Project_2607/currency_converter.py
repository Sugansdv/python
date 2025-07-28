import requests
import datetime
import matplotlib.pyplot as plt

# ---- Globals ---- #
favorites = []

# ---- API URLs ---- #
BASE_URL = "https://api.frankfurter.app"

# ---- Currency Conversion ---- #
def convert_currency(from_currency, to_currency, amount):
    try:
        response = requests.get(
            f"{BASE_URL}/latest",
            params={"from": from_currency, "to": to_currency, "amount": amount},
            timeout=10
        )
        data = response.json()
        rate = data["rates"].get(to_currency)
        if rate:
            return rate
        else:
            print(" Currency not found.")
    except Exception as e:
        print(" Error fetching data:", e)
    return None

# ---- Historical Rates ---- #
def historical_lookup(from_currency, to_currency, date_str):
    try:
        response = requests.get(
            f"{BASE_URL}/{date_str}",
            params={"from": from_currency, "to": to_currency},
            timeout=10
        )
        data = response.json()
        return data["rates"].get(to_currency)
    except Exception as e:
        print(" Error fetching historical data:", e)
    return None

# ---- 7-Day Trend Chart ---- #
def show_trend(from_currency, to_currency):
    try:
        end = datetime.date.today()
        start = end - datetime.timedelta(days=7)
        response = requests.get(
            f"{BASE_URL}/{start.strftime('%Y-%m-%d')}..{end.strftime('%Y-%m-%d')}",
            params={"from": from_currency, "to": to_currency},
            timeout=10
        )
        data = response.json()
        dates = list(data["rates"].keys())
        dates.sort()
        rates = [data["rates"][date][to_currency] for date in dates]

        plt.plot(dates, rates, marker="o")
        plt.title(f"7-Day Trend: {from_currency} to {to_currency}")
        plt.xlabel("Date")
        plt.ylabel(f"{to_currency} Rate")
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.grid(True)
        plt.show()
    except Exception as e:
        print(" Error generating chart:", e)

# ---- Favorite Currencies ---- #
def add_to_favorites(from_currency, to_currency):
    pair = f"{from_currency} → {to_currency}"
    if pair not in favorites:
        favorites.append(pair)
        print(f" Added to favorites: {pair}")
    else:
        print(f" Already in favorites: {pair}")

def show_favorites():
    if favorites:
        print("\n Favorite Currency Pairs:")
        for i, fav in enumerate(favorites, 1):
            print(f"{i}. {fav}")
    else:
        print("No favorites yet.")

# ---- Menu ---- #
def main():
    while True:
        print("\n=====  Currency Converter =====")
        print("1. Convert Currency")
        print("2. Historical Rate Lookup")
        print("3. Favorite Currencies")
        print("4. Show 7-Day Trend Chart")
        print("5. Exit")

        choice = input("Select an option: ")

        if choice == "1":
            from_cur = input("From Currency (e.g., USD): ").upper()
            to_cur = input("To Currency (e.g., INR): ").upper()
            try:
                amount = float(input("Amount: "))
            except ValueError:
                print(" Invalid amount.")
                continue

            result = convert_currency(from_cur, to_cur, amount)
            if result:
                print(f" {amount} {from_cur} = {result:.2f} {to_cur}")
                add_to_favorites(from_cur, to_cur)
            else:
                print(" Conversion failed.")

        elif choice == "2":
            from_cur = input("From Currency: ").upper()
            to_cur = input("To Currency: ").upper()
            date = input("Date (YYYY-MM-DD): ")
            try:
                datetime.datetime.strptime(date, "%Y-%m-%d")
            except ValueError:
                print(" Invalid date format.")
                continue

            rate = historical_lookup(from_cur, to_cur, date)
            if rate:
                print(f" Rate on {date}: 1 {from_cur} = {rate:.2f} {to_cur}")
            else:
                print(" Historical rate not found.")

        elif choice == "3":
            show_favorites()

        elif choice == "4":
            from_cur = input("From Currency: ").upper()
            to_cur = input("To Currency: ").upper()
            show_trend(from_cur, to_cur)

        elif choice == "5":
            print(" Exiting. Goodbye!")
            break
        else:
            print(" Invalid option. Try again.")

if __name__ == "__main__":
    main()
