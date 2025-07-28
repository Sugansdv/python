import os
import shutil
import time
import hashlib

def organize_by_extension(folder_path):
    if not os.path.exists(folder_path):
        print(" Folder does not exist!")
        return

    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        if os.path.isfile(file_path):
            ext = filename.split('.')[-1]
            ext_folder = os.path.join(folder_path, ext)
            if not os.path.exists(ext_folder):
                os.makedirs(ext_folder)
                print(f" Created folder: {ext}")
            shutil.move(file_path, os.path.join(ext_folder, filename))
            print(f" Moved {filename} to {ext}/")


def remove_duplicates(folder_path):
    seen_hashes = set()
    removed = 0

    for root, _, files in os.walk(folder_path):
        for filename in files:
            file_path = os.path.join(root, filename)
            try:
                with open(file_path, 'rb') as f:
                    file_hash = hashlib.md5(f.read()).hexdigest()
                if file_hash in seen_hashes:
                    os.remove(file_path)
                    print(f" Removed duplicate: {file_path}")
                    removed += 1
                else:
                    seen_hashes.add(file_hash)
            except Exception as e:
                print(f" Error: {e}")

    print(f" Removed {removed} duplicate files.")


def bulk_rename(folder_path, pattern):
    if not os.path.exists(folder_path):
        print(" Folder does not exist!")
        return

    count = 1
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        if os.path.isfile(file_path):
            ext = os.path.splitext(filename)[1]
            new_name = f"{pattern}_{count}{ext}"
            new_path = os.path.join(folder_path, new_name)
            os.rename(file_path, new_path)
            print(f" Renamed {filename} to {new_name}")
            count += 1


def show_largest_files(folder_path, top_n=5):
    file_sizes = []
    for root, _, files in os.walk(folder_path):
        for file in files:
            try:
                path = os.path.join(root, file)
                size = os.path.getsize(path)
                file_sizes.append((file, size))
            except Exception as e:
                print(f" Error reading {file}: {e}")

    file_sizes.sort(key=lambda x: x[1], reverse=True)
    print(f"\n Top {top_n} largest files:")
    for i, (file, size) in enumerate(file_sizes[:top_n], 1):
        print(f"{i}. {file} — {size / 1024:.2f} KB")


def auto_organize(folder_path, delay_seconds=60):
    print(f" Waiting for {delay_seconds} seconds...")
    time.sleep(delay_seconds)
    print(" Auto organizing...")
    organize_by_extension(folder_path)
    print(" Done.")


def main():
    print("=====  File Organizer =====")
    print("1. Organize by Extension")
    print("2. Remove Duplicate Files")
    print("3. Bulk Rename Files")
    print("4. Show Largest Files")
    print("5. Auto Organize (in 1 min)")
    print("6. Exit")

    choice = input(" Choose an option (1-6): ")

    if choice == "6":
        print(" Goodbye!")
        return

    folder = input(" Enter folder path: ").strip()

    if choice == "1":
        organize_by_extension(folder)
    elif choice == "2":
        remove_duplicates(folder)
    elif choice == "3":
        pattern = input(" Enter rename pattern: ")
        bulk_rename(folder, pattern)
    elif choice == "4":
        show_largest_files(folder)
    elif choice == "5":
        auto_organize(folder)
    else:
        print(" Invalid choice.")


if __name__ == "__main__":
    main()
