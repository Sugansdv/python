#  6. ATM Withdrawal Limit System
# Objective: Simulate withdrawal up to ₹10,000 per day.

# Initial total withdrawal
total_withdrawn = 0
limit = 10000

# • Use while loop to allow multiple transactions.
while total_withdrawn < limit:
    user_input = input("Enter amount to withdraw or type 'stop': ").strip()

    # • Stop when total withdrawal reaches 10,000 or user types “stop”.
    if user_input.lower() == "stop":
        print(" Transaction stopped by user.")
        break

    try:
        amount = int(user_input)

        if amount <= 0:
            print(" Invalid amount. Must be positive.")
            # • Use break to exit early on error or stop request.
            break

        if total_withdrawn + amount > limit:
            print(f" Cannot withdraw ₹{amount}. Daily limit ₹10,000 exceeded.")
            break

        total_withdrawn += amount
        print(f" ₹{amount} withdrawn. Total withdrawn: ₹{total_withdrawn}")

    except ValueError:
        print(" Invalid input. Please enter a number or 'stop'.")
        break
else:
    print(" Daily withdrawal limit of ₹10,000 reached.")
