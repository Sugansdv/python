import os
import time
from datetime import datetime

LOG_DIR = "chat_logs"
SESSION_START = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
LOG_FILE = os.path.join(LOG_DIR, f"chat_{SESSION_START}.txt")

# Ensure log directory exists
os.makedirs(LOG_DIR, exist_ok=True)

def log_message(user, message):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    entry = f"[{timestamp}] {user}: {message}\n"
    with open(LOG_FILE, "a", encoding="utf-8") as file:
        file.write(entry)

def delete_log():
    if os.path.exists(LOG_FILE):
        os.remove(LOG_FILE)
        print(" Log deleted successfully.")
    else:
        print(" No log file to delete.")

def chat_session():
    print(f" Chat session started. Log file: {LOG_FILE}")
    print("Type 'exit' to end, 'delete_log' to remove log (admin only).")

    while True:
        user = input("User: ").strip()
        if user == "":
            continue
        message = input(f"{user}: ").strip()

        if message.lower() == "exit":
            print(" Chat session ended.")
            break
        elif message.lower() == "delete_log":
            admin_pwd = input(" Admin password: ")
            if admin_pwd == "admin123":
                delete_log()
            else:
                print(" Incorrect password.")
            continue

        log_message(user, message)

if __name__ == "__main__":
    chat_session()
