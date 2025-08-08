from flask import Flask
import random

app = Flask(__name__)

msgs = ["Believe in yourself!", "Keep going!", "Dream big!", "Stay positive!"]

@app.route("/message")
def random_msg():
    return f"<h2 style='color:blue'>{random.choice(msgs)}</h2>"

@app.route("/message/<int:i>")
def msg_by_index(i):
    return f"<h2 style='color:green'>{msgs[i]}</h2>" if 0 <= i < len(msgs) else "Invalid index!"

if __name__ == "__main__":
    app.run(debug=True)
