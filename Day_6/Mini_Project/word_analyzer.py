#  3. Word Analyzer Tool

# • Accept multiple words
def analyze_words(*args):
    print("Original words:", args)

    # • Print word lengths using map()
    lengths = list(map(len, args))
    print("Word lengths:", lengths)

    # • Use lambda to convert words to uppercase
    uppercased = list(map(lambda word: word.upper(), args))
    print("Uppercase words:", uppercased)

    # • Return most frequent character in each word
    def most_frequent_char(word):
        freq = {}
        for char in word:
            freq[char] = freq.get(char, 0) + 1
        return max(freq, key=freq.get)

    print("Most frequent characters:")
    for word in args:
        print(f"{word}: '{most_frequent_char(word)}'")

analyze_words("banana", "apple", "strawberry")
