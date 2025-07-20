from modules.voting import vote
from modules.tally import show_results

candidates = set()
voters = set()
votes = {}

def main():
    print(" Simple Voting System")
    
    while True:
        print("\nMenu:")
        print("1. Add Candidate")
        print("2. Vote")
        print("3. Show Results")
        print("4. Exit")
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            name = input("Enter candidate name: ").strip()
            if name:
                candidates.add(name)
                if name not in votes:
                    votes[name] = 0
                print(f"✅ {name} added.")
        elif choice == "2":
            voter = input("Enter your name: ").strip()
            if voter in voters:
                print("❌ You have already voted.")
            else:
                vote(voter, candidates, voters, votes)
        elif choice == "3":
            show_results(votes)
        elif choice == "4":
            print("Exiting Voting System.")
            break
        else:
            print("Invalid option.")

if __name__ == "__main__":
    main()
