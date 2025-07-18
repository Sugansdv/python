
from exam_creator import add_question, get_question, get_all_questions, get_topics

def main():
    while True:
        print("\n--- Online Exam Creator ---")
        print("1. Add Question")
        print("2. View Question by ID")
        print("3. View All Questions")
        print("4. View All Topics")
        print("5. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == '1':
            qid = input("Enter unique question ID (e.g., Q001): ").strip()
            question = input("Enter the question text: ").strip()
            options = []
            print("Enter 4 options:")
            for i in range(4):
                options.append(input(f"Option {i + 1}: "))
            answer = input("Enter correct answer: ").strip()
            topic = input("Enter topic name: ").strip()
            add_question(qid, question, options, answer, topic)

        elif choice == '2':
            qid = input("Enter question ID: ").strip()
            print("Question Info:", get_question(qid))

        elif choice == '3':
            questions = get_all_questions()
            for qid, data in questions.items():
                print(f"\nID: {qid[0]}")
                print("Question:", data["question"])
                for i, opt in enumerate(data["options"]):
                    print(f"  {chr(65+i)}. {opt}")
                print("Answer:", data["answer"])
                print("Topic:", data["topic"])

        elif choice == '4':
            print("Available Topics:", get_topics())

        elif choice == '5':
            print("Exiting Exam Creator.")
            break

        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
