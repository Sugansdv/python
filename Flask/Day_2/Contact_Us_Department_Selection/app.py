from flask import Flask, request, redirect

app = Flask(__name__)

@app.route('/contact')
def contact():
    return '''
        <h2>Contact Us</h2>
        <form method="POST" action="/submit">
          Name: <input name="name"><br>
          Email: <input name="email"><br>
          Message: <textarea name="message"></textarea><br>
          Department:
          <select name="department">
            <option value="sales">Sales</option>
            <option value="support">Support</option>
            <option value="hr">HR</option>
          </select><br><br>
          <input type="submit" value="Send">
        </form>
    '''

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    email = request.form['email']
    message = request.form['message']
    department = request.form['department']
    source = request.args.get('source', 'unknown')

    print(f"Received message from {name} ({email}) for {department} department. Source: {source}")
    print(f"Message: {message}")

    return f"Thanks {name}! Your message has been sent to {department} department."

@app.route('/contact/<department>')
def contact_department(department):
    return f"You are viewing the contact page for the {department.capitalize()} department."

if __name__ == '__main__':
    app.run(debug=True)
