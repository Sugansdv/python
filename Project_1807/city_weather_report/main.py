# main.py

from weather_data import fetch_weather_by_coords, print_weather_info

def main():
    city_data = {
        (13.0827, 80.2707): "Chennai",
        (19.0760, 72.8777): "Mumbai",
        (28.6139, 77.2090): "Delhi",
        (12.9716, 77.5946): "Bengaluru",
        (22.5726, 88.3639): "Kolkata"
    }

    visited_cities = set()

    while True:
        print("\n--- City Weather Report (Live API) ---")
        print("1. View Weather by Coordinates")
        print("2. Show Visited Cities")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            try:
                lat = float(input("Enter latitude: "))
                lon = float(input("Enter longitude: "))
                coord = (lat, lon)

                weather, city_name = fetch_weather_by_coords(lat, lon)
                visited_cities.add(city_name)
                print_weather_info(city_name, coord, weather)
            except ValueError:
                print("Invalid input. Please enter valid numeric coordinates.")

        elif choice == "2":
            if visited_cities:
                print("\nVisited Cities:")
                for city in visited_cities:
                    print(f"- {city}")
            else:
                print("No cities visited yet.")

        elif choice == "3":
            print("Exiting program.")
            break

        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
