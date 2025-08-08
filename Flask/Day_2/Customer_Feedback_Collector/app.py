from flask import Flask, request, redirect

app = Flask(__name__)
feedbacks = []

@app.route('/feedback-form')
def form():
    return '''
    <form method="POST" action="/submit-feedback">
        Name:<input name="name"><br>
        Email:<input name="email"><br>
        Message:<textarea name="message"></textarea><br>
        <button>Send</button>
    </form>
    '''

@app.route('/submit-feedback', methods=['POST'])
def submit():
    feedbacks.append(dict(request.form))
    return redirect('/thank-you')

@app.route('/thank-you')
def thank():
    return "Thank you!"

@app.route('/feedbacks')
def list_feedback():
    user = request.args.get('user')
    data = [f for f in feedbacks if not user or f['name'] == user]
    return str(data)

@app.route('/user/<username>')
def user_page(username):
    return str([f for f in feedbacks if f['name'] == username])

if __name__ == '__main__':
    app.run(debug=True)
