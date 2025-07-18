from gradesystem.grade import calculate_cgpa, get_grade

def test_cgpa():
    assert calculate_cgpa([8, 9, 7]) == 8.0

def test_grades():
    assert get_grade(9.2) == 'A+'
    assert get_grade(7.5) == 'B'
    assert get_grade(4.9) == 'F'
