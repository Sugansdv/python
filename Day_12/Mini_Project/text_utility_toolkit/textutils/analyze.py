import re
from collections import Counter

def word_frequency(text):
    words = re.findall(r'\b\w+\b', text.lower())
    return dict(Counter(words))

def is_palindrome(text):
    cleaned = re.sub(r'[^a-zA-Z0-9]', '', text.lower())
    return cleaned == cleaned[::-1]

def is_anagram(text1, text2):
    return sorted(re.sub(r'\W+', '', text1.lower())) == sorted(re.sub(r'\W+', '', text2.lower()))
