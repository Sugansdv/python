from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('layout/home.html')

@app.route('/products')
def products():
    product_list = [
        {
            "name": "Wireless Headphones",
            "price": 59.99,
            "in_stock": True,
            "image": "product1.jpg"
        },
        {
            "name": "Smart Watch",
            "price": 199.99,
            "in_stock": False,
            "image": "product2.jpg"
        },
        {
            "name": "Bluetooth Speaker",
            "price": 79.99,
            "in_stock": True,
            "image": "product3.jpg"
        }
    ]
    return render_template('layout/products.html', products=product_list)

if __name__ == "__main__":
    app.run(debug=True)
