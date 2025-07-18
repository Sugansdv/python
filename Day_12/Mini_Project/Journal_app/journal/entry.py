import os
from datetime import datetime

JOURNAL_DIR = "journal_data"

def ensure_dir():
    os.makedirs(JOURNAL_DIR, exist_ok=True)

def add_entry(text):
    ensure_dir()
    today = datetime.now().strftime("%Y-%m-%d")
    filename = os.path.join(JOURNAL_DIR, f"{today}.txt")
    timestamp = datetime.now().strftime("[%H:%M]")
    
    with open(filename, "a", encoding="utf-8") as f:
        f.write(f"{timestamp} {text.strip()}\n")

    print(f" Entry added to {filename}")
