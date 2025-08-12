from flask import Flask, render_template

app = Flask(__name__)

portfolio_data = {
    "name": "Suganya S",
    "skills": ["Python", "Flask", "HTML", "CSS", "JavaScript"],
    "projects": [
        {"title": "Portfolio Website", "description": "A personal website using Flask."},
        {"title": "Blog App", "description": "A full blog app with CRUD."},
        {"title": "Chat App", "description": "Real-time chat application."}
    ],
    "available_for_hire": True
}

@app.route("/")
def home():
    return render_template("layout/home.html", data=portfolio_data)

@app.route("/about")
def about():
    return render_template("layout/about.html", data=portfolio_data)

@app.route("/projects")
def projects():
    return render_template("layout/projects.html", data=portfolio_data)

@app.route("/contact")
def contact():
    return render_template("layout/contact.html", data=portfolio_data)

if __name__ == "__main__":
    app.run(debug=True)
