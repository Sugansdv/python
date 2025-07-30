from core.account import BankAccount

def main():
    user1 = BankAccount("alice")
    user2 = BankAccount("bob")

    while True:
        print("\n1. Deposit\n2. Withdraw\n3. Transfer\n4. Interest\n5. Transactions\n6. Filter\n7. Exit")
        choice = input("Choose an option: ")

        try:
            if choice == "1":
                amt = float(input("Amount to deposit: "))
                print(user1.deposit(amt))
            elif choice == "2":
                amt = float(input("Amount to withdraw: "))
                print(user1.withdraw(amt))
            elif choice == "3":
                amt = float(input("Amount to transfer to Bob: "))
                print(user1.transfer(amt, user2))
            elif choice == "4":
                print(user1.apply_interest() or "No interest applied.")
            elif choice == "5":
                user1.display_transactions()
            elif choice == "6":
                t_type = input("Enter type (deposit/withdraw/transfer): ")
                for t in user1.filter_transactions(t_type):
                    print(t)
            elif choice == "7":
                break
        except Exception as e:
            print("Error:", e)

if __name__ == "__main__":
    main()
