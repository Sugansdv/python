from modules.poll_ops import create_poll, vote_poll, display_results
from modules.user_ops import has_voted, mark_voted

polls = {}
voted_users = set()

def main():
    while True:
        print("\n Online Polling System")
        print("1. Create Poll")
        print("2. Vote on Poll")
        print("3. Show Results")
        print("4. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            create_poll(polls)
        elif choice == "2":
            user = input("Enter your username: ").strip()
            if has_voted(user, voted_users):
                print(" You have already voted.")
            else:
                voted = vote_poll(polls)
                if voted:
                    mark_voted(user, voted_users)
        elif choice == "3":
            display_results(polls)
        elif choice == "4":
            print(" Exiting Polling System.")
            break
        else:
            print(" Invalid option.")

if __name__ == "__main__":
    main()
