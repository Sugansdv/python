import os
import shutil

def move_files(path, file_map):
    for ext, files in file_map.items():
        folder_name = f"{ext}_files"
        folder_path = os.path.join(path, folder_name)
        os.makedirs(folder_path, exist_ok=True)

        for file in files:
            src = os.path.join(path, file)
            dst = os.path.join(folder_path, file)
            shutil.move(src, dst)
            print(f"Moved: {file} -> {folder_name}")
    print("✅ Files organized by type.")
