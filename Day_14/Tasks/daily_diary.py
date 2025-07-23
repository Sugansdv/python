from datetime import datetime

def save_diary():
    date_str = datetime.now().strftime("%Y-%m-%d")
    filename = f"{date_str}.txt"
    entry = input("Write your diary entry:\n")

    with open(filename, "a") as f:
        f.write(entry + "\n")
    print(f"Entry saved to {filename}")

save_diary()
