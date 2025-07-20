import random

def add_flashcard(flashcards, categories):
    word = input("Enter word: ").strip()
    translation = input("Enter translation: ").strip()
    category = input("Enter category: ").strip().lower()
    flashcards.append((word, translation, category))
    categories.add(category)
    print("Flashcard added.")

def review_flashcards(flashcards):
    if not flashcards:
        print("No flashcards to review.")
        return
    for i, (word, translation, category) in enumerate(flashcards, 1):
        print(f"{i}. {word} → {translation} (Category: {category})")

def delete_flashcard(flashcards):
    if not flashcards:
        print("No flashcards to delete.")
        return
    review_flashcards(flashcards)
    try:
        index = int(input("Enter flashcard number to delete: ")) - 1
        if 0 <= index < len(flashcards):
            removed = flashcards.pop(index)
            print(f"Deleted: {removed[0]} → {removed[1]}")
        else:
            print("Invalid index.")
    except ValueError:
        print("Invalid input.")

def quiz_mode(flashcards, quiz_results):
    if not flashcards:
        print("No flashcards available for quiz.")
        return
    random.shuffle(flashcards)
    for word, translation, _ in flashcards:
        answer = input(f"What is the translation of '{word}'? ").strip()
        if answer.lower() == translation.lower():
            print("Correct!")
            quiz_results["correct"] += 1
        else:
            print(f"Incorrect. The correct translation is '{translation}'.")
            quiz_results["incorrect"] += 1
