# 24. Feedback Collector with Sentiment Count
# Concepts: strings, list, functions.
# • Collect feedback.
# • Count how many are "good", "bad", "average".
# • Use in, lower(), etc.

feedback_list = []

def collect_feedback():
    fb = input("Enter your feedback: ")
    feedback_list.append(fb)

def analyze_feedback():
    good = bad = average = 0
    for fb in feedback_list:
        fb_lower = fb.lower()
        if "good" in fb_lower:
            good += 1
        elif "bad" in fb_lower:
            bad += 1
        elif "average" in fb_lower:
            average += 1
    print("\n--- Sentiment Summary ---")
    print(f"Good: {good}")
    print(f"Bad: {bad}")
    print(f"Average: {average}")
    print()

while True:
    print("1. Add Feedback")
    print("2. Show Sentiment Count")
    print("3. Exit")
    choice = input("Choose an option: ")

    if choice == "1":
        collect_feedback()
    elif choice == "2":
        analyze_feedback()
    elif choice == "3":
        break
    else:
        print("Invalid choice.\n")
