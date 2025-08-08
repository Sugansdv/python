from flask import Flask, request, redirect

app = Flask(__name__)

bugs = []
bug_id = 1

@app.route('/report')
def report():
    return '''
        <form method="POST" action="/submit-report">
          Title: <input name="title"><br>
          Description: <input name="description"><br>
          Priority: <input name="priority"><br>
          <input type="submit" value="Submit">
        </form>
    '''

@app.route('/submit-report', methods=['POST'])
def submit_report():
    global bug_id
    bug = {
        'id': bug_id,
        'title': request.form['title'],
        'description': request.form['description'],
        'priority': request.form['priority']
    }
    bugs.append(bug)
    bug_id += 1
    return redirect('/report-confirm')

@app.route('/report-confirm')
def report_confirm():
    return 'Bug submitted!'

@app.route('/bugs')
def bugs_list():
    priority = request.args.get('priority')
    output = ''
    for bug in bugs:
        if not priority or bug['priority'] == priority:
            output += f"Bug {bug['id']}: {bug['title']} (Priority: {bug['priority']})<br>"
    if output == '':
        return 'No bugs found.'
    return output

@app.route('/bug/<int:id>')
def bug_detail(id):
    for bug in bugs:
        if bug['id'] == id:
            return f"Bug {bug['id']}<br>Title: {bug['title']}<br>Description: {bug['description']}<br>Priority: {bug['priority']}"
    return 'Bug not found.'

if __name__ == '__main__':
    app.run(debug=True)
