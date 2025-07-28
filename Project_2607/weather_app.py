import requests
import json
import os

FAVORITES_FILE = "favorite_locations.json"
BASE_URL = "https://geocoding-api.open-meteo.com/v1/search"
WEATHER_URL = "https://api.open-meteo.com/v1/forecast"


def get_coordinates(city):
    params = {"name": city, "count": 1, "language": "en", "format": "json"}
    res = requests.get(BASE_URL, params=params)
    data = res.json()
    if "results" in data:
        return data["results"][0]["latitude"], data["results"][0]["longitude"]
    return None, None


def get_weather(lat, lon, unit="C"):
    temp_unit = "celsius" if unit.upper() == "C" else "fahrenheit"
    params = {
        "latitude": lat,
        "longitude": lon,
        "current_weather": True,
        "daily": "temperature_2m_max,temperature_2m_min",
        "timezone": "auto",
        "temperature_unit": temp_unit,
    }
    res = requests.get(WEATHER_URL, params=params)
    return res.json()


def load_favorites():
    if os.path.exists(FAVORITES_FILE):
        with open(FAVORITES_FILE, "r") as f:
            return json.load(f)
    return []


def save_favorites(favorites):
    with open(FAVORITES_FILE, "w") as f:
        json.dump(favorites, f, indent=2)


def display_weather(data, unit):
    current = data.get("current_weather", {})
    print(f"  Temperature: {current.get('temperature')}°{unit.upper()}")
    print(f" Windspeed: {current.get('windspeed')} km/h")
    print(f" Time: {current.get('time')}")


def display_forecast(data, unit):
    print("\n 5-Day Forecast:")
    daily = data.get("daily", {})
    dates = daily.get("time", [])
    max_temp = daily.get("temperature_2m_max", [])
    min_temp = daily.get("temperature_2m_min", [])
    for i in range(min(5, len(dates))):
        print(f"{dates[i]} → Min: {min_temp[i]}°, Max: {max_temp[i]}° {unit.upper()}")


def check_weather_alerts(data):
    temp = data.get("current_weather", {}).get("temperature", 0)
    alerts = []
    if temp > 40:
        alerts.append(" Heat Alert: Stay hydrated!")
    elif temp < 5:
        alerts.append(" Cold Alert: Dress warmly!")
    return alerts


def main():
    favorites = load_favorites()
    unit = "C"

    while True:
        print("\n=====  Weather App =====")
        print("1. Get Current Weather")
        print("2. 5-Day Forecast")
        print("3. Switch °C/°F")
        print("4. Weather Alerts")
        print("5. Save Favorite Location")
        print("6. View Favorite Locations")
        print("7. Exit")

        choice = input("Select an option: ")

        if choice == "1":
            city = input("Enter city name: ")
            lat, lon = get_coordinates(city)
            if lat:
                data = get_weather(lat, lon, unit)
                print(f"\nCurrent weather in {city.title()}:")
                display_weather(data, unit)
            else:
                print(" Could not find city.")

        elif choice == "2":
            city = input("Enter city name: ")
            lat, lon = get_coordinates(city)
            if lat:
                data = get_weather(lat, lon, unit)
                display_forecast(data, unit)
            else:
                print(" Could not find city.")

        elif choice == "3":
            unit = "F" if unit == "C" else "C"
            print(f" Switched to {unit.upper()}")

        elif choice == "4":
            city = input("Enter city name: ")
            lat, lon = get_coordinates(city)
            if lat:
                data = get_weather(lat, lon, unit)
                alerts = check_weather_alerts(data)
                if alerts:
                    for alert in alerts:
                        print(f" {alert}")
                else:
                    print(" No alerts.")
            else:
                print(" Could not find city.")

        elif choice == "5":
            city = input("Enter city to add to favorites: ")
            if city not in favorites:
                favorites.append(city)
                save_favorites(favorites)
                print(" City saved.")
            else:
                print(" City already in favorites.")

        elif choice == "6":
            print(" Favorite Locations:")
            for city in favorites:
                print(f"- {city}")

        elif choice == "7":
            print(" Exiting...")
            break

        else:
            print(" Invalid choice.")


if __name__ == "__main__":
    main()
