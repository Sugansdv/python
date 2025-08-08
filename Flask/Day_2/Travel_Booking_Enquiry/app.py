from flask import Flask, request, redirect

app = Flask(__name__)

bookings = []

@app.route('/booking')
def booking_form():
    return '''
        <h2>Travel Booking Enquiry</h2>
        <form method="POST" action="/booking">
          Name: <input name="name"><br>
          Destination: <input name="destination"><br>
          Travel Date: <input type="date" name="travel_date"><br>
          <input type="submit" value="Submit">
        </form>
    '''

@app.route('/booking', methods=['POST'])
def booking_submit():
    name = request.form['name']
    destination = request.form['destination']
    travel_date = request.form['travel_date']

    bookings.append({
        'name': name,
        'destination': destination,
        'travel_date': travel_date
    })

    return redirect(f'/booking/confirm/{name}')

@app.route('/booking/confirm/<name>')
def booking_confirm(name):
    return f'Thank you, {name}, for your booking enquiry!'

@app.route('/deals')
def deals():
    destination = request.args.get('destination')
    filtered = [b for b in bookings if b['destination'].lower() == destination.lower()] if destination else bookings

    response = ''
    for b in filtered:
        response += f"{b['name']} booked {b['destination']} on {b['travel_date']}<br>"
    return response if response else 'No deals found.'

if __name__ == '__main__':
    app.run(debug=True)
