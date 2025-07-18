import os
import glob
from .config import EBOOK_DIR

def list_books():
    txt_files = glob.glob(os.path.join(EBOOK_DIR, '*.txt'))
    books = [os.path.basename(book) for book in txt_files]
    return books
