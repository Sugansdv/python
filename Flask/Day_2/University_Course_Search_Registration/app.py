from flask import Flask, request, redirect

app = Flask(__name__)

courses = [
    {'code': 'CS101', 'name': 'Intro to Computer Science', 'dept': 'CS'},
    {'code': 'CS102', 'name': 'Data Structures', 'dept': 'CS'},
    {'code': 'MATH101', 'name': 'Calculus I', 'dept': 'Math'},
    {'code': 'ENG101', 'name': 'English Literature', 'dept': 'Eng'},
]

registrations = []

@app.route('/courses')
def courses_list():
    dept = request.args.get('dept')
    filtered = []
    for c in courses:
        if not dept or c['dept'].lower() == dept.lower():
            filtered.append(c)
    
    result = '<h2>Courses</h2>'
    for c in filtered:
        result += f"{c['code']}: {c['name']} ({c['dept']})<br>"
    return result

@app.route('/register')
def register_form():
    return '''
        <h2>Register for a Course</h2>
        <form method="POST" action="/register">
          Student Name: <input name="student_name"><br>
          Course Code: <input name="course_code"><br>
          <input type="submit" value="Register">
        </form>
    '''

@app.route('/register', methods=['POST'])
def register_submit():
    student_name = request.form['student_name']
    course_code = request.form['course_code']
    registrations.append({'student': student_name, 'course': course_code})
    return redirect(f'/confirm-registration/{student_name}')

@app.route('/confirm-registration/<name>')
def confirm_registration(name):
    return f"Thank you, {name}, for registering!"

if __name__ == '__main__':
    app.run(debug=True)
