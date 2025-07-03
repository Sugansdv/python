## 12. Simple Quiz

print("========================================")
print("              Simple Quiz               ")
print("========================================")

# 1. Ask the user three simple questions
q1 = input("Which planet is known as the Red Planet? ")
q2 = input("What is 2 + 2? ")
q3 = input("What color is the sky? ")

# 2. Store answers in a list
answers = [q1, q2, q3]

# 3. Print the answers
print("\n Your Answers:")
for index, answer in enumerate(answers, start=1):
    print(f"{index}. {answer}")

# 4. Print the type of each answer
print("\n Data Types of Answers:")
for index, answer in enumerate(answers, start=1):
    print(f"Answer {index} type: {type(answer)}")
