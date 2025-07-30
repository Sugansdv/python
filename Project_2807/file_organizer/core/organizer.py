import os
import shutil
from core.decorators import dry_run_decorator

# Extension-to-folder mapping
EXTENSION_MAP = {
    "jpg": "Images", "jpeg": "Images", "png": "Images", "gif": "Images",
    "mp4": "Videos", "mov": "Videos",
    "pdf": "Documents", "docx": "Documents", "txt": "Documents",
    "mp3": "Audio",
    "zip": "Archives", "rar": "Archives"
}

@dry_run_decorator
def organize(directory):
    if not os.path.isdir(directory):
        raise ValueError(f"{directory} is not a valid directory.")

    for filename in os.listdir(directory):
        path = os.path.join(directory, filename)

        if os.path.isfile(path):
            ext = filename.split(".")[-1].lower()
            folder = EXTENSION_MAP.get(ext, "Others")
            target_folder = os.path.join(directory, folder)
            os.makedirs(target_folder, exist_ok=True)

            new_path = os.path.join(target_folder, filename)

            try:
                yield f"Moving: {filename} → {folder}"
                shutil.move(path, new_path)
            except PermissionError:
                yield f"Permission denied: {filename}"
