from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Usage | weight in kg, height in m | : /bmi/70/1.75"

@app.route("/bmi/<weight>/<height>")
def bmi(weight, height):
    w = float(weight)
    h = float(height)
    bmi_value = round(w / (h ** 2), 2)

    if bmi_value < 18.5:
        category = "Underweight"
    elif bmi_value < 24.9:
        category = "Normal weight"
    elif bmi_value < 29.9:
        category = "Overweight"
    else:
        category = "Obese"

    return f"Your BMI is {bmi_value} → {category}"

if __name__ == "__main__":
    app.run(debug=True)
