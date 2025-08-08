from flask import Flask
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def home():
    now = datetime.now().hour
    if 10 <= now < 17:
        return "<h1><b>We are open!</b></h1>"
    else:
        return "<h1><b>Closed</b></h1>"

@app.route("/contact")
def contact():
    return """
        <h1>Contact</h1>
        <hr>
        <p>Email: <b>support@mail.com</b></p>
        <p>Phone: <b>9637418520</b></p>
    """

if __name__ == "__main__":
    app.run(debug=True)  
