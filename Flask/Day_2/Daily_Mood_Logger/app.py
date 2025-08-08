from flask import Flask, request, redirect

app = Flask(__name__)

logs = []

@app.route('/log-mood')
def log_mood():
    return '''
        <h2>Log Your Mood</h2>
        <form method="POST" action="/mood-result">
          Name: <input name="name"><br><br>
          Mood: <input name="mood"><br><br>
          Reason: <textarea name="reason"></textarea><br><br>
          <input type="submit" value="Submit">
        </form>
    '''

@app.route('/mood-result', methods=['POST'])
def mood_result():
    name = request.form['name']
    mood = request.form['mood']
    reason = request.form['reason']
    logs.append({'name': name, 'mood': mood, 'reason': reason})
    return redirect(f'/thank-you/{name}')

@app.route('/thank-you/<name>')
def thank_you(name):
    return f'Thank you, {name}, for logging your mood!'

@app.route('/logs')
def logs_list():
    mood_filter = request.args.get('mood')
    filtered = []
    for log in logs:
        if not mood_filter or log['mood'].lower() == mood_filter.lower():
            filtered.append(log)
    
    if not filtered:
        return 'No mood logs found.'
    
    result = '<h2>Mood Logs</h2>'
    for log in filtered:
        result += f"Name: {log['name']}, Mood: {log['mood']}, Reason: {log['reason']}<br>"
    return result

if __name__ == '__main__':
    app.run(debug=True)
