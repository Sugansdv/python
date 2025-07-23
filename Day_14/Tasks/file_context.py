import time
from datetime import datetime

# 11. Rewrite a script using 'with' to ensure file auto-closing
def write_with_context():
    with open("auto_close.txt", "w") as file:
        file.write("This file uses a context manager for safe handling.\n")

# 12. Reading and writing a binary file using 'wb' and 'rb'
def binary_rw():
    data = b"Binary data example"
    with open("binaryfile.bin", "wb") as file:
        file.write(data)
    with open("binaryfile.bin", "rb") as file:
        print("12. Binary read:", file.read())

# 13. File reader that checks if a file is readable or writable
def check_file_modes(filename):
    with open(filename, "r") as file:
        print("13. Readable:", file.readable())
        print("   Writable:", file.writable())

# 14. Function to count words, lines, and characters
def file_stats(filename):
    with open(filename, "r") as file:
        text = file.read()
        lines = text.splitlines()
        words = text.split()
        print(f"14. File Stats for {filename}:")
        print("   Lines:", len(lines))
        print("   Words:", len(words))
        print("   Characters:", len(text))

# 15. Report file for login/logout time logging
def log_user_activity(log_file, action):
    with open(log_file, "a") as file:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        file.write(f"{action} at {timestamp}\n")

# 16. Count how many times a specific word appears
def count_word(filename, target_word):
    with open(filename, "r") as file:
        text = file.read()
        count = text.lower().count(target_word.lower())
        print(f"16. '{target_word}' appears {count} times in '{filename}'.")

# 17. Replace a word in a file and save result
def replace_word(filename, old_word, new_word):
    with open(filename, "r") as file:
        content = file.read()
    new_content = content.replace(old_word, new_word)
    with open("replaced_output.txt", "w") as file:
        file.write(new_content)
    print(f"17. Replaced '{old_word}' with '{new_word}' and saved to 'replaced_output.txt'.")

# 18. Copy contents from one file to another
def copy_file(src, dest):
    with open(src, "r") as file1:
        content = file1.read()
    with open(dest, "w") as file2:
        file2.write(content)
    print(f"18. Copied from '{src}' to '{dest}'.")

# 19. Reverse contents line by line and save to new file
def reverse_lines(src, dest):
    with open(src, "r") as infile:
        lines = infile.readlines()
    with open(dest, "w") as outfile:
        for line in reversed(lines):
            outfile.write(line)
    print(f"19. Reversed lines saved to '{dest}'.")

# 20. Write and read structured data using writelines() and readlines()
def structured_data():
    lines = ["Name: Alice\n", "Age: 30\n", "Occupation: Developer\n"]
    with open("structured.txt", "w") as file:
        file.writelines(lines)
    with open("structured.txt", "r") as file:
        read_lines = file.readlines()
        print("20. Structured Read:")
        for line in read_lines:
            print("   " + line.strip())


# ------------------ Test or Demonstration Section ------------------

write_with_context()
binary_rw()
check_file_modes("auto_close.txt")
file_stats("auto_close.txt")
log_user_activity("user_report.txt", "User logged in")
time.sleep(1)  # simulate activity delay
log_user_activity("user_report.txt", "User logged out")
count_word("auto_close.txt", "file")
replace_word("auto_close.txt", "file", "document")
copy_file("auto_close.txt", "copy_of_file.txt")
reverse_lines("auto_close.txt", "reversed_lines.txt")
structured_data()
