from collections import Counter

def analyze_text_file(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as file:
            content = file.read()

        words = content.split()
        word_count = len(words)
        char_count = len(content)

        # Count word frequencies (convert to lowercase for uniformity)
        word_freq = Counter(word.lower().strip(".,!?;:\"()") for word in words)
        most_common_word, freq = word_freq.most_common(1)[0] if word_freq else ("None", 0)

        print("\n Text File Analysis:")
        print(f"- Total Words: {word_count}")
        print(f"- Total Characters: {char_count}")
        print(f"- Most Frequent Word: '{most_common_word}' (used {freq} times)")

    except FileNotFoundError:
        print(" Error: File not found.")
    except Exception as e:
        print(f" Unexpected Error: {e}")

def main():
    print(" Text File Analyzer")
    filepath = input("Enter path to text file: ").strip()
    analyze_text_file(filepath)

if __name__ == "__main__":
    main()
