from flask import Flask, request, redirect

app = Flask(__name__)

votes = {'A': 0, 'B': 0, 'C': 0}
user_votes = {}

@app.route('/poll')
def poll():
    return '''
        <form method="POST" action="/vote">
          Name: <input name="name"><br>
          Vote for:
          <input type="radio" name="option" value="A">A
          <input type="radio" name="option" value="B">B
          <input type="radio" name="option" value="C">C<br>
          <input type="submit" value="Vote">
        </form>
    '''

@app.route('/vote', methods=['POST'])
def vote():
    name = request.form['name']
    option = request.form['option']
    votes[option] = votes.get(option, 0) + 1
    user_votes[name] = option
    return redirect('/result')

@app.route('/result')
def result():
    result_text = ''
    for option, count in votes.items():
        result_text += f'{option}: {count}<br>'
    return result_text

@app.route('/voter/<name>')
def voter(name):
    vote = user_votes.get(name)
    if vote:
        return f'{name} voted for {vote}'
    else:
        return f'No vote found for {name}'

if __name__ == '__main__':
    app.run(debug=True)
