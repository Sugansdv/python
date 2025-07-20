def create_poll(polls):
    question = input("Enter the poll question: ").strip()
    options = input("Enter options (comma-separated): ").split(',')
    options = [opt.strip() for opt in options if opt.strip()]
    if question in polls:
        print("Poll already exists.")
        return
    polls[question] = {
        "options": options,
        "votes": {opt: 0 for opt in options}
    }
    print(" Poll created.")

def vote_poll(polls):
    if not polls:
        print(" No polls available.")
        return False

    for i, question in enumerate(polls, start=1):
        print(f"{i}. {question}")
    choice = input("Choose poll number: ").strip()
    
    try:
        poll_index = int(choice) - 1
        question = list(polls.keys())[poll_index]
    except (IndexError, ValueError):
        print(" Invalid choice.")
        return False

    options = polls[question]["options"]
    for i, opt in enumerate(options, start=1):
        print(f"{i}. {opt}")
    
    opt_choice = input("Select an option: ").strip()
    try:
        selected = options[int(opt_choice) - 1]
        polls[question]["votes"][selected] += 1
        print(" Vote cast.")
        return True
    except (IndexError, ValueError):
        print(" Invalid option.")
        return False

def display_results(polls):
    if not polls:
        print(" No polls to display.")
        return
    for question, data in polls.items():
        print(f"\n {question}")
        for opt, count in data["votes"].items():
            print(f" - {opt}: {count} votes")
