from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('layout/home.html')

@app.route('/movies')
def movies():
    movie_list = [
        {
            "title": "Inception",
            "poster": "https://m.media-amazon.com/images/I/51v5ZpFyaFL._AC_SY679_.jpg",
            "new_release": False,
            "rating": 5
        },
        {
            "title": "Dune",
            "poster": "https://m.media-amazon.com/images/I/91r4g02wB0L._AC_SY679_.jpg",
            "new_release": True,
            "rating": 4
        },
        {
            "title": "No Time To Die",
            "poster": "https://m.media-amazon.com/images/I/71aG+xDKSYL._AC_SY679_.jpg",
            "new_release": True,
            "rating": 3
        }
    ]
    return render_template('layout/movies.html', movies=movie_list)

if __name__ == "__main__":
    app.run(debug=True)
