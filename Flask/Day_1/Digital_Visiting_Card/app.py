from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h1>Sugan S</h1>
    <p>Profession: Frontend Developer</p>
    <p>Email: sugan@gmail.com</p>
    <p>Phone: 9876543210</p>
    """

@app.route("/about")
def about():
    return "I am a frontend developer passionate about building responsive and user-friendly web applications."

@app.route("/skills/<name>")
def skills(name):
    return f"Skills for {name.title()}: HTML, CSS, React, Redux"


if __name__ == "__main__":
    app.run(debug=True)
