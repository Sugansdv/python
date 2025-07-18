import os
import glob

def scan_files(folder):
    file_types = {
        'images': ['*.jpg', '*.png', '*.gif'],
        'documents': ['*.pdf', '*.docx', '*.txt'],
        'videos': ['*.mp4', '*.avi'],
        'archives': ['*.zip', '*.rar', '*.tar'],
        'others': ['*']
    }

    files_by_type = {key: [] for key in file_types}

    for category, patterns in file_types.items():
        for pattern in patterns:
            for filepath in glob.glob(os.path.join(folder, pattern)):
                if not any(filepath in lst for lst in files_by_type.values()):
                    files_by_type[category].append(filepath)

    return files_by_type
