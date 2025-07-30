import string

strength_thresholds = {
    "Weak": 0,
    "Medium": 3,
    "Strong": 5
}

def evaluate_strength(password):
    score = 0
    if len(password) >= 8:
        score += 1
    if any(c.islower() for c in password):
        score += 1
    if any(c.isupper() for c in password):
        score += 1
    if any(c.isdigit() for c in password):
        score += 1
    if any(c in string.punctuation for c in password):
        score += 1

    if score >= strength_thresholds["Strong"]:
        return "Strong"
    elif score >= strength_thresholds["Medium"]:
        return "Medium"
    else:
        return "Weak"
