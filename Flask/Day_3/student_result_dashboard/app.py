from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('layout/home.html')

@app.route('/result')
def result():
    student = {
        "name": "Sugan",
        "grade": "A",
        "subjects": {
            "Math": 95,
            "English": 88,
            "Science": 92,
            "History": 85
        }
    }
    return render_template('layout/result.html', student=student)

if __name__ == '__main__':
    app.run(debug=True)
