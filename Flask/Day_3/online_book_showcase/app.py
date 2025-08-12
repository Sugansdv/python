from flask import Flask, render_template

app = Flask(__name__)

books_data = [
    {"name": "The Alchemist", "author": "Paulo Coelho", "cover": "book1.webp"},
    {"name": "1984", "author": "George Orwell", "cover": "book2.webp"},
    {"name": "To Kill a Mockingbird", "author": "Harper Lee", "cover": "book3.jpg"},
]

@app.route("/")
def home():
    return render_template("layout/home.html")

@app.route("/books")
def books():
    return render_template("layout/books.html", books=books_data)

if __name__ == "__main__":
    app.run(debug=True)
