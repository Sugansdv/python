# 6. Customer Feedback Analyzer
# Description: Categorize customer feedback into positive and negative.
# Requirements:
# - Structure: {customer_id: {"feedback": ..., "rating": ...}}
# - Use .values() to compute average rating
# - Count number of each feedback type using a summary dictionary
# - Use comprehension to extract customers with rating > 4

feedback_data = {
    201: {"feedback": "positive", "rating": 5},
    202: {"feedback": "negative", "rating": 2},
    203: {"feedback": "positive", "rating": 4},
    204: {"feedback": "neutral", "rating": 3},
    205: {"feedback": "positive", "rating": 5}
}

def compute_average_rating():
    total = sum(entry["rating"] for entry in feedback_data.values())
    count = len(feedback_data)
    average = total / count if count > 0 else 0
    print(f"\nAverage Rating: {average:.2f}")

def summarize_feedback():
    summary = {}
    for entry in feedback_data.values():
        f_type = entry["feedback"]
        summary[f_type] = summary.get(f_type, 0) + 1
    print("\nFeedback Summary:")
    for feedback_type, count in summary.items():
        print(f"{feedback_type.capitalize()}: {count}")

def high_rating_customers(threshold=4):
    high_raters = {cid: data for cid, data in feedback_data.items() if data["rating"] > threshold}
    print(f"\nCustomers with rating > {threshold}:")
    for cid, entry in high_raters.items():
        print(f"Customer {cid}: Rating = {entry['rating']} ({entry['feedback']})")

compute_average_rating()
summarize_feedback()
high_rating_customers()
