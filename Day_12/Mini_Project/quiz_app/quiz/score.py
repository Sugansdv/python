def display_score(name, score, total):
    print(f"\n{name}, your score is {score}/{total}.")

def save_score(name, score, total, file="quiz/scores.json"):
    import json, os

    record = {"name": name, "score": score, "total": total}
    if not os.path.exists(file):
        with open(file, 'w') as f:
            json.dump([], f)

    with open(file, 'r') as f:
        data = json.load(f)

    data.append(record)

    with open(file, 'w') as f:
        json.dump(data, f, indent=4)
