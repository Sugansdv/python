from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('layout/home.html')

@app.route('/weather')
def weather():
    weather_data = {
        "temperature": 35,
        "condition": "sunny",
        "location": "Chennai",
        "temperatures_last_week": [32, 33, 34, 35, 36, 33, 32],
    }
    return render_template('layout/weather.html', weather=weather_data)

if __name__ == "__main__":
    app.run(debug=True)
