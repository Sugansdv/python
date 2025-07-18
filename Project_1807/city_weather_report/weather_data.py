# weather_data.py

import requests

API_KEY = "6d52164c59c33ed19cc500a3280a52a0"    
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

def fetch_weather_by_coords(lat, lon):
    try:
        params = {
            "lat": lat,
            "lon": lon,
            "appid": API_KEY,
            "units": "metric"
        }
        response = requests.get(BASE_URL, params=params)
        response.raise_for_status()
        data = response.json()
        
        weather = data["weather"][0]["description"].capitalize()
        temp = data["main"]["temp"]
        city_name = data.get("name", "Unknown")

        return f"{weather}, {temp}°C", city_name

    except requests.RequestException as e:
        return "Error fetching data", "N/A"

def print_weather_info(city, coord, weather):
    lat, lon = coord
    print(f"\n📍 City: {city}")
    print(f"   Coordinates: Latitude={lat}, Longitude={lon}")
    print(f"   Weather: {weather}")
