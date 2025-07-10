#19. Unique Word Counter
# • Accept a paragraph
def analyze_paragraph(text):
    words = text.split()

    # • Return total word count and unique word count
    total_words = len(words)
    unique_words = len(set(words))

    # • Optionally return longest word
    longest_word = max(words, key=len) if words else ""

    return total_words, unique_words, longest_word

# Input paragraph
paragraph = input("Enter a paragraph: ")

# Call function and unpack results
total, unique, longest = analyze_paragraph(paragraph)

print(f"\nTotal words: {total}")
print(f"Unique words: {unique}")
print(f"Longest word: {longest}")
