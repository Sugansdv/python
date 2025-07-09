# 18. Voting Eligibility Checker
# Objective: Take 5 people’s age and check who can vote.

count = 0
eligible_voters = 0

# • Use while loop for 5 iterations.
while count < 5:
    try:
        age = int(input(f"Enter age of person {count + 1}: "))

        # • Use pass in future logic for address validation.
        pass  

        # • Use if condition to check age ≥ 18.
        if age >= 18:
            eligible_voters += 1
            print(" Eligible to vote.")
        else:
            print(" Not eligible to vote.")

        count += 1

    except ValueError:
        print(" Please enter a valid age.")

# • Count eligible voters.
print(f"\n Total eligible voters out of 5: {eligible_voters}")
