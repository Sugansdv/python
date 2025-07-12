# 12. Palindrome Checker
# Concepts: string slicing, functions, loop.
# • User inputs a word/sentence.
# • Check if it's a palindrome using [::-1].
# • Loop for multiple checks.

def is_palindrome(text):
    cleaned = ''.join(c.lower() for c in text if c.isalnum())
    return cleaned == cleaned[::-1]

while True:
    user_input = input("Enter a word or sentence: ")
    if is_palindrome(user_input):
        print("It's a palindrome!\n")
    else:
        print("Not a palindrome.\n")
    
    again = input("Check another? (yes/no): ").strip().lower()
    if again != "yes":
        break
