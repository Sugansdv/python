

feedback_data = {}  # {(customer_id, name): feedback_text}
keywords_set = set()


def add_feedback(customer_id, name, feedback_text):
    key = (customer_id, name)
    if key in feedback_data:
        print("Feedback already exists for this customer.")
        return

    feedback_data[key] = feedback_text
    extracted_keywords = extract_keywords(feedback_text)
    keywords_set.update(extracted_keywords)
    print(f"Feedback from {name} added.")


def extract_keywords(text):
    words = text.lower().replace('.', '').replace(',', '').split()
    # Remove common words (stop words)
    stop_words = {'the', 'and', 'is', 'in', 'of', 'to', 'a', 'with', 'for'}
    return {word for word in words if word not in stop_words}


def list_feedback():
    if not feedback_data:
        print("No feedback available.")
        return

    for key, text in feedback_data.items():
        print(f"Customer ID: {key[0]}, Name: {key[1]}")
        print(f"Feedback: {text}")
        print("-" * 40)


def list_keywords():
    print("Extracted Keywords:", ", ".join(sorted(keywords_set)))
