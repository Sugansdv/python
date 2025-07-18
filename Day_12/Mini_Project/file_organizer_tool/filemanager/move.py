import os
import shutil

def move_files(files_by_type, base_folder):
    for category, files in files_by_type.items():
        if category == 'others':
            continue

        category_folder = os.path.join(base_folder, category)
        os.makedirs(category_folder, exist_ok=True)

        for filepath in files:
            try:
                shutil.move(filepath, category_folder)
            except Exception as e:
                print(f"Error moving {filepath}: {e}")
