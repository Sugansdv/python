class Question:
    def __init__(self, text, options, answer):
        self.text = text
        self.options = options
        self.answer = answer

    def is_correct(self, guess):
        return self.answer == guess


class Quiz:
    def __init__(self):
        self.questions = []
        self.score = 0

    def add_question(self, question):
        self.questions.append(question)

    def start(self):
        for i, q in enumerate(self.questions, 1):
            print(f"Q{i}: {q.text}")
            for opt in q.options:
                print(f"- {opt}")
            guess = input("Your answer: ")
            if q.is_correct(guess):
                self.score += 1
                print("Correct!\n")
            else:
                print(f"Wrong! Correct answer: {q.answer}\n")
        print(f"Quiz Completed! Your score: {self.score}/{len(self.questions)}")

# Example
quiz = Quiz()
quiz.add_question(Question("Capital of France?", ["Paris", "Rome", "Berlin"], "Paris"))
quiz.add_question(Question("2 + 2 = ?", ["3", "4", "5"], "4"))
# quiz.start()  # Uncomment to run
