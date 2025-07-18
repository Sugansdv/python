import requests
import datetime as dt

API_KEY = "YOUR_API_KEY"  # Replace with real API key (e.g., OpenWeatherMap)
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

def get_weather(city_name):
    params = {
        "q": city_name,
        "appid": "6d52164c59c33ed19cc500a3280a52a0",
        "units": "metric"
    }

    try:
        response = requests.get(BASE_URL, params=params, timeout=5)
        response.raise_for_status()
        data = response.json()

        weather = {
            "city": data["name"],
            "temp": data["main"]["temp"],
            "description": data["weather"][0]["description"],
            "humidity": data["main"]["humidity"],
            "wind": data["wind"]["speed"],
            "datetime": dt.datetime.fromtimestamp(data["dt"]).strftime('%Y-%m-%d %H:%M:%S')
        }
        return weather
    except Exception as e:
        return {"error": str(e)}
