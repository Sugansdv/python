class LowCreditScoreError(Exception):
    pass

try:
    income = float(input("Enter your monthly income: "))
    assert income > 0, "Income must be positive."

    credit_score = int(input("Enter your credit score: "))

    if credit_score < 600:
        raise LowCreditScoreError("Your credit score is too low for loan eligibility.")
    
except ValueError:
    print("Please enter valid numeric input.")
except LowCreditScoreError as e:
    print(e)
except AssertionError as e:
    print(e)
else:
    print("You are eligible for a loan.")
