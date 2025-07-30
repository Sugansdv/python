import os
from editor.utils import autosave

class FileHandler:
    def __init__(self):
        self.recent_files = []

    def read_file(self, path):
        if not os.access(path, os.R_OK):
            raise PermissionError("Cannot read file.")
        with open(path, 'r', encoding='utf-8') as file:
            content = file.read()
        self._add_to_recent(path)
        return content

    @autosave
    def write_file(self, path, content):
        if not os.access(os.path.dirname(path) or ".", os.W_OK):
            raise PermissionError("Cannot write to file.")
        with open(path, 'w', encoding='utf-8') as file:
            file.write(content)
        self._add_to_recent(path)

    def _add_to_recent(self, path):
        if path not in self.recent_files:
            self.recent_files.insert(0, path)
        if len(self.recent_files) > 5:
            self.recent_files = self.recent_files[:5]

    def get_recent_files(self):
        return self.recent_files
