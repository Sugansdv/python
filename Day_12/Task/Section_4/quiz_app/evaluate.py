def evaluate_answers(questions, responses):
    score = 0
    for q, user_ans in zip(questions, responses):
        if user_ans.strip().lower() == q["answer"].strip().lower():
            score += 1
    return score
