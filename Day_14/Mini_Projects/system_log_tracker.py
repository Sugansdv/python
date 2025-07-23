import os
from datetime import datetime

LOG_FOLDER = "logs"
MAX_ENTRIES_PER_FILE = 10

def get_log_file_path():
    """Determine the appropriate log file path with rotation."""
    today = datetime.now().strftime("%Y-%m-%d")
    base_filename = os.path.join(LOG_FOLDER, f"{today}.log")

    # Start with base file
    if not os.path.exists(base_filename):
        return base_filename

    # Check if rotation is needed
    index = 1
    while True:
        log_path = os.path.join(LOG_FOLDER, f"{today}_{index}.log")
        if not os.path.exists(log_path):
            return log_path
        with open(log_path, "r") as f:
            if len(f.readlines()) < MAX_ENTRIES_PER_FILE:
                return log_path
        index += 1

def write_log(message):
    """Write a log message with timestamp."""
    if not os.path.exists(LOG_FOLDER):
        os.makedirs(LOG_FOLDER)

    log_file = get_log_file_path()
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_entry = f"[{timestamp}] {message}\n"

    with open(log_file, "a") as f:
        f.write(log_entry)

def my_function():
    # Example function that logs its execution
    print("Running important function...")
    write_log("Function my_function was executed.")

# Example usage
if __name__ == "__main__":
    print(" Running System Log Tracker")
    for _ in range(25):
        my_function()
