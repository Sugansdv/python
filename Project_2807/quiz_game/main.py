from core.quiz import Quiz
from utils.decorators import timer

@timer
def main():
    quiz = Quiz("data/questions.json")
    quiz.start()

if __name__ == "__main__":
    main()
