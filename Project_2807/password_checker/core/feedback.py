import string

def missing_criteria_generator(password):
    if len(password) < 8:
        yield "Use at least 8 characters"
    if not any(c.islower() for c in password):
        yield "Add a lowercase letter"
    if not any(c.isupper() for c in password):
        yield "Add an uppercase letter"
    if not any(c.isdigit() for c in password):
        yield "Add a digit"
    if not any(c in string.punctuation for c in password):
        yield "Add a special character (e.g., !@#$%)"
