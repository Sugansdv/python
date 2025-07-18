
from poll_utils import cast_vote, show_results

def main():
    print("=== Online Polling System ===")
    while True:
        print("\n1. Cast Vote\n2. View Results\n3. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter your name: ")
            id_num = input("Enter your voter ID number: ")
            voter_id = (name.strip().lower(), id_num.strip())
            candidate = input("Enter candidate name: ")
            print(cast_vote(voter_id, candidate.strip().title()))
        elif choice == '2':
            print(show_results())
        elif choice == '3':
            print("Thank you for using the Polling System.")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
