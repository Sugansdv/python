def log_weather(weather: str):
    with open("data/history.txt", "a") as f:
        f.write(weather + "\n")
