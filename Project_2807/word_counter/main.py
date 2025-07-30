from core.analyzer import WordAnalyzer

def main():
    filepath = "data/sample.txt"
    analyzer = WordAnalyzer(filepath)

    print("\n--- File Statistics ---")
    print(f"Total Lines: {analyzer.count_lines()}")
    print(f"Total Words: {analyzer.count_words()}")
    print(f"Total Characters: {analyzer.count_characters()}")
    print(f"Most Common Word: {analyzer.most_common_word()}")

    print("\n--- Word Generator ---")
    for word in analyzer.word_generator():
        print(word, end=" ")

if __name__ == "__main__":
    main()
