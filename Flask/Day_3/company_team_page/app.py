from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('layout/home.html')

@app.route('/team')
def team():
    team_members = [
        {
            "name": "Alice Johnson",
            "role": "Team Lead",
            "photo": "member.png"
        },
        {
            "name": "Bob Smith",
            "role": "Developer",
           "photo": "member2.webp"
        },
        {
            "name": "Carol Williams",
            "role": "Designer",
            "photo": "member3.jpg"
        }
    ]
    return render_template('layout/team.html', team=team_members)

if __name__ == "__main__":
    app.run(debug=True)
