from modules.logger_ops import add_weather_data, view_weather_data
from modules.analysis import monthly_summary, unique_conditions

weather_log = {}

def main():
    while True:
        print("\nWeather Data Logger")
        print("1. Add Weather Data")
        print("2. View Weather Data")
        print("3. Monthly Summary")
        print("4. Unique Conditions")
        print("5. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            add_weather_data(weather_log)
        elif choice == "2":
            view_weather_data(weather_log)
        elif choice == "3":
            monthly_summary(weather_log)
        elif choice == "4":
            unique_conditions(weather_log)
        elif choice == "5":
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
