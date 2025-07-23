import os

def backup_file():
    source_file = input("Enter the source filename (with extension): ").strip()

    # Check if file exists
    if not os.path.exists(source_file):
        print("❌ Error: File does not exist.")
        return

    # Create backup file name
    filename, ext = os.path.splitext(source_file)
    backup_filename = f"{filename}_backup{ext}"

    # Check if backup already exists
    if os.path.exists(backup_filename):
        print("⚠️ Backup file already exists:", backup_filename)
        overwrite = input("Do you want to overwrite it? (y/n): ").lower()
        if overwrite != 'y':
            print("❌ Operation cancelled.")
            return

    try:
        with open(source_file, "r") as src:
            content = src.read()

        with open(backup_filename, "w") as dest:
            dest.write(content)

        print(f"✅ Backup successful! File saved as: {backup_filename}")

    except FileNotFoundError:
        print("❌ Source file not found.")
    except IOError as e:
        print(f"❌ IO Error occurred: {e}")
    except Exception as e:
        print(f"❌ Unexpected error: {e}")

if __name__ == "__main__":
    print("📁 File Backup Utility")
    backup_file()
