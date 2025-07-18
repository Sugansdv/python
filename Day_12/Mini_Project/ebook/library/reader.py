import os
from .config import EBOOK_DIR

def read_book(book_name):
    file_path = os.path.join(EBOOK_DIR, book_name)
    if not os.path.exists(file_path):
        print(" Book not found.")
        return
    with open(file_path, 'r', encoding='utf-8') as f:
        print("\n--- Content Start ---\n")
        print(f.read(1000))  # Read first 1000 chars
        print("\n--- Content End ---\n")
