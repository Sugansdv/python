import requests
from utils.decorators import retry

API_KEY = "0e7f4e08dd7ff3d70af9a9ee9ce804e0"  

@retry()
def fetch_weather_data(city):
    url = f"http://api.weatherapi.com/v1/forecast.json?key={API_KEY}&q={city}&days=3"
    response = requests.get(url)
    if response.status_code != 200:
        raise Exception("Failed to fetch weather data.")
    return response.json()
