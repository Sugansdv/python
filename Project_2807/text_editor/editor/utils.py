from functools import wraps
import datetime

def autosave(func):
    @wraps(func)
    def wrapper(self, path, content):
        backup_path = f"{path}.bak"
        try:
            with open(backup_path, 'w', encoding='utf-8') as backup:
                backup.write(content)
            print(f"[AutoSave] Backup saved at {datetime.datetime.now()}")
        except Exception as e:
            print(f"[AutoSave Failed] {e}")
        return func(self, path, content)
    return wrapper
