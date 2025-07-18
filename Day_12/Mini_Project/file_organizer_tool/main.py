import sys
import os
from filemanager import scan_files, move_files, generate_report

def main():
    if len(sys.argv) < 2:
        print("Usage: python main.py <target_folder>")
        return

    target_folder = sys.argv[1]
    if not os.path.isdir(target_folder):
        print("Invalid folder path.")
        return

    files = scan_files(target_folder)
    move_files(files, target_folder)
    generate_report(files)

if __name__ == "__main__":
    main()
