#13. Voting Eligibility Checker
# • Accept age
age = int(input("Enter your age: "))

# • Return whether eligible or not
def check_eligibility(age):
    if age >= 18:
        return "You are eligible to vote."
    else:
        return "You are not eligible to vote."

print(check_eligibility(age))

# • Bonus: Use lambda to check age >= 18
is_eligible = lambda a: a >= 18
print("Lambda check:", "Eligible" if is_eligible(age) else "Not Eligible")
