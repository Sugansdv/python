from flask import Flask
import datetime

app = Flask(__name__)

quotes = {
    "monday": "Start your week with positivity!",
    "tuesday": "Keep pushing forward!",
    "wednesday": "Halfway there, stay strong!",
    "thursday": "Make today amazing!",
    "friday": "Finish the week on a high note!",
    "saturday": "Relax and recharge!",
    "sunday": "Plan and prepare for success!"
}

@app.route("/")
def today_quote():
    day = datetime.datetime.now().strftime("%A").lower()
    return f"<h1 style='color:green;'>Quote for {day.title()}</h1><p>{quotes[day]}</p>"

@app.route("/quote/<day>")
def quote_by_day(day):
    return f"<h1>Quote for {day.title()}</h1><p>{quotes.get(day.lower(), 'No quote found')}</p>"

if __name__ == "__main__":
    app.run(debug=True)
