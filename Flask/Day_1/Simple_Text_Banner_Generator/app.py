from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return 'Enter your banner text <a href="/banner/Enter_Text">Click here</a>'

@app.route("/banner/<text>")
def banner_text(text):
    return f"<h1>{text}</h1>"

@app.route("/banner/<text>/<size>")
def banner_with_size(text, size):
    return f"<{size}>{text}</{size}>"

if __name__ == "__main__":
    app.run(debug=True)
