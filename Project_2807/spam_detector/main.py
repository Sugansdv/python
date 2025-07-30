from spam.classifier import SpamClassifier

# Initialize and load model
classifier = SpamClassifier()

try:
    classifier.load()
except:
    classifier.train("data/spam.csv")
    classifier.load()

# Example predictions
test_messages = [
    "Hey, are we meeting today?",
    "Congratulations! You've won a free ticket!",
    "Don't miss this limited-time offer!",
    "Let’s grab lunch tomorrow."
]

print("\n--- Predictions ---")
for msg, label in zip(test_messages, classifier.predict(test_messages)):
    print(f"{msg} ➜ {label}")
