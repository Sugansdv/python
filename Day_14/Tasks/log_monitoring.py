import logging
import os
import time
from datetime import datetime
from logging.handlers import TimedRotatingFileHandler

# 41. Simple logger that writes logs with timestamps
def simple_logger():
    logging.basicConfig(filename="app.log", level=logging.INFO,
                        format="%(asctime)s - %(message)s", datefmt="%Y-%m-%d %H:%M:%S")
    logging.info("41. Application started.")
    logging.info("41. Simple logger initialized.")

# 42. Monitor directory for new files (mock logic using snapshots)
def monitor_directory(path="test_dir"):
    if not os.path.exists(path):
        os.makedirs(path)
    log_path = "directory_monitor.log"
    logging.basicConfig(filename=log_path, level=logging.INFO,
                        format="%(asctime)s - %(message)s")

    before = set(os.listdir(path))
    print("42. Monitoring for new files (mock: will check again after delay)...")
    time.sleep(2)  # Simulate delay
    with open(os.path.join(path, "mock_file.txt"), "w") as f:  # Mock: create file
        f.write("Mock file content.")

    after = set(os.listdir(path))
    new_files = after - before
    for file in new_files:
        logging.info(f"New file added: {file}")
    print(f"42. New files logged to {log_path}.")

# 43. Track user login activity with timestamp
def log_user_login(user="guest"):
    with open("user_login.log", "a") as f:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        f.write(f"User '{user}' logged in at {timestamp}\n")
    print("43. User login recorded.")

# 44. Record program steps to a log and allow filtering (with fix)
def filtered_logger():
    steps_log = "execution.log"
    logger = logging.getLogger("stepLogger")
    logger.setLevel(logging.DEBUG)

    # Prevent multiple handlers from being added during reruns
    if not logger.handlers:
        handler = logging.FileHandler(steps_log)
        formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
        handler.setFormatter(formatter)
        logger.addHandler(handler)

    # Log steps
    logger.info("Step 1: Starting task.")
    logger.debug("Step 2: Debugging info.")
    logger.warning("Step 3: Warning encountered.")
    logger.error("Step 4: Error occurred.")
    logger.critical("Step 5: Critical issue.")

    # Filter log entries
    if os.path.exists(steps_log):
        print("44. Showing WARNING+ entries from execution.log:")
        with open(steps_log, "r") as f:
            for line in f:
                if any(level in line for level in ["WARNING", "ERROR", "CRITICAL"]):
                    print("   " + line.strip())
    else:
        print("44. execution.log not found.")

# 45. Rotate log files daily and archive them by date
def rotating_logger():
    rotate_log = "daily.log"
    logger = logging.getLogger("rotatingLogger")
    logger.setLevel(logging.INFO)

    handler = TimedRotatingFileHandler(rotate_log, when="midnight", interval=1, backupCount=7)
    handler.suffix = "%Y-%m-%d"
    formatter = logging.Formatter("%(asctime)s - %(message)s")
    handler.setFormatter(formatter)

    if not logger.handlers:
        logger.addHandler(handler)

    logger.info("45. This log entry will be archived by date.")
    print(f"45. Rotating logger wrote to '{rotate_log}' (rotation mocked).")

# ------------------ Test / Run Section ------------------

if __name__ == "__main__":
    simple_logger()
    monitor_directory()
    log_user_login("admin")
    filtered_logger()
    rotating_logger()
