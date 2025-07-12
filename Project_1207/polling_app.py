# 14. Dynamic Polling App
# Concepts: list, functions, strings, while.
# • Ask user a poll question.
# • Record options and votes.
# • Show results dynamically.
# • Allow multiple users.

poll_question = input("Enter your poll question: ")
options = []
votes = []

def setup_options():
    count = int(input("How many options? "))
    for i in range(count):
        option = input(f"Enter option {i + 1}: ")
        options.append(option)
        votes.append(0)

def cast_vote():
    print(f"\n{poll_question}")
    for i, option in enumerate(options, start=1):
        print(f"{i}. {option}")
    choice = input("Enter your choice (number): ")
    if choice.isdigit():
        idx = int(choice) - 1
        if 0 <= idx < len(votes):
            votes[idx] += 1
            print("Vote recorded.\n")
        else:
            print("Invalid option number.\n")
    else:
        print("Invalid input.\n")

def show_results():
    print("\n--- Poll Results ---")
    total = sum(votes)
    for i, option in enumerate(options):
        percent = (votes[i] / total * 100) if total > 0 else 0
        print(f"{option}: {votes[i]} vote(s) - {percent:.1f}%")

setup_options()

while True:
    cast_vote()
    again = input("Another user? (yes/no): ").strip().lower()
    if again != "yes":
        break

show_results()
