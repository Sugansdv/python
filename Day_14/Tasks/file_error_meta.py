import os
import glob
import shutil
from datetime import datetime

# 21. Handle FileNotFoundError
def safe_file_read(filename):
    try:
        with open(filename, "r") as file:
            print("21. File content:\n", file.read())
    except FileNotFoundError:
        print(f"21. Error: '{filename}' not found!")

# 22. Display file size and last modified date
def file_info(filename):
    if os.path.exists(filename):
        size = os.path.getsize(filename)
        modified_time = os.path.getmtime(filename)
        print(f"22. File: {filename}")
        print("    Size:", size, "bytes")
        print("    Last modified:", datetime.fromtimestamp(modified_time))
    else:
        print("22. File does not exist.")

# 23. Check if file exists and has write permission
def check_permissions(filename):
    if os.path.exists(filename):
        print(f"23. '{filename}' exists.")
        if os.access(filename, os.W_OK):
            print("    File is writable.")
        else:
            print("    File is not writable.")
    else:
        print(f"23. '{filename}' does not exist.")

# 24. try-except-finally for file closing
def safe_read_with_finally(filename):
    file = None
    try:
        file = open(filename, "r")
        print("24. Content:\n", file.read())
    except Exception as e:
        print("24. Error:", e)
    finally:
        if file:
            file.close()
            print("24. File closed in finally block.")

# 25. Check file extensions in folder
def print_file_extensions(folder):
    print("25. File extensions in folder:")
    for file in os.listdir(folder):
        if os.path.isfile(os.path.join(folder, file)):
            _, ext = os.path.splitext(file)
            print(f"    {file}: {ext}")

# 26. Display all .txt files in directory
def list_txt_files(directory):
    print("26. .txt files:")
    txt_files = glob.glob(os.path.join(directory, "*.txt"))
    for file in txt_files:
        print(f"    {file}")

# 27. Rename a file and handle name collision
def rename_file(old_name, new_name):
    try:
        if os.path.exists(new_name):
            raise FileExistsError(f"'{new_name}' already exists.")
        os.rename(old_name, new_name)
        print(f"27. Renamed '{old_name}' → '{new_name}'")
    except FileNotFoundError:
        print(f"27. Error: '{old_name}' not found.")
    except FileExistsError as e:
        print(f"27. Error: {e}")

# 28. Delete file with error handling
def delete_file(filename):
    try:
        os.remove(filename)
        print(f"28. Deleted '{filename}' successfully.")
    except FileNotFoundError:
        print(f"28. Error: '{filename}' not found.")
    except PermissionError:
        print(f"28. Error: No permission to delete '{filename}'.")

# 29. Create folder structure with os.makedirs
def create_folders(path):
    try:
        os.makedirs(path, exist_ok=True)
        print(f"29. Folders created: {path}")
    except Exception as e:
        print("29. Error:", e)

# 30. Move file using shutil
def move_file(src, dest_folder):
    try:
        os.makedirs(dest_folder, exist_ok=True)
        dest_path = os.path.join(dest_folder, os.path.basename(src))
        shutil.move(src, dest_path)
        print(f"30. Moved '{src}' → '{dest_path}'")
    except FileNotFoundError:
        print(f"30. Error: '{src}' not found.")
    except Exception as e:
        print("30. Error:", e)


# ------------------ Test/Demo ------------------

demo_file = "demo_file.txt"
with open(demo_file, "w") as f:
    f.write("This is a demo file.\n")

safe_file_read("nonexistent.txt")
file_info(demo_file)
check_permissions(demo_file)
safe_read_with_finally(demo_file)
print_file_extensions(".")
list_txt_files(".")
rename_file(demo_file, "renamed_demo.txt")
delete_file("renamed_demo.txt")
create_folders("reports/2025/July")
with open("temp_move.txt", "w") as f:
    f.write("To be moved.")
move_file("temp_move.txt", "reports/2025/July")
