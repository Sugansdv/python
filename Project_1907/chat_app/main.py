from modules.user_ops import register_user
from modules.chat_ops import send_message, view_messages, delete_messages

users = set()
chat_logs = {}

def main():
    print("Welcome to Simple Chat CLI")
    
    while True:
        print("\nMenu:")
        print("1. Register User")
        print("2. Send Message")
        print("3. View Chat History")
        print("4. Delete Chat History")
        print("5. Exit")
        
        choice = input("Enter choice: ").strip()
        
        if choice == "1":
            register_user(users)
        elif choice == "2":
            send_message(users, chat_logs)
        elif choice == "3":
            view_messages(users, chat_logs)
        elif choice == "4":
            delete_messages(users, chat_logs)
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
