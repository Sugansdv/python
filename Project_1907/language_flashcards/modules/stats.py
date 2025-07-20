def show_stats(results):
    total = results["correct"] + results["incorrect"]
    if total == 0:
        print("No quiz attempts yet.")
        return
    print(f"Total attempts: {total}")
    print(f"Correct: {results['correct']}")
    print(f"Incorrect: {results['incorrect']}")
    accuracy = (results["correct"] / total) * 100
    print(f"Accuracy: {accuracy:.2f}%")
