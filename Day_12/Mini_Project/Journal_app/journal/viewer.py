import os
import re
import fnmatch
import textwrap
from journal.entry import JOURNAL_DIR

def view_entries(date=None):
    if date:
        pattern = f"{date}.txt"
    else:
        pattern = "*.txt"

    matched_files = fnmatch.filter(os.listdir(JOURNAL_DIR), pattern)
    if not matched_files:
        print("No entries found.")
        return

    for file in sorted(matched_files):
        print(f"\n {file[:-4]}")
        path = os.path.join(JOURNAL_DIR, file)
        with open(path, encoding="utf-8") as f:
            for line in f:
                wrapped = textwrap.fill(line.strip(), width=80)
                print(f"  {wrapped}")

def search_entries(keyword):
    regex = re.compile(keyword, re.IGNORECASE)
    found = False

    for file in sorted(os.listdir(JOURNAL_DIR)):
        if not file.endswith(".txt"):
            continue

        path = os.path.join(JOURNAL_DIR, file)
        with open(path, encoding="utf-8") as f:
            lines = f.readlines()
            matches = [line for line in lines if regex.search(line)]
            if matches:
                found = True
                print(f"\n🔎 Matches in {file}:")
                for match in matches:
                    print(f"  {textwrap.fill(match.strip(), width=80)}")

    if not found:
        print(" No matches found.")
