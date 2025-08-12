from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('layout/home.html')

@app.route('/jobs')
def jobs():
    jobs_list = [
        {
            "title": "Frontend Developer",
            "company": "Tech Corp",
            "remote": True,
            "location": "Remote",
            "logo_icon": "💻"
        },
        {
            "title": "Backend Engineer",
            "company": "DataSoft",
            "remote": False,
            "location": "New York",
            "logo_icon": "🗄️"
        },
        {
            "title": "UX Designer",
            "company": "Creative Studio",
            "remote": True,
            "location": "Remote",
            "logo_icon": "🎨"
        }
    ]
    return render_template('layout/jobs.html', jobs=jobs_list)

if __name__ == "__main__":
    app.run(debug=True)
