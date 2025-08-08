from flask import Flask, request, redirect

app = Flask(__name__)

applications = []

@app.route('/apply')
def apply():
    return '''
        <form method="POST" action="/submit-application">
          Name: <input name="name"><br>
          Email: <input name="email"><br>
          Position: <input name="position"><br>
          <input type="submit" value="Apply">
        </form>
    '''

@app.route('/submit-application', methods=['POST'])
def submit_application():
    applications.append({
        'name': request.form['name'],
        'email': request.form['email'],
        'position': request.form['position']
    })
    return redirect('/application-status')

@app.route('/application-status')
def application_status():
    return 'Application received!'

@app.route('/applications')
def applications_list():
    pos = request.args.get('position')
    filtered = [a for a in applications if not pos or a['position'].lower() == pos.lower()]
    return '<br>'.join(f"{a['name']} - {a['position']}" for a in filtered)

@app.route('/applicant/<name>')
def applicant(name):
    for a in applications:
        if a['name'].lower() == name.lower():
            return f"Name: {a['name']}<br>Email: {a['email']}<br>Position: {a['position']}"
    return 'Applicant not found.'

if __name__ == '__main__':
    app.run(debug=True)
