
from feedback import feedback_handler as fh

def main():
    fh.add_feedback("C101", "Alice", "The service was excellent and fast.")
    fh.add_feedback("C102", "Bob", "Great product quality and helpful support.")
    fh.add_feedback("C103", "Charlie", "Delivery was quick, but packaging can improve.")

    print("\nAll Feedbacks:")
    fh.list_feedback()

    print("\nCollected Keywords:")
    fh.list_keywords()


if __name__ == "__main__":
    main()
