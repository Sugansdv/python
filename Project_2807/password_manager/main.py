from core.manager import PasswordManager

def main():
    key = input("Enter master key: ")
    manager = PasswordManager(key)

    if not manager.authenticated:
        return

    while True:
        print("\n--- Password Manager ---")
        print("1. Add Password")
        print("2. View All Passwords")
        print("3. Delete Password")
        print("4. Generate Strong Password")
        print("5. List Weak Passwords")
        print("6. List Compromised Passwords")
        print("7. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            site = input("Website: ")
            user = input("Username: ")
            pwd = input("Password: ")
            manager.add_password(site, user, pwd)
            print("Password added.")

        elif choice == "2":
            for p in manager.retrieve_passwords():
                print(p)

        elif choice == "3":
            site = input("Website to delete: ")
            manager.delete_password(site)
            print("Deleted.")

        elif choice == "4":
            print("Generated Password:", manager.generate_strong_password())

        elif choice == "5":
            print("Weak Passwords:")
            for p in manager.weak_passwords():
                print(p)

        elif choice == "6":
            print("Compromised Passwords:")
            for pwd in manager.compromised:
                print(pwd)

        elif choice == "7":
            print("Goodbye!")
            break

        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
