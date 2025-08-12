from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('layout/home.html')

@app.route('/menu')
def menu():
    menu_data = {
        "Starters": [
            {"name": "Bruschetta", "price": 5.99, "available": True, "image": "starter1.jpg"},
            {"name": "Stuffed Mushrooms", "price": 6.99, "available": False, "image": "starter2.webp"}
        ],
        "Mains": [
            {"name": "Grilled Salmon", "price": 15.99, "available": True, "image": "main.jpg"},
            {"name": "Steak Frites", "price": 18.99, "available": True, "image": "main2.webp"}
        ],
        "Desserts": [
            {"name": "Cheesecake", "price": 7.99, "available": True, "image": "cake1.webp"},
            {"name": "Chocolate Lava Cake", "price": 8.99, "available": False, "image": "cake2.webp"}
        ],
    }
    return render_template('layout/menu.html', menu=menu_data)

if __name__ == "__main__":
    app.run(debug=True)
