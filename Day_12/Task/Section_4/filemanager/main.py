# Create test.txt 
with open("test.txt", "w") as f:
    f.write("This is a test file.\n")

from copier import copy_file
from mover import move_file
from deleter import delete_file

# File operations
copy_file("test.txt", "copy_test.txt")
move_file("copy_test.txt", "moved_test.txt")
delete_file("moved_test.txt")

print("All file operations completed.")
