from flask import Flask
app = Flask(__name__)

data = {
    "suganya": {
        "skills": ["HTML", "CSS", "React", "Python"],
        "projects": ["E-commerce Website", "Exam Portal"]
    }
}

@app.route("/portfolio/<name>")
def portfolio(name):
    return f"<h1>{name.title()}'s Portfolio</h1><a href='/portfolio/{name}/skills'>Skills</a> | <a href='/portfolio/{name}/projects'>Projects</a>"

@app.route("/portfolio/<name>/skills")
def skills(name):
    return "<br>".join(data.get(name.lower(), {}).get("skills", ["No skills found"]))

@app.route("/portfolio/<name>/projects")
def projects(name):
    return "<br>".join(data.get(name.lower(), {}).get("projects", ["No projects found"]))

if __name__ == "__main__":
    app.run(debug=True)
