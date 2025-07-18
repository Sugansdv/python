from .config import DEFAULT_CONFIG

def capitalize_text(text):
    return text.capitalize()

def word_count(text):
    return len(text.split())

def find_keywords(text, keyword):
    return keyword in text
