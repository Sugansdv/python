import os
from collections import Counter
from core.decorators import time_execution
from utils.file_loader import load_file

class WordAnalyzer:
    def __init__(self, filepath):
        self.filepath = filepath
        self.content = load_file(filepath)

    @time_execution
    def count_words(self):
        return len(self.content.split())

    @time_execution
    def count_lines(self):
        return len(self.content.splitlines())

    @time_execution
    def count_characters(self):
        return len(self.content)

    @time_execution
    def most_common_word(self):
        words = self.content.lower().split()
        count = Counter(words)
        return count.most_common(1)[0] if count else ("None", 0)

    def word_generator(self):
        for word in self.content.split():
            yield word
