from abc import ABC, abstractmethod

# Abstract User Class
class User(ABC):
    def __init__(self, username):
        self.username = username

    @abstractmethod
    def get_role(self):
        pass

# Admin Class
class Admin(User):
    def __init__(self, username):
        super().__init__(username)
        self.exams = []

    def get_role(self):
        return "Admin"

    def create_exam(self, title):
        exam = Exam(title)
        self.exams.append(exam)
        print(f" Exam '{title}' created.")
        return exam

# Student Class
class Student(User):
    def __init__(self, username):
        super().__init__(username)
        self.results = {}

    def get_role(self):
        return "Student"

    def take_exam(self, exam):
        print(f"\n {self.username} is taking the exam: {exam.title}")
        score = 0
        for i, question in enumerate(exam.questions, 1):
            print(f"\nQ{i}. {question.text}")
            for idx, opt in enumerate(question.options, 1):
                print(f"   {idx}. {opt}")
            try:
                ans = int(input("Your answer (1-4): "))
            except:
                ans = 0
            if question.check_answer(ans):
                score += 1
        self.results[exam.title] = score
        print(f"\n Exam Completed. Score: {score}/{len(exam.questions)}")

    def view_results(self):
        print(f"\n Results for {self.username}:")
        for exam, score in self.results.items():
            print(f"  - {exam}: {score} points")

# Exam Class
class Exam:
    def __init__(self, title):
        self.title = title
        self.questions = []

    def add_question(self, text, options, correct_index):
        q = Question(text, options, correct_index)
        self.questions.append(q)
        print(f" Question added to '{self.title}'")

# Question Class
class Question:
    def __init__(self, text, options, correct_index):
        self.text = text
        self.options = options
        self.__correct_index = correct_index  # Private

    def check_answer(self, selected_index):
        return selected_index == self.__correct_index

# Demo Usage
if __name__ == "__main__":
    admin = Admin("Admin123")
    student = Student("JohnDoe")

    # Admin creates exam and questions
    python_exam = admin.create_exam("Python Basics")
    python_exam.add_question("What is the output of 2 + 2?", ["3", "4", "5", "6"], 2)
    python_exam.add_question("Which keyword defines a function?", ["func", "define", "def", "lambda"], 3)

    # Student takes the exam
    student.take_exam(python_exam)
    student.view_results()
