import os
import shutil
from journal.entry import JOURNAL_DIR

def export_all(destination="journal_export"):
    if not os.path.exists(JOURNAL_DIR):
        print("No journal data to export.")
        return

    os.makedirs(destination, exist_ok=True)

    for file in os.listdir(JOURNAL_DIR):
        src = os.path.join(JOURNAL_DIR, file)
        dst = os.path.join(destination, file)
        shutil.copyfile(src, dst)

    print(f" All journal entries exported to '{destination}'")
