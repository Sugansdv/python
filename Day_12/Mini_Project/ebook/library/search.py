import re
from .config import EBOOK_DIR
import os

def search_books(keyword):
    results = []
    for file in os.listdir(EBOOK_DIR):
        if file.endswith('.txt'):
            file_path = os.path.join(EBOOK_DIR, file)
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
                if re.search(keyword, content, re.IGNORECASE):
                    results.append(file)
    return results
