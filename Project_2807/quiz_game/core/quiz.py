import json
from pathlib import Path

class Question:
    def __init__(self, text, options, answer):
        self.text = text
        self.options = options
        self.answer = answer

    def display(self):
        print(f"\n {self.text}")
        for idx, opt in enumerate(self.options, start=1):
            print(f"{idx}. {opt}")

    def is_correct(self, user_choice):
        return self.options[user_choice - 1].lower() == self.answer.lower()

class Quiz:
    def __init__(self, question_file):
        self.questions = self.load_questions(question_file)
        self.score = 0

    def load_questions(self, filepath):
        path = Path(filepath)
        if not path.exists():
            raise FileNotFoundError("Questions file not found.")
        with open(filepath, "r") as f:
            data = json.load(f)
            return [Question(q["question"], q["options"], q["answer"]) for q in data]

    def question_generator(self):
        for q in self.questions:
            yield q

    def start(self):
        print("\n Welcome to the Quiz Game!")
        for question in self.question_generator():
            question.display()
            try:
                choice = int(input("Enter your choice (1-4): "))
                if choice < 1 or choice > 4:
                    raise ValueError("Invalid option.")
                if question.is_correct(choice):
                    print(" Correct!")
                    self.score += 1
                else:
                    print(f" Wrong! Answer: {question.answer}")
            except ValueError as ve:
                print(f" {ve}")
        print(f"\n Your final score: {self.score}/{len(self.questions)}")
