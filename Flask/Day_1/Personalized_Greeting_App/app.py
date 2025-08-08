from flask import Flask

app = Flask(__name__)

@app.route("/hello/<name>")
def hello(name):
    return f"Hello, {name}!"

@app.route("/greet/<name>/<time>")
def greet(name, time):
    if time.lower() == "morning":
        return f"Good Morning {name}!"
    elif time.lower() == "evening":
        return f"Good Evening {name}!"
    else:
        return f"Hello {name}, have a great {time}!"

if __name__ == "__main__":
    app.run(debug=True) 
