from flask import Flask, request, redirect

app = Flask(__name__)

warranty_data = {
    'ABC123': 'Valid until 2025-12-31',
    'XYZ789': 'Expired on 2023-06-30',
    'DEF456': 'Valid until 2024-08-15'
}

@app.route('/check-warranty')
def check_warranty():
    return '''
        <h2>Check Product Warranty</h2>
        <form method="POST" action="/check-warranty">
          Product Serial: <input name="serial"><br><br>
          <input type="submit" value="Check">
        </form>
    '''

@app.route('/check-warranty', methods=['POST'])
def check_warranty_post():
    serial = request.form['serial']
    return redirect(f'/result?serial={serial}')

@app.route('/result')
def result():
    serial = request.args.get('serial')
    warranty = warranty_data.get(serial.upper(), 'No warranty information found.')
    return f'<h2>Warranty Result</h2><p>Serial: {serial}</p><p>Status: {warranty}</p>'

@app.route('/warranty/<product>')
def warranty(product):
    warranty = warranty_data.get(product.upper(), 'No warranty information found.')
    return f'<h2>Warranty Info for {product.upper()}</h2><p>{warranty}</p>'

if __name__ == '__main__':
    app.run(debug=True)
