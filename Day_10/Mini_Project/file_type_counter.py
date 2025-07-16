# 15. File Type Counter
# Description: Count file types from a list of filenames.
# Requirements:
# - Input: List of filenames
# - Output: Dictionary of file extensions and their counts
# - Use split() and .get() to update dictionary

filenames = [
    "report.docx", "data.csv", "image.png", "notes.txt", "archive.zip",
    "presentation.pptx", "data.csv", "image.jpg", "summary.docx", "script.py"
]

file_counts = {}

for file in filenames:
    if "." in file:
        ext = file.split(".")[-1]
        file_counts[ext] = file_counts.get(ext, 0) + 1

print("File Type Counts:")
for ext, count in file_counts.items():
    print(f".{ext}: {count}")
