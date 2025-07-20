import os
from modules.scanner import scan_directory
from modules.mover import move_files

def main():
    print("File Organizer Utility")
    path = input("Enter the directory path to organize: ").strip()

    if not os.path.isdir(path):
        print(" Invalid directory.")
        return

    file_map = scan_directory(path)
    move_files(path, file_map)

if __name__ == "__main__":
    main()
