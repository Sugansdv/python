# 15. Typing Speed Test
# Concepts: string methods, while, lists, functions.
# • Show a sentence.
# • Record typing and compare.
# • Calculate time taken, errors.
# • Use split() and string comparison.

import time

sentence = "The quick brown fox jumps over the lazy dog"

def typing_test():
    print("\nType the following sentence:")
    print(f"\"{sentence}\"\n")
    
    input("Press Enter when you're ready...")
    start_time = time.time()
    typed = input("\nStart typing: ")
    end_time = time.time()
    
    duration = end_time - start_time
    errors = count_errors(sentence, typed)
    wpm = calculate_wpm(typed, duration)
    
    print(f"\nTime Taken: {duration:.2f} seconds")
    print(f"Errors: {errors}")
    print(f"Typing Speed: {wpm:.2f} WPM\n")

def count_errors(original, typed):
    original_words = original.split()
    typed_words = typed.split()
    errors = 0
    for o, t in zip(original_words, typed_words):
        if o != t:
            errors += 1
    errors += abs(len(original_words) - len(typed_words))
    return errors

def calculate_wpm(typed, duration):
    word_count = len(typed.split())
    minutes = duration / 60
    return word_count / minutes if minutes > 0 else 0

while True:
    typing_test()
    again = input("Try again? (yes/no): ").strip().lower()
    if again != "yes":
        break
