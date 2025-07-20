import os

def scan_directory(path):
    file_map = {}
    for file in os.listdir(path):
        full_path = os.path.join(path, file)
        if os.path.isfile(full_path):
            ext = os.path.splitext(file)[1][1:].lower()
            if ext == "":
                ext = "no_extension"
            file_map.setdefault(ext, []).append(file)
    return file_map
