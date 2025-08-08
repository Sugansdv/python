from flask import Flask, request, redirect, url_for

app = Flask(__name__)

guests = []

@app.route('/rsvp')
def rsvp_form():
    return '''
        <form method="POST" action="/rsvp-confirm">
          Name: <input name="name"><br>
          Email: <input name="email"><br>
          Attending: 
          <select name="attending">
            <option value="yes">Yes</option>
            <option value="no">No</option>
          </select><br>
          <input type="submit" value="RSVP">
        </form>
    '''

@app.route('/rsvp-confirm', methods=['POST'])
def rsvp_confirm():
    name = request.form['name']
    email = request.form['email']
    attending = request.form['attending']
    guests.append({'name': name, 'email': email, 'attending': attending})
    return redirect(url_for('thank_you', name=name))

@app.route('/thank-you/<name>')
def thank_you(name):
    return f"Thank you, {name}, for your response!"

@app.route('/guests')
def guests_list():
    attending_filter = request.args.get('attending')
    if attending_filter:
        filtered = [g for g in guests if g['attending'] == attending_filter]
    else:
        filtered = guests
    return '<br>'.join(f"{g['name']} ({g['email']}) - Attending: {g['attending']}" for g in filtered)

if __name__ == '__main__':
    app.run(debug=True)
