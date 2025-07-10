# 10. Personal Diary Entry Tool

# • Main function accepts entry
def diary_entry(text):
    # • Inner function saves or prints entry
    def print_entry():
        print("\n Your Diary Entry:")
        print(text)

    print_entry()

    # • Return length of entry and word count
    length = len(text)
    word_count = len(text.split())
    return length, word_count

entry = "Today I learned about inner functions and how they work in Python."
length, words = diary_entry(entry)
print(f"\nLength: {length} characters | Word Count: {words} words")
