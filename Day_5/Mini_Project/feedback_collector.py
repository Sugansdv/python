#  16. Feedback Collector
# Objective: Accept feedbacks until user types “exit”.

feedback_list = []

# • Use while loop.
while True:
    feedback = input(" Enter your feedback (type 'exit' to finish): ").strip()

    # • Use break when “exit” is typed.
    if feedback.lower() == "exit":
        print(" Feedback collection ended.")
        break

    # • Use continue if feedback is under 3 characters.
    if len(feedback) < 3:
        print(" Feedback too short. Minimum 3 characters.")
        continue

    feedback_list.append(feedback)
    print(" Feedback saved!")

# Display all collected feedbacks
print("\n All Feedbacks Received:")
for i, f in enumerate(feedback_list, start=1):
    print(f"{i}. {f}")
