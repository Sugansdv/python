import os
from pathlib import Path
from .utils import human_readable

class DirectoryAnalyzer:
    def __init__(self, root_path):
        self.root_path = Path(root_path)
        self.file_sizes = {}

    def scan(self):
        print(f"🔍 Scanning directory: {self.root_path}\n")
        for dirpath, _, filenames in os.walk(self.root_path):
            for filename in filenames:
                try:
                    full_path = Path(dirpath) / filename
                    size = full_path.stat().st_size
                    self.file_sizes[str(full_path)] = size
                except (PermissionError, FileNotFoundError) as e:
                    print(f"⚠️ Skipped: {filename} ({e})")

    def get_largest_files(self, limit=5):
        sorted_files = sorted(self.file_sizes.items(), key=lambda x: x[1], reverse=True)
        for path, size in sorted_files[:limit]:
            yield (path, size)

    @human_readable
    def total_size(self):
        return sum(self.file_sizes.values())